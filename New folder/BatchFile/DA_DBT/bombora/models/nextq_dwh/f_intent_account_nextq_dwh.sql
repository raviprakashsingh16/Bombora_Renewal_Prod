
                        {{ config(materialized='table', schema='nextq_dwh', alias ='f_intent_account') }}                      
                        -- depends_on: { ref('f_bombora_select_topic_nextq_dwh') }  
                        {{ f_intent_account_macro(custom_schema='nextq_dwh',table1='f_bombora_select_topic_nextq_dwh') }}
                        