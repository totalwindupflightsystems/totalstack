---
id: "@specs/aws/cloudfront/docs/API_AssociateDistributionWebACL"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AssociateDistributionWebACL"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# AssociateDistributionWebACL

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_AssociateDistributionWebACL
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AssociateDistributionWebACL
<a name="API_AssociateDistributionWebACL"></a>

Associates the AWS WAF web ACL with a distribution.

## Request Syntax
<a name="API_AssociateDistributionWebACL_RequestSyntax"></a>

```
PUT /2020-05-31/distribution/{{Id}}/associate-web-acl HTTP/1.1
If-Match: {{IfMatch}}
<?xml version="1.0" encoding="UTF-8"?>
<AssociateDistributionWebACLRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <WebACLArn>{{string}}</WebACLArn>
</AssociateDistributionWebACLRequest>
```

## URI Request Parameters
<a name="API_AssociateDistributionWebACL_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_AssociateDistributionWebACL_RequestSyntax) **   <a name="cloudfront-AssociateDistributionWebACL-request-uri-Id"></a>
The ID of the distribution.  
Required: Yes

 ** [If-Match](#API_AssociateDistributionWebACL_RequestSyntax) **   <a name="cloudfront-AssociateDistributionWebACL-request-IfMatch"></a>
The value of the `ETag` header that you received when retrieving the distribution that you're associating with the AWS WAF web ACL.

## Request Body
<a name="API_AssociateDistributionWebACL_RequestBody"></a>

The request accepts the following data in XML format.

 ** [AssociateDistributionWebACLRequest](#API_AssociateDistributionWebACL_RequestSyntax) **   <a name="cloudfront-AssociateDistributionWebACL-request-AssociateDistributionWebACLRequest"></a>
Root level tag for the AssociateDistributionWebACLRequest parameters.  
Required: Yes

 ** [WebACLArn](#API_AssociateDistributionWebACL_RequestSyntax) **   <a name="cloudfront-AssociateDistributionWebACL-request-WebACLArn"></a>
The Amazon Resource Name (ARN) of the AWS WAF web ACL to associate.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_AssociateDistributionWebACL_ResponseSyntax"></a>

```
HTTP/1.1 200
ETag: {{ETag}}
<?xml version="1.0" encoding="UTF-8"?>
<AssociateDistributionWebACLResult>
   <Id>string</Id>
   <WebACLArn>string</WebACLArn>
</AssociateDistributionWebACLResult>
```

## Response Elements
<a name="API_AssociateDistributionWebACL_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [ETag](#API_AssociateDistributionWebACL_ResponseSyntax) **   <a name="cloudfront-AssociateDistributionWebACL-response-ETag"></a>
The current version of the distribution.

The following data is returned in XML format by the service.

 ** [AssociateDistributionWebACLResult](#API_AssociateDistributionWebACL_ResponseSyntax) **   <a name="cloudfront-AssociateDistributionWebACL-response-AssociateDistributionWebACLResult"></a>
Root level tag for the AssociateDistributionWebACLResult parameters.  
Required: Yes

 ** [Id](#API_AssociateDistributionWebACL_ResponseSyntax) **   <a name="cloudfront-AssociateDistributionWebACL-response-Id"></a>
The ID of the distribution.  
Type: String

 ** [WebACLArn](#API_AssociateDistributionWebACL_ResponseSyntax) **   <a name="cloudfront-AssociateDistributionWebACL-response-WebACLArn"></a>
The ARN of the AWS WAF web ACL that you associated with the distribution.  
Type: String

## Errors
<a name="API_AssociateDistributionWebACL_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** EntityLimitExceeded **   
The entity limit has been exceeded.  
HTTP Status Code: 400

 ** EntityNotFound **   
The entity was not found.  
HTTP Status Code: 404

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** InvalidIfMatchVersion **   
The `If-Match` version is missing or not valid.  
HTTP Status Code: 400

 ** PreconditionFailed **   
The precondition in one or more of the request fields evaluated to `false`.  
HTTP Status Code: 412

## See Also
<a name="API_AssociateDistributionWebACL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/AssociateDistributionWebACL) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/AssociateDistributionWebACL) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/AssociateDistributionWebACL) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/AssociateDistributionWebACL) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/AssociateDistributionWebACL) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/AssociateDistributionWebACL) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/AssociateDistributionWebACL) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/AssociateDistributionWebACL) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/AssociateDistributionWebACL) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/AssociateDistributionWebACL) 