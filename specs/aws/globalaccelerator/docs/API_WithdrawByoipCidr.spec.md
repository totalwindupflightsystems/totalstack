---
id: "@specs/aws/globalaccelerator/docs/API_WithdrawByoipCidr"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS WithdrawByoipCidr"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# WithdrawByoipCidr

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_WithdrawByoipCidr
> **target_lang:** meta — documentation tier. ALL sections preserved.



# WithdrawByoipCidr
<a name="API_WithdrawByoipCidr"></a>

Stops advertising an address range that is provisioned as an address pool. You can perform this operation at most once every 10 seconds, even if you specify different address ranges each time.

It can take a few minutes before traffic to the specified addresses stops routing to AWS because of propagation delays.

For more information, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html) in the * AWS Global Accelerator Developer Guide*.

## Request Syntax
<a name="API_WithdrawByoipCidr_RequestSyntax"></a>

```
{
   "Cidr": "{{string}}"
}
```

## Request Parameters
<a name="API_WithdrawByoipCidr_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Cidr](#API_WithdrawByoipCidr_RequestSyntax) **   <a name="globalaccelerator-WithdrawByoipCidr-request-Cidr"></a>
The address range, in CIDR notation.  
 For more information, see [Bring your own IP addresses (BYOIP)](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html) in the AWS Global Accelerator Developer Guide.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

## Response Syntax
<a name="API_WithdrawByoipCidr_ResponseSyntax"></a>

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
<a name="API_WithdrawByoipCidr_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ByoipCidr](#API_WithdrawByoipCidr_ResponseSyntax) **   <a name="globalaccelerator-WithdrawByoipCidr-response-ByoipCidr"></a>
Information about the BYOIP address pool.  
Type: [ByoipCidr](API_ByoipCidr.md) object

## Errors
<a name="API_WithdrawByoipCidr_Errors"></a>

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
<a name="API_WithdrawByoipCidr_Examples"></a>

### Withdrawing an address range from advertising by
<a name="API_WithdrawByoipCidr_Example_1"></a>

The following is an example of withdrawing an address range from advertising by AWS and the response.

```
aws globalaccelerator withdraw-byoip-cidr 
    --cidr 203.0.113.25/24
```

```
{
    "ByoipCidr": {
        "Cidr": "203.0.113.25/24",
        "State": "PENDING_WITHDRAWING"
    }
}
```

## See Also
<a name="API_WithdrawByoipCidr_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/WithdrawByoipCidr) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/WithdrawByoipCidr) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/WithdrawByoipCidr) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/WithdrawByoipCidr) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/WithdrawByoipCidr) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/WithdrawByoipCidr) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/WithdrawByoipCidr) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/WithdrawByoipCidr) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/WithdrawByoipCidr) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/WithdrawByoipCidr) 