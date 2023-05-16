cd /home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile
cd new_arch_setup
python new_arch_db.py
python new_arch_schema.py
cd ..

cd DA_DBT
python sql_batch.py
python da_dbt_batch.py
python view_batch.py
cd ..

#cd DU
#python du_batch.py

pause

