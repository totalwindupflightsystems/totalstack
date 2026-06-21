---
id: "@specs/aws/cloudfront/docs/API_UpdateDomainAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateDomainAssociation"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# UpdateDomainAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_UpdateDomainAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateDomainAssociation
<a name="API_UpdateDomainAssociation"></a>

**Note**  
We recommend that you use the `UpdateDomainAssociation` API operation to move a domain association, as it supports both standard distributions and distribution tenants. [AssociateAlias](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_AssociateAlias.html) performs similar checks but only supports standard distributions.

Moves a domain from its current standard distribution or distribution tenant to another one.

You must first disable the source distribution (standard distribution or distribution tenant) and then separately call this operation to move the domain to another target distribution (standard distribution or distribution tenant).

To use this operation, specify the domain and the ID of the target resource (standard distribution or distribution tenant). For more information, including how to set up the target resource, prerequisites that you must complete, and other restrictions, see [Moving an alternate domain name to a different standard distribution or distribution tenant](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-move) in the *Amazon CloudFront Developer Guide*.

## Request Syntax
<a name="API_UpdateDomainAssociation_RequestSyntax"></a>

```
POST /2020-05-31/domain-association HTTP/1.1
If-Match: {{IfMatch}}
<?xml version="1.0" encoding="UTF-8"?>
<UpdateDomainAssociationRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <Domain>{{string}}</Domain>
   <TargetResource>
      <DistributionId>{{string}}</DistributionId>
      <DistributionTenantId>{{string}}</DistributionTenantId>
   </TargetResource>
</UpdateDomainAssociationRequest>
```

## URI Request Parameters
<a name="API_UpdateDomainAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [If-Match](#API_UpdateDomainAssociation_RequestSyntax) **   <a name="cloudfront-UpdateDomainAssociation-request-IfMatch"></a>
The value of the `ETag` identifier for the standard distribution or distribution tenant that will be associated with the domain.

## Request Body
<a name="API_UpdateDomainAssociation_RequestBody"></a>

The request accepts the following data in XML format.

 ** [UpdateDomainAssociationRequest](#API_UpdateDomainAssociation_RequestSyntax) **   <a name="cloudfront-UpdateDomainAssociation-request-UpdateDomainAssociationRequest"></a>
Root level tag for the UpdateDomainAssociationRequest parameters.  
Required: Yes

 ** [Domain](#API_UpdateDomainAssociation_RequestSyntax) **   <a name="cloudfront-UpdateDomainAssociation-request-Domain"></a>
The domain to update.  
Type: String  
Required: Yes

 ** [TargetResource](#API_UpdateDomainAssociation_RequestSyntax) **   <a name="cloudfront-UpdateDomainAssociation-request-TargetResource"></a>
The target standard distribution or distribution tenant resource for the domain. You can specify either `DistributionId` or `DistributionTenantId`, but not both.  
Type: [DistributionResourceId](API_DistributionResourceId.md) object  
Required: Yes

## Response Syntax
<a name="API_UpdateDomainAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
ETag: {{ETag}}
<?xml version="1.0" encoding="UTF-8"?>
<UpdateDomainAssociationResult>
   <Domain>string</Domain>
   <ResourceId>string</ResourceId>
</UpdateDomainAssociationResult>
```

## Response Elements
<a name="API_UpdateDomainAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [ETag](#API_UpdateDomainAssociation_ResponseSyntax) **   <a name="cloudfront-UpdateDomainAssociation-response-ETag"></a>
The current version of the target standard distribution or distribution tenant that was associated with the domain.

The following data is returned in XML format by the service.

 ** [UpdateDomainAssociationResult](#API_UpdateDomainAssociation_ResponseSyntax) **   <a name="cloudfront-UpdateDomainAssociation-response-UpdateDomainAssociationResult"></a>
Root level tag for the UpdateDomainAssociationResult parameters.  
Required: Yes

 ** [Domain](#API_UpdateDomainAssociation_ResponseSyntax) **   <a name="cloudfront-UpdateDomainAssociation-response-Domain"></a>
The domain that you're moving.  
Type: String

 ** [ResourceId](#API_UpdateDomainAssociation_ResponseSyntax) **   <a name="cloudfront-UpdateDomainAssociation-response-ResourceId"></a>
The intended destination for the domain.  
Type: String

## Errors
<a name="API_UpdateDomainAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** EntityNotFound **   
The entity was not found.  
HTTP Status Code: 404

 ** IllegalUpdate **   
The update contains modifications that are not allowed.  
HTTP Status Code: 400

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** InvalidAssociation **   
The specified CloudFront resource can't be associated.  
HTTP Status Code: 409

 ** InvalidIfMatchVersion **   
The `If-Match` version is missing or not valid.  
HTTP Status Code: 400

 ** PreconditionFailed **   
The precondition in one or more of the request fields evaluated to `false`.  
HTTP Status Code: 412

## See Also
<a name="API_UpdateDomainAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/UpdateDomainAssociation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/UpdateDomainAssociation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/UpdateDomainAssociation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/UpdateDomainAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/UpdateDomainAssociation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/UpdateDomainAssociation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/UpdateDomainAssociation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/UpdateDomainAssociation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/UpdateDomainAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/UpdateDomainAssociation) 