from sqlalchemy import create_engine,text,Insert
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

engine_name=os.getenv("engine")
engine= create_engine(engine_name,pool_pre_ping=True)

def load_jobs_fromdb():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        result_dicts=[]
        for row in result.all():
        #dict() is unable to convert the table data from list to dict (giving sequence element #0 unable to convert)so we need to use _asdict() as it will be able to do the conversions
            result_dicts.append(row._asdict())
        return result_dicts


def load_job_fromdb(id):
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM jobs WHERE id = :val"),{"val": id})
        rows = result.mappings().all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])
    

def add_application_to_db(job_id, data):
   with engine.connect() as conn:
        query = text(
            f"INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES ({job_id}, '{data['full_name']}', '{data['email']}', '{data['linkedin_url']}', '{data['education']}', '{data['work_experience']}', '{data['resume_url']}')")
        conn.execute(query)
    
    
# def add_application_to_db(job_id,data):
#   with engine.connect() as conn:
#     query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url)"
#                  " VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

#     conn.execute(query,
#                  job_id=job_id,
#                  full_name=data['full_name'],
#                  email=data['email'],
#                  linkedin_url=data['linkedin_url'],
#                  education=data['education'],
#                  work_experience=data['work_experience'],
#                  resume_url=data['resume_url'])
