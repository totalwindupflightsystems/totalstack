---
id: "@specs/aws/cloudfront/docs/API_GetFieldLevelEncryptionConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetFieldLevelEncryptionConfig"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# GetFieldLevelEncryptionConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_GetFieldLevelEncryptionConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetFieldLevelEncryptionConfig
<a name="API_GetFieldLevelEncryptionConfig"></a>

Get the field-level encryption configuration information.

## Request Syntax
<a name="API_GetFieldLevelEncryptionConfig_RequestSyntax"></a>

```
GET /2020-05-31/field-level-encryption/{{Id}}/config HTTP/1.1
```

## URI Request Parameters
<a name="API_GetFieldLevelEncryptionConfig_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_GetFieldLevelEncryptionConfig_RequestSyntax) **   <a name="cloudfront-GetFieldLevelEncryptionConfig-request-uri-Id"></a>
Request the ID for the field-level encryption configuration information.  
Required: Yes

## Request Body
<a name="API_GetFieldLevelEncryptionConfig_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetFieldLevelEncryptionConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<FieldLevelEncryptionConfig>
   <CallerReference>string</CallerReference>
   <Comment>string</Comment>
   <ContentTypeProfileConfig>
      <ContentTypeProfiles>
         <Items>
            <ContentTypeProfile>
               <ContentType>string</ContentType>
               <Format>string</Format>
               <ProfileId>string</ProfileId>
            </ContentTypeProfile>
         </Items>
         <Quantity>integer</Quantity>
      </ContentTypeProfiles>
      <ForwardWhenContentTypeIsUnknown>boolean</ForwardWhenContentTypeIsUnknown>
   </ContentTypeProfileConfig>
   <QueryArgProfileConfig>
      <ForwardWhenQueryArgProfileIsUnknown>boolean</ForwardWhenQueryArgProfileIsUnknown>
      <QueryArgProfiles>
         <Items>
            <QueryArgProfile>
               <ProfileId>string</ProfileId>
               <QueryArg>string</QueryArg>
            </QueryArgProfile>
         </Items>
         <Quantity>integer</Quantity>
      </QueryArgProfiles>
   </QueryArgProfileConfig>
</FieldLevelEncryptionConfig>
```

## Response Elements
<a name="API_GetFieldLevelEncryptionConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [FieldLevelEncryptionConfig](#API_GetFieldLevelEncryptionConfig_ResponseSyntax) **   <a name="cloudfront-GetFieldLevelEncryptionConfig-response-FieldLevelEncryptionConfig"></a>
Root level tag for the FieldLevelEncryptionConfig parameters.  
Required: Yes

 ** [CallerReference](#API_GetFieldLevelEncryptionConfig_ResponseSyntax) **   <a name="cloudfront-GetFieldLevelEncryptionConfig-response-CallerReference"></a>
A unique number that ensures the request can't be replayed.  
Type: String

 ** [Comment](#API_GetFieldLevelEncryptionConfig_ResponseSyntax) **   <a name="cloudfront-GetFieldLevelEncryptionConfig-response-Comment"></a>
An optional comment about the configuration. The comment cannot be longer than 128 characters.  
Type: String

 ** [ContentTypeProfileConfig](#API_GetFieldLevelEncryptionConfig_ResponseSyntax) **   <a name="cloudfront-GetFieldLevelEncryptionConfig-response-ContentTypeProfileConfig"></a>
A complex data type that specifies when to forward content if a content type isn't recognized and profiles to use as by default in a request if a query argument doesn't specify a profile to use.  
Type: [ContentTypeProfileConfig](API_ContentTypeProfileConfig.md) object

 ** [QueryArgProfileConfig](#API_GetFieldLevelEncryptionConfig_ResponseSyntax) **   <a name="cloudfront-GetFieldLevelEncryptionConfig-response-QueryArgProfileConfig"></a>
A complex data type that specifies when to forward content if a profile isn't found and the profile that can be provided as a query argument in a request.  
Type: [QueryArgProfileConfig](API_QueryArgProfileConfig.md) object

## Errors
<a name="API_GetFieldLevelEncryptionConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** NoSuchFieldLevelEncryptionConfig **   
The specified configuration for field-level encryption doesn't exist.  
HTTP Status Code: 404

## See Also
<a name="API_GetFieldLevelEncryptionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetFieldLevelEncryptionConfig) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/GetFieldLevelEncryptionConfig) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetFieldLevelEncryptionConfig) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetFieldLevelEncryptionConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetFieldLevelEncryptionConfig) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetFieldLevelEncryptionConfig) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetFieldLevelEncryptionConfig) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetFieldLevelEncryptionConfig) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetFieldLevelEncryptionConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetFieldLevelEncryptionConfig) 