from django.http import HttpResponse
from django.shortcuts import render
import json

def edit_phases(request):
	login = request.GET['login']
	status = request.GET['status']
	path = '../mysite/projects.json'
	path_2 = '../mysite/users.json'
	json_data = json.load(open(path, encoding='utf-8'))
	json_data_2 = json.load(open(path_2, encoding='utf-8'))
	d = json_data['projects']
	d_2 = json_data_2['users']
	logins = []
	last_names = []
	first_names = []
	middle_names = []
	phases_list = []
	phases_tmp_list = []

	for i in range(len(d_2)):
		last_names.append(d_2[i]['last_name'])
		first_names.append(d_2[i]['first_name'])
		middle_names.append(d_2[i]['middle_name'])
		logins.append(d_2[i]['login'])

	last_name = last_names[logins.index(login)]
	first_name = first_names[logins.index(login)]
	middle_name = middle_names[logins.index(login)]

	for i in range(len(d)):
		for j in range(len(d[i]['phases'])):
			if d[i]['phases'][j]['worker'] == (last_name + " " + first_name + " " + middle_name):
				phases_tmp_list.append(d[i]['name'])
				phases_tmp_list.append("Название этапа: " + str(d[i]['phases'][j]['name']))
				phases_tmp_list.append("Дата начала: " + str(d[i]['phases'][j]['start_date']))
				phases_tmp_list.append("Дата окончания: " + str(d[i]['phases'][j]['end_date']))
				phases_tmp_list.append("Исполнитель: " + str(d[i]['phases'][j]['worker']))
				phases_tmp_list.append("Описание: " + str(d[i]['phases'][j]['description']))
				phases_tmp_list.append("Статус выполнения этапа: " + d[i]['phases'][j]['status'])
				phases_tmp_list.append(d[i]['phases'][j]['phase_id'])
				phases_list.append(phases_tmp_list)
				phases_tmp_list = []

	return render(request, 'edit/editPhases.html', {'phases': phases_list, 'login': login,
		'status': status})

def edit_phase(request):
	login = request.GET['login']
	status = request.GET['status']
	phase_id = request.GET['phase_id']
	path = '../mysite/projects.json'
	json_data = json.load(open(path, encoding='utf-8'))
	d = json_data['projects']
	phases_list = []

	for i in range(len(d)):
		for j in range(len(d[i]['phases'])):
			if d[i]['phases'][j]['phase_id'] == phase_id:
				phases_list.append(d[i]['name'])
				phases_list.append("Название этапа: " + str(d[i]['phases'][j]['name']))
				phases_list.append("Дата начала: " + str(d[i]['phases'][j]['start_date']))
				phases_list.append("Дата окончания: " + str(d[i]['phases'][j]['end_date']))
				phases_list.append("Исполнитель: " + str(d[i]['phases'][j]['worker']))
				phases_list.append("Описание: " + str(d[i]['phases'][j]['description']))
				phases_list.append(d[i]['phases'][j]['status'])

	return render(request, 'edit/editPhase.html', {'login': login,
		'status': status, 'phase_id': phase_id, 'phases': phases_list})

