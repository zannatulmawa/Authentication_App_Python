from flask import Flask

#This is a system to create the flask app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bonybod' #secret code


    from .views import views
    from .auth import auth

    #registering the view and auth with our flask application
    #url_prefix will give the location that we wanted to go 
    #or function location that we wanted to call
    app.register_blueprint(views, url_prefix='/') 
    app.register_blueprint(auth, url_prefix='/')
    return app