from django.http import HttpResponse
from django.shortcuts import render
import json

def index(request):
	return render(request, 'main/homePage.html')

def render_profile(request):
	path = '../mysite/users.json'
	json_data = json.load(open(path, encoding='utf-8'))
	logins = []
	passwords = []
	statuses = []
	conditions = []
	last_names = []
	first_names = []
	middle_names = []

	if request.method == "GET":
		login = request.GET['login']

		for i in range(len(json_data['users'])):
			last_names.append(json_data['users'][i]['last_name'])
			first_names.append(json_data['users'][i]['first_name'])
			middle_names.append(json_data['users'][i]['middle_name'])
			logins.append(json_data['users'][i]['login'])
			passwords.append(json_data['users'][i]['password'])
			statuses.append(json_data['users'][i]['status'])

		last_name = last_names[logins.index(login)]
		first_name = first_names[logins.index(login)]
		middle_name = middle_names[logins.index(login)]
		password = passwords[logins.index(login)]
		status = statuses[logins.index(login)]

		return render(request, 'main/profile.html', {'last_name': last_name, 'first_name': first_name,
			'middle_name': middle_name,'login': login, 'password': password, 'status': status})

	data = {}
	data['login'] = request.POST['login']
	data['password'] = request.POST['password']

	for i in range(len(json_data['users'])):
		last_names.append(json_data['users'][i]['last_name'])
		first_names.append(json_data['users'][i]['first_name'])
		middle_names.append(json_data['users'][i]['middle_name'])
		logins.append(json_data['users'][i]['login'])
		passwords.append(json_data['users'][i]['password'])
		statuses.append(json_data['users'][i]['status'])
		conditions.append(json_data['users'][i]['condition'])
	
	if data['login'] in logins and data['password'] in passwords:
		last_name = last_names[logins.index(data['login'])]
		first_name = first_names[logins.index(data['login'])]
		middle_name = middle_names[logins.index(data['login'])]
		status = statuses[logins.index(data['login'])]
		condition = conditions[logins.index(data['login'])]

		if condition == "blocked":
			return render(request, 'main/homePage.html', {'message': "Извините, Ваш аккаунт заблокирован. Обратитесь к администратору."})
		else:
			return render(request, 'main/profile.html', {'last_name': last_name, 'first_name': first_name,
				'middle_name': middle_name, 'login': data['login'], 'password': data['password'], 'status': status})
	else:
		return render(request, 'main/homePage.html', {'message': "Неверная пара логин/пароль"})
