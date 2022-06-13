from xmlrpc.client import boolean
from flask import Blueprint, render_template
from sqlalchemy import true

#Blueprint means it has many routes and urls in it.
#we can add multiple files of views inside this


#auth is the name of our blueprint
auth = Blueprint('auth', __name__) 


@auth.route('/login')
def login(): #method
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout(): #method
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")
    

