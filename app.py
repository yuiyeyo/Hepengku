from flask import Flask, render_template
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient('localhost', 27017)
db = client.hepengku

#Routes
from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join')
def join():
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/user/signup', methods=['POST'])
def signup_routes():
    return signup()

if __name__ == '__main__':
    from user.routes import signup
    app.run(debug=True)
