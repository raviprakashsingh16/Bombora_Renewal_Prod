do
$$
DECLARE filename TEXT;
DECLARE v_datestamp TEXT;
begin
select COALESCE(to_char(max(datestamp) + 7,'yyyymmdd'),'20230423') into v_datestamp  from "bombora_dwh".f_adat_bombora;
execute 'truncate table "bombora_dwh".f_adat_bombora';
for i in 1..50 loop
filename='/'|| v_datestamp||'/MasterSurgeFile_'||v_datestamp||'_'||i||'.csv';
execute 'SELECT aws_s3.table_import_from_s3(
'' "bombora_dwh"."f_adat_bombora"'', '''', ''(format csv, header true)'',
(SELECT aws_commons.create_s3_uri(
''ai-bombora-prod'','''|| filename||''', ''us-east-1'' ) AS s3_uri_bombora))';
end loop;
end;
$$