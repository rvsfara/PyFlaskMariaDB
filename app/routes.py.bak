from flask import render_template
from app import app
from app.frm_entry import EntryForm
@app.route("/")
@app.route("/index")
def index():
    form=EntryForm()
    return render_template("frm_entry.html",title="Entry and Result Form",formnya=form)