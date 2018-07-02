from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
import json

def index(request):
	return render(request, 'registration/registration.html')

def register(request):
	path = '../mysite/users.json'
	json_data = json.load(open(path, encoding='utf-8'))
	logins = []
	data = {}
	data['lastName'] = request.POST['lastName']
	data['firstName'] = request.POST['firstName']
	data['middleName'] = request.POST['middleName']
	data['login'] = request.POST['login']
	data['password1'] = request.POST['password1']
	data['password2'] = request.POST['password2']
	
	for i in range(len(json_data['users'])):
		logins.append(json_data['users'][i]['login'])

	if data['password1'] != data['password2']:
		return render(request, 'registration/registration.html', {'message': 'Пароли не совпадают'})
	elif data['login'] in logins:
		return render(request, 'registration/registration.html', {'message': 'Такой логин уже занят'})
	else:
		f = open(path, 'w+')
		json_data['users'].append({'user_id': len(json_data['users']) + 1, 'last_name': data['lastName'],
			'first_name': data['firstName'], 'middle_name': data['middleName'],
			'login': data['login'], 'password': data['password1'], 'status': request.POST['status'], 'condition': "active"})
		f.write(json.dumps(json_data))
		f.close()
		
		return render(request, 'registration/registration.html', {'message': 'Вы зарегистрированы'})