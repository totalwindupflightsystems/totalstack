---
id: "@specs/aws/cloudfront/docs/API_UpdateAnycastIpList"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateAnycastIpList"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# UpdateAnycastIpList

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_UpdateAnycastIpList
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateAnycastIpList
<a name="API_UpdateAnycastIpList"></a>

Updates an Anycast static IP list.

## Request Syntax
<a name="API_UpdateAnycastIpList_RequestSyntax"></a>

```
PUT /2020-05-31/anycast-ip-list/{{Id}} HTTP/1.1
If-Match: {{IfMatch}}
<?xml version="1.0" encoding="UTF-8"?>
<UpdateAnycastIpListRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <IpAddressType>{{string}}</IpAddressType>
</UpdateAnycastIpListRequest>
```

## URI Request Parameters
<a name="API_UpdateAnycastIpList_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_UpdateAnycastIpList_RequestSyntax) **   <a name="cloudfront-UpdateAnycastIpList-request-uri-Id"></a>
The ID of the Anycast static IP list.  
Required: Yes

 ** [If-Match](#API_UpdateAnycastIpList_RequestSyntax) **   <a name="cloudfront-UpdateAnycastIpList-request-IfMatch"></a>
The current version (ETag value) of the Anycast static IP list that you are updating.  
Required: Yes

## Request Body
<a name="API_UpdateAnycastIpList_RequestBody"></a>

The request accepts the following data in XML format.

 ** [UpdateAnycastIpListRequest](#API_UpdateAnycastIpList_RequestSyntax) **   <a name="cloudfront-UpdateAnycastIpList-request-UpdateAnycastIpListRequest"></a>
Root level tag for the UpdateAnycastIpListRequest parameters.  
Required: Yes

 ** [IpAddressType](#API_UpdateAnycastIpList_RequestSyntax) **   <a name="cloudfront-UpdateAnycastIpList-request-IpAddressType"></a>
The IP address type for the Anycast static IP list. You can specify one of the following options:  
+  `ipv4` only
+  `ipv6` only
+  `dualstack` - Allocate a list of both IPv4 and IPv6 addresses
Type: String  
Valid Values: `ipv4 | ipv6 | dualstack`   
Required: No

## Response Syntax
<a name="API_UpdateAnycastIpList_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<AnycastIpList>
   <AnycastIps>
      <AnycastIp>string</AnycastIp>
   </AnycastIps>
   <Arn>string</Arn>
   <Id>string</Id>
   <IpAddressType>string</IpAddressType>
   <IpamConfig>
      <IpamCidrConfigs>
         <IpamCidrConfig>
            <AnycastIp>string</AnycastIp>
            <Cidr>string</Cidr>
            <IpamPoolArn>string</IpamPoolArn>
            <Status>string</Status>
         </IpamCidrConfig>
      </IpamCidrConfigs>
      <Quantity>integer</Quantity>
   </IpamConfig>
   <IpCount>integer</IpCount>
   <LastModifiedTime>timestamp</LastModifiedTime>
   <Name>string</Name>
   <Status>string</Status>
</AnycastIpList>
```

## Response Elements
<a name="API_UpdateAnycastIpList_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [AnycastIpList](#API_UpdateAnycastIpList_ResponseSyntax) **   <a name="cloudfront-UpdateAnycastIpList-response-AnycastIpList"></a>
Root level tag for the AnycastIpList parameters.  
Required: Yes

 ** [AnycastIps](#API_UpdateAnycastIpList_ResponseSyntax) **   <a name="cloudfront-UpdateAnycastIpList-response-AnycastIps"></a>
The static IP addresses that are allocated to the Anycast static IP list.  
Type: Array of strings

 ** [Arn](#API_UpdateAnycastIpList_ResponseSyntax) **   <a name="cloudfront-UpdateAnycastIpList-response-Arn"></a>
The Amazon Resource Name (ARN) of the Anycast static IP list.  
Type: String

 ** [Id](#API_UpdateAnycastIpList_ResponseSyntax) **   <a name="cloudfront-UpdateAnycastIpList-response-Id"></a>
The ID of the Anycast static IP list.  
Type: String

 ** [IpAddressType](#API_UpdateAnycastIpList_ResponseSyntax) **   <a name="cloudfront-UpdateAnycastIpList-response-IpAddressType"></a>
The IP address type for the Anycast static IP list.  
Type: String  
Valid Values: `ipv4 | ipv6 | dualstack` 

 ** [IpamConfig](#API_UpdateAnycastIpList_ResponseSyntax) **   <a name="cloudfront-UpdateAnycastIpList-response-IpamConfig"></a>
The IPAM configuration for the Anycast static IP list, that contains the quantity and list of IPAM CIDR configurations.  
Type: [IpamConfig](API_IpamConfig.md) object

 ** [IpCount](#API_UpdateAnycastIpList_ResponseSyntax) **   <a name="cloudfront-UpdateAnycastIpList-response-IpCount"></a>
The number of IP addresses in the Anycast static IP list.  
Type: Integer

 ** [LastModifiedTime](#API_UpdateAnycastIpList_ResponseSyntax) **   <a name="cloudfront-UpdateAnycastIpList-response-LastModifiedTime"></a>
The last time the Anycast static IP list was modified.  
Type: Timestamp

 ** [Name](#API_UpdateAnycastIpList_ResponseSyntax) **   <a name="cloudfront-UpdateAnycastIpList-response-Name"></a>
The name of the Anycast static IP list.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9-_]{1,64}` 

 ** [Status](#API_UpdateAnycastIpList_ResponseSyntax) **   <a name="cloudfront-UpdateAnycastIpList-response-Status"></a>
The status of the Anycast static IP list. Valid values: `Deployed`, `Deploying`, or `Failed`.  
Type: String

## Errors
<a name="API_UpdateAnycastIpList_Errors"></a>

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

 ** InvalidIfMatchVersion **   
The `If-Match` version is missing or not valid.  
HTTP Status Code: 400

 ** PreconditionFailed **   
The precondition in one or more of the request fields evaluated to `false`.  
HTTP Status Code: 412

 ** UnsupportedOperation **   
This operation is not supported in this AWS Region.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateAnycastIpList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/UpdateAnycastIpList) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/UpdateAnycastIpList) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/UpdateAnycastIpList) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/UpdateAnycastIpList) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/UpdateAnycastIpList) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/UpdateAnycastIpList) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/UpdateAnycastIpList) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/UpdateAnycastIpList) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/UpdateAnycastIpList) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/UpdateAnycastIpList) 