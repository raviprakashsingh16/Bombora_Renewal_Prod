import json
from sqlalchemy import create_engine
import os

with open("E:/Bombora/DA_DBT/tenant_info.json", "r") as f:
    tenant_info = json.load(f)["tenant_info"]

def get_db_creds():
    """ Based on tenant ID get DB Credentials"""
    db_creds = None
    for each_info in tenant_info:
            db_creds = each_info
            break
    return db_creds

def get_db_engine(db_creds):
    if db_creds is None:
        return None

    # TODO: Handle DSN later
    etl_engine = create_engine(
        'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(db_creds["db_user"], db_creds["db_password"], db_creds["db_host"],
                                                      db_creds["db_port"], db_creds["db_name"]))    
    return etl_engine

def updateToDB(db_engine):
    
    with db_engine.connect() as cnx:
        # cnx.execute("CREATE OR REPLACE VIEW aiml.v_pre_loaded_topics AS WITH v_pre_loaded_topics AS (SELECT d_pre_loaded_topics.topic_id, d_pre_loaded_topics.theme, d_pre_loaded_topics.category, d_pre_loaded_topics.topic_name, d_pre_loaded_topics.description FROM dwh.d_pre_loaded_topics) SELECT v_pre_loaded_topics.topic_id, v_pre_loaded_topics.theme, v_pre_loaded_topics.category, v_pre_loaded_topics.topic_name, v_pre_loaded_topics.description FROM v_pre_loaded_topics")
        path=os.getcwd() + "/sql_queries"
        cnx.execute(open(path + "/v_pre_loaded_topics.sql", "r").read()) 
        print("view_completed")
    cnx.close()


#####


db_creds = get_db_creds()
print("get_creds, Done")
db_engine = get_db_engine(db_creds)
print("db_engine, Done")

updateToDB(db_engine)
print("updateToDB, Done")
