# coding: utf-8

import os

'''
=================== задание 1 ===================
считать из файла список чисел, разделенных между собой символом ';'
найти мин, макс и посчитать кол-во чисел
результат сохранить в отдельный фал
'''
file_input  = os.path.abspath('numbers')
file_output = os.path.abspath('result')
delimeter = ";"

if os.path.exists(file_input):
	with open(file_input, mode='r') as file:
		data = file.read()
		numbers = data.split(delimeter)
		numbers = [ int(s) for s in numbers ] # генератор списка (создание списка через выражение)
else:
	numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

	with open(file_input, mode='w') as file:
		data = ";".join([ str(n) for n in numbers ])
		file.write(data)

		print ("Created file " + file_input)

min_value = numbers[0]
max_value = min_value
summ	  = 0
counts    = {}

for n in numbers:
	if n in counts:
		counts[n] += 1
	else:
		counts[n] = 1

	if n < min_value:
		min_value = n
	if n > max_value:
		max_value = n;

	summ += n

with open(file_output, mode='w') as file:
	lst = []
	for c in counts:
		string = str(c) + " = " + str(counts[c])
		lst.append(string)

	string = ", ".join(lst);
	data = """
		min value: {}
		max value: {}
		sum: {}
		counts: {}
	""".format(min_value, max_value, summ, string).strip("\t\n\r")
	data = data.replace("\t", "")

	file.write(data)

	print ("Result saved to file " + file_output)


'''
=================== задание 2*===================
замена нескольких подряд идущих букв на одну
'''
text = """
	Hello, Bill!

	Send me    some info about lesson.
""";

print (text)

words = text.split()
count_words = len(words)

for word in words:
	word_len = len(word)

	lst = {}
	c = 1

	for i in range(0, word_len - 1):
		if word[i] == word[i+1]:
			c = c + 1
			lst[word[i]] = c

	for l in lst:
		c = lst[l]
		com = l * c
		word = word.replace(com, l)
		print (word)