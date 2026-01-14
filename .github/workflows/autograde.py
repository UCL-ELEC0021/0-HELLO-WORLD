#!/usr/bin/env python3
"""
ELEC0021 Lab 1 autograder.

Checks that main.py exists and that running it matches the required CLI behaviour:
- python main.py                  -> Hello, World!
- python main.py --uppercase       -> HELLO, WORLD!
- python main.py --uppercase --times 3 -> repeated 3 times

Writes:
- autograde_results.json
- autograde_summary.md

Exit code:
- 0 if all tests pass
- 1 otherwise
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import textwrap
from dataclasses import dataclass, asdict
from typing import List, Optional


@dataclass
class TestResult:
    name: str
    passed: bool
    points: int
    max_points: int
    message: str = ""
    stdout: str = ""
    stderr: str = ""
    returncode: Optional[int] = None


def _norm(s: str) -> str:
    """Normalise newlines and allow a missing final newline."""
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    # Accept either with or without a final newline
    if s.endswith("\n"):
        return s
    return s + "\n"


def _run(cmd: List[str], timeout_s: float = 3.0) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout_s,
        cwd=os.getcwd(),
    )


def _expected_lines(line: str, times: int) -> str:
    return "\n".join([line] * times) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", default="autograde_results.json", help="Path to write JSON results.")
    parser.add_argument("--summary", default="autograde_summary.md", help="Path to write Markdown summary.")
    args = parser.parse_args()

    results: List[TestResult] = []
    total = 0
    max_total = 0

    def add_result(r: TestResult) -> None:
        nonlocal total, max_total
        results.append(r)
        total += r.points
        max_total += r.max_points

    # --- Sanity checks ---
    if not os.path.exists("main.py"):
        add_result(
            TestResult(
                name="main.py exists",
                passed=False,
                points=0,
                max_points=10,
                message="main.py not found in repo root.",
            )
        )
        # Still write outputs for visibility
        return _write_outputs(args.json, args.summary, results, total, max_total, passed=False)

    add_result(
        TestResult(
            name="main.py exists",
            passed=True,
            points=10,
            max_points=10,
            message="Found main.py in repo root.",
        )
    )

    python = sys.executable

    tests = [
        {
            "name": "Default output: python main.py",
            "cmd": [python, "main.py"],
            "expected": _expected_lines("Hello, World!", 1),
            "points": 10,
        },
        {
            "name": "Uppercase flag: python main.py --uppercase",
            "cmd": [python, "main.py", "--uppercase"],
            "expected": _expected_lines("HELLO, WORLD!", 1),
            "points": 10,
        },
        {
            "name": "Uppercase + times: python main.py --uppercase --times 3",
            "cmd": [python, "main.py", "--uppercase", "--times", "3"],
            "expected": _expected_lines("HELLO, WORLD!", 3),
            "points": 10,
        },
        # A small extra: times without uppercase (still within spec)
        {
            "name": "Times only: python main.py --times 2",
            "cmd": [python, "main.py", "--times", "2"],
            "expected": _expected_lines("Hello, World!", 2),
            "points": 5,
        },
    ]

    for t in tests:
        name = t["name"]
        cmd = t["cmd"]
        expected = t["expected"]
        pts = int(t["points"])

        try:
            proc = _run(cmd)
            out = proc.stdout
            err = proc.stderr
            rc = proc.returncode

            ok = (rc == 0) and (_norm(out) == _norm(expected))

            msg = "OK" if ok else "Output did not match expected."
            if rc != 0:
                msg = f"Program exited with non-zero status {rc}."
            # We don't hard-fail on stderr alone, but we include it in the report.
            add_result(
                TestResult(
                    name=name,
                    passed=ok,
                    points=pts if ok else 0,
                    max_points=pts,
                    message=msg,
                    stdout=out,
                    stderr=err,
                    returncode=rc,
                )
            )
        except subprocess.TimeoutExpired:
            add_result(
                TestResult(
                    name=name,
                    passed=False,
                    points=0,
                    max_points=pts,
                    message=f"Timed out after running: {' '.join(cmd)}",
                )
            )

    passed_all = all(r.passed for r in results if r.max_points > 0)
    return _write_outputs(args.json, args.summary, results, total, max_total, passed=passed_all)


def _write_outputs(
    json_path: str,
    summary_path: str,
    results: List[TestResult],
    total: int,
    max_total: int,
    passed: bool,
) -> int:
    payload = {
        "passed": passed,
        "score": total,
        "max_score": max_total,
        "tests": [asdict(r) for r in results],
    }

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    # Markdown summary (for GitHub Actions Job Summary)
    lines: List[str] = []
    lines.append("# Autograding Report")
    lines.append("")
    lines.append(f"**Result:** {'✅ PASS' if passed else '❌ FAIL'}")
    lines.append(f"**Score:** {total}/{max_total}")
    lines.append("")
    lines.append("## Tests")
    lines.append("")
    lines.append("| Test | Points | Status |")
    lines.append("|---|---:|:---:|")

    for r in results:
        status = "✅" if r.passed else "❌"
        lines.append(f"| {r.name} | {r.points}/{r.max_points} | {status} |")

    # Include details only for failures
    failures = [r for r in results if not r.passed]
    if failures:
        lines.append("")
        lines.append("## Failure Details")
        for r in failures:
            lines.append("")
            lines.append(f"### {r.name}")
            if r.message:
                lines.append("")
                lines.append(f"**Reason:** {r.message}")
            if r.returncode is not None:
                lines.append(f"**Return code:** {r.returncode}")
            if r.stderr:
                lines.append("")
                lines.append("**stderr:**")
                lines.append("```")
                lines.append(r.stderr.rstrip("\n"))
                lines.append("```")
            if r.stdout:
                lines.append("")
                lines.append("**stdout:**")
                lines.append("```")
                lines.append(r.stdout.rstrip("\n"))
                lines.append("```")

        lines.append("")
        lines.append("> [!NOTE]")
        lines.append(
            textwrap.dedent(
                """\
                Output is compared exactly (case + punctuation). A missing final newline is tolerated.
                """
            ).strip()
        )

    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