def save_edit_phase(request):
	login = request.GET['login']
	status = request.GET['status']
	path = '../mysite/projects.json'
	path_2 = '../mysite/users.json'
	json_data = json.load(open(path, encoding='utf-8'))
	json_data_2 = json.load(open(path_2, encoding='utf-8'))
	d = json_data['projects']
	d_2 = json_data_2['users']
	logins = []
	last_names = []
	first_names = []
	middle_names = []
	phases_list = []
	phases_tmp_list = []

	phase_id = request.GET['phase_id']
	phase_status = request.POST['phaseStatus']

	f = open(path, 'w')
	
	for i in range(len(d)):
		for j in range(len(d[i]['phases'])):
			if d[i]['phases'][j]['phase_id'] == phase_id:
				json_data['projects'][i]['phases'][j]['status'] = phase_status

	f.write(json.dumps(json_data))
	f.close()

	for i in range(len(d_2)):
		last_names.append(d_2[i]['last_name'])
		first_names.append(d_2[i]['first_name'])
		middle_names.append(d_2[i]['middle_name'])
		logins.append(d_2[i]['login'])

	last_name = last_names[logins.index(login)]
	first_name = first_names[logins.index(login)]
	middle_name = middle_names[logins.index(login)]

	for i in range(len(d)):
		for j in range(len(d[i]['phases'])):
			if d[i]['phases'][j]['worker'] == (last_name + " " + first_name + " " + middle_name):
				phases_tmp_list.append(d[i]['name'])
				phases_tmp_list.append("Название этапа: " + str(d[i]['phases'][j]['name']))
				phases_tmp_list.append("Дата начала: " + str(d[i]['phases'][j]['start_date']))
				phases_tmp_list.append("Дата окончания: " + str(d[i]['phases'][j]['end_date']))
				phases_tmp_list.append("Исполнитель: " + str(d[i]['phases'][j]['worker']))
				phases_tmp_list.append("Описание: " + str(d[i]['phases'][j]['description']))
				phases_tmp_list.append("Статус выполнения этапа: " + d[i]['phases'][j]['status'])
				phases_tmp_list.append(d[i]['phases'][j]['phase_id'])
				phases_list.append(phases_tmp_list)
				phases_tmp_list = []

	return render(request, 'edit/editPhases.html', {'phases': phases_list, 'login': login,
		'status': status, 'message': "Изменения сохранены"})

def edit_projects(request):
	login = request.GET['login']
	status = request.GET['status']
	path = '../mysite/projects.json'
	path_2 = '../mysite/users.json'
	json_data = json.load(open(path, encoding='utf-8'))
	json_data_2 = json.load(open(path_2, encoding='utf-8'))
	d = json_data['projects']
	d_2 = json_data_2['users']
	logins = []
	last_names = []
	first_names = []
	middle_names = []
	projects_list = []
	projects_tmp_list = []

	for i in range(len(d_2)):
		last_names.append(d_2[i]['last_name'])
		first_names.append(d_2[i]['first_name'])
		middle_names.append(d_2[i]['middle_name'])
		logins.append(d_2[i]['login'])

	last_name = last_names[logins.index(login)]
	first_name = first_names[logins.index(login)]
	middle_name = middle_names[logins.index(login)]

	for i in range(len(d)):
		if (str(d[i]['leader']['last_name']) + " " +
		str(d[i]['leader']['first_name']) + " " +
		str(d[i]['leader']['middle_name'])) == (last_name + " " + first_name + " " + middle_name):
			projects_tmp_list.append(d[i]['name'])
			projects_tmp_list.append("Дата начала: " + str(d[i]['start_date']))
			projects_tmp_list.append("Планируемая дата окончания: " + d[i]['end_date'])
			projects_tmp_list.append("Руководитель: " + str(d[i]['leader']['last_name']) + " " +
			str(d[i]['leader']['first_name']) + " " +
			str(d[i]['leader']['middle_name']))
			projects_tmp_list.append("Дата рождения руководителя: " + d[i]['leader']['birthday'])
			projects_tmp_list.append(d[i]['project_id'])
			projects_list.append(projects_tmp_list)
			projects_tmp_list = []		

	return render(request, 'edit/editProjects.html', {'projects': projects_list,
		'login': login, 'status': status})

def edit_project(request):
	login = request.GET['login']
	status = request.GET['status']
	project_id = request.GET['project_id']
	path = '../mysite/projects.json'
	json_data = json.load(open(path, encoding='utf-8'))
	d = json_data['projects']
	projects_list = []

	for i in range(len(d)):
		if str(d[i]['project_id']) == project_id:
			projects_list.append(d[i]['name'])
			projects_list.append(d[i]['start_date'])
			projects_list.append(d[i]['end_date'])

	return render(request, 'edit/editProject.html', {'login': login,
		'status': status, 'project_id': project_id,'projects': projects_list})

