---
id: "@specs/aws/globalaccelerator/docs/API_ListEndpointGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListEndpointGroups"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# ListEndpointGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_ListEndpointGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListEndpointGroups
<a name="API_ListEndpointGroups"></a>

List the endpoint groups that are associated with a listener. 

## Request Syntax
<a name="API_ListEndpointGroups_RequestSyntax"></a>

```
{
   "ListenerArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListEndpointGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ListenerArn](#API_ListEndpointGroups_RequestSyntax) **   <a name="globalaccelerator-ListEndpointGroups-request-ListenerArn"></a>
The Amazon Resource Name (ARN) of the listener.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: Yes

 ** [MaxResults](#API_ListEndpointGroups_RequestSyntax) **   <a name="globalaccelerator-ListEndpointGroups-request-MaxResults"></a>
The number of endpoint group objects that you want to return with this call. The default value is 10.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListEndpointGroups_RequestSyntax) **   <a name="globalaccelerator-ListEndpointGroups-request-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.  
Type: String  
Length Constraints: Maximum length of 255.  
Required: No

## Response Syntax
<a name="API_ListEndpointGroups_ResponseSyntax"></a>

```
{
   "EndpointGroups": [ 
      { 
         "EndpointDescriptions": [ 
            { 
               "ClientIPPreservationEnabled": boolean,
               "EndpointId": "string",
               "HealthReason": "string",
               "HealthState": "string",
               "Weight": number
            }
         ],
         "EndpointGroupArn": "string",
         "EndpointGroupRegion": "string",
         "HealthCheckIntervalSeconds": number,
         "HealthCheckPath": "string",
         "HealthCheckPort": number,
         "HealthCheckProtocol": "string",
         "PortOverrides": [ 
            { 
               "EndpointPort": number,
               "ListenerPort": number
            }
         ],
         "ThresholdCount": number,
         "TrafficDialPercentage": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEndpointGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EndpointGroups](#API_ListEndpointGroups_ResponseSyntax) **   <a name="globalaccelerator-ListEndpointGroups-response-EndpointGroups"></a>
The list of the endpoint groups associated with a listener.  
Type: Array of [EndpointGroup](API_EndpointGroup.md) objects

 ** [NextToken](#API_ListEndpointGroups_ResponseSyntax) **   <a name="globalaccelerator-ListEndpointGroups-response-NextToken"></a>
The token for the next set of results. You receive this token from a previous call.  
Type: String  
Length Constraints: Maximum length of 255.

## Errors
<a name="API_ListEndpointGroups_Errors"></a>

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
<a name="API_ListEndpointGroups_Examples"></a>

### List endpoint groups
<a name="API_ListEndpointGroups_Example_1"></a>

The following is an example for listing the endpoint groups for listener, and the response.

```
aws globalaccelerator list-endpoint-groups 
         --listener-arn arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/abcdef1234
         --region us-west-2
```

```
{
    "EndpointGroups": [
        {
            "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/abcdef1234/endpoint-group/ab88888example",
            "EndpointGroupRegion": "eu-central-1",
            "EndpointDescriptions": [],
            "TrafficDialPercentage": 100.0,
            "HealthCheckPort": 80,
            "HealthCheckProtocol": "TCP",
            "HealthCheckIntervalSeconds": 30,
            "ThresholdCount": 3
        }
        {
            "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/abcdef1234/endpoint-group/ab99999example",
            "EndpointGroupRegion": "us-east-1",
            "EndpointDescriptions": [],
            "TrafficDialPercentage": 50.0,
            "HealthCheckPort": 80,
            "HealthCheckProtocol": "TCP",
            "HealthCheckIntervalSeconds": 30,
            "ThresholdCount": 3
        }
    ]
}
```

## See Also
<a name="API_ListEndpointGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/ListEndpointGroups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/ListEndpointGroups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/ListEndpointGroups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/ListEndpointGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/ListEndpointGroups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/ListEndpointGroups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/ListEndpointGroups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/ListEndpointGroups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/ListEndpointGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/ListEndpointGroups) 