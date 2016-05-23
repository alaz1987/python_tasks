# coding: utf-8
import os

def webserver(url, name):
	file_path = os.path.abspath(__file__)
	count = len(os.path.basename(__file__))
	dir_path = file_path[:len(file_path)-count]
	template_file = dir_path + 'template.html';

	with open(template_file, 'r') as f:
		data = f.read()
		data = data.replace('#name#', name)

	def ya(name):
		nonlocal data
		return data.replace('#engine#', 'Yandex')

	def google(name):
		nonlocal data
		return data.replace('#engine#', 'Google')

	urls = {
		'ya.ru' : ya,
		'google.com' : google
	}

	return urls[url](name)

print (webserver('ya.ru', 'Alex'))
print (webserver('google.com', 'Mike'))