---
id: "@specs/aws/lambda/docs/configuration-vpc"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Attaching functions to a VPC"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Attaching functions to a VPC

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/configuration-vpc
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Giving Lambda functions access to resources in an Amazon VPC
<a name="configuration-vpc"></a>

With Amazon Virtual Private Cloud (Amazon VPC), you can create private networks in your AWS account to host resources such as Amazon Elastic Compute Cloud (Amazon EC2) instances, Amazon Relational Database Service (Amazon RDS) instances, and Amazon ElastiCache instances. You can give your Lambda function access to resources hosted in an Amazon VPC by attaching your function to the VPC through the private subnets that contain the resources. Follow the instructions in the following sections to attach a Lambda function to an Amazon VPC using the Lambda console, the AWS Command Line Interface (AWS CLI), or AWS SAM.

**Note**  
Every Lambda function runs inside a VPC that is owned and managed by the Lambda service. These VPCs are maintained automatically by Lambda and are not visible to customers. Configuring your function to access other AWS resources in an Amazon VPC has no effect on the Lambda-managed VPC your function runs inside.

**Topics**
+ [Required IAM permissions](#configuration-vpc-permissions)
+ [Attaching Lambda functions to an Amazon VPC in your AWS account](#configuration-vpc-attaching)
+ [Internet access when attached to a VPC](#configuration-vpc-internet-access)
+ [IPv6 support](#configuration-vpc-ipv6)
+ [Best practices for using Lambda with Amazon VPCs](#configuration-vpc-best-practice)
+ [Understanding Hyperplane Elastic Network Interfaces (ENIs)](#configuration-vpc-enis)
+ [Using IAM condition keys for VPC settings](#vpc-conditions)
+ [VPC tutorials](#vpc-tutorials)

## Required IAM permissions
<a name="configuration-vpc-permissions"></a>

To attach a Lambda function to an Amazon VPC in your AWS account, Lambda needs permissions to create and manage the network interfaces it uses to give your function access to the resources in the VPC.

The network interfaces that Lambda creates are known as Hyperplane Elastic Network Interfaces, or Hyperplane ENIs. To learn more about these network interfaces, see [Understanding Hyperplane Elastic Network Interfaces (ENIs)](#configuration-vpc-enis).

You can give your function the permissions it needs by attaching the AWS managed policy [AWSLambdaVPCAccessExecutionRole](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaVPCAccessExecutionRole.html) to your function's execution role. When you create a new function in the Lambda console and attach it to a VPC, Lambda automatically adds this permissions policy for you.

If you prefer to create your own IAM permissions policy, make sure to add all of the following permissions and allow them on all resources (`"Resource": "*"`):
+ ec2:CreateNetworkInterface
+ ec2:DescribeNetworkInterfaces
+ ec2:DescribeSubnets
+ ec2:DeleteNetworkInterface
+ ec2:AssignPrivateIpAddresses
+ ec2:UnassignPrivateIpAddresses

Note that your function's role only needs these permissions to create the network interfaces, not to invoke your function. You can still invoke your function successfully when it’s attached to an Amazon VPC, even if you remove these permissions from your function’s execution role. 

To attach your function to a VPC, Lambda also needs to verify network resources using your IAM user role. Ensure that your user role has the following IAM permissions:
+ **ec2:DescribeSecurityGroups**
+ **ec2:DescribeSubnets**
+ **ec2:DescribeVpcs**
+ **ec2:GetSecurityGroupsForVpc**

**Note**  
The Amazon EC2 permissions that you grant to your function's execution role are used by the Lambda service to attach your function to a VPC. However, you're also implicitly granting these permissions to your function's code. This means that your function code is able to make these Amazon EC2 API calls. For advice on following security best practices, see [Security best practices](#configuration-vpc-best-practice-security).

## Attaching Lambda functions to an Amazon VPC in your AWS account
<a name="configuration-vpc-attaching"></a>

Attach your function to an Amazon VPC in your AWS account by using the Lambda console, the AWS CLI or AWS SAM. If you're using the AWS CLI or AWS SAM, or attaching an existing function to a VPC using the Lambda console, make sure that your function's execution role has the necessary permissions listed in the previous section.

Lambda functions can't connect directly to a VPC with [ dedicated instance tenancy](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html). To connect to resources in a dedicated VPC, [peer it to a second VPC with default tenancy](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-dedicated-vpc/).

------
#### [ Lambda console ]

**To attach a function to an Amazon VPC when you create it**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console and choose **Create function**.

1. Under **Basic information**, for **Function name**, enter a name for your function.

1. Configure VPC settings for the function by doing the following:

   1. Expand **Advanced settings**.

   1. Select **Enable VPC**, and then select the VPC you want to attach the function to.

   1. (Optional) To allow [outbound IPv6 traffic](#configuration-vpc-ipv6), select **Allow IPv6 traffic for dual-stack subnets**.

   1. Choose the subnets and security groups to create the network interface for. If you selected **Allow IPv6 traffic for dual-stack subnets**, all selected subnets must have an IPv4 CIDR block and an IPv6 CIDR block.
**Note**  
To access private resources, connect your function to private subnets. If your function needs internet access, see [Enable internet access for VPC-connected Lambda functions](configuration-vpc-internet.md). Connecting a function to a public subnet doesn't give it internet access or a public IP address. 

1. Choose **Create function**.

**To attach an existing function to an Amazon VPC**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console and select your function.

1. Choose the **Configuration** tab, then choose **VPC**.

1. Choose **Edit**.

1. Under **VPC**, select the Amazon VPC you want to attach your function to.

1. (Optional) To allow [outbound IPv6 traffic](#configuration-vpc-ipv6), select **Allow IPv6 traffic for dual-stack subnets**. 

1. Choose the subnets and security groups to create the network interface for. If you selected **Allow IPv6 traffic for dual-stack subnets**, all selected subnets must have an IPv4 CIDR block and an IPv6 CIDR block.
**Note**  
To access private resources, connect your function to private subnets. If your function needs internet access, see [Enable internet access for VPC-connected Lambda functions](configuration-vpc-internet.md). Connecting a function to a public subnet doesn't give it internet access or a public IP address. 

1. Choose **Save**.

------
#### [ AWS CLI ]

**To attach a function to an Amazon VPC when you create it**
+ To create a Lambda function and attach it to a VPC, run the following CLI `create-function` command.

  ```
  aws lambda create-function --function-name {{my-function}} \
  --runtime {{nodejs24.x}} --handler {{index.js}} --zip-file {{fileb://function.zip}} \
  --role {{arn:aws:iam::123456789012:role/lambda-role}} \
  --vpc-config Ipv6AllowedForDualStack={{true}},SubnetIds={{subnet-071f712345678e7c8}},{{subnet-07fd123456788a036}},SecurityGroupIds={{sg-085912345678492fb}}
  ```

  Specify your own subnets and security groups and set `Ipv6AllowedForDualStack` to `true` or `false` according to your use case.

**To attach an existing function to an Amazon VPC**
+ To attach an existing function to a VPC, run the following CLI `update-function-configuration` command.

  ```
  aws lambda update-function-configuration --function-name {{my-function}} \
  --vpc-config Ipv6AllowedForDualStack={{true}}, SubnetIds={{subnet-071f712345678e7c8}},{{subnet-07fd123456788a036}},SecurityGroupIds={{sg-085912345678492fb}}
  ```

**To unattach your function from a VPC**
+ To unattach your function from a VPC, run the following `update-function-configuration`CLI command with an empty list of VPC subnets and security groups.

  ```
  aws lambda update-function-configuration --function-name {{my-function}} \
  --vpc-config SubnetIds=[],SecurityGroupIds=[]
  ```

------
#### [ AWS SAM ]

**To attach your function to a VPC**
+ To attach a Lambda function to an Amazon VPC, add the `VpcConfig` property to your function definition as shown in the following example template. For more information about this property, see [AWS::Lambda::Function VpcConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html) in the *CloudFormation User Guide* (the AWS SAM `VpcConfig` property is passed directly to the `VpcConfig` property of an CloudFormation `AWS::Lambda::Function` resource).

  ```
  AWSTemplateFormatVersion: '2010-09-09'
  Transform: AWS::Serverless-2016-10-31
  
  Resources:
    MyFunction:
      Type: AWS::Serverless::Function
      Properties:
        CodeUri: ./lambda_function/
        Handler: lambda_function.handler
        Runtime: python3.12
        VpcConfig:
          SecurityGroupIds:
            - !Ref MySecurityGroup
          SubnetIds:
            - !Ref MySubnet1
            - !Ref MySubnet2
        Policies:
          - AWSLambdaVPCAccessExecutionRole
  
    MySecurityGroup:
      Type: AWS::EC2::SecurityGroup
      Properties:
        GroupDescription: Security group for Lambda function
        VpcId: !Ref MyVPC
  
    MySubnet1:
      Type: AWS::EC2::Subnet
      Properties:
        VpcId: !Ref MyVPC
        CidrBlock: 10.0.1.0/24
  
    MySubnet2:
      Type: AWS::EC2::Subnet
      Properties:
        VpcId: !Ref MyVPC
        CidrBlock: 10.0.2.0/24
  
    MyVPC:
      Type: AWS::EC2::VPC
      Properties:
        CidrBlock: 10.0.0.0/16
  ```

  For more information about configuring your VPC in AWS SAM, see [AWS::EC2::VPC](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpc.html) in the *CloudFormation User Guide*.

------

## Internet access when attached to a VPC
<a name="configuration-vpc-internet-access"></a>

By default, Lambda functions have access to the public internet. When you attach your function to a VPC, it can only access resources available within that VPC. To give your function access to the internet, you also need to configure the VPC to have internet access. To learn more, see [Enable internet access for VPC-connected Lambda functions](configuration-vpc-internet.md).

## IPv6 support
<a name="configuration-vpc-ipv6"></a>

Your function can connect to resources in dual-stack VPC subnets over IPv6. This option is turned off by default. To allow outbound IPv6 traffic, use the console or the `--vpc-config Ipv6AllowedForDualStack=true` option with the [create-function](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-function.html) or [update-function-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-configuration.html) command.

**Note**  
To allow outbound IPv6 traffic in a VPC, all of the subnets that are connected to the function must be dual-stack subnets. Lambda doesn't support outbound IPv6 connections for IPv6-only subnets in a VPC or outbound IPv6 connections for functions that are not connected to a VPC.

You can update your function code to explicitly connect to subnet resources over IPv6. The following Python example opens a socket and connects to an IPv6 server.

**Example — Connect to IPv6 server**  

```
def connect_to_server(event, context):
    server_address = event['host']
    server_port = event['port']
    message = event['message']
    run_connect_to_server(server_address, server_port, message)

def run_connect_to_server(server_address, server_port, message):
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
    try:
        # Send data
        sock.connect((server_address, int(server_port), 0, 0))
        sock.sendall(message.encode())
        BUFF_SIZE = 4096
        data = b''
        while True:
            segment = sock.recv(BUFF_SIZE)
            data += segment
            # Either 0 or end of data
            if len(segment) < BUFF_SIZE:
                break
        return data
    finally:
        sock.close()
```

## Best practices for using Lambda with Amazon VPCs
<a name="configuration-vpc-best-practice"></a>

To ensure that your Lambda VPC configuration meets best practice guidelines, follow the advice in the following sections.

### Security best practices
<a name="configuration-vpc-best-practice-security"></a>

To attach your Lambda function to a VPC, you need to give your function’s execution role a number of Amazon EC2 permissions. These permissions are required to create the network interfaces your function uses to access the resources in the VPC. However, these permissions are also implicitly granted to your function’s code. This means that your function code has permission to make these Amazon EC2 API calls.

To follow the principle of least-privilege access, add a deny policy like the following example to your function’s execution role. This policy prevents your function code from making calls to the Amazon EC2 APIs, while still allowing the Lambda service to manage VPC resources on your behalf. The policy uses the `lambda:SourceFunctionArn` condition key, which only applies to API calls made by your function code during execution. For more information, see [Using source function ARN to control function access behavior](permissions-source-function-arn.md).

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Deny",
            "Action": [ 
                 "ec2:CreateNetworkInterface",
                 "ec2:DeleteNetworkInterface",
                 "ec2:DescribeNetworkInterfaces",
                 "ec2:DescribeSubnets",
                 "ec2:DetachNetworkInterface",
                 "ec2:AssignPrivateIpAddresses",
                 "ec2:UnassignPrivateIpAddresses"
            ],
            "Resource": [ "*" ],
            "Condition": {
                "ArnEquals": {
                    "lambda:SourceFunctionArn": [
                        "arn:aws:lambda:us-west-2:123456789012:function:my_function"
                    ]
                }
            }
        }
    ]
}
```

------

AWS provides *[security groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)* and *[network Access Control Lists (ACLs)](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)* to increase security in your VPC. Security groups control inbound and outbound traffic for your resources, and network ACLs control inbound and outbound traffic for your subnets. Security groups provide enough access control for most subnets. You can use network ACLs if you want an additional layer of security for your VPC. For general guidelines on security best practices when using Amazon VPCs, see [Security best practices for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html) in the *Amazon Virtual Private Cloud User Guide*.

### Performance best practices
<a name="configuration-vpc-best-practice-performance"></a>

When you attach your function to a VPC, Lambda checks to see if there is an available network resource (Hyperplane ENI) it can use to connect to. Hyperplane ENIs are associated with a particular combination of security groups and VPC subnets. If you’ve already attached one function to a VPC, specifying the same subnets and security groups when you attach another function means that Lambda can share the network resources and avoid the need to create a new Hyperplane ENI. For more information about Hyperplane ENIs and their lifecycle, see [Understanding Hyperplane Elastic Network Interfaces (ENIs)](#configuration-vpc-enis).

## Understanding Hyperplane Elastic Network Interfaces (ENIs)
<a name="configuration-vpc-enis"></a>

A Hyperplane ENI is a managed resource that acts as a network interface between your Lambda function and the resources you want your function to connect to. The Lambda service creates and manages these ENIs automatically when you attach your function to a VPC.

Hyperplane ENIs are not directly visible to you, and you don’t need to configure or manage them. However, knowing how they work can help you to understand your function’s behavior when you attach it to a VPC.

The first time you attach a function to a VPC using a particular subnet and security group combination, Lambda creates a Hyperplane ENI. Other functions in your account that use the same subnet and security group combination can also use this ENI. Wherever possible, Lambda reuses existing ENIs to optimize resource utilization and minimize the creation of new ENIs. Each Hyperplane ENI supports up to 65,000 connections/ports. If the number of connections exceeds this limit, Lambda scales the number of ENIs automatically based on network traffic and concurrency requirements.

For new functions, while Lambda is creating a Hyperplane ENI, your function remains in the Pending state and you can’t invoke it. Your function transitions to the Active state only when the Hyperplane ENI is ready, which can take several minutes. For existing functions, you can’t perform additional operations that target the function, such as creating versions or updating the function’s code, but you can continue to invoke previous versions of the function.

As part of managing the ENI lifecycle, Lambda may delete and recreate ENIs to load balance network traffic across ENIs or to address issues found in ENI health-checks. Additionally, if a Lambda function remains idle for 14 days, Lambda reclaims any unused Hyperplane ENIs and sets the function state to `Inactive`. The next invocation attempt will fail, and the function re-enters the Pending state until Lambda completes the creation or allocation of a Hyperplane ENI. We recommend that your design doesn't rely on the persistence of ENIs.

When you update a function to remove its VPC configuration, Lambda requires up to 20 minutes to delete the attached Hyperplane ENI. Lambda only deletes the ENI if no other function (or published function version) is using that Hyperplane ENI. 

Lambda relies on permissions in the function [ execution role](lambda-intro-execution-role.md) to delete the Hyperplane ENI. If you delete the execution role before Lambda deletes the Hyperplane ENI, Lambda won't be able to delete the Hyperplane ENI. You can manually perform the deletion.

## Using IAM condition keys for VPC settings
<a name="vpc-conditions"></a>

You can use Lambda-specific condition keys for VPC settings to provide additional permission controls for your Lambda functions. For example, you can require that all functions in your organization are connected to a VPC. You can also specify the subnets and security groups that the function's users can and can't use.

Lambda supports the following condition keys in IAM policies:
+ **lambda:VpcIds** – Allow or deny one or more VPCs.
+ **lambda:SubnetIds** – Allow or deny one or more subnets.
+ **lambda:SecurityGroupIds** – Allow or deny one or more security groups.

The Lambda API operations [CreateFunction](https://docs.aws.amazon.com/lambda/latest/api/API_CreateFunction.html) and [UpdateFunctionConfiguration](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateFunctionConfiguration.html) support these condition keys. For more information about using condition keys in IAM policies, see [IAM JSON Policy Elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.

**Tip**  
If your function already includes a VPC configuration from a previous API request, you can send an `UpdateFunctionConfiguration` request without the VPC configuration.

### Example policies with condition keys for VPC settings
<a name="vpc-condition-examples"></a>

The following examples demonstrate how to use condition keys for VPC settings. After you create a policy statement with the desired restrictions, append the policy statement for the target user or role.

#### Ensure that users deploy only VPC-connected functions
<a name="vpc-condition-example-1"></a>

To ensure that all users deploy only VPC-connected functions, you can deny function create and update operations that don't include a valid VPC ID. 

Note that VPC ID is not an input parameter to the `CreateFunction` or `UpdateFunctionConfiguration` request. Lambda retrieves the VPC ID value based on the subnet and security group parameters.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "EnforceVPCFunction",
      "Action": [
          "lambda:CreateFunction",
          "lambda:UpdateFunctionConfiguration"
       ],
      "Effect": "Deny",
      "Resource": "*",
      "Condition": {
        "Null": {
           "lambda:VpcIds": "true"
        }
      }
    }
  ]
}
```

------

#### Deny users access to specific VPCs, subnets, or security groups
<a name="vpc-condition-example-2"></a>

To deny users access to specific VPCs, use `StringEquals` to check the value of the `lambda:VpcIds` condition. The following example denies users access to `vpc-1` and `vpc-2`.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "EnforceOutOfVPC",
            "Action": [
                "lambda:CreateFunction",
                "lambda:UpdateFunctionConfiguration"
            ],
            "Effect": "Deny",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "lambda:VpcIds": [
                        "vpc-1",
                        "vpc-2"
                    ]
                }
            }
        }
    ]
}
```

------

To deny users access to specific subnets, use `StringEquals` to check the value of the `lambda:SubnetIds` condition. The following example denies users access to `subnet-1` and `subnet-2`.

```
{
      "Sid": "EnforceOutOfSubnet",
      "Action": [
          "lambda:CreateFunction",
          "lambda:UpdateFunctionConfiguration"
       ],
      "Effect": "Deny",
      "Resource": "*",
      "Condition": {
        "ForAnyValue:StringEquals": {
            "lambda:SubnetIds": ["subnet-1", "subnet-2"]
        }
      }
    }
```

To deny users access to specific security groups, use `StringEquals` to check the value of the `lambda:SecurityGroupIds` condition. The following example denies users access to `sg-1` and `sg-2`.

```
{
      "Sid": "EnforceOutOfSecurityGroups",
      "Action": [
          "lambda:CreateFunction",
          "lambda:UpdateFunctionConfiguration"
       ],
      "Effect": "Deny",
      "Resource": "*",
      "Condition": {
        "ForAnyValue:StringEquals": {
            "lambda:SecurityGroupIds": ["sg-1", "sg-2"]
        }
      }
    }
  ]
}
```

#### Allow users to create and update functions with specific VPC settings
<a name="vpc-condition-example-3"></a>

To allow users to access specific VPCs, use `StringEquals` to check the value of the `lambda:VpcIds` condition. The following example allows users to access `vpc-1` and `vpc-2`.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "EnforceStayInSpecificVpc",
            "Action": [
                "lambda:CreateFunction",
                "lambda:UpdateFunctionConfiguration"
            ],
            "Effect": "Allow",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "lambda:VpcIds": [
                        "vpc-1",
                        "vpc-2"
                    ]
                }
            }
        }
    ]
}
```

------

To allow users to access specific subnets, use `StringEquals` to check the value of the `lambda:SubnetIds` condition. The following example allows users to access `subnet-1` and `subnet-2`.

```
{
      "Sid": "EnforceStayInSpecificSubnets",
      "Action": [
          "lambda:CreateFunction",
          "lambda:UpdateFunctionConfiguration"
       ],
      "Effect": "Allow",
      "Resource": "*",
      "Condition": {
        "ForAllValues:StringEquals": {
            "lambda:SubnetIds": ["subnet-1", "subnet-2"]
        }
      }
    }
```

To allow users to access specific security groups, use `StringEquals` to check the value of the `lambda:SecurityGroupIds` condition. The following example allows users to access `sg-1` and `sg-2`.

```
{
      "Sid": "EnforceStayInSpecificSecurityGroup",
      "Action": [
          "lambda:CreateFunction",
          "lambda:UpdateFunctionConfiguration"
       ],
      "Effect": "Allow",
      "Resource": "*",
      "Condition": {
        "ForAllValues:StringEquals": {
            "lambda:SecurityGroupIds": ["sg-1", "sg-2"]
        }
      }
    }
  ]
}
```

## VPC tutorials
<a name="vpc-tutorials"></a>

In the following tutorials, you connect a Lambda function to resources in your VPC.
+ [Tutorial: Using a Lambda function to access Amazon RDS in an Amazon VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-lambda-tutorial.html)
+ [Tutorial: Configuring a Lambda function to access Amazon ElastiCache in an Amazon VPC](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/LambdaRedis.html)