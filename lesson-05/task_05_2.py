# coding: utf-8
import sys

def calc(a, b, o):
	if o == '+':
		return a + b
	elif o == '-':
		return a - b
	elif o == '*':
		return a * b
	elif o == '^':
		return a ** b
	elif o == '/':
		return None if b == 0 else a / b
	elif o == '%':
		return a % b
	else:
		return None

def parse(statment):
	ops = ['*', '/', '+', '-', '%', '^']
	for n in range(len(statment)):
		s = statment[n]
		if s in ops:
			sa = statment[:n].strip()
			sb = statment[n+1:].strip()
			
			if sa.isdigit() and sb.isdigit():
				a = float(sa)
				b = float(sb)
				return calc(a, b, s)

print ('Enter arifmetical expression: <a operator b> or <exit> to exit program')

while (True):
	line = input()

	if line == 'exit':
		break

	result = parse(line)
	
	if result != None:
		print (line, '=', result)
