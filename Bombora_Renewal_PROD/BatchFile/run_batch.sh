#!/bin/bash
echo "Activating virtual enviornment"
if [ -f "/home/ubuntu/appdata/venv_features/venv_bombora/bin/activate" ]; then
    . "/home/ubuntu/appdata/venv/bin/activate"
 echo "Virtual environment found "
else
    echo "Virtual environment not found or path incorrect!"
    exit 1
fi

cd /home/ubuntu/appdata/Bombora_Renewal_PROD/BatchFile
cd new_arch_setup 
python addCrdAWS.py
python new_arch_db.py 
python new_arch_schema.py 
cd ..
cd DA_DBT
python sql_batch.py 
python da_dbt_batch.py 
cd ..
cd DU
python du_batch.py
python rmCrdAWS.py


pause
