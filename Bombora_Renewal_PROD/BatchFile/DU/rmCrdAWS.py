import os
import json
import yaml

BASE_PATH = "/home/ubuntu/appdata/Bombora_Renewal_PROD/BatchFile"

def read_json_file(file_path):
    with open(file_path, 'r') as fp:
        data = json.load(fp)
    return data

def write_json_file(file_path, data):
    with open(file_path, 'w') as fp:
        json.dump(data, fp, indent=4)

def read_yaml_file(file_path):
    with open(file_path, 'r') as fp:
        data = yaml.safe_load(fp)
    return data

def write_yaml_file(file_path, data):
    with open(file_path, 'w') as fp:
        yaml.dump(data, fp)

def update_multitenant_info():
    input_json_file = os.path.join(BASE_PATH, 'multitenant.json')
    multitenant = read_json_file(input_json_file)

    li_secret_name = []

    for tn in multitenant:
        if 'org' in tn:
            li_secret_name.append(tn["org"])

    updated_multitenant_info = []

    for tenant in multitenant:
        secret_tenant = {}
        org = tenant.get("org", "")

        if org in li_secret_name:
            for key, value in tenant.items():
                if key == 'tenant_id':
                    secret_tenant['tenant_id'] = tenant['tenant_id']
                else:
                    secret_tenant[key] = ""
            if 'account_surge' in tenant:
                secret_tenant['account_surge'] = tenant['account_surge']
            if 'lead' in tenant:
                secret_tenant['lead'] = tenant['lead']
            if 'org' in tenant:
                secret_tenant['org'] = tenant['org']
        else:
            for key, value in tenant.items():
                if key == 'tenant_id':
                    secret_tenant['tenant_id'] = tenant['tenant_id']
                else:
                    secret_tenant[key] = ""
            if 'account_surge' in tenant:
                secret_tenant['account_surge'] = tenant['account_surge']
            if 'lead' in tenant:
                secret_tenant['lead'] = tenant['lead']
            if 'org' in tenant:
                secret_tenant['org'] = tenant['org']
            if 'db_schema' in tenant:
                secret_tenant['db_schema'] = tenant['db_schema']
        updated_multitenant_info.append(secret_tenant)

    write_json_file(input_json_file, updated_multitenant_info)

def update_profile_yml():
    input_yaml_file = os.path.join(BASE_PATH, 'profiles.yml')
    profile_yml = read_yaml_file(input_yaml_file)

    if 'dev' in profile_yml['bombora']['outputs']:
        dev = profile_yml['bombora']['outputs']['dev']
        updated_dev = {}

        for key, value in dev.items():
            if key in ('dbname', 'host', 'user', 'password', 'port'):
                updated_dev[key] = ''
            else:
                updated_dev[key] = value

        profile_yml['bombora']['outputs']['dev'] = updated_dev

    write_yaml_file(input_yaml_file, profile_yml)

def update_arch_tenant_info():
    input_json_file = os.path.join(BASE_PATH+'/new_arch_setup', 'new_arch_tenant.json')
    new_arch_tenant = read_json_file(input_json_file)

    if 'tenant_info' in new_arch_tenant:
        tenant_info = new_arch_tenant['tenant_info'][0]
        updated_tenant_info = {}

        for key, value in tenant_info.items():
            if key in ('schema', 'db_name','tenant_id'):
                updated_tenant_info[key] = value
            else:
                updated_tenant_info[key] = ""

        new_arch_tenant['tenant_info'][0] = updated_tenant_info

    write_json_file(input_json_file, new_arch_tenant)

if __name__ == "__main__":
    update_multitenant_info()
    update_profile_yml()
    update_arch_tenant_info()
