from flask import Flask, session
from markupsafe import escape
from flask import url_for
from flask import request
app = Flask(__name__)
from flask import render_template
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from flask import flash
import sys

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:12345@localhost/Test'
db=SQLAlchemy(app)
app.config['SECRET_KEY'] = 'AJDJRJS24$($(#$$33--'
from app import db
class People(db.Model):
    __tablename__='People'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
SECRET_KEY = 'the random string'
con = psycopg2.connect(database="Test", user="postgres", password="12345", host="127.0.0.1", port="5432")
cursor = con.cursor()
@app.route('/submit', methods=['GET','POST'])
def submit():

    if request.method=='POST':


        print("heloo")
        username =request.form['username']
        email=request.form['password']
  

        student=People(username,email)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('landing'))
    else:
         

        i=0
        i=i+1
        print(i)
        studentResult=db.session.query(People).filter(People.id==1)
        for result in studentResult:


            print(result.username)
        return render_template('login3.html')
        
    # return render_template('login3.html')


  

@app.route("/")
def index():


    #db.create_all()
    return redirect(url_for('login'))
if __name__ == '__main__':
    session['secrrt']='sec'
    db.create_all()
    app.run()
@app.route("/landing")
def landing():
    return render_template('landing.html')
# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {(name)}!"
# @app.route("/A.html")
# def home2():
#    return"<p>Hello, World</p>"
# @app.route("/boy/<path:name>")
# def fhunc1(name):
#     return f"hello world {escape(name)}"
   

# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login3')
# def login3():
#     return 'login'

# @app.route('/user/<username>')
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     x=url_for('profile', username='John Doe')
#     print(x)

# @app.route("/login1",methods=['GET','POST'])
# def fun1():
#     if request.method=='POST':
#         return login()
#     else:

#         return index()
# # @app.route("/login", methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':
# #         return do_the_login()
# #     else:
# #         return show_the_login_form()
   
# from flask import render_template

# #@app.route('/hello/')
# x=['saif','usama']
# y='amna'
# @app.route('/hello/')
# def hello():
#     print(x)
#     return render_template('hello.html', name1=x,name2=y)

@app.route("/home")
def home():
    return("logged in successfully")

@app.route('/login', methods=['GET', 'POST'])
def login():



    



    
    try:
        
        if request.method=='POST':
             
       
        
        #l='saif'
        # cursor.execute('select username from public."People" where username='saif' ')
        # result = cursor.fetchall()
        # print(result)
            studentResult=db.session.query(People).filter(People.username==request.form['username'])

            for i in studentResult:

                print(i)
                if request.form['username'] == i.username and request.form['password'] == i.email:
                

                    return redirect(url_for('landing'))
                else:
                   ('Incorrect Username or Password')
        else:




           
            return render_template('login2.html')
    except:
        return render_template('login2.html')
@app.route('/Delete', methods=['GET', 'POST'])
def Delete():



    



    
    try:
        
        if request.method=='POST':
             
       
        
        #l='saif'
        # cursor.execute('select username from public."People" where username='saif' ')
        # result = cursor.fetchall()
        # print(result)
            #db.session.delete(People).filter(People.username==request.form['username'])
            People.query.filter(People.username==request.form['username']).delete()
            db.session.commit()
            return redirect(url_for('landing'))

            
        else:




           
            return render_template('del.html')
    except:
        return render_template('login2.html')
@app.route('/update', methods=['GET', 'POST'])
def update():



    



    
    try:
        
        if request.method=='POST':
             
       
        
        #l='saif'
        # cursor.execute('select username from public."People" where username='saif' ')
        # result = cursor.fetchall()
        # print(result)
            #db.session.delete(People).filter(People.username==request.form['username'])
            users=People.query.filter(People.username==request.form['username'])
            # users.email="lk"
            # db.session.commit()
            # return(redirect(login))

            for i in users:
                print(i.username)
                i.email=request.form['password']
                
                db.session.commit()
                return redirect(url_for('landing'))
            
        else:




           
            return render_template('update.html')
    except:
        return render_template('login2.html')
@app.route('/Delete1', methods=['GET', 'POST'])
def Delete1():




    



    
    try:
        
        if request.method=='POST':

             
       
        
        #l='saif'
        # cursor.execute('select username from public."People" where username='saif' ')
        # result = cursor.fetchall()
        # print(result)
            #db.session.delete(People).filter(People.username==request.form['username'])
            print('post')
            cursor.execute('DELETE FROM public."People" WHERE username = %s', (request.form['username'],))
            # x=cursor.fetchone()
            # for i in x:
            #     print(i)
            # People.query.filter(People.username==request.form['username']).delete()
            # db.session.commit()
            return(redirect(login))

            
        else:




           
            return render_template('del.html')
    except:
        return render_template('login2.html')
    

   
    
    

  