from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/hello/")
@application.route("/hello/<name>")
def helloname(name="Bob"):
    return render_template("index.html", name=name)

@application.route("/names/")
def names():
    table = """        <table style="width:100%">
            <tr>
                <th>Firstname</th>
                <th>Lastname</th> 
                <th>Age</th>
            </tr>
            <tr>
                <td>Jill</td>
                <td>Smith</td> 
                <td>50</td>
            </tr>
            <tr>
                <td>Eve</td>
                <td>Jackson</td> 
                <td>94</td>
            </tr>
        </table>"""
    name = "admin"
    return render_template("index.html", name=name, table=table)

if __name__ == "__main__":
    application.run()
