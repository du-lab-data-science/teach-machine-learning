# How to set up a virtual environment on your local computer?

## 1. Clone the repository

```bash
git clone git@github.com:du-lab-data-science/teach-machine-learning.git
cd <YOUR_REPO_FOLDER>
```
## 2. Create a virtual environment

For Mac/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

For Windows:
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

## 3. Install dependencies

For Mac/Linux:
```bash
pip install -r docs/requirements.txt
```

For Windows:
```cmd
pip install -r docs\requirements.txt
```

## 4. Deactivate the virtual environment

After you are done with working on the project, you need to deactivate the virtual environment.

For Mac/Linux:
```bash
deactivate
```

For Windows:
```cmd
deactivate
```