from flask import Flask,render_template,redirect,request
import sqlite3 as sql

app = Flask(__name__)

# @app.route("/")
# def home():
#     conn =sql.connect('user.db')
#     conn.row_factory = sql.Row
#     cur =conn.cursor()

#     cur.execute("SELECT * FROM post")
#     data =cur.fetchall()

#     return render_template("index.html",data=data)


@app.route("/",methods=['POST','GET'])
def function():
    id=request.form.get("scheme_code")
    conn=sql.connect("fund.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("Select * from money where scheme_code=?",(id,))
    data=cur.fetchall()
    return render_template("fund.html",data=data)




if __name__=='__main__':
    app.run(debug=True)