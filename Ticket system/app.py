from flask import Flask
from flask import render_template
from flask import request

app= Flask(__name__)

@app.route("/login", methods=["GET","POST"])

def hi():
    if request.method =="GET":
        return  render_template("login.html")
    elif request.method == "POST":
        user_id=request.form["user_id"]
        return render_template("hi.html",name=user_id)
    else:
        print("ERROR")


if __name__=="__main__":
    app.debug=True
    app.run()