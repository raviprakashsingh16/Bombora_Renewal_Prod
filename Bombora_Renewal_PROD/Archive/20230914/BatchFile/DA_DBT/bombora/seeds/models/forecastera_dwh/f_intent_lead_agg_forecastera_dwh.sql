
                        {{ config(materialized='incremental',unique_key='f_intent_lead_agg_key', schema='forecastera_dwh', alias ='f_intent_lead_agg', post_hook=["delete from forecastera_dwh.f_intent_lead_agg where datestamp < (select max(datestamp) -56 from forecastera_dwh.f_intent_lead_agg) " ,"update forecastera_dwh.loadexecution_detail set loadenddatetime =current_date, loadcomplete = 'y' where loadcomplete is null"]) }}                      
                        -- depends_on: { ref('f_intent_lead_forecastera_dwh') }  
                        {{ f_intent_lead_agg_macro(custom_schema='forecastera_dwh',table1='f_intent_lead_forecastera_dwh') }}
                        