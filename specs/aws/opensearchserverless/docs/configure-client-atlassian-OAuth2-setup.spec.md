---
id: "@specs/aws/opensearchserverless/docs/configure-client-atlassian-OAuth2-setup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Connecting an Amazon OpenSearch Ingestion pipeline to Atlassian Jira or Confluence using OAuth 2.0"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Connecting an Amazon OpenSearch Ingestion pipeline to Atlassian Jira or Confluence using OAuth 2.0

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/configure-client-atlassian-OAuth2-setup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Connecting an Amazon OpenSearch Ingestion pipeline to Atlassian Jira or Confluence using OAuth 2.0
<a name="configure-client-atlassian-OAuth2-setup"></a>

Use the information in this topic to help you configure and connect an Amazon OpenSearch Ingestion pipeline to a Jira or Confluence account using OAuth 2.0 authentication. Perform this task when are are completing the [Prerequisites](configure-client-atlassian.md#atlassian-prerequisites) for using an OpenSearch Ingestion pipeline with Atlassian Services but choose not to use API key credentials.

**Topics**
+ [Create an OAuth 2.0 integration app](#create-OAuth2-integration-app)
+ [Generating and refreshing an Atlassian Developer access token](#generate-and-refresh-jira-access-token)

## Create an OAuth 2.0 integration app
<a name="create-OAuth2-integration-app"></a>

Use the following procedure to help you create an OAuth 2.0 integration app on the Atlassian Developer website.

**To create an OAuth 2.0 integration app**

1. Log in to your Atlassian Developer account at [ https://developer.atlassian.com/console/myapps/](https://developer.atlassian.com/console/myapps/).

1. Choose **Create**, **OAuth 2.0 integration**.

1. For **Name**, enter a name to identify the purpose of the app.

1. Select the **I agree to be bound by Atlassian's developer terms** check box, and then choose **Create**.

1. In the left navigation, choose **Authorization**, and then choose **Add**.

1. For **Callback URL**, enter any URL, such as **https://www.amazon.com** or **https://www.example.com**, and then choose **Save changes**.

1. In the left navigation, choose **Permissions** page, and then in the row for Jira API, choose **Add**, and then choose **Configure**. and select all the Classic Scopes Read permissions (list given below) and then select Save

1. Choose the **Granular scopes** tab, and then choose **Edit Scopes** to open the **Edit Jira API** dialog box.

1. Select the permissions for source plugin you are using:

------
#### [ Jira ]

   ```
   read:audit-log:jira
   read:issue:jira
   read:issue-meta:jira
   read:attachment:jira
   read:comment:jira
   read:comment.property:jira
   read:field:jira
   read:field.default-value:jira
   read:field.option:jira
   read:field-configuration-scheme:jira
   read:field-configuration:jira
   read:issue-link:jira
   read:issue-link-type:jira
   read:issue-link-type:jira
   read:issue.remote-link:jira
   read:issue.property:jira
   read:resolution:jira
   read:issue-details:jira
   read:issue-type:jira
   read:issue-worklog:jira
   read:issue-field-values:jira
   read:issue.changelog:jira
   read:issue.transition:jira
   read:issue.vote:jira
   read:jira-expressions:jira
   ```

------
#### [ Confluence ]

   ```
   read:content:confluence
   read:content-details:confluence
   read:space-details:confluence
   read:audit-log:confluence
   read:page:confluence
   read:blogpost:confluence
   read:custom-content:confluence
   read:comment:confluence
   read:space:confluence
   read:space.property:confluence
   read:space.setting:confluence
   read:content.property:confluence
   read:content.metadata:confluence
   read:task:confluence
   read:whiteboard:confluence
   read:app-data:confluence
   manage:confluence-configuration
   ```

------

1. Choose **Save**.

For related information, see [Implementing OAuth 2.0 (3LO)](https://developer.atlassian.com/cloud/oauth/getting-started/implementing-oauth-3lo/) and [Determining the scopes required for an operation](https://developer.atlassian.com/cloud/oauth/getting-started/determining-scopes/) on the Atlassian Developer website.

## Generating and refreshing an Atlassian Developer access token
<a name="generate-and-refresh-jira-access-token"></a>

Use the following procedure to help you generate and refresh an Atlassian Developer access token on the Atlassian Developer website.

**To generate and refresh a Jira access token**

1. Log in to your Atlassian Developer account at [ https://developer.atlassian.com/console/myapps/](https://developer.atlassian.com/console/myapps/).

1. Choose the app you created in [Create an OAuth 2.0 integration app](#create-OAuth2-integration-app).

1. In the left navigation, choose **Authorization.**

1. Copy the granular Atlassian API authorization URL value from the bottom of the page and paste it into the text editor of your choice.

   The format of the URL is as follows:

   ```
   https://auth.atlassian.com/authorize?
   audience=api.atlassian.com 
   &client_id={{YOUR_CLIENT_ID}}
   &scope={{REQUESTED_SCOPE%20REQUESTED_SCOPE_TWO}}
   &redirect_uri=https://{{YOUR_APP_CALLBACK_URL}}
   &state=YOUR_USER_BOUND_VALUE 
   &response_type=code
   &prompt=consent
   ```

1. For `state=YOUR_USER_BOUND_VALUE`, change the parameter value to anything you choose, such as state="**sample\_text**".

   For more information, see [What is the state parameter used for?](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/#what-is-the-state-parameter-used-for-) on the Atlassian Developer website.

1. Note that the `scope` section lists the granular scopes you selected in an earlier task. For example: `scope=read%3Ajira-work%20read%3Ajira-user%20offline_access`

   `offline_access` indicates that you want to generate a `refresh_token`.

1. Open a web browser window and enter the authorization URL you copied into the browser window's address bar.

1. When the target page opens, verify that the information is correct, and then choose **Accept** to be redirected to your Jira or Confluence homepage.

1. After the homepage has loaded, copy the URL of this page. It contains the authorization code for your application. You use this code to generate your access token. The entire section after `code=` is the authorization code.

1. Use the following cURL command to generate the access token. Replace the {{placeholder values}} with your own information.
**Tip**  
You can also use a third-party service such as Postman.

   ```
   curl --request POST --url 'https://auth.atlassian.com/oauth/token' \
   --header 'Content-Type: application/json' \
   --data '{"grant_type": "authorization_code",
   "client_id": "{{YOUR_CLIENT_ID}}",
   "client_secret": "{{YOUR_CLIENT_SECRET}}",
   "code": "{{AUTHORIZATION_CODE}}",
   "redirect_uri": "{{YOUR_CALLBACK_URL}}"}'
   ```

   The response to this command includes the values for `access_code` and `refresh_token`.