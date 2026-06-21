---
id: "@specs/aws/cloudfront/docs/API_UpdateFieldLevelEncryptionConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateFieldLevelEncryptionConfig"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# UpdateFieldLevelEncryptionConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_UpdateFieldLevelEncryptionConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateFieldLevelEncryptionConfig
<a name="API_UpdateFieldLevelEncryptionConfig"></a>

Update a field-level encryption configuration.

## Request Syntax
<a name="API_UpdateFieldLevelEncryptionConfig_RequestSyntax"></a>

```
PUT /2020-05-31/field-level-encryption/{{Id}}/config HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<FieldLevelEncryptionConfig xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <CallerReference>{{string}}</CallerReference>
   <Comment>{{string}}</Comment>
   <ContentTypeProfileConfig>
      <ContentTypeProfiles>
         <Items>
            <ContentTypeProfile>
               <ContentType>{{string}}</ContentType>
               <Format>{{string}}</Format>
               <ProfileId>{{string}}</ProfileId>
            </ContentTypeProfile>
         </Items>
         <Quantity>{{integer}}</Quantity>
      </ContentTypeProfiles>
      <ForwardWhenContentTypeIsUnknown>{{boolean}}</ForwardWhenContentTypeIsUnknown>
   </ContentTypeProfileConfig>
   <QueryArgProfileConfig>
      <ForwardWhenQueryArgProfileIsUnknown>{{boolean}}</ForwardWhenQueryArgProfileIsUnknown>
      <QueryArgProfiles>
         <Items>
            <QueryArgProfile>
               <ProfileId>{{string}}</ProfileId>
               <QueryArg>{{string}}</QueryArg>
            </QueryArgProfile>
         </Items>
         <Quantity>{{integer}}</Quantity>
      </QueryArgProfiles>
   </QueryArgProfileConfig>
</FieldLevelEncryptionConfig>
```

## URI Request Parameters
<a name="API_UpdateFieldLevelEncryptionConfig_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateFieldLevelEncryptionConfig_RequestBody"></a>

The request accepts the following data in XML format.

 ** [FieldLevelEncryptionConfig](#API_UpdateFieldLevelEncryptionConfig_RequestSyntax) **   <a name="cloudfront-UpdateFieldLevelEncryptionConfig-request-FieldLevelEncryptionConfig"></a>
Root level tag for the FieldLevelEncryptionConfig parameters.  
Required: Yes

 ** [CallerReference](#API_UpdateFieldLevelEncryptionConfig_RequestSyntax) **   <a name="cloudfront-UpdateFieldLevelEncryptionConfig-request-CallerReference"></a>
A unique number that ensures the request can't be replayed.  
Type: String  
Required: Yes

 ** [Comment](#API_UpdateFieldLevelEncryptionConfig_RequestSyntax) **   <a name="cloudfront-UpdateFieldLevelEncryptionConfig-request-Comment"></a>
An optional comment about the configuration. The comment cannot be longer than 128 characters.  
Type: String  
Required: No

 ** [ContentTypeProfileConfig](#API_UpdateFieldLevelEncryptionConfig_RequestSyntax) **   <a name="cloudfront-UpdateFieldLevelEncryptionConfig-request-ContentTypeProfileConfig"></a>
A complex data type that specifies when to forward content if a content type isn't recognized and profiles to use as by default in a request if a query argument doesn't specify a profile to use.  
Type: [ContentTypeProfileConfig](API_ContentTypeProfileConfig.md) object  
Required: No

 ** [QueryArgProfileConfig](#API_UpdateFieldLevelEncryptionConfig_RequestSyntax) **   <a name="cloudfront-UpdateFieldLevelEncryptionConfig-request-QueryArgProfileConfig"></a>
A complex data type that specifies when to forward content if a profile isn't found and the profile that can be provided as a query argument in a request.  
Type: [QueryArgProfileConfig](API_QueryArgProfileConfig.md) object  
Required: No

## Response Syntax
<a name="API_UpdateFieldLevelEncryptionConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<FieldLevelEncryption>
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
   <Id>string</Id>
   <LastModifiedTime>timestamp</LastModifiedTime>
</FieldLevelEncryption>
```

## Response Elements
<a name="API_UpdateFieldLevelEncryptionConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [FieldLevelEncryption](#API_UpdateFieldLevelEncryptionConfig_ResponseSyntax) **   <a name="cloudfront-UpdateFieldLevelEncryptionConfig-response-FieldLevelEncryption"></a>
Root level tag for the FieldLevelEncryption parameters.  
Required: Yes

 ** [FieldLevelEncryptionConfig](#API_UpdateFieldLevelEncryptionConfig_ResponseSyntax) **   <a name="cloudfront-UpdateFieldLevelEncryptionConfig-response-FieldLevelEncryptionConfig"></a>
A complex data type that includes the profile configurations specified for field-level encryption.  
Type: [FieldLevelEncryptionConfig](API_FieldLevelEncryptionConfig.md) object

 ** [Id](#API_UpdateFieldLevelEncryptionConfig_ResponseSyntax) **   <a name="cloudfront-UpdateFieldLevelEncryptionConfig-response-Id"></a>
The configuration ID for a field-level encryption configuration which includes a set of profiles that specify certain selected data fields to be encrypted by specific public keys.  
Type: String

 ** [LastModifiedTime](#API_UpdateFieldLevelEncryptionConfig_ResponseSyntax) **   <a name="cloudfront-UpdateFieldLevelEncryptionConfig-response-LastModifiedTime"></a>
The last time the field-level encryption configuration was changed.  
Type: Timestamp

## Errors
<a name="API_UpdateFieldLevelEncryptionConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** IllegalUpdate **   
The update contains modifications that are not allowed.  
HTTP Status Code: 400

 ** InconsistentQuantities **   
The value of `Quantity` and the size of `Items` don't match.  
HTTP Status Code: 400

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** InvalidIfMatchVersion **   
The `If-Match` version is missing or not valid.  
HTTP Status Code: 400

 ** NoSuchFieldLevelEncryptionConfig **   
The specified configuration for field-level encryption doesn't exist.  
HTTP Status Code: 404

 ** NoSuchFieldLevelEncryptionProfile **   
The specified profile for field-level encryption doesn't exist.  
HTTP Status Code: 404

 ** PreconditionFailed **   
The precondition in one or more of the request fields evaluated to `false`.  
HTTP Status Code: 412

 ** QueryArgProfileEmpty **   
No profile specified for the field-level encryption query argument.  
HTTP Status Code: 400

 ** TooManyFieldLevelEncryptionContentTypeProfiles **   
The maximum number of content type profiles for field-level encryption have been created.  
HTTP Status Code: 400

 ** TooManyFieldLevelEncryptionQueryArgProfiles **   
The maximum number of query arg profiles for field-level encryption have been created.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateFieldLevelEncryptionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/UpdateFieldLevelEncryptionConfig) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/UpdateFieldLevelEncryptionConfig) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/UpdateFieldLevelEncryptionConfig) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/UpdateFieldLevelEncryptionConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/UpdateFieldLevelEncryptionConfig) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/UpdateFieldLevelEncryptionConfig) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/UpdateFieldLevelEncryptionConfig) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/UpdateFieldLevelEncryptionConfig) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/UpdateFieldLevelEncryptionConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/UpdateFieldLevelEncryptionConfig) 