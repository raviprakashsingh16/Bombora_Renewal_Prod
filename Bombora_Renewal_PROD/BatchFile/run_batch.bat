E:
cd E:/Bombora_capegemini_demo/BatchFile
cd new_arch_setup 
python addCrdAWS.py
python new_arch_db.py %1
python new_arch_schema.py %1
cd ..

cd DA_DBT
python sql_batch.py %1
python da_dbt_batch.py %1
cd ..

cd DU
# python du_batch.py %1
python rmCrdAWS.py
pause

