
                        {{ config(materialized='table', schema='nextq_dwh', alias ='f_bombora_select_topic') }}                      
                        
                        {{ f_bombora_select_topic_macro(custom_schema='nextq_dwh',table1='_nextq_dwh') }}
                        