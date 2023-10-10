
                        {{ config(materialized='incremental', schema='forecastera_dwh', alias ='f_intent_account_agg', post_hook=["delete from forecastera_dwh.f_intent_account_agg where datestamp < (select max(datestamp) -56 from forecastera_dwh.f_intent_account_agg) "]) }}                      
                        -- depends_on: { ref('f_intent_account_forecastera_dwh') }  
                        {{ f_intent_account_agg_macro(custom_schema='forecastera_dwh',table1='f_intent_account_forecastera_dwh') }}
                        