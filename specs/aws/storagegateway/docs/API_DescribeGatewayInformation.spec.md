---
id: "@specs/aws/storagegateway/docs/API_DescribeGatewayInformation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeGatewayInformation"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DescribeGatewayInformation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DescribeGatewayInformation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeGatewayInformation
<a name="API_DescribeGatewayInformation"></a>

Returns metadata about a gateway such as its name, network interfaces, time zone, status, and software version. To specify which gateway to describe, use the Amazon Resource Name (ARN) of the gateway in your request.

## Request Syntax
<a name="API_DescribeGatewayInformation_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeGatewayInformation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_DescribeGatewayInformation_RequestSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_DescribeGatewayInformation_ResponseSyntax"></a>

```
{
   "CloudWatchLogGroupARN": "string",
   "DeprecationDate": "string",
   "Ec2InstanceId": "string",
   "Ec2InstanceRegion": "string",
   "EndpointType": "string",
   "GatewayARN": "string",
   "GatewayCapacity": "string",
   "GatewayId": "string",
   "GatewayName": "string",
   "GatewayNetworkInterfaces": [ 
      { 
         "Ipv4Address": "string",
         "Ipv6Address": "string",
         "MacAddress": "string"
      }
   ],
   "GatewayState": "string",
   "GatewayTimezone": "string",
   "GatewayType": "string",
   "HostEnvironment": "string",
   "HostEnvironmentId": "string",
   "LastSoftwareUpdate": "string",
   "NextUpdateAvailabilityDate": "string",
   "SoftwareUpdatesEndDate": "string",
   "SoftwareVersion": "string",
   "SupportedGatewayCapacities": [ "string" ],
   "Tags": [ 
      { 
         "Key": "string",
         "Value": "string"
      }
   ],
   "VPCEndpoint": "string"
}
```

## Response Elements
<a name="API_DescribeGatewayInformation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CloudWatchLogGroupARN](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-CloudWatchLogGroupARN"></a>
The Amazon Resource Name (ARN) of the Amazon CloudWatch log group that is used to monitor events in the gateway. This field only only exist and returns once it have been chosen and set by the SGW service, based on the OS version of the gateway VM  
Type: String  
Length Constraints: Maximum length of 562.

 ** [DeprecationDate](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-DeprecationDate"></a>
Date after which this gateway will not receive software updates for new features and bug fixes.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 25.

 ** [Ec2InstanceId](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-Ec2InstanceId"></a>
The ID of the Amazon EC2 instance that was used to launch the gateway.  
Type: String

 ** [Ec2InstanceRegion](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-Ec2InstanceRegion"></a>
The AWS Region where the Amazon EC2 instance is located.  
Type: String

 ** [EndpointType](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-EndpointType"></a>
The type of endpoint for your gateway.  
Valid Values: `STANDARD` \| `FIPS`   
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 8.

 ** [GatewayARN](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

 ** [GatewayCapacity](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-GatewayCapacity"></a>
Specifies the size of the gateway's metadata cache.  
Type: String  
Valid Values: `Small | Medium | Large` 

 ** [GatewayId](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-GatewayId"></a>
The unique identifier assigned to your gateway during activation. This ID becomes part of the gateway Amazon Resource Name (ARN), which you use as input for other operations.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 30.

 ** [GatewayName](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-GatewayName"></a>
The name you configured for your gateway.  
Type: String

 ** [GatewayNetworkInterfaces](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-GatewayNetworkInterfaces"></a>
A [NetworkInterface](API_NetworkInterface.md) array that contains descriptions of the gateway network interfaces.  
Type: Array of [NetworkInterface](API_NetworkInterface.md) objects

 ** [GatewayState](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-GatewayState"></a>
A value that indicates the operating state of the gateway.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 25.

 ** [GatewayTimezone](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-GatewayTimezone"></a>
A value that indicates the time zone configured for the gateway.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 10.

 ** [GatewayType](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-GatewayType"></a>
The type of the gateway.  
Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use the service normally. For capabilities similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/).
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 20.

 ** [HostEnvironment](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-HostEnvironment"></a>
The type of hardware or software platform on which the gateway is running.  
Tape Gateway is no longer available on Snow Family devices.
Type: String  
Valid Values: `VMWARE | HYPER-V | EC2 | KVM | OTHER | SNOWBALL` 

 ** [HostEnvironmentId](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-HostEnvironmentId"></a>
A unique identifier for the specific instance of the host platform running the gateway. This value is only available for certain host environments, and its format depends on the host environment type.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [LastSoftwareUpdate](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-LastSoftwareUpdate"></a>
The date on which the last software update was applied to the gateway. If the gateway has never been updated, this field does not return a value in the response. This only only exist and returns once it have been chosen and set by the SGW service, based on the OS version of the gateway VM  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 25.

 ** [NextUpdateAvailabilityDate](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-NextUpdateAvailabilityDate"></a>
The date on which an update to the gateway is available. This date is in the time zone of the gateway. If the gateway is not available for an update this field is not returned in the response.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 25.

 ** [SoftwareUpdatesEndDate](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-SoftwareUpdatesEndDate"></a>
Date after which this gateway will not receive software updates for new features.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 25.

 ** [SoftwareVersion](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-SoftwareVersion"></a>
The version number of the software running on the gateway appliance.  
Type: String

 ** [SupportedGatewayCapacities](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-SupportedGatewayCapacities"></a>
A list of the metadata cache sizes that the gateway can support based on its current hardware specifications.  
Type: Array of strings  
Valid Values: `Small | Medium | Large` 

 ** [Tags](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-Tags"></a>
A list of up to 50 tags assigned to the gateway, sorted alphabetically by key name. Each tag is a key-value pair. For a gateway with more than 10 tags assigned, you can view all tags using the `ListTagsForResource` API operation.  
Type: Array of [Tag](API_Tag.md) objects

 ** [VPCEndpoint](#API_DescribeGatewayInformation_ResponseSyntax) **   <a name="StorageGateway-DescribeGatewayInformation-response-VPCEndpoint"></a>
The configuration settings for the virtual private cloud (VPC) endpoint for your gateway.  
Type: String

## Errors
<a name="API_DescribeGatewayInformation_Errors"></a>

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
<a name="API_DescribeGatewayInformation_Examples"></a>

### Return metadata about a gateway
<a name="API_DescribeGatewayInformation_Example_1"></a>

The following example shows a request for describing a gateway.

#### Sample Request
<a name="API_DescribeGatewayInformation_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.DescribeGatewayInformation

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B"
}
```

#### Sample Response
<a name="API_DescribeGatewayInformation_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 227

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B",
    "GatewayId": "sgw-AABB1122",
    "GatewayNetworkInterfaces": [
        {
            "Ipv4Address": "10.35.69.216"
        }
    ],
    "GatewayState": "STATE_RUNNING",
    "GatewayTimezone": "GMT-8:00",
    "LastSoftwareUpdate": "2015-01-02T16:00:00",
    "NextUpdateAvailabilityDate": "2016-01-02T16:00:00"
}
```

## See Also
<a name="API_DescribeGatewayInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DescribeGatewayInformation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DescribeGatewayInformation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DescribeGatewayInformation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DescribeGatewayInformation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DescribeGatewayInformation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DescribeGatewayInformation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DescribeGatewayInformation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DescribeGatewayInformation) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DescribeGatewayInformation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DescribeGatewayInformation) 