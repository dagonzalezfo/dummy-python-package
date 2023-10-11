# Example Package

This is a simple example package to create a package with a self build executable
by following this: https://gehrcke.de/2014/02/distributing-a-python-command-line-application/

Further details about this magic here: 
- https://setuptools.pypa.io/en/latest/userguide/entry_point.html
- https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools

Hints:
- example.py: contains the source of example package
- __main__.py: do the magic by importing and calling main()
- __init__.py: dummy file to enable example as a package
- setup.py: Instruction for setup tools
