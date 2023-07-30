from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

DB_NAME = 'mydb.db'

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    from .views import views
    from .learnflask import learnflask

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(learnflask, url_prefix='/')

    from .models import Note, User


    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    with app.app_context():
        db.init_app(app)
        db.create_all()
        print('Created Database')

    return app
