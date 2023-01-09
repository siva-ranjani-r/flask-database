from flask import Flask,render_template,redirect,request
import requests
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
def home():
    conn =sql.connect('user.db')
    conn.row_factory = sql.Row
    cur =conn.cursor()

    cur.execute("SELECT * FROM post")
    data =cur.fetchall()

    return render_template("index.html",data=data)



if __name__=='__main__':
    app.run(debug=True)