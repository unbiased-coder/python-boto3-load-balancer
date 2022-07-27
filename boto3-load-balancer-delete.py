import pprint
from boto3_helper import init_aws_session

session = init_aws_session()
elb = session.client('elbv2')
response = elb.delete_load_balancer(LoadBalancerArn='arn:aws:elasticloadbalancing:us-east-1:033533902081:loadbalancer/app/UnbiasedCoderLoadBalancerNew/229e0cd4748d1d6a')
pprint.pprint(response)
