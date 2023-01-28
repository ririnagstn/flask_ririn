from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route("/home")
def awal():
    return render_template("index.html", a="Selamat Malam")

if (__name__=="__main__"):
    app.run(debug=True)