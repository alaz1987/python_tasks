# coding: utf-8
import random

def gen(n=1):
	if not isinstance(n, int):
		return None
	elif n < 1:
		return []
	else:
		return [random.randint(1, 100) for i in range(n)]

for i in range(1, 10):
	lst = gen(i)
	print (lst)