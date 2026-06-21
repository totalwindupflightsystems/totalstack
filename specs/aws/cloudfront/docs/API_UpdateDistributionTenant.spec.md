---
id: "@specs/aws/cloudfront/docs/API_UpdateDistributionTenant"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateDistributionTenant"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# UpdateDistributionTenant

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_UpdateDistributionTenant
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateDistributionTenant
<a name="API_UpdateDistributionTenant"></a>

Updates a distribution tenant.

## Request Syntax
<a name="API_UpdateDistributionTenant_RequestSyntax"></a>

```
PUT /2020-05-31/distribution-tenant/{{Id}} HTTP/1.1
If-Match: {{IfMatch}}
<?xml version="1.0" encoding="UTF-8"?>
<UpdateDistributionTenantRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <ConnectionGroupId>{{string}}</ConnectionGroupId>
   <Customizations>
      <Certificate>
         <Arn>{{string}}</Arn>
      </Certificate>
      <GeoRestrictions>
         <Locations>
            <Location>{{string}}</Location>
         </Locations>
         <RestrictionType>{{string}}</RestrictionType>
      </GeoRestrictions>
      <WebAcl>
         <Action>{{string}}</Action>
         <Arn>{{string}}</Arn>
      </WebAcl>
   </Customizations>
   <DistributionId>{{string}}</DistributionId>
   <Domains>
      <DomainItem>
         <Domain>{{string}}</Domain>
      </DomainItem>
   </Domains>
   <Enabled>{{boolean}}</Enabled>
   <ManagedCertificateRequest>
      <CertificateTransparencyLoggingPreference>{{string}}</CertificateTransparencyLoggingPreference>
      <PrimaryDomainName>{{string}}</PrimaryDomainName>
      <ValidationTokenHost>{{string}}</ValidationTokenHost>
   </ManagedCertificateRequest>
   <Parameters>
      <Parameter>
         <Name>{{string}}</Name>
         <Value>{{string}}</Value>
      </Parameter>
   </Parameters>
</UpdateDistributionTenantRequest>
```

