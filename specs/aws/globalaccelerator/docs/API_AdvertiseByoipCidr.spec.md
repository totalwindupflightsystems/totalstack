---
id: "@specs/aws/globalaccelerator/docs/API_AdvertiseByoipCidr"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AdvertiseByoipCidr"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# AdvertiseByoipCidr

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_AdvertiseByoipCidr
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AdvertiseByoipCidr
<a name="API_AdvertiseByoipCidr"></a>

Advertises an IPv4 address range that is provisioned for use with your AWS resources through bring your own IP addresses (BYOIP). It can take a few minutes before traffic to the specified addresses starts routing to AWS because of propagation delays. 

To stop advertising the BYOIP address range, use [ WithdrawByoipCidr](https://docs.aws.amazon.com/global-accelerator/latest/api/WithdrawByoipCidr.html).

For more information, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html) in the * AWS Global Accelerator Developer Guide*.

## Request Syntax
<a name="API_AdvertiseByoipCidr_RequestSyntax"></a>

```
{
   "Cidr": "{{string}}"
}
```

## Request Parameters
<a name="API_AdvertiseByoipCidr_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Cidr](#API_AdvertiseByoipCidr_RequestSyntax) **   <a name="globalaccelerator-AdvertiseByoipCidr-request-Cidr"></a>
The address range, in CIDR notation. This must be the exact range that you provisioned. You can't advertise only a portion of the provisioned range.  
 For more information, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html) in the AWS Global Accelerator Developer Guide.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

## Response Syntax
<a name="API_AdvertiseByoipCidr_ResponseSyntax"></a>

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
<a name="API_AdvertiseByoipCidr_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ByoipCidr](#API_AdvertiseByoipCidr_ResponseSyntax) **   <a name="globalaccelerator-AdvertiseByoipCidr-response-ByoipCidr"></a>
Information about the address range.  
Type: [ByoipCidr](API_ByoipCidr.md) object

## Errors
<a name="API_AdvertiseByoipCidr_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access permission.  
HTTP Status Code: 400

 ** ByoipCidrNotFoundException **   
The CIDR that you specified was not found or is incorrect.  
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

## Examples
<a name="API_AdvertiseByoipCidr_Examples"></a>

### Advertise address range
<a name="API_AdvertiseByoipCidr_Example_1"></a>

The following is an example of advertising an address range, and the response.

```
aws globalaccelerator advertise-byoip-cidr --cidr "198.51.100.0/24"
```

```
{
    "ByoipCidr": {
        "Cidr": "198.51.100.0/24",
        "State": "PENDING_ADVERTISING"
    }
}
```

## See Also
<a name="API_AdvertiseByoipCidr_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/AdvertiseByoipCidr) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/AdvertiseByoipCidr) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/AdvertiseByoipCidr) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/AdvertiseByoipCidr) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/AdvertiseByoipCidr) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/AdvertiseByoipCidr) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/AdvertiseByoipCidr) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/AdvertiseByoipCidr) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/AdvertiseByoipCidr) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/AdvertiseByoipCidr) 