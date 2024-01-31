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

@app.route('/budget')
def budget():
    return render_template('budget.html')

@app.route('/dashboard')
@login_required
def dashboard():
    if 'user' not in session:
        return redirect('/')

    user = db.users.find_one({"_id": session['user']['_id']})

    if not user:
        return jsonify({"error": "User not found in the database"}), 404

    budget = db.budgeting.find_one({"users_id": session['user']['_id']})

    return render_template('dashboard.html', user=user, budget=budget)

@app.route('/addincome')
@login_required
def addincome():
    return 'add income'

@app.route('/user/signup', methods=['POST'])
def signup_routes():
    return signup()

@app.route ('/user/signout')
def signout_routes():
    return signout()

@app.route ('/user/signin', methods = ['POST'])
def signin_routes():
    return signin()

@app.route ('/user/budgeting', methods = ['POST'])
@login_required
def budgeting_routes():
    return budgeting()

if __name__ == '__main__':
    from user.routes import signup, signout, signin, budgeting
    app.run(debug=True)
