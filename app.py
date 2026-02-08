from flask import Flask , request , render_template

app=Flask(__name__)


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

    def withinRange():
        valid=True
        for m in marks:
            if m<0 or m>100:
                valid=False
                raise ValueError("Marks are not in range")
        return valid
    

    
    def passing():
        pass_status=True
        for m in marks:
            if m<33:
                pass_status=False
                break;
        if pass_status:
            return "PASS"
        else :
            return "FAIL"
    
        
    
    def total_calculation():
        total=0
        for m in marks:
            total+=m
        return total
 
        

    def percentage():
        total_subjects=len(marks)
        percentage=(total/(total_subjects*100))*100
        return percentage
    
    
    try :
        rangeOrNot = withinRange()
        total_marks=total_calculation()
        percentage_marks=percentage()
        passedOrNot=passing()
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
            "total" : total_marks,
            "percentage" : percentage_marks,
            "result" : passedOrNot

        }
        return render_template("testing.html" , **context)

    except ValueError as e :
        return render_template("marks_error.html" , error=str(e))
    

if __name__ =="__main__":
    app.run(debug=True)
