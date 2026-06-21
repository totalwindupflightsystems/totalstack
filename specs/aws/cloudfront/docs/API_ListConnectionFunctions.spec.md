---
id: "@specs/aws/cloudfront/docs/API_ListConnectionFunctions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListConnectionFunctions"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ListConnectionFunctions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ListConnectionFunctions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListConnectionFunctions
<a name="API_ListConnectionFunctions"></a>

Lists connection functions.

## Request Syntax
<a name="API_ListConnectionFunctions_RequestSyntax"></a>

```
POST /2020-05-31/connection-functions HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ListConnectionFunctionsRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <Marker>{{string}}</Marker>
   <MaxItems>{{integer}}</MaxItems>
   <Stage>{{string}}</Stage>
</ListConnectionFunctionsRequest>
```

## URI Request Parameters
<a name="API_ListConnectionFunctions_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListConnectionFunctions_RequestBody"></a>

The request accepts the following data in XML format.

 ** [ListConnectionFunctionsRequest](#API_ListConnectionFunctions_RequestSyntax) **   <a name="cloudfront-ListConnectionFunctions-request-ListConnectionFunctionsRequest"></a>
Root level tag for the ListConnectionFunctionsRequest parameters.  
Required: Yes

 ** [Marker](#API_ListConnectionFunctions_RequestSyntax) **   <a name="cloudfront-ListConnectionFunctions-request-Marker"></a>
Use this field when paginating results to indicate where to begin in your list. The response includes items in the list that occur after the marker. To get the next page of the list, set this field's value to the value of `NextMarker` from the current page's response.  
Type: String  
Required: No

 ** [MaxItems](#API_ListConnectionFunctions_RequestSyntax) **   <a name="cloudfront-ListConnectionFunctions-request-MaxItems"></a>
The maximum number of connection functions that you want returned in the response.  
Type: Integer  
Required: No

 ** [Stage](#API_ListConnectionFunctions_RequestSyntax) **   <a name="cloudfront-ListConnectionFunctions-request-Stage"></a>
The connection function's stage.  
Type: String  
Valid Values: `DEVELOPMENT | LIVE`   
Required: No

## Response Syntax
<a name="API_ListConnectionFunctions_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListConnectionFunctionsResult>
   <ConnectionFunctions>
      <ConnectionFunctionSummary>
         <ConnectionFunctionArn>string</ConnectionFunctionArn>
         <ConnectionFunctionConfig>
            <Comment>string</Comment>
            <KeyValueStoreAssociations>
               <Items>
                  <KeyValueStoreAssociation>
                     <KeyValueStoreARN>string</KeyValueStoreARN>
                  </KeyValueStoreAssociation>
               </Items>
               <Quantity>integer</Quantity>
            </KeyValueStoreAssociations>
            <Runtime>string</Runtime>
         </ConnectionFunctionConfig>
         <CreatedTime>timestamp</CreatedTime>
         <Id>string</Id>
         <LastModifiedTime>timestamp</LastModifiedTime>
         <Name>string</Name>
         <Stage>string</Stage>
         <Status>string</Status>
      </ConnectionFunctionSummary>
   </ConnectionFunctions>
   <NextMarker>string</NextMarker>
</ListConnectionFunctionsResult>
```

## Response Elements
<a name="API_ListConnectionFunctions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ListConnectionFunctionsResult](#API_ListConnectionFunctions_ResponseSyntax) **   <a name="cloudfront-ListConnectionFunctions-response-ListConnectionFunctionsResult"></a>
Root level tag for the ListConnectionFunctionsResult parameters.  
Required: Yes

 ** [ConnectionFunctions](#API_ListConnectionFunctions_ResponseSyntax) **   <a name="cloudfront-ListConnectionFunctions-response-ConnectionFunctions"></a>
A list of connection functions.  
Type: Array of [ConnectionFunctionSummary](API_ConnectionFunctionSummary.md) objects

 ** [NextMarker](#API_ListConnectionFunctions_ResponseSyntax) **   <a name="cloudfront-ListConnectionFunctions-response-NextMarker"></a>
Indicates the next page of connection functions. To get the next page of the list, use this value in the `Marker` field of your request.  
Type: String

## Errors
<a name="API_ListConnectionFunctions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
This operation is not supported in this AWS Region.  
HTTP Status Code: 400

## See Also
<a name="API_ListConnectionFunctions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListConnectionFunctions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/ListConnectionFunctions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListConnectionFunctions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListConnectionFunctions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListConnectionFunctions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListConnectionFunctions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListConnectionFunctions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListConnectionFunctions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListConnectionFunctions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListConnectionFunctions) 