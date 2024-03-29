from flask import Flask
from app import app
from user.models import User

@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup()

@app.route ('/user/signout')
def signout():
    return User().signout()

@app.route ('/user/signin', methods = ['POST'])
def signin():
    return User().signin()

@app.route ('/user/budgeting', methods = ['POST'])
def budgeting():
    return User().budgeting()

@app.route ('/user/income', methods = ['POST'])
def income():
    return User().income()

@app.route ('/user/expenses', methods = ['POST'])
def expenses():
    return User().expenses()