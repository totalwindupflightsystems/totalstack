---
id: "@specs/aws/quicksight/docs/API_CreateOAuthClientApplication"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateOAuthClientApplication"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateOAuthClientApplication

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateOAuthClientApplication
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateOAuthClientApplication
<a name="API_CreateOAuthClientApplication"></a>

Creates an OAuthClientApplication.

## Request Syntax
<a name="API_CreateOAuthClientApplication_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/oauth-client-applications HTTP/1.1
Content-type: application/json

{
   "ClientId": "{{string}}",
   "ClientSecret": "{{string}}",
   "DataSourceType": "{{string}}",
   "IdentityProviderVpcConnectionProperties": { 
      "VpcConnectionArn": "{{string}}"
   },
   "Name": "{{string}}",
   "OAuthAuthorizationEndpointUrl": "{{string}}",
   "OAuthClientApplicationId": "{{string}}",
   "OAuthClientAuthenticationType": "{{string}}",
   "OAuthScopes": "{{string}}",
   "OAuthTokenEndpointUrl": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateOAuthClientApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateOAuthClientApplication_RequestSyntax) **   <a name="QS-CreateOAuthClientApplication-request-uri-AwsAccountId"></a>
The AWS account ID.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_CreateOAuthClientApplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientId](#API_CreateOAuthClientApplication_RequestSyntax) **   <a name="QS-CreateOAuthClientApplication-request-ClientId"></a>
The client ID of the OAuth application that is registered with the identity provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[^\p{Cc}]+`   
Required: Yes

 ** [ClientSecret](#API_CreateOAuthClientApplication_RequestSyntax) **   <a name="QS-CreateOAuthClientApplication-request-ClientSecret"></a>
The client secret of the OAuth application that is registered with the identity provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[^\p{Cc}]+`   
Required: Yes

 ** [Name](#API_CreateOAuthClientApplication_RequestSyntax) **   <a name="QS-CreateOAuthClientApplication-request-Name"></a>
The display name for the OAuthClientApplication.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

 ** [OAuthClientApplicationId](#API_CreateOAuthClientApplication_RequestSyntax) **   <a name="QS-CreateOAuthClientApplication-request-OAuthClientApplicationId"></a>
An ID for the OAuthClientApplication that you want to create. This ID is unique per AWS Region for each AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[^/][^\p{Cc}]*`   
Required: Yes

 ** [OAuthClientAuthenticationType](#API_CreateOAuthClientApplication_RequestSyntax) **   <a name="QS-CreateOAuthClientApplication-request-OAuthClientAuthenticationType"></a>
The authentication type to use for the OAuthClientApplication. This determines the OAuth 2.0 grant flow that is used when the data source connects to the identity provider. Valid values are `TOKEN`.  
Type: String  
Valid Values: `TOKEN`   
Required: Yes

 ** [OAuthTokenEndpointUrl](#API_CreateOAuthClientApplication_RequestSyntax) **   <a name="QS-CreateOAuthClientApplication-request-OAuthTokenEndpointUrl"></a>
The token endpoint URL of the identity provider that is used to obtain access tokens.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^https://[^\p{Cc}]+`   
Required: Yes

 ** [DataSourceType](#API_CreateOAuthClientApplication_RequestSyntax) **   <a name="QS-CreateOAuthClientApplication-request-DataSourceType"></a>
The type of data source that the OAuthClientApplication is used with. Valid values are `SNOWFLAKE`.  
Type: String  
Valid Values: `ADOBE_ANALYTICS | AMAZON_ELASTICSEARCH | ATHENA | AURORA | AURORA_POSTGRESQL | AWS_IOT_ANALYTICS | GITHUB | JIRA | MARIADB | MYSQL | ORACLE | POSTGRESQL | PRESTO | REDSHIFT | S3 | S3_TABLES | SALESFORCE | SERVICENOW | SNOWFLAKE | SPARK | SQLSERVER | TERADATA | TWITTER | TIMESTREAM | AMAZON_OPENSEARCH | EXASOL | DATABRICKS | STARBURST | TRINO | BIGQUERY | GOOGLESHEETS | GOOGLE_DRIVE | CONFLUENCE | SHAREPOINT | ONE_DRIVE | WEB_CRAWLER | S3_KNOWLEDGE_BASE | QBUSINESS`   
Required: No

 ** [IdentityProviderVpcConnectionProperties](#API_CreateOAuthClientApplication_RequestSyntax) **   <a name="QS-CreateOAuthClientApplication-request-IdentityProviderVpcConnectionProperties"></a>
VPC connection properties.  
Type: [VpcConnectionProperties](API_VpcConnectionProperties.md) object  
Required: No

 ** [OAuthAuthorizationEndpointUrl](#API_CreateOAuthClientApplication_RequestSyntax) **   <a name="QS-CreateOAuthClientApplication-request-OAuthAuthorizationEndpointUrl"></a>
The authorization endpoint URL of the identity provider that is used to obtain authorization codes.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^https://[^\p{Cc}]+`   
Required: No

 ** [OAuthScopes](#API_CreateOAuthClientApplication_RequestSyntax) **   <a name="QS-CreateOAuthClientApplication-request-OAuthScopes"></a>
The OAuth scopes that are requested when the OAuthClientApplication obtains an access token from the identity provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `[^\p{Cc}]+`   
Required: No

 ** [Tags](#API_CreateOAuthClientApplication_RequestSyntax) **   <a name="QS-CreateOAuthClientApplication-request-Tags"></a>
Contains a map of the key-value pairs for the resource tag or tags assigned to the OAuthClientApplication.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateOAuthClientApplication_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "CreationStatus": "string",
   "OAuthClientApplicationId": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_CreateOAuthClientApplication_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateOAuthClientApplication_ResponseSyntax) **   <a name="QS-CreateOAuthClientApplication-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateOAuthClientApplication_ResponseSyntax) **   <a name="QS-CreateOAuthClientApplication-response-Arn"></a>
The Amazon Resource Name (ARN) of the OAuthClientApplication.  
Type: String

 ** [CreationStatus](#API_CreateOAuthClientApplication_ResponseSyntax) **   <a name="QS-CreateOAuthClientApplication-response-CreationStatus"></a>
The status of creating the OAuthClientApplication.  
Type: String  
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED` 

 ** [OAuthClientApplicationId](#API_CreateOAuthClientApplication_ResponseSyntax) **   <a name="QS-CreateOAuthClientApplication-response-OAuthClientApplicationId"></a>
The ID of the OAuthClientApplication. This ID is unique per AWS Region for each AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[^/][^\p{Cc}]*` 

 ** [RequestId](#API_CreateOAuthClientApplication_ResponseSyntax) **   <a name="QS-CreateOAuthClientApplication-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_CreateOAuthClientApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **   
Updating or deleting a resource can cause an inconsistent state.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **   
An internal failure occurred.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **   
A limit is exceeded.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
Limit exceeded.
HTTP Status Code: 409

 ** ResourceExistsException **   
The resource specified already exists.     
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 409

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_CreateOAuthClientApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateOAuthClientApplication) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateOAuthClientApplication) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateOAuthClientApplication) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateOAuthClientApplication) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateOAuthClientApplication) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateOAuthClientApplication) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateOAuthClientApplication) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateOAuthClientApplication) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateOAuthClientApplication) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateOAuthClientApplication) 