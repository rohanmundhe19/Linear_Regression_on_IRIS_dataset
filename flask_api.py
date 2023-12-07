from flask import Flask,request,render_template
from IRIS_Model.utils import Iris

app= Flask(__name__)
@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/sepallengthcalculator",methods=['POST'])
def sepallength():
    data=request.form

    sepalwidth=eval(data['sepalwidth'])
    petallength=eval(data['petallength'])
    petalwidth=eval(data['petalwidth'])
    species=data['species']

    obj=Iris(sepalwidth,petallength,petalwidth,species)
    output=obj.get_sepallength()
    return render_template("index.html",sepallength=output)

if __name__=='__main__':
    app.run(debug=True)