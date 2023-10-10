
import os
import sys
import subprocess
from subprocess import PIPE, run
from datetime import date, datetime
import json
import sys
from org_secret_mgr import list_path_filenames

a = datetime.now()
BASE_PATH = "/home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile"

# filename = BASE_PATH+ "/multitenant.json"

job_base_path =BASE_PATH+ "/DA_DBT/multitenatization_0.1"

batch_order = [
    "multitenatization"

]

# list_path_filenames = []
# with open(BASE_PATH + "/multitenant.json", "r") as f:
    # tenant_info = json.load(f)
    # for json_obj in tenant_info:
        # if json_obj['tenant_id']!='bombora':
            # filename=json_obj['tenant_id']+'.json'
            # path_filename=os.path.join(BASE_PATH + '/DA_DBT/', filename)
            # list_path_filenames.append(path_filename)        
            # with open(path_filename, 'w') as out_json_file:
                # json.dump(json_obj, out_json_file, indent=4)

# print(len(list_path_filenames))
os.system("python org_secret_mgr.py")
print(len(list_path_filenames))
with open(BASE_PATH+"/DA_DBT/logs_da.txt", "w") as f:
        f.write("LOG STARTED\n\n")
        
try:    
    if  sys.argv[1] != '':
        print('Following try path')
        n = sys.argv[1]
        folder=n+"_dwh"
        for filename in list_path_filenames:
         if n in filename:
            print(filename)
            context_param = [
                
             "--context_param filename={}".format(filename)
            ]
            # ##########
            status = "Y"
            # def run_job():
          
            for each_order in batch_order:
                script_dir_path = job_base_path + "/{}".format(each_order)
                os.chdir(script_dir_path)
    
                command = [script_dir_path + "/{}_run.sh".format(each_order)] + context_param
    
                print(command)
                result = run(command, stdout=PIPE, stderr=PIPE, text=True)
    
                if result.returncode != 0:
                    status = 'N'
                    with open(BASE_PATH+"/DA_DBT/logs_da.txt", "a") as f:
                        f.write('\nFor filename: '+ str(filename) + '\n\n')
                        f.write(str(result.returncode))
                        f.write(str(result.stdout))
                        f.write(str(result.stderr))
                        f.write("Job Failed")
                        b = datetime.now()
                        print(b-a)
                        
        
                else:
                    with open(BASE_PATH+"/DA_DBT/logs_da.txt", "a") as f:
                        f.write('\nFor filename: '+ str(filename) + '\n\n')
                        f.write(str(result.returncode))
                        f.write(str(result.stdout))
                        f.write(str(result.stderr))
                        f.write("Job Completed")
                        b = datetime.now()
                        print(b-a)
        print(os.getcwd())
        BASE_PATH = "/home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile/DA_DBT"
        #BASE_PATH=os.getcwd()
        os.chdir(BASE_PATH)
        kpi_file_path = os.path.join("src", "kpi.py")
        kpi_cmd = f'python {kpi_file_path}'
        p = subprocess.Popen(kpi_cmd, stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate() 
        print(out)

        os.chdir(BASE_PATH+"/bombora")
        print(os.getcwd())

        print(">>>>>>>>")

        os.chdir(BASE_PATH+"/bombora/models")

        print(os.getcwd())
        p = subprocess.Popen("dbt seed --profiles-dir /home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile/", stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate() 
        print(out,">>")
        with open(BASE_PATH+"/logs_seed.txt", "w") as f:
           f.write(str(out))
           f.write(str(err))
        BASE_PATH = "/home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile"
        with open(BASE_PATH + "/multitenant.json", "r") as f:
            tenant_obj = json.load(f)   
            for each_info in tenant_obj:
                if each_info["tenant_id"] == n:
                    print(each_info)
                    if each_info["lead"] == 'n' and each_info["account_surge"] == 'y':        
                        p = subprocess.Popen ("dbt run --exclude f_intent_lead_agg_"+folder+" f_intent_lead_"+folder+" --profiles-dir /home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile/ --models "+folder+".*", stdout=subprocess.PIPE, shell=True)
                        out, err = p.communicate()
                        print(p) 
                        with open(BASE_PATH+"/DA_DBT/logs_run_surge.txt", "a") as f:
                            f.write(str(out))
                            f.write(str(err))
                    elif each_info["lead"] == 'y' and each_info["account_surge"] == 'n':
                                p = subprocess.Popen ("dbt run --exclude f_intent_account_agg_"+folder+" f_intent_account_"+folder+" --profiles-dir /home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile/ --models "+folder+".*", stdout=subprocess.PIPE, shell=True)
                                out, err = p.communicate() 
                                with open(BASE_PATH+"/DA_DBT/logs_run_lead.txt", "a") as f:
                                    f.write(str(out))
                                    f.write(str(err))
                    else :
                        p = subprocess.Popen ("dbt run --profiles-dir /home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile/ --models "+folder+".*", stdout=subprocess.PIPE, shell=True)
                        out, err = p.communicate() 
                        with open(BASE_PATH+"/DA_DBT/logs_run_surge_lead.txt", "a") as f:
                            f.write(str(out))
                            f.write(str(err))
            
except IndexError as ex:
    print('Following exception path')
    for filename in list_path_filenames:
        print(filename)
        context_param = [
   
        "--context_param filename={}".format(filename)
   
        ]
        # ##########
        status = "Y"
        # def run_job():
   
        
   
        for each_order in batch_order:
        
            script_dir_path = job_base_path + "/{}".format(each_order)
            os.chdir(script_dir_path)
        
            command = [script_dir_path + "/{}_run.sh".format(each_order)] + context_param
        
            print(command)
            result = run(command, stdout=PIPE, stderr=PIPE, text=True)
        
            if result.returncode != 0:
                status = 'N'
                with open(BASE_PATH+"/DA_DBT/logs_da.txt", "a") as f:
                    f.write('\nFor filename: '+ str(filename) + '\n\n')
                    f.write(str(result.returncode))
                    f.write(str(result.stdout))
                    f.write(str(result.stderr))
                    f.write("Job Failed")
                    b = datetime.now()
                    print(b-a)
                        
        
            else:
                with open(BASE_PATH+"/DA_DBT/logs_da.txt", "a") as f:
                    f.write('\nFor filename: '+ str(filename) + '\n\n')
                    f.write(str(result.returncode))
                    f.write(str(result.stdout))
                    f.write(str(result.stderr))
                    f.write("Job Completed")
                    b = datetime.now()
                    print(b-a)
     
    print(os.getcwd())
    BASE_PATH = "/home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile/DA_DBT"
    #BASE_PATH=os.getcwd()
    os.chdir(BASE_PATH)
    kpi_file_path = os.path.join("src", "kpi.py")
    kpi_cmd = f'python {kpi_file_path}'
    p = subprocess.Popen(kpi_cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate() 
    print(out)

    os.chdir(BASE_PATH+"/bombora")
    print(os.getcwd())

    print(">>>>>>>>")

    os.chdir(BASE_PATH+"/bombora/models")

    print(os.getcwd())
    p = subprocess.Popen("dbt seed --profiles-dir /home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile/", stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate() 
    print(out,">>")
    with open(BASE_PATH+"/logs_seed.txt", "w") as f:
       f.write(str(out))
       f.write(str(err))
    BASE_PATH = "/home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile"
    with open(BASE_PATH + "/multitenant.json", "r") as f:
        list_path_filenames = []
        tenant_info = json.load(f)
        for each_info in tenant_info:
         if each_info['tenant_id']!='bombora':
            print(each_info)
            if each_info["lead"] == 'n' and each_info["account_surge"] == 'y':        
                p = subprocess.Popen ("dbt run --exclude f_intent_lead_agg_"+each_info['db_schema']+" f_intent_lead_"+each_info['db_schema']+" --profiles-dir /home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile/ --models "+each_info['db_schema']+".*", stdout=subprocess.PIPE, shell=True)
                out, err = p.communicate()
                print(p) 
                with open(BASE_PATH+"/DA_DBT/logs_run_surge.txt", "a") as f:
                    f.write(str(out))
                    f.write(str(err))
            elif each_info["lead"] == 'y' and each_info["account_surge"] == 'n':
                        p = subprocess.Popen ( "dbt run --exclude f_intent_account_agg_"+each_info['db_schema']+" f_intent_account_"+each_info['db_schema']+" --profiles-dir /home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile/ --models "+each_info['db_schema']+".*", stdout=subprocess.PIPE, shell=True)
                        out, err = p.communicate() 
                        with open(BASE_PATH+"/DA_DBT/logs_run_lead.txt", "a") as f:
                            f.write(str(out))
                            f.write(str(err))
            else :
                p = subprocess.Popen ("dbt run --profiles-dir /home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile/ --models "+each_info["db_schema"]+".*", stdout=subprocess.PIPE, shell=True)
                out, err = p.communicate() 
                with open(BASE_PATH+"/DA_DBT/logs_run_surge_lead.txt", "a") as f:
                    f.write(str(out))
                    f.write(str(err))