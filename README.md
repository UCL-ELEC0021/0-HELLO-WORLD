# ELEC0021 — Lab 1: Setup + “Hello, World!” + GitHub Classroom Workflow

Welcome to your first lab. Today you’ll set up a working Python development environment and learn the *exact* Git/GitHub workflow you’ll use for the rest of the module.


Your task is to build a Python program whose entry point is a `main.py` file, that prints a greeting for a certain number of times, and accepts command-line arguments, e.g.

```bash
python main.py --times 3 --uppercase
```
```
# HELLO, WORLD!
# HELLO, WORLD!
# HELLO, WORLD!
```



By the end of this lab you will be able to:

* Install and use **VS Code** as a Python IDE (including selecting the correct interpreter).
* Install **Miniconda** and create/activate an isolated **conda environment** for a project.
* Write and run a Python program from the command line, including **parsing CLI arguments**.
* Use core **Git** commands (`clone`, `status`, `add`, `commit`, `push`, `pull`) confidently.
* Submit work correctly on **GitHub Classroom** by merging the **“Feedback”** pull request.

> [!NOTE]
> We assume you can use the command line (Terminal). If you want a fun refresher, play **Bandit** (OverTheWire): [https://overthewire.org/wargames/bandit/](https://overthewire.org/wargames/bandit/)


To complete this lab, follow the instructions in the following files:
* [SETUP.md](SETUP.md) — Install Git, VS Code, Miniconda, and create the conda environment.
* [COMPLETE.md](COMPLETE.md) — Write the “Hello, World!” Python program.
* [SUBMIT.md](SUBMIT.md) — Commit, push, and submit your work on GitHub Classroom.


## Common Issues

<details>
<summary><strong>“conda: command not found”</strong></summary>

* Restart your terminal after installation.
* Try:

  ```bash
  conda init
  ```
* If you’re on macOS/Linux, check your shell (`bash` vs `zsh`) and that Miniconda is on your PATH.

</details>

<details>
<summary><strong>VS Code runs the wrong Python</strong></summary>

* Command Palette → **Python: Select Interpreter** → choose `elec0021-lab1`
* In VS Code terminal, make sure you activated:

  ```bash
  conda activate elec0021
  ```

</details>

<details>
<summary><strong>I can’t push to GitHub</strong></summary>

* You may need to authenticate (GitHub login / token).
* Confirm your remote:

  ```bash
  git remote -v
  ```
* Try pushing again:

  ```bash
  git push
  ```

</details>