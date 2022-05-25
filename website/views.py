from flask import Blueprint

#Blueprint means it has many routes and urls in it.
#we can add multiple files of views inside this


#views is the name of our blueprint
views = Blueprint('views', __name__) 

#@view notation will go to the requested route or url
@views.route('/')
def home():
    return "<h1>Python App</h1>"

