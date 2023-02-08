# Where to run your Python code

## Quick answer

Pick one: [Google Colab](https://colab.research.google.com/)

Try next: [repl.it](https://replit.com/) and [pydyode console][pyodide_console]

More: Anaconda and VS Code.

## In your browser

You can try Python very quickly from:

- [Google Colab](https://colab.research.google.com/) if you prefer notebooks, or
- [repl.it](https://replit.com/) if you will run scripts and use command line.

Colab has been a fine and free service for years, while repl.it made its way from
an experimental code runner to a comprehensive remote IDE with good interface.

To make a picture complete you can also use and [in-browser REPL from pydyode][pyodide_console].
It is the same environment that you get when running `python -i` command locally.
`pydyode` is an exciting project as the code runs entirely in browser -
there is no server behind it (Colab and repl.it provision a virtual machine for you).

[pyodide_console]: https://pyodide.org/en/stable/console.html

Hint: try Colab, then repl.it.

Glossary:

- **REPL (Read-Evaluate-Print-Loop)** -- an interactive programming environment that allows a user
  to enter a command and immediately see the result. If you have Python installed a REPL starts with `python -i`. Great to try one-line code. Example: Use [pyodide console][pyodide_console] for a REPL.

- **script or module** -- text of a program save in a file. Runs with `python code.py` where
  `code.py` is a text file with your program. `hello.py` or `my_first_program.py` are equally good names for a file. _module_ is an official name for any file with Python code, while the _script_ may hint at a file content -- it is usually a short program with simple structure. Example: [repl.it](https://replit.com/) is an environment where you can run and save scripts.

  - **package** -- several modules in one folder.
  - **library** -- practically the same as package.

- **Jupyter notebook** -- REPL will not show the graphs and hard to keep track of what code did  
  already execute. Scripts need `print()` to show anything to console and run all of the program
  at once. Do students like them? Not really. Smart people in education came up with a format where code blaock are stored by cells and program ouput can be seen per each cell. Notebooks are extremely popular with data scientists who may not know any other living form of Python code. [Google Colab](https://colab.research.google.com/) is an enhanced version of a Jupyter notebook.

## Local installation

You can install Python on your computer from [Python.org](https://www.python.org/downloads/)
or from [Anaconda](https://www.anaconda.com/). Anaconda distribution is rather big, but already
contains many useful libraries, such as NumPy, SciPy, and pandas.

Discipline yourself to have just one installation of Python on your computer until
you figure how deal with many and why you might need more than one.

Hint: install Anaconda.

## Text editors

Unlike R ecosystem, where everyone codes in RStudio, there is no single text editor for Python,
but a selection of choices:

- IDLE is simple editor supplied together with Python installation
- Visual Studio Code (VS Code) is extremely popular and has a good Python extension
- PyCharm is very intelligent, but probably too heavy for simple code
- some people would say Jupyter notebook or Jupyter Lab is all you need
- [Wings](https://wingware.com/) looks nice and very Pythonic
- vim and emacs are beacons of excellence, but not recommended for novice users

You can get some popularity comparisons from Stack Overflow and Jetbrains developper surveys.

I personally used Spyder a lot to write Python code and occasionally use Notepad++ and Sublime.
I was exploring Atom text editor when released (now depreciated) and gave up on emacs.

Hint: start with IDLE and switch to VS Code next.

Why not VS Code right away?

With VS Code, you can customize the editor and take advantage of different workflows to run Python code, such as running a whole script, using `% ##` cells, or using Jupyter notebooks. You can also use VS Code remotely. Customization comes at a cost of a learning curve ahead of you -- things may not work out of the box as expected and sometimes you are left wondering if you are really using the VS Code to the fullest or indeed correctly. Going up the curve is worth the investment: VS Code a prevalent editor for remote services such as Github Codespaces and Gitpod -- once you learn to use it, you can use it in many places (that even offer free resources such as a remote machine with Python installed).

## More tools

Great if you understand operating system and network basics, comfortable using command line, know what git and Gihub/Gitlab are for, write text im Markdown and gradually become familiar with Python packaging.