def save_edit_project(request):
	login = request.GET['login']
	status = request.GET['status']
	project_id = request.GET['project_id']
	path = '../mysite/projects.json'
	path_2 = '../mysite/users.json'
	json_data = json.load(open(path, encoding='utf-8'))
	json_data_2 = json.load(open(path_2, encoding='utf-8'))
	d = json_data['projects']
	d_2 = json_data_2['users']
	logins = []
	last_names = []
	first_names = []
	middle_names = []
	projects_list = []
	projects_tmp_list = []

	project_name = request.POST['projectName']
	project_start_date = request.POST['projectStartDate']
	project_end_date = request.POST['projectEndDate']

	f = open(path, 'w')
	
	for i in range(len(d)):
		if str(d[i]['project_id']) == project_id:
			json_data['projects'][i]['name'] = project_name
			json_data['projects'][i]['start_date'] = project_start_date
			json_data['projects'][i]['end_date'] = project_end_date

	f.write(json.dumps(json_data))
	f.close()

	for i in range(len(d_2)):
		last_names.append(d_2[i]['last_name'])
		first_names.append(d_2[i]['first_name'])
		middle_names.append(d_2[i]['middle_name'])
		logins.append(d_2[i]['login'])

	last_name = last_names[logins.index(login)]
	first_name = first_names[logins.index(login)]
	middle_name = middle_names[logins.index(login)]

	for i in range(len(d)):
		if (str(d[i]['leader']['last_name']) + " " +
		str(d[i]['leader']['first_name']) + " " +
		str(d[i]['leader']['middle_name'])) == (last_name + " " + first_name + " " + middle_name):
			projects_tmp_list.append(d[i]['name'])
			projects_tmp_list.append("Дата начала: " + str(d[i]['start_date']))
			projects_tmp_list.append("Планируемая дата окончания: " + d[i]['end_date'])
			projects_tmp_list.append("Руководитель: " + str(d[i]['leader']['last_name']) + " " +
			str(d[i]['leader']['first_name']) + " " +
			str(d[i]['leader']['middle_name']))
			projects_tmp_list.append("Дата рождения руководителя: " + d[i]['leader']['birthday'])
			projects_tmp_list.append(d[i]['project_id'])
			projects_list.append(projects_tmp_list)
			projects_tmp_list = []

	return render(request, 'edit/editProjects.html', {'projects': projects_list, 'login': login,
		'status': status, 'message': "Изменения сохранены"})

def edit_projects_manager(request):
	login = request.GET['login']
	status = request.GET['status']
	path = '../mysite/projects.json'
	path_2 = '../mysite/users.json'
	json_data = json.load(open(path, encoding='utf-8'))
	json_data_2 = json.load(open(path_2, encoding='utf-8'))
	d = json_data['projects']
	d_2 = json_data_2['users']
	projects_list = []
	projects_tmp_list = []
	logins = []
	user_ids = []

	for i in range(len(d_2)):
		user_ids.append(d_2[i]['user_id'])
		logins.append(d_2[i]['login'])

	user_id = user_ids[logins.index(login)]

	for i in range(len(d)):
		if d[i]['creator_id'] == user_id:
			projects_tmp_list.append(d[i]['name'])
			projects_tmp_list.append("Дата начала: " + str(d[i]['start_date']))
			projects_tmp_list.append("Планируемая дата окончания: " + d[i]['end_date'])
			projects_tmp_list.append("Руководитель: " + str(d[i]['leader']['last_name']) + " " +
			str(d[i]['leader']['first_name']) + " " +
			str(d[i]['leader']['middle_name']))
			projects_tmp_list.append("Дата рождения руководителя: " + d[i]['leader']['birthday'])
			projects_tmp_list.append(d[i]['project_id'])
			projects_list.append(projects_tmp_list)
			projects_tmp_list = []		

	return render(request, 'edit/editProjectsManager.html', {'projects': projects_list,
		'login': login, 'status': status})

