---
id: "@specs/aws/appconfig/docs/appconfig-agent-how-to-use-additional-features-multi-account"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring AWS AppConfig Agent to retrieve configurations from multiple accounts"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Configuring AWS AppConfig Agent to retrieve configurations from multiple accounts

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-agent-how-to-use-additional-features-multi-account
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring AWS AppConfig Agent to retrieve configurations from multiple accounts
<a name="appconfig-agent-how-to-use-additional-features-multi-account"></a>

You can configure AWS AppConfig Agent to retrieve configurations from multiple AWS accounts by entering credential overrides in the AWS AppConfig Agent manifest. *Credential overrides* include the Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role, a role ID, a session name, and a duration for how long the agent can assume the role. 

You enter these details in a "credentials" section in the manifest. The "credentials" section uses the following format:

```
{
    "{{application_name}}:{{environment_name}}:{{configuration_name}}": {
        "credentials": {
            "roleArn": "arn:{{partition}}:iam::{{account_ID}}:role/roleName",
            "roleExternalId": "{{string}}",
            "roleSessionName": "{{string}}",
            "credentialsDuration": "{{time_in_hours}}" 
        }
    }
}
```

Here is an example:

```
{
    "My2ndApp:Beta:MyEnableMobilePaymentsFeatureFlagConfiguration": {
        "credentials": {
            "roleArn": "arn:aws:us-west-1:iam::123456789012:role/MyTestRole",
            "roleExternalId": "00b148e2-4ea4-46a1-ab0f-c422b54d0aac",
            "roleSessionName": "AWSAppConfigAgent",
            "credentialsDuration": "2h" 
        }
    }
}
```

Before retrieving a configuration, the agent reads the credential details for the configuration from the manifest and then assumes the IAM role specified for that configuration. You can specify a different set of credential overrides for different configurations in a single manifest. The following diagram shows how AWS AppConfig Agent, while running in Account A (the retrieval account), assumes separate roles specified for Accounts B and C (the vendor accounts) and then calls the [GetLatestConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html) API operation to retrieve configuration data from AWS AppConfig running in those accounts:

![How AWS AppConfig Agent works with IAM roles across separate AWS accounts.](http://docs.aws.amazon.com/appconfig/latest/userguide/images/agent multi-account.png)


## Configure permissions to retrieve configuration data from vendor accounts
<a name="appconfig-agent-how-to-use-additional-features-multi-account-permission"></a>

AWS AppConfig Agent running in the retrieval account needs permission to retrieve configuration data from the vendor accounts. You give the agent permission by creating an AWS Identity and Access Management (IAM) role in each of the vendor accounts. AWS AppConfig Agent in the retrieval account assumes this role to get data from vendor accounts. Complete the procedures in this section to create an IAM permissions policy, an IAM role, and add agent overrides to the manifest.

**Before you begin**  
Collect the following information before you create a permission policy and a role in IAM.
+ The IDs for each AWS account. The *retrieval* account is the account that will call other accounts for configuration data. The *vendor* accounts are the accounts that will vend configuration data to the retrieval account.
+ The name of the IAM role used by AWS AppConfig in the retrieval account. Here's a list of the roles used by AWS AppConfig, by default:
  + For Amazon Elastic Compute Cloud (Amazon EC2), AWS AppConfig uses the instance role.
  + For AWS Lambda, AWS AppConfig uses the Lambda execution role.
  + For Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS), AWS AppConfig uses the container role.

  If you configured AWS AppConfig Agent to use a different IAM role by specifying the `ROLE_ARN` environment variable, make a note of that name.

**Create the permissions policy**  
Use the following procedure to create a permissions policy using the IAM console. Complete the procedure in each AWS account that will vend configuration data for the retrieval account.

**To create an IAM policy**

1. Sign in to the AWS Management Console in a vendor account.

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**, and then choose **Create policy**.

1. Choose the **JSON** option.

