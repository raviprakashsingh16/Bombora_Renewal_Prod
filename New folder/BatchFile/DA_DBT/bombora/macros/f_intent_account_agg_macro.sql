{% macro f_intent_account_agg_macro(custom_schema,table1) -%}
with f_intent_account_agg as (
{%- set target_relation = adapter.get_relation(
      database=this.database,
      schema=this.schema,
      identifier=this.name) -%}
{%- set table_exists=target_relation is not none -%}
{%- if table_exists -%}
    select distinct a.*,case when b.nq_external_id is null then null else a.topic_count - b.topic_count end delta_topic_count ,
    a.avg_surge_score - b.avg_surge_score delta_avg_surge_score from 
    (
    SELECT distinct
    concat(trim("domain"),'_',trim(cluster_ui),'_',datestamp) as f_intent_account_agg_key, 
    md5(trim(concat(trim("domain"),'_',trim(cluster_ui),'_',trim(accountid)))) as "nq_external_id",
    accountid,accountname,"domain",company,cluster_ui "cluster",datestamp,count(topic) topic_count,round(avg(composite_score::integer)) avg_surge_score,
    concat(string_agg(concat(replace(replace(topic,',','-'),'^',','),' ',':',' ',composite_score),', '),',') topic_data
    FROM {{ ref(table1) }}  group by accountid,accountname,"domain",company,cluster_ui,datestamp) a
    left outer join
    (select * from (select max(datestamp) as max_datestamp from {{custom_schema}}."f_intent_account_agg") c,
    {{custom_schema}}."f_intent_account_agg" b  where b.datestamp =  c.max_datestamp) b
    on a.nq_external_id =b.nq_external_id 
    and  b.datestamp < a.datestamp
{%- else -%}    
    SELECT distinct
    concat(trim("domain"),'_',trim(cluster_ui),'_',datestamp) as f_intent_account_agg_key, 
    md5(trim(concat(trim("domain"),'_',trim(cluster_ui),'_',trim(accountid)))) as "nq_external_id",
    accountid,accountname,"domain",company,cluster_ui "cluster",datestamp,count(topic) topic_count,round(avg(composite_score::integer)) avg_surge_score,
    concat(string_agg(concat(replace(replace(topic,',','-'),'^',','),' ',':',' ',composite_score),', '),',') topic_data,null delta_topic_count,null delta_avg_surge_score
    FROM {{ ref(table1) }}  group by accountid,accountname,"domain",company,cluster_ui,datestamp
{%- endif -%}
)
select *
from f_intent_account_agg
{% endmacro %}