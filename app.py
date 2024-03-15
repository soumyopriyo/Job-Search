#calling class flask
from flask import Flask, render_template,jsonify,request
from database import load_jobs_fromdb,load_job_fromdb,add_application_to_db


app=Flask(__name__)

@app.route("/") #or path
def job_search():
    jobs=load_jobs_fromdb()
    return render_template("home.html",jobs=jobs)

#return data a json
@app.route("/job/<int:id>")
def show_jobs(id):
    job=load_job_fromdb(id)
    if not job:
        return "Not Found", 404
    return render_template("jobdetails.html",job=job)

@app.route("/job/<int:id>/apply", methods=["POST"])
def apply_to_job(id):
    data = request.form
    job=load_job_fromdb(id)
    add_application_to_db(id,data)
    return render_template("applied.html",application=data,job=job)
    


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)