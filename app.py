import MySQLdb.cursors
from flask import Flask, render_template, url_for,  redirect, request, jsonify,json,session,flash
from flask_mysqldb import MySQL
from flask_login import LoginManager , UserMixin, login_user , login_required ,current_user, logout_user
import re
from flask_mail import Mail, Message
app = Flask(__name__)
leave_data=[]
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to the 'login' route if a user is not logged in

# Mock user data (replace with database queries)
class User(UserMixin):
    def __init__(self, name,id):
        self.id = name
        self.id = id

users = {'user1': {'password': 'password1'}, 'user2': {'password': 'password2'}}

@login_manager.user_loader
def load_user(name,id):
    return User(name,id)

@app.route('/userdashboard')
@login_required
def userdasboard():
    return render_template('userdashboad.html', user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Configure Flask-Mail settings
app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '62ff8857c4be36'
app.config['MAIL_PASSWORD'] = 'b7e1b286e040db'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False


mail = Mail(app)
# MySQL database connection
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "leave_managment"
app.config["MYSQL_PASSWORD"] = "Dhivya"
app.config["MYSQL_DB"] = "leave_mangement"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)

@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/get_user_data', methods=['POST'])
def get_user_data():
    if request.method == 'POST':
        userid = request.form['userid']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM leave_requests WHERE userid = %s", (userid,))
        user = cursor.fetchone()
        mysql.connection.commit()
        cursor.close()
        if user:
            return render_template('user_data.html', data=user)
        else:
            flash('User not found.', 'error')
            return redirect(url_for('index'))
#email sent
@app.route('/send_email')
def send_email():
       recipient = ["dhivyabharathin29@gmail.com"]
       subject = "test mail"
       message_body = "this is testing message. "

       msg = Message(subject=subject, sender="dhivyabharathi2923@gmail.com", recipients=["dhivyabharathin29@gmail.com"])
       msg.body = message_body

       try:
           mail.send(msg)
           return "email sent successfully !!"
       except Exception as e:
           return "error sending mail : "+ str(e)

#loading home pge
@app.route("/")
def dashboard():
    return render_template("dashboard.html")



@app.route("/adminpage")
def adminpage():
    return render_template("adminpage.html")

@app.route("/about")
def about():
    return render_template("about.html")

#contact page
@app.route("/contact")
def contact():
    return render_template("contact.html",)

#student register
@app.route("/register",methods=['GET','POST'])
def register():
    message = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['name']
        password = request.form['password']
        email = request.form['email']
        con = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        con.execute('select * FROM user WHERE email = % s',(email, ))
        sql = "insert into user (email, password) value (%s,%s)"
        account = con.fetchone()
        if account:
            message= 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            message ='invalid email address !'
        elif not email or not password:
            message ='please fill out the form !'
        else:
            con.execute('INSERT INTO user VALUES(NULL, % s,% s,% s)', (username, email, password, ))
            mysql.connection.commit()
            message = 'you have successfully registered !'
    elif request.method== 'POST':
        message = 'plese fill out the form !'
    return render_template('register.html',message = message)

#admin register
@app.route("/adminregister",methods=['GET','POST'])
def adminregister():
    message = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['name']
        password = request.form['password']
        email = request.form['email']
        con = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        con.execute('select * FROM admin WHERE email = % s',(email, ))
        sql = "insert into admin (email, password) value (%s,%s)"
        account = con.fetchone()
        if account:
            message= 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            message ='invalid email address !'
        elif not email or not password:
            message ='please fill out the form !'
        else:
            con.execute('INSERT INTO admin VALUES(NULL, % s,% s,% s)', (username, email, password, ))
            mysql.connection.commit()
            message = 'you have successfully registered !'
    elif request.method== 'POST':
        message = 'plese fill out the form !'
    return render_template('adminregister.html',message = message)

#student login
@app.route("/login", methods=['GET', 'POST'])
def login():
    message=''
    if request.method == 'POST' and 'userid' in request.form and 'name' in request.form and 'email' in request.form and 'password' in request.form :
        userid = request.form['userid']
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE userid = % s AND name = % s AND email = % s AND password = % s', (userid, name, email, password,))
        user = cursor.fetchone()
        if user:
            session['loggedin']= True
            session['name'] = user['name']
            session['email'] = user['email']
            session['password'] = user['password']
            message = 'logged in successfully !'
            return render_template('userdashboad.html',message=message,user=user)
        else:
            flash('Invalid credentials. Please try again.', 'danger')
            message = 'please enter correct email/ password !'

    return render_template('login.html', message=message)


#leave apply
@app.route("/leaveapply",methods=['GET','POST'])
def leaveapply():
    if request.method=='POST':
        leavetype=request.form['leavetype']
        start_date=request.form['start_date']
        end_date=request.form['end_date']
        reason=request.form['reason']
        leave_data.append({
            'id':id,
            'leavetype':leavetype,
            'start_date':start_date,
            'end_date':end_date,
            'reason':reason,
            'status':'pending'
        })
        con = mysql.connection.cursor()
        query="insert into leave_requests (leavetype,start_date,end_date,reason) value (%s,%s,%s,%s)"
        con.execute(query,[leavetype,start_date,end_date,reason])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("leave_status"))
    return render_template("leave_apply.html")


# leave status
@app.route('/status')
def leave_status():
    con1 = mysql.connection.cursor()
    select_query = "SELECT * FROM leave_requests"
    con1.execute(select_query)
    data = con1.fetchall()
    return render_template("leave_status.html", data = data)
'''@app.route('/leave/status')
def leave_status():
        if 'userid' in session:
            userid = session['userid']
            data = get_leave_status(userid)
            return render_template('leave_status.html', data=data)
def get_leave_status(userid):
    try:
        connection = mysql.connection.connect(app.config)
        cursor = connection.cursor()
        query = "SELECT * FROM leave_requests WHERE userid = %s"
        cursor.execute(query, (userid,))
        data = cursor.fetchall()
        return data

    except mysql.connection.Error as e:
        print("Database error:", e)
    finally:
        cursor.close()
        connection.close()

    return None
# Add a default response at the end
    return render_template('leave_status.html', data=[])'''

#admin login
@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    message=''
    if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'password' in request.form :
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM admin WHERE name = % s AND email = % s AND password = % s',(name,email,password,))
        user = cursor.fetchone()
        if user:
            session['loggedin']= True
            session['name'] = user['name']
            session['email'] = user['email']
            session['password'] = user['password']
            message = 'logged in successfully !'
            return render_template('adminpage.html',message=message)
        else:
            message = 'please enter correct email/ password !'

    return render_template('adminlogin.html', message=message)


#add student
@app.route("/addemployee",methods=['GET','POST'])
def addemployee():
    if request.method== 'POST':
        employee_name = request.form['employee_name']
        department = request.form['department']
        email = request.form['email']
        con = mysql.connection.cursor()
        sql = "insert into employeess (employee_name,department,email) value (%s,%s,%s)"
        con.execute(sql, [employee_name, department, email])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("view_student"))

    return render_template("add_employee.html")

#view student login
@app.route('/view_student_login',methods=['GET','POST'])
def view_student_login():
    con = mysql.connection.cursor()
    select_query = "SELECT * FROM user "
    con.execute(select_query)
    data = con.fetchall()
    return render_template("view_student_login.html", data = data)

#view student
@app.route('/view_student',methods=['GET','POST'])
def view_student():
    con = mysql.connection.cursor()
    select_query = "SELECT * FROM employeess "
    con.execute(select_query)
    data = con.fetchall()
    return render_template("view_student.html", data = data)
@app.route('/view_admin',methods=['GET','POST'])
def view_admin():
    con = mysql.connection.cursor()
    select_query = "SELECT * FROM admin "
    con.execute(select_query)
    data = con.fetchall()
    return render_template("view_admin.html", data = data)
#update user
@app.route("/edituser/<string:userid>",methods=['GET','POST'])
def edituser(userid):
    con = mysql.connection.cursor()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        sql = "update user set name=%s,email=%s  where userid=%s"
        con.execute(sql,[name,email,userid])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("view_student_login"))
        con = mysql.connection.cursor()
    sql = "select * from user where userid=%s"
    con.execute(sql, [userid])
    data = con.fetchone()
    return render_template("edituser.html",data=data)
@app.route("/edit_student/<string:id>",methods=['GET','POST'])
def edit_student(id):
    con = mysql.connection.cursor()
    if request.method == 'POST':
        employee_name = request.form['employee_name']
        department = request.form['department']
        email = request.form['email']
        sql = (f"update employeess set employee_name =%s,department=%s , email=%s  where id=%s")
        con.execute(sql,[employee_name,department,email,id])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("view_student"))
        con = mysql.connection.cursor()
    sql = "select * from employeess where id=%s"
    con.execute(sql, [id])
    data = con.fetchone()
    return render_template("edit_student.html",data=data)

@app.route("/passsword_change/<string:id>",methods=['GET','POST'])
def password_change(id):
    con = mysql.connection.cursor()
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        password = request.form['password']
        sql = "update admin set name=%s,password=%s,password=%s where id=%s"
        con.execute(sql,[name,password,password,id])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("view_admin"))
        con = mysql.connection.cursor()
    sql = "select * from admin where id=%s"
    con.execute(sql, [id])
    data = con.fetchone()
    return render_template("password_change.html",data=data)
#delete student
@app.route("/delet_student/<string:id>",methods=['GET','POST'])
def delete_student(id):
    con=mysql.connection.cursor()
    sql = "delete from employeess where id=%s"
    con.execute(sql, [id])
    res=con.fetchone()
    mysql.connection.commit()
    con.close()
    flash("user detailes deleted")
    return redirect(url_for("view_student",data=res))
#delete user
@app.route("/deleteuser/<string:userid>",methods=['GET','POST'])
def deleteuser(userid):
    con=mysql.connection.cursor()
    sql = "delete from user where userid=%s"
    con.execute(sql, [userid])
    res=con.fetchone()
    mysql.connection.commit()
    con.close()
    flash("user detailes deleted")
    return redirect(url_for("view_student_login",data=res))
@app.route("/deleteleave/<string:request_id>",methods=['GET','POST'])
def deleteleave(request_id):
    con=mysql.connection.cursor()
    sql = "delete from leave_requests where request_id=%s"
    con.execute(sql, [request_id])
    res=con.fetchone()
    mysql.connection.commit()
    con.close()
    flash("user detailes deleted")
    return redirect(url_for("leave_status",data=res))





#hod dashboard
@app.route('/hod_dashboard',methods=['GET','POST'])
def hod_dashboard():
        con = mysql.connection.cursor()
        sql = "SELECT * FROM leave_requests"
        con.execute(sql)
        data= con.fetchall()
        return render_template('hod_dashboard.html',data = data)



#leave approvel
@app.route('/approve/<int:request_id>',methods=['GET','POST'])
def approve(request_id):
    # Update the status of the leave request to 'approved'
    con = mysql.connection.cursor()
    con.execute(f"UPDATE leave_requests SET status='approved' WHERE request_id={request_id}")
    mysql.connection.commit()
    con.close()
    return redirect(url_for("leave_status"))


#leave reject
@app.route('/reject/<int:request_id>',methods=['GET','POST'])
def reject(request_id):
    # Update the status of the leave request to 'rejected'
    con = mysql.connection.cursor()
    con.execute(f"UPDATE leave_requests SET status='rejected' WHERE request_id={request_id}")
    mysql.connection.commit()
    con.close()
    return redirect(url_for("leave_status"))


#view approvel
@app.route('/viewapprove',methods=['GET','POST'])
def viewapprovel():
    con = mysql.connection.cursor()
    select_query = "SELECT * FROM leave_requests where status like '%approved%'"
    con.execute(select_query)
    result1 = con.fetchall()
    return render_template("leave_status.html", data = result1)


#view reject
@app.route('/viewreject',methods=['GET','POST'])
def viewreject():
    con1 = mysql.connection.cursor()
    select_query = "SELECT * FROM leave_requests where status like '%rejected%'"
    con1.execute(select_query)
    result1 = con1.fetchall()
    return render_template("leave_status.html", data = result1)


if __name__ == '__main__':
    app.secret_key="abc123"
    app.run(debug=True)
