#this includes all the queries
import sys
import json
import os
from dotenv import load_dotenv
from pandas import notnull
load_dotenv("//../")
#from config import settings,newsettings,BASE_PATH
import pydash as p_
#from config import BASE_PATH
from json import loads, load
import subprocess
from subprocess import PIPE, run
from datetime import date, datetime
import json

modelDir:str = "/home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile/DA_DBT/bombora/models"
with open("/home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile/multitenant.json") as tenantfile:
    json_settings = json.load(tenantfile)
    #print(json_settings)
    for elem in json_settings:
          for key, value in elem.items():
            if key=='db_schema' and value != 'bombora_dwh':
              folder_name= value
              #print(folder_name)
              path = os.path.join(modelDir, folder_name)
              #print(path)
              os.makedirs(path, exist_ok=True)
              with open("/home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile/DA_DBT/src/kpi.json") as file:
                kpi_settings = json.load(file)
                #print(kpi_settings)
                for w in kpi_settings:
                  #print(w.macro)
                  for key, value in w.items():
                   
                    if key== 'model':
                      model=value
                      print(model)
                    elif key== 'macro':
                      macro=value
                    elif key== 'materialized':
                      materialized=value
                    elif key== 'param':
                      param=value
                    elif key== 'history':
                      history=value
                    elif key == 'posthook' :
                      posthook = value
                      if len(param) >1 :                       
                        dependency=f'''-- depends_on: {{ ref('{param}_{folder_name}') }}  '''
                      else :
                        dependency =''
                      if  history >0 and posthook== 'y' :
                        modelString:str = f'''
                        {{{{ config(materialized='{materialized}', schema='{folder_name}', alias ='{model}', post_hook=["delete from {folder_name}.{model} where datestamp < (select max(datestamp) -56 from {folder_name}.{model}) " ,"update {folder_name}.loadexecution_detail set loadenddatetime =current_date, loadcomplete = 'y' where loadcomplete is null"]) }}}}                      
                        {dependency}
                        {{{{ {macro}(custom_schema='{folder_name}',table1='{param}_{folder_name}') }}}}
                        '''
                        with open(f"{path}/{model}_{folder_name}.sql", "w") as f:
                          f.write(modelString) 
                       
                      elif history >0 and posthook != 'y' :
                        modelString:str = f'''
                        {{{{ config(materialized='{materialized}', schema='{folder_name}', alias ='{model}', post_hook=["delete from {folder_name}.{model} where datestamp < (select max(datestamp) -56 from {folder_name}.{model}) "]) }}}}                      
                        {dependency}
                        {{{{ {macro}(custom_schema='{folder_name}',table1='{param}_{folder_name}') }}}}
                        '''
                        with open(f"{path}/{model}_{folder_name}.sql", "w") as f:
                          f.write(modelString) 
                      else :
                        modelString:str = f'''
                        {{{{ config(materialized='{materialized}', schema='{folder_name}', alias ='{model}') }}}}                      
                        {dependency}
                        {{{{ {macro}(custom_schema='{folder_name}',table1='{param}_{folder_name}') }}}}
                        '''
                        with open(f"{path}/{model}_{folder_name}.sql", "w") as f:
                          f.write(modelString) 
                      #print(modelString)
                        

#pydantic models to represent mixer json structure
# class Recp(BaseModel):
    # model:str
    # macro:str
   
# class RecpList(BaseModel):
  # __root__:List[Recp] = []

# BASE_PATH = os.getcwd()
  
# #load the jsons. once we load the json it confirms the json structure is valie
# #mixers:MixerList = parse_file_as(MixerList,f"{BASE_PATH}/metadata/mixer.json") 
# recps:RecpList = parse_file_as(RecpList,f"{settings.jsonDir}/kpi.json")

# def buildModels()->None:
  # for recp in recps.__root__:
    
    # params:List[str] = []
    # for k, v in recp.params.items():
      # value_type = type(v)
      # if value_type is list:
        # params.append(f'{k}={v}')
      # else:
        # params.append(f'{k}=\'{v}\'')
    # paramsStr:str = ' , '.join(params)
    # #build the model string then write 
    # paramsStr = paramsStr + f', key_column=\'{recp.model}_key\''
    # modelString:str = f'''
    # {{{{ config(materialized='table', schema='{recp.target}') }}}}
      # {{{{ {recp.macro}( {paramsStr} ) }}}}
    # '''
    # with open(f"{newsettings.modelDir}/{recp.model}.sql", "w") as f:
      # f.write(modelString)
  
# def runModels()->None:
  # return
# def testBuildModels()->None:
  # buildModels()
  # return

# if __name__ == '__main__':
  # testBuildModels()

  # print (f"{BASE_PATH}/metadata/mixer.json")
  # with open(f"{BASE_PATH}/metadata/mixer.json", "r") as f:
  #   print(f.read())
