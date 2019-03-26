import threading 
from ParseFunc import ParseFunc
from FuncGenerator import FuncGenerator

print('\n______Testing ParseFunc and FuncGenerator______\n')

tests = ['f(x,y) = -.02*x+tan(y)','f(x) = log(y)', 'x+y','f(x,y) = tan(x-y))','f(x,y) = -3.1415*y+x','f(x) x*y','f(x,y) = sin(-x-log(y))']

for test in tests:
	if FuncGenerator(test) == False:
		print('\n')






