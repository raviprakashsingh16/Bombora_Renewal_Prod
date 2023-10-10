
                        {{ config(materialized='table', schema='', alias ='f_intent_lead') }}                      
                        -- depends_on: { ref('f_bombora_select_topic_') }  
                        {{ f_intent_lead_macro(custom_schema='',table1='f_bombora_select_topic_') }}
                        