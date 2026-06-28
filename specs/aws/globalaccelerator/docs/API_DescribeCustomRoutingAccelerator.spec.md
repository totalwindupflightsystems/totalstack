---
id: "@specs/aws/globalaccelerator/docs/API_DescribeCustomRoutingAccelerator"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeCustomRoutingAccelerator"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# DescribeCustomRoutingAccelerator

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_DescribeCustomRoutingAccelerator
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeCustomRoutingAccelerator
<a name="API_DescribeCustomRoutingAccelerator"></a>

Describe a custom routing accelerator. 

## Request Syntax
<a name="API_DescribeCustomRoutingAccelerator_RequestSyntax"></a>

```
{
   "AcceleratorArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCustomRoutingAccelerator_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AcceleratorArn](#API_DescribeCustomRoutingAccelerator_RequestSyntax) **   <a name="globalaccelerator-DescribeCustomRoutingAccelerator-request-AcceleratorArn"></a>
The Amazon Resource Name (ARN) of the accelerator to describe.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

## Response Syntax
<a name="API_DescribeCustomRoutingAccelerator_ResponseSyntax"></a>

```
{
   "Accelerator": { 
      "AcceleratorArn": "string",
      "CreatedTime": number,
      "DnsName": "string",
      "Enabled": boolean,
      "IpAddressType": "string",
      "IpSets": [ 
         { 
            "IpAddresses": [ "string" ],
            "IpAddressFamily": "string",
            "IpFamily": "string"
         }
      ],
      "LastModifiedTime": number,
      "Name": "string",
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_DescribeCustomRoutingAccelerator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Accelerator](#API_DescribeCustomRoutingAccelerator_ResponseSyntax) **   <a name="globalaccelerator-DescribeCustomRoutingAccelerator-response-Accelerator"></a>
The description of the custom routing accelerator.  
Type: [CustomRoutingAccelerator](API_CustomRoutingAccelerator.md) object

## Errors
<a name="API_DescribeCustomRoutingAccelerator_Errors"></a>

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
<a name="API_DescribeCustomRoutingAccelerator_Examples"></a>

### Describe a custom routing accelerator
<a name="API_DescribeCustomRoutingAccelerator_Example_1"></a>

The following is an example for describing a custom routing accelerator, and the response.

```
aws --region us-west-2 globalaccelerator describe-custom-routing-accelerator 
         --accelerator-arn arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh
```

```
{
    "Accelerator": {
        "AcceleratorArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh", 
        "IpAddressType": "IPV4", 
        "Name": "ExampleAaccelerator", 
        "Enabled": true, 
        "Status": "IN_PROGRESS", 
        "IpSets": [
            {
                "IpAddresses": [
                   "192.0.2.250",
                   "198.51.100.52"
                ], 
                "IpFamily": "IPv4"
            }
        ],
        "DnsName":"a1234567890abcdef.awsglobalaccelerator.com",
        "CreatedTime": 1542394847.0, 
        "LastModifiedTime": 1542395013.0
    }
}
```

## See Also
<a name="API_DescribeCustomRoutingAccelerator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/DescribeCustomRoutingAccelerator) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/DescribeCustomRoutingAccelerator) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/DescribeCustomRoutingAccelerator) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/DescribeCustomRoutingAccelerator) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/DescribeCustomRoutingAccelerator) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/DescribeCustomRoutingAccelerator) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/DescribeCustomRoutingAccelerator) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/DescribeCustomRoutingAccelerator) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/DescribeCustomRoutingAccelerator) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/DescribeCustomRoutingAccelerator) 