{% macro f_bombora_select_topic_macro(custom_schema,table1) -%}
with f_bombora_select_topic as (
    select a.company, a."domain", a."size", a.industry, a.category, a.topic, a.composite_score, 
    a.metro_area,a.domain_origin,a.bucket_code,datestamp,
    b.accountid as accountid_ui , b.accountname as accountname_ui, b.userid as userid_ui, b.theme as theme_ui, b."cluster" as cluster_ui,b.category as category_ui,b.cluster_type as cluster_type_ui,b."cluster_initial" as cluster_initial
    from "bombora_dwh"."f_adat_bombora" a
    inner join lateral (select accountid,accountname,userid,theme,category,cluster,cluster_type,cluster_initial, unnest(string_to_array( topic,'^')) topic 
---unnest(string_to_array( topic,',')) topic 
                        from "{{custom_schema}}"."f_acc_topics") b
    on 
    trim(a."topic") = trim(b."topic") 


)

select *
from f_bombora_select_topic
{% endmacro %}


 