from flask import Flask , request , render_template
from datetime import datetime
import sqlite3


app=Flask(__name__)


def init_db():
    conn =  sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT , 
            name TEXT,    
            reg TEXT UNIQUE,
            english REAL,
            hindi REAL,
            physics REAL,
            chemistry REAL,
            biology REAL,
            total REAL,
            percentage REAL,
            passfail TEXT ,
            created_at TEXT
        )
    """)
    conn.commit()
    conn.close()






@app.route("/")
def index():
    return render_template("jinja.html")



@app.route("/result" , methods=['POST'])
def result():
    form=request.form
    subjects=["english","hindi","physics","chemistry" ,"biology"]
    marks=[]
    for s in subjects:
        marks.append(float(form.get(s)))
    total=sum(marks)

    
    try :
        withinRange(marks)
        percentage_marks=percentage(marks , total)
        passedOrNot=passing(marks)
        context={
            "name" : form.get("name"),
            "reg"  : form.get("reg"),
            "marks" : {
                subjects[0] : marks[0],
                subjects[1] : marks[1],
                subjects[2] : marks[2],
                subjects[3] : marks[3],
                subjects[4] : marks[4],

            },
            "total" : total,
            "percentage" : percentage_marks,
            "passfail" : passedOrNot

        }

        with sqlite3.connect("students.db") as conn:
            cursor = conn.cursor()

            cursor.execute("""
            INSERT INTO students
            (name , reg , english , hindi , physics , chemistry , biology , total , percentage, passfail , created_at )
            VALUES(?,?,?,?,?,?,?,?,?,?,?)""" , 

            (
                form.get("name"),
                form.get("reg"),
                marks[0],
                marks[1],
                marks[2],
                marks[3],
                marks[4],
                total,
                percentage_marks,
                passedOrNot,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            ))
            conn.commit()
    
        return render_template("testing.html" , **context)

    except ValueError as e :
        return render_template("marks_error.html" , error=str(e))

@app.route("/history")
def history():
    with sqlite3.connect("students.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall() 
    
    return render_template("history.html" , students=students)


def withinRange(marks):
    for m in marks:
        if m<0 or m>100:
            raise ValueError("Marks are not in range")
    



def passing(marks):
    for m in marks:
        if m<33:
            return "FAIL"
    return "PASS"

    

def percentage(marks , total):
    total_subjects=len(marks)
    percentage=(total/(total_subjects*100))*100
    return percentage

if __name__ =="__main__":
    init_db();
    app.run(debug=True)