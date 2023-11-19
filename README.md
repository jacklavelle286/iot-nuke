
# IoT Button Cloud-Nuke Solution

## Introduction

The IoT button cloud-nuke solution is designed to provide an efficient and automated way to clean up AWS resources in a development environment. By integrating an AWS IoT button with AWS Lambda and CloudFormation, this solution allows you to conveniently delete all resources in a specific AWS account and Organizational Unit (OU) with the simple press of a button. It's particularly useful for managing resources in a development environment, where frequent build-ups and tear-downs are common.

## Solution Overview

The solution operates across AWS accounts, with the IoT button and Lambda function residing in the management account, and the target of the cleanup being the development account within the specified OU in AWS Organizations.

*Note* whilst this successfully deletes the stack resources in your target account, currently you will have to delete the stack set instance in your deletion account and the stack set itself in your payer account manually after your cloud-nuke solution has run before you click your iot button again. This is because a stack will try to be recreated with the same name as previously, and therefore it will fail. I am working on this change currently.

### Solution Flow

1. **Click IoT Button**: A physical IoT button is clicked.
2. **Trigger Lambda Function**: The button click triggers a Lambda function in the management account.
3. **Deploy Stack Set in Dev Account**: The Lambda function deploys a CloudFormation stack set in the development account. This stack set includes a cloud-nuke EC2 instance and its associated role.
4. **Run Cloud-Nuke**: The cloud-nuke instance executes and deletes all resources within the development account, including itself and its associated resources.

## First-Time Setup (Management Account)

### Prerequisites

- AWS Management and Development accounts under AWS Organizations.
- An IoT button
- a default VPC in the destination account

### Steps
1. **Launch Initial CloudFormation Stack**:
   - Use `first_template.yaml` to create the initial resources.
   - This stack creates:
     - An S3 Bucket for the second CloudFormation template (`delete-resources.yaml`).
     - An S3 Bucket for the Lambda function's code (`launch-stack.zip`).

2. **Prepare and Upload Lambda Function**:
   - Zip the `launch-stack.py` file.
   - Upload the zip file to the code S3 bucket created in step 1.

3. **Deploy the Second Stack**:
   - Use the S3 URL of `lambda.yaml` to deploy the second CloudFormation stack.
   - Provide parameters referring to:
     - The S3 bucket where the Lambda code resides.
     - The OU ID and account name for the target environment.
     - The S3 URL of the `delete-resources.yaml` template.

4. **Manual Trigger Test**:
   - Initially, trigger the Lambda function manually to validate the deployment of the cloud-nuke EC2 instance in your target account.

## Optional: IoT Button Setup

To set up the IoT button as a trigger for the Lambda function, follow these steps:

1. **Register and Configure IoT Button**:
   - Register the IoT button in AWS IoT 1-Click and configure it to connect to your network.

2. **Create IoT 1-Click Project**:
   - Create a new project in IoT 1-Click and add the IoT button to this project.

3. **Associate Lambda Function**:
   - Link the Lambda function to the IoT button within the IoT 1-Click project.

4. **Test Button Trigger**:
   - Test the setup by pressing the IoT button and monitoring the execution of the Lambda function and the deployment of resources in the development account.
