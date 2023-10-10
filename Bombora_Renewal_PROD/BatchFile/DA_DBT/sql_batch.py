import json
from sqlalchemy import create_engine
import os
import psycopg2
from sqlalchemy import text

BASE_PATH = "/home/ubuntu/appdata/Bombora_Renewal_PROD/BatchFile"
PATH2= "/home/ubuntu/appdata/Bombora_Renewal_PROD/BatchFile/DA_DBT"

with open(BASE_PATH + "/multitenant.json", "r") as f:
    tenant_info = json.load(f)

def get_db_creds(tenantid):
    """ Based on tenant ID get DB Credentials"""
    db_creds = None
    for each_info in tenant_info:
        if each_info['tenant_id'] == tenantid:
            db_creds = each_info
            break
    return db_creds

# def get_db_engine(db_creds):
#     if db_creds is None:
#         return None

#     # TODO: Handle DSN later
#     etl_engine = create_engine(
#         'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(db_creds["db_username"], db_creds["db_password"], db_creds["db_host"],
#                                                       db_creds["db_port"], db_creds["db_database"]))    
#     return etl_engine

def updateToDB(db_creds):
    db_conn = None

    try:
        db_conn = psycopg2.connect(database=db_creds["db_database"], user=db_creds["db_username"], password=db_creds["db_password"],\
             host=db_creds["db_host"], port= db_creds["db_port"])
        db_conn.autocommit = True
        cnx = db_conn.cursor()

    # with db_engine.connect() as cnx:
        # cnx.execute("CREATE TABLE IF NOT EXISTS dwh.f_adat_bombora (company character varying(64) ,domain character varying(50),size character varying(50) ,industry character varying(64) ,category character varying(50) ,topic character varying(50) ,composite_score integer,bucket_code character varying(50) ,metro_area character varying(50) ,metro_composite_score integer,metro_bucket_code character varying(50) ,domain_origin character varying(50) ,date_stamp integer)")
        # cnx.execute("CREATE TABLE IF NOT EXISTS dwh.f_acc_topics (accountid varchar(18) NULL, accountname varchar(255) NULL, userid varchar(18) NULL, theme varchar(1024) NULL, category varchar(255) NULL, topic varchar(255) NULL, \"cluster\" varchar(255) NULL )")
        # cnx.execute("create index IF NOT EXISTS idx_f_adat_bombora_topic on \"dwh\".\"f_adat_bombora\"(topic)")
        path=PATH2 + "/sql_queries"
        print(path)

        try :
            cnx.execute("CREATE EXTENSION if not exists aws_s3 CASCADE")
            with open(PATH2+"/logs_sql_batch.txt", "a") as f:
                f.write('aws_s3 created\n') 
        except Exception as ex:
            print("aws_s3 failed")
            with open(PATH2+"/logs_sql_batch.txt", "a") as f:
                f.write(str(ex)) 

        try :
            cnx.execute(open(path + "/f_adat_bombora.sql", "r").read())
            with open(PATH2+"/logs_sql_batch.txt", "a") as f:
                f.write('f_adat_bombora creation, Done\n') 
        except Exception as ex:
            print("f_adat_bombora failed")
            with open(PATH2+"/logs_sql_batch.txt", "a") as f:
                f.write(str(ex))

        #cnx.execute(open(path + "/f_acc_topics.sql", "r").read())

        try:
            cnx.execute(open(path + "/drop_idx_f_adat_bombora_topic.sql", "r").read())
            with open(PATH2+"/logs_sql_batch.txt", "a") as f:
                f.write('drop_idx_f_adat_bombora_topic, Done\n') 
        except Exception as ex:
            print("drop_idx_f_adat_bombora_topic failed")
            with open(PATH2+"/logs_sql_batch.txt", "a") as f:
                f.write(str(ex))

        try :
            cnx.execute(open(path + "/file_load.sql", "r").read())
            with open(PATH2+"/logs_sql_batch.txt", "a") as f:
                f.write('Bombora file loading, Done\n')   
        except Exception as ex:
            print("Bombora file loading failed")
            with open(PATH2+"/logs_sql_batch.txt", "a") as f:
                f.write(str(ex))
        
        try:
            cnx.execute(open(path + "/idx_f_adat_bombora_topic.sql", "r").read())  
            with open(PATH2+"/logs_sql_batch.txt", "a") as f:
                f.write('idx_f_adat_bombora_topic , Done\n')   
        except Exception as ex:
            print("idx_f_adat_bombora_topic failed")
            with open(PATH2+"/logs_sql_batch.txt", "a") as f:
                f.write(str(ex))
    
    except Exception as ex:
        print("Outer Exception")
        with open(PATH2+"/logs_sql_batch.txt", "a") as f:
            f.write(str(ex))

    cnx.close()


#####
list_tenantids=[]

for each_info in tenant_info:
    list_tenantids.append(each_info['tenant_id'])
# print(list_tenantids)

with open(PATH2+"/logs_sql_batch.txt", "w") as f:
    f.write('LOG STARTED\n\n') 

for tenantid in list_tenantids:
    
    
    if tenantid=='bombora':
        # print(tenantid)  
        # with open(PATH2+"/logs_sql_batch.txt", "a") as f:
        #     f.write(str(tenantid) + '\n\n')  
        db_creds = get_db_creds(tenantid)
        print("get_creds, Done")
        # db_engine = get_db_engine(db_creds)
        # print("db_engine, Done")
        updateToDB(db_creds)
        print("updateToDB, Done")


