---
id: "@specs/aws/storagegateway/docs/API_DescribeMaintenanceStartTime"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeMaintenanceStartTime"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# DescribeMaintenanceStartTime

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_DescribeMaintenanceStartTime
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeMaintenanceStartTime
<a name="API_DescribeMaintenanceStartTime"></a>

Returns your gateway's maintenance window schedule information, with values for monthly or weekly cadence, specific day and time to begin maintenance, and which types of updates to apply. Time values returned are for the gateway's time zone.

## Request Syntax
<a name="API_DescribeMaintenanceStartTime_RequestSyntax"></a>

```
{
   "GatewayARN": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeMaintenanceStartTime_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayARN](#API_DescribeMaintenanceStartTime_RequestSyntax) **   <a name="StorageGateway-DescribeMaintenanceStartTime-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

## Response Syntax
<a name="API_DescribeMaintenanceStartTime_ResponseSyntax"></a>

```
{
   "DayOfMonth": number,
   "DayOfWeek": number,
   "GatewayARN": "string",
   "HourOfDay": number,
   "MinuteOfHour": number,
   "SoftwareUpdatePreferences": { 
      "AutomaticUpdatePolicy": "string"
   },
   "Timezone": "string"
}
```

## Response Elements
<a name="API_DescribeMaintenanceStartTime_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DayOfMonth](#API_DescribeMaintenanceStartTime_ResponseSyntax) **   <a name="StorageGateway-DescribeMaintenanceStartTime-response-DayOfMonth"></a>
The day of the month component of the maintenance start time represented as an ordinal number from 1 to 28, where 1 represents the first day of the month. It is not possible to set the maintenance schedule to start on days 29 through 31.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 28.

 ** [DayOfWeek](#API_DescribeMaintenanceStartTime_ResponseSyntax) **   <a name="StorageGateway-DescribeMaintenanceStartTime-response-DayOfWeek"></a>
An ordinal number between 0 and 6 that represents the day of the week, where 0 represents Sunday and 6 represents Saturday. The day of week is in the time zone of the gateway.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 6.

 ** [GatewayARN](#API_DescribeMaintenanceStartTime_ResponseSyntax) **   <a name="StorageGateway-DescribeMaintenanceStartTime-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

 ** [HourOfDay](#API_DescribeMaintenanceStartTime_ResponseSyntax) **   <a name="StorageGateway-DescribeMaintenanceStartTime-response-HourOfDay"></a>
The hour component of the maintenance start time represented as *hh*, where *hh* is the hour (0 to 23). The hour of the day is in the time zone of the gateway.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 23.

 ** [MinuteOfHour](#API_DescribeMaintenanceStartTime_ResponseSyntax) **   <a name="StorageGateway-DescribeMaintenanceStartTime-response-MinuteOfHour"></a>
The minute component of the maintenance start time represented as *mm*, where *mm* is the minute (0 to 59). The minute of the hour is in the time zone of the gateway.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 59.

 ** [SoftwareUpdatePreferences](#API_DescribeMaintenanceStartTime_ResponseSyntax) **   <a name="StorageGateway-DescribeMaintenanceStartTime-response-SoftwareUpdatePreferences"></a>
A set of variables indicating the software update preferences for the gateway.  
Includes `AutomaticUpdatePolicy` parameter with the following inputs:  
 `ALL_VERSIONS` - Enables regular gateway maintenance updates.  
 `EMERGENCY_VERSIONS_ONLY` - Disables regular gateway maintenance updates. The gateway will still receive emergency version updates on rare occasions if necessary to remedy highly critical security or durability issues. You will be notified before an emergency version update is applied. These updates are applied during your gateway's scheduled maintenance window.  
Type: [SoftwareUpdatePreferences](API_SoftwareUpdatePreferences.md) object

 ** [Timezone](#API_DescribeMaintenanceStartTime_ResponseSyntax) **   <a name="StorageGateway-DescribeMaintenanceStartTime-response-Timezone"></a>
A value that indicates the time zone that is set for the gateway. The start time and day of week specified should be in the time zone of the gateway.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 10.

## Errors
<a name="API_DescribeMaintenanceStartTime_Errors"></a>

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
<a name="API_DescribeMaintenanceStartTime_Examples"></a>

### Return information about a gateway's maintenance window
<a name="API_DescribeMaintenanceStartTime_Example_1"></a>

The following example shows a request that describes a gateway's maintenance window.

#### Sample Request
<a name="API_DescribeMaintenanceStartTime_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.DescribeMaintenanceStartTime

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B"
}
```

#### Sample Response
<a name="API_DescribeMaintenanceStartTime_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Date: Wed, 25 Apr 2012 12:00:02 GMT
Content-type: application/x-amz-json-1.1
Content-length: 136

{
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B",
    "DayOfMonth": "28",
    "DayOfWeek": "2",
    "HourOfDay": "15",
    "MinuteOfHour": "35",
    "Timezone": "GMT+7:00"
}
```

## See Also
<a name="API_DescribeMaintenanceStartTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/DescribeMaintenanceStartTime) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/DescribeMaintenanceStartTime) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/DescribeMaintenanceStartTime) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/DescribeMaintenanceStartTime) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/DescribeMaintenanceStartTime) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/DescribeMaintenanceStartTime) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/DescribeMaintenanceStartTime) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/DescribeMaintenanceStartTime) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/DescribeMaintenanceStartTime) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/DescribeMaintenanceStartTime) 