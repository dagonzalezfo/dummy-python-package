import sys
import os

def add_one(number):
	return number + 21
def main():
	data_path = os.path.join(os.path.dirname(__file__),'data','data.rst')
	test=add_one(int(sys.argv[1]))
#	print(data_path)
	with open(data_path,'r') as file:
		print(file.read())
	print(test)
