
                        {{ config(materialized='incremental',unique_key='f_intent_account_agg_key', schema='revature_dwh', alias ='f_intent_account_agg', post_hook=["delete from revature_dwh.f_intent_account_agg where datestamp < (select max(datestamp) -84 from revature_dwh.f_intent_account_agg) "]) }}                      
                        -- depends_on: { ref('f_intent_account_revature_dwh') }  
                        {{ f_intent_account_agg_macro(custom_schema='revature_dwh',table1='f_intent_account_revature_dwh') }}
                        