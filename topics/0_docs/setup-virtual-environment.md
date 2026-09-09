# How to set up a virtual environment on your local computer?

## Introduction
A Python virtual environment is an isolated workspace for a specific Python project, allowing you to manage its dependencies independently.  

By default, Python installs all external libraries globally. If you work on multiple projects without virtual environments, they will all share the same global folder. This quickly leads to major issues that virtual environments are designed to solve:

- **Preventing version conflicts:** If Project A requires Django 3.2 but Project B requires Django 5.0, a global installation will force you to overwrite one for the other, breaking one of your projects. A virtual environment gives each project its own isolated sandbox with the exact library versions it needs.

- **Keeping the system clean:** Your operating system often relies on its own "system Python" installation to run background tasks. Installing, upgrading, or deleting random third-party packages globally can accidentally break critical system tools.

- **Ensuring reproducibility:** When your project is isolated, you can easily generate a list of its exact dependencies (usually in a requirements.txt file). This allows other developers or production servers to recreate your precise environment with a single command.

- **No admin/root privileges required:** Installing global packages often requires administrator permissions (sudo on Mac/Linux or admin command prompt on Windows). Virtual environments live in local folders, meaning you can install any library without needing elevated system access.

## Steps to clone this repo and set up a virtual environment for it
### 1. Clone the repository

```bash
git clone git@github.com:du-lab-data-science/teach-machine-learning.git
cd <YOUR_REPO_FOLDER>
```
### 2. Create a virtual environment

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

### 3. Install dependencies

For Mac/Linux:
```bash
pip install -r topics/0_docs/requirements.txt
```

For Windows:
```cmd
pip install -r topics\0_docs\requirements.txt
```

### 4. Deactivate the virtual environment

After you are done with working on the project, you need to deactivate the virtual environment.

For Mac/Linux:
```bash
deactivate
```

For Windows:
```cmd
deactivate
```