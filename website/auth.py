from flask import Blueprint

#Blueprint means it has many routes and urls in it.
#we can add multiple files of views inside this


#auth is the name of our blueprint
auth = Blueprint('auth', __name__) 


@auth.route('/login')
def login(): #method
    return "<p>Login</p>"

@auth.route('/logout')
def logout(): #method
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p> Sign up </p>"
    

