

## 1. Clone the GitHub Classroom Repo

From the GitHub Classroom link you accepted, clone your repository:

```bash
git clone <YOUR_REPO_URL>
cd <YOUR_REPO_FOLDER>
```

Confirm Git is working:

```bash
git status
```

You should see something like “On branch main” (or similar).


## 2. Connect VS Code to Your Conda Environment

1. Open the repo in VS Code:

   * File → Open Folder… → select your repo
2. Select the Python interpreter:

   * Command Palette (CTRL + SHIFT + P) → **Python: Select Interpreter**
   * Choose the one that mentions `elec0021-lab1`

Verify from the VS Code terminal:

```bash
python --version
```

> [!WARNING]
> If VS Code is using the wrong interpreter, your code may run in a different Python installation than the one you configured.



## 3. Implement `main.py` (CLI Arguments)

Create a file `main.py` in the repo root.
Your script must:

* Print **Hello, World!** when run with no arguments.
* Accept a `--uppercase` argument (flag) to print the greeting in uppercase.
* Have a `--times` argument (integer, default `1`) to repeat the greeting.
* Use the standard library only (recommended: `argparse`).

Examples:

```bash
python main.py
# Hello, World!

python main.py --uppercase
# HELLO, WORLD!

python main.py --uppercase --times 3
# HELLO, WORLD!
# HELLO, WORLD!
# HELLO, WORLD!
```
