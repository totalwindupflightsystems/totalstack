---
id: "@specs/aws/cloudfront/docs/API_CreateFieldLevelEncryptionProfile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateFieldLevelEncryptionProfile"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CreateFieldLevelEncryptionProfile

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CreateFieldLevelEncryptionProfile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateFieldLevelEncryptionProfile
<a name="API_CreateFieldLevelEncryptionProfile"></a>

Create a field-level encryption profile.

## Request Syntax
<a name="API_CreateFieldLevelEncryptionProfile_RequestSyntax"></a>

```
POST /2020-05-31/field-level-encryption-profile HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<FieldLevelEncryptionProfileConfig xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <CallerReference>{{string}}</CallerReference>
   <Comment>{{string}}</Comment>
   <EncryptionEntities>
      <Items>
         <EncryptionEntity>
            <FieldPatterns>
               <Items>
                  <FieldPattern>{{string}}</FieldPattern>
               </Items>
               <Quantity>{{integer}}</Quantity>
            </FieldPatterns>
            <ProviderId>{{string}}</ProviderId>
            <PublicKeyId>{{string}}</PublicKeyId>
         </EncryptionEntity>
      </Items>
      <Quantity>{{integer}}</Quantity>
   </EncryptionEntities>
   <Name>{{string}}</Name>
</FieldLevelEncryptionProfileConfig>
```

## URI Request Parameters
<a name="API_CreateFieldLevelEncryptionProfile_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateFieldLevelEncryptionProfile_RequestBody"></a>

The request accepts the following data in XML format.

 ** [FieldLevelEncryptionProfileConfig](#API_CreateFieldLevelEncryptionProfile_RequestSyntax) **   <a name="cloudfront-CreateFieldLevelEncryptionProfile-request-FieldLevelEncryptionProfileConfig"></a>
Root level tag for the FieldLevelEncryptionProfileConfig parameters.  
Required: Yes

 ** [CallerReference](#API_CreateFieldLevelEncryptionProfile_RequestSyntax) **   <a name="cloudfront-CreateFieldLevelEncryptionProfile-request-CallerReference"></a>
A unique number that ensures that the request can't be replayed.  
Type: String  
Required: Yes

 ** [Comment](#API_CreateFieldLevelEncryptionProfile_RequestSyntax) **   <a name="cloudfront-CreateFieldLevelEncryptionProfile-request-Comment"></a>
An optional comment for the field-level encryption profile. The comment cannot be longer than 128 characters.  
Type: String  
Required: No

 ** [EncryptionEntities](#API_CreateFieldLevelEncryptionProfile_RequestSyntax) **   <a name="cloudfront-CreateFieldLevelEncryptionProfile-request-EncryptionEntities"></a>
A complex data type of encryption entities for the field-level encryption profile that include the public key ID, provider, and field patterns for specifying which fields to encrypt with this key.  
Type: [EncryptionEntities](API_EncryptionEntities.md) object  
Required: Yes

 ** [Name](#API_CreateFieldLevelEncryptionProfile_RequestSyntax) **   <a name="cloudfront-CreateFieldLevelEncryptionProfile-request-Name"></a>
Profile name for the field-level encryption profile.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_CreateFieldLevelEncryptionProfile_ResponseSyntax"></a>

```
HTTP/1.1 201
<?xml version="1.0" encoding="UTF-8"?>
<FieldLevelEncryptionProfile>
   <FieldLevelEncryptionProfileConfig>
      <CallerReference>string</CallerReference>
      <Comment>string</Comment>
      <EncryptionEntities>
         <Items>
            <EncryptionEntity>
               <FieldPatterns>
                  <Items>
                     <FieldPattern>string</FieldPattern>
                  </Items>
                  <Quantity>integer</Quantity>
               </FieldPatterns>
               <ProviderId>string</ProviderId>
               <PublicKeyId>string</PublicKeyId>
            </EncryptionEntity>
         </Items>
         <Quantity>integer</Quantity>
      </EncryptionEntities>
      <Name>string</Name>
   </FieldLevelEncryptionProfileConfig>
   <Id>string</Id>
   <LastModifiedTime>timestamp</LastModifiedTime>
</FieldLevelEncryptionProfile>
```

## Response Elements
<a name="API_CreateFieldLevelEncryptionProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in XML format by the service.

 ** [FieldLevelEncryptionProfile](#API_CreateFieldLevelEncryptionProfile_ResponseSyntax) **   <a name="cloudfront-CreateFieldLevelEncryptionProfile-response-FieldLevelEncryptionProfile"></a>
Root level tag for the FieldLevelEncryptionProfile parameters.  
Required: Yes

 ** [FieldLevelEncryptionProfileConfig](#API_CreateFieldLevelEncryptionProfile_ResponseSyntax) **   <a name="cloudfront-CreateFieldLevelEncryptionProfile-response-FieldLevelEncryptionProfileConfig"></a>
A complex data type that includes the profile name and the encryption entities for the field-level encryption profile.  
Type: [FieldLevelEncryptionProfileConfig](API_FieldLevelEncryptionProfileConfig.md) object

 ** [Id](#API_CreateFieldLevelEncryptionProfile_ResponseSyntax) **   <a name="cloudfront-CreateFieldLevelEncryptionProfile-response-Id"></a>
The ID for a field-level encryption profile configuration which includes a set of profiles that specify certain selected data fields to be encrypted by specific public keys.  
Type: String

 ** [LastModifiedTime](#API_CreateFieldLevelEncryptionProfile_ResponseSyntax) **   <a name="cloudfront-CreateFieldLevelEncryptionProfile-response-LastModifiedTime"></a>
The last time the field-level encryption profile was updated.  
Type: Timestamp

## Errors
<a name="API_CreateFieldLevelEncryptionProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** FieldLevelEncryptionProfileAlreadyExists **   
The specified profile for field-level encryption already exists.  
HTTP Status Code: 409

 ** FieldLevelEncryptionProfileSizeExceeded **   
The maximum size of a profile for field-level encryption was exceeded.  
HTTP Status Code: 400

 ** InconsistentQuantities **   
The value of `Quantity` and the size of `Items` don't match.  
HTTP Status Code: 400

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** NoSuchPublicKey **   
The specified public key doesn't exist.  
HTTP Status Code: 404

 ** TooManyFieldLevelEncryptionEncryptionEntities **   
The maximum number of encryption entities for field-level encryption have been created.  
HTTP Status Code: 400

 ** TooManyFieldLevelEncryptionFieldPatterns **   
The maximum number of field patterns for field-level encryption have been created.  
HTTP Status Code: 400

 ** TooManyFieldLevelEncryptionProfiles **   
The maximum number of profiles for field-level encryption have been created.  
HTTP Status Code: 400

## See Also
<a name="API_CreateFieldLevelEncryptionProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile) 