---
id: "@specs/aws/globalaccelerator/docs/API_CreateAccelerator"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAccelerator"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# CreateAccelerator

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_CreateAccelerator
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAccelerator
<a name="API_CreateAccelerator"></a>

Create an accelerator. An accelerator includes one or more listeners that process inbound connections and direct traffic to one or more endpoint groups, each of which includes endpoints, such as Network Load Balancers. 

**Important**  
Global Accelerator is a global service that supports endpoints in multiple AWS Regions but you must specify the US West (Oregon) Region to create, update, or otherwise work with accelerators. That is, for example, specify `--region us-west-2` on AWS CLI commands.

## Request Syntax
<a name="API_CreateAccelerator_RequestSyntax"></a>

```
{
   "Enabled": {{boolean}},
   "IdempotencyToken": "{{string}}",
   "IpAddresses": [ "{{string}}" ],
   "IpAddressType": "{{string}}",
   "Name": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateAccelerator_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Enabled](#API_CreateAccelerator_RequestSyntax) **   <a name="globalaccelerator-CreateAccelerator-request-Enabled"></a>
Indicates whether an accelerator is enabled. The value is true or false. The default value is true.   
If the value is set to true, an accelerator cannot be deleted. If set to false, the accelerator can be deleted.  
Type: Boolean  
Required: No

 ** [IdempotencyToken](#API_CreateAccelerator_RequestSyntax) **   <a name="globalaccelerator-CreateAccelerator-request-IdempotencyToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of an accelerator.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [IpAddresses](#API_CreateAccelerator_RequestSyntax) **   <a name="globalaccelerator-CreateAccelerator-request-IpAddresses"></a>
Optionally, if you've added your own IP address pool to Global Accelerator (BYOIP), you can choose an IPv4 address from your own pool to use for the accelerator's static IPv4 address when you create an accelerator.   
After you bring an address range to AWS, it appears in your account as an address pool. When you create an accelerator, you can assign one IPv4 address from your range to it. Global Accelerator assigns you a second static IPv4 address from an Amazon IP address range. If you bring two IPv4 address ranges to AWS, you can assign one IPv4 address from each range to your accelerator. This restriction is because Global Accelerator assigns each address range to a different network zone, for high availability.  
You can specify one or two addresses, separated by a space. Do not include the /32 suffix.  
Note that you can't update IP addresses for an existing accelerator. To change them, you must create a new accelerator with the new addresses.  
For more information, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html) in the * AWS Global Accelerator Developer Guide*.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 2 items.  
Length Constraints: Maximum length of 45.  
Required: No

 ** [IpAddressType](#API_CreateAccelerator_RequestSyntax) **   <a name="globalaccelerator-CreateAccelerator-request-IpAddressType"></a>
The IP address type that an accelerator supports. For a standard accelerator, the value can be IPV4 or DUAL\_STACK.  
Type: String  
Valid Values: `IPV4 | DUAL_STACK`   
Required: No

 ** [Name](#API_CreateAccelerator_RequestSyntax) **   <a name="globalaccelerator-CreateAccelerator-request-Name"></a>
The name of the accelerator. The name can have a maximum of 64 characters, must contain only alphanumeric characters, periods (.), or hyphens (-), and must not begin or end with a hyphen or period.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [Tags](#API_CreateAccelerator_RequestSyntax) **   <a name="globalaccelerator-CreateAccelerator-request-Tags"></a>
Create tags for an accelerator.  
For more information, see [Tagging in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html) in the * AWS Global Accelerator Developer Guide*.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Syntax
<a name="API_CreateAccelerator_ResponseSyntax"></a>

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
<a name="API_CreateAccelerator_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Accelerator](#API_CreateAccelerator_ResponseSyntax) **   <a name="globalaccelerator-CreateAccelerator-response-Accelerator"></a>
The accelerator that is created by specifying a listener and the supported IP address types.  
Type: [Accelerator](API_Accelerator.md) object

## Errors
<a name="API_CreateAccelerator_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access permission.  
HTTP Status Code: 400

 ** InternalServiceErrorException **   
There was an internal error for AWS Global Accelerator.  
HTTP Status Code: 400

 ** InvalidArgumentException **   
An argument that you specified is invalid.  
HTTP Status Code: 400

 ** LimitExceededException **   
Processing your request would cause you to exceed an AWS Global Accelerator limit.  
HTTP Status Code: 400

 ** TransactionInProgressException **   
There's already a transaction in progress. Another transaction can't be processed.  
HTTP Status Code: 400

## Examples
<a name="API_CreateAccelerator_Examples"></a>

### Create an accelerator
<a name="API_CreateAccelerator_Example_1"></a>

The following is an example of creating an accelerator with two tags, and the response (which does not include the tag information).

```
aws globalaccelerator create-accelerator 
        --name ExampleAccelerator
        --tags Key="Name",Value="Example Name" Key="Project",Value="Example Project"
        --region us-west-2
        --ip-addresses 192.0.2.250 198.51.100.52
```

```
{
    "Accelerator": {
        "AcceleratorArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh", 
        "IpAddressType": "IPV4", 
        "Name": "ExampleAccelerator", 
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
        "LastModifiedTime": 1542394847.0
    }
}
```

## See Also
<a name="API_CreateAccelerator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/CreateAccelerator) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/CreateAccelerator) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/CreateAccelerator) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/CreateAccelerator) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/CreateAccelerator) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/CreateAccelerator) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/CreateAccelerator) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/CreateAccelerator) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/CreateAccelerator) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/CreateAccelerator) 