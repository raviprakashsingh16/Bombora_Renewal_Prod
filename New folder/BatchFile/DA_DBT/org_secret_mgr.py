import os
import boto3
from botocore.exceptions import ClientError
import ast
import json

BASE_PATH = "/home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile"
def get_secret(sn):

    secret_name = sn
    region_name = "us-east-1"

    # Create a Secrets Manager client
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
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']
    result = ast.literal_eval(secret)
    return result

    # Your code goes here.
#li_secret_name=["AI/AWS_Org","AI/NewDevHub_Org"]

li_secret_name=[]
with open('/home/ubuntu/appdata/Bombora_Integration_PROD/BatchFile/multitenant.json', 'r') as fp:
    multitenant=json.load(fp)
    for tn in multitenant:
        if tn["tenant_id"]!="bombora":
            try:
                li_secret_name.append(tn["org"])
            except:
                continue

list_path_filenames=[]
print(li_secret_name)

for sn in li_secret_name:
    gs=get_secret(sn)
    # filename=tn['tenant_id']+'.json'
    # path_filename=os.path.join(BASE_PATH + '/DA_DBT/', filename)
    # list_path_filenames.append(path_filename)
    with open(gs["tenant_id"]+'.json', 'w') as fp:
        json.dump(gs, fp)
        path_filename=os.path.join(BASE_PATH + '/DA_DBT/', gs["tenant_id"]+'.json')
        print(path_filename)
        list_path_filenames.append(path_filename)
print (list_path_filenames)