def edit_project_manager(request):
	login = request.GET['login']
	status = request.GET['status']
	project_id = request.GET['project_id']
	path = '../mysite/projects.json'
	json_data = json.load(open(path, encoding='utf-8'))
	d = json_data['projects']
	projects_list = []

	for i in range(len(d)):
		if str(d[i]['project_id']) == project_id:
			projects_list.append(d[i]['name'])
			projects_list.append(d[i]['start_date'])
			projects_list.append(d[i]['end_date'])
			projects_list.append(d[i]['leader']['last_name'])
			projects_list.append(d[i]['leader']['first_name'])
			projects_list.append(d[i]['leader']['middle_name'])
			projects_list.append(d[i]['leader']['birthday'])

	return render(request, 'edit/editProjectManager.html', {'login': login,
		'status': status, 'project_id': project_id,'projects': projects_list})

def save_edit_project_manager(request):
	login = request.GET['login']
	status = request.GET['status']
	project_id = request.GET['project_id']
	path = '../mysite/projects.json'
	path_2 = '../mysite/users.json'
	json_data = json.load(open(path, encoding='utf-8'))
	json_data_2 = json.load(open(path_2, encoding='utf-8'))
	d = json_data['projects']
	d_2 = json_data_2['users']
	logins = []
	last_names = []
	first_names = []
	middle_names = []
	projects_list = []
	projects_tmp_list = []

	project_name = request.POST['projectName']
	project_start_date = request.POST['projectStartDate']
	project_end_date = request.POST['projectEndDate']
	leader_last_name = request.POST['leaderLastName']
	leader_first_name = request.POST['leaderFirstName']
	leader_middle_name = request.POST['leaderMiddleName']
	leader_birthday = request.POST['leaderBirthday']

	f = open(path, 'w')
	
	for i in range(len(d)):
		if str(d[i]['project_id']) == project_id:
			json_data['projects'][i]['name'] = project_name
			json_data['projects'][i]['start_date'] = project_start_date
			json_data['projects'][i]['end_date'] = project_end_date
			json_data['projects'][i]['leader']['last_name'] = leader_last_name
			json_data['projects'][i]['leader']['first_name'] = leader_first_name
			json_data['projects'][i]['leader']['middle_name'] = leader_middle_name
			json_data['projects'][i]['leader']['birthday'] = leader_birthday

	f.write(json.dumps(json_data))
	f.close()

	for i in range(len(d_2)):
		last_names.append(d_2[i]['last_name'])
		first_names.append(d_2[i]['first_name'])
		middle_names.append(d_2[i]['middle_name'])
		logins.append(d_2[i]['login'])

	last_name = last_names[logins.index(login)]
	first_name = first_names[logins.index(login)]
	middle_name = middle_names[logins.index(login)]

	for i in range(len(d)):
		for j in range(len(json_data_2['users'])):
			if d[i]['creator_id'] == json_data_2['users'][j]['user_id']:
				projects_tmp_list.append(d[i]['name'])
				projects_tmp_list.append("Дата начала: " + str(d[i]['start_date']))
				projects_tmp_list.append("Планируемая дата окончания: " + d[i]['end_date'])
				projects_tmp_list.append("Руководитель: " + str(d[i]['leader']['last_name']) + " " +
				str(d[i]['leader']['first_name']) + " " +
				str(d[i]['leader']['middle_name']))
				projects_tmp_list.append("Дата рождения руководителя: " + d[i]['leader']['birthday'])
				projects_tmp_list.append(d[i]['project_id'])
				projects_list.append(projects_tmp_list)
				projects_tmp_list = []

	return render(request, 'edit/editProjectsManager.html', {'projects': projects_list, 'login': login,
		'status': status, 'message': "Изменения сохранены"})

def edit_users(request):
	login = request.GET['login']
	status = request.GET['status']
	path = '../mysite/users.json'
	json_data = json.load(open(path, encoding='utf-8'))
	d = json_data['users']
	users_list = []
	users_tmp_list = []

	for i in range(len(d)):
		users_tmp_list.append(d[i]['last_name'] + " " + d[i]['first_name'] + " " + d[i]['middle_name'])
		users_tmp_list.append(d[i]['status'])
		users_tmp_list.append(d[i]['user_id'])
		users_list.append(users_tmp_list)
		users_tmp_list = []

	return render(request, 'edit/editUsers.html', {'login': login, 'status': status, 'users': users_list})

