
# IoT Button Cloud-Nuke Solution

## Introduction

The IoT button cloud-nuke solution is designed to provide an efficient and automated way to clean up AWS resources in a development environment. By integrating an AWS IoT button with AWS Lambda and CloudFormation, this solution allows you to conveniently delete all resources in a specific AWS account and Organizational Unit (OU) with the simple press of a button. It's particularly useful for managing resources in a development environment, where frequent build-ups and tear-downs are common.

## Solution Overview

The solution operates across AWS accounts, with the IoT button and Lambda function residing in the management account, and the target of the cleanup being the development account within the specified OU in AWS Organizations.

*Note* whilst this successfully deletes the stack resources in your target account, currently you will have to delete the stack set in your payer account manually after your cloud-nuke solution has run before you click your iot button again. This is because a stack will try to he recreated with the same name, and therefore it will fail. I am working on this change currently.

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








