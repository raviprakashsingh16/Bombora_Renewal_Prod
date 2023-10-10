
                        {{ config(materialized='incremental',unique_key='f_intent_lead_agg_key', schema='pythian_dwh', alias ='f_intent_lead_agg', post_hook=["delete from pythian_dwh.f_intent_lead_agg where datestamp < (select max(datestamp) -84 from pythian_dwh.f_intent_lead_agg) " ,"update pythian_dwh.loadexecution_detail set loadenddatetime =current_date, loadcomplete = 'y' where loadcomplete is null"]) }}                      
                        -- depends_on: { ref('f_intent_lead_pythian_dwh') }  
                        {{ f_intent_lead_agg_macro(custom_schema='pythian_dwh',table1='f_intent_lead_pythian_dwh') }}
                        