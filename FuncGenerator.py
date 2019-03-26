import threading
from ParseFunc import ParseFunc

def FuncGenerator(w):
	if ParseFunc(w):
		print('')
		print('Python Function:\n')
		i = w.index("=")
		print("def " + w[:i] + ":")
		print("\tz = " + w[i+1:])
		print("\treturn z")
		print('')