1. In the **Policy editor**, replace the default JSON with the following policy statement. Update each {{example resource placeholder}} with vendor account details.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "appconfig:StartConfigurationSession",
                   "appconfig:GetLatestConfiguration"
               ],
               "Resource": "arn:aws:appconfig:{{us-east-1}}:{{111122223333}}:application/{{vendor_application_ID}}/environment/{{vendor_environment_ID}}/configuration/{{vendor_configuration_ID}}"
           }
       ]
   }
   ```

------

   Here's an example:

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [{
           "Effect": "Allow",
           "Action": [
               "appconfig:StartConfigurationSession",
               "appconfig:GetLatestConfiguration"
           ],
           "Resource": "arn:aws:appconfig:us-east-2:{{111122223333}}:application/abc123/environment/def456/configuration/hij789"
       }
      ]
   }
   ```

------

1. Choose **Next**.

1. In the **Policy name** field, enter a name.

1. (Optional) For **Add tags**, add one or more tag-key value pairs to organize, track, or control access for this policy.

1. Choose **Create policy**. The system returns you to the **Policies** page.

1. Repeat this procedure in each AWS account that will vend configuration data for the retrieval account.

**Create the IAM role**  
Use the following procedure to create an IAM role using the IAM console. Complete the procedure in each AWS account that will vend configuration data for the retrieval account.

**To create an IAM role**

1. Sign in to the AWS Management Console in a vendor account.

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**, and then choose **Create policy**.

1. For **Trusted entity type**, choose **AWS account**.

1. In the **AWS account** section, choose **Another AWS account**.

1. In the **Account ID** field, enter the retrieval account ID.

1. (Optional) As a security best practice for this assume role, choose **Require external ID** and enter a string.

1. Choose **Next**.

1. On the **Add permissions** page, use the **Search** field to locate the policy you created in the previous procedure. Select the check box next to its name. 

1. Choose **Next**.

1. For **Role name**, enter a name.

1. (Optional) For **Description**, enter a description.

1. For **Step 1: Select trusted entities**, choose **Edit**. Replace the default JSON trust policy with the following policy. Update each {{example resource placeholder}} with information from your retrieval account.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "AWS": "arn:aws:iam::{{111122223333}}:role/{{appconfig_role_in_retrieval_account}}"
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }
   ```

------

1. (Optional) For **Tags**, add one or more tag-key value pairs to organize, track, or control access for this role.

1. Choose **Create role**. The system returns you to the **Roles** page.

1. Search for the role you just created. Choose it. In the **ARN** section, copy the ARN. You'll specify this information in the next procedure.

**Add credential overrides to the manifest**  
After you create the IAM role in your vendor account, update the manifest in the retrieval account. Specifically, add the credentials block and the IAM role ARN for retrieving configuration data from the vendor account. Here is the JSON format:

```
{
    "{{vendor_application_name}}:{{vendor_environment_name}}:{{vendor_configuration_name}}": {
        "credentials": {
            "roleArn": "arn:{{partition}}:iam::{{vendor_account_ID}}:role/{{name_of_role_created_in_vendor_account}}",
            "roleExternalId": "{{string}}",
            "roleSessionName": "{{string}}",
            "credentialsDuration": "{{time_in_hours}}" 
        }
    }
}
```

Here is an example:

```
{
    "My2ndApp:Beta:MyEnableMobilePaymentsFeatureFlagConfiguration": {
        "credentials": {
            "roleArn": "arn:aws:us-west-1:iam::123456789012:role/MyTestRole",
            "roleExternalId": "00b148e2-4ea4-46a1-ab0f-c422b54d0aac",
            "roleSessionName": "AwsAppConfigAgent",
            "credentialsDuration": "2h" 
        }
    }
}
```

**Validate that multi-account retrieval is working**  
You can validate that that agent is able to retrieve configuration data from multiple accounts by reviewing the AWS AppConfig agent logs. The `INFO` level log for retrieved initial data for '`YourApplicationName`:`YourEnvironmentName`:`YourConfigurationName`' is the best indicator for successful retrievals. If retrievals are failing, you should see an `ERROR` level log indicating the failure reason. Here is an example for a successful retrieval from a vendor account:

```
[appconfig agent] 2023/11/13 11:33:27 INFO AppConfig Agent 2.0.x
[appconfig agent] 2023/11/13 11:33:28 INFO serving on localhost:2772
[appconfig agent] 2023/11/13 11:33:28 INFO retrieved initial data for 'MyTestApplication:MyTestEnvironment:MyDenyListConfiguration' in XX.Xms
```