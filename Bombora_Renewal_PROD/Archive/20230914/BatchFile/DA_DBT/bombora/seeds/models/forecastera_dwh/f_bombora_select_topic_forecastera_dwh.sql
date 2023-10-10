
                        {{ config(materialized='table', schema='forecastera_dwh', alias ='f_bombora_select_topic') }}                      
                        
                        {{ f_bombora_select_topic_macro(custom_schema='forecastera_dwh',table1='_forecastera_dwh') }}
                        