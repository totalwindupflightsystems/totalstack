---
id: "@specs/aws/cloudfront/docs/API_UpdateFieldLevelEncryptionProfile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateFieldLevelEncryptionProfile"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# UpdateFieldLevelEncryptionProfile

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_UpdateFieldLevelEncryptionProfile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateFieldLevelEncryptionProfile
<a name="API_UpdateFieldLevelEncryptionProfile"></a>

Update a field-level encryption profile.

## Request Syntax
<a name="API_UpdateFieldLevelEncryptionProfile_RequestSyntax"></a>

```
PUT /2020-05-31/field-level-encryption-profile/{{Id}}/config HTTP/1.1
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
<a name="API_UpdateFieldLevelEncryptionProfile_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateFieldLevelEncryptionProfile_RequestBody"></a>

The request accepts the following data in XML format.

 ** [FieldLevelEncryptionProfileConfig](#API_UpdateFieldLevelEncryptionProfile_RequestSyntax) **   <a name="cloudfront-UpdateFieldLevelEncryptionProfile-request-FieldLevelEncryptionProfileConfig"></a>
Root level tag for the FieldLevelEncryptionProfileConfig parameters.  
Required: Yes

 ** [CallerReference](#API_UpdateFieldLevelEncryptionProfile_RequestSyntax) **   <a name="cloudfront-UpdateFieldLevelEncryptionProfile-request-CallerReference"></a>
A unique number that ensures that the request can't be replayed.  
Type: String  
Required: Yes

 ** [Comment](#API_UpdateFieldLevelEncryptionProfile_RequestSyntax) **   <a name="cloudfront-UpdateFieldLevelEncryptionProfile-request-Comment"></a>
An optional comment for the field-level encryption profile. The comment cannot be longer than 128 characters.  
Type: String  
Required: No

 ** [EncryptionEntities](#API_UpdateFieldLevelEncryptionProfile_RequestSyntax) **   <a name="cloudfront-UpdateFieldLevelEncryptionProfile-request-EncryptionEntities"></a>
A complex data type of encryption entities for the field-level encryption profile that include the public key ID, provider, and field patterns for specifying which fields to encrypt with this key.  
Type: [EncryptionEntities](API_EncryptionEntities.md) object  
Required: Yes

 ** [Name](#API_UpdateFieldLevelEncryptionProfile_RequestSyntax) **   <a name="cloudfront-UpdateFieldLevelEncryptionProfile-request-Name"></a>
Profile name for the field-level encryption profile.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_UpdateFieldLevelEncryptionProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_UpdateFieldLevelEncryptionProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [FieldLevelEncryptionProfile](#API_UpdateFieldLevelEncryptionProfile_ResponseSyntax) **   <a name="cloudfront-UpdateFieldLevelEncryptionProfile-response-FieldLevelEncryptionProfile"></a>
Root level tag for the FieldLevelEncryptionProfile parameters.  
Required: Yes

 ** [FieldLevelEncryptionProfileConfig](#API_UpdateFieldLevelEncryptionProfile_ResponseSyntax) **   <a name="cloudfront-UpdateFieldLevelEncryptionProfile-response-FieldLevelEncryptionProfileConfig"></a>
A complex data type that includes the profile name and the encryption entities for the field-level encryption profile.  
Type: [FieldLevelEncryptionProfileConfig](API_FieldLevelEncryptionProfileConfig.md) object

 ** [Id](#API_UpdateFieldLevelEncryptionProfile_ResponseSyntax) **   <a name="cloudfront-UpdateFieldLevelEncryptionProfile-response-Id"></a>
The ID for a field-level encryption profile configuration which includes a set of profiles that specify certain selected data fields to be encrypted by specific public keys.  
Type: String

 ** [LastModifiedTime](#API_UpdateFieldLevelEncryptionProfile_ResponseSyntax) **   <a name="cloudfront-UpdateFieldLevelEncryptionProfile-response-LastModifiedTime"></a>
The last time the field-level encryption profile was updated.  
Type: Timestamp

## Errors
<a name="API_UpdateFieldLevelEncryptionProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** FieldLevelEncryptionProfileAlreadyExists **   
The specified profile for field-level encryption already exists.  
HTTP Status Code: 409

 ** FieldLevelEncryptionProfileSizeExceeded **   
The maximum size of a profile for field-level encryption was exceeded.  
HTTP Status Code: 400

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

 ** NoSuchFieldLevelEncryptionProfile **   
The specified profile for field-level encryption doesn't exist.  
HTTP Status Code: 404

 ** NoSuchPublicKey **   
The specified public key doesn't exist.  
HTTP Status Code: 404

 ** PreconditionFailed **   
The precondition in one or more of the request fields evaluated to `false`.  
HTTP Status Code: 412

 ** TooManyFieldLevelEncryptionEncryptionEntities **   
The maximum number of encryption entities for field-level encryption have been created.  
HTTP Status Code: 400

 ** TooManyFieldLevelEncryptionFieldPatterns **   
The maximum number of field patterns for field-level encryption have been created.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateFieldLevelEncryptionProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/UpdateFieldLevelEncryptionProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/UpdateFieldLevelEncryptionProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/UpdateFieldLevelEncryptionProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/UpdateFieldLevelEncryptionProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/UpdateFieldLevelEncryptionProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/UpdateFieldLevelEncryptionProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/UpdateFieldLevelEncryptionProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/UpdateFieldLevelEncryptionProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/UpdateFieldLevelEncryptionProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/UpdateFieldLevelEncryptionProfile) 