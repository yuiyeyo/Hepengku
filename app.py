from flask import Flask, render_template

app = Flask(__name__)

#Routes
from user import routes

@app.route('/')
def home():
    return render_template('home.html')

#@app.route('/join')
#def signup():
#    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/user/signup', methods=['GET'])
def signup_route():
    return signup()

if __name__ == '__main__':
    from user.routes import signup
    app.run(debug=True)