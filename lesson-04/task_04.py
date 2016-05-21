# coding: utf-8

# пузырьковая сортировка: вариант 1
def bubble_sort(lst):
	n = len(lst)
	count_iteration = 0

	for i in range(n):
		for j in range(n - 1):
			count_iteration += 1
			if lst[j] > lst[j + 1]:
				lst[j], lst[j + 1] = lst[j + 1], lst[j]

	print ("iteration:", count_iteration)
	return lst

# пузырьковая сортировка: вариант 2
def bubble_sort2(lst):
	max_n = len(lst)
	n = 0
	count_iteration = 0

	for i in range(max_n):
		for j in range(max_n - 1 - n):
			count_iteration += 1
			if lst[j] > lst[j + 1]:
				lst[j], lst[j + 1] = lst[j + 1], lst[j]
		n += 1

	print ("iteration:", count_iteration)
	return lst

# пузырьковая сортировка: вариант 3
def bubble_sort3(lst):
	max_n = len(lst)
	n = 0
	count_iteration = 0

	for i in range(max_n):
		sort = False

		for j in range(max_n - 1 - n):
			count_iteration += 1
			if lst[j] > lst[j + 1]:
				lst[j], lst[j + 1] = lst[j + 1], lst[j]
				sort = True
		
		if not sort:
			break
		n += 1

	print ("iteration:", count_iteration)
	return lst

lst_sourse = [4, 7, 1, 3, 5]
print ("sourse list:", lst_sourse)

lst1 = bubble_sort(lst_sourse)
print ("sorted list 1", lst1)

lst2 = bubble_sort2(lst_sourse)
print ("sorted list 2", lst2)

lst3 = bubble_sort3(lst_sourse)
print ("sorted list 3", lst3)