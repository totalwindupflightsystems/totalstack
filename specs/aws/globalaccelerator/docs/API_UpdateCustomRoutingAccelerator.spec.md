---
id: "@specs/aws/globalaccelerator/docs/API_UpdateCustomRoutingAccelerator"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateCustomRoutingAccelerator"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# UpdateCustomRoutingAccelerator

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_UpdateCustomRoutingAccelerator
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateCustomRoutingAccelerator
<a name="API_UpdateCustomRoutingAccelerator"></a>

Update a custom routing accelerator. 

## Request Syntax
<a name="API_UpdateCustomRoutingAccelerator_RequestSyntax"></a>

```
{
   "AcceleratorArn": "{{string}}",
   "Enabled": {{boolean}},
   "IpAddresses": [ "{{string}}" ],
   "IpAddressType": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateCustomRoutingAccelerator_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AcceleratorArn](#API_UpdateCustomRoutingAccelerator_RequestSyntax) **   <a name="globalaccelerator-UpdateCustomRoutingAccelerator-request-AcceleratorArn"></a>
The Amazon Resource Name (ARN) of the accelerator to update.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [Enabled](#API_UpdateCustomRoutingAccelerator_RequestSyntax) **   <a name="globalaccelerator-UpdateCustomRoutingAccelerator-request-Enabled"></a>
Indicates whether an accelerator is enabled. The value is true or false. The default value is true.   
If the value is set to true, the accelerator cannot be deleted. If set to false, the accelerator can be deleted.  
Type: Boolean  
Required: No

 ** [IpAddresses](#API_UpdateCustomRoutingAccelerator_RequestSyntax) **   <a name="globalaccelerator-UpdateCustomRoutingAccelerator-request-IpAddresses"></a>
The IP addresses for an accelerator.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 2 items.  
Length Constraints: Maximum length of 45.  
Required: No

 ** [IpAddressType](#API_UpdateCustomRoutingAccelerator_RequestSyntax) **   <a name="globalaccelerator-UpdateCustomRoutingAccelerator-request-IpAddressType"></a>
The IP address type that an accelerator supports. For a custom routing accelerator, the value must be IPV4.  
Type: String  
Valid Values: `IPV4 | DUAL_STACK`   
Required: No

 ** [Name](#API_UpdateCustomRoutingAccelerator_RequestSyntax) **   <a name="globalaccelerator-UpdateCustomRoutingAccelerator-request-Name"></a>
The name of the accelerator. The name can have a maximum of 64 characters, must contain only alphanumeric characters, periods (.), or hyphens (-), and must not begin or end with a hyphen or period.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

## Response Syntax
<a name="API_UpdateCustomRoutingAccelerator_ResponseSyntax"></a>

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
<a name="API_UpdateCustomRoutingAccelerator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Accelerator](#API_UpdateCustomRoutingAccelerator_ResponseSyntax) **   <a name="globalaccelerator-UpdateCustomRoutingAccelerator-response-Accelerator"></a>
Information about the updated custom routing accelerator.  
Type: [CustomRoutingAccelerator](API_CustomRoutingAccelerator.md) object

## Errors
<a name="API_UpdateCustomRoutingAccelerator_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AcceleratorNotFoundException **   
The accelerator that you specified doesn't exist.  
HTTP Status Code: 400

 ** ConflictException **   
You can't use both of those options.  
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
<a name="API_UpdateCustomRoutingAccelerator_Examples"></a>

### Update a custom routing accelerator
<a name="API_UpdateCustomRoutingAccelerator_Example_1"></a>

The following is an example for updating a custom routing accelerator.

```
aws --region us-west-2 globalaccelerator update-custom-routing-accelerator 
       --accelerator-arn arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh 
       --enabled
```

```
{
    "Accelerator": {
        "AcceleratorArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh",
        "Name": "testaccelerator",
        "IpAddressType": "IPV4",
        "Enabled": true,
        "IpSets": [
            {
                "IpAddresses": [
                   "192.0.2.250",
                   "198.51.100.52"
                ], 
                "IpFamily": "IPv4"
            }
        ]
        "DnsName": "a1234567890abcdef.awsglobalaccelerator.com",
        "Status": "IN_PROGRESS",
        "CreatedTime": 1605833295.0,
        "LastModifiedTime": 1605910135.0
    }
}
```

## See Also
<a name="API_UpdateCustomRoutingAccelerator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/UpdateCustomRoutingAccelerator) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/UpdateCustomRoutingAccelerator) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/UpdateCustomRoutingAccelerator) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/UpdateCustomRoutingAccelerator) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/UpdateCustomRoutingAccelerator) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/UpdateCustomRoutingAccelerator) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/UpdateCustomRoutingAccelerator) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/UpdateCustomRoutingAccelerator) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/UpdateCustomRoutingAccelerator) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/UpdateCustomRoutingAccelerator) 