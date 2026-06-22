---
id: "@specs/aws/sesv2/docs/API_UpdateEmailIdentityPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateEmailIdentityPolicy"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# UpdateEmailIdentityPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_UpdateEmailIdentityPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateEmailIdentityPolicy
<a name="API_UpdateEmailIdentityPolicy"></a>

Updates the specified sending authorization policy for the given identity (an email address or a domain). This API returns successfully even if a policy with the specified name does not exist.

**Note**  
This API is for the identity owner only. If you have not verified the identity, this API will return an error.

Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html).

You can execute this operation no more than once per second.

## Request Syntax
<a name="API_UpdateEmailIdentityPolicy_RequestSyntax"></a>

```
PUT /v2/email/identities/{{EmailIdentity}}/policies/{{PolicyName}} HTTP/1.1
Content-type: application/json

{
   "Policy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateEmailIdentityPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EmailIdentity](#API_UpdateEmailIdentityPolicy_RequestSyntax) **   <a name="SES-UpdateEmailIdentityPolicy-request-uri-EmailIdentity"></a>
The email identity.  
Length Constraints: Minimum length of 1.  
Required: Yes

 ** [PolicyName](#API_UpdateEmailIdentityPolicy_RequestSyntax) **   <a name="SES-UpdateEmailIdentityPolicy-request-uri-PolicyName"></a>
The name of the policy.  
The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

## Request Body
<a name="API_UpdateEmailIdentityPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Policy](#API_UpdateEmailIdentityPolicy_RequestSyntax) **   <a name="SES-UpdateEmailIdentityPolicy-request-Policy"></a>
The text of the policy in JSON format. The policy cannot exceed 4 KB.  
 For information about the syntax of sending authorization policies, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-policies.html).  
Type: String  
Length Constraints: Minimum length of 1.  
Required: Yes

## Response Syntax
<a name="API_UpdateEmailIdentityPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateEmailIdentityPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateEmailIdentityPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** NotFoundException **   
The resource you attempted to access doesn't exist.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_UpdateEmailIdentityPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/UpdateEmailIdentityPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/UpdateEmailIdentityPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/UpdateEmailIdentityPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/UpdateEmailIdentityPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/UpdateEmailIdentityPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/UpdateEmailIdentityPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/UpdateEmailIdentityPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/UpdateEmailIdentityPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/UpdateEmailIdentityPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/UpdateEmailIdentityPolicy) 