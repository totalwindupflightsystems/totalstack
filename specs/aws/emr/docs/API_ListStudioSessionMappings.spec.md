---
id: "@specs/aws/emr/docs/API_ListStudioSessionMappings"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListStudioSessionMappings"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ListStudioSessionMappings

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ListStudioSessionMappings
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListStudioSessionMappings
<a name="API_ListStudioSessionMappings"></a>

Returns a list of all user or group session mappings for the Amazon EMR Studio specified by `StudioId`.

## Request Syntax
<a name="API_ListStudioSessionMappings_RequestSyntax"></a>

```
{
   "IdentityType": "{{string}}",
   "Marker": "{{string}}",
   "StudioId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListStudioSessionMappings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IdentityType](#API_ListStudioSessionMappings_RequestSyntax) **   <a name="EMR-ListStudioSessionMappings-request-IdentityType"></a>
Specifies whether to return session mappings for users or groups. If not specified, the results include session mapping details for both users and groups.  
Type: String  
Valid Values: `USER | GROUP`   
Required: No

 ** [Marker](#API_ListStudioSessionMappings_RequestSyntax) **   <a name="EMR-ListStudioSessionMappings-request-Marker"></a>
The pagination token that indicates the set of results to retrieve.  
Type: String  
Required: No

 ** [StudioId](#API_ListStudioSessionMappings_RequestSyntax) **   <a name="EMR-ListStudioSessionMappings-request-StudioId"></a>
The ID of the Amazon EMR Studio.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: No

## Response Syntax
<a name="API_ListStudioSessionMappings_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "SessionMappings": [ 
      { 
         "CreationTime": number,
         "IdentityId": "string",
         "IdentityName": "string",
         "IdentityType": "string",
         "SessionPolicyArn": "string",
         "StudioId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListStudioSessionMappings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_ListStudioSessionMappings_ResponseSyntax) **   <a name="EMR-ListStudioSessionMappings-response-Marker"></a>
The pagination token that indicates the next set of results to retrieve.  
Type: String

 ** [SessionMappings](#API_ListStudioSessionMappings_ResponseSyntax) **   <a name="EMR-ListStudioSessionMappings-response-SessionMappings"></a>
A list of session mapping summary objects. Each object includes session mapping details such as creation time, identity type (user or group), and Amazon EMR Studio ID.  
Type: Array of [SessionMappingSummary](API_SessionMappingSummary.md) objects

## Errors
<a name="API_ListStudioSessionMappings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Indicates that an error occurred while processing the request and that the request was not completed.  
HTTP Status Code: 400

 ** InvalidRequestException **   
This exception occurs when there is something wrong with user input.    
 ** ErrorCode **   
The error code associated with the exception.  
 ** Message **   
The message associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListStudioSessionMappings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/ListStudioSessionMappings) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/ListStudioSessionMappings) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ListStudioSessionMappings) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/ListStudioSessionMappings) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ListStudioSessionMappings) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/ListStudioSessionMappings) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/ListStudioSessionMappings) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/ListStudioSessionMappings) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/ListStudioSessionMappings) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ListStudioSessionMappings) 