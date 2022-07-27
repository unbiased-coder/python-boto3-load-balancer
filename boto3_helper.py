import os
from urllib import response
import boto3
import pprint
from dotenv import load_dotenv

def get_aws_keys():
    load_dotenv()
    return os.getenv('AWS_ACCESS_KEY'), os.getenv('AWS_SECRET_KEY')

def init_aws_session():
    access_key, secret_key = get_aws_keys()
    return boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=os.getenv('AWS_REGION'))

def ec2_get_vpc_list():
    session = init_aws_session()
    ec2 = session.client('ec2')
    response = ec2.describe_vpcs()
    return response['Vpcs']

def elb_create_target_group(target_group_name, vpc_id):
    session = init_aws_session()
    elb = session.client('elbv2')
    response = elb.create_target_group(Name=target_group_name, Protocol='HTTP', Port=80, VpcId=vpc_id)
    return response

def ec2_get_subnet_list():
    session = init_aws_session()
    ec2 = session.client('ec2')
    response = ec2.describe_subnets()
    return response['Subnets']

def ec2_get_security_group_list():
    session = init_aws_session()
    ec2 = session.client('ec2')
    response = ec2.describe_security_groups()
    return response['SecurityGroups']