def edit_user(request):
	login = request.GET['login']
	status = request.GET['status']
	user_id = request.GET['user_id']
	path = '../mysite/users.json'
	json_data = json.load(open(path, encoding='utf-8'))
	d = json_data['users']
	users_list = []

	for i in range(len(d)):
		if str(d[i]['user_id']) == user_id:
			users_list.append(d[i]['last_name'] + " " + d[i]['first_name'] + " " + d[i]['middle_name'])
			users_list.append(d[i]['login'])
			users_list.append(d[i]['status'])
			users_list.append(d[i]['condition'])
			users_list.append(d[i]['user_id'])

	return render(request, 'edit/editUser.html', {'login': login, 'status': status, 'users': users_list})

def save_edit_user(request):
	login = request.GET['login']
	status = request.GET['status']
	user_id = request.GET['user_id']
	path = '../mysite/users.json'
	json_data = json.load(open(path, encoding='utf-8'))
	d = json_data['users']
	users_list = []

	f = open(path, 'w')

	for i in range(len(d)):
		if str(d[i]['user_id']) == user_id:
			if json_data['users'][i]['condition'] == "active":
				json_data['users'][i]['condition'] = "blocked"
			else:
				json_data['users'][i]['condition'] = "active"

	f.write(json.dumps(json_data))
	f.close()

	for i in range(len(d)):
		if str(d[i]['user_id']) == user_id:
			users_list.append(d[i]['last_name'] + " " + d[i]['first_name'] + " " + d[i]['middle_name'])
			users_list.append(d[i]['login'])
			users_list.append(d[i]['status'])
			users_list.append(d[i]['condition'])
			users_list.append(d[i]['user_id'])

	return render(request, 'edit/editUser.html', {'login': login, 'status': status, 'users': users_list})

def delete_project(request):
	login = request.GET['login']
	status = request.GET['status']
	project_id = request.GET['project_id']
	path = '../mysite/projects.json'
	path_2 = '../mysite/users.json'
	json_data = json.load(open(path, encoding='utf-8'))
	json_data_2 = json.load(open(path_2, encoding='utf-8'))
	d = json_data['projects']
	d_2 = json_data_2['users']
	projects_list = []
	projects_tmp_list = []
	logins = []
	user_ids = []

	f = open(path, 'w')

	for i in range(len(d)):
		if str(d[i]['project_id']) == project_id:
			del json_data['projects'][i]
			break

	for i in range(i, len(d)):
		json_data['projects'][i]['project_id'] -= 1
		for j in range(len(d[i]['phases'])):
			json_data['projects'][i]['phases'][j]['phase_id'] = (str(json_data['projects'][i]['project_id'])
				+ "." + str(j + 1))

	f.write(json.dumps(json_data))
	f.close()

	for i in range(len(d_2)):
		user_ids.append(d_2[i]['user_id'])
		logins.append(d_2[i]['login'])

	user_id = user_ids[logins.index(login)]

	for i in range(len(d)):
		if d[i]['creator_id'] == user_id:
			projects_tmp_list.append(d[i]['name'])
			projects_tmp_list.append("Дата начала: " + str(d[i]['start_date']))
			projects_tmp_list.append("Планируемая дата окончания: " + d[i]['end_date'])
			projects_tmp_list.append("Руководитель: " + str(d[i]['leader']['last_name']) + " " +
			str(d[i]['leader']['first_name']) + " " +
			str(d[i]['leader']['middle_name']))
			projects_tmp_list.append("Дата рождения руководителя: " + d[i]['leader']['birthday'])
			projects_tmp_list.append(d[i]['project_id'])
			projects_list.append(projects_tmp_list)
			projects_tmp_list = []		

	return render(request, 'edit/editProjectsManager.html', {'projects': projects_list,
		'login': login, 'status': status})