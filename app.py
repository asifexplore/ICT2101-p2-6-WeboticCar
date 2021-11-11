from flask import render_template, url_for, request, redirect
from init import app
from UserManagement import userLogin, addStudent, redirectDashboard



@app.route('/')
def index():
    return redirectDashboard() 

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        if userLogin(request.form['username'], request.form['password']):
            return render_template("dashboard.html")
        return render_template("login.html")

@app.route('/addStudent', methods = ['GET', 'POST'])
def register():
    addStudent(request.form['username'], request.form['password'])
    return redirectDashboard()


@app.route('/test')
def test():
    return render_template("test.html")


if __name__ == "__main__":
    context = ('cert.pem', 'key.pem')
    app.run(ssl_context = context, debug = True)