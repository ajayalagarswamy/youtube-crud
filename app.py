from flask import Flask,render_template
import sqlite3 as sql

app=Flask(__name__)

@app.route('/',methods=["POST","GET"])
def home():
    conn= sql.connect("youtube.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()  
    cur.execute("Select * from display")
    data=cur.fetchall()
    return render_template("index.html",thumbnaillist1=data)

if __name__=="__main__":
    app.run(debug=True)