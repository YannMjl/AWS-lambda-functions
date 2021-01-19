# AWS Lambda function

> These project contents Python's scripts Lambda function to deploy CloudFormation stacks

## Intro

AWS is announcing that AWS CloudFormation now supports creating AppStream 2.0 resources. With a single template, you can automate the creation of your stacks, fleets, image builders, directory configurations, and user pool users. You can now create AppStream 2.0 resources in your AWS CloudFormation templates along with your other AWS resources.

AWS CloudFormation lets you use a text file to model and provision, in an automated and secure manner, all the resources needed for your applications across all AWS Regions and accounts. 
You can now use AWS CloudFormation to create and manage your AppStream 2.0 image builders, stacks, fleets, directory configs, and user pool users.

## Getting Started

This script setup a Lambda function to deploy a CloudFormation stack

* The initial tutorial posted on AWS can be found here: **[Deploy CloudFormation stacks at the click of a button](https://aws.amazon.com/blogs/infrastructure-and-automation/deploy-cloudformation-stacks-at-the-click-of-a-button/)**

The Lambda function is set up with two variables, templateUrl and paramsFile, that point to your input template URL and parameters file. 
If in the future you want to test with a different template and input parameters, you can use the Lambda console to update the environment variables of the Lambda function.
The Lambda function has been granted the Administrator role to allow AWS CloudFormation to create any AWS resources that are defined in your template.
