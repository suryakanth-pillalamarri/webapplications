from flask import Flask,render_template

app=Flask(__name__)



@app.route("/")
def index():
    #return "Hello,krishna!!!!@"
    headline="Little about krishna"
    return render_template("hello.html",head_line=headline)

#@app.route("/<string:name>")


@app.route("/rama")
def rama():
    #name=name.capitalize()
    #return f"<h1>Hello, {name}!</h1>"*10
    return render_template("indexone.html")
    


@app.route("/avathar")
def avathar():
    return render_template("avathar.html")
