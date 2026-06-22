---
id: "@specs/aws/timestream-influxdb/docs/JDBC.withAzureAD.IAM"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Setting up IAM Identity Provider and roles"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Setting up IAM Identity Provider and roles

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/JDBC.withAzureAD.IAM
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Setting up IAM Identity Provider and roles in AWS
<a name="JDBC.withAzureAD.IAM"></a>

 Complete each section below to set up IAM for Timestream for LiveAnalytics JDBC single sign-on authentication with Microsoft Azure AD: 

**Topics**
+ [Create a SAML Identity Provider](#JDBC.withAzureAD.IAM.SAML)
+ [Create an IAM role](#JDBC.withAzureAD.IAM.roleForIAM)
+ [Create an IAM policy](#JDBC.withAzureAD.IAM.policyForIAM)
+ [Provisioning](#JDBC.withAzureAD.IAM.provisioning)

## Create a SAML Identity Provider
<a name="JDBC.withAzureAD.IAM.SAML"></a>

To create a SAML Identity Provider for the Timestream for LiveAnalytics JDBC single sign-on authentication with Microsoft Azure AD, complete the following steps:

1. Sign in to the AWS Management Console

1. Choose **Services** and select **IAM** under Security, Identity, & Compliance

1. Choose **Identity providers** under Access management

1. Choose **Create Provider** and choose **SAML** as the provider type. Enter the **Provider Name**. This example will use AzureADProvider.

1. Upload the previously downloaded Federation Metadata XML file

1. Choose **Next**, then choose **Create**.

1. Upon completion, the page will be redirected back to the Identity providers page

## Create an IAM role
<a name="JDBC.withAzureAD.IAM.roleForIAM"></a>

To create an IAM role for the Timestream for LiveAnalytics JDBC single sign-on authentication with Microsoft Azure AD, complete the following steps:

1. On the sidebar select **Roles** under Access management

1. Choose Create role

1. Choose **SAML 2.0 federation** as the trusted entity

1. Choose the **Azure AD provider**

1. Choose **Allow programmatic and AWS Management Console access**

1. Choose **Next: Permissions**

1. Attach permissions policies or continue to Next:Tags

1. Add optional tags or continue to Next:Review

1. Enter a Role name. This example will use AzureSAMLRole

1. Provide a role description

1. Choose **Create Role** to complete

## Create an IAM policy
<a name="JDBC.withAzureAD.IAM.policyForIAM"></a>

To create an IAM policy for the Timestream for LiveAnalytics JDBC single sign-on authentication with Microsoft Azure AD complete the following steps:

1. On the sidebar, choose **Policies** under Access management

1. Choose **Create policy** and select the **JSON** tab

1. Add the following policy

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
                    "iam:ListRoles",
                    "iam:ListAccountAliases"
              ],
              "Resource": "*"
         }
   ]
   }
   ```

------

1. Choose **Create policy**

1. Enter a policy name. This example will use TimestreamAccessPolicy.

1. Choose **Create Policy**

1. On the sidebar, choose **Roles** under Access management. 

1.  Choose the previously created **Azure AD role** and choose **Attach policies** under Permissions.

1. Select the previously created access policy.

## Provisioning
<a name="JDBC.withAzureAD.IAM.provisioning"></a>

To provision the identity provider for Timestream for LiveAnalytics JDBC single sign-on authentication with Microsoft Azure AD, complete the following steps:

1. Go back to Azure Portal

1. Choose **Azure Active Directory** in the list of Azure services. This will redirect to the Default Directory page

1. Choose **Enterprise Applications** under the Manage section on the sidebar

1. Choose **Provisioning**

1. Choose **Automatic mode** for the Provisioning Method

1. Under Admin Credentials, enter your **AwsAccessKeyID** for clientsecret, and **SecretAccessKey** for Secret Token

1. Set the **Provisioning Status** to **On**

1. Choose **save**. This allows Azure AD to load the necessary IAM Roles

1. Once the Current cycle status is completed, choose **Users and groups** on the sidebar

1. Choose **\+ Add user**

1. Choose the Azure AD user to provide access to Timestream for LiveAnalytics

1. Choose the IAM Azure AD role and the corresponding Azure Identity Provider created in AWS

1. Choose **Assign**