---
id: "@specs/aws/cloudfront/docs/API_ListRealtimeLogConfigs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListRealtimeLogConfigs"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ListRealtimeLogConfigs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ListRealtimeLogConfigs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListRealtimeLogConfigs
<a name="API_ListRealtimeLogConfigs"></a>

Gets a list of real-time log configurations.

You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the `NextMarker` value from the current response as the `Marker` value in the subsequent request.

## Request Syntax
<a name="API_ListRealtimeLogConfigs_RequestSyntax"></a>

```
GET /2020-05-31/realtime-log-config?Marker={{Marker}}&MaxItems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListRealtimeLogConfigs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Marker](#API_ListRealtimeLogConfigs_RequestSyntax) **   <a name="cloudfront-ListRealtimeLogConfigs-request-uri-Marker"></a>
Use this field when paginating results to indicate where to begin in your list of real-time log configurations. The response includes real-time log configurations in the list that occur after the marker. To get the next page of the list, set this field's value to the value of `NextMarker` from the current page's response.

 ** [MaxItems](#API_ListRealtimeLogConfigs_RequestSyntax) **   <a name="cloudfront-ListRealtimeLogConfigs-request-uri-MaxItems"></a>
The maximum number of real-time log configurations that you want in the response.

## Request Body
<a name="API_ListRealtimeLogConfigs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListRealtimeLogConfigs_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<RealtimeLogConfigs>
   <IsTruncated>boolean</IsTruncated>
   <Items>
      <RealtimeLogConfig>
         <ARN>string</ARN>
         <EndPoints>
            <EndPoint>
               <KinesisStreamConfig>
                  <RoleARN>string</RoleARN>
                  <StreamARN>string</StreamARN>
               </KinesisStreamConfig>
               <StreamType>string</StreamType>
            </EndPoint>
         </EndPoints>
         <Fields>
            <Field>string</Field>
         </Fields>
         <Name>string</Name>
         <SamplingRate>long</SamplingRate>
      </RealtimeLogConfig>
   </Items>
   <Marker>string</Marker>
   <MaxItems>integer</MaxItems>
   <NextMarker>string</NextMarker>
</RealtimeLogConfigs>
```

## Response Elements
<a name="API_ListRealtimeLogConfigs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [RealtimeLogConfigs](#API_ListRealtimeLogConfigs_ResponseSyntax) **   <a name="cloudfront-ListRealtimeLogConfigs-response-RealtimeLogConfigs"></a>
Root level tag for the RealtimeLogConfigs parameters.  
Required: Yes

 ** [IsTruncated](#API_ListRealtimeLogConfigs_ResponseSyntax) **   <a name="cloudfront-ListRealtimeLogConfigs-response-IsTruncated"></a>
A flag that indicates whether there are more real-time log configurations than are contained in this list.  
Type: Boolean

 ** [Items](#API_ListRealtimeLogConfigs_ResponseSyntax) **   <a name="cloudfront-ListRealtimeLogConfigs-response-Items"></a>
Contains the list of real-time log configurations.  
Type: Array of [RealtimeLogConfig](API_RealtimeLogConfig.md) objects

 ** [Marker](#API_ListRealtimeLogConfigs_ResponseSyntax) **   <a name="cloudfront-ListRealtimeLogConfigs-response-Marker"></a>
This parameter indicates where this list of real-time log configurations begins. This list includes real-time log configurations that occur after the marker.  
Type: String

 ** [MaxItems](#API_ListRealtimeLogConfigs_ResponseSyntax) **   <a name="cloudfront-ListRealtimeLogConfigs-response-MaxItems"></a>
The maximum number of real-time log configurations requested.  
Type: Integer

 ** [NextMarker](#API_ListRealtimeLogConfigs_ResponseSyntax) **   <a name="cloudfront-ListRealtimeLogConfigs-response-NextMarker"></a>
If there are more items in the list than are in this response, this element is present. It contains the value that you should use in the `Marker` field of a subsequent request to continue listing real-time log configurations where you left off.   
Type: String

## Errors
<a name="API_ListRealtimeLogConfigs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** NoSuchRealtimeLogConfig **   
The real-time log configuration does not exist.  
HTTP Status Code: 404

## See Also
<a name="API_ListRealtimeLogConfigs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListRealtimeLogConfigs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/ListRealtimeLogConfigs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListRealtimeLogConfigs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListRealtimeLogConfigs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListRealtimeLogConfigs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListRealtimeLogConfigs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListRealtimeLogConfigs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListRealtimeLogConfigs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListRealtimeLogConfigs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListRealtimeLogConfigs) 