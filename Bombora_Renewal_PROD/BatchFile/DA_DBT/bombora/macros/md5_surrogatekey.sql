{% macro md5_surrogatekey(id) %}
(select md5('{{id}}'))
{% endmacro %}