---
id: "@specs/aws/globalaccelerator/docs/API_ListCustomRoutingEndpointGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListCustomRoutingEndpointGroups"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# ListCustomRoutingEndpointGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_ListCustomRoutingEndpointGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListCustomRoutingEndpointGroups
<a name="API_ListCustomRoutingEndpointGroups"></a>

List the endpoint groups that are associated with a listener for a custom routing accelerator. 

## Request Syntax
<a name="API_ListCustomRoutingEndpointGroups_RequestSyntax"></a>

```
{
   "ListenerArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListCustomRoutingEndpointGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ListenerArn](#API_ListCustomRoutingEndpointGroups_RequestSyntax) **   <a name="globalaccelerator-ListCustomRoutingEndpointGroups-request-ListenerArn"></a>
The Amazon Resource Name (ARN) of the listener to list endpoint groups for.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [MaxResults](#API_ListCustomRoutingEndpointGroups_RequestSyntax) **   <a name="globalaccelerator-ListCustomRoutingEndpointGroups-request-MaxResults"></a>
The number of endpoint group objects that you want to return with this call. The default value is 10.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListCustomRoutingEndpointGroups_RequestSyntax) **   <a name="globalaccelerator-ListCustomRoutingEndpointGroups-request-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

## Response Syntax
<a name="API_ListCustomRoutingEndpointGroups_ResponseSyntax"></a>

```
{
   "EndpointGroups": [ 
      { 
         "DestinationDescriptions": [ 
            { 
               "FromPort": number,
               "Protocols": [ "string" ],
               "ToPort": number
            }
         ],
         "EndpointDescriptions": [ 
            { 
               "EndpointId": "string"
            }
         ],
         "EndpointGroupArn": "string",
         "EndpointGroupRegion": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListCustomRoutingEndpointGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndpointGroups](#API_ListCustomRoutingEndpointGroups_ResponseSyntax) **   <a name="globalaccelerator-ListCustomRoutingEndpointGroups-response-EndpointGroups"></a>
The list of the endpoint groups associated with a listener for a custom routing accelerator.  
Type: Array of [CustomRoutingEndpointGroup](API_CustomRoutingEndpointGroup.md) objects

 ** [NextToken](#API_ListCustomRoutingEndpointGroups_ResponseSyntax) **   <a name="globalaccelerator-ListCustomRoutingEndpointGroups-response-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.  
Type: String  
Length Constraints: Maximum length of 255.

## Errors
<a name="API_ListCustomRoutingEndpointGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceErrorException **   
There was an internal error for AWS Global Accelerator.  
HTTP Status Code: 400

 ** InvalidArgumentException **   
An argument that you specified is invalid.  
HTTP Status Code: 400

 ** InvalidNextTokenException **   
There isn't another item to return.  
HTTP Status Code: 400

 ** ListenerNotFoundException **   
The listener that you specified doesn't exist.  
HTTP Status Code: 400

## Examples
<a name="API_ListCustomRoutingEndpointGroups_Examples"></a>

### List endpoint groups for a custom routing accelerator
<a name="API_ListCustomRoutingEndpointGroups_Example_1"></a>

The following is an example for listing the endpoint groups associated with a listener for a custom routing accelerator, and the response.

```
aws globalaccelerator list-custom-routing-endpoint-groups 
         --listener-arn arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/abcdef1234
         --region us-west-2
```

```
{
    "EndpointGroups": [
        {
            "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/abcdef1234/endpoint-group/ab88888example",
            "EndpointGroupRegion": "eu-central-1",
            "EndpointDescriptions": []
        }
        {
            "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/abcdef1234/endpoint-group/ab99999example",
            "EndpointGroupRegion": "us-east-1",
            "EndpointDescriptions": []
        }
    ]
}
```

## See Also
<a name="API_ListCustomRoutingEndpointGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/ListCustomRoutingEndpointGroups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/ListCustomRoutingEndpointGroups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/ListCustomRoutingEndpointGroups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/ListCustomRoutingEndpointGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/ListCustomRoutingEndpointGroups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/ListCustomRoutingEndpointGroups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/ListCustomRoutingEndpointGroups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/ListCustomRoutingEndpointGroups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/ListCustomRoutingEndpointGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/ListCustomRoutingEndpointGroups) 