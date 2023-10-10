import os
import boto3
from botocore.exceptions import ClientError
import ast
import json
from multiprocessing.sharedctypes import Value
import yaml

BASE_PATH = "/home/ubuntu/appdata/Bombora_Renewal_PROD/BatchFile"

def get_secret(sn):
    secret_name = sn
    region_name = "us-east-1"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise e

    secret = get_secret_value_response['SecretString']
    result = json.loads(secret)
    return result

# Function to update multitenant information
def update_multitenant_info():
    li_secret_name = []

    with open(BASE_PATH+'/multitenant.json', 'r') as fp:
        multitenant = json.load(fp)
        for tn in multitenant:
            if 'org' in tn:
                li_secret_name.append(tn["org"])

    # print('li_secret_name', li_secret_name)

    for sn in li_secret_name:
        gs = get_secret(sn)

    updated_multitenant_info = []

    for tenant in multitenant:
        secret_tenant = {}
        org = tenant.get("org", "")
        if org in li_secret_name:
            gs = get_secret(org)
            for key, value in tenant.items():
                if key in gs:
                    if key == 'tenant_id':
                        secret_tenant[key] = value
                    else:
                        secret_tenant[key] = gs[key]
            if 'account_surge' in tenant:
                secret_tenant['account_surge'] = tenant['account_surge']
            if 'lead' in tenant:
                secret_tenant['lead'] = tenant['lead']
            if 'org' in tenant:
                secret_tenant['org'] = tenant['org']
        else:
            gs = get_secret(li_secret_name[0])
            for key, value in tenant.items():
                if key in gs:
                    if key == 'tenant_id':
                        secret_tenant[key] = value
                    else:
                        secret_tenant[key] = gs[key]
            if 'account_surge' in tenant:
                secret_tenant['account_surge'] = tenant['account_surge']
            if 'lead' in tenant:
                secret_tenant['lead'] = tenant['lead']
            if 'org' in tenant:
                secret_tenant['org'] = tenant['org']
            if 'db_schema' in tenant:
                secret_tenant['db_schema'] = tenant['db_schema']
        updated_multitenant_info.append(secret_tenant)

    # print(updated_multitenant_info)
    # print("Updated updated_multitenant_info:", updated_multitenant_info)

    with open(BASE_PATH+'/multitenant.json', 'w') as fp:
        json.dump(updated_multitenant_info, fp, indent=4)
        fp.write('\n')

# Function to update profile YML
def update_profile_yml():
    li_secret_name = []

    with open(BASE_PATH+'/multitenant.json', 'r') as fp:
        multitenant = json.load(fp)
        for tn in multitenant:
            try:
                li_secret_name.append(tn["org"])
                if len(li_secret_name) == 1:
                    break
            except:
                pass

    with open(BASE_PATH+'/profiles.yml', 'r') as fp:
        profile_yml = yaml.safe_load(fp)

    for sn in li_secret_name:
        gs = get_secret(sn)

    updated_profile_yml = {}

    if 'dev' in profile_yml['bombora']['outputs'] and len(profile_yml['bombora']['outputs']) > 0:
        dev = profile_yml['bombora']['outputs']['dev']
        for key, value in dev.items():
            if key == 'dbname':
                updated_profile_yml['dbname'] = gs['db_database']
            if key == 'host':
                updated_profile_yml['host'] = gs['db_host']
            if key == 'user':
                updated_profile_yml['user'] = gs['db_username']
            if key == 'password':
                updated_profile_yml['password'] = gs['db_password']
            if key == 'port':
                updated_profile_yml['port'] = int(gs['db_port'])

        if 'type' in profile_yml['bombora']['outputs']['dev']:
            updated_profile_yml['type'] = profile_yml['bombora']['outputs']['dev']['type']
        if 'schema' in profile_yml['bombora']['outputs']['dev']:
            updated_profile_yml['schema'] = profile_yml['bombora']['outputs']['dev']['schema']
        if 'threads' in profile_yml['bombora']['outputs']['dev']:
            updated_profile_yml['threads'] = profile_yml['bombora']['outputs']['dev']['threads']
        if 'keepalives_idle' in profile_yml['bombora']['outputs']['dev']:
            updated_profile_yml['keepalives_idle'] = profile_yml['bombora']['outputs']['dev']['keepalives_idle']
        if 'connect_timeout' in profile_yml['bombora']['outputs']['dev']:
            updated_profile_yml['connect_timeout'] = profile_yml['bombora']['outputs']['dev']['connect_timeout']

    if 'dev' in profile_yml['bombora']['outputs']:
        profile_yml['bombora']['outputs']['dev'] = updated_profile_yml

    with open(BASE_PATH+'/profiles.yml', 'w') as fp:
        yaml.safe_dump(profile_yml, fp, default_flow_style=False)

# Function to update new_arch_tenant information
def update_new_arch_tenant_info():
    #li_secret_name = ["AI/JuneDevHub_Org_Log"]
    li_secret_name = []

    with open(BASE_PATH+'/multitenant.json', 'r') as fp:
        multitenant = json.load(fp)
        for tn in multitenant:
            try:
                li_secret_name.append(tn["org"])
                if len(li_secret_name) == 1:
                    break
            except:
                pass
                
    with open(BASE_PATH+'/new_arch_setup/new_arch_tenant.json', 'r') as fp:
        new_arch_tenant = json.load(fp)

    for sn in li_secret_name:
        gs = get_secret(sn)

    updated_tenant_info = {}

    if 'tenant_info' in new_arch_tenant and len(new_arch_tenant['tenant_info']) > 0:
        tenant_info = new_arch_tenant['tenant_info'][0]
        for key, value in tenant_info.items():
            if key in gs:
                if key == 'tenant_id':
                    updated_tenant_info[key] = value
                else:
                    updated_tenant_info[key] = gs[key]
            else:
                if key == 'db_user':
                    updated_tenant_info['db_user'] = gs['db_username']
                if key == 'db_create':
                    updated_tenant_info['db_create'] = gs['db_database']

        if 'schema' in new_arch_tenant['tenant_info'][0]:
            updated_tenant_info['schema'] = new_arch_tenant['tenant_info'][0]['schema']
        if 'db_name' in new_arch_tenant['tenant_info'][0]:
            updated_tenant_info['db_name'] = new_arch_tenant['tenant_info'][0]['db_name']

    if 'tenant_info' in new_arch_tenant:
        new_arch_tenant['tenant_info'][0] = updated_tenant_info

    with open(BASE_PATH+'/new_arch_setup/new_arch_tenant.json', 'w') as fp:
        for key, value in new_arch_tenant.items():
            json.dump({key: value}, fp, indent=4)
            fp.write('\n')

# Main program
if __name__ == "__main__":
    update_multitenant_info()
    update_profile_yml()
    update_new_arch_tenant_info()
