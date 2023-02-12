# Where to run your Python code

## Quick answers

- First pick: [Google Colab](https://colab.research.google.com/).
- Try next: [repl.it](https://replit.com/) and [pydyode console][pyodide_console].
- More capabilities: Anaconda and VS Code.

## In your browser

You can try Python very quickly from:

- [Google Colab](https://colab.research.google.com/) if you prefer notebooks, or
- [repl.it](https://replit.com/) if you will run scripts and use command line.

Colab has been a fine and free service offed by Google for years, 
while repl.it made its way from an experimental code runner 
to a comprehensive remote IDE with good interface.

You can also use and [in-browser REPL from pydyode][pyodide_console].
It is the same environment that you get when running `python -i` command locally.
`pydyode` is an exciting project because the code runs entirely in browser --
there is no server behind it while Colab and repl.it provision a virtual machine for you.

[pyodide_console]: https://pyodide.org/en/stable/console.html

> Hint: try Colab, then repl.it.


## Local installation

You can install Python on your computer from [Python.org](https://www.python.org/downloads/)
or from [Anaconda](https://www.anaconda.com/). Anaconda distribution is rather big in size, 
but already contains many useful libraries, such as NumPy, SciPy, and pandas.

Discipline yourself to have just one installation of Python on your computer 
until you figure how deal with several and why you might need more than one.

> Hint: install Anaconda.

## Text editors

For R programming language there is one preferred editor called RStudio, 
while for Python there is no single "best" text editor or IDE, 
but a selection of choices depending on type of work you do:

- IDLE is simple editor supplied together with Python installation
- Visual Studio Code (VS Code) is extremely popular and has a good Python extension
- PyCharm is very intelligent, but probably too heavy for simple code
- some people would say Jupyter notebook or Jupyter Lab is all you need
- [Wings](https://wingware.com/) looks nice and very Pythonic
- vim and emacs shine with excellence, but not recommended for novice users

You can get some editor and IDE popularity comparisons from Stack Overflow, Jetbrains and 
State of Octoverse developper surveys.

My personal choices are the following: 

- used Spyder a lot to write Python code (Spyder layout is similar to MATLAB and RStudio)
- occasionally used Notepad++ and Sublime, but less so for coding
- explored a now depreciated Atom text editor when it was released 
- tried, but gave up on learning emacs.

> Hint: start with IDLE and switch to VS Code next.

Why not VS Code right away?

With VS Code, you can customize the editor and take advantage of different workflows to run Python code, such as running a whole script, using `% ##` cells, or using Jupyter notebooks. You can also use VS Code remotely. Customization comes at a cost of a learning curve ahead of you -- things may not work out of the box as expected and sometimes you are left wondering if you are really using the VS Code to the fullest or indeed correctly. Going up the curve is worth the investment: VS Code a prevalent editor for remote services such as Github Codespaces and Gitpod -- once you learn to use and customize it, you can use it in many places (that even offer free resources such as a remote machine with Python installed).

## More tools

Great if you understand operating system and network basics, comfortable using command line, know what git and Gihub/Gitlab are for, write text im Markdown and gradually become familiar with Python packaging.
