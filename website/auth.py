from xmlrpc.client import boolean
from flask import Blueprint, render_template, request, flash
from sqlalchemy import true

#Blueprint means it has many routes and urls in it.
#we can add multiple files of views inside this


#auth is the name of our blueprint
auth = Blueprint('auth', __name__) 


@auth.route('/login', methods=['GET', 'POST'])
def login(): #method
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout(): #method
    return "<p>Logout</p>"

@auth.route('/sign-up' , methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email=request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) < 2:
            flash('First Name should be more than 4 characters.', category='error')
        elif password1 != password2:
            flash('passwords should be matched.', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 7 characters.', category='error')
        else:
            flash('Account Created', category='success')
        

    return render_template("sign_up.html")
    

