
                        {{ config(materialized='table', schema='revature_dwh', alias ='f_intent_lead') }}                      
                        -- depends_on: { ref('f_bombora_select_topic_revature_dwh') }  
                        {{ f_intent_lead_macro(custom_schema='revature_dwh',table1='f_bombora_select_topic_revature_dwh') }}
                        