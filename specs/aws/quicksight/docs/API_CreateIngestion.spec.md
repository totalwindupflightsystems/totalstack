---
id: "@specs/aws/quicksight/docs/API_CreateIngestion"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateIngestion"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateIngestion

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateIngestion
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateIngestion
<a name="API_CreateIngestion"></a>

Creates and starts a new SPICE ingestion for a dataset. You can manually refresh datasets in an Enterprise edition account 32 times in a 24-hour period. You can manually refresh datasets in a Standard edition account 8 times in a 24-hour period. Each 24-hour period is measured starting 24 hours before the current date and time.

Any ingestions operating on tagged datasets inherit the same tags automatically for use in access control. For an example, see [How do I create an IAM policy to control access to Amazon EC2 resources using tags?](http://aws.amazon.com/premiumsupport/knowledge-center/iam-ec2-resource-tags/) in the AWS Knowledge Center. Tags are visible on the tagged dataset, but not on the ingestion resource.

## Request Syntax
<a name="API_CreateIngestion_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/data-sets/{{DataSetId}}/ingestions/{{IngestionId}} HTTP/1.1
Content-type: application/json

{
   "IngestionType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateIngestion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateIngestion_RequestSyntax) **   <a name="QS-CreateIngestion-request-uri-AwsAccountId"></a>
The AWS account ID.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [DataSetId](#API_CreateIngestion_RequestSyntax) **   <a name="QS-CreateIngestion-request-uri-DataSetId"></a>
The ID of the dataset used in the ingestion.  
Required: Yes

 ** [IngestionId](#API_CreateIngestion_RequestSyntax) **   <a name="QS-CreateIngestion-request-uri-IngestionId"></a>
An ID for the ingestion.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-_]+$`   
Required: Yes

## Request Body
<a name="API_CreateIngestion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [IngestionType](#API_CreateIngestion_RequestSyntax) **   <a name="QS-CreateIngestion-request-IngestionType"></a>
The type of ingestion that you want to create.  
Type: String  
Valid Values: `INCREMENTAL_REFRESH | FULL_REFRESH`   
Required: No

## Response Syntax
<a name="API_CreateIngestion_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "IngestionId": "string",
   "IngestionStatus": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_CreateIngestion_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateIngestion_ResponseSyntax) **   <a name="QS-CreateIngestion-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateIngestion_ResponseSyntax) **   <a name="QS-CreateIngestion-response-Arn"></a>
The Amazon Resource Name (ARN) for the data ingestion.  
Type: String

 ** [IngestionId](#API_CreateIngestion_ResponseSyntax) **   <a name="QS-CreateIngestion-response-IngestionId"></a>
An ID for the ingestion.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-_]+$` 

 ** [IngestionStatus](#API_CreateIngestion_ResponseSyntax) **   <a name="QS-CreateIngestion-response-IngestionStatus"></a>
The ingestion status.  
Type: String  
Valid Values: `INITIALIZED | QUEUED | RUNNING | FAILED | COMPLETED | CANCELLED` 

 ** [RequestId](#API_CreateIngestion_ResponseSyntax) **   <a name="QS-CreateIngestion-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_CreateIngestion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** InternalFailureException **   
An internal failure occurred.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **   
A limit is exceeded.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
Limit exceeded.
HTTP Status Code: 409

 ** ResourceExistsException **   
The resource specified already exists.     
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 409

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## Examples
<a name="API_CreateIngestion_Examples"></a>

### Example
<a name="API_CreateIngestion_Example_1"></a>

This example illustrates one usage of CreateIngestion.

#### Sample Request
<a name="API_CreateIngestion_Example_1_Request"></a>

```
PUT /accounts/*AwsAccountId*/data-sets/*DataSetID*/ingestions/*IngestionID* HTTP/1.1
```

## See Also
<a name="API_CreateIngestion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateIngestion) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateIngestion) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateIngestion) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateIngestion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateIngestion) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateIngestion) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateIngestion) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateIngestion) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateIngestion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateIngestion) 