{% macro f_intent_lead_macro(custom_schema,table1) -%}
with f_intent_lead as (
    select 
    trim(concat(trim(a."domain"),'_',trim(a.topic))) as "f_intent_lead_key",
    a.*
    from {{ ref(table1) }} a
    where a.domain not in (select website from {{custom_schema}}."d_account")
    )
select *
from f_intent_lead
{% endmacro %}