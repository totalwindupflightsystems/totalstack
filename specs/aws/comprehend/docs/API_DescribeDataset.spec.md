---
id: "@specs/aws/comprehend/docs/API_DescribeDataset"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDataset"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# DescribeDataset

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_DescribeDataset
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDataset
<a name="API_DescribeDataset"></a>

Returns information about the dataset that you specify. For more information about datasets, see [ Flywheel overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html) in the *Amazon Comprehend Developer Guide*.

## Request Syntax
<a name="API_DescribeDataset_RequestSyntax"></a>

```
{
   "DatasetArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDataset_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DatasetArn](#API_DescribeDataset_RequestSyntax) **   <a name="comprehend-DescribeDataset-request-DatasetArn"></a>
The ARN of the dataset.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:flywheel/[a-zA-Z0-9](-*[a-zA-Z0-9])*/dataset/[a-zA-Z0-9](-*[a-zA-Z0-9])*`   
Required: Yes

## Response Syntax
<a name="API_DescribeDataset_ResponseSyntax"></a>

```
{
   "DatasetProperties": { 
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
}
```

## Response Elements
<a name="API_DescribeDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DatasetProperties](#API_DescribeDataset_ResponseSyntax) **   <a name="comprehend-DescribeDataset-response-DatasetProperties"></a>
The dataset properties.  
Type: [DatasetProperties](API_DatasetProperties.md) object

## Errors
<a name="API_DescribeDataset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

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
<a name="API_DescribeDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/DescribeDataset) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/DescribeDataset) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/DescribeDataset) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/DescribeDataset) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/DescribeDataset) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/DescribeDataset) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/DescribeDataset) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/DescribeDataset) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/DescribeDataset) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/DescribeDataset) 