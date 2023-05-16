{% macro f_intent_account_macro_archive(custom_schema,table1) -%}
with f_intent_account as (
    select 
    substr(concat(b."domain",'_',b.topic,'_',a.accountid),1,255) as "f_intent_account_key",
    a."accountid",
    a."accountname",
    a."accountnumber",
    a."website",
    a."ownership",
    a."industry" as "industry_account",
    a."description",
    b.*
    from {{custom_schema}}.d_account a
    inner join {{ ref(table1) }} b
    on 
     trim(trailing '/' from trim('www.' from trim(leading 'https://' from a."website")))  = trim(trailing '/' from trim('www.' from trim(leading 'https://' from b."domain")))
)

select *
from f_intent_account
{% endmacro %}