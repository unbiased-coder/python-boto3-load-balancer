import pprint
from boto3_helper import init_aws_session

session = init_aws_session()
elb = session.client('elbv2')
response = elb.describe_load_balancers()
pprint.pprint(response['LoadBalancers'])