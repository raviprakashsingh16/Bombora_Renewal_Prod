
                        {{ config(materialized='incremental',unique_key='f_intent_account_agg_key', schema='pythian_dwh', alias ='f_intent_account_agg', post_hook=["delete from pythian_dwh.f_intent_account_agg where datestamp < (select max(datestamp) -84 from pythian_dwh.f_intent_account_agg) "]) }}                      
                        -- depends_on: { ref('f_intent_account_pythian_dwh') }  
                        {{ f_intent_account_agg_macro(custom_schema='pythian_dwh',table1='f_intent_account_pythian_dwh') }}
                        