from flask import Flask,render_template,request
from db import Database

app = Flask(__name__)

dbo = Database()

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/perform_registration', methods=['POST'])
def perform_registration():
    # Here you would handle the registration logic
    data = request.form
    response=dbo.insert(data['email'], data['name'], data['password'])
    if response:
        return render_template("login.html",message="Registration successful! Please log in.")
    else:
        return render_template("register.html",message="User already exists!")

@app.route('/perform_login', methods=['POST'])
def perform_login():
    data = request.form
    response=dbo.search(data['email'], data['password'])
    if response:
        return "Welcome!"
    else:
        return render_template("login.html",message="Invalid email or password.") 

app.run(debug=True)
