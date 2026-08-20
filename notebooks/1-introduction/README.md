# Lecture 2 - Setup of the Computational Environment

BINF 6210/8210: Machine Learning for Bioinformatics (Fall 2026)

## Recommended route: `venv` + `pip`

From a terminal in this folder:

### Windows PowerShell

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name binf6210 --display-name "Python 3 (BINF 6210)"
python -m jupyter lab
```

If PowerShell blocks activation, use Command Prompt and run `.venv\Scripts\activate.bat`, or follow your institution's PowerShell policy. Do not weaken security policy without institutional guidance.

### macOS or Linux

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name binf6210 --display-name "Python 3 (BINF 6210)"
python -m jupyter lab
```

If `python3.12` is unavailable, use an installed supported Python 3 version chosen for the course.

## Alternative route: Conda

```bash
conda env create -f environment.yml
conda activate binf6210
python -m ipykernel install --user --name binf6210 --display-name "Python 3 (BINF 6210)"
python -m jupyter lab
```

Use one route for this course environment; do not mix `venv` and Conda for the same environment.

## In Jupyter

Open `Lecture_02_Computational_Environment.ipynb`, select **Python 3 (BINF 6210)**, restart the kernel, and run all cells from top to bottom.

## Useful commands

```bash
python --version
python -m pip --version
python -m pip list
python -m pip show scikit-learn
python -m pip freeze > requirements-lock.txt
```

## Troubleshooting order

1. Copy the full error message.
2. Record operating system, `python --version`, `python -m pip --version`, and `sys.executable`.
3. Confirm the selected Jupyter kernel.
4. Restart the kernel after an installation.
5. Reproduce the problem in the smallest possible cell.
6. Share commands and outputs, but never passwords, tokens, protected data, or `.env` contents.
