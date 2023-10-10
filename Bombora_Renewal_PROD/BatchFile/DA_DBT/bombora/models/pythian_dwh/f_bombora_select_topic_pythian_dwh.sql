
                        {{ config(materialized='table',unique_key='', schema='pythian_dwh', alias ='f_bombora_select_topic', post_hook=["drop index if exists pythian_dwh.ind_domain1","create index if not exists ind_domain1 on pythian_dwh.f_bombora_select_topic(trim(trailing '/' from REGEXP_REPLACE(REGEXP_REPLACE(REGEXP_REPLACE('domain','https://',''),'http://',''),'www.','')))"]) }}                      
                        
                        {{ f_bombora_select_topic_macro(custom_schema='pythian_dwh',table1='_pythian_dwh') }}
                        