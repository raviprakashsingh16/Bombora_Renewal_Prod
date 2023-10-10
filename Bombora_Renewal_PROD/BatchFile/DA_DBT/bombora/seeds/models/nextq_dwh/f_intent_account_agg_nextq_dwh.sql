
                        {{ config(materialized='incremental', schema='nextq_dwh', alias ='f_intent_account_agg', post_hook=["delete from nextq_dwh.f_intent_account_agg where datestamp < (select max(datestamp) -56 from nextq_dwh.f_intent_account_agg) "]) }}                      
                        -- depends_on: { ref('f_intent_account_nextq_dwh') }  
                        {{ f_intent_account_agg_macro(custom_schema='nextq_dwh',table1='f_intent_account_nextq_dwh') }}
                        