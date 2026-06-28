---
id: "@specs/aws/globalaccelerator/docs/API_ListCustomRoutingListeners"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListCustomRoutingListeners"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# ListCustomRoutingListeners

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_ListCustomRoutingListeners
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListCustomRoutingListeners
<a name="API_ListCustomRoutingListeners"></a>

List the listeners for a custom routing accelerator. 

## Request Syntax
<a name="API_ListCustomRoutingListeners_RequestSyntax"></a>

```
{
   "AcceleratorArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCustomRoutingListeners_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AcceleratorArn](#API_ListCustomRoutingListeners_RequestSyntax) **   <a name="globalaccelerator-ListCustomRoutingListeners-request-AcceleratorArn"></a>
The Amazon Resource Name (ARN) of the accelerator to list listeners for.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [MaxResults](#API_ListCustomRoutingListeners_RequestSyntax) **   <a name="globalaccelerator-ListCustomRoutingListeners-request-MaxResults"></a>
The number of listener objects that you want to return with this call. The default value is 10.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListCustomRoutingListeners_RequestSyntax) **   <a name="globalaccelerator-ListCustomRoutingListeners-request-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

## Response Syntax
<a name="API_ListCustomRoutingListeners_ResponseSyntax"></a>

```
{
   "Listeners": [ 
      { 
         "ListenerArn": "string",
         "PortRanges": [ 
            { 
               "FromPort": number,
               "ToPort": number
            }
         ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCustomRoutingListeners_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Listeners](#API_ListCustomRoutingListeners_ResponseSyntax) **   <a name="globalaccelerator-ListCustomRoutingListeners-response-Listeners"></a>
The list of listeners for a custom routing accelerator.  
Type: Array of [CustomRoutingListener](API_CustomRoutingListener.md) objects

 ** [NextToken](#API_ListCustomRoutingListeners_ResponseSyntax) **   <a name="globalaccelerator-ListCustomRoutingListeners-response-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.  
Type: String  
Length Constraints: Maximum length of 255.

## Errors
<a name="API_ListCustomRoutingListeners_Errors"></a>

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

 ** InvalidNextTokenException **   
There isn't another item to return.  
HTTP Status Code: 400

## Examples
<a name="API_ListCustomRoutingListeners_Examples"></a>

### List listeners for a custom routing accelerator
<a name="API_ListCustomRoutingListeners_Example_1"></a>

The following is an example for listing the listeners for a custom routing accelerator, and the response.

```
aws globalaccelerator list-custom-routing-listeners 
         --accelerator-arn arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh
         --region us-west-2
```

```
{
    "Listeners": [
        {
            "ListenerArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/abcdef1234",
            "PortRanges": [
                {
                    "FromPort": 5000,
                    "ToPort": 10000
                }
            ],
            "Protocol": "TCP",
        }
    ]
}
```

## See Also
<a name="API_ListCustomRoutingListeners_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/ListCustomRoutingListeners) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/ListCustomRoutingListeners) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/ListCustomRoutingListeners) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/ListCustomRoutingListeners) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/ListCustomRoutingListeners) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/ListCustomRoutingListeners) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/ListCustomRoutingListeners) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/ListCustomRoutingListeners) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/ListCustomRoutingListeners) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/ListCustomRoutingListeners) 