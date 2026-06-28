---
id: "@specs/aws/quicksight/docs/API_CreateAccountSubscription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAccountSubscription"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateAccountSubscription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateAccountSubscription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAccountSubscription
<a name="API_CreateAccountSubscription"></a>

Creates an Amazon Quick Sight account, or subscribes to Amazon Quick Sight Q.

The AWS Region for the account is derived from what is configured in the AWS CLI or SDK.

Before you use this operation, make sure that you can connect to an existing AWS account. If you don't have an AWS account, see [Sign up for AWS](https://docs.aws.amazon.com/quicksight/latest/user/setting-up-aws-sign-up.html) in the *Amazon Quick Sight User Guide*. The person who signs up for Amazon Quick Sight needs to have the correct AWS Identity and Access Management (IAM) permissions. For more information, see [IAM Policy Examples for Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/iam-policy-examples.html) in the *Amazon Quick Sight User Guide*.

If your IAM policy includes both the `Subscribe` and `CreateAccountSubscription` actions, make sure that both actions are set to `Allow`. If either action is set to `Deny`, the `Deny` action prevails and your API call fails.

You can't pass an existing IAM role to access other AWS services using this API operation. To pass your existing IAM role to Amazon Quick Sight, see [Passing IAM roles to Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/security_iam_service-with-iam.html#security-create-iam-role) in the *Amazon Quick Sight User Guide*.

You can't set default resource access on the new account from the Amazon Quick Sight API. Instead, add default resource access from the Amazon Quick Sight console. For more information about setting default resource access to AWS services, see [Setting default resource access to AWS services](https://docs.aws.amazon.com/quicksight/latest/user/scoping-policies-defaults.html) in the *Amazon Quick Sight User Guide*.

## Request Syntax
<a name="API_CreateAccountSubscription_RequestSyntax"></a>

```
POST /account/{{AwsAccountId}} HTTP/1.1
Content-type: application/json

{
   "AccountName": "{{string}}",
   "ActiveDirectoryName": "{{string}}",
   "AdminGroup": [ "{{string}}" ],
   "AdminProGroup": [ "{{string}}" ],
   "AuthenticationMethod": "{{string}}",
   "AuthorGroup": [ "{{string}}" ],
   "AuthorProGroup": [ "{{string}}" ],
   "ContactNumber": "{{string}}",
   "DirectoryId": "{{string}}",
   "Edition": "{{string}}",
   "EmailAddress": "{{string}}",
   "FirstName": "{{string}}",
   "IAMIdentityCenterInstanceArn": "{{string}}",
   "LastName": "{{string}}",
   "NotificationEmail": "{{string}}",
   "ReaderGroup": [ "{{string}}" ],
   "ReaderProGroup": [ "{{string}}" ],
   "Realm": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateAccountSubscription_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateAccountSubscription_RequestSyntax) **   <a name="QS-CreateAccountSubscription-request-uri-AwsAccountId"></a>
The AWS account ID of the account that you're using to create your Quick Sight account.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_CreateAccountSubscription_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountName](#API_CreateAccountSubscription_RequestSyntax) **   <a name="QS-CreateAccountSubscription-request-AccountName"></a>
The name of your Amazon Quick Sight account. This name is unique over all of AWS, and it appears only when users sign in. You can't change `AccountName` value after the Amazon Quick Sight account is created.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 62.  
Pattern: `^(?!D-|d-)([\da-zA-Z]+)([-]*[\da-zA-Z])*`   
Required: Yes

 ** [AuthenticationMethod](#API_CreateAccountSubscription_RequestSyntax) **   <a name="QS-CreateAccountSubscription-request-AuthenticationMethod"></a>
The method that you want to use to authenticate your Quick Sight account.  
If you choose `ACTIVE_DIRECTORY`, provide an `ActiveDirectoryName` and an `AdminGroup` associated with your Active Directory.  
If you choose `IAM_IDENTITY_CENTER`, provide an `AdminGroup` associated with your IAM Identity Center account.  
Type: String  
Valid Values: `IAM_AND_QUICKSIGHT | IAM_ONLY | ACTIVE_DIRECTORY | IAM_IDENTITY_CENTER`   
Required: Yes

 ** [NotificationEmail](#API_CreateAccountSubscription_RequestSyntax) **   <a name="QS-CreateAccountSubscription-request-NotificationEmail"></a>
The email address that you want Quick Sight to send notifications to regarding your Quick Sight account or Quick Sight subscription.  
Type: String  
Required: Yes

 ** [ActiveDirectoryName](#API_CreateAccountSubscription_RequestSyntax) **   <a name="QS-CreateAccountSubscription-request-ActiveDirectoryName"></a>
The name of your Active Directory. This field is required if `ACTIVE_DIRECTORY` is the selected authentication method of the new Quick Sight account.  
Type: String  
Required: No

 ** [AdminGroup](#API_CreateAccountSubscription_RequestSyntax) **   <a name="QS-CreateAccountSubscription-request-AdminGroup"></a>
The admin group associated with your Active Directory or IAM Identity Center account. Either this field or the `AdminProGroup` field is required if `ACTIVE_DIRECTORY` or `IAM_IDENTITY_CENTER` is the selected authentication method of the new Quick Sight account.  
For more information about using IAM Identity Center in Amazon Quick Sight, see [Using IAM Identity Center with Amazon Quick Sight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html) in the Amazon Quick Sight User Guide. For more information about using Active Directory in Amazon Quick Sight, see [Using Active Directory with Amazon Quick Sight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html) in the Amazon Quick Sight User Guide.  
Type: Array of strings  
Required: No

 ** [AdminProGroup](#API_CreateAccountSubscription_RequestSyntax) **   <a name="QS-CreateAccountSubscription-request-AdminProGroup"></a>
The admin pro group associated with your Active Directory or IAM Identity Center account. Either this field or the `AdminGroup` field is required if `ACTIVE_DIRECTORY` or `IAM_IDENTITY_CENTER` is the selected authentication method of the new Quick Sight account.  
For more information about using IAM Identity Center in Amazon Quick Sight, see [Using IAM Identity Center with Amazon Quick Sight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html) in the Amazon Quick Sight User Guide. For more information about using Active Directory in Amazon Quick Sight, see [Using Active Directory with Amazon Quick Sight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html) in the Amazon Quick Sight User Guide.  
Type: Array of strings  
Required: No

 ** [AuthorGroup](#API_CreateAccountSubscription_RequestSyntax) **   <a name="QS-CreateAccountSubscription-request-AuthorGroup"></a>
The author group associated with your Active Directory or IAM Identity Center account.  
For more information about using IAM Identity Center in Amazon Quick Sight, see [Using IAM Identity Center with Amazon Quick Sight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html) in the Amazon Quick Sight User Guide. For more information about using Active Directory in Amazon Quick Sight, see [Using Active Directory with Amazon Quick Sight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html) in the Amazon Quick Sight User Guide.  
Type: Array of strings  
Required: No

 ** [AuthorProGroup](#API_CreateAccountSubscription_RequestSyntax) **   <a name="QS-CreateAccountSubscription-request-AuthorProGroup"></a>
The author pro group associated with your Active Directory or IAM Identity Center account.  
For more information about using IAM Identity Center in Amazon Quick Sight, see [Using IAM Identity Center with Amazon Quick Sight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html) in the Amazon Quick Sight User Guide. For more information about using Active Directory in Amazon Quick Sight, see [Using Active Directory with Amazon Quick Sight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html) in the Amazon Quick Sight User Guide.  
Type: Array of strings  
Required: No

 ** [ContactNumber](#API_CreateAccountSubscription_RequestSyntax) **   <a name="QS-CreateAccountSubscription-request-ContactNumber"></a>
A 10-digit phone number for the author of the Amazon Quick Sight account to use for future communications. This field is required if `ENTERPPRISE_AND_Q` is the selected edition of the new Amazon Quick Sight account.  
Type: String  
Required: No

 ** [DirectoryId](#API_CreateAccountSubscription_RequestSyntax) **   <a name="QS-CreateAccountSubscription-request-DirectoryId"></a>
The ID of the Active Directory that is associated with your Quick Sight account.  
Type: String  
Required: No

 ** [Edition](#API_CreateAccountSubscription_RequestSyntax) **   <a name="QS-CreateAccountSubscription-request-Edition"></a>
The edition of Amazon Quick Sight that you want your account to have. Currently, you can choose from `ENTERPRISE` or `ENTERPRISE_AND_Q`.  
If you choose `ENTERPRISE_AND_Q`, the following parameters are required:  
+  `FirstName` 
+  `LastName` 
+  `EmailAddress` 
+  `ContactNumber` 
Type: String  
Valid Values: `STANDARD | ENTERPRISE | ENTERPRISE_AND_Q`   
Required: No

 ** [EmailAddress](#API_CreateAccountSubscription_RequestSyntax) **   <a name="QS-CreateAccountSubscription-request-EmailAddress"></a>
The email address of the author of the Amazon Quick Sight account to use for future communications. This field is required if `ENTERPPRISE_AND_Q` is the selected edition of the new Amazon Quick Sight account.  
Type: String  
Required: No

 ** [FirstName](#API_CreateAccountSubscription_RequestSyntax) **   <a name="QS-CreateAccountSubscription-request-FirstName"></a>
The first name of the author of the Amazon Quick Sight account to use for future communications. This field is required if `ENTERPPRISE_AND_Q` is the selected edition of the new Amazon Quick Sight account.  
Type: String  
Required: No

 ** [IAMIdentityCenterInstanceArn](#API_CreateAccountSubscription_RequestSyntax) **   <a name="QS-CreateAccountSubscription-request-IAMIdentityCenterInstanceArn"></a>
The Amazon Resource Name (ARN) for the IAM Identity Center instance.  
Type: String  
Required: No

 ** [LastName](#API_CreateAccountSubscription_RequestSyntax) **   <a name="QS-CreateAccountSubscription-request-LastName"></a>
The last name of the author of the Amazon Quick Sight account to use for future communications. This field is required if `ENTERPPRISE_AND_Q` is the selected edition of the new Amazon Quick Sight account.  
Type: String  
Required: No

 ** [ReaderGroup](#API_CreateAccountSubscription_RequestSyntax) **   <a name="QS-CreateAccountSubscription-request-ReaderGroup"></a>
The reader group associated with your Active Directory or IAM Identity Center account.  
For more information about using IAM Identity Center in Amazon Quick Sight, see [Using IAM Identity Center with Amazon Quick Sight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html) in the Amazon Quick Sight User Guide. For more information about using Active Directory in Amazon Quick Sight, see [Using Active Directory with Amazon Quick Sight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html) in the Amazon Quick Sight User Guide.  
Type: Array of strings  
Required: No

 ** [ReaderProGroup](#API_CreateAccountSubscription_RequestSyntax) **   <a name="QS-CreateAccountSubscription-request-ReaderProGroup"></a>
The reader pro group associated with your Active Directory or IAM Identity Center account.  
For more information about using IAM Identity Center in Amazon Quick Sight, see [Using IAM Identity Center with Amazon Quick Sight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/sec-identity-management-identity-center.html) in the Amazon Quick Sight User Guide. For more information about using Active Directory in Amazon Quick Sight, see [Using Active Directory with Amazon Quick Sight Enterprise Edition](https://docs.aws.amazon.com/quicksight/latest/user/aws-directory-service.html) in the Amazon Quick Sight User Guide.  
Type: Array of strings  
Required: No

 ** [Realm](#API_CreateAccountSubscription_RequestSyntax) **   <a name="QS-CreateAccountSubscription-request-Realm"></a>
The realm of the Active Directory that is associated with your Quick Sight account. This field is required if `ACTIVE_DIRECTORY` is the selected authentication method of the new Quick Sight account.  
Type: String  
Required: No

## Response Syntax
<a name="API_CreateAccountSubscription_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RequestId": "string",
   "SignupResponse": { 
      "accountName": "string",
      "directoryType": "string",
      "IAMUser": boolean,
      "userLoginName": "string"
   }
}
```

## Response Elements
<a name="API_CreateAccountSubscription_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateAccountSubscription_ResponseSyntax) **   <a name="QS-CreateAccountSubscription-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_CreateAccountSubscription_ResponseSyntax) **   <a name="QS-CreateAccountSubscription-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [SignupResponse](#API_CreateAccountSubscription_ResponseSyntax) **   <a name="QS-CreateAccountSubscription-response-SignupResponse"></a>
A `SignupResponse` object that returns information about a newly created Quick Sight account.  
Type: [SignupResponse](API_SignupResponse.md) object

## Errors
<a name="API_CreateAccountSubscription_Errors"></a>

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
<a name="API_CreateAccountSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateAccountSubscription) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateAccountSubscription) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateAccountSubscription) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateAccountSubscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateAccountSubscription) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateAccountSubscription) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateAccountSubscription) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateAccountSubscription) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateAccountSubscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateAccountSubscription) 