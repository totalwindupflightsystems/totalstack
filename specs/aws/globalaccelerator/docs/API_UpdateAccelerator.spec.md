---
id: "@specs/aws/globalaccelerator/docs/API_UpdateAccelerator"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateAccelerator"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# UpdateAccelerator

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_UpdateAccelerator
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateAccelerator
<a name="API_UpdateAccelerator"></a>

Update an accelerator to make changes, such as the following: 
+ Change the name of the accelerator.
+ Disable the accelerator so that it no longer accepts or routes traffic, or so that you can delete it.
+ Enable the accelerator, if it is disabled.
+ Change the IP address type to dual-stack if it is IPv4, or change the IP address type to IPv4 if it's dual-stack.

Be aware that static IP addresses remain assigned to your accelerator for as long as it exists, even if you disable the accelerator and it no longer accepts or routes traffic. However, when you delete the accelerator, you lose the static IP addresses that are assigned to it, so you can no longer route traffic by using them.

**Important**  
Global Accelerator is a global service that supports endpoints in multiple AWS Regions but you must specify the US West (Oregon) Region to create, update, or otherwise work with accelerators. That is, for example, specify `--region us-west-2` on AWS CLI commands.

## Request Syntax
<a name="API_UpdateAccelerator_RequestSyntax"></a>

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
<a name="API_UpdateAccelerator_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AcceleratorArn](#API_UpdateAccelerator_RequestSyntax) **   <a name="globalaccelerator-UpdateAccelerator-request-AcceleratorArn"></a>
The Amazon Resource Name (ARN) of the accelerator to update.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [Enabled](#API_UpdateAccelerator_RequestSyntax) **   <a name="globalaccelerator-UpdateAccelerator-request-Enabled"></a>
Indicates whether an accelerator is enabled. The value is true or false. The default value is true.   
If the value is set to true, the accelerator cannot be deleted. If set to false, the accelerator can be deleted.  
Type: Boolean  
Required: No

 ** [IpAddresses](#API_UpdateAccelerator_RequestSyntax) **   <a name="globalaccelerator-UpdateAccelerator-request-IpAddresses"></a>
The IP addresses for an accelerator.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 2 items.  
Length Constraints: Maximum length of 45.  
Required: No

 ** [IpAddressType](#API_UpdateAccelerator_RequestSyntax) **   <a name="globalaccelerator-UpdateAccelerator-request-IpAddressType"></a>
The IP address type that an accelerator supports. For a standard accelerator, the value can be IPV4 or DUAL\_STACK.  
Type: String  
Valid Values: `IPV4 | DUAL_STACK`   
Required: No

 ** [Name](#API_UpdateAccelerator_RequestSyntax) **   <a name="globalaccelerator-UpdateAccelerator-request-Name"></a>
The name of the accelerator. The name can have a maximum of 64 characters, must contain only alphanumeric characters, periods (.), or hyphens (-), and must not begin or end with a hyphen or period.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

## Response Syntax
<a name="API_UpdateAccelerator_ResponseSyntax"></a>

```
{
   "Accelerator": { 
      "AcceleratorArn": "string",
      "CreatedTime": number,
      "DnsName": "string",
      "DualStackDnsName": "string",
      "Enabled": boolean,
      "Events": [ 
         { 
            "Message": "string",
            "Timestamp": number
         }
      ],
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
<a name="API_UpdateAccelerator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Accelerator](#API_UpdateAccelerator_ResponseSyntax) **   <a name="globalaccelerator-UpdateAccelerator-response-Accelerator"></a>
Information about the updated accelerator.  
Type: [Accelerator](API_Accelerator.md) object

## Errors
<a name="API_UpdateAccelerator_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AcceleratorNotFoundException **   
The accelerator that you specified doesn't exist.  
HTTP Status Code: 400

 ** AccessDeniedException **   
You don't have access permission.  
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
<a name="API_UpdateAccelerator_Examples"></a>

### Update an accelerator
<a name="API_UpdateAccelerator_Example_1"></a>

The following is an example for updating an accelerator to change the name.

```
aws globalaccelerator update-accelerator 
       --accelerator-arn arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh 
       --name ExampleAcceleratorNew
       --region us-west-2
```

```
{  
   "Accelerator":{  
      "AcceleratorArn":"arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh",
      "IpAddressType":"IPV4",
      "Name":"ExampleAcceleratorNew",
      "Enabled":true,
      "Status":"IN_PROGRESS",
      "IpSets":[  
         {  
            "IpAddresses":[  
                "192.0.2.250",
                "198.51.100.52"
            ],
            "IpFamily":"IPv4"
         }
      ],
      "DnsName":"a1234567890abcdef.awsglobalaccelerator.com",
      "CreatedTime":1232394847.0,
      "LastModifiedTime":1232395654.0
   }
}
```

## See Also
<a name="API_UpdateAccelerator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/UpdateAccelerator) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/UpdateAccelerator) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/UpdateAccelerator) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/UpdateAccelerator) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/UpdateAccelerator) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/UpdateAccelerator) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/UpdateAccelerator) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/UpdateAccelerator) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/UpdateAccelerator) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/UpdateAccelerator) 