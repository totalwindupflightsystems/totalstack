---
id: "@specs/aws/cloudfront/docs/API_AssociateAlias"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AssociateAlias"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# AssociateAlias

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_AssociateAlias
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AssociateAlias
<a name="API_AssociateAlias"></a>

**Note**  
The `AssociateAlias` API operation only supports standard distributions. To move domains between distribution tenants and/or standard distributions, we recommend that you use the [UpdateDomainAssociation](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_UpdateDomainAssociation.html) API operation instead.

Associates an alias with a CloudFront standard distribution. An alias is commonly known as a custom domain or vanity domain. It can also be called a CNAME or alternate domain name.

With this operation, you can move an alias that's already used for a standard distribution to a different standard distribution. This prevents the downtime that could occur if you first remove the alias from one standard distribution and then separately add the alias to another standard distribution.

To use this operation, specify the alias and the ID of the target standard distribution.

For more information, including how to set up the target standard distribution, prerequisites that you must complete, and other restrictions, see [Moving an alternate domain name to a different standard distribution or distribution tenant](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-move) in the *Amazon CloudFront Developer Guide*.

## Request Syntax
<a name="API_AssociateAlias_RequestSyntax"></a>

```
PUT /2020-05-31/distribution/{{TargetDistributionId}}/associate-alias?Alias={{Alias}} HTTP/1.1
```

## URI Request Parameters
<a name="API_AssociateAlias_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Alias](#API_AssociateAlias_RequestSyntax) **   <a name="cloudfront-AssociateAlias-request-uri-Alias"></a>
The alias (also known as a CNAME) to add to the target standard distribution.  
Required: Yes

 ** [TargetDistributionId](#API_AssociateAlias_RequestSyntax) **   <a name="cloudfront-AssociateAlias-request-uri-TargetDistributionId"></a>
The ID of the standard distribution that you're associating the alias with.  
Required: Yes

## Request Body
<a name="API_AssociateAlias_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_AssociateAlias_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AssociateAlias_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateAlias_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** IllegalUpdate **   
The update contains modifications that are not allowed.  
HTTP Status Code: 400

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** NoSuchDistribution **   
The specified distribution does not exist.  
HTTP Status Code: 404

 ** TooManyDistributionCNAMEs **   
Your request contains more CNAMEs than are allowed per distribution.  
HTTP Status Code: 400

## See Also
<a name="API_AssociateAlias_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/AssociateAlias) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/AssociateAlias) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/AssociateAlias) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/AssociateAlias) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/AssociateAlias) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/AssociateAlias) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/AssociateAlias) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/AssociateAlias) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/AssociateAlias) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/AssociateAlias) 