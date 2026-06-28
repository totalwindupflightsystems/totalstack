---
id: "@specs/aws/quicksight/docs/API_CreateAccountCustomization"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAccountCustomization"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateAccountCustomization

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateAccountCustomization
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAccountCustomization
<a name="API_CreateAccountCustomization"></a>

Creates Amazon Quick Sight customizations. Currently, you can add a custom default theme by using the `CreateAccountCustomization` or `UpdateAccountCustomization` API operation. To further customize Amazon Quick Sight by removing Amazon Quick Sight sample assets and videos for all new users, see [Customizing Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/customizing-quicksight.html) in the *Amazon Quick Sight User Guide.* 

You can create customizations for your AWS account or, if you specify a namespace, for a Quick Sight namespace instead. Customizations that apply to a namespace always override customizations that apply to an AWS account. To find out which customizations apply, use the `DescribeAccountCustomization` API operation.

Before you use the `CreateAccountCustomization` API operation to add a theme as the namespace default, make sure that you first share the theme with the namespace. If you don't share it with the namespace, the theme isn't visible to your users even if you make it the default theme. To check if the theme is shared, view the current permissions by using the ` [DescribeThemePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeThemePermissions.html) ` API operation. To share the theme, grant permissions by using the ` [UpdateThemePermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateThemePermissions.html) ` API operation. 

## Request Syntax
<a name="API_CreateAccountCustomization_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/customizations?namespace={{Namespace}} HTTP/1.1
Content-type: application/json

{
   "AccountCustomization": { 
      "DefaultEmailCustomizationTemplate": "{{string}}",
      "DefaultTheme": "{{string}}"
   },
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateAccountCustomization_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateAccountCustomization_RequestSyntax) **   <a name="QS-CreateAccountCustomization-request-uri-AwsAccountId"></a>
The ID for the AWS account that you want to customize Quick Sight for.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [Namespace](#API_CreateAccountCustomization_RequestSyntax) **   <a name="QS-CreateAccountCustomization-request-uri-Namespace"></a>
The Quick Sight namespace that you want to add customizations to.  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$` 

## Request Body
<a name="API_CreateAccountCustomization_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountCustomization](#API_CreateAccountCustomization_RequestSyntax) **   <a name="QS-CreateAccountCustomization-request-AccountCustomization"></a>
The Quick Sight customizations you're adding. You can add these to an AWS account and a QuickSight namespace.   
For example, you can add a default theme by setting `AccountCustomization` to the midnight theme: `"AccountCustomization": { "DefaultTheme": "arn:aws:quicksight::aws:theme/MIDNIGHT" }`. Or, you can add a custom theme by specifying `"AccountCustomization": { "DefaultTheme": "arn:aws:quicksight:us-west-2:111122223333:theme/bdb844d0-0fe9-4d9d-b520-0fe602d93639" }`.   
Type: [AccountCustomization](API_AccountCustomization.md) object  
Required: Yes

 ** [Tags](#API_CreateAccountCustomization_RequestSyntax) **   <a name="QS-CreateAccountCustomization-request-Tags"></a>
A list of the tags that you want to attach to this resource.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateAccountCustomization_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AccountCustomization": { 
      "DefaultEmailCustomizationTemplate": "string",
      "DefaultTheme": "string"
   },
   "Arn": "string",
   "AwsAccountId": "string",
   "Namespace": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_CreateAccountCustomization_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateAccountCustomization_ResponseSyntax) **   <a name="QS-CreateAccountCustomization-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AccountCustomization](#API_CreateAccountCustomization_ResponseSyntax) **   <a name="QS-CreateAccountCustomization-response-AccountCustomization"></a>
The Quick Sight customizations you're adding.   
Type: [AccountCustomization](API_AccountCustomization.md) object

 ** [Arn](#API_CreateAccountCustomization_ResponseSyntax) **   <a name="QS-CreateAccountCustomization-response-Arn"></a>
The Amazon Resource Name (ARN) for the customization that you created for this AWS account.  
Type: String

 ** [AwsAccountId](#API_CreateAccountCustomization_ResponseSyntax) **   <a name="QS-CreateAccountCustomization-response-AwsAccountId"></a>
The ID for the AWS account that you want to customize Quick Sight for.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$` 

 ** [Namespace](#API_CreateAccountCustomization_ResponseSyntax) **   <a name="QS-CreateAccountCustomization-response-Namespace"></a>
The namespace associated with the customization you're creating.   
Type: String  
Length Constraints: Maximum length of 64.  
Pattern: `^[a-zA-Z0-9._-]*$` 

 ** [RequestId](#API_CreateAccountCustomization_ResponseSyntax) **   <a name="QS-CreateAccountCustomization-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_CreateAccountCustomization_Errors"></a>

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
<a name="API_CreateAccountCustomization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateAccountCustomization) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateAccountCustomization) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateAccountCustomization) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateAccountCustomization) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateAccountCustomization) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateAccountCustomization) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateAccountCustomization) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateAccountCustomization) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateAccountCustomization) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateAccountCustomization) 