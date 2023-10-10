do
$$
DECLARE filename TEXT;
DECLARE v_datestamp TEXT;
DECLARE v_next_datestamp date;
begin
select COALESCE(to_char(max(datestamp) + 7,'yyyymmdd'),'20230903') into v_datestamp  from "bombora_dwh".f_adat_bombora;
select COALESCE(max(datestamp) + 7,to_date('20230903','yyyymmdd')) into v_next_datestamp  from "bombora_dwh".f_adat_bombora;
if current_date < v_next_datestamp then
RAISE NOTICE 'Value: %', v_next_datestamp;
else
execute 'truncate table "bombora_dwh".f_adat_bombora';
for i in 1..50 loop
filename='/'|| v_datestamp||'/MasterSurgeFile_'||v_datestamp||'_'||i||'.csv';
execute 'SELECT aws_s3.table_import_from_s3(
'' "bombora_dwh"."f_adat_bombora"'', '''', ''(format csv, header true)'',
(SELECT aws_commons.create_s3_uri(
''lakshmifcst'','''|| filename||''', ''us-east-1'' ) AS s3_uri_bombora))';
end loop;
end if;
end;
$$