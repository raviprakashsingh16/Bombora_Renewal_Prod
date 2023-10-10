
                        {{ config(materialized='table', schema='pythian_dwh', alias ='f_bombora_select_topic') }}                      
                        
                        {{ f_bombora_select_topic_macro(custom_schema='pythian_dwh',table1='_pythian_dwh') }}
                        