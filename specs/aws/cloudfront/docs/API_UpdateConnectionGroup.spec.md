---
id: "@specs/aws/cloudfront/docs/API_UpdateConnectionGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateConnectionGroup"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# UpdateConnectionGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_UpdateConnectionGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateConnectionGroup
<a name="API_UpdateConnectionGroup"></a>

Updates a connection group.

## Request Syntax
<a name="API_UpdateConnectionGroup_RequestSyntax"></a>

```
PUT /2020-05-31/connection-group/{{Id}} HTTP/1.1
If-Match: {{IfMatch}}
<?xml version="1.0" encoding="UTF-8"?>
<UpdateConnectionGroupRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <AnycastIpListId>{{string}}</AnycastIpListId>
   <Enabled>{{boolean}}</Enabled>
   <Ipv6Enabled>{{boolean}}</Ipv6Enabled>
</UpdateConnectionGroupRequest>
```

## URI Request Parameters
<a name="API_UpdateConnectionGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_UpdateConnectionGroup_RequestSyntax) **   <a name="cloudfront-UpdateConnectionGroup-request-uri-Id"></a>
The ID of the connection group.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: Yes

 ** [If-Match](#API_UpdateConnectionGroup_RequestSyntax) **   <a name="cloudfront-UpdateConnectionGroup-request-IfMatch"></a>
The value of the `ETag` header that you received when retrieving the connection group that you're updating.  
Required: Yes

## Request Body
<a name="API_UpdateConnectionGroup_RequestBody"></a>

The request accepts the following data in XML format.

 ** [UpdateConnectionGroupRequest](#API_UpdateConnectionGroup_RequestSyntax) **   <a name="cloudfront-UpdateConnectionGroup-request-UpdateConnectionGroupRequest"></a>
Root level tag for the UpdateConnectionGroupRequest parameters.  
Required: Yes

 ** [AnycastIpListId](#API_UpdateConnectionGroup_RequestSyntax) **   <a name="cloudfront-UpdateConnectionGroup-request-AnycastIpListId"></a>
The ID of the Anycast static IP list.  
Type: String  
Required: No

 ** [Enabled](#API_UpdateConnectionGroup_RequestSyntax) **   <a name="cloudfront-UpdateConnectionGroup-request-Enabled"></a>
Whether the connection group is enabled.  
Type: Boolean  
Required: No

 ** [Ipv6Enabled](#API_UpdateConnectionGroup_RequestSyntax) **   <a name="cloudfront-UpdateConnectionGroup-request-Ipv6Enabled"></a>
Enable IPv6 for the connection group. For more information, see [Enable IPv6](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesEnableIPv6) in the *Amazon CloudFront Developer Guide*.  
Type: Boolean  
Required: No

## Response Syntax
<a name="API_UpdateConnectionGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ConnectionGroup>
   <AnycastIpListId>string</AnycastIpListId>
   <Arn>string</Arn>
   <CreatedTime>timestamp</CreatedTime>
   <Enabled>boolean</Enabled>
   <Id>string</Id>
   <Ipv6Enabled>boolean</Ipv6Enabled>
   <IsDefault>boolean</IsDefault>
   <LastModifiedTime>timestamp</LastModifiedTime>
   <Name>string</Name>
   <RoutingEndpoint>string</RoutingEndpoint>
   <Status>string</Status>
   <Tags>
      <Items>
         <Tag>
            <Key>string</Key>
            <Value>string</Value>
         </Tag>
      </Items>
   </Tags>
</ConnectionGroup>
```

## Response Elements
<a name="API_UpdateConnectionGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ConnectionGroup](#API_UpdateConnectionGroup_ResponseSyntax) **   <a name="cloudfront-UpdateConnectionGroup-response-ConnectionGroup"></a>
Root level tag for the ConnectionGroup parameters.  
Required: Yes

 ** [AnycastIpListId](#API_UpdateConnectionGroup_ResponseSyntax) **   <a name="cloudfront-UpdateConnectionGroup-response-AnycastIpListId"></a>
The ID of the Anycast static IP list.  
Type: String

 ** [Arn](#API_UpdateConnectionGroup_ResponseSyntax) **   <a name="cloudfront-UpdateConnectionGroup-response-Arn"></a>
The Amazon Resource Name (ARN) of the connection group.  
Type: String

 ** [CreatedTime](#API_UpdateConnectionGroup_ResponseSyntax) **   <a name="cloudfront-UpdateConnectionGroup-response-CreatedTime"></a>
The date and time when the connection group was created.  
Type: Timestamp

 ** [Enabled](#API_UpdateConnectionGroup_ResponseSyntax) **   <a name="cloudfront-UpdateConnectionGroup-response-Enabled"></a>
Whether the connection group is enabled.  
Type: Boolean

 ** [Id](#API_UpdateConnectionGroup_ResponseSyntax) **   <a name="cloudfront-UpdateConnectionGroup-response-Id"></a>
The ID of the connection group.  
Type: String

 ** [Ipv6Enabled](#API_UpdateConnectionGroup_ResponseSyntax) **   <a name="cloudfront-UpdateConnectionGroup-response-Ipv6Enabled"></a>
IPv6 is enabled for the connection group.  
Type: Boolean

 ** [IsDefault](#API_UpdateConnectionGroup_ResponseSyntax) **   <a name="cloudfront-UpdateConnectionGroup-response-IsDefault"></a>
Whether the connection group is the default connection group for the distribution tenants.  
Type: Boolean

 ** [LastModifiedTime](#API_UpdateConnectionGroup_ResponseSyntax) **   <a name="cloudfront-UpdateConnectionGroup-response-LastModifiedTime"></a>
The date and time when the connection group was updated.  
Type: Timestamp

 ** [Name](#API_UpdateConnectionGroup_ResponseSyntax) **   <a name="cloudfront-UpdateConnectionGroup-response-Name"></a>
The name of the connection group.  
Type: String

 ** [RoutingEndpoint](#API_UpdateConnectionGroup_ResponseSyntax) **   <a name="cloudfront-UpdateConnectionGroup-response-RoutingEndpoint"></a>
The routing endpoint (also known as the DNS name) that is assigned to the connection group, such as d111111abcdef8.cloudfront.net.  
Type: String

 ** [Status](#API_UpdateConnectionGroup_ResponseSyntax) **   <a name="cloudfront-UpdateConnectionGroup-response-Status"></a>
The status of the connection group.  
Type: String

 ** [Tags](#API_UpdateConnectionGroup_ResponseSyntax) **   <a name="cloudfront-UpdateConnectionGroup-response-Tags"></a>
A complex type that contains zero or more `Tag` elements.  
Type: [Tags](API_Tags.md) object

## Errors
<a name="API_UpdateConnectionGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

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

 ** InvalidIfMatchVersion **   
The `If-Match` version is missing or not valid.  
HTTP Status Code: 400

 ** PreconditionFailed **   
The precondition in one or more of the request fields evaluated to `false`.  
HTTP Status Code: 412

 ** ResourceInUse **   
Cannot delete this resource because it is in use.  
HTTP Status Code: 409

## See Also
<a name="API_UpdateConnectionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/UpdateConnectionGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/UpdateConnectionGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/UpdateConnectionGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/UpdateConnectionGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/UpdateConnectionGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/UpdateConnectionGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/UpdateConnectionGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/UpdateConnectionGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/UpdateConnectionGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/UpdateConnectionGroup) 