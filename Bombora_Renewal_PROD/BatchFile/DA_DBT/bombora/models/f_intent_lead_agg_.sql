
                        {{ config(materialized='incremental',unique_key='f_intent_lead_agg_key', schema='', alias ='f_intent_lead_agg', post_hook=["delete from .f_intent_lead_agg where datestamp < (select max(datestamp) -84 from .f_intent_lead_agg) " ,"update .loadexecution_detail set loadenddatetime =current_date, loadcomplete = 'y' where loadcomplete is null"]) }}                      
                        -- depends_on: { ref('f_intent_lead_') }  
                        {{ f_intent_lead_agg_macro(custom_schema='',table1='f_intent_lead_') }}
                        