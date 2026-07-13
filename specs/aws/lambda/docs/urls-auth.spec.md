---
id: "@specs/aws/lambda/docs/urls-auth"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Access control"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Access control

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/urls-auth
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Control access to Lambda function URLs
<a name="urls-auth"></a>

**Note**  
Starting in October 2025, new function URLs will require both `lambda:InvokeFunctionUrl` and `lambda:InvokeFunction` permissions.

You can control access to your Lambda function URLs using the [AuthType](https://docs.aws.amazon.com/lambda/latest/api/API_CreateFunctionUrlConfig.html#lambda-CreateFunctionUrlConfig-request-AuthType) parameter combined with [resource-based policies](access-control-resource-based.md) attached to your specific function. The configuration of these two components determines who can invoke or perform other administrative actions on your function URL.

The `AuthType` parameter determines how Lambda authenticates or authorizes requests to your function URL. When you configure your function URL, you must specify one of the following `AuthType` options:
+ `AWS_IAM` – Lambda uses AWS Identity and Access Management (IAM) to authenticate and authorize requests based on the IAM principal's identity policy and the function's resource-based policy. Choose this option if you want only authenticated users and roles to invoke your function using the function URL.
+ `NONE` – Lambda doesn't perform any authentication before invoking your function. However, your function's resource-based policy is always in effect and must grant public access before your function URL can receive requests. Choose this option to allow public, unauthenticated access to your function URL.

For additional insights into security, you can use AWS Identity and Access Management Access Analyzer to get a comprehensive analysis of external access to your function URL. IAM Access Analyzer also monitors for new or updated permissions on your Lambda functions to help you identify permissions that grant public and cross-account access. You can use IAM Access Analyzer at no charge. To get started with IAM Access Analyzer, see [Using AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html).

This page contains examples of resource-based policies for both auth types, and how to create these policies using the [AddPermission](https://docs.aws.amazon.com/lambda/latest/api/API_AddPermission.html) API operation or the Lambda console. For information about how to invoke your function URL after you've set up permissions, see [Invoking Lambda function URLs](urls-invocation.md).

**Topics**
+ [Using the `AWS_IAM` auth type](#urls-auth-iam)
+ [Using the `NONE` auth type](#urls-auth-none)
+ [Governance and access control](#urls-governance)

## Using the `AWS_IAM` auth type
<a name="urls-auth-iam"></a>

If you choose the `AWS_IAM` auth type, users who need to invoke your Lambda function URL must have the `lambda:InvokeFunctionUrl` and `lambda:InvokeFunction` permissions. Depending on who makes the invocation request, you might have to grant this permission using a [resource-based policy](access-control-resource-based.md).

If the principal making the request is in the same AWS account as the function URL, then the principal must **either** have `lambda:InvokeFunctionUrl` and `lambda:InvokeFunction` permissions in their [identity-based policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html), **or** have permissions granted to them in the function's resource-based policy. In other words, a resource-based policy is optional if the user already has `lambda:InvokeFunctionUrl` and `lambda:InvokeFunction` permissions in their identity-based policy. Policy evaluation follows the rules outlined in [Policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html).

If the principal making the request is in a different account, then the principal must have **both** an identity-based policy that gives them `lambda:InvokeFunctionUrl` and `lambda:InvokeFunction` permissions **and** permissions granted to them in a resource-based policy on the function that they are trying to invoke. Policy evaluation follows the rules outlined in [Determining whether a cross-account request is allowed](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic-cross-account.html#policy-eval-cross-account).

The following resource-based policy allows the `example` role in AWS account `444455556666` to invoke the function URL associated with function `my-function`. The [lambda:InvokedViaFunctionUrl](https://docs.aws.amazon.com/lambda/latest/api/API_AddPermission.html#lambda-AddPermission-request-InvokedViaFunctionUrl) context key restricts the `lambda:InvokeFunction` action to function URL calls. This means that the principal must use the function URL to invoke the function. If you don't include `lambda:InvokedViaFunctionUrl`, the principal can invoke your function through other invocation methods, in addition to the function URL.

**Example — Cross-account resource-based policy**    
****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::444455556666:role/example"
      },
      "Action": "lambda:InvokeFunctionUrl",
      "Resource": "arn:aws:lambda:us-east-1:123456789012:function:my-function",
      "Condition": {
        "StringEquals": {
          "lambda:FunctionUrlAuthType": "AWS_IAM"
        }
      }
    },
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::444455556666:role/example"
      },
      "Action": "lambda:InvokeFunction",
      "Resource": "arn:aws:lambda:us-east-1:123456789012:function:my-function",
      "Condition": {
        "Bool": {
          "lambda:InvokedViaFunctionUrl": "true"
        }
      }
    }
  ]
}
```

You can create this resource-based policy through the console using the following steps:

**To grant URL invocation permissions to another account (console)**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the name of the function that you want to grant URL invocation permissions for.

1. Choose the **Configuration** tab, and then choose **Permissions**.

1. Under **Resource-based policy**, choose **Add permissions**.

1. Choose **Function URL**.

1. For **Auth type**, choose **AWS\_IAM**.

1. Enter a **Statement ID** for your policy statement.

1. For **Principal**, enter the account ID or the Amazon Resource Name (ARN) of the user or role that you want to grant permissions to. For example: **444455556666**.

1. Choose **Save**.

Alternatively, you can create this policy using the following [add-permission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/add-permission.html) AWS Command Line Interface (AWS CLI) commands. When you use the AWS CLI, you must add the `lambda:InvokeFunctionUrl` and `lambda:InvokeFunction` statements separately. For example:

```
aws lambda add-permission --function-name my-function \
  --statement-id UrlPolicyInvokeURL \
  --action {{lambda:InvokeFunctionUrl}} \
  --principal 444455556666 \
  --function-url-auth-type AWS_IAM
```

```
aws lambda add-permission --function-name my-function \
  --statement-id UrlPolicyInvokeFunction \
  --action {{lambda:InvokeFunction}} \
  --principal 444455556666 \
  --invoked-via-function-url
```

## Using the `NONE` auth type
<a name="urls-auth-none"></a>

**Important**  
When your function URL auth type is `NONE` and you have a [resource-based policy](access-control-resource-based.md) that grants public access, any unauthenticated user with your function URL can invoke your function.

In some cases, you might want your function URL to be public. For example, you might want to serve requests made directly from a web browser. To allow public access to your function URL, choose the `NONE` auth type.

If you choose the `NONE` auth type, Lambda doesn't use IAM to authenticate requests to your function URL. However, your function must have a resource-based policy that allows `lambda:InvokeFunctionUrl` and `lambda:InvokeFunction`. When you create a function URL with auth type `NONE` using the console or AWS Serverless Application Model (AWS SAM), Lambda automatically creates the resource-based policy for you. If you're using the AWS CLI, AWS CloudFormation, or the Lambda API directly, you must [add the policy yourself](#policy-cli).

We recommend that you include the [lambda:InvokedViaFunctionUrl](https://docs.aws.amazon.com/lambda/latest/api/API_AddPermission.html#lambda-AddPermission-request-InvokedViaFunctionUrl) context key in your resource-based policies when using the `NONE` auth type. This context key ensures that the function can only be invoked through the function URL and not through other invocation methods.

Note the following about this policy:
+ All entities can call `lambda:InvokeFunctionUrl` and `lambda:InvokeFunction`. This means that anyone who has your function URL can invoke your function.
+ The `lambda:FunctionUrlAuthType` condition key value is `NONE`. This means that the policy statement allows access only when your function URL's auth type is also `NONE`.
+ The `lambda:InvokedViaFunctionUrl` condition ensures that the function can only be invoked through the function URL and not through other invocation methods.

**Example — Default resource-based policy for NONE auth type**    
****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "FunctionURLAllowPublicAccess",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "lambda:InvokeFunctionUrl",
      "Resource": "arn:aws:lambda:us-east-2:123456789012:function:my-function",
      "Condition": {
        "StringEquals": {
          "lambda:FunctionUrlAuthType": "NONE"
        }
      }
    },
    {
      "Sid": "FunctionURLInvokeAllowPublicAccess",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "lambda:InvokeFunction",
      "Resource": "arn:aws:lambda:us-east-2:123456789012:function:my-function",
      "Condition": {
        "Bool": {
          "lambda:InvokedViaFunctionUrl": "true"
        }
      }
    }
  ]
}
```

**Create the resource-based policy using the AWS CLI**  
Unless you use the console or AWS SAM to create a function URL with auth type `NONE`, you must add the resource-based policy yourself. Use the following commands to create statements for the `lambda:InvokeFunctionUrl` and `lambda:InvokeFunction` permissions. Each statement must be added in a separate command.

```
aws lambda add-permission \
  --function-name UrlTestFunction \
  --statement-id UrlPolicyInvokeURL \
  --action {{lambda:InvokeFunctionUrl}} \
  --principal * \
  --function-url-auth-type NONE
```

```
aws lambda add-permission \
  --function-name UrlTestFunction \
  --statement-id UrlPolicyInvokeFunction \
  --action {{lambda:InvokeFunction}} \
  --principal * \
  --invoked-via-function-url
```

**Note**  
If you delete a function URL with auth type `NONE`, Lambda doesn't automatically delete the associated resource-based policy. If you want to delete this policy, you must manually do so.

If a function's resource-based policy doesn't grant `lambda:invokeFunctionUrl` and `lambda:InvokeFunction` permissions, users will get a 403 Forbidden error code when they try to invoke your function URL. This will occur even if the function URL uses the `NONE` auth type.

## Governance and access control
<a name="urls-governance"></a>

In addition to function URL invocation permissions, you can also control access on actions used to configure function URLs. Lambda supports the following IAM policy actions for function URLs:
+ `lambda:InvokeFunctionUrl` – Invoke a Lambda function using the function URL.
+ `lambda:CreateFunctionUrlConfig` – Create a function URL and set its `AuthType`.
+ `lambda:UpdateFunctionUrlConfig` – Update a function URL configuration and its `AuthType`.
+ `lambda:GetFunctionUrlConfig` – View the details of a function URL.
+ `lambda:ListFunctionUrlConfigs` – List function URL configurations.
+ `lambda:DeleteFunctionUrlConfig` – Delete a function URL.

To allow or deny function URL access to other AWS entities, include these actions in IAM policies. For example, the following policy grants the `example` role in AWS account `444455556666` permissions to update the function URL for function **my-function** in account `123456789012`.

**Example cross-account function URL policy**    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": { 
                "AWS": "arn:aws:iam::444455556666:role/example"
            },
            "Action": "lambda:UpdateFunctionUrlConfig",
            "Resource": "arn:aws:lambda:us-east-2:123456789012:function:{{my-function}}"
        }
    ]
}
```

### Condition keys
<a name="urls-condition-keys"></a>

For fine-grained access control over your function URLs, use condition context keys. Lambda supports the following context keys for function URLs:
+ `lambda:FunctionUrlAuthType` – Defines an enum value describing the auth type that your function URL uses. The value can be either `AWS_IAM` or `NONE`.
+ `lambda:InvokedViaFunctionUrl` – Restricts the `lambda:InvokeFunction` action to calls made through the function URL. This ensures that the function can only be invoked using the function URL and not through other invocation methods. For examples of resource-based policies that use the `lambda:InvokedViaFunctionUrl` context key, see the examples in [Using the `AWS_IAM` auth type](#urls-auth-iam) and [Using the `NONE` auth type](#urls-auth-none).

You can use these context keys in policies associated with your function. For example, you might want to restrict who can make configuration changes to your function URLs. To deny all `UpdateFunctionUrlConfig` requests to any function with URL auth type `NONE`, you can define the following policy:

**Example function URL policy with explicit deny**    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Deny",
            "Principal": "*",
            "Action":[
                "lambda:UpdateFunctionUrlConfig"
            ],
            "Resource": "arn:aws:lambda:us-east-1:123456789012:function:*",
            "Condition": {
                "StringEquals": {
                    "lambda:FunctionUrlAuthType": "NONE"
                }
            }
        }
    ]
}
```

To grant the `example` role in AWS account `444455556666` permissions to make `CreateFunctionUrlConfig` and `UpdateFunctionUrlConfig` requests on functions with URL auth type `AWS_IAM`, you can define the following policy:

**Example function URL policy with explicit allow**    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": { 
                "AWS": "arn:aws:iam::444455556666:role/example"
            },
            "Action":[
                "lambda:CreateFunctionUrlConfig",
                "lambda:UpdateFunctionUrlConfig"
            ],
            "Resource": "arn:aws:lambda:us-east-1:123456789012:function:*",
            "Condition": {
                "StringEquals": {
                    "lambda:FunctionUrlAuthType": "AWS_IAM"
                }
            }
        }
    ]
}
```

You can also use this condition key in a [service control policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) (SCP). Use SCPs to manage permissions across an entire organization in AWS Organizations. For example, to deny users from creating or updating function URLs that use anything other than the `AWS_IAM` auth type, use the following service control policy:

**Example function URL SCP with explicit deny**    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Deny",
            "Action":[
                "lambda:CreateFunctionUrlConfig",
                "lambda:UpdateFunctionUrlConfig"
            ],
            "Resource": "arn:aws:lambda:*:123456789012:function:*",
            "Condition": {
                "StringNotEquals": {
                    "lambda:FunctionUrlAuthType": "AWS_IAM"
                }
            }
        }
    ]
}
```