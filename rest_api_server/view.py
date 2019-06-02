# модуль отвечает за обработку запросов
from flask import  jsonify,request
from app import app
#добавляет класс запись в бд 
from models import UsersSite
headers = {'Access-Control-Allow-Origin': '*',
		   'Content-type': 'text/html',		}


def find_user(login):
	user = UsersSite.query.filter(UsersSite.login==login).first()
	return user and user.password

def validate(password):
	return True

# добавляем пользователя в бд, если такого не существует и пароль достаточно сложен 
def fun1(form):
	user_exist = 'Такой пользователь существует, выберите другой логин'
	password_not_validate = 'Пароль слишком прост используйте более сложный'
	list_errors = []
	if find_user(form['login']): list_errors.append(user_exist)
	if not validate(form['password']): list_errors.append(password_not_validate)
	if list_errors:
		return jsonify({'response':False,'errors':list_errors}),300,headers
	# cоздаем экземпляр класса запись в таблицы бд, с задаными полями
	# , сохраняем его в бд
	UsersSite(login=form.get('login'),
					eMail=form.get('eMail'),
					password=form.get('password'),
					someParametr=form.get('someParametr')).save()
	return jsonify({'response':True,'errors':[]}),201,headers
	
#возвращает список пользователей с полями почти и дополнительные параметры
def fun2(form):
	# return '{'+'users:[{}]'.format(UsersSite.query.all())+'}',200, headers
	return jsonify({'users':
		[user.json() for user in UsersSite.query.all()]}),200, headers

#проверяет есть ли пользователь в бд, совпадает пароль
def fun3(form):
	find = find_user(form['login'])
	if find and find==form['password']:
		return jsonify({'response': True,'errors':[]}),200,headers
	return jsonify({'response':False,'errors':['Неверный логин или пароль',]}),300,headers

#если метод запроса не определен, возвращает сообщение об этом
def fun4(form):
	return jsonify({'response': 'undefined_request'}),400,headers

#в зависимости какой метод передан в запросе, различные функции обрабатывают данные запроса
procesing_request = {
	'register-page':fun1,
	'show-users':fun2,
	'login':fun3,
	None:fun4,
}

@app.route('/',methods =['POST','GET'])
def index():
	# return jsonify({'response': 'undefined_request'}),300,headers

	form = request.values
	return procesing_request[form.get('method')](form)