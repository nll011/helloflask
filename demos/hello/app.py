from flask import Flask
import click
app=Flask(__name__)

@app.route('/greet',defaults={'name':'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello %s</h1>' % name

@app.cli.command()
def hello():
    """Just say hello"""
    click.echo('Hello, Human!')