## URI Request Parameters
<a name="API_UpdateDistributionTenant_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_UpdateDistributionTenant_RequestSyntax) **   <a name="cloudfront-UpdateDistributionTenant-request-uri-Id"></a>
The ID of the distribution tenant.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

 ** [If-Match](#API_UpdateDistributionTenant_RequestSyntax) **   <a name="cloudfront-UpdateDistributionTenant-request-IfMatch"></a>
The value of the `ETag` header that you received when retrieving the distribution tenant to update. This value is returned in the response of the `GetDistributionTenant` API operation.  
Required: Yes

## Request Body
<a name="API_UpdateDistributionTenant_RequestBody"></a>

The request accepts the following data in XML format.

 ** [UpdateDistributionTenantRequest](#API_UpdateDistributionTenant_RequestSyntax) **   <a name="cloudfront-UpdateDistributionTenant-request-UpdateDistributionTenantRequest"></a>
Root level tag for the UpdateDistributionTenantRequest parameters.  
Required: Yes

 ** [ConnectionGroupId](#API_UpdateDistributionTenant_RequestSyntax) **   <a name="cloudfront-UpdateDistributionTenant-request-ConnectionGroupId"></a>
The ID of the target connection group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

 ** [Customizations](#API_UpdateDistributionTenant_RequestSyntax) **   <a name="cloudfront-UpdateDistributionTenant-request-Customizations"></a>
Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and AWS WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.  
Type: [Customizations](API_Customizations.md) object  
Required: No

 ** [DistributionId](#API_UpdateDistributionTenant_RequestSyntax) **   <a name="cloudfront-UpdateDistributionTenant-request-DistributionId"></a>
The ID for the multi-tenant distribution.  
Type: String  
Required: No

 ** [Domains](#API_UpdateDistributionTenant_RequestSyntax) **   <a name="cloudfront-UpdateDistributionTenant-request-Domains"></a>
The domains to update for the distribution tenant. A domain object can contain only a domain property. You must specify at least one domain. Each distribution tenant can have up to 5 domains.  
Type: Array of [DomainItem](API_DomainItem.md) objects  
Required: No

 ** [Enabled](#API_UpdateDistributionTenant_RequestSyntax) **   <a name="cloudfront-UpdateDistributionTenant-request-Enabled"></a>
Indicates whether the distribution tenant should be updated to an enabled state. If you update the distribution tenant and it's not enabled, the distribution tenant won't serve traffic.  
Type: Boolean  
Required: No

 ** [ManagedCertificateRequest](#API_UpdateDistributionTenant_RequestSyntax) **   <a name="cloudfront-UpdateDistributionTenant-request-ManagedCertificateRequest"></a>
An object that contains the CloudFront managed ACM certificate request.  
Type: [ManagedCertificateRequest](API_ManagedCertificateRequest.md) object  
Required: No

 ** [Parameters](#API_UpdateDistributionTenant_RequestSyntax) **   <a name="cloudfront-UpdateDistributionTenant-request-Parameters"></a>
A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.  
Type: Array of [Parameter](API_Parameter.md) objects  
Required: No

## Response Syntax
<a name="API_UpdateDistributionTenant_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<DistributionTenant>
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
   <Id>string</Id>
   <LastModifiedTime>timestamp</LastModifiedTime>
   <Name>string</Name>
   <Parameters>
      <Parameter>
         <Name>string</Name>
         <Value>string</Value>
      </Parameter>
   </Parameters>
   <Status>string</Status>
   <Tags>
      <Items>
         <Tag>
            <Key>string</Key>
            <Value>string</Value>
         </Tag>
      </Items>
   </Tags>
</DistributionTenant>
```

## Response Elements
<a name="API_UpdateDistributionTenant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [DistributionTenant](#API_UpdateDistributionTenant_ResponseSyntax) **   <a name="cloudfront-UpdateDistributionTenant-response-DistributionTenant"></a>
Root level tag for the DistributionTenant parameters.  
Required: Yes

 ** [Arn](#API_UpdateDistributionTenant_ResponseSyntax) **   <a name="cloudfront-UpdateDistributionTenant-response-Arn"></a>
The Amazon Resource Name (ARN) of the distribution tenant.  
Type: String

 ** [ConnectionGroupId](#API_UpdateDistributionTenant_ResponseSyntax) **   <a name="cloudfront-UpdateDistributionTenant-response-ConnectionGroupId"></a>
The ID of the connection group for the distribution tenant. If you don't specify a connection group, CloudFront uses the default connection group.  
Type: String

 ** [CreatedTime](#API_UpdateDistributionTenant_ResponseSyntax) **   <a name="cloudfront-UpdateDistributionTenant-response-CreatedTime"></a>
The date and time when the distribution tenant was created.  
Type: Timestamp

 ** [Customizations](#API_UpdateDistributionTenant_ResponseSyntax) **   <a name="cloudfront-UpdateDistributionTenant-response-Customizations"></a>
Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and AWS WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.  
Type: [Customizations](API_Customizations.md) object

 ** [DistributionId](#API_UpdateDistributionTenant_ResponseSyntax) **   <a name="cloudfront-UpdateDistributionTenant-response-DistributionId"></a>
The ID of the multi-tenant distribution.  
Type: String

 ** [Domains](#API_UpdateDistributionTenant_ResponseSyntax) **   <a name="cloudfront-UpdateDistributionTenant-response-Domains"></a>
The domains associated with the distribution tenant.  
Type: Array of [DomainResult](API_DomainResult.md) objects

 ** [Enabled](#API_UpdateDistributionTenant_ResponseSyntax) **   <a name="cloudfront-UpdateDistributionTenant-response-Enabled"></a>
Indicates whether the distribution tenant is in an enabled state. If disabled, the distribution tenant won't serve traffic.  
Type: Boolean

 ** [Id](#API_UpdateDistributionTenant_ResponseSyntax) **   <a name="cloudfront-UpdateDistributionTenant-response-Id"></a>
The ID of the distribution tenant.  
Type: String

 ** [LastModifiedTime](#API_UpdateDistributionTenant_ResponseSyntax) **   <a name="cloudfront-UpdateDistributionTenant-response-LastModifiedTime"></a>
The date and time when the distribution tenant was updated.  
Type: Timestamp

 ** [Name](#API_UpdateDistributionTenant_ResponseSyntax) **   <a name="cloudfront-UpdateDistributionTenant-response-Name"></a>
The name of the distribution tenant.  
Type: String

 ** [Parameters](#API_UpdateDistributionTenant_ResponseSyntax) **   <a name="cloudfront-UpdateDistributionTenant-response-Parameters"></a>
A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.  
Type: Array of [Parameter](API_Parameter.md) objects

 ** [Status](#API_UpdateDistributionTenant_ResponseSyntax) **   <a name="cloudfront-UpdateDistributionTenant-response-Status"></a>
The status of the distribution tenant.  
Type: String

 ** [Tags](#API_UpdateDistributionTenant_ResponseSyntax) **   <a name="cloudfront-UpdateDistributionTenant-response-Tags"></a>
A complex type that contains zero or more `Tag` elements.  
Type: [Tags](API_Tags.md) object

## Errors
<a name="API_UpdateDistributionTenant_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** CNAMEAlreadyExists **   
The CNAME specified is already defined for CloudFront.  
HTTP Status Code: 409

 ** EntityAlreadyExists **   
The entity already exists. You must provide a unique entity.  
HTTP Status Code: 409

 ** EntityLimitExceeded **   
The entity limit has been exceeded.  
HTTP Status Code: 400

 ** EntityNotFound **   
The entity was not found.  
HTTP Status Code: 404

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
<a name="API_UpdateDistributionTenant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/UpdateDistributionTenant) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/UpdateDistributionTenant) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/UpdateDistributionTenant) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/UpdateDistributionTenant) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/UpdateDistributionTenant) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/UpdateDistributionTenant) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/UpdateDistributionTenant) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/UpdateDistributionTenant) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/UpdateDistributionTenant) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/UpdateDistributionTenant) 