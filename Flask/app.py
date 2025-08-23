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
        return "Registration successful!"
    else:
        return "User already exists!"

app.run(debug=True)
