---
id: "@specs/aws/quicksight/docs/API_CreateNamespace"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateNamespace"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateNamespace

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateNamespace
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateNamespace
<a name="API_CreateNamespace"></a>

(Enterprise edition only) Creates a new namespace for you to use with Amazon Quick Sight.

A namespace allows you to isolate the Quick Sight users and groups that are registered for that namespace. Users that access the namespace can share assets only with other users or groups in the same namespace. They can't see users and groups in other namespaces. You can create a namespace after your AWS account is subscribed to Quick Sight. The namespace must be unique within the AWS account. By default, there is a limit of 100 namespaces per AWS account. To increase your limit, create a ticket with AWS Support. 

## Request Syntax
<a name="API_CreateNamespace_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}} HTTP/1.1
Content-type: application/json

{
   "IdentityStore": "{{string}}",
   "Namespace": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateNamespace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateNamespace_RequestSyntax) **   <a name="QS-CreateNamespace-request-uri-AwsAccountId"></a>
The ID for the AWS account that you want to create the Quick Sight namespace in.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_CreateNamespace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [IdentityStore](#API_CreateNamespace_RequestSyntax) **   <a name="QS-CreateNamespace-request-IdentityStore"></a>
Specifies the type of your user identity directory. Currently, this supports users with an identity type of `QUICKSIGHT`.  
Type: String  
Valid Values: `QUICKSIGHT`   
Required: Yes

 ** [Namespace](#API_CreateNamespace_RequestSyntax) **   <a name="QS-CreateNamespace-request-Namespace"></a>
The name that you want to use to describe the new namespace.  
Type: String  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$`   
Required: Yes

 ** [Tags](#API_CreateNamespace_RequestSyntax) **   <a name="QS-CreateNamespace-request-Tags"></a>
The tags that you want to associate with the namespace that you're creating.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateNamespace_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "CapacityRegion": "string",
   "CreationStatus": "string",
   "IdentityStore": "string",
   "Name": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_CreateNamespace_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateNamespace_ResponseSyntax) **   <a name="QS-CreateNamespace-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateNamespace_ResponseSyntax) **   <a name="QS-CreateNamespace-response-Arn"></a>
The ARN of the Quick Sight namespace you created.   
Type: String

 ** [CapacityRegion](#API_CreateNamespace_ResponseSyntax) **   <a name="QS-CreateNamespace-response-CapacityRegion"></a>
The AWS Region; that you want to use for the free SPICE capacity for the new namespace. This is set to the region that you run CreateNamespace in.   
Type: String

 ** [CreationStatus](#API_CreateNamespace_ResponseSyntax) **   <a name="QS-CreateNamespace-response-CreationStatus"></a>
The status of the creation of the namespace. This is an asynchronous process. A status of `CREATED` means that your namespace is ready to use. If an error occurs, it indicates if the process is `retryable` or `non-retryable`. In the case of a non-retryable error, refer to the error message for follow-up tasks.  
Type: String  
Valid Values: `CREATED | CREATING | DELETING | RETRYABLE_FAILURE | NON_RETRYABLE_FAILURE` 

 ** [IdentityStore](#API_CreateNamespace_ResponseSyntax) **   <a name="QS-CreateNamespace-response-IdentityStore"></a>
Specifies the type of your user identity directory. Currently, this supports users with an identity type of `QUICKSIGHT`.  
Type: String  
Valid Values: `QUICKSIGHT` 

 ** [Name](#API_CreateNamespace_ResponseSyntax) **   <a name="QS-CreateNamespace-response-Name"></a>
The name of the new namespace that you created.  
Type: String  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$` 

 ** [RequestId](#API_CreateNamespace_ResponseSyntax) **   <a name="QS-CreateNamespace-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_CreateNamespace_Errors"></a>

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

 ** PreconditionNotMetException **   
One or more preconditions aren't met.    
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
<a name="API_CreateNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateNamespace) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateNamespace) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateNamespace) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateNamespace) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateNamespace) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateNamespace) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateNamespace) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateNamespace) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateNamespace) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateNamespace) 