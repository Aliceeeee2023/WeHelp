from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session

app=Flask(__name__,static_folder="folder",static_url_path="/") 
app.secret_key="task4"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "test" and password == "test":
        session["SIGNED-IN"]=True
        return redirect("/member")
    else:
        session["SIGNED-IN"]=False
        return redirect("/")        

@app.route("/member")
def member():
    if session.get("SIGNED-IN"):
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/signout")
def signout():
    session.pop("SIGNED-IN", None)
    return redirect("/")

@app.route("/error")
def error():
    message=request.args.get("message")
    return render_template("error.html", message=message)
  
app.run(port=3000)
