---
id: "@specs/aws/cloudfront/docs/API_CreateAnycastIpList"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAnycastIpList"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CreateAnycastIpList

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CreateAnycastIpList
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAnycastIpList
<a name="API_CreateAnycastIpList"></a>

Creates an Anycast static IP list.

## Request Syntax
<a name="API_CreateAnycastIpList_RequestSyntax"></a>

```
POST /2020-05-31/anycast-ip-list HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateAnycastIpListRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <IpAddressType>{{string}}</IpAddressType>
   <IpamCidrConfigs>
      <IpamCidrConfig>
         <AnycastIp>{{string}}</AnycastIp>
         <Cidr>{{string}}</Cidr>
         <IpamPoolArn>{{string}}</IpamPoolArn>
         <Status>{{string}}</Status>
      </IpamCidrConfig>
   </IpamCidrConfigs>
   <IpCount>{{integer}}</IpCount>
   <Name>{{string}}</Name>
   <Tags>
      <Items>
         <Tag>
            <Key>{{string}}</Key>
            <Value>{{string}}</Value>
         </Tag>
      </Items>
   </Tags>
</CreateAnycastIpListRequest>
```

## URI Request Parameters
<a name="API_CreateAnycastIpList_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateAnycastIpList_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CreateAnycastIpListRequest](#API_CreateAnycastIpList_RequestSyntax) **   <a name="cloudfront-CreateAnycastIpList-request-CreateAnycastIpListRequest"></a>
Root level tag for the CreateAnycastIpListRequest parameters.  
Required: Yes

 ** [IpAddressType](#API_CreateAnycastIpList_RequestSyntax) **   <a name="cloudfront-CreateAnycastIpList-request-IpAddressType"></a>
The IP address type for the Anycast static IP list. You can specify one of the following options:  
+  `ipv4` only
+  `ipv6` only 
+  `dualstack` - Allocate a list of both IPv4 and IPv6 addresses
Type: String  
Valid Values: `ipv4 | ipv6 | dualstack`   
Required: No

 ** [IpamCidrConfigs](#API_CreateAnycastIpList_RequestSyntax) **   <a name="cloudfront-CreateAnycastIpList-request-IpamCidrConfigs"></a>
 A list of IPAM CIDR configurations that specify the IP address ranges and IPAM pool settings for creating the Anycast static IP list.   
Type: Array of [IpamCidrConfig](API_IpamCidrConfig.md) objects  
Required: No

 ** [IpCount](#API_CreateAnycastIpList_RequestSyntax) **   <a name="cloudfront-CreateAnycastIpList-request-IpCount"></a>
The number of static IP addresses that are allocated to the Anycast static IP list. Valid values: 21 or 3.  
Type: Integer  
Required: Yes

 ** [Name](#API_CreateAnycastIpList_RequestSyntax) **   <a name="cloudfront-CreateAnycastIpList-request-Name"></a>
Name of the Anycast static IP list.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9-_]{1,64}`   
Required: Yes

 ** [Tags](#API_CreateAnycastIpList_RequestSyntax) **   <a name="cloudfront-CreateAnycastIpList-request-Tags"></a>
A complex type that contains zero or more `Tag` elements.  
Type: [Tags](API_Tags.md) object  
Required: No

## Response Syntax
<a name="API_CreateAnycastIpList_ResponseSyntax"></a>

```
HTTP/1.1 202
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
<a name="API_CreateAnycastIpList_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in XML format by the service.

 ** [AnycastIpList](#API_CreateAnycastIpList_ResponseSyntax) **   <a name="cloudfront-CreateAnycastIpList-response-AnycastIpList"></a>
Root level tag for the AnycastIpList parameters.  
Required: Yes

 ** [AnycastIps](#API_CreateAnycastIpList_ResponseSyntax) **   <a name="cloudfront-CreateAnycastIpList-response-AnycastIps"></a>
The static IP addresses that are allocated to the Anycast static IP list.  
Type: Array of strings

 ** [Arn](#API_CreateAnycastIpList_ResponseSyntax) **   <a name="cloudfront-CreateAnycastIpList-response-Arn"></a>
The Amazon Resource Name (ARN) of the Anycast static IP list.  
Type: String

 ** [Id](#API_CreateAnycastIpList_ResponseSyntax) **   <a name="cloudfront-CreateAnycastIpList-response-Id"></a>
The ID of the Anycast static IP list.  
Type: String

 ** [IpAddressType](#API_CreateAnycastIpList_ResponseSyntax) **   <a name="cloudfront-CreateAnycastIpList-response-IpAddressType"></a>
The IP address type for the Anycast static IP list.  
Type: String  
Valid Values: `ipv4 | ipv6 | dualstack` 

 ** [IpamConfig](#API_CreateAnycastIpList_ResponseSyntax) **   <a name="cloudfront-CreateAnycastIpList-response-IpamConfig"></a>
The IPAM configuration for the Anycast static IP list, that contains the quantity and list of IPAM CIDR configurations.  
Type: [IpamConfig](API_IpamConfig.md) object

 ** [IpCount](#API_CreateAnycastIpList_ResponseSyntax) **   <a name="cloudfront-CreateAnycastIpList-response-IpCount"></a>
The number of IP addresses in the Anycast static IP list.  
Type: Integer

 ** [LastModifiedTime](#API_CreateAnycastIpList_ResponseSyntax) **   <a name="cloudfront-CreateAnycastIpList-response-LastModifiedTime"></a>
The last time the Anycast static IP list was modified.  
Type: Timestamp

 ** [Name](#API_CreateAnycastIpList_ResponseSyntax) **   <a name="cloudfront-CreateAnycastIpList-response-Name"></a>
The name of the Anycast static IP list.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9-_]{1,64}` 

 ** [Status](#API_CreateAnycastIpList_ResponseSyntax) **   <a name="cloudfront-CreateAnycastIpList-response-Status"></a>
The status of the Anycast static IP list. Valid values: `Deployed`, `Deploying`, or `Failed`.  
Type: String

## Errors
<a name="API_CreateAnycastIpList_Errors"></a>

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

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** InvalidTagging **   
The tagging specified is not valid.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
This operation is not supported in this AWS Region.  
HTTP Status Code: 400

## See Also
<a name="API_CreateAnycastIpList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateAnycastIpList) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/CreateAnycastIpList) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateAnycastIpList) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateAnycastIpList) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateAnycastIpList) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateAnycastIpList) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateAnycastIpList) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateAnycastIpList) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateAnycastIpList) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateAnycastIpList) 