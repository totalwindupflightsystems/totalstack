---
id: "@specs/aws/storagegateway/docs/API_ListGateways"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListGateways"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# ListGateways

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_ListGateways
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListGateways
<a name="API_ListGateways"></a>

Lists gateways owned by an AWS account in an AWS Region specified in the request. The returned list is ordered by gateway Amazon Resource Name (ARN).

By default, the operation returns a maximum of 100 gateways. This operation supports pagination that allows you to optionally reduce the number of gateways returned in a response.

If you have more gateways than are returned in a response (that is, the response returns only a truncated list of your gateways), the response contains a marker that you can specify in your next request to fetch the next page of gateways.

## Request Syntax
<a name="API_ListGateways_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "Marker": "{{string}}"
}
```

## Request Parameters
<a name="API_ListGateways_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Limit](#API_ListGateways_RequestSyntax) **   <a name="StorageGateway-ListGateways-request-Limit"></a>
Specifies that the list of gateways returned be limited to the specified number of items.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** [Marker](#API_ListGateways_RequestSyntax) **   <a name="StorageGateway-ListGateways-request-Marker"></a>
An opaque string that indicates the position at which to begin the returned list of gateways.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Required: No

## Response Syntax
<a name="API_ListGateways_ResponseSyntax"></a>

```
{
   "Gateways": [ 
      { 
         "DeprecationDate": "string",
         "Ec2InstanceId": "string",
         "Ec2InstanceRegion": "string",
         "GatewayARN": "string",
         "GatewayId": "string",
         "GatewayName": "string",
         "GatewayOperationalState": "string",
         "GatewayType": "string",
         "HostEnvironment": "string",
         "HostEnvironmentId": "string",
         "SoftwareVersion": "string"
      }
   ],
   "Marker": "string"
}
```

## Response Elements
<a name="API_ListGateways_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Gateways](#API_ListGateways_ResponseSyntax) **   <a name="StorageGateway-ListGateways-response-Gateways"></a>
An array of [GatewayInfo](API_GatewayInfo.md) objects.  
Type: Array of [GatewayInfo](API_GatewayInfo.md) objects

 ** [Marker](#API_ListGateways_ResponseSyntax) **   <a name="StorageGateway-ListGateways-response-Marker"></a>
Use the marker in your next request to fetch the next set of gateways in the list. If there are no more gateways to list, this field does not appear in the response.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors
<a name="API_ListGateways_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
An internal server error has occurred during the request. For more information, see the error and message fields.    
 ** error **   
A [StorageGatewayError](API_StorageGatewayError.md) that provides more information about the cause of the error.  
 ** message **   
A human-readable message describing the error that occurred.
HTTP Status Code: 400

 ** InvalidGatewayRequestException **   
An exception occurred because an invalid gateway request was issued to the service. For more information, see the error and message fields.    
 ** error **   
A [StorageGatewayError](API_StorageGatewayError.md) that provides more detail about the cause of the error.  
 ** message **   
A human-readable message describing the error that occurred.
HTTP Status Code: 400

## Examples
<a name="API_ListGateways_Examples"></a>

### List of gateways owned by an in a specified
<a name="API_ListGateways_Example_1"></a>

The following example does not specify any criteria for the returned list. Note that the request body is "{}". The response returns gateways (or up to the first 100) in the specified AWS Region owned by the AWS account.

#### Sample Request
<a name="API_ListGateways_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.ListGateways
```

#### Sample Response
<a name="API_ListGateways_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 178

{
    "GatewayList": [
        {
            "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-23A4567C"
        }
    ]
}
```

## See Also
<a name="API_ListGateways_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/ListGateways) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/ListGateways) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/ListGateways) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/ListGateways) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/ListGateways) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/ListGateways) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/ListGateways) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/ListGateways) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/ListGateways) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/ListGateways) 