from flask import Flask, request, redirect, render_template, session
import mysql.connector, json

con = mysql.connector.connect(
    user="root",
    password="123456",
    host="localhost",
    database="website"
)

app = Flask( __name__, static_folder="folder", static_url_path="/") 
app.secret_key = "week6"

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/signup", methods=["POST"])
def signup():
    cursor = con.cursor()

    name = request.form["signup_name"]
    username = request.form["signup_username"]
    password = request.form["signup_password"]

    cursor.execute("SELECT username FROM member WHERE username=%s", (username,))
    data = cursor.fetchone()

    if data is None:
        cursor.execute("INSERT INTO member (name, username, password) VALUES(%s, %s, %s)", (name, username, password))
        con.commit()

        return redirect("/")        
    else:
        return redirect("/error?message=帳號已經被註冊")

@app.route("/signin", methods=["POST"])
def signin():
    cursor = con.cursor()

    checkUsername = request.form["signin_username"]
    checkPassword = request.form["signin_password"]

    cursor.execute("SELECT id, name, username, password FROM member WHERE username=%s", (checkUsername,))
    data = cursor.fetchone()

    if data is None:
        return redirect("/error?message=帳號或密碼輸入錯誤") 
    else:
        id, name, username, password = data
        
        if password != checkPassword:
            return redirect("/error?message=帳號或密碼輸入錯誤") 
        else:            
            session["userId"] = id       
            session["name"] = name   
            session["userName"] = username
            session["userPassword"] = password
            session["signIn"] = True
            return redirect("/member")

@app.route("/signout")
def signout():
    session.pop("signIn", None)
    return redirect("/")

@app.route("/member")
def member():
    if session.get("signIn"):
        cursor = con.cursor()
        cursor.execute("SELECT name, content FROM message INNER JOIN member ON message.member_id=member.id ORDER BY message.time DESC")
        data = cursor.fetchall()

        nameData = []
        contentData = []

        for name, content in data:
            nameData.append(name)
            contentData.append(content)

        nameJson = json.dumps(nameData)
        contentJson = json.dumps(contentData)

        name = session["name"]
        return render_template("member.html", name=name, nameJson=nameJson, contentJson=contentJson)
    else:
        return redirect("/")

@app.route("/createMessage", methods=["POST"])
def createMessage():
    cursor = con.cursor()

    id = session["userId"]
    message = request.form["message"]

    cursor.execute("INSERT INTO message (member_id, content) VALUES(%s, %s)", (id, message))
    con.commit()
    
    return redirect("/member")

@app.route("/error")
def error():
    message = request.args.get("message")
    return render_template("error.html", message=message)

app.run(port=3000)
