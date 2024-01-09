import sqlite3
from flask import *
app = Flask(__name__)

@app.route('/')

def homepage():
    return render_template("homepages.html")

@app.route('/admin')

def adminpage():
    return render_template("adminpages.html")


@app.route('/login')

def loginpage():
    return  render_template("logins.html")

@app.route("/register")

def registerpage():
    return render_template("registers.html")

@app.route("/stulogins",methods=['GET','POST'])

def studentlogin():
    if request.method == 'POST':
        conn = sqlite3.connect('librarydatas.db')
        cur = conn.cursor()
        email = (request.form["email"])
        passwords = (request.form["passwords"])
        print(email,passwords)
        query = "select email,passwords from student where email='"+email+"'and passwords='"+passwords+"'"
        cur.execute(query)
        result =cur.fetchall()
        if len(result) == 0:
            return render_template("stulogins.html",message="password not matched")
        else:
            return render_template("libhomepage.html")

    return render_template("stulogins.html")

@app.route('/stusigns')

def studensignpage():

    return render_template("stusings.html")
@app.route("/tealogins",methods=['GET','POST'])

def teacherslogin():
    if request.method == 'POST':
        conn = sqlite3.connect('librarydatas.db')
        cur = conn.cursor()
        email = (request.form["email"])
        passwords = (request.form["passwords"])
        print(email,passwords)
        query = "select email,passwords from teacher where email='"+email+"'and passwords='"+passwords+"'"
        cur.execute(query)
        result =cur.fetchall()
        if len(result) == 0:
            return render_template("teacherslogin.html",message="password not matched")
        else:
            return render_template("libhomepage.html")
    return render_template("teacherslogin.html")

@app.route('/teasigns')

def teacherssignpage():


    return render_template("teacherssign.html")


@app.route('/studentdb',methods=['POST','GET'])
def studentdatas():

    conn = sqlite3.connect('librarydatas.db')
    cur=conn.cursor()
    if request.method == 'POST':
        a = (request.form["fname"])
        b = (request.form["lname"])
        c = (request.form ["gender"])
        d = (request.form["email"])
        e = (request.form["department"])
        f = (request.form["passwords"])
        sql = f"insert into student values('{a}','{b}','{c}','{d}','{e}','{f}')"
        print(sql)
        cur.execute(sql)
        conn.commit()
        cur.close()
        message = "SUCCESSFULLY REGISTERED"
    return render_template("messages.html",msg = message)

@app.route('/teacherdb',methods=['POST','GET'])
def teacherdatas():

    conn = sqlite3.connect('librarydatas.db')
    cur=conn.cursor()
    if request.method == 'POST':
        a = (request.form["fname"])
        b = (request.form["lname"])
        c = (request.form ["gender"])
        d = (request.form["email"])
        e = (request.form["department"])
        f = (request.form["passwords"])
        sql = f"insert into teacher values('{a}','{b}','{c}','{d}','{e}','{f}')"
        print(sql)
        cur.execute(sql)
        conn.commit()
        cur.close()
        message = "SUCCESSFULLY REGISTERED"
    return render_template("messages.html",msg = message)

@app.route('/viewstudents')

def studentview():
    conn=sqlite3.connect('librarydatas.db')
    cur=conn.cursor()
    sql = "select * from student"
    cur.execute(sql)
    rows=cur.fetchall()
    for a in rows:
        print(a)
    return render_template("viewstudentsrecord.html",rows=rows)

@app.route('/viewteachers')

def teacherview():
    conn = sqlite3.connect('librarydatas.db')
    cur=conn.cursor()
    sql = "select * from teacher"
    cur.execute(sql)
    rows = cur.fetchall()
    for a in rows:
        print(a)
    return render_template("viewteachersrecord.html",rows=rows)

@app.route('/main')
def mainpage():
    return render_template("homepages.html")

@app.route('/lihome')

def libhomespage():
    return render_template("libhomepage.html")

@app.route('/liabout')

def libaboutspage():
    return render_template("libaboutpage.html")

@app.route('/lilib')

def lilibpage():
    return render_template("librarypage.html")

@app.route('/book1')

def book1pages():
    return render_template("book1page.html")

@app.route('/book2')

def book2pages():
    return render_template("book2page.html")

@app.route('/book3')

def book3pages():
    return render_template("book3page.html")


if __name__ == '__main__':
    app.run(port=4000)

