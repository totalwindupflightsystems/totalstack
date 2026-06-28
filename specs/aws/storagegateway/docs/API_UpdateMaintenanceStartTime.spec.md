---
id: "@specs/aws/storagegateway/docs/API_UpdateMaintenanceStartTime"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateMaintenanceStartTime"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# UpdateMaintenanceStartTime

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_UpdateMaintenanceStartTime
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateMaintenanceStartTime
<a name="API_UpdateMaintenanceStartTime"></a>

Updates a gateway's maintenance window schedule, with settings for monthly or weekly cadence, specific day and time to begin maintenance, and which types of updates to apply. Time configuration uses the gateway's time zone. You can pass values for a complete maintenance schedule, or update policy, or both. Previous values will persist for whichever setting you choose not to modify. If an incomplete or invalid maintenance schedule is passed, the entire request will be rejected with an error and no changes will occur.

A complete maintenance schedule must include values for *both* `MinuteOfHour` and `HourOfDay`, and *either* `DayOfMonth` *or* `DayOfWeek`.

**Note**  
We recommend keeping maintenance updates turned on, except in specific use cases where the brief disruptions caused by updating the gateway could critically impact your deployment.

## Request Syntax
<a name="API_UpdateMaintenanceStartTime_RequestSyntax"></a>

```
{
   "DayOfMonth": {{number}},
   "DayOfWeek": {{number}},
   "GatewayARN": "{{string}}",
   "HourOfDay": {{number}},
   "MinuteOfHour": {{number}},
   "SoftwareUpdatePreferences": { 
      "AutomaticUpdatePolicy": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateMaintenanceStartTime_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DayOfMonth](#API_UpdateMaintenanceStartTime_RequestSyntax) **   <a name="StorageGateway-UpdateMaintenanceStartTime-request-DayOfMonth"></a>
The day of the month component of the maintenance start time represented as an ordinal number from 1 to 28, where 1 represents the first day of the month. It is not possible to set the maintenance schedule to start on days 29 through 31.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 28.  
Required: No

 ** [DayOfWeek](#API_UpdateMaintenanceStartTime_RequestSyntax) **   <a name="StorageGateway-UpdateMaintenanceStartTime-request-DayOfWeek"></a>
The day of the week component of the maintenance start time week represented as an ordinal number from 0 to 6, where 0 represents Sunday and 6 represents Saturday.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 6.  
Required: No

 ** [GatewayARN](#API_UpdateMaintenanceStartTime_RequestSyntax) **   <a name="StorageGateway-UpdateMaintenanceStartTime-request-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.  
Required: Yes

 ** [HourOfDay](#API_UpdateMaintenanceStartTime_RequestSyntax) **   <a name="StorageGateway-UpdateMaintenanceStartTime-request-HourOfDay"></a>
The hour component of the maintenance start time represented as *hh*, where *hh* is the hour (00 to 23). The hour of the day is in the time zone of the gateway.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 23.  
Required: No

 ** [MinuteOfHour](#API_UpdateMaintenanceStartTime_RequestSyntax) **   <a name="StorageGateway-UpdateMaintenanceStartTime-request-MinuteOfHour"></a>
The minute component of the maintenance start time represented as *mm*, where *mm* is the minute (00 to 59). The minute of the hour is in the time zone of the gateway.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 59.  
Required: No

 ** [SoftwareUpdatePreferences](#API_UpdateMaintenanceStartTime_RequestSyntax) **   <a name="StorageGateway-UpdateMaintenanceStartTime-request-SoftwareUpdatePreferences"></a>
A set of variables indicating the software update preferences for the gateway.  
Includes `AutomaticUpdatePolicy` field with the following inputs:  
 `ALL_VERSIONS` - Enables regular gateway maintenance updates.  
 `EMERGENCY_VERSIONS_ONLY` - Disables regular gateway maintenance updates. The gateway will still receive emergency version updates on rare occasions if necessary to remedy highly critical security or durability issues. You will be notified before an emergency version update is applied. These updates are applied during your gateway's scheduled maintenance window.  
Type: [SoftwareUpdatePreferences](API_SoftwareUpdatePreferences.md) object  
Required: No

## Response Syntax
<a name="API_UpdateMaintenanceStartTime_ResponseSyntax"></a>

```
{
   "GatewayARN": "string"
}
```

## Response Elements
<a name="API_UpdateMaintenanceStartTime_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayARN](#API_UpdateMaintenanceStartTime_ResponseSyntax) **   <a name="StorageGateway-UpdateMaintenanceStartTime-response-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.  
Type: String  
Length Constraints: Minimum length of 50. Maximum length of 500.

## Errors
<a name="API_UpdateMaintenanceStartTime_Errors"></a>

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
<a name="API_UpdateMaintenanceStartTime_Examples"></a>

### Update a gateway's maintenance start time
<a name="API_UpdateMaintenanceStartTime_Example_1"></a>

The following example shows a request that enables automatic maintenance updates and sets a maintenance start time on the 28th day of each month for gateway ID sgw-12A3456B.

#### Sample Request
<a name="API_UpdateMaintenanceStartTime_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: storagegateway.us-east-2.amazonaws.com
x-amz-Date: 20120425T120000Z
Authorization: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-type: application/x-amz-json-1.1
x-amz-target: StorageGateway_20130630.UpdateMaintenanceStartTime
{
    "SoftwareUpdatePreferences": {
        "AutomaticUpdatePolicy": "ALL_VERSIONS"
     },
    "GatewayARN": "arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B",
    "DayOfMonth": "28",
    "HourOfDay": "15",
    "MinuteOfHour": "35"
}
```

## See Also
<a name="API_UpdateMaintenanceStartTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/storagegateway-2013-06-30/UpdateMaintenanceStartTime) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/storagegateway-2013-06-30/UpdateMaintenanceStartTime) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/UpdateMaintenanceStartTime) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/storagegateway-2013-06-30/UpdateMaintenanceStartTime) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/UpdateMaintenanceStartTime) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/storagegateway-2013-06-30/UpdateMaintenanceStartTime) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/storagegateway-2013-06-30/UpdateMaintenanceStartTime) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/storagegateway-2013-06-30/UpdateMaintenanceStartTime) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/storagegateway-2013-06-30/UpdateMaintenanceStartTime) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/UpdateMaintenanceStartTime) 