
                        {{ config(materialized='table', schema='pythian_dwh', alias ='f_intent_lead') }}                      
                        -- depends_on: { ref('f_bombora_select_topic_pythian_dwh') }  
                        {{ f_intent_lead_macro(custom_schema='pythian_dwh',table1='f_bombora_select_topic_pythian_dwh') }}
                        