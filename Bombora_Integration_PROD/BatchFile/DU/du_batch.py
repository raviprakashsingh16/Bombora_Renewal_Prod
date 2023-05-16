import os
import sys
import subprocess
from subprocess import PIPE, run
from datetime import date, datetime
import json


BASE_PATH = "/home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile"
BASE_PATH_DU = BASE_PATH + "/DU"
PATH_jsons = BASE_PATH + "/DA_DBT/"

# filename = BASE_PATH + "/db_connection_newdevhub_bombora.txt"

job_base_path = BASE_PATH_DU + "/f_intent_account_agg_to_surge_json_1.0"

batch_order = [
    "f_intent_account_agg_to_surge_json"

]

list_path_filenames  = []

with open(BASE_PATH + "/multitenant.json", "r") as f:
    tenant_info = json.load(f)
    for json_obj in tenant_info:
        if json_obj['tenant_id']!='bombora':
            filename=json_obj['tenant_id']+'.json'
            path_filename=os.path.join(PATH_jsons +  filename)
            list_path_filenames.append(path_filename)        
           

# print(len(list_path_filenames))

with open(BASE_PATH_DU+"/logs_f_intent_account_agg_to_surge_json.txt", "w") as f:
        f.write("LOG STARTED\n\n")


for filename in list_path_filenames:
    print(filename)
    a = datetime.now()
    
    context_param = [

    "--context_param filename={}".format(filename)

    ]

    ##########
    status = "Y"
    for each_order in batch_order:

        script_dir_path = job_base_path + "/{}".format(each_order)
        os.chdir(script_dir_path)

        command = [script_dir_path + "/{}_run.sh".format(each_order)] + context_param
    

        result = run(command, stdout=PIPE, stderr=PIPE, text=True)

        if result.returncode != 0:
            status = 'N'
            with open(BASE_PATH_DU + "/logs_f_intent_account_agg_to_surge_json.txt", "a") as f:
                f.write('\n\nFor filename: '+ str(filename) + '\n\n')
                f.write(str(result.returncode))
                f.write(str(result.stdout))
                f.write(str(result.stderr))
                f.write("Job Failed")
                b = datetime.now()
                print(b-a)
                

        else:
            with open(BASE_PATH_DU + "/logs_f_intent_account_agg_to_surge_json.txt", "a") as f:
                f.write('\n\nFor filename: '+ str(filename) + '\n\n')
                f.write(str(result.returncode))
                f.write(str(result.stdout))
                f.write(str(result.stderr))
                f.write("Job Completed")
                b = datetime.now()
                print(b-a)
            




# filename = BASE_PATH + "/db_connection_newdevhub_bombora.txt"

#job_base_path = BASE_PATH_DU + "/f_intent_lead_agg_to_sf_lead_json_1.0"
#
#batch_order = [
#    "f_intent_lead_agg_to_sf_lead_json"
#
#]
#
## list_path_filenames = []
## with open(BASE_PATH + "/multitenant.json", "r") as f:
##     tenant_info = json.load(f)
##     for json_obj in tenant_info:
##         if json_obj['tenant_id']!='bombora':
##             filename=json_obj['tenant_id']+'.json'
##             path_filename=os.path.join(BASE_PATH + '/DU/', filename)
##             list_path_filenames.append(path_filename)        
##             with open(path_filename, 'w') as out_json_file:
##                 json.dump(json_obj, out_json_file, indent=4)
#
## print(len(list_path_filenames))
#
#with open(BASE_PATH_DU +"/logs_f_intent_lead_agg_to_sf_lead_json.txt", "w") as f:
#        f.write("LOG STARTED\n\n")
#
#
#for filename in list_path_filenames:
#    print(filename)
#
#    a = datetime.now()
#
#    context_param = [
#
#    "--context_param filename={}".format(filename)
#
#    ]
#
#    ##########
#    status = "Y"
#    for each_order in batch_order:
#
#        script_dir_path = job_base_path + "/{}".format(each_order)
#        os.chdir(script_dir_path)
#
#        command = [script_dir_path + "/{}_run.sh".format(each_order)] + context_param
#    
#
#        result = run(command, stdout=PIPE, stderr=PIPE, text=True)
#
#        if result.returncode != 0:
#            status = 'N'
#            with open(BASE_PATH_DU +"/logs_f_intent_lead_agg_to_sf_lead_json.txt", "a") as f:
#                f.write('\n\nFor filename: '+ str(filename) + '\n\n')
#                f.write(str(result.returncode))
#                f.write(str(result.stdout))
#                f.write(str(result.stderr))
#                f.write("Job Failed")
#                b = datetime.now()
#                print(b-a)                
#
#        else:
#            with open( BASE_PATH_DU +"/logs_f_intent_lead_agg_to_sf_lead_json.txt", "a") as f:
#                f.write('\n\nFor filename: '+ str(filename) + '\n\n')
#                f.write(str(result.returncode))
#                f.write(str(result.stdout))
#                f.write(str(result.stderr))
#                f.write("Job Completed")
#                b = datetime.now()
#                print(b-a)
