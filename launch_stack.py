import os
import json
import boto3

def lambda_handler(event, context):
    cf_client = boto3.client('cloudformation')
    stack_set_name = 'deleteresources'  # Name for the CloudFormation StackSet
    template_url = os.environ['TEMPLATE_URL']  # URL from the CloudFormation parameter
    target_ou = os.environ['TARGET_OU']  # Target OU from the CloudFormation parameter
    target_account = os.environ['TARGET_ACCOUNT']  # Target account ID from the CloudFormation parameter
    region = 'us-east-1'  # Deployment region

    try:
        # Create the CloudFormation stack set
        cf_client.create_stack_set(
            StackSetName=stack_set_name,
            TemplateURL=template_url,
            Capabilities=['CAPABILITY_NAMED_IAM'],
            PermissionModel='SERVICE_MANAGED',
            AutoDeployment={
                'Enabled': True,
                'RetainStacksOnAccountRemoval': False
            },
            Parameters=[
                # Add any necessary parameters here
            ]
        )

        # Deploy the stack set to the specified OU or account
        cf_client.create_stack_instances(
            StackSetName=stack_set_name,
            DeploymentTargets={
                'OrganizationalUnitIds': [target_ou],
                # Alternatively, for a specific account: 'Accounts': [target_account]
            },
            Regions=[region]
        )

        return {
            'statusCode': 200,
            'body': json.dumps(f'StackSet {stack_set_name} deployment initiated.')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
