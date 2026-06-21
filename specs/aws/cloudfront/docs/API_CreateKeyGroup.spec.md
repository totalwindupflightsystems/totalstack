---
id: "@specs/aws/cloudfront/docs/API_CreateKeyGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateKeyGroup"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CreateKeyGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CreateKeyGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateKeyGroup
<a name="API_CreateKeyGroup"></a>

Creates a key group that you can use with [CloudFront signed URLs and signed cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html).

To create a key group, you must specify at least one public key for the key group. After you create a key group, you can reference it from one or more cache behaviors. When you reference a key group in a cache behavior, CloudFront requires signed URLs or signed cookies for all requests that match the cache behavior. The URLs or cookies must be signed with a private key whose corresponding public key is in the key group. The signed URL or cookie contains information about which public key CloudFront should use to verify the signature. For more information, see [Serving private content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) in the *Amazon CloudFront Developer Guide*.

## Request Syntax
<a name="API_CreateKeyGroup_RequestSyntax"></a>

```
POST /2020-05-31/key-group HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<KeyGroupConfig xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <Comment>{{string}}</Comment>
   <Items>
      <PublicKey>{{string}}</PublicKey>
   </Items>
   <Name>{{string}}</Name>
</KeyGroupConfig>
```

## URI Request Parameters
<a name="API_CreateKeyGroup_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateKeyGroup_RequestBody"></a>

The request accepts the following data in XML format.

 ** [KeyGroupConfig](#API_CreateKeyGroup_RequestSyntax) **   <a name="cloudfront-CreateKeyGroup-request-KeyGroupConfig"></a>
Root level tag for the KeyGroupConfig parameters.  
Required: Yes

 ** [Comment](#API_CreateKeyGroup_RequestSyntax) **   <a name="cloudfront-CreateKeyGroup-request-Comment"></a>
A comment to describe the key group. The comment cannot be longer than 128 characters.  
Type: String  
Required: No

 ** [Items](#API_CreateKeyGroup_RequestSyntax) **   <a name="cloudfront-CreateKeyGroup-request-Items"></a>
A list of the identifiers of the public keys in the key group.  
Type: Array of strings  
Required: Yes

 ** [Name](#API_CreateKeyGroup_RequestSyntax) **   <a name="cloudfront-CreateKeyGroup-request-Name"></a>
A name to identify the key group.  
Type: String  
Required: Yes

## Response Syntax
<a name="API_CreateKeyGroup_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateKeyGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in XML format by the service.

 ** [KeyGroup](#API_CreateKeyGroup_ResponseSyntax) **   <a name="cloudfront-CreateKeyGroup-response-KeyGroup"></a>
Root level tag for the KeyGroup parameters.  
Required: Yes

 ** [Id](#API_CreateKeyGroup_ResponseSyntax) **   <a name="cloudfront-CreateKeyGroup-response-Id"></a>
The identifier for the key group.  
Type: String

 ** [KeyGroupConfig](#API_CreateKeyGroup_ResponseSyntax) **   <a name="cloudfront-CreateKeyGroup-response-KeyGroupConfig"></a>
The key group configuration.  
Type: [KeyGroupConfig](API_KeyGroupConfig.md) object

 ** [LastModifiedTime](#API_CreateKeyGroup_ResponseSyntax) **   <a name="cloudfront-CreateKeyGroup-response-LastModifiedTime"></a>
The date and time when the key group was last modified.  
Type: Timestamp

## Errors
<a name="API_CreateKeyGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** KeyGroupAlreadyExists **   
A key group with this name already exists. You must provide a unique name. To modify an existing key group, use `UpdateKeyGroup`.  
HTTP Status Code: 409

 ** TooManyKeyGroups **   
You have reached the maximum number of key groups for this AWS account. For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 400

 ** TooManyPublicKeysInKeyGroup **   
The number of public keys in this key group is more than the maximum allowed. For more information, see [Quotas](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.html) (formerly known as limits) in the *Amazon CloudFront Developer Guide*.  
HTTP Status Code: 400

## See Also
<a name="API_CreateKeyGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateKeyGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/CreateKeyGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateKeyGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateKeyGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateKeyGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateKeyGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateKeyGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateKeyGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateKeyGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateKeyGroup) 