---
id: "@specs/aws/cloudfront/docs/API_ListDomainConflicts"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListDomainConflicts"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ListDomainConflicts

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ListDomainConflicts
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListDomainConflicts
<a name="API_ListDomainConflicts"></a>

**Note**  
We recommend that you use the `ListDomainConflicts` API operation to check for domain conflicts, as it supports both standard distributions and distribution tenants. [ListConflictingAliases](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListConflictingAliases.html) performs similar checks but only supports standard distributions.

Lists existing domain associations that conflict with the domain that you specify.

You can use this API operation to identify potential domain conflicts when moving domains between standard distributions and/or distribution tenants. Domain conflicts must be resolved first before they can be moved. 

For example, if you provide `www.example.com` as input, the returned list can include `www.example.com` and the overlapping wildcard alternate domain name (`*.example.com`), if they exist. If you provide `*.example.com` as input, the returned list can include `*.example.com` and any alternate domain names covered by that wildcard (for example, `www.example.com`, `test.example.com`, `dev.example.com`, and so on), if they exist.

To list conflicting domains, specify the following:
+ The domain to search for
+ The ID of a standard distribution or distribution tenant in your account that has an attached TLS certificate, which covers the specified domain

For more information, including how to set up the standard distribution or distribution tenant, and the certificate, see [Moving an alternate domain name to a different standard distribution or distribution tenant](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-move) in the *Amazon CloudFront Developer Guide*.

You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the `NextMarker` value from the current response as the `Marker` value in the subsequent request.

## Request Syntax
<a name="API_ListDomainConflicts_RequestSyntax"></a>

```
POST /2020-05-31/domain-conflicts HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ListDomainConflictsRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <Domain>{{string}}</Domain>
   <DomainControlValidationResource>
      <DistributionId>{{string}}</DistributionId>
      <DistributionTenantId>{{string}}</DistributionTenantId>
   </DomainControlValidationResource>
   <Marker>{{string}}</Marker>
   <MaxItems>{{integer}}</MaxItems>
</ListDomainConflictsRequest>
```

## URI Request Parameters
<a name="API_ListDomainConflicts_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListDomainConflicts_RequestBody"></a>

The request accepts the following data in XML format.

 ** [ListDomainConflictsRequest](#API_ListDomainConflicts_RequestSyntax) **   <a name="cloudfront-ListDomainConflicts-request-ListDomainConflictsRequest"></a>
Root level tag for the ListDomainConflictsRequest parameters.  
Required: Yes

 ** [Domain](#API_ListDomainConflicts_RequestSyntax) **   <a name="cloudfront-ListDomainConflicts-request-Domain"></a>
The domain to check for conflicts.  
Type: String  
Required: Yes

 ** [DomainControlValidationResource](#API_ListDomainConflicts_RequestSyntax) **   <a name="cloudfront-ListDomainConflicts-request-DomainControlValidationResource"></a>
The distribution resource identifier. This can be the standard distribution or distribution tenant that has a valid certificate, which covers the domain that you specify.  
Type: [DistributionResourceId](API_DistributionResourceId.md) object  
Required: Yes

 ** [Marker](#API_ListDomainConflicts_RequestSyntax) **   <a name="cloudfront-ListDomainConflicts-request-Marker"></a>
The marker for the next set of domain conflicts.  
Type: String  
Required: No

 ** [MaxItems](#API_ListDomainConflicts_RequestSyntax) **   <a name="cloudfront-ListDomainConflicts-request-MaxItems"></a>
The maximum number of domain conflicts to return.  
Type: Integer  
Required: No

## Response Syntax
<a name="API_ListDomainConflicts_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListDomainConflictsResult>
   <DomainConflicts>
      <DomainConflicts>
         <AccountId>string</AccountId>
         <Domain>string</Domain>
         <ResourceId>string</ResourceId>
         <ResourceType>string</ResourceType>
      </DomainConflicts>
   </DomainConflicts>
   <NextMarker>string</NextMarker>
</ListDomainConflictsResult>
```

## Response Elements
<a name="API_ListDomainConflicts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListDomainConflictsResult](#API_ListDomainConflicts_ResponseSyntax) **   <a name="cloudfront-ListDomainConflicts-response-ListDomainConflictsResult"></a>
Root level tag for the ListDomainConflictsResult parameters.  
Required: Yes

 ** [DomainConflicts](#API_ListDomainConflicts_ResponseSyntax) **   <a name="cloudfront-ListDomainConflicts-response-DomainConflicts"></a>
Contains details about the domain conflicts.  
Type: Array of [DomainConflict](API_DomainConflict.md) objects

 ** [NextMarker](#API_ListDomainConflicts_ResponseSyntax) **   <a name="cloudfront-ListDomainConflicts-response-NextMarker"></a>
A token used for pagination of results returned in the response. You can use the token from the previous request to define where the current request should begin.  
Type: String

## Errors
<a name="API_ListDomainConflicts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** EntityNotFound **   
The entity was not found.  
HTTP Status Code: 404

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

## See Also
<a name="API_ListDomainConflicts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListDomainConflicts) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/ListDomainConflicts) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListDomainConflicts) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListDomainConflicts) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListDomainConflicts) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListDomainConflicts) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListDomainConflicts) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListDomainConflicts) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListDomainConflicts) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListDomainConflicts) 