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
