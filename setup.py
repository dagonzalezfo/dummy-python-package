import re
from setuptools import setup
 
# reading the version directy from the example.py file 
version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('example/example.py').read(),
    re.M
    ).group(1)
 
setup(
    name = "example-integrated",
    packages = ["example"],
	# Here is where the magic happens, here setuptools create the script to give access
    entry_points = {
        "console_scripts": ['example-test = example.example:main']
        },
    version = version,
    description = "Python command line application bare bones template.",
    long_description = long_descr,
    author = "Danilo Gonzalez",
    author_email = "lala@googlemail.com",
    url = "http://gehrcke.de/2014/02/distributing-a-python-command-line-application",
    )

