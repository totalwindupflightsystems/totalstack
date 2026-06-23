---
id: "@specs/aws/comprehend/docs/API_CreateDataset"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDataset"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# CreateDataset

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_CreateDataset
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDataset
<a name="API_CreateDataset"></a>

Creates a dataset to upload training or test data for a model associated with a flywheel. For more information about datasets, see [ Flywheel overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html) in the *Amazon Comprehend Developer Guide*.

## Request Syntax
<a name="API_CreateDataset_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "DatasetName": "{{string}}",
   "DatasetType": "{{string}}",
   "Description": "{{string}}",
   "FlywheelArn": "{{string}}",
   "InputDataConfig": { 
      "AugmentedManifests": [ 
         { 
            "AnnotationDataS3Uri": "{{string}}",
            "AttributeNames": [ "{{string}}" ],
            "DocumentType": "{{string}}",
            "S3Uri": "{{string}}",
            "SourceDocumentsS3Uri": "{{string}}"
         }
      ],
      "DataFormat": "{{string}}",
      "DocumentClassifierInputDataConfig": { 
         "LabelDelimiter": "{{string}}",
         "S3Uri": "{{string}}"
      },
      "EntityRecognizerInputDataConfig": { 
         "Annotations": { 
            "S3Uri": "{{string}}"
         },
         "Documents": { 
            "InputFormat": "{{string}}",
            "S3Uri": "{{string}}"
         },
         "EntityList": { 
            "S3Uri": "{{string}}"
         }
      }
   },
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateDataset_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateDataset_RequestSyntax) **   <a name="comprehend-CreateDataset-request-ClientRequestToken"></a>
A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [DatasetName](#API_CreateDataset_RequestSyntax) **   <a name="comprehend-CreateDataset-request-DatasetName"></a>
Name of the dataset.  
Type: String  
Length Constraints: Maximum length of 63.  
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`   
Required: Yes

 ** [DatasetType](#API_CreateDataset_RequestSyntax) **   <a name="comprehend-CreateDataset-request-DatasetType"></a>
The dataset type. You can specify that the data in a dataset is for training the model or for testing the model.  
Type: String  
Valid Values: `TRAIN | TEST`   
Required: No

 ** [Description](#API_CreateDataset_RequestSyntax) **   <a name="comprehend-CreateDataset-request-Description"></a>
Description of the dataset.  
Type: String  
Length Constraints: Maximum length of 2048.  
Pattern: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`   
Required: No

 ** [FlywheelArn](#API_CreateDataset_RequestSyntax) **   <a name="comprehend-CreateDataset-request-FlywheelArn"></a>
The Amazon Resource Number (ARN) of the flywheel of the flywheel to receive the data.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:flywheel/[a-zA-Z0-9](-*[a-zA-Z0-9])*`   
Required: Yes

 ** [InputDataConfig](#API_CreateDataset_RequestSyntax) **   <a name="comprehend-CreateDataset-request-InputDataConfig"></a>
Information about the input data configuration. The type of input data varies based on the format of the input and whether the data is for a classifier model or an entity recognition model.  
Type: [DatasetInputDataConfig](API_DatasetInputDataConfig.md) object  
Required: Yes

 ** [Tags](#API_CreateDataset_RequestSyntax) **   <a name="comprehend-CreateDataset-request-Tags"></a>
Tags for the dataset.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Syntax
<a name="API_CreateDataset_ResponseSyntax"></a>

```
{
   "DatasetArn": "string"
}
```

## Response Elements
<a name="API_CreateDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DatasetArn](#API_CreateDataset_ResponseSyntax) **   <a name="comprehend-CreateDataset-response-DatasetArn"></a>
The ARN of the dataset.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws(-[^:]+)?:comprehend:[a-zA-Z0-9-]*:[0-9]{12}:flywheel/[a-zA-Z0-9](-*[a-zA-Z0-9])*/dataset/[a-zA-Z0-9](-*[a-zA-Z0-9])*` 

## Errors
<a name="API_CreateDataset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** InvalidRequestException **   
The request is invalid.    
 ** Detail **   
Provides additional detail about why the request failed.
HTTP Status Code: 400

 ** ResourceInUseException **   
The specified resource name is already in use. Use a different name and try your request again.  
HTTP Status Code: 400

 ** ResourceLimitExceededException **   
The maximum number of resources per account has been exceeded. Review the resources, and then try your request again.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The specified resource ARN was not found. Check the ARN and try your request again.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 400

 ** TooManyTagsException **   
The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request.   
HTTP Status Code: 400

## See Also
<a name="API_CreateDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/CreateDataset) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/CreateDataset) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/CreateDataset) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/CreateDataset) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/CreateDataset) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/CreateDataset) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/CreateDataset) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/CreateDataset) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/CreateDataset) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/CreateDataset) 