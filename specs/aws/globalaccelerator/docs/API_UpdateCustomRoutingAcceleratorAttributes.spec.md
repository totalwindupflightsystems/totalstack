---
id: "@specs/aws/globalaccelerator/docs/API_UpdateCustomRoutingAcceleratorAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateCustomRoutingAcceleratorAttributes"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# UpdateCustomRoutingAcceleratorAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_UpdateCustomRoutingAcceleratorAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateCustomRoutingAcceleratorAttributes
<a name="API_UpdateCustomRoutingAcceleratorAttributes"></a>

Update the attributes for a custom routing accelerator. 

## Request Syntax
<a name="API_UpdateCustomRoutingAcceleratorAttributes_RequestSyntax"></a>

```
{
   "AcceleratorArn": "{{string}}",
   "FlowLogsEnabled": {{boolean}},
   "FlowLogsS3Bucket": "{{string}}",
   "FlowLogsS3Prefix": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateCustomRoutingAcceleratorAttributes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AcceleratorArn](#API_UpdateCustomRoutingAcceleratorAttributes_RequestSyntax) **   <a name="globalaccelerator-UpdateCustomRoutingAcceleratorAttributes-request-AcceleratorArn"></a>
The Amazon Resource Name (ARN) of the custom routing accelerator to update attributes for.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [FlowLogsEnabled](#API_UpdateCustomRoutingAcceleratorAttributes_RequestSyntax) **   <a name="globalaccelerator-UpdateCustomRoutingAcceleratorAttributes-request-FlowLogsEnabled"></a>
Update whether flow logs are enabled. The default value is false. If the value is true, `FlowLogsS3Bucket` and `FlowLogsS3Prefix` must be specified.  
For more information, see [Flow logs](https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html) in the * AWS Global Accelerator Developer Guide*.  
Type: Boolean  
Required: No

 ** [FlowLogsS3Bucket](#API_UpdateCustomRoutingAcceleratorAttributes_RequestSyntax) **   <a name="globalaccelerator-UpdateCustomRoutingAcceleratorAttributes-request-FlowLogsS3Bucket"></a>
The name of the Amazon S3 bucket for the flow logs. Attribute is required if `FlowLogsEnabled` is `true`. The bucket must exist and have a bucket policy that grants AWS Global Accelerator permission to write to the bucket.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

 ** [FlowLogsS3Prefix](#API_UpdateCustomRoutingAcceleratorAttributes_RequestSyntax) **   <a name="globalaccelerator-UpdateCustomRoutingAcceleratorAttributes-request-FlowLogsS3Prefix"></a>
Update the prefix for the location in the Amazon S3 bucket for the flow logs. Attribute is required if `FlowLogsEnabled` is `true`.   
If you specify slash (/) for the S3 bucket prefix, the log file bucket folder structure will include a double slash (//), like the following:  
DOC-EXAMPLE-BUCKET//AWSLogs/aws\_account\_id  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

## Response Syntax
<a name="API_UpdateCustomRoutingAcceleratorAttributes_ResponseSyntax"></a>

```
{
   "AcceleratorAttributes": { 
      "FlowLogsEnabled": boolean,
      "FlowLogsS3Bucket": "string",
      "FlowLogsS3Prefix": "string"
   }
}
```

## Response Elements
<a name="API_UpdateCustomRoutingAcceleratorAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AcceleratorAttributes](#API_UpdateCustomRoutingAcceleratorAttributes_ResponseSyntax) **   <a name="globalaccelerator-UpdateCustomRoutingAcceleratorAttributes-response-AcceleratorAttributes"></a>
Updated custom routing accelerator.  
Type: [CustomRoutingAcceleratorAttributes](API_CustomRoutingAcceleratorAttributes.md) object

## Errors
<a name="API_UpdateCustomRoutingAcceleratorAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AcceleratorNotFoundException **   
The accelerator that you specified doesn't exist.  
HTTP Status Code: 400

 ** AccessDeniedException **   
You don't have access permission.  
HTTP Status Code: 400

 ** InternalServiceErrorException **   
There was an internal error for AWS Global Accelerator.  
HTTP Status Code: 400

 ** InvalidArgumentException **   
An argument that you specified is invalid.  
HTTP Status Code: 400

 ** TransactionInProgressException **   
There's already a transaction in progress. Another transaction can't be processed.  
HTTP Status Code: 400

## Examples
<a name="API_UpdateCustomRoutingAcceleratorAttributes_Examples"></a>

### Update attributes for an accelerator
<a name="API_UpdateCustomRoutingAcceleratorAttributes_Example_1"></a>

The following is an example for updating a custom routing accelerator to enable flow logs.

```
aws globalaccelerator update-custom-routing-accelerator-attributes 
       --accelerator-arn arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh 
       --flow-logs-enabled 
       --flow-logs-s3-bucket flowlogs-abc 
       --flow-logs-s3-prefix bucketprefix-abc
       --region us-west-2
```

```
{
    "AcceleratorAttributes": {
        "FlowLogsEnabled": true
        "FlowLogsS3Bucket": flowlogs-abc
        "FlowLogsS3Prefix": bucketprefix-abc
    }
}
```

## See Also
<a name="API_UpdateCustomRoutingAcceleratorAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/UpdateCustomRoutingAcceleratorAttributes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/UpdateCustomRoutingAcceleratorAttributes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/UpdateCustomRoutingAcceleratorAttributes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/UpdateCustomRoutingAcceleratorAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/UpdateCustomRoutingAcceleratorAttributes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/UpdateCustomRoutingAcceleratorAttributes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/UpdateCustomRoutingAcceleratorAttributes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/UpdateCustomRoutingAcceleratorAttributes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/UpdateCustomRoutingAcceleratorAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/UpdateCustomRoutingAcceleratorAttributes) 