---
id: "@specs/aws/opensearchserverless/docs/serverless-iam-identity-center"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS IAM Identity Center support for Amazon OpenSearch Serverless"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# IAM Identity Center support for Amazon OpenSearch Serverless

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-iam-identity-center
> **target_lang:** meta — documentation tier. ALL sections preserved.



# IAM Identity Center support for Amazon OpenSearch Serverless
<a name="serverless-iam-identity-center"></a>

## IAM Identity Center support for Amazon OpenSearch Serverless
<a name="serverless-iam-identity-support"></a>

You can use IAM Identity Center principals (users and groups) to access Amazon OpenSearch Serverless data through Amazon OpenSearch Applications. In order to enable IAM Identity Center support for Amazon OpenSearch Serverless, you will need to enable use of IAM Identity Center. To learn more on how to do this, see [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)

**Note**  
To access Amazon OpenSearch Serverless collections using IAM Identity Center users or groups, you must use the OpenSearch UI (Applications) feature. Direct access to OpenSearch Serverless Dashboards using IAM Identity Center credentials is not supported. For more information, see [Getting started with the OpenSearch user interface](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application.html).

After the IAM Identity Center instance is created, the customer account administrator needs to create an IAM Identity Center application for the Amazon OpenSearch Serverless service. This can be done by calling the [CreateSecurityConfig:](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateSecurityConfig.html). The customer account administrator can specify what attributes will be used for authorizing the request. The default attributes used are `UserId` and `GroupId.`

The IAM Identity Center integration for Amazon OpenSearch Serverless uses the following AWS IAM Identity Center (IAM) permissions:
+ `aoss:CreateSecurityConfig` – Create an IAM Identity Center provider
+ `aoss:ListSecurityConfig` – List all IAM Identity Center providers in the current account.
+ `aoss:GetSecurityConfig` – View IAM Identity Center provider information.
+ `aoss:UpdateSecurityConfig` – Modify a given IAM Identity Center configuration
+ `aoss:DeleteSecurityConfig` – Delete an IAM Identity Centerprovider. 

The following identity-based access policy can be used to manage all IAM Identity Center configurations:

------
#### [ JSON ]

****  

```
{
"Version": "2012-10-17",
    "Statement": [
        {
"Action": [
                "aoss:CreateSecurityConfig",
                "aoss:DeleteSecurityConfig",
                "aoss:GetSecurityConfig",
                "aoss:UpdateSecurityConfig",
                "aoss:ListSecurityConfigs"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

------

**Note**  
The `Resource` element must be a wildcard.

## Creating an IAM Identity Center provider (console)
<a name="serverless-iam-console"></a>

You can create an IAM Identity Center provider to enable authentication with OpenSearch Application. To enable IAM Identity Center authentication for OpenSearch Dashboards, perform the following steps:

1. Sign in to the [Amazon OpenSearch Service console](https://console.aws.amazon.com/aos/home.).

1. On the left navigation panel, expand ** Serverless** and choose **Authentication**.

1. Choose** IAM Identity Center authentication**.

1. Select **Edit**

1. Check the box next to Authenticate with IAM Identity Center.

1. Select the **user and group** attribute key from the dropdown menu. User attributes will be used to authorize users based on `UserName`, `UserId`, and `Email`. Group attributes will be used to authenticate users based on `GroupName` and `GroupId`.

1. Select the **IAM Identity Center** instance.

1. Select **Save**

## Creating IAM Identity Center provider (AWS CLI)
<a name="serverless-iam-identity-center-cli"></a>

To create an IAM Identity Center provider using the AWS Command Line Interface (AWS CLI) use the following command:

```
aws opensearchserverless create-security-config \
--region us-east-2 \
--name "iamidentitycenter-config" \
--description "description" \
--type "iamidentitycenter" \
--iam-identity-center-options '{
    "instanceArn": "arn:aws:sso:::instance/ssoins-99199c99e99ee999",
    "userAttribute": "UserName",                  
    "groupAttribute": "GroupId"
}'
```

After an IAM Identity Center is enabled, customers can only modify **user and group** attributes.

```
aws opensearchserverless update-security-config \
--region us-east-1 \
--id <id_from_list_security_configs> \
--config-version <config_version_from_get_security_config> \
--iam-identity-center-options-updates '{
    "userAttribute": "UserId",
    "groupAttribute": "GroupId"
}'
```

In order to view the IAM Identity Center provider using the AWS Command Line Interface, use the following command:

```
aws opensearchserverless list-security-configs --type iamidentitycenter
```

## Deleting an IAM Identity Center provider
<a name="serverless-iam-identity-center-deleting"></a>

 IAM Identity Center offers two instances of providers, one for your organization account and one for your member account. If you need to change your IAM Identity Center instance, you need to delete your security configuration through the `DeleteSecurityConfig` API and create a new security configuration using the new IAM Identity Center instance. The following command can be used to delete an IAM Identity Center provider:

```
aws opensearchserverless delete-security-config \
--region us-east-1 \
--id <id_from_list_security_configs>
```

## Granting IAM Identity Center access to collection data
<a name="serverless-iam-identity-center-collection-data"></a>

After your IAM Identity Center provider is enabled, you can update the collection data access policy to include IAM Identity Center principals. IAM Identity Center principals need to be updated in the following format: 

```
[
   {
"Rules":[
       ...  
      ],
      "Principal":[
         "iamidentitycenter/<iamidentitycenter-instance-id>/user/<UserName>",
         "iamidentitycenter/<iamidentitycenter-instance-id>/group/<GroupId>"
      ]
   }
]
```

**Note**  
Amazon OpenSearch Serverless supports only one IAM Identity Center instance for all customer collections and can support up to 100 groups for a single user. If you try to use more than the number of allowed instances, you will experience inconsistency with your data access policy authorization processing and receive a `403`error message. 

You can grant access to collections, indexes, or both. If you want different users to have different permssions, you will need to create multiple rules. For a list of available permissions, see [Identity and Access Management in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html). For information about how to format an access policy, see [Granting SAML identities access to collection data ](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-saml.html#serverless-saml-policies). 