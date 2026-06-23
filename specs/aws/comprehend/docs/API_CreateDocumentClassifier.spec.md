---
id: "@specs/aws/comprehend/docs/API_CreateDocumentClassifier"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDocumentClassifier"
status: active
depends_on:
  - "@specs/aws/comprehend/meta"
---

# CreateDocumentClassifier

> **source:** AWS Documentation
> **spec:id:** @specs/aws/comprehend/docs/API_CreateDocumentClassifier
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDocumentClassifier
<a name="API_CreateDocumentClassifier"></a>

Creates a new document classifier that you can use to categorize documents. To create a classifier, you provide a set of training documents that are labeled with the categories that you want to use. For more information, see [Training classifier models](https://docs.aws.amazon.com/comprehend/latest/dg/training-classifier-model.html) in the Comprehend Developer Guide. 

## Request Syntax
<a name="API_CreateDocumentClassifier_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "DataAccessRoleArn": "{{string}}",
   "DocumentClassifierName": "{{string}}",
   "InputDataConfig": { 
      "AugmentedManifests": [ 
         { 
            "AnnotationDataS3Uri": "{{string}}",
            "AttributeNames": [ "{{string}}" ],
            "DocumentType": "{{string}}",
            "S3Uri": "{{string}}",
            "SourceDocumentsS3Uri": "{{string}}",
            "Split": "{{string}}"
         }
      ],
      "DataFormat": "{{string}}",
      "DocumentReaderConfig": { 
         "DocumentReadAction": "{{string}}",
         "DocumentReadMode": "{{string}}",
         "FeatureTypes": [ "{{string}}" ]
      },
      "Documents": { 
         "S3Uri": "{{string}}",
         "TestS3Uri": "{{string}}"
      },
      "DocumentType": "{{string}}",
      "LabelDelimiter": "{{string}}",
      "S3Uri": "{{string}}",
      "TestS3Uri": "{{string}}"
   },
   "LanguageCode": "{{string}}",
   "Mode": "{{string}}",
   "ModelKmsKeyId": "{{string}}",
   "ModelPolicy": "{{string}}",
   "OutputDataConfig": { 
      "FlywheelStatsS3Prefix": "{{string}}",
      "KmsKeyId": "{{string}}",
      "S3Uri": "{{string}}"
   },
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VersionName": "{{string}}",
   "VolumeKmsKeyId": "{{string}}",
   "VpcConfig": { 
      "SecurityGroupIds": [ "{{string}}" ],
      "Subnets": [ "{{string}}" ]
   }
}
```

## Request Parameters
<a name="API_CreateDocumentClassifier_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateDocumentClassifier_RequestSyntax) **   <a name="comprehend-CreateDocumentClassifier-request-ClientRequestToken"></a>
A unique identifier for the request. If you don't set the client request token, Amazon Comprehend generates one.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [DataAccessRoleArn](#API_CreateDocumentClassifier_RequestSyntax) **   <a name="comprehend-CreateDocumentClassifier-request-DataAccessRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants Amazon Comprehend read access to your input data.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`   
Required: Yes

 ** [DocumentClassifierName](#API_CreateDocumentClassifier_RequestSyntax) **   <a name="comprehend-CreateDocumentClassifier-request-DocumentClassifierName"></a>
The name of the document classifier.  
Type: String  
Length Constraints: Maximum length of 63.  
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`   
Required: Yes

 ** [InputDataConfig](#API_CreateDocumentClassifier_RequestSyntax) **   <a name="comprehend-CreateDocumentClassifier-request-InputDataConfig"></a>
Specifies the format and location of the input data for the job.  
Type: [DocumentClassifierInputDataConfig](API_DocumentClassifierInputDataConfig.md) object  
Required: Yes

 ** [LanguageCode](#API_CreateDocumentClassifier_RequestSyntax) **   <a name="comprehend-CreateDocumentClassifier-request-LanguageCode"></a>
The language of the input documents. You can specify any of the languages supported by Amazon Comprehend. All documents must be in the same language.  
Type: String  
Valid Values: `en | es | fr | de | it | pt | ar | hi | ja | ko | zh | zh-TW`   
Required: Yes

 ** [Mode](#API_CreateDocumentClassifier_RequestSyntax) **   <a name="comprehend-CreateDocumentClassifier-request-Mode"></a>
Indicates the mode in which the classifier will be trained. The classifier can be trained in multi-class (single-label) mode or multi-label mode. Multi-class mode identifies a single class label for each document and multi-label mode identifies one or more class labels for each document. Multiple labels for an individual document are separated by a delimiter. The default delimiter between labels is a pipe (\|).  
Type: String  
Valid Values: `MULTI_CLASS | MULTI_LABEL`   
Required: No

 ** [ModelKmsKeyId](#API_CreateDocumentClassifier_RequestSyntax) **   <a name="comprehend-CreateDocumentClassifier-request-ModelKmsKeyId"></a>
ID for the AWS KMS key that Amazon Comprehend uses to encrypt trained custom models. The ModelKmsKeyId can be either of the following formats:  
+ KMS Key ID: `"1234abcd-12ab-34cd-56ef-1234567890ab"` 
+ Amazon Resource Name (ARN) of a KMS Key: `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"` 
Type: String  
Length Constraints: Maximum length of 2048.  
Pattern: `^\p{ASCII}+$`   
Required: No

 ** [ModelPolicy](#API_CreateDocumentClassifier_RequestSyntax) **   <a name="comprehend-CreateDocumentClassifier-request-ModelPolicy"></a>
The resource-based policy to attach to your custom document classifier model. You can use this policy to allow another AWS account to import your custom model.  
Provide your policy as a JSON body that you enter as a UTF-8 encoded string without line breaks. To provide valid JSON, enclose the attribute names and values in double quotes. If the JSON body is also enclosed in double quotes, then you must escape the double quotes that are inside the policy:  
 `"{\"attribute\": \"value\", \"attribute\": [\"value\"]}"`   
To avoid escaping quotes, you can use single quotes to enclose the policy and double quotes to enclose the JSON names and values:  
 `'{"attribute": "value", "attribute": ["value"]}'`   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20000.  
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`   
Required: No

 ** [OutputDataConfig](#API_CreateDocumentClassifier_RequestSyntax) **   <a name="comprehend-CreateDocumentClassifier-request-OutputDataConfig"></a>
Specifies the location for the output files from a custom classifier job. This parameter is required for a request that creates a native document model.  
Type: [DocumentClassifierOutputDataConfig](API_DocumentClassifierOutputDataConfig.md) object  
Required: No

 ** [Tags](#API_CreateDocumentClassifier_RequestSyntax) **   <a name="comprehend-CreateDocumentClassifier-request-Tags"></a>
Tags to associate with the document classifier. A tag is a key-value pair that adds as a metadata to a resource used by Amazon Comprehend. For example, a tag with "Sales" as the key might be added to a resource to indicate its use by the sales department.   
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** [VersionName](#API_CreateDocumentClassifier_RequestSyntax) **   <a name="comprehend-CreateDocumentClassifier-request-VersionName"></a>
The version name given to the newly created classifier. Version names can have a maximum of 256 characters. Alphanumeric characters, hyphens (-) and underscores (\_) are allowed. The version name must be unique among all models with the same classifier name in the AWS account/AWS Region.  
Type: String  
Length Constraints: Maximum length of 63.  
Pattern: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*$`   
Required: No

 ** [VolumeKmsKeyId](#API_CreateDocumentClassifier_RequestSyntax) **   <a name="comprehend-CreateDocumentClassifier-request-VolumeKmsKeyId"></a>
ID for the AWS Key Management Service (KMS) key that Amazon Comprehend uses to encrypt data on the storage volume attached to the ML compute instance(s) that process the analysis job. The VolumeKmsKeyId can be either of the following formats:  
+ KMS Key ID: `"1234abcd-12ab-34cd-56ef-1234567890ab"` 
+ Amazon Resource Name (ARN) of a KMS Key: `"arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"` 
Type: String  
Length Constraints: Maximum length of 2048.  
Pattern: `^\p{ASCII}+$`   
Required: No

 ** [VpcConfig](#API_CreateDocumentClassifier_RequestSyntax) **   <a name="comprehend-CreateDocumentClassifier-request-VpcConfig"></a>
Configuration parameters for an optional private Virtual Private Cloud (VPC) containing the resources you are using for your custom classifier. For more information, see [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).   
Type: [VpcConfig](API_VpcConfig.md) object  
Required: No

## Response Syntax
<a name="API_CreateDocumentClassifier_ResponseSyntax"></a>

```
{
   "DocumentClassifierArn": "string"
}
```

## Response Elements
<a name="API_CreateDocumentClassifier_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DocumentClassifierArn](#API_CreateDocumentClassifier_ResponseSyntax) **   <a name="comprehend-CreateDocumentClassifier-response-DocumentClassifierArn"></a>
The Amazon Resource Name (ARN) that identifies the document classifier.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:aws[A-Za-z0-9-]{0,63}:comprehend:[A-Za-z0-9-]{0,63}:([0-9]{12}|aws):document-classifier/[A-Za-z0-9-]{0,63}(/version/[A-Za-z0-9-]{0,63})?` 

## Errors
<a name="API_CreateDocumentClassifier_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** InvalidRequestException **   
The request is invalid.    
 ** Detail **   
Provides additional detail about why the request failed.
HTTP Status Code: 400

 ** KmsKeyValidationException **   
The KMS customer managed key (CMK) entered cannot be validated. Verify the key and re-enter it.  
HTTP Status Code: 400

 ** ResourceInUseException **   
The specified resource name is already in use. Use a different name and try your request again.  
HTTP Status Code: 400

 ** ResourceLimitExceededException **   
The maximum number of resources per account has been exceeded. Review the resources, and then try your request again.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 400

 ** TooManyTagsException **   
The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request.   
HTTP Status Code: 400

 ** UnsupportedLanguageException **   
Amazon Comprehend can't process the language of the input text. For a list of supported languages, [Supported languages](https://docs.aws.amazon.com/comprehend/latest/dg/supported-languages.html) in the Comprehend Developer Guide.   
HTTP Status Code: 400

## See Also
<a name="API_CreateDocumentClassifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehend-2017-11-27/CreateDocumentClassifier) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehend-2017-11-27/CreateDocumentClassifier) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/CreateDocumentClassifier) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehend-2017-11-27/CreateDocumentClassifier) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/CreateDocumentClassifier) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehend-2017-11-27/CreateDocumentClassifier) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehend-2017-11-27/CreateDocumentClassifier) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehend-2017-11-27/CreateDocumentClassifier) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehend-2017-11-27/CreateDocumentClassifier) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/CreateDocumentClassifier) 