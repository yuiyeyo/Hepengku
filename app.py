from flask import Flask, render_template, redirect, session
from functools import wraps
from datetime import datetime
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

    user = db.users.find_one({"_id": session['user']['_id']})

    if not user:
        return jsonify({"error": "User not found in the database"}), 404

    budget = db.budgeting.find_one({"users_id": session['user']['_id']})

    transactions_data = db.transactions.find({"users_id": session['user']['_id']}).sort("date", -1)

    today = datetime.now()
    start_date = today.replace(day=1)

    transactions_data_current_month = db.transactions.find({
        "users_id": session['user']['_id'],
        "date": {"$gte": start_date.strftime('%Y-%m-%d')}
    }).sort("date", -1)

    total_amount_current_month = sum(int(transaction['amount']) for transaction in transactions_data_current_month)

    current_date = today.strftime('%Y-%m-%d')

    return render_template('dashboard.html', user=user, budget=budget, transactions_data=transactions_data, current_date=current_date, transactions_data_current_month=transactions_data_current_month, total_amount_current_month=total_amount_current_month)


@app.route('/addincome')
@login_required
def addincome():
    return render_template('addincome.html')

@app.route('/addoutcome')
@login_required
def addoutcome():
    return render_template('addoutcome.html')

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

@app.route ('/user/income', methods = ['POST'])
@login_required
def income_routes():
    return income()

@app.route ('/user/outcome', methods = ['POST'])
@login_required
def outcome_routes():
    return outcome()

if __name__ == '__main__':
    from user.routes import signup, signout, signin, budgeting, income, outcome
    app.run(debug=True)
