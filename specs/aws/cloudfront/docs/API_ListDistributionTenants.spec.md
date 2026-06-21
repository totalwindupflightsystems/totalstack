---
id: "@specs/aws/cloudfront/docs/API_ListDistributionTenants"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListDistributionTenants"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ListDistributionTenants

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ListDistributionTenants
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListDistributionTenants
<a name="API_ListDistributionTenants"></a>

Lists the distribution tenants in your AWS account.

## Request Syntax
<a name="API_ListDistributionTenants_RequestSyntax"></a>

```
POST /2020-05-31/distribution-tenants HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ListDistributionTenantsRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <AssociationFilter>
      <ConnectionGroupId>{{string}}</ConnectionGroupId>
      <DistributionId>{{string}}</DistributionId>
   </AssociationFilter>
   <Marker>{{string}}</Marker>
   <MaxItems>{{integer}}</MaxItems>
</ListDistributionTenantsRequest>
```

## URI Request Parameters
<a name="API_ListDistributionTenants_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListDistributionTenants_RequestBody"></a>

The request accepts the following data in XML format.

 ** [ListDistributionTenantsRequest](#API_ListDistributionTenants_RequestSyntax) **   <a name="cloudfront-ListDistributionTenants-request-ListDistributionTenantsRequest"></a>
Root level tag for the ListDistributionTenantsRequest parameters.  
Required: Yes

 ** [AssociationFilter](#API_ListDistributionTenants_RequestSyntax) **   <a name="cloudfront-ListDistributionTenants-request-AssociationFilter"></a>
Filter by the associated distribution ID or connection group ID.  
Type: [DistributionTenantAssociationFilter](API_DistributionTenantAssociationFilter.md) object  
Required: No

 ** [Marker](#API_ListDistributionTenants_RequestSyntax) **   <a name="cloudfront-ListDistributionTenants-request-Marker"></a>
The marker for the next set of results.  
Type: String  
Required: No

 ** [MaxItems](#API_ListDistributionTenants_RequestSyntax) **   <a name="cloudfront-ListDistributionTenants-request-MaxItems"></a>
The maximum number of distribution tenants to return.  
Type: Integer  
Required: No

## Response Syntax
<a name="API_ListDistributionTenants_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListDistributionTenantsResult>
   <DistributionTenantList>
      <DistributionTenantSummary>
         <Arn>string</Arn>
         <ConnectionGroupId>string</ConnectionGroupId>
         <CreatedTime>timestamp</CreatedTime>
         <Customizations>
            <Certificate>
               <Arn>string</Arn>
            </Certificate>
            <GeoRestrictions>
               <Locations>
                  <Location>string</Location>
               </Locations>
               <RestrictionType>string</RestrictionType>
            </GeoRestrictions>
            <WebAcl>
               <Action>string</Action>
               <Arn>string</Arn>
            </WebAcl>
         </Customizations>
         <DistributionId>string</DistributionId>
         <Domains>
            <DomainResult>
               <Domain>string</Domain>
               <Status>string</Status>
            </DomainResult>
         </Domains>
         <Enabled>boolean</Enabled>
         <ETag>string</ETag>
         <Id>string</Id>
         <LastModifiedTime>timestamp</LastModifiedTime>
         <Name>string</Name>
         <Status>string</Status>
      </DistributionTenantSummary>
   </DistributionTenantList>
   <NextMarker>string</NextMarker>
</ListDistributionTenantsResult>
```

## Response Elements
<a name="API_ListDistributionTenants_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListDistributionTenantsResult](#API_ListDistributionTenants_ResponseSyntax) **   <a name="cloudfront-ListDistributionTenants-response-ListDistributionTenantsResult"></a>
Root level tag for the ListDistributionTenantsResult parameters.  
Required: Yes

 ** [DistributionTenantList](#API_ListDistributionTenants_ResponseSyntax) **   <a name="cloudfront-ListDistributionTenants-response-DistributionTenantList"></a>
The list of distribution tenants that you retrieved.  
Type: Array of [DistributionTenantSummary](API_DistributionTenantSummary.md) objects

 ** [NextMarker](#API_ListDistributionTenants_ResponseSyntax) **   <a name="cloudfront-ListDistributionTenants-response-NextMarker"></a>
A token used for pagination of results returned in the response. You can use the token from the previous request to define where the current request should begin.  
Type: String

## Errors
<a name="API_ListDistributionTenants_Errors"></a>

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
<a name="API_ListDistributionTenants_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListDistributionTenants) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/ListDistributionTenants) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListDistributionTenants) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListDistributionTenants) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListDistributionTenants) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListDistributionTenants) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListDistributionTenants) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListDistributionTenants) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListDistributionTenants) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListDistributionTenants) 