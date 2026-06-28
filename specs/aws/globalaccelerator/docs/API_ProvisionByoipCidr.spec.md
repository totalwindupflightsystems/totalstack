---
id: "@specs/aws/globalaccelerator/docs/API_ProvisionByoipCidr"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ProvisionByoipCidr"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# ProvisionByoipCidr

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_ProvisionByoipCidr
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ProvisionByoipCidr
<a name="API_ProvisionByoipCidr"></a>

Provisions an IP address range to use with your AWS resources through bring your own IP addresses (BYOIP) and creates a corresponding address pool. After the address range is provisioned, it is ready to be advertised using [ AdvertiseByoipCidr](https://docs.aws.amazon.com/global-accelerator/latest/api/AdvertiseByoipCidr.html).

For more information, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html) in the * AWS Global Accelerator Developer Guide*.

## Request Syntax
<a name="API_ProvisionByoipCidr_RequestSyntax"></a>

```
{
   "Cidr": "{{string}}",
   "CidrAuthorizationContext": { 
      "Message": "{{string}}",
      "Signature": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_ProvisionByoipCidr_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Cidr](#API_ProvisionByoipCidr_RequestSyntax) **   <a name="globalaccelerator-ProvisionByoipCidr-request-Cidr"></a>
The public IPv4 address range, in CIDR notation. The most specific IP prefix that you can specify is /24. The address range cannot overlap with another address range that you've brought to this AWS Region or another Region.  
 For more information, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html) in the AWS Global Accelerator Developer Guide.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [CidrAuthorizationContext](#API_ProvisionByoipCidr_RequestSyntax) **   <a name="globalaccelerator-ProvisionByoipCidr-request-CidrAuthorizationContext"></a>
A signed document that proves that you are authorized to bring the specified IP address range to Amazon using BYOIP.   
Type: [CidrAuthorizationContext](API_CidrAuthorizationContext.md) object  
Required: Yes

## Response Syntax
<a name="API_ProvisionByoipCidr_ResponseSyntax"></a>

```
{
   "ByoipCidr": { 
      "Cidr": "string",
      "Events": [ 
         { 
            "Message": "string",
            "Timestamp": number
         }
      ],
      "State": "string"
   }
}
```

## Response Elements
<a name="API_ProvisionByoipCidr_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ByoipCidr](#API_ProvisionByoipCidr_ResponseSyntax) **   <a name="globalaccelerator-ProvisionByoipCidr-response-ByoipCidr"></a>
Information about the address range.  
Type: [ByoipCidr](API_ByoipCidr.md) object

## Errors
<a name="API_ProvisionByoipCidr_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access permission.  
HTTP Status Code: 400

 ** IncorrectCidrStateException **   
The CIDR that you specified is not valid for this action. For example, the state of the CIDR might be incorrect for this action.  
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

## Examples
<a name="API_ProvisionByoipCidr_Examples"></a>

### Provisioning an address range for BYOIP
<a name="API_ProvisionByoipCidr_Example_1"></a>

The following is an example of provisioning an address range for BYOIP and the response.

For more information about creating the values for `text_message` and `signature`, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html) in the * AWS Global Accelerator Developer Guide*.

```
aws globalaccelerator provision-byoip-cidr 
    --cidr 203.0.113.25/24
    --cidr-authorization-context Message="$text_message",Signature="$signed_message"
```

```
{
    "ByoipCidr": {
        "Cidr": "203.0.113.25/24",
        "State": "PENDING_PROVISIONING"
    }
}
```

## See Also
<a name="API_ProvisionByoipCidr_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/ProvisionByoipCidr) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/ProvisionByoipCidr) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/ProvisionByoipCidr) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/ProvisionByoipCidr) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/ProvisionByoipCidr) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/ProvisionByoipCidr) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/ProvisionByoipCidr) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/ProvisionByoipCidr) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/ProvisionByoipCidr) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/ProvisionByoipCidr) 