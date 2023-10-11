
__version__= "0.0.1"
import sys

def add_one(number):
	return number + 1

def main():
	test=add_one(int(sys.argv[1]))
	print(test)
