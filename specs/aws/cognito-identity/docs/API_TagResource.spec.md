---
id: "@specs/aws/cognito-identity/docs/API_TagResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TagResource"
status: active
depends_on:
  - "@specs/aws/cognito-identity/meta"
---

# TagResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cognito-identity/docs/API_TagResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TagResource
<a name="API_TagResource"></a>

Assigns a set of tags to the specified Amazon Cognito identity pool. A tag is a label that you can use to categorize and manage identity pools in different ways, such as by purpose, owner, environment, or other criteria.

Each tag consists of a key and value, both of which you define. A key is a general category for more specific values. For example, if you have two versions of an identity pool, one for testing and another for production, you might assign an `Environment` tag key to both identity pools. The value of this key might be `Test` for one identity pool and `Production` for the other.

Tags are useful for cost tracking and access control. You can activate your tags so that they appear on the Billing and Cost Management console, where you can track the costs associated with your identity pools. In an IAM policy, you can constrain permissions for identity pools based on specific tags or tag values.

You can use this action up to 5 times per second, per account. An identity pool can have as many as 50 tags.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}",
   "Tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## Request Parameters
<a name="API_TagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_TagResource_RequestSyntax) **   <a name="CognitoIdentity-TagResource-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the identity pool.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Required: Yes

 ** [Tags](#API_TagResource_RequestSyntax) **   <a name="CognitoIdentity-TagResource-request-Tags"></a>
The tags to assign to the identity pool.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: Yes

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **   
Thrown when the service encounters an error during processing the request.    
 ** message **   
The message returned by an InternalErrorException.
HTTP Status Code: 500

 ** InvalidParameterException **   
Thrown for missing or bad input parameter(s).    
 ** message **   
The message returned by an InvalidParameterException.
HTTP Status Code: 400

 ** NotAuthorizedException **   
Thrown when a user is not authorized to access the requested resource.    
 ** message **   
The message returned by a NotAuthorizedException
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Thrown when the requested resource (for example, a dataset or record) does not exist.    
 ** message **   
The message returned by a ResourceNotFoundException.
HTTP Status Code: 400

 ** TooManyRequestsException **   
Thrown when a request is throttled.    
 ** message **   
Message returned by a TooManyRequestsException
HTTP Status Code: 400

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-identity-2014-06-30/TagResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-identity-2014-06-30/TagResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-identity-2014-06-30/TagResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-identity-2014-06-30/TagResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-identity-2014-06-30/TagResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-identity-2014-06-30/TagResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-identity-2014-06-30/TagResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-identity-2014-06-30/TagResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-identity-2014-06-30/TagResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-identity-2014-06-30/TagResource) 