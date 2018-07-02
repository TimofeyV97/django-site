from django.http import HttpResponse
from django.shortcuts import render
import json

def index(request):
	path = '../mysite/projects.json'
	json_data = json.load(open(path, encoding='utf-8'))
	d = json_data['projects']
	projects_list = []
	projects_tmp_list = []
	workers_list = []
	workers_tmp_list = []
	phases_list = []
	phases_tmp_list = []

	for i in range(len(d)):
		projects_tmp_list.append(d[i]['name'])
		projects_tmp_list.append(d[i]['project_id'])
		projects_tmp_list.append("Дата начала: " + str(d[i]['start_date']))
		projects_tmp_list.append("Планируемая дата окончания: " + d[i]['end_date'])
		projects_tmp_list.append("Руководитель: " + str(d[i]['leader']['last_name']) + " " +
			str(d[i]['leader']['first_name']) + " " +
			str(d[i]['leader']['middle_name']))
		projects_tmp_list.append("Дата рождения руководителя: " + d[i]['leader']['birthday'])
		projects_tmp_list.append("Исполнители:")
		projects_tmp_list.append("Этапы:")
		projects_list.append(projects_tmp_list)
		projects_tmp_list = []

		for j in range(len(d[i]['workers'])):
			workers_tmp_list.append(d[i]['project_id'])
			workers_tmp_list.append(str(d[i]['workers'][j]['last_name']) + " " +
				str(d[i]['workers'][j]['first_name']) + " " +
				str(d[i]['workers'][j]['middle_name']))
			workers_tmp_list.append("Дата рождения: " + str(d[i]['workers'][j]['birthday']))
			workers_list.append(workers_tmp_list)
			workers_tmp_list = []

		for j in range(len(d[i]['phases'])):
			phases_tmp_list.append(d[i]['project_id'])
			phases_tmp_list.append((d[i]['phases'][j]['name']))
			phases_tmp_list.append("Дата начала: " + str(d[i]['phases'][j]['start_date']))
			phases_tmp_list.append("Дата окончания: " + str(d[i]['phases'][j]['end_date']))
			phases_tmp_list.append("Статус выполнения: " + str(d[i]['phases'][j]['status']))
			phases_tmp_list.append("Исполнитель: " + str(d[i]['phases'][j]['worker']))
			phases_tmp_list.append("Описание: " + str(d[i]['phases'][j]['description']))
			phases_list.append(phases_tmp_list)
			phases_tmp_list = []

	login = request.GET['login']
	status = request.GET['status']

	return render(request, 'projects/projects.html', {'projects_info': projects_list, 'workers_info': workers_list,
		'phases_info': phases_list, 'login': login, 'status': status})

def create_project(request):
	login = request.GET['login']
	status = request.GET['status']

	return render(request, 'projects/createProject.html', {'login': login, 'status': status})

def save_project(request):
	path = '../mysite/projects.json'
	path2 = '../mysite/users.json'
	json_data = json.load(open(path, encoding='utf-8'))
	json_data2 = json.load(open(path2, encoding='utf-8'))
	d = json_data['projects']
	login = request.GET['login']
	status = request.GET['status']
	workersNum = request.GET['w']
	phasesNum = request.GET['p']
	data = {}
	logins = []
	workers = []
	phases = []
	workers_tmp_dict = {}
	phase_tmp_dict = {}

	data['projectName'] = request.POST['projectName']
	data['projectStartDate'] = request.POST['projectStartDate']
	data['projectEndDate'] = request.POST['projectEndDate']
	data['leaderLastName'] = request.POST['leaderLastName']
	data['leaderFirstName'] = request.POST['leaderFirstName']
	data['leaderMiddleName'] = request.POST['leaderMiddleName']
	data['leaderBirthday'] = request.POST['leaderBirthday']
	
	for i in range(1, int(workersNum) + 1):
		workers_tmp_dict['last_name'] = request.POST['workerLastName' + str(i)]
		workers_tmp_dict['first_name'] = request.POST['workerFirstName' + str(i)]
		workers_tmp_dict['middle_name'] = request.POST['workerMiddleName' + str(i)]
		workers_tmp_dict['birthday'] = request.POST['workerBirthday' + str(i)]
		workers.append(workers_tmp_dict)
		workers_tmp_dict = {}

	for i in range(1, int(phasesNum) + 1):
		phase_tmp_dict['phase_id'] = str(len(d) + 1) + "." + str(i)
		phase_tmp_dict['name'] = request.POST['phaseName' + str(i)]
		phase_tmp_dict['start_date'] = request.POST['phaseStartDate' + str(i)]
		phase_tmp_dict['end_date'] = request.POST['phaseEndDate' + str(i)]
		phase_tmp_dict['status'] = request.POST['phaseStatus' + str(i)]
		phase_tmp_dict['worker'] = request.POST['phaseWorker' + str(i)]
		phase_tmp_dict['description'] = request.POST['phaseDescription' + str(i)]
		phases.append(phase_tmp_dict)
		phase_tmp_dict = {}

	for i in range(len(json_data2['users'])):
		logins.append(json_data2['users'][i]['login'])

	creator_id = logins.index(login)
	leader = {}
	leader['last_name'] = data['leaderLastName']
	leader['first_name'] = data['leaderFirstName']
	leader['middle_name'] = data['leaderMiddleName']
	leader['birthday'] = data['leaderBirthday']

	f = open(path, 'w+')
	json_data['projects'].append({'project_id': len(d) + 1, 'creator_id': creator_id + 1, 'name': data['projectName'], 'start_date': data['projectStartDate'],
		'end_date': data['projectEndDate'], 'leader' : leader, 'phases': phases, 'workers': workers})
	f.write(json.dumps(json_data))
	f.close()

	return render(request, 'projects/createProject.html', {'message': "Проект успешно добавлен", 'login': login, 'status': status})