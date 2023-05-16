from sqlalchemy import create_engine, except_all
import json
import pyodbc
import pandas as pd
import statsmodels.api as sm
import pickle
import os
import warnings

warnings.filterwarnings('ignore')
from datetime import date
from datetime import datetime
from sklearn.preprocessing import PowerTransformer

from timeit import default_timer as timer
from datetime import timedelta
import numpy as np
import psycopg2
# project_path = ""

##################

###################

with open("./new_arch_tenant.json", "r") as f:
    tenant_info = json.load(f)["tenant_info"]

BASE_PATH = "/home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile/new_arch_setup"


####################


def get_db_creds(tenant_id):
    """ Based on tenant ID get DB Credentials"""

    db_creds = None

    for each_info in tenant_info:
    #    if each_info["tenant_id"] == tenant_id:
            db_creds = each_info
         #   break

    return db_creds


def create_db(db_creds):
    db_conn = None
    if db_creds is None:
        return None    
    
    db_create =  db_creds["db_create"]

    query= "CREATE DATABASE {};".format(db_create)
    
    try:
        db_conn = psycopg2.connect(database=db_creds["db_name"], user=db_creds["db_user"], password=db_creds["db_password"], host=db_creds["db_host"], port= db_creds["db_port"])
        db_conn.autocommit = True
        cursor = db_conn.cursor()
        cursor.execute(query)
        query = 'GRANT ALL PRIVILEGES ON DATABASE "{}" to postgres;'.format(db_create)
        
        db_conn.close()
        with open(BASE_PATH+"/logs.txt", "a") as f:
            f.write('Database created\n')
        return True
    except Exception as ex:
        
        if db_conn:
            db_conn.close()        
        with open(BASE_PATH+"/logs.txt", "a") as f:
            f.write(str(ex))
        return False

db_creds = get_db_creds("postgres")

with open(BASE_PATH+"/logs.txt", "a") as f:
    f.write("get_creds, Done\n")

create_db(db_creds)
with open(BASE_PATH+"/logs.txt", "a") as f:
    f.write("DB creation, Completed\n")

