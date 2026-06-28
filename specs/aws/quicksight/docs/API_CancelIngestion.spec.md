---
id: "@specs/aws/quicksight/docs/API_CancelIngestion"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CancelIngestion"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CancelIngestion

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CancelIngestion
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CancelIngestion
<a name="API_CancelIngestion"></a>

Cancels an ongoing ingestion of data into SPICE.

## Request Syntax
<a name="API_CancelIngestion_RequestSyntax"></a>

```
DELETE /accounts/{{AwsAccountId}}/data-sets/{{DataSetId}}/ingestions/{{IngestionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelIngestion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CancelIngestion_RequestSyntax) **   <a name="QS-CancelIngestion-request-uri-AwsAccountId"></a>
The AWS account ID.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [DataSetId](#API_CancelIngestion_RequestSyntax) **   <a name="QS-CancelIngestion-request-uri-DataSetId"></a>
The ID of the dataset used in the ingestion.  
Required: Yes

 ** [IngestionId](#API_CancelIngestion_RequestSyntax) **   <a name="QS-CancelIngestion-request-uri-IngestionId"></a>
An ID for the ingestion.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-_]+$`   
Required: Yes

## Request Body
<a name="API_CancelIngestion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelIngestion_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "IngestionId": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_CancelIngestion_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CancelIngestion_ResponseSyntax) **   <a name="QS-CancelIngestion-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CancelIngestion_ResponseSyntax) **   <a name="QS-CancelIngestion-response-Arn"></a>
The Amazon Resource Name (ARN) for the data ingestion.  
Type: String

 ** [IngestionId](#API_CancelIngestion_ResponseSyntax) **   <a name="QS-CancelIngestion-response-IngestionId"></a>
An ID for the ingestion.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-_]+$` 

 ** [RequestId](#API_CancelIngestion_ResponseSyntax) **   <a name="QS-CancelIngestion-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_CancelIngestion_Errors"></a>

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
<a name="API_CancelIngestion_Examples"></a>

### Example
<a name="API_CancelIngestion_Example_1"></a>

This example illustrates one usage of CancelIngestion.

#### Sample Request
<a name="API_CancelIngestion_Example_1_Request"></a>

```
DELETE /accounts/*AwsAccountId*/data-sets/*DataSetID*/ingestions/*IngestionID* HTTP/1.1
```

## See Also
<a name="API_CancelIngestion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CancelIngestion) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CancelIngestion) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CancelIngestion) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CancelIngestion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CancelIngestion) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CancelIngestion) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CancelIngestion) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CancelIngestion) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CancelIngestion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CancelIngestion) 