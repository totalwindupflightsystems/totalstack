---
id: "@specs/aws/cloudfront/docs/API_ListFieldLevelEncryptionProfiles"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListFieldLevelEncryptionProfiles"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ListFieldLevelEncryptionProfiles

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ListFieldLevelEncryptionProfiles
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListFieldLevelEncryptionProfiles
<a name="API_ListFieldLevelEncryptionProfiles"></a>

Request a list of field-level encryption profiles that have been created in CloudFront for this account.

## Request Syntax
<a name="API_ListFieldLevelEncryptionProfiles_RequestSyntax"></a>

```
GET /2020-05-31/field-level-encryption-profile?Marker={{Marker}}&MaxItems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListFieldLevelEncryptionProfiles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Marker](#API_ListFieldLevelEncryptionProfiles_RequestSyntax) **   <a name="cloudfront-ListFieldLevelEncryptionProfiles-request-uri-Marker"></a>
Use this when paginating results to indicate where to begin in your list of profiles. The results include profiles in the list that occur after the marker. To get the next page of results, set the `Marker` to the value of the `NextMarker` from the current page's response (which is also the ID of the last profile on that page).

 ** [MaxItems](#API_ListFieldLevelEncryptionProfiles_RequestSyntax) **   <a name="cloudfront-ListFieldLevelEncryptionProfiles-request-uri-MaxItems"></a>
The maximum number of field-level encryption profiles you want in the response body. 

## Request Body
<a name="API_ListFieldLevelEncryptionProfiles_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListFieldLevelEncryptionProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<FieldLevelEncryptionProfileList>
   <Items>
      <FieldLevelEncryptionProfileSummary>
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
         <Id>string</Id>
         <LastModifiedTime>timestamp</LastModifiedTime>
         <Name>string</Name>
      </FieldLevelEncryptionProfileSummary>
   </Items>
   <MaxItems>integer</MaxItems>
   <NextMarker>string</NextMarker>
   <Quantity>integer</Quantity>
</FieldLevelEncryptionProfileList>
```

## Response Elements
<a name="API_ListFieldLevelEncryptionProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [FieldLevelEncryptionProfileList](#API_ListFieldLevelEncryptionProfiles_ResponseSyntax) **   <a name="cloudfront-ListFieldLevelEncryptionProfiles-response-FieldLevelEncryptionProfileList"></a>
Root level tag for the FieldLevelEncryptionProfileList parameters.  
Required: Yes

 ** [Items](#API_ListFieldLevelEncryptionProfiles_ResponseSyntax) **   <a name="cloudfront-ListFieldLevelEncryptionProfiles-response-Items"></a>
The field-level encryption profile items.  
Type: Array of [FieldLevelEncryptionProfileSummary](API_FieldLevelEncryptionProfileSummary.md) objects

 ** [MaxItems](#API_ListFieldLevelEncryptionProfiles_ResponseSyntax) **   <a name="cloudfront-ListFieldLevelEncryptionProfiles-response-MaxItems"></a>
The maximum number of field-level encryption profiles you want in the response body.   
Type: Integer

 ** [NextMarker](#API_ListFieldLevelEncryptionProfiles_ResponseSyntax) **   <a name="cloudfront-ListFieldLevelEncryptionProfiles-response-NextMarker"></a>
If there are more elements to be listed, this element is present and contains the value that you can use for the `Marker` request parameter to continue listing your profiles where you left off.  
Type: String

 ** [Quantity](#API_ListFieldLevelEncryptionProfiles_ResponseSyntax) **   <a name="cloudfront-ListFieldLevelEncryptionProfiles-response-Quantity"></a>
The number of field-level encryption profiles.  
Type: Integer

## Errors
<a name="API_ListFieldLevelEncryptionProfiles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

## See Also
<a name="API_ListFieldLevelEncryptionProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListFieldLevelEncryptionProfiles) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/ListFieldLevelEncryptionProfiles) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListFieldLevelEncryptionProfiles) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListFieldLevelEncryptionProfiles) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListFieldLevelEncryptionProfiles) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListFieldLevelEncryptionProfiles) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListFieldLevelEncryptionProfiles) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListFieldLevelEncryptionProfiles) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListFieldLevelEncryptionProfiles) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListFieldLevelEncryptionProfiles) 