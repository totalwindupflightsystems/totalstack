---
id: "@specs/aws/globalaccelerator/docs/API_DeprovisionByoipCidr"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeprovisionByoipCidr"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# DeprovisionByoipCidr

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_DeprovisionByoipCidr
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeprovisionByoipCidr
<a name="API_DeprovisionByoipCidr"></a>

Releases the specified address range that you provisioned to use with your AWS resources through bring your own IP addresses (BYOIP) and deletes the corresponding address pool. 

Before you can release an address range, you must stop advertising it by using [WithdrawByoipCidr](https://docs.aws.amazon.com/global-accelerator/latest/api/WithdrawByoipCidr.html) and you must not have any accelerators that are using static IP addresses allocated from its address range. 

For more information, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html) in the * AWS Global Accelerator Developer Guide*.

## Request Syntax
<a name="API_DeprovisionByoipCidr_RequestSyntax"></a>

```
{
   "Cidr": "{{string}}"
}
```

## Request Parameters
<a name="API_DeprovisionByoipCidr_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Cidr](#API_DeprovisionByoipCidr_RequestSyntax) **   <a name="globalaccelerator-DeprovisionByoipCidr-request-Cidr"></a>
The address range, in CIDR notation. The prefix must be the same prefix that you specified when you provisioned the address range.  
 For more information, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html) in the AWS Global Accelerator Developer Guide.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

## Response Syntax
<a name="API_DeprovisionByoipCidr_ResponseSyntax"></a>

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
<a name="API_DeprovisionByoipCidr_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ByoipCidr](#API_DeprovisionByoipCidr_ResponseSyntax) **   <a name="globalaccelerator-DeprovisionByoipCidr-response-ByoipCidr"></a>
Information about the address range.  
Type: [ByoipCidr](API_ByoipCidr.md) object

## Errors
<a name="API_DeprovisionByoipCidr_Errors"></a>

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
<a name="API_DeprovisionByoipCidr_Examples"></a>

### Deprovision address range
<a name="API_DeprovisionByoipCidr_Example_1"></a>

The following is an example of deprovisioning an address range, and the response.

```
aws globalaccelerator deprovision-byoip-cidr --cidr "198.51.100.0/24"
```

```
{
    "ByoipCidr": {
        "Cidr": "198.51.100.0/24",
        "State": "PENDING_DEPROVISIONING"
    }
}
```

## See Also
<a name="API_DeprovisionByoipCidr_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/DeprovisionByoipCidr) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/DeprovisionByoipCidr) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/DeprovisionByoipCidr) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/DeprovisionByoipCidr) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/DeprovisionByoipCidr) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/DeprovisionByoipCidr) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/DeprovisionByoipCidr) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/DeprovisionByoipCidr) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/DeprovisionByoipCidr) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/DeprovisionByoipCidr) 