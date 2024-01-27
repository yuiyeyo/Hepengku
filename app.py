from flask import Flask, render_template, redirect, session
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = b'\xcb\xc1\xf98\x7f\xa5\xa5/\xe22\xb7\x19\x0bb\x8bL'

client = pymongo.MongoClient('localhost', 27017)
db = client.hepengku

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
        
    return wrap

#Routes
from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join')
def join():
    return render_template('signup.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/user/signup', methods=['POST'])
def signup_routes():
    return signup()

@app.route ('/user/signout')
def signout_routes():
    return signout()

@app.route ('/user/signin', methods = ['POST'])
def signin_routes():
    return signin()

if __name__ == '__main__':
    from user.routes import signup, signout, signin
    app.run(debug=True)
