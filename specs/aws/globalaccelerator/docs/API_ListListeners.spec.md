---
id: "@specs/aws/globalaccelerator/docs/API_ListListeners"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListListeners"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# ListListeners

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_ListListeners
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListListeners
<a name="API_ListListeners"></a>

List the listeners for an accelerator. 

## Request Syntax
<a name="API_ListListeners_RequestSyntax"></a>

```
{
   "AcceleratorArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListListeners_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AcceleratorArn](#API_ListListeners_RequestSyntax) **   <a name="globalaccelerator-ListListeners-request-AcceleratorArn"></a>
The Amazon Resource Name (ARN) of the accelerator for which you want to list listener objects.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [MaxResults](#API_ListListeners_RequestSyntax) **   <a name="globalaccelerator-ListListeners-request-MaxResults"></a>
The number of listener objects that you want to return with this call. The default value is 10.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListListeners_RequestSyntax) **   <a name="globalaccelerator-ListListeners-request-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

## Response Syntax
<a name="API_ListListeners_ResponseSyntax"></a>

```
{
   "Listeners": [ 
      { 
         "ClientAffinity": "string",
         "ListenerArn": "string",
         "PortRanges": [ 
            { 
               "FromPort": number,
               "ToPort": number
            }
         ],
         "Protocol": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListListeners_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Listeners](#API_ListListeners_ResponseSyntax) **   <a name="globalaccelerator-ListListeners-response-Listeners"></a>
The list of listeners for an accelerator.  
Type: Array of [Listener](API_Listener.md) objects

 ** [NextToken](#API_ListListeners_ResponseSyntax) **   <a name="globalaccelerator-ListListeners-response-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.  
Type: String  
Length Constraints: Maximum length of 255.

## Errors
<a name="API_ListListeners_Errors"></a>

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
<a name="API_ListListeners_Examples"></a>

### List listeners
<a name="API_ListListeners_Example_1"></a>

The following is an example for listing the listeners for an accelerator, and the response.

```
aws globalaccelerator list-listeners 
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
                    "FromPort": 80,
                    "ToPort": 80
                }
            ],
            "Protocol": "TCP",
            "ClientAffinity": "NONE"
        }
    ]
}
```

## See Also
<a name="API_ListListeners_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/ListListeners) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/ListListeners) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/ListListeners) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/ListListeners) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/ListListeners) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/ListListeners) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/ListListeners) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/ListListeners) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/ListListeners) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/ListListeners) 