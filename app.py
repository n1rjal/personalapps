from flask import Flask, request,render_template
from getter import getdata
app=Flask(__name__)


@app.route("/",methods=['POST','GET'])
def home():
    if request.method=="GET":
        return render_template("index.html")
    
    if request.method=="POST":
        data=getdata()
        country=request.form['country']
        print(country)
        data=data[country]
        print(data)
        return render_template("index.html",data=data)

if __name__=="__main__":
    app.run(debug=False)