
                        {{ config(materialized='incremental',unique_key='f_intent_account_agg_key', schema='', alias ='f_intent_account_agg', post_hook=["delete from .f_intent_account_agg where datestamp < (select max(datestamp) -84 from .f_intent_account_agg) "]) }}                      
                        -- depends_on: { ref('f_intent_account_') }  
                        {{ f_intent_account_agg_macro(custom_schema='',table1='f_intent_account_') }}
                        