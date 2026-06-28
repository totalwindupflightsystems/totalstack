---
id: "@specs/aws/quicksight/docs/API_CreateActionConnector"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateActionConnector"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateActionConnector

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateActionConnector
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateActionConnector
<a name="API_CreateActionConnector"></a>

Creates an action connector that enables Amazon Quick Sight to connect to external services and perform actions. Action connectors support various authentication methods and can be configured with specific actions from supported connector types like Amazon S3, Salesforce, JIRA.

## Request Syntax
<a name="API_CreateActionConnector_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/action-connectors HTTP/1.1
Content-type: application/json

{
   "ActionConnectorId": "{{string}}",
   "AuthenticationConfig": { 
      "AuthenticationMetadata": { ... },
      "AuthenticationType": "{{string}}"
   },
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Permissions": [ 
      { 
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ],
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Type": "{{string}}",
   "VpcConnectionArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateActionConnector_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateActionConnector_RequestSyntax) **   <a name="QS-CreateActionConnector-request-uri-AwsAccountId"></a>
The AWS account ID associated with the action connector.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_CreateActionConnector_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ActionConnectorId](#API_CreateActionConnector_RequestSyntax) **   <a name="QS-CreateActionConnector-request-ActionConnectorId"></a>
A unique identifier for the action connector. This ID must be unique within the AWS account. The `ActionConnectorId` must not start with the prefix `quicksuite-`   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [AuthenticationConfig](#API_CreateActionConnector_RequestSyntax) **   <a name="QS-CreateActionConnector-request-AuthenticationConfig"></a>
The authentication configuration for connecting to the external service. This includes the authentication type, base URL, and authentication metadata such as client credentials or API keys.  
Type: [AuthConfig](API_AuthConfig.md) object  
Required: Yes

 ** [Name](#API_CreateActionConnector_RequestSyntax) **   <a name="QS-CreateActionConnector-request-Name"></a>
A descriptive name for the action connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z0-9](?:[\w- ]*[A-Za-z0-9])?`   
Required: Yes

 ** [Type](#API_CreateActionConnector_RequestSyntax) **   <a name="QS-CreateActionConnector-request-Type"></a>
The type of action connector.  
Type: String  
Valid Values: `GENERIC_HTTP | SERVICENOW_NOW_PLATFORM | SALESFORCE_CRM | MICROSOFT_OUTLOOK | PAGERDUTY_ADVANCE | JIRA_CLOUD | ATLASSIAN_CONFLUENCE | AMAZON_S3 | AMAZON_BEDROCK_AGENT_RUNTIME | AMAZON_BEDROCK_RUNTIME | AMAZON_BEDROCK_DATA_AUTOMATION_RUNTIME | AMAZON_TEXTRACT | AMAZON_COMPREHEND | AMAZON_COMPREHEND_MEDICAL | MICROSOFT_ONEDRIVE | MICROSOFT_SHAREPOINT | MICROSOFT_TEAMS | SAP_BUSINESSPARTNER | SAP_PRODUCTMASTERDATA | SAP_PHYSICALINVENTORY | SAP_BILLOFMATERIALS | SAP_MATERIALSTOCK | ZENDESK_SUITE | SMARTSHEET | SLACK | ASANA | BAMBOO_HR`   
Required: Yes

 ** [Description](#API_CreateActionConnector_RequestSyntax) **   <a name="QS-CreateActionConnector-request-Description"></a>
An optional description of the action connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[A-Za-z0-9 _.,!?-]*`   
Required: No

 ** [Permissions](#API_CreateActionConnector_RequestSyntax) **   <a name="QS-CreateActionConnector-request-Permissions"></a>
The permissions configuration that defines which users, groups, or namespaces can access this action connector and what operations they can perform.  
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 64 items.  
Required: No

 ** [Tags](#API_CreateActionConnector_RequestSyntax) **   <a name="QS-CreateActionConnector-request-Tags"></a>
A list of tags to apply to the action connector for resource management and organization.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** [VpcConnectionArn](#API_CreateActionConnector_RequestSyntax) **   <a name="QS-CreateActionConnector-request-VpcConnectionArn"></a>
The ARN of the VPC connection to use for secure connectivity to the external service.  
Type: String  
Required: No

## Response Syntax
<a name="API_CreateActionConnector_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "ActionConnectorId": "string",
   "Arn": "string",
   "CreationStatus": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_CreateActionConnector_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateActionConnector_ResponseSyntax) **   <a name="QS-CreateActionConnector-response-Status"></a>
The HTTP status code of the request.

The following data is returned in JSON format by the service.

 ** [ActionConnectorId](#API_CreateActionConnector_ResponseSyntax) **   <a name="QS-CreateActionConnector-response-ActionConnectorId"></a>
The unique identifier of the created action connector.  
Type: String

 ** [Arn](#API_CreateActionConnector_ResponseSyntax) **   <a name="QS-CreateActionConnector-response-Arn"></a>
The Amazon Resource Name (ARN) of the created action connector.  
Type: String

 ** [CreationStatus](#API_CreateActionConnector_ResponseSyntax) **   <a name="QS-CreateActionConnector-response-CreationStatus"></a>
The creation status of the action connector.  
Type: String  
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED` 

 ** [RequestId](#API_CreateActionConnector_ResponseSyntax) **   <a name="QS-CreateActionConnector-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_CreateActionConnector_Errors"></a>

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

 ** ResourceExistsException **   
The resource specified already exists.     
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 409

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_CreateActionConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateActionConnector) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateActionConnector) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateActionConnector) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateActionConnector) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateActionConnector) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateActionConnector) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateActionConnector) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateActionConnector) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateActionConnector) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateActionConnector) 