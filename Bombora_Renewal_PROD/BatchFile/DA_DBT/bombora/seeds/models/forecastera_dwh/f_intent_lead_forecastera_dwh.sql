
                        {{ config(materialized='table', schema='forecastera_dwh', alias ='f_intent_lead') }}                      
                        -- depends_on: { ref('f_bombora_select_topic_forecastera_dwh') }  
                        {{ f_intent_lead_macro(custom_schema='forecastera_dwh',table1='f_bombora_select_topic_forecastera_dwh') }}
                        