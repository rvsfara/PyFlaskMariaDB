from flask import render_template, request, url_for, redirect
from flaskext.mysql import MySQL
from app import app
from app.frm_entry import EntryForm# Connecting database
app.config["MYSQL_DATABASE_HOST"]="localhost"
app.config["MYSQL_DATABASE_USER"]="root"
app.config["MYSQL_DATABASE_PASSWORD"]="opansan63"
app.config["MYSQL_DATABASE_DB"]="test"
app.config["MYSQL_PORT"]="3306"# Preparing variable on mysqlnya
mysqlnya=MySQL(app)
mysqlnya.init_app(app)@app.route("/")
def home():
    return render_template("home.html", title="Home")@app.route("/frm_entry", methods=["GET","POST"])
def frm_entry():
    resultnya=0
    rem=""
    xvalue_1=0
    xvalue_2=0
    xoperator=""    
    
    formnya=EntryForm()
    
    # Save inputted data to variables
    if request.method=="POST":
        details=request.form
        xvalue_1=details["value_1"]
        xvalue_2=details["value_2"]
        xoperator=details["operatornya"]
    
    # Processing result
    if xoperator=="+":
       resultnya=int(xvalue_1)+int(xvalue_2)
    elif xoperator=="-":
       resultnya=int(xvalue_1)-int(xvalue_2)
    elif xoperator=="/":
       resultnya=int(xvalue_1)/int(xvalue_2)
    elif xoperator=="*":
       resultnya=int(xvalue_1)*int(xvalue_2)    
   
    # Processing remarks, Even, Odd or Zero
    if resultnya==0:
        rem="Zero"
    elif resultnya % 2 ==0:    
        rem="Even"
    elif resultnya % 2==1:
         rem="Odd"    
    else:
        rem=""# Save data        
    cur=mysqlnya.connect().cursor()
    cur.execute("insert into penjumlahan (value_1,value_2,operator,result, remark) values (%s,%s,%s,%s,%s)",((xvalue_1,xvalue_2,xoperator,resultnya,rem)))
    cur.connection.commit()
    cur.close()
    
    return render_template("frm_entry.html", title="Nilai", formnya=formnya, xresultnya=resultnya, remnya=rem)