
## 1. Push your changes to GitHub

0. Make sure you are in the project directory and your conda environment is activated:

   ```bash
   cd path/to/0-HELLO-WORLD
   conda activate elec0021
   ```

1. Check what changed:

   ```bash
   git status
   ```

2. Stage your file:

   ```bash
   git add hello.py
   ```

3. Commit with a clear message:

   ```bash
   git commit -m "Add hello world CLI program"
   ```

4. Push to GitHub:

   ```bash
   git push
   ```

> [!TIP]
> If `git push` complains about upstream, follow the suggestion it prints (usually a `--set-upstream` command).



## 2. Submission: Merge the “Feedback” Pull Request

GitHub Classroom will create a pull request called **Feedback**.

### What you must do

1. Go to your GitHub repo page.
2. Click **Pull requests**.
3. Open the PR titled **Feedback**.
4. Ensure your latest commit is present and (if applicable) checks are green.
5. Click **Merge pull request** → **Confirm merge**.

> [!WARNING]
> **Your submission is not considered complete until the “Feedback” PR is merged.**
> If you only push commits but don’t merge the PR, you may not receive marks/feedback correctly.

> [!NOTE]
> If you don’t see a “Feedback” PR, refresh the page and check again after a minute. If it still doesn’t exist, tell a TA.

