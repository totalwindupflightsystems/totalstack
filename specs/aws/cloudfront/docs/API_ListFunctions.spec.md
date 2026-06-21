---
id: "@specs/aws/cloudfront/docs/API_ListFunctions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListFunctions"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ListFunctions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ListFunctions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListFunctions
<a name="API_ListFunctions"></a>

Gets a list of all CloudFront functions in your AWS account.

You can optionally apply a filter to return only the functions that are in the specified stage, either `DEVELOPMENT` or `LIVE`.

You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the `NextMarker` value from the current response as the `Marker` value in the subsequent request.

## Request Syntax
<a name="API_ListFunctions_RequestSyntax"></a>

```
GET /2020-05-31/function?Marker={{Marker}}&MaxItems={{MaxItems}}&Stage={{Stage}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListFunctions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Marker](#API_ListFunctions_RequestSyntax) **   <a name="cloudfront-ListFunctions-request-uri-Marker"></a>
Use this field when paginating results to indicate where to begin in your list of functions. The response includes functions in the list that occur after the marker. To get the next page of the list, set this field's value to the value of `NextMarker` from the current page's response.

 ** [MaxItems](#API_ListFunctions_RequestSyntax) **   <a name="cloudfront-ListFunctions-request-uri-MaxItems"></a>
The maximum number of functions that you want in the response.

 ** [Stage](#API_ListFunctions_RequestSyntax) **   <a name="cloudfront-ListFunctions-request-uri-Stage"></a>
An optional filter to return only the functions that are in the specified stage, either `DEVELOPMENT` or `LIVE`.  
Valid Values: `DEVELOPMENT | LIVE` 

## Request Body
<a name="API_ListFunctions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListFunctions_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<FunctionList>
   <Items>
      <FunctionSummary>
         <FunctionConfig>
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
         </FunctionConfig>
         <FunctionMetadata>
            <CreatedTime>timestamp</CreatedTime>
            <FunctionARN>string</FunctionARN>
            <LastModifiedTime>timestamp</LastModifiedTime>
            <Stage>string</Stage>
         </FunctionMetadata>
         <Name>string</Name>
         <Status>string</Status>
      </FunctionSummary>
   </Items>
   <MaxItems>integer</MaxItems>
   <NextMarker>string</NextMarker>
   <Quantity>integer</Quantity>
</FunctionList>
```

## Response Elements
<a name="API_ListFunctions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [FunctionList](#API_ListFunctions_ResponseSyntax) **   <a name="cloudfront-ListFunctions-response-FunctionList"></a>
Root level tag for the FunctionList parameters.  
Required: Yes

 ** [Items](#API_ListFunctions_ResponseSyntax) **   <a name="cloudfront-ListFunctions-response-Items"></a>
Contains the functions in the list.  
Type: Array of [FunctionSummary](API_FunctionSummary.md) objects

 ** [MaxItems](#API_ListFunctions_ResponseSyntax) **   <a name="cloudfront-ListFunctions-response-MaxItems"></a>
The maximum number of functions requested.  
Type: Integer

 ** [NextMarker](#API_ListFunctions_ResponseSyntax) **   <a name="cloudfront-ListFunctions-response-NextMarker"></a>
If there are more items in the list than are in this response, this element is present. It contains the value that you should use in the `Marker` field of a subsequent request to continue listing functions where you left off.  
Type: String

 ** [Quantity](#API_ListFunctions_ResponseSyntax) **   <a name="cloudfront-ListFunctions-response-Quantity"></a>
The number of functions returned in the response.  
Type: Integer

## Errors
<a name="API_ListFunctions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
This operation is not supported in this AWS Region.  
HTTP Status Code: 400

## See Also
<a name="API_ListFunctions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListFunctions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/ListFunctions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListFunctions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListFunctions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListFunctions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListFunctions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListFunctions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListFunctions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListFunctions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListFunctions) 