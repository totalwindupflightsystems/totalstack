---
id: "@specs/aws/storagegateway/docs/API_DescribeVTLDevices"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeVTLDevices"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DescribeVTLDevices

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DescribeVTLDevices
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeVTLDevices
<a name="API_DescribeVTLDevices"></a>

Returns a description of virtual tape library (VTL) devices for the specified tape gateway. In the response, Storage Gateway returns VTL device information.

This operation is only supported in the tape gateway type.

## Request Syntax
<a name="API_DescribeVTLDevices_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}",
   "Limit": {{number}},
   "Marker": "{{string}}",
   "VTLDeviceARNs": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeVTLDevices_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_DescribeVTLDevices_RequestSyntax) **   <a name="StorageGateway-DescribeVTLDevices-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [Limit](#API_DescribeVTLDevices_RequestSyntax) **   <a name="StorageGateway-DescribeVTLDevices-request-Limit"></a>
Specifies that the number of VTL devices described be limited to the specified number.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** [Marker](#API_DescribeVTLDevices_RequestSyntax) **   <a name="StorageGateway-DescribeVTLDevices-request-Marker"></a>
An opaque string that indicates the position at which to begin describing the VTL devices.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Required: No

 ** [VTLDeviceARNs](#API_DescribeVTLDevices_RequestSyntax) **   <a name="StorageGateway-DescribeVTLDevices-request-VTLDeviceARNs"></a>
An array of strings, where each string represents the Amazon Resource Name (ARN) of a VTL device.  
All of the specified VTL devices must be from the same gateway. If no VTL devices are specified, the result will contain all devices on the specified gateway.
Type: Array of strings  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: No

## Response Syntax
<a name="API_DescribeVTLDevices_ResponseSyntax"></a>

```
{
   "GatewayARN": "string",
   "Marker": "string",
   "VTLDevices": [ 
      { 
         "DeviceiSCSIAttributes": { 
            "ChapEnabled": boolean,
            "NetworkInterfaceId": "string",
            "NetworkInterfacePort": number,
            "TargetARN": "string"
         },
         "VTLDeviceARN": "string",
         "VTLDeviceProductIdentifier": "string",
         "VTLDeviceType": "string",
         "VTLDeviceVendor": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeVTLDevices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayARN](#API_DescribeVTLDevices_ResponseSyntax) **   <a name="StorageGateway-DescribeVTLDevices-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

 ** [Marker](#API_DescribeVTLDevices_ResponseSyntax) **   <a name="StorageGateway-DescribeVTLDevices-response-Marker"></a>
An opaque string that indicates the position at which the VTL devices that were fetched for description ended. Use the marker in your next request to fetch the next set of VTL devices in the list. If there are no more VTL devices to describe, this field does not appear in the response.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [VTLDevices](#API_DescribeVTLDevices_ResponseSyntax) **   <a name="StorageGateway-DescribeVTLDevices-response-VTLDevices"></a>
An array of VTL device objects composed of the Amazon Resource Name (ARN) of the VTL devices.  
Type: Array of [VTLDevice](API_VTLDevice.md) objects

## Errors
<a name="API_DescribeVTLDevices_Errors"></a>

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
<a name="API_DescribeVTLDevices_Examples"></a>

### Get descriptions of the VTL devices on a gateway
<a name="API_DescribeVTLDevices_Example_1"></a>

The following example gets descriptions of all the VTL devices on a gateway with ID sgw-12A3456B. The request identifies the gateway by ARN. In the request, string 999999999999 is the account number associated with the AWS account sending the request. Note that the response shown is truncated, it shows the media changer and only two tape drives. The trailing string in each device ARN is the device ID.

#### Sample Request
<a name="API_DescribeVTLDevices_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20131025T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9EXAMPLE
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.DescribeVTLDevices

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:999999999999:gateway/sgw-12A3456B"
}
```

#### Sample Response
<a name="API_DescribeVTLDevices_Example_1_Response"></a>

```
{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:999999999999:gateway/sgw-12A3456B",
    "VTLDevices": [
        {
            "DeviceiSCSIAttributes": {
                "ChapEnabled": "false",
                "NetworkInterfaceId": "*",
                "NetworkInterfacePort": "3260",
                "TargetARN": "arn:aws:storagegateway:us-east-2:999999999999:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:sgw-1fad4876-mediachanger"
            },
            "VTLDeviceARN": "arn:aws:storagegateway:us-east-2:999999999999:gateway/sgw-12A3456B/device/AMZN_SGW-1FAD4876_MEDIACHANGER_00001",
            "VTLDeviceProductIdentifier": "L700",
            "VTLDeviceType": "Medium Changer",
            "VTLDeviceVendor": "STK"
        },
        {
            "DeviceiSCSIAttributes": {
                "ChapEnabled": "false",
                "NetworkInterfaceId": "*",
                "NetworkInterfacePort": "3260",
                "TargetARN": "arn:aws:storagegateway:us-east-2:999999999999:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:sgw-1fad4876-tapedrive-01"
            },
            "VTLDeviceARN": "arn:aws:storagegateway:us-east-2:999999999999:gateway/sgw-12A3456B/device/AMZN_SGW-1FAD4876_TAPEDRIVE_00001",
            "VTLDeviceProductIdentifier": "ULT3580-TD5",
            "VTLDeviceType": "Tape Drive",
            "VTLDeviceVendor": "IBM"
        },
        {
            "DeviceiSCSIAttributes": {
                "ChapEnabled": "false",
                "NetworkInterfaceId": "*",
                "NetworkInterfacePort": "3260",
                "TargetARN": "arn:aws:storagegateway:us-east-2:999999999999:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:sgw-1fad4876-tapedrive-02"
            },
            "VTLDeviceARN": "arn:aws:storagegateway:us-east-2:999999999999:gateway/sgw-12A3456B/device/AMZN_SGW-1FAD4876_TAPEDRIVE_00002",
            "VTLDeviceProductIdentifier": "ULT3580-TD5",
            "VTLDeviceType": "Tape Drive",
            "VTLDeviceVendor": "IBM"
        }
    ]
}
```

## See Also
<a name="API_DescribeVTLDevices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DescribeVTLDevices) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DescribeVTLDevices) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DescribeVTLDevices) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DescribeVTLDevices) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DescribeVTLDevices) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DescribeVTLDevices) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DescribeVTLDevices) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DescribeVTLDevices) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DescribeVTLDevices) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DescribeVTLDevices) 