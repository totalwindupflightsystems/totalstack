---
id: "@specs/aws/quicksight/docs/API_DeleteAccountSubscription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteAccountSubscription"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DeleteAccountSubscription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DeleteAccountSubscription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteAccountSubscription
<a name="API_DeleteAccountSubscription"></a>

**Important**  
Deleting your Quick Sight account subscription has permanent, irreversible consequences across all AWS regions:  
Global deletion – Running this operation from any single region will delete your Quick Sight account and all data in every AWS region where you have Quick Sight resources.
Complete data loss – All dashboards, analyses, datasets, data sources, and custom visuals will be permanently deleted across all regions.
Embedded content failure – All embedded dashboards and visuals in your applications will immediately stop working and display errors to end users.
Shared resources removed – All shared dashboards, folders, and resources will become inaccessible to other users and external recipients.
User access terminated – All Quick Sight users in your account will lose access immediately, including authors, readers, and administrators.
 **No recovery possible** – Once deleted, your Quick Sight account and all associated data cannot be restored.
Consider exporting critical dashboards and data before proceeding with account deletion.

Use the `DeleteAccountSubscription` operation to delete an Quick Sight account. This operation will result in an error message if you have configured your account termination protection settings to `True`. To change this setting and delete your account, call the `UpdateAccountSettings` API and set the value of the `TerminationProtectionEnabled` parameter to `False`, then make another call to the `DeleteAccountSubscription` API.

## Request Syntax
<a name="API_DeleteAccountSubscription_RequestSyntax"></a>

```
DELETE /account/{{AwsAccountId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteAccountSubscription_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DeleteAccountSubscription_RequestSyntax) **   <a name="QS-DeleteAccountSubscription-request-uri-AwsAccountId"></a>
The AWS account ID of the account that you want to delete.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_DeleteAccountSubscription_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteAccountSubscription_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DeleteAccountSubscription_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DeleteAccountSubscription_ResponseSyntax) **   <a name="QS-DeleteAccountSubscription-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_DeleteAccountSubscription_ResponseSyntax) **   <a name="QS-DeleteAccountSubscription-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DeleteAccountSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

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

 ** PreconditionNotMetException **   
One or more preconditions aren't met.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** ResourceUnavailableException **   
This resource is currently unavailable.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 503

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_DeleteAccountSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DeleteAccountSubscription) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DeleteAccountSubscription) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DeleteAccountSubscription) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DeleteAccountSubscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DeleteAccountSubscription) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DeleteAccountSubscription) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DeleteAccountSubscription) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DeleteAccountSubscription) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DeleteAccountSubscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DeleteAccountSubscription) 