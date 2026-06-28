---
id: "@specs/aws/globalaccelerator/docs/API_ListByoipCidrs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListByoipCidrs"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# ListByoipCidrs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_ListByoipCidrs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListByoipCidrs
<a name="API_ListByoipCidrs"></a>

Lists the IP address ranges that were specified in calls to [ProvisionByoipCidr](https://docs.aws.amazon.com/global-accelerator/latest/api/ProvisionByoipCidr.html), including the current state and a history of state changes.

## Request Syntax
<a name="API_ListByoipCidrs_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListByoipCidrs_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListByoipCidrs_RequestSyntax) **   <a name="globalaccelerator-ListByoipCidrs-request-MaxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListByoipCidrs_RequestSyntax) **   <a name="globalaccelerator-ListByoipCidrs-request-NextToken"></a>
The token for the next page of results.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

## Response Syntax
<a name="API_ListByoipCidrs_ResponseSyntax"></a>

```
{
   "ByoipCidrs": [ 
      { 
         "Cidr": "string",
         "Events": [ 
            { 
               "Message": "string",
               "Timestamp": number
            }
         ],
         "State": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListByoipCidrs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ByoipCidrs](#API_ListByoipCidrs_ResponseSyntax) **   <a name="globalaccelerator-ListByoipCidrs-response-ByoipCidrs"></a>
Information about your address ranges.  
Type: Array of [ByoipCidr](API_ByoipCidr.md) objects

 ** [NextToken](#API_ListByoipCidrs_ResponseSyntax) **   <a name="globalaccelerator-ListByoipCidrs-response-NextToken"></a>
The token for the next page of results.  
Type: String  
Length Constraints: Maximum length of 255.

## Errors
<a name="API_ListByoipCidrs_Errors"></a>

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

 ** InvalidNextTokenException **   
There isn't another item to return.  
HTTP Status Code: 400

## Examples
<a name="API_ListByoipCidrs_Examples"></a>

### List BYOIP CIDR addresses
<a name="API_ListByoipCidrs_Example_1"></a>

The following is an example of listing BYOIP CIDR addresses and the response.

```
aws globalaccelerator list-byoip-cidrs
```

```
{
    "ByoipCidrs": [
        {
            "Cidr": "198.51.100.0/24",
            "State": "DEPROVISIONED",
            "Events": [
                {
                    "Message": "CIDR is deprovisioned",
                    "Timestamp": 1584977476.0
                },
                {
                    "Message": "Initiated CIDR deprovisioning",
                    "Timestamp": 1584977440.0
                },
                {
                    "Message": "CIDR is no longer advertising",
                    "Timestamp": 1584977429.0
                },
                {
                    "Message": "Initiated CIDR withdrawal",
                    "Timestamp": 1584977348.0
                },
                {
                    "Message": "CIDR is advertising",
                    "Timestamp": 1584977334.0
                },
                {
                    "Message": "Initiated CIDR advertisement",
                    "Timestamp": 1584977298.0
                },
                {
                    "Message": "CIDR is provisioned",
                    "Timestamp": 1584977280.0
                },
                {
                    "Message": "Initiated CIDR provisioning",
                    "Timestamp": 1584977239.0
                }
            ]
        }
        {
            "Cidr": "203.0.113.25/24",
            "State": "READY",
            "Events": [
                {
                    "Message": "CIDR is provisioned",
                    "Timestamp": 1584977802.0
                },
                {
                    "Message": "Initiated CIDR provisioning",
                    "Timestamp": 1584977367.0
                }
            ]
        }
    ]
}
```

## See Also
<a name="API_ListByoipCidrs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/ListByoipCidrs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/ListByoipCidrs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/ListByoipCidrs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/ListByoipCidrs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/ListByoipCidrs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/ListByoipCidrs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/ListByoipCidrs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/ListByoipCidrs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/ListByoipCidrs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/ListByoipCidrs) 