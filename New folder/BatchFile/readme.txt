Updates on Sep 18
1.) Added addCrdAWS,rmCrdAWS python scripts to access the db credentials from aws secret manager
2.) Updated kpi.py,kpi.json to create index in f_bombora_select_topic table to improve the performance
3.) Uploaded latest d_pre_loaded_topics seed file
*******************************************************************************************
DBT Updates on Jun 23
1.) Removed the fields "accountname","industry" from DA jobs as per Pythian requirement.Moved the old DA job to Archive  in folder 20230619

2.) Updated f_intent_account_macro to  populate the fields "accountname","industry" as '' null

3.)Updated the DU job as per AWS secret manger code from RM.

4.)Updated d_pre_loaded_topics with new file

****************************************************************************************
DBT Updates on Jun 15
1.) Updated topic_data with "converting ',' into '-' and converting delimiters(^) again into ','" 

2.)  Adding ','  at the end of Topic words for Single or Multiple Topics

3.) Removed the fields "accountnumber","ownership","description" from f_intent_account_macro as these are missing in NextQ

4.)Moved the old DA job to Archive  in folder 20230619

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
