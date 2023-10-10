{% macro loadexecution_start() %}
{% set sql %}
CREATE TABLE IF NOT EXISTS staging.loadexecution_detail
(
    loadexecution_detail_key bigint,
    loadstartdatetime timestamp without time zone,
    loadenddatetime timestamp without time zone,
    loadcomplete character varying(255) COLLATE pg_catalog."default",
    executiondate timestamp 
)
{%- endset -%}
{% do run_query(sql) %}
{% do log("created table if not exists ", info=True) %}
{% set insertload %}
INSERT INTO staging.loadexecution_detail( loadstartdatetime, loadexecution_detail_key,executiondate)
VALUES (now(),(select max(coalesce(loadexecution_detail_key,0)+1) from staging.loadexecution_detail),now())
{% endset %} 
{{ print("Running query: " ~ query) }}
{% do run_query(insertload) %}
{% endmacro %}