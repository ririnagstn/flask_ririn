from flask import Flask,redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    x=15
    if(x>10):
      return redirect(url_for("lihat",xx=x))
    else:
      return f"<h1>HELLO WORLD {x} </h1>"

@app.route("/lihat")
def lihat():
    y=request.args.get("xx")
    return f"ini halaman yang berbeda {y}"

if (__name__=="__main__"):
    app.run(debug=True)