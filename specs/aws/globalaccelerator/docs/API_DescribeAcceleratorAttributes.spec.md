---
id: "@specs/aws/globalaccelerator/docs/API_DescribeAcceleratorAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeAcceleratorAttributes"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# DescribeAcceleratorAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_DescribeAcceleratorAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeAcceleratorAttributes
<a name="API_DescribeAcceleratorAttributes"></a>

Describe the attributes of an accelerator. 

## Request Syntax
<a name="API_DescribeAcceleratorAttributes_RequestSyntax"></a>

```
{
   "AcceleratorArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAcceleratorAttributes_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AcceleratorArn](#API_DescribeAcceleratorAttributes_RequestSyntax) **   <a name="globalaccelerator-DescribeAcceleratorAttributes-request-AcceleratorArn"></a>
The Amazon Resource Name (ARN) of the accelerator with the attributes that you want to describe.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

## Response Syntax
<a name="API_DescribeAcceleratorAttributes_ResponseSyntax"></a>

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
<a name="API_DescribeAcceleratorAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AcceleratorAttributes](#API_DescribeAcceleratorAttributes_ResponseSyntax) **   <a name="globalaccelerator-DescribeAcceleratorAttributes-response-AcceleratorAttributes"></a>
The attributes of the accelerator.  
Type: [AcceleratorAttributes](API_AcceleratorAttributes.md) object

## Errors
<a name="API_DescribeAcceleratorAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AcceleratorNotFoundException **   
The accelerator that you specified doesn't exist.  
HTTP Status Code: 400

 ** InternalServiceErrorException **   
There was an internal error for AWS Global Accelerator.  
HTTP Status Code: 400

 ** InvalidArgumentException **   
An argument that you specified is invalid.  
HTTP Status Code: 400

## Examples
<a name="API_DescribeAcceleratorAttributes_Examples"></a>

### Describe attributes for an accelerator
<a name="API_DescribeAcceleratorAttributes_Example_1"></a>

The following is an example for describing the attributes for an accelerator.

```
aws globalaccelerator describe-accelerator-attributes 
       --accelerator-arn arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh
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
<a name="API_DescribeAcceleratorAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/DescribeAcceleratorAttributes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/DescribeAcceleratorAttributes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/DescribeAcceleratorAttributes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/DescribeAcceleratorAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/DescribeAcceleratorAttributes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/DescribeAcceleratorAttributes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/DescribeAcceleratorAttributes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/DescribeAcceleratorAttributes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/DescribeAcceleratorAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/DescribeAcceleratorAttributes) 