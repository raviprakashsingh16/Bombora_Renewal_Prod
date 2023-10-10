
                        {{ config(materialized='table',unique_key='', schema='revature_dwh', alias ='f_bombora_select_topic', post_hook=["drop index if exists revature_dwh.ind_domain1","create index if not exists ind_domain1 on revature_dwh.f_bombora_select_topic(trim(trailing '/' from REGEXP_REPLACE(REGEXP_REPLACE(REGEXP_REPLACE('domain','https://',''),'http://',''),'www.','')))"]) }}                      
                        
                        {{ f_bombora_select_topic_macro(custom_schema='revature_dwh',table1='_revature_dwh') }}
                        