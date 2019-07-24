import boto3
import json

def lambda_handler(event, context):
    
    client = boto3.client('iam')
    sts_client = boto3.client('sts')

    #role = client.get_role(RoleName='apiExecuteRole',)
    # arn = role['Role']['Arn']
    
    #arn:aws:iam::122312312312:role/apiExecuteRole  
    assumedRoleObject = sts_client.assume_role(
        RoleArn="arn:aws:iam::123122313213:role/apiExecuteRole",
        RoleSessionName = "AssumeRoleSession",
        DurationSeconds=3600
    )
    credentials = assumedRoleObject['Credentials']
    print(credentials)
    
    region = 'ap-northeast-1a'
    ec2 = boto3.client(
        'ec2',
        aws_access_key_id = credentials['AccessKeyId'],
        aws_secret_access_key = credentials['SecretAccessKey'],
        aws_session_token = credentials['SessionToken'],
    )
    instance = ['i-09040xxxxxxxxxxxx6']
    
    
    instances = ec2.describe_instances();
    ec2.start_instances(InstanceIdxs=instance)
    #print (instances)

    # for bucket in s3_resource.buckets.all():
    #     print(bucket.name)
    
    # region = ['ap-northeast-1a']
    # ec2 = boto3.client('ec2',region_name=region)
    # instances = ['i-09xxxxxxxxxx']

    # ec2_resource.start_instances(InstanceIds=instances)
