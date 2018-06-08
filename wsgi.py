from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route('/hello/')
@application.route('/hello/<name>')
def helloname(name='Bob'):
    return render_template('index.html', name=name)

if __name__ == "__main__":
    application.run()
