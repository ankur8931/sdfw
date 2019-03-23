from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sdfw/")
def sdfw():
    return render_template('test.html')

if __name__=="__main__":
   app.run(host='0.0.0.0', port=80)
