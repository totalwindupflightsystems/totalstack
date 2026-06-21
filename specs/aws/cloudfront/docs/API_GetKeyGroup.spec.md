---
id: "@specs/aws/cloudfront/docs/API_GetKeyGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetKeyGroup"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# GetKeyGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_GetKeyGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetKeyGroup
<a name="API_GetKeyGroup"></a>

Gets a key group, including the date and time when the key group was last modified.

To get a key group, you must provide the key group's identifier. If the key group is referenced in a distribution's cache behavior, you can get the key group's identifier using `ListDistributions` or `GetDistribution`. If the key group is not referenced in a cache behavior, you can get the identifier using `ListKeyGroups`.

## Request Syntax
<a name="API_GetKeyGroup_RequestSyntax"></a>

```
GET /2020-05-31/key-group/{{Id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetKeyGroup_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetKeyGroup_RequestSyntax) **   <a name="cloudfront-GetKeyGroup-request-uri-Id"></a>
The identifier of the key group that you are getting. To get the identifier, use `ListKeyGroups`.  
Required: Yes

## Request Body
<a name="API_GetKeyGroup_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetKeyGroup_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<KeyGroup>
   <Id>string</Id>
   <KeyGroupConfig>
      <Comment>string</Comment>
      <Items>
         <PublicKey>string</PublicKey>
      </Items>
      <Name>string</Name>
   </KeyGroupConfig>
   <LastModifiedTime>timestamp</LastModifiedTime>
</KeyGroup>
```

## Response Elements
<a name="API_GetKeyGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [KeyGroup](#API_GetKeyGroup_ResponseSyntax) **   <a name="cloudfront-GetKeyGroup-response-KeyGroup"></a>
Root level tag for the KeyGroup parameters.  
Required: Yes

 ** [Id](#API_GetKeyGroup_ResponseSyntax) **   <a name="cloudfront-GetKeyGroup-response-Id"></a>
The identifier for the key group.  
Type: String

 ** [KeyGroupConfig](#API_GetKeyGroup_ResponseSyntax) **   <a name="cloudfront-GetKeyGroup-response-KeyGroupConfig"></a>
The key group configuration.  
Type: [KeyGroupConfig](API_KeyGroupConfig.md) object

 ** [LastModifiedTime](#API_GetKeyGroup_ResponseSyntax) **   <a name="cloudfront-GetKeyGroup-response-LastModifiedTime"></a>
The date and time when the key group was last modified.  
Type: Timestamp

## Errors
<a name="API_GetKeyGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoSuchResource **   
A resource that was specified is not valid.  
HTTP Status Code: 404

## See Also
<a name="API_GetKeyGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetKeyGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/GetKeyGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetKeyGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetKeyGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetKeyGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetKeyGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetKeyGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetKeyGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetKeyGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetKeyGroup) 