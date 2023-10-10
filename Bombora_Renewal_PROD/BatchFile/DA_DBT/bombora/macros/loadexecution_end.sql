{% macro loadexecution_end() %}

{% set updateload %}
update staging.loadexecution_detail
set loadenddatetime=now(),
loadcomplete='y'
where loadexecution_detail_key=(select max (loadexecution_detail_key) from staging.loadexecution_detail)
{% endset %} 
{% do run_query(updateload) %}
{% endmacro %}