# модуль создает экземпляр приложения, добавляет необходимые настройки, бд
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:t0sy{}b0sy@localhost/users_site'
# настройки подключения к бд, бд-postgres пароль-t0sy{}b0sy таблица-users_site
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)#в полноценном приложение реализовать менеджер управления бд
db.create_all()


# if __name__ == '__main__':
# 	app.run(debug=True)#приложение запускается в режиме отладки
