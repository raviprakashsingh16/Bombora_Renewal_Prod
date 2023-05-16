
                        {{ config(materialized='table', schema='revature_dwh', alias ='f_bombora_select_topic') }}                      
                        
                        {{ f_bombora_select_topic_macro(custom_schema='revature_dwh',table1='_revature_dwh') }}
                        