from email.policy import default
from flask import Flask
app=Flask(__name__)

@app.route('/greet',defaults={'name':'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello %s</h1>' % name