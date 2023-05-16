
                        {{ config(materialized='incremental', schema='revature_dwh', alias ='f_intent_lead_agg', post_hook=["delete from revature_dwh.f_intent_lead_agg where datestamp < (select max(datestamp) -56 from revature_dwh.f_intent_lead_agg) " ,"update revature_dwh.loadexecution_detail set loadenddatetime =current_date, loadcomplete = 'y' where loadcomplete is null"]) }}                      
                        -- depends_on: { ref('f_intent_lead_revature_dwh') }  
                        {{ f_intent_lead_agg_macro(custom_schema='revature_dwh',table1='f_intent_lead_revature_dwh') }}
                        