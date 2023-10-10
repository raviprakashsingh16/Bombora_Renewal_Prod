Updates on Sep 18
1.) Added addCrdAWS,rmCrdAWS python scripts to access the db credentials from aws secret manager
2.) Updated kpi.py,kpi.json to create index in f_bombora_select_topic table to improve the performance
3.) Uploaded latest d_pre_loaded_topics seed file
****************************************************************************
Sep5 - DBT Update
1.) Updated 2 new files addCrdAWS,rmCrdAWS for a error
********************************************************************************
Sep4 - DBT Update
1.) Add 2 new files addCrdAWS,rmCrdAWS to add and remove db credentials in new_archtenant.json,multi_tenant.json,profiles.yml
********************************************************************************
Aug29 - DBT Update
1.) Updated da_dbt_batch.py for logger updation
********************************************************************************
Jul7 -DBT Update
1.) Added column id,cluster_initial as per UI in f_acc_topics manually and updated the f_acc_topics.sql
2.) cluster_initial is updated in f_intent_account_agg_macro,f_bombora_select_topic_macro
********************************************************************************
June 28-  update
1.) Updated DA ,DBT to sync PROD code to remove the unwanted fields(industry,accountname,description,ownership,accountnumber)
2.) Updated DBT to include cluste_type in (f_intent_account_agg_macro,f_bombora_select_topic_macro
3.) Updated DU (f_intent_account_agg_to_surge_json)job added a new field cluster_type,cluster of f_intent_account_agg table  mapped to FCSTSales__NQ_Cluster_Type__c ,FCSTSales__NQ_Cluster_Name__c fields in FCSTSales__NQ_Company_Surge__c object  

********************************************************************************
June 25- DBT update
Removed the = sign in "if current_date <= v_next_datestamp" condition of file_load.sql
************************************************************************************
In F_acc_topic - field size 0increased to 1000 
****************************************************************************************
Bombora_integration BatchFile latest code repository (25-May-2023) updates: 

1.) DU as per Configuration (Account/Lead/Both) 
	components impacted is du_batch.py and multitenant.json added new objects account_surge='y' & lead ='y' added

2.) DBT as per Configuration (Account/Lead/Both)  
	components impacted is da_dbt_batch.py and modified according to new features 

3.) Client specific batch execution (DA and DBT passing tenantID and executing run_batch.bat). 
	components impacted is run_batch.bat.

4.) Accessing confidential information from Vault/AWS Secret Manager (especially Salesforce connected app). 
	components impacted is da_dbt_batch.py 

5.) Removing Json files in DA_DBT folder after completion of DU jobs 
	components impacted is du_batch.py and modified according to new features 


6.) American Eagle Outfitters" in "Industry" Cluster showing multiple times in Revature

7.) inside the kpi.py added uniquekey was added 

8.) added REGEXP_REPLACE(REGEXP_REPLACE(REGEXP_REPLACE(a."website",'https://',''),'http://',''),'www.','')) in   f_intent_account_macro

9.) Handling the scenario if running the batch file multiple times in the same week

****************************************************************************************