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
BASE_PATH = "/home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile"
PATH2="/home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile/new_arch_setup"

with open(BASE_PATH + "/multitenant.json", "r") as f:
    tenant_info = json.load(f)

def get_db_creds(tenant_id):
    """ Based on tenant ID get DB Credentials"""

    db_creds = None

    for each_info in tenant_info:
        if each_info["tenant_id"] == tenant_id:
            db_creds = each_info
            break
    return db_creds

    
def create_schema(db_creds):
    db_conn = None

    try:

        db_conn = psycopg2.connect(database=db_creds["db_database"], user=db_creds["db_username"], password=db_creds["db_password"], host=db_creds["db_host"], port= db_creds["db_port"])
        db_conn.autocommit = True
        cursor = db_conn.cursor()
        query= "CREATE SCHEMA "+ db_creds["db_schema"] + ";"
        cursor.execute(query)     

        with open(PATH2+"/logs_new_arch_schema.txt", "a") as f:
            f.write('Schema ' + db_creds["db_schema"] + ' created\n')
        
        db_conn.close()         
        return True

    except Exception as ex:
        with open(PATH2+"/logs_new_arch_schema.txt", "a") as f:
            f.write(str(ex))

        if db_conn:
            db_conn.close()
        return False

def create_table(db_creds):
    try:
        db_conn = psycopg2.connect(database=db_creds["db_database"], user=db_creds["db_username"], password=db_creds["db_password"], host=db_creds["db_host"], port= db_creds["db_port"])
        db_conn.autocommit = True
        cursor = db_conn.cursor()

        path=PATH2 + "/sql_queries"
        query=open(path + "/f_acc_topics.sql", "r").read()        
        query =  str(query)
        query = query.replace("dwh",db_creds["db_schema"])

        cursor.execute(query)  

        with open(PATH2+"/logs_new_arch_schema.txt", "a") as f:
            f.write('Table f_acc_topics created\n')

        db_conn.close()         
        return True

    except Exception as ex:
        with open(PATH2+"/logs_new_arch_schema.txt", "a") as f:
            f.write(str(ex))

        if db_conn:
            db_conn.close()
        return False

################################################

with open(PATH2+"/logs_new_arch_schema.txt", "w") as f:
        f.write("LOG STARTED \n\n")

list_tenantids=[]

for each_info in tenant_info:
    list_tenantids.append(each_info['tenant_id'])
# print(list_tenantids)

for tenantid in list_tenantids:
    db_creds = get_db_creds(tenantid)
    create_schema(db_creds)
    
    if db_creds['db_schema']!='bombora_dwh':
        create_table(db_creds)

    



