---
id: "@specs/aws/emr/docs/API_ListReleaseLabels"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListReleaseLabels"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ListReleaseLabels

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ListReleaseLabels
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListReleaseLabels
<a name="API_ListReleaseLabels"></a>

Retrieves release labels of Amazon EMR services in the Region where the API is called.

## Request Syntax
<a name="API_ListReleaseLabels_RequestSyntax"></a>

```
{
   "Filters": { 
      "Application": "{{string}}",
      "Prefix": "{{string}}"
   },
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListReleaseLabels_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListReleaseLabels_RequestSyntax) **   <a name="EMR-ListReleaseLabels-request-Filters"></a>
Filters the results of the request. `Prefix` specifies the prefix of release labels to return. `Application` specifies the application (with/without version) of release labels to return.  
Type: [ReleaseLabelFilter](API_ReleaseLabelFilter.md) object  
Required: No

 ** [MaxResults](#API_ListReleaseLabels_RequestSyntax) **   <a name="EMR-ListReleaseLabels-request-MaxResults"></a>
Defines the maximum number of release labels to return in a single response. The default is `100`.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListReleaseLabels_RequestSyntax) **   <a name="EMR-ListReleaseLabels-request-NextToken"></a>
Specifies the next page of results. If `NextToken` is not specified, which is usually the case for the first request of ListReleaseLabels, the first page of results are determined by other filtering parameters or by the latest version. The `ListReleaseLabels` request fails if the identity (AWS account ID) and all filtering parameters are different from the original request, or if the `NextToken` is expired or tampered with.  
Type: String  
Required: No

## Response Syntax
<a name="API_ListReleaseLabels_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ReleaseLabels": [ "string" ]
}
```

## Response Elements
<a name="API_ListReleaseLabels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListReleaseLabels_ResponseSyntax) **   <a name="EMR-ListReleaseLabels-response-NextToken"></a>
Used to paginate the next page of results if specified in the next `ListReleaseLabels` request.  
Type: String

 ** [ReleaseLabels](#API_ListReleaseLabels_ResponseSyntax) **   <a name="EMR-ListReleaseLabels-response-ReleaseLabels"></a>
The returned release labels.  
Type: Array of strings

## Errors
<a name="API_ListReleaseLabels_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
This exception occurs when there is an internal failure in the Amazon EMR service.    
 ** Message **   
The message associated with the exception.
HTTP Status Code: 500

 ** InvalidRequestException **   
This exception occurs when there is something wrong with user input.    
 ** ErrorCode **   
The error code associated with the exception.  
 ** Message **   
The message associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListReleaseLabels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/ListReleaseLabels) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/ListReleaseLabels) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ListReleaseLabels) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/ListReleaseLabels) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ListReleaseLabels) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/ListReleaseLabels) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/ListReleaseLabels) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/ListReleaseLabels) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/ListReleaseLabels) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ListReleaseLabels) 