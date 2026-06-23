---
id: "@specs/aws/comprehend/docs/API_ListDatasets"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListDatasets"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# ListDatasets

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_ListDatasets
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListDatasets
<a name="API_ListDatasets"></a>

List the datasets that you have configured in this Region. For more information about datasets, see [ Flywheel overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html) in the *Amazon Comprehend Developer Guide*.

## Request Syntax
<a name="API_ListDatasets_RequestSyntax"></a>

```
{
   "Filter": { 
      "CreationTimeAfter": {{number}},
      "CreationTimeBefore": {{number}},
      "DatasetType": "{{string}}",
      "Status": "{{string}}"
   },
   "FlywheelArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDatasets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filter](#API_ListDatasets_RequestSyntax) **   <a name="comprehend-ListDatasets-request-Filter"></a>
Filters the datasets to be returned in the response.  
Type: [DatasetFilter](API_DatasetFilter.md) object  
Required: No

 ** [FlywheelArn](#API_ListDatasets_RequestSyntax) **   <a name="comprehend-ListDatasets-request-FlywheelArn"></a>
The Amazon Resource Number (ARN) of the flywheel.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:flywheel/[a-zA-Z0-9](-*[a-zA-Z0-9])*`   
Required: No

 ** [MaxResults](#API_ListDatasets_RequestSyntax) **   <a name="comprehend-ListDatasets-request-MaxResults"></a>
Maximum number of results to return in a response. The default is 100.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 500.  
Required: No

 ** [NextToken](#API_ListDatasets_RequestSyntax) **   <a name="comprehend-ListDatasets-request-NextToken"></a>
Identifies the next page of results to return.  
Type: String  
Length Constraints: Minimum length of 1.  
Required: No

## Response Syntax
<a name="API_ListDatasets_ResponseSyntax"></a>

```
{
   "DatasetPropertiesList": [ 
      { 
         "CreationTime": number,
         "DatasetArn": "string",
         "DatasetName": "string",
         "DatasetS3Uri": "string",
         "DatasetType": "string",
         "Description": "string",
         "EndTime": number,
         "Message": "string",
         "NumberOfDocuments": number,
         "Status": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDatasets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DatasetPropertiesList](#API_ListDatasets_ResponseSyntax) **   <a name="comprehend-ListDatasets-response-DatasetPropertiesList"></a>
The dataset properties list.  
Type: Array of [DatasetProperties](API_DatasetProperties.md) objects

 ** [NextToken](#API_ListDatasets_ResponseSyntax) **   <a name="comprehend-ListDatasets-response-NextToken"></a>
Identifies the next page of results to return.  
Type: String  
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListDatasets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** InvalidFilterException **   
The filter specified for the operation is invalid. Specify a different filter.  
HTTP Status Code: 400

 ** InvalidRequestException **   
The request is invalid.    
 ** Detail **   
Provides additional detail about why the request failed.
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The specified resource ARN was not found. Check the ARN and try your request again.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 400

## See Also
<a name="API_ListDatasets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/ListDatasets) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/ListDatasets) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/ListDatasets) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/ListDatasets) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/ListDatasets) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/ListDatasets) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/ListDatasets) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/ListDatasets) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/ListDatasets) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/ListDatasets) 