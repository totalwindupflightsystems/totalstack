---
id: "@specs/aws/sesv2/docs/API_GetEmailIdentityPolicies"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetEmailIdentityPolicies"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# GetEmailIdentityPolicies

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_GetEmailIdentityPolicies
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetEmailIdentityPolicies
<a name="API_GetEmailIdentityPolicies"></a>

Returns the requested sending authorization policies for the given identity (an email address or a domain). The policies are returned as a map of policy names to policy contents. You can retrieve a maximum of 20 policies at a time.

**Note**  
This API is for the identity owner only. If you have not verified the identity, this API will return an error.

Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html).

You can execute this operation no more than once per second.

## Request Syntax
<a name="API_GetEmailIdentityPolicies_RequestSyntax"></a>

```
GET /v2/email/identities/{{EmailIdentity}}/policies HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEmailIdentityPolicies_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EmailIdentity](#API_GetEmailIdentityPolicies_RequestSyntax) **   <a name="SES-GetEmailIdentityPolicies-request-uri-EmailIdentity"></a>
The email identity.  
Length Constraints: Minimum length of 1.  
Required: Yes

## Request Body
<a name="API_GetEmailIdentityPolicies_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEmailIdentityPolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Policies": { 
      "string" : "string" 
   }
}
```

## Response Elements
<a name="API_GetEmailIdentityPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policies](#API_GetEmailIdentityPolicies_ResponseSyntax) **   <a name="SES-GetEmailIdentityPolicies-response-Policies"></a>
A map of policy names to policies.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 64.  
Value Length Constraints: Minimum length of 1.

## Errors
<a name="API_GetEmailIdentityPolicies_Errors"></a>

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
<a name="API_GetEmailIdentityPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/GetEmailIdentityPolicies) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/GetEmailIdentityPolicies) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/GetEmailIdentityPolicies) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/GetEmailIdentityPolicies) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/GetEmailIdentityPolicies) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/GetEmailIdentityPolicies) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/GetEmailIdentityPolicies) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/GetEmailIdentityPolicies) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/GetEmailIdentityPolicies) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/GetEmailIdentityPolicies) 