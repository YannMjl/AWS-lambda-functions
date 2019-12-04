import os
import json
import boto3
from datetime import datetime
from urllib.parse import urlparse

#-----------------------------------------------------------------------------#
# It takes the two inputs that I mentioned in the prerequisites section: 
# 1. the URL of the AWS CloudFormation template you want to deploy, and 
# 2. the URI of the input parameter file you want to use for setting up 
# the CloudFormation stack.
#-----------------------------------------------------------------------------#

params_url = os.environ['paramsFile']
template_url = os.environ['templateUrl']


def parse_params():

    s3 = boto3.resource('s3')
    s3_parse = urlparse(params_url)
    bucket = s3_parse.netloc
    s3_key = s3_parse.path.lstrip('/')
    s3_obj = s3.Object(bucket, s3_key)
    template_raw_data = s3_obj.get()["Body"].read().decode('utf-8')
    template_params = json.loads(template_raw_data)

    return template_params

#-----------------------------------------------------------------------------#
# The Lambda function is set up with two variables, templateUrl and paramsFile, 
# that point to your input template URL and parameters file. If in the future 
# you want to test with a different template and input parameters, you can use 
# the Lambda console to update the environment variables of the Lambda function.

# The Lambda function has been granted the Administrator role to allow AWS 
# CloudFormation to create any AWS resources that are defined in your template.
#-----------------------------------------------------------------------------#

def launch_stack():
    cfn = boto3.client('cloudformation')
    current_ts = datetime.now().isoformat().split('.')[0].replace(':', '-')
    stackname = 'Iot-qs-deploy-' + current_ts
    capabilities = ['CAPABILITY_IAM', 'CAPABILITY_AUTO_EXPAND']

    try:
        template_params = parse_params()

        stackdata = cfn.create_stack(
            StackName=stackname,
            DisableRollback=True,
            TemplateURL=template_url,
            Parameters=template_params,
            Capabilities=capabilities
        )

    except Exception as e:
        print(str(e))

    return stackdata


def handler(event, context):

    print("Received event:")
    stack_result = launch_stack()
    print(stack_result)
