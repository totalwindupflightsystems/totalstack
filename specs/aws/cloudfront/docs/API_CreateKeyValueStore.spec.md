---
id: "@specs/aws/cloudfront/docs/API_CreateKeyValueStore"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateKeyValueStore"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CreateKeyValueStore

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CreateKeyValueStore
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateKeyValueStore
<a name="API_CreateKeyValueStore"></a>

Specifies the key value store resource to add to your account. In your account, the key value store names must be unique. You can also import key value store data in JSON format from an S3 bucket by providing a valid `ImportSource` that you own.

## Request Syntax
<a name="API_CreateKeyValueStore_RequestSyntax"></a>

```
POST /2020-05-31/key-value-store HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateKeyValueStoreRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <Comment>{{string}}</Comment>
   <ImportSource>
      <SourceARN>{{string}}</SourceARN>
      <SourceType>{{string}}</SourceType>
   </ImportSource>
   <Name>{{string}}</Name>
   <Tags>
      <Items>
         <Tag>
            <Key>{{string}}</Key>
            <Value>{{string}}</Value>
         </Tag>
      </Items>
   </Tags>
</CreateKeyValueStoreRequest>
```

## URI Request Parameters
<a name="API_CreateKeyValueStore_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateKeyValueStore_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CreateKeyValueStoreRequest](#API_CreateKeyValueStore_RequestSyntax) **   <a name="cloudfront-CreateKeyValueStore-request-CreateKeyValueStoreRequest"></a>
Root level tag for the CreateKeyValueStoreRequest parameters.  
Required: Yes

 ** [Comment](#API_CreateKeyValueStore_RequestSyntax) **   <a name="cloudfront-CreateKeyValueStore-request-Comment"></a>
The comment of the key value store.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Required: No

 ** [ImportSource](#API_CreateKeyValueStore_RequestSyntax) **   <a name="cloudfront-CreateKeyValueStore-request-ImportSource"></a>
The S3 bucket that provides the source for the import. The source must be in a valid JSON format.  
Type: [ImportSource](API_ImportSource.md) object  
Required: No

 ** [Name](#API_CreateKeyValueStore_RequestSyntax) **   <a name="cloudfront-CreateKeyValueStore-request-Name"></a>
The name of the key value store. The minimum length is 1 character and the maximum length is 64 characters.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9-_]{1,64}`   
Required: Yes

 ** [Tags](#API_CreateKeyValueStore_RequestSyntax) **   <a name="cloudfront-CreateKeyValueStore-request-Tags"></a>
A complex type that contains zero or more `Tag` elements.  
Type: [Tags](API_Tags.md) object  
Required: No

## Response Syntax
<a name="API_CreateKeyValueStore_ResponseSyntax"></a>

```
HTTP/1.1 201
<?xml version="1.0" encoding="UTF-8"?>
<KeyValueStore>
   <ARN>string</ARN>
   <Comment>string</Comment>
   <Id>string</Id>
   <LastModifiedTime>timestamp</LastModifiedTime>
   <Name>string</Name>
   <Status>string</Status>
</KeyValueStore>
```

## Response Elements
<a name="API_CreateKeyValueStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in XML format by the service.

 ** [KeyValueStore](#API_CreateKeyValueStore_ResponseSyntax) **   <a name="cloudfront-CreateKeyValueStore-response-KeyValueStore"></a>
Root level tag for the KeyValueStore parameters.  
Required: Yes

 ** [ARN](#API_CreateKeyValueStore_ResponseSyntax) **   <a name="cloudfront-CreateKeyValueStore-response-ARN"></a>
The Amazon Resource Name (ARN) of the key value store.  
Type: String

 ** [Comment](#API_CreateKeyValueStore_ResponseSyntax) **   <a name="cloudfront-CreateKeyValueStore-response-Comment"></a>
A comment for the key value store.  
Type: String

 ** [Id](#API_CreateKeyValueStore_ResponseSyntax) **   <a name="cloudfront-CreateKeyValueStore-response-Id"></a>
The unique Id for the key value store.  
Type: String

 ** [LastModifiedTime](#API_CreateKeyValueStore_ResponseSyntax) **   <a name="cloudfront-CreateKeyValueStore-response-LastModifiedTime"></a>
The last-modified time of the key value store.  
Type: Timestamp

 ** [Name](#API_CreateKeyValueStore_ResponseSyntax) **   <a name="cloudfront-CreateKeyValueStore-response-Name"></a>
The name of the key value store.  
Type: String

 ** [Status](#API_CreateKeyValueStore_ResponseSyntax) **   <a name="cloudfront-CreateKeyValueStore-response-Status"></a>
The status of the key value store.  
Type: String

## Errors
<a name="API_CreateKeyValueStore_Errors"></a>

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

 ** EntitySizeLimitExceeded **   
The entity size limit was exceeded.  
HTTP Status Code: 413

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
<a name="API_CreateKeyValueStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateKeyValueStore) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/CreateKeyValueStore) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateKeyValueStore) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateKeyValueStore) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateKeyValueStore) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateKeyValueStore) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateKeyValueStore) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateKeyValueStore) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateKeyValueStore) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateKeyValueStore) 