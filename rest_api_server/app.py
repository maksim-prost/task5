from flask import Flask, jsonify,request, Response
some_url = ''
app = Flask(__name__)
db = []
headers = {'Access-Control-Allow-Origin': '*',
			'Content-type': 'text/html',}
			# "Access-Control-Allow-Methods":"GET, PUT, POST, DELETE",
			# "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept, Authorization"
		 #  }
def find_user(login):
	for user in db:
		if user['login']==login:return user['password']
	return False
def validate(password):
	return True

def fun1(form):
	user_exist = 'Такой пользователь существует, выберите другой логин'
	password_not_validate = 'Пароль слишком прост используйте более сложный'
	list_errors = []
	if find_user(form['login']): list_errors.append(user_exist)
	if not validate(form['password']): list_errors.append(password_not_validate)
	if list_errors:
		return jsonify({'response':False,'errors':list_errors}),300,headers
	db.append({'login': form.get('login'),
				'eMail':form.get('eMail'),
				'password':form.get('password'),
				'someParametr':form.get('someParametr')})#{key:form.get(key) for key in form})
	return jsonify({'response':True,'errors':[]}),201,headers
	# return jsonify({'login':form.get('login'),'password':form.get('password')}),200,headers
def fun2(form):
	return jsonify({'users':
		[[user['login'],user['eMail'],user['someParametr'] ]for user in db]}),200, headers
	# return jsonify({'users':  list(range(12))}),201, headers

def fun3(form):
	# return jsonify({'form':form,'db':db}),200,headers
	find = find_user(form['login'])
	if find and find==form['password']:
		return jsonify({'response': True,'errors':[]}),200,headers
	return jsonify({'response':False,'errors':['Неверный логин или пароль',]}),300,headers
def fun4(form):
	return jsonify({'task': 'undefined_request'}),400,headers


procesing_request = {
	'register-page':fun1,
	'show-users':fun2,
	'login':fun3,
	None:fun4,
}

@app.route('/',methods =['POST','GET'])
def index():
	form = request.values
	# return jsonify({'method':form.getlist('method'),'dir':dir(form)}),201, headers
	return procesing_request[form.get('method')](form)

if __name__ == '__main__':
	app.run(debug=True)
