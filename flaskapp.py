#!/usr/bin/python3

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name='Bob'):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run()
