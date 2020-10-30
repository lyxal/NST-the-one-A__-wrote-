from sys import argv
from lazy import *
from collections.abc import Iterable

code = open(argv[1], encoding = "utf-8-sig").read()

oprnd = []
while True:
	try:
		a = input()
		if a == "":
			break
		oprnd.append(eval(a))
	except EOFError:
		# Allow EOF terminator to end input.
		break