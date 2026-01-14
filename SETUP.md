
## 1. Install Git
Install **Git** by following the instructions on the [official Git website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). After installing, confirm it works by running:
```bash
git --version
```


## 2. Install VS Code

Download and install **Visual Studio Code** from the official site: [https://code.visualstudio.com/](https://code.visualstudio.com/).

### 3. Install the required VS Code extensions
Open VS Code → Go to "Extensions" in the left sidebar and install the following extensions:

* **Python** (by Microsoft)
* **Pylance** (by Microsoft)
* **Jupyter** (optional, but useful later)


## 4. Install Miniconda

Install **Miniconda** from the official site: [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html). After installing, confirm it works:

```bash
conda --version
```

If that prints a version number, you’re good.

> [!WARNING]
> If `conda` is “command not found”, your shell might not be initialised. Try:
>
> ```bash
> conda init
> ```
>
> Then **close and reopen** your terminal.


### 5. Create the environment
Create a new conda environment for this module. The environment is a self-contained Python installation with all the packages you need. You can use multiple environments for different projects without conflicts.
To create a new environment, in your terminal, run:

```bash
conda create -n elec0021 python=3.11
```
You can activate it with:

```bash
conda activate elec0021
```

You can also create an environment from a file that lists all dependencies. This is useful for sharing environments with others. This repo provides an `environment.yml` file for you. To create the environment from that file, run:

```bash
conda env create -f environment.yml -n elec0021
conda activate elec0021
```

For more information on conda environments, see the [Conda documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).