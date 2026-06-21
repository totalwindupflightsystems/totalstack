---
id: "@specs/aws/cloudfront/docs/API_CreateTrustStore"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateTrustStore"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# CreateTrustStore

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_CreateTrustStore
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateTrustStore
<a name="API_CreateTrustStore"></a>

Creates a trust store.

## Request Syntax
<a name="API_CreateTrustStore_RequestSyntax"></a>

```
POST /2020-05-31/trust-store HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateTrustStoreRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <CaCertificatesBundleSource>
      <CaCertificatesBundleS3Location>
         <Bucket>{{string}}</Bucket>
         <Key>{{string}}</Key>
         <Region>{{string}}</Region>
         <Version>{{string}}</Version>
      </CaCertificatesBundleS3Location>
   </CaCertificatesBundleSource>
   <Name>{{string}}</Name>
   <Tags>
      <Items>
         <Tag>
            <Key>{{string}}</Key>
            <Value>{{string}}</Value>
         </Tag>
      </Items>
   </Tags>
</CreateTrustStoreRequest>
```

## URI Request Parameters
<a name="API_CreateTrustStore_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateTrustStore_RequestBody"></a>

The request accepts the following data in XML format.

 ** [CreateTrustStoreRequest](#API_CreateTrustStore_RequestSyntax) **   <a name="cloudfront-CreateTrustStore-request-CreateTrustStoreRequest"></a>
Root level tag for the CreateTrustStoreRequest parameters.  
Required: Yes

 ** [CaCertificatesBundleSource](#API_CreateTrustStore_RequestSyntax) **   <a name="cloudfront-CreateTrustStore-request-CaCertificatesBundleSource"></a>
The CA certificates bundle source for the trust store.  
Type: [CaCertificatesBundleSource](API_CaCertificatesBundleSource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [Name](#API_CreateTrustStore_RequestSyntax) **   <a name="cloudfront-CreateTrustStore-request-Name"></a>
A name for the trust store.  
Type: String  
Required: Yes

 ** [Tags](#API_CreateTrustStore_RequestSyntax) **   <a name="cloudfront-CreateTrustStore-request-Tags"></a>
A complex type that contains zero or more `Tag` elements.  
Type: [Tags](API_Tags.md) object  
Required: No

## Response Syntax
<a name="API_CreateTrustStore_ResponseSyntax"></a>

```
HTTP/1.1 201
<?xml version="1.0" encoding="UTF-8"?>
<TrustStore>
   <Arn>string</Arn>
   <Id>string</Id>
   <LastModifiedTime>timestamp</LastModifiedTime>
   <Name>string</Name>
   <NumberOfCaCertificates>integer</NumberOfCaCertificates>
   <Reason>string</Reason>
   <Status>string</Status>
</TrustStore>
```

## Response Elements
<a name="API_CreateTrustStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in XML format by the service.

 ** [TrustStore](#API_CreateTrustStore_ResponseSyntax) **   <a name="cloudfront-CreateTrustStore-response-TrustStore"></a>
Root level tag for the TrustStore parameters.  
Required: Yes

 ** [Arn](#API_CreateTrustStore_ResponseSyntax) **   <a name="cloudfront-CreateTrustStore-response-Arn"></a>
The trust store's Amazon Resource Name (ARN).  
Type: String

 ** [Id](#API_CreateTrustStore_ResponseSyntax) **   <a name="cloudfront-CreateTrustStore-response-Id"></a>
The trust store's ID.  
Type: String

 ** [LastModifiedTime](#API_CreateTrustStore_ResponseSyntax) **   <a name="cloudfront-CreateTrustStore-response-LastModifiedTime"></a>
The trust store's last modified time.  
Type: Timestamp

 ** [Name](#API_CreateTrustStore_ResponseSyntax) **   <a name="cloudfront-CreateTrustStore-response-Name"></a>
The trust store's name.  
Type: String

 ** [NumberOfCaCertificates](#API_CreateTrustStore_ResponseSyntax) **   <a name="cloudfront-CreateTrustStore-response-NumberOfCaCertificates"></a>
The trust store's number of CA certificates.  
Type: Integer

 ** [Reason](#API_CreateTrustStore_ResponseSyntax) **   <a name="cloudfront-CreateTrustStore-response-Reason"></a>
The trust store's reason.  
Type: String

 ** [Status](#API_CreateTrustStore_ResponseSyntax) **   <a name="cloudfront-CreateTrustStore-response-Status"></a>
The trust store's status.  
Type: String  
Valid Values: `pending | active | failed` 

## Errors
<a name="API_CreateTrustStore_Errors"></a>

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

 ** EntityNotFound **   
The entity was not found.  
HTTP Status Code: 404

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** InvalidTagging **   
The tagging specified is not valid.  
HTTP Status Code: 400

## See Also
<a name="API_CreateTrustStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateTrustStore) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/CreateTrustStore) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateTrustStore) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateTrustStore) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateTrustStore) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateTrustStore) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateTrustStore) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateTrustStore) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateTrustStore) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateTrustStore) 