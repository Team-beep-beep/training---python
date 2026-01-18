# Exercise 1 - Getting Started with Python

---

## Part 1 – Setup

**Exercise:**

Your first task is to prepare your development environment from scratch.

- Fork the training repo to your account and clone it afterwards.
- Add me as a collaborator.
- In PyCharm, create a new project and set up a virtual environment (venv) as the Python interpreter for this project.
- Inside your project, add a `requirements.txt` file containing only the package `numpy`.
- Install the dependencies listed in `requirements.txt` inside your virtual environment.
- You can see the installed dependencies via "pip list"
- Run setup_check.py to make sure everything runs properly.
- Commit your changes with a clear and descriptive message.

*Tip*: To set up venv and install requirements
- Open the PyCharm terminal and run "python -m venv venv".
- Run "venv/Scripts/activate".
- You should see "(venv)" appear at the start of the line.
- Now you can install the requirements using "pip install -r .\requirements.txt".
- Make sure you see "Python 3.11" set up as the venv interpreter on the bottom right.

**Reflect on:**

- Why is it important to avoid using the global Python interpreter for projects?
- What advantages does a virtual environment provide when working on multiple projects?
- Which files should you track in Git, and which should be excluded? Why?
- What role does `requirements.txt` play in managing dependencies?

**Remember:**

- Do not commit your virtual environment directory to Git.
- Ensure your project runs cleanly and correctly after setup.
- Make sure your initial commit message clearly describes your changes.

---

## Part 2 – Working with numpy and pandas

**Exercise:**

Now that your environment is set, work on data manipulation:

- Load data from a file into your program.
- Use `numpy` to perform numerical calculations on this data efficiently.
- Utilize `pandas` to conduct basic data analysis and extract meaningful insights.
- Output a clear, concise result from your analysis.

**Reflect on:**

- Why does `numpy` offer better performance than using Python loops for numerical operations?
- In what situations is `pandas` the right tool to use, and when might it be less appropriate?
- How can you verify which Python packages are installed in your environment?

**Remember:**

- Use vectorized operations with `numpy` instead of loops for better efficiency.
- Write readable, well-organized code by creating small and focused functions.
- Use Git branches to separate new features or experiments from your main code.

---

## Part 3 – Adding Features: Configuration and Testing

**Exercise:**

Enhance your project with configuration management and automated testing:

- Create a configuration file in YAML or JSON format to store parameters.
- Implement a function to load and parse this configuration using tools like `hydra` or `omegaconf`.
- Write pytest tests that verify your function correctly reads and returns configuration data.

**Reflect on:**

- Why should configuration parameters not be hardcoded inside your source code?
- What distinguishes unit tests from integration tests, and why are both important?

**Remember:**

- Write deterministic tests that always produce the same result.
- Avoid including logic in your tests; tests should verify behavior, not implement it.
- Keep configuration files separate from your source code.
- Manage feature development using separate Git branches.

---
