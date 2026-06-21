---
id: "@specs/aws/cloudfront/docs/API_GetKeyGroupConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetKeyGroupConfig"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# GetKeyGroupConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_GetKeyGroupConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetKeyGroupConfig
<a name="API_GetKeyGroupConfig"></a>

Gets a key group configuration.

To get a key group configuration, you must provide the key group's identifier. If the key group is referenced in a distribution's cache behavior, you can get the key group's identifier using `ListDistributions` or `GetDistribution`. If the key group is not referenced in a cache behavior, you can get the identifier using `ListKeyGroups`.

## Request Syntax
<a name="API_GetKeyGroupConfig_RequestSyntax"></a>

```
GET /2020-05-31/key-group/{{Id}}/config HTTP/1.1
```

## URI Request Parameters
<a name="API_GetKeyGroupConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetKeyGroupConfig_RequestSyntax) **   <a name="cloudfront-GetKeyGroupConfig-request-uri-Id"></a>
The identifier of the key group whose configuration you are getting. To get the identifier, use `ListKeyGroups`.  
Required: Yes

## Request Body
<a name="API_GetKeyGroupConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetKeyGroupConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<KeyGroupConfig>
   <Comment>string</Comment>
   <Items>
      <PublicKey>string</PublicKey>
   </Items>
   <Name>string</Name>
</KeyGroupConfig>
```

## Response Elements
<a name="API_GetKeyGroupConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [KeyGroupConfig](#API_GetKeyGroupConfig_ResponseSyntax) **   <a name="cloudfront-GetKeyGroupConfig-response-KeyGroupConfig"></a>
Root level tag for the KeyGroupConfig parameters.  
Required: Yes

 ** [Comment](#API_GetKeyGroupConfig_ResponseSyntax) **   <a name="cloudfront-GetKeyGroupConfig-response-Comment"></a>
A comment to describe the key group. The comment cannot be longer than 128 characters.  
Type: String

 ** [Items](#API_GetKeyGroupConfig_ResponseSyntax) **   <a name="cloudfront-GetKeyGroupConfig-response-Items"></a>
A list of the identifiers of the public keys in the key group.  
Type: Array of strings

 ** [Name](#API_GetKeyGroupConfig_ResponseSyntax) **   <a name="cloudfront-GetKeyGroupConfig-response-Name"></a>
A name to identify the key group.  
Type: String

## Errors
<a name="API_GetKeyGroupConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoSuchResource **   
A resource that was specified is not valid.  
HTTP Status Code: 404

## See Also
<a name="API_GetKeyGroupConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetKeyGroupConfig) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/GetKeyGroupConfig) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetKeyGroupConfig) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetKeyGroupConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetKeyGroupConfig) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetKeyGroupConfig) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetKeyGroupConfig) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetKeyGroupConfig) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetKeyGroupConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetKeyGroupConfig) 