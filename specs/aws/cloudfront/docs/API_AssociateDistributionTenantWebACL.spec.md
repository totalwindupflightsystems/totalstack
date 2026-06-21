---
id: "@specs/aws/cloudfront/docs/API_AssociateDistributionTenantWebACL"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AssociateDistributionTenantWebACL"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# AssociateDistributionTenantWebACL

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_AssociateDistributionTenantWebACL
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AssociateDistributionTenantWebACL
<a name="API_AssociateDistributionTenantWebACL"></a>

Associates the AWS WAF web ACL with a distribution tenant.

## Request Syntax
<a name="API_AssociateDistributionTenantWebACL_RequestSyntax"></a>

```
PUT /2020-05-31/distribution-tenant/{{Id}}/associate-web-acl HTTP/1.1
If-Match: {{IfMatch}}
<?xml version="1.0" encoding="UTF-8"?>
<AssociateDistributionTenantWebACLRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <WebACLArn>{{string}}</WebACLArn>
</AssociateDistributionTenantWebACLRequest>
```

## URI Request Parameters
<a name="API_AssociateDistributionTenantWebACL_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_AssociateDistributionTenantWebACL_RequestSyntax) **   <a name="cloudfront-AssociateDistributionTenantWebACL-request-uri-Id"></a>
The ID of the distribution tenant.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

 ** [If-Match](#API_AssociateDistributionTenantWebACL_RequestSyntax) **   <a name="cloudfront-AssociateDistributionTenantWebACL-request-IfMatch"></a>
The current `ETag` of the distribution tenant. This value is returned in the response of the `GetDistributionTenant` API operation.

## Request Body
<a name="API_AssociateDistributionTenantWebACL_RequestBody"></a>

The request accepts the following data in XML format.

 ** [AssociateDistributionTenantWebACLRequest](#API_AssociateDistributionTenantWebACL_RequestSyntax) **   <a name="cloudfront-AssociateDistributionTenantWebACL-request-AssociateDistributionTenantWebACLRequest"></a>
Root level tag for the AssociateDistributionTenantWebACLRequest parameters.  
Required: Yes

 ** [WebACLArn](#API_AssociateDistributionTenantWebACL_RequestSyntax) **   <a name="cloudfront-AssociateDistributionTenantWebACL-request-WebACLArn"></a>
The Amazon Resource Name (ARN) of the AWS WAF web ACL to associate.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_AssociateDistributionTenantWebACL_ResponseSyntax"></a>

```
HTTP/1.1 200
ETag: {{ETag}}
<?xml version="1.0" encoding="UTF-8"?>
<AssociateDistributionTenantWebACLResult>
   <Id>string</Id>
   <WebACLArn>string</WebACLArn>
</AssociateDistributionTenantWebACLResult>
```

## Response Elements
<a name="API_AssociateDistributionTenantWebACL_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [ETag](#API_AssociateDistributionTenantWebACL_ResponseSyntax) **   <a name="cloudfront-AssociateDistributionTenantWebACL-response-ETag"></a>
The current version of the distribution tenant.

The following data is returned in XML format by the service.

 ** [AssociateDistributionTenantWebACLResult](#API_AssociateDistributionTenantWebACL_ResponseSyntax) **   <a name="cloudfront-AssociateDistributionTenantWebACL-response-AssociateDistributionTenantWebACLResult"></a>
Root level tag for the AssociateDistributionTenantWebACLResult parameters.  
Required: Yes

 ** [Id](#API_AssociateDistributionTenantWebACL_ResponseSyntax) **   <a name="cloudfront-AssociateDistributionTenantWebACL-response-Id"></a>
The ID of the distribution tenant.  
Type: String

 ** [WebACLArn](#API_AssociateDistributionTenantWebACL_ResponseSyntax) **   <a name="cloudfront-AssociateDistributionTenantWebACL-response-WebACLArn"></a>
The ARN of the AWS WAF web ACL that you associated with the distribution tenant.  
Type: String

## Errors
<a name="API_AssociateDistributionTenantWebACL_Errors"></a>

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
<a name="API_AssociateDistributionTenantWebACL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/AssociateDistributionTenantWebACL) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/AssociateDistributionTenantWebACL) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/AssociateDistributionTenantWebACL) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/AssociateDistributionTenantWebACL) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/AssociateDistributionTenantWebACL) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/AssociateDistributionTenantWebACL) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/AssociateDistributionTenantWebACL) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/AssociateDistributionTenantWebACL) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/AssociateDistributionTenantWebACL) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/AssociateDistributionTenantWebACL) 