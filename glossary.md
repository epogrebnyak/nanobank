# Glossary

- **REPL (Read-Evaluate-Print-Loop)** -- an interactive programming environment that allows a user
  to enter a command and immediately see the result. If you have Python installed a REPL starts with `python -i`. Great to try one-line code. Example: Use [pyodide console][pyodide_console] for a REPL.

- **script or module** -- text of a program save in a file. Runs with `python code.py` where
  `code.py` is a text file with your program. `hello.py` or `my_first_program.py` are equally good names for a file. _module_ is an official name for any file with Python code, while the _script_ may hint at a file content -- it is usually a short program with simple structure. Example: [repl.it](https://replit.com/) is an environment where you can run and save scripts.

  - **package** -- several modules in one folder.
  - **library** -- practically the same as package.

- **Jupyter notebook** -- REPL will not show the graphs and hard to keep track of what code did  
  already execute. Scripts need `print()` to show anything to console and run all of the program
  at once. Do students like them? Not really. Smart people in education came up with a format where code blaock are stored by cells and program ouput can be seen per each cell. Notebooks are extremely popular with data scientists who may not know any other living form of Python code. [Google Colab](https://colab.research.google.com/) is an enhanced version of a Jupyter notebook.
