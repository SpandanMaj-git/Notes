# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from os import path

# db = SQLAlchemy()
# DB_NAME = 'mydb.db'


# def create_app():
#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'secretkey'
#     app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
#     db.init_app(app)

#     from .views import views
#     from .learnflask import learnflask

#     app.register_blueprint(views, url_prefix='/')
#     app.register_blueprint(learnflask, url_prefix='/')

#     from .models import User, Note
#     return app

# def create_database(app):

#     if not path.exists('website/' + DB_NAME):
#             db.create_all(app = app)
#             print('Database created')

# with app.app_context():
#     create_database(app)

# app = create_app()

# with app.app_context():
#     create_database(app)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'mydb.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .learnflask import learnflask

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(learnflask, url_prefix='/')

    from .models import User, Note
    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Database created')


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        create_database(app)
    app.run(debug=True)
