---
id: "@specs/aws/timestream-influxdb/docs/JDBC.withAzureAD.setUp"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Setting up Azure AD"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Setting up Azure AD

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/JDBC.withAzureAD.setUp
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Setting up Azure AD
<a name="JDBC.withAzureAD.setUp"></a>

1. Sign in to Azure Portal

1. Choose **Azure Active Directory** in the list of Azure services. This will redirect to the Default Directory page.

1. Choose **Enterprise Applications** under the **Manage** section on the sidebar

1. Choose **\+ New application**.

1. Find and select **Amazon Web Services**.

1. Choose **Single Sign-On** under the **Manage** section in the sidebar

1. Choose **SAML** as the single sign-on method

1. In the Basic SAML Configuration section, enter the following URL for both the Identifier and the Reply URL:

   ```
   https://signin.aws.amazon.com/saml
   ```

1. Choose **Save**

1. Download the Federation Metadata XML in the SAML Signing Certificate section. This will be used when creating the IAM Identity Provider later

1. Return to the Default Directory page and choose **App registrations** under **Manage**.

1. Choose **Timestream for LiveAnalytics** from the **All Applications** section. The page will be redirected to the application's Overview page
**Note**  
Note the Application (client) ID and the Directory (tenant) ID. These values are required for when creating a connection.

1. Choose **Certificates and Secrets**

1. Under **Client secrets**, create a new client secret with **\+ New client secret**.
**Note**  
Note the generated client secret, as this is required when creating a connection to Timestream for LiveAnalytics.

1. On the sidebar under **Manage**, select **API permissions**

1. In the **Configured permissions**, use **Add a permission** to grant Azure AD permission to sign in to Timestream for LiveAnalytics. Choose **Microsoft Graph** on the Request API permissions page.

1. Choose **Delegated permissions** and select the **User.Read **permission

1. Choose **Add permissions**

1. Choose **Grant admin consent for Default Directory**