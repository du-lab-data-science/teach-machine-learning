# Instructor Guide: Lecture 2 - Setup of the Computational Environment

**Course:** BINF 6210/8210, Machine Learning for Bioinformatics  
**Class length:** 75 minutes  
**Position in course:** After ML/AI introduction and before data preprocessing  
**Format:** Short explanations, live demonstration, guided notebook lab, and exit ticket

## Learning outcomes

Students will be able to distinguish the interpreter, environment, package manager, Jupyter server, and kernel; build and validate an isolated environment; diagnose common interpreter/kernel mismatches; use portable project paths; and capture computational provenance for a small ML experiment.

## Instructor preparation

- Post this entire folder to Canvas before class.
- Ask students to install Python 3 and Git before class, but provide a browser-based fallback if local installation fails.
- Test both the Windows and macOS commands on clean machines or disposable environments.
- Decide one supported Python minor version for the semester. The provided files use Python 3.12 as a conservative course baseline.
- Do not require TensorFlow and PyTorch today; install one or both later when the deep-learning module begins.
- Keep a clean demonstration environment and a deliberately mismatched Jupyter kernel ready.

## 75-minute lesson plan

### 0-5 min - Motivation and diagnostic prompt
Ask: “It runs on my computer. What information would another researcher need?” Connect environment control to reproducibility, collaboration, grading, and deployment. Emphasize that bioinformatics analyses combine code, data, packages, system libraries, hardware, and random processes.

### 5-15 min - Mental model
Draw the five layers: operating system → Python interpreter → environment/packages → Jupyter server → kernel. Demonstrate that the terminal's activated environment and the notebook kernel can differ. Use `sys.executable` as the decisive check.

**Formative question:** If `pip list` in the terminal shows scikit-learn but `import sklearn` fails in the notebook, name two plausible causes.

### 15-28 min - Create the course environment
Demonstrate the recommended `venv` route from `README.md`; briefly show the Conda alternative without mixing the two. Explain `python -m pip`: the selected Python executes the `pip` module. Register and select the `binf6210` kernel.

**Check:** Students compare terminal `python -m pip --version` with notebook `sys.executable`.

### 28-50 min - Guided notebook lab
Students complete Sections 1-5. Pause after the package table, portable-path section, and repeated experiment. Circulate using the troubleshooting decision tree below. Pair students across operating systems if possible and have them compare paths.

### 50-60 min - Reproducibility and provenance
Discuss seed control, package versions, raw-data immutability, checksums, data-use restrictions, and why `pip freeze` is a snapshot rather than a universally portable specification. Connect these practices to later assignments and the final project.

### 60-68 min - CPU, GPU, and cloud choices
Classical models usually need only a CPU. GPU support will matter later for neural networks. Google Colab is a fallback and GPU access is not guaranteed; code and data governance still apply. Never upload restricted human-subject data to an unapproved cloud service.

### 68-73 min - Failure drill
In pairs, diagnose one scenario: wrong kernel, missing package, wrong working directory, or stale kernel after installation. Require evidence before proposing a fix.

### 73-75 min - Exit ticket
Students answer the three questions at the end of the notebook. Collect through Canvas.

## Key concepts and talking points

### Environment isolation
An environment prevents one project's dependency choices from silently changing another project. It does not virtualize the entire operating system and does not automatically preserve data, system libraries, or hardware details.

### Reproducibility levels
- **Repeatability:** same team, same setup, same result.
- **Reproducibility:** another team can obtain a consistent result using documented artifacts.
- **Robustness:** conclusions remain stable under reasonable analytical choices.

Avoid presenting exact bitwise equality as the only form of scientific reproducibility.

### Dependency strategy
`requirements.txt` lists the small direct teaching stack. A generated `requirements-lock.txt` captures one machine's fuller package state. For major projects, use a deliberate lock-file workflow and test it on a clean environment.

### Notebooks and execution order
Notebook output can reflect an execution order different from the visible cell order. Require students to restart the kernel and run all cells before submission. A notebook is not reproducible merely because its existing outputs look correct.

## Troubleshooting decision tree

1. **What failed?** Capture the full command, cell, traceback, and expected behavior.
2. **Which Python?** Compare `sys.executable`, `python --version`, and `python -m pip --version`.
3. **Which kernel?** Confirm the notebook kernel points to the intended interpreter.
4. **Is the package present there?** Run `python -m pip show PACKAGE`. Note that installation name `scikit-learn` differs from import name `sklearn`.
5. **Is the path correct?** Print `Path.cwd()` and verify file existence with `Path.exists()`.
6. **Did state become stale?** Restart the kernel and rerun from the top.
7. **Can it be minimized?** Reduce the problem to imports and the smallest failing operation.

## Common misconceptions and responses

- “Jupyter is my environment.” Jupyter is an interface/server; the kernel supplies the Python interpreter.
- “`import sys` installed packages.” Importing a standard-library module does not install packages; a different interpreter or environment was likely inspected.
- “Deactivating failed because `.venv` still appears in the prompt.” Confirm with `sys.executable` or the shell's Python path; some IDE labels are project/interpreter indicators rather than shell activation indicators.
- “`pip freeze` is all I need.” It omits data, code revision, system libraries, commands, and often hardware details.
- “A seed guarantees identical results.” Hardware kernels, parallelism, package versions, and nondeterministic operations can still differ.

## Formative assessment prompts

1. Explain why `python -m pip install numpy` is safer than an unqualified `pip install numpy`.
2. A teammate gets a different train/test split. What should you compare first?
3. Why should raw bioinformatics data usually be treated as immutable?
4. What belongs in Git, and what generally should not?
5. How would you prove which Python executed a notebook cell?

## Post-class assignment (10 points)

Submit a single HTML-exported notebook or `.ipynb` plus `environment_report.json`.

1. **Environment evidence (2):** show interpreter, OS, and versions.
2. **Package smoke test (2):** run the core imports and array/data-frame test.
3. **Portable paths (2):** construct `data` and `results` paths with `pathlib`; no absolute user-specific path.
4. **Reproducible model (2):** run the supplied experiment twice with the same seed and explain the result.
5. **Reflection (2):** answer the exit ticket accurately and concisely.

Deduct up to 2 points if the notebook cannot run from top to bottom after a kernel restart. Do not deduct for unavailable GPU hardware.

## 8210 extension (optional)

Ask doctoral students to compare a direct-dependency file, a full `pip freeze` snapshot, and a Conda environment export. They should identify platform-specific entries and propose a validation strategy using a fresh environment or continuous integration.

## Accessibility and inclusion

Provide commands as selectable text, narrate live terminal actions, avoid relying on color alone, allow the browser-based fallback for installation barriers, and ensure students never use protected data during setup exercises.

## Deliverables in this package

- `Lecture_02_Computational_Environment.ipynb`: guided, self-checking lab
- `README.md`: student setup instructions for Windows, macOS/Linux, and Conda
- `requirements.txt`: minimal direct dependencies
- `environment.yml`: Conda alternative
- `.gitignore`: safe starter exclusions
