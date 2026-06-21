---
id: "@specs/aws/cloudtrail/docs/API_UpdateDashboard"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateDashboard"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# UpdateDashboard

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_UpdateDashboard
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateDashboard
<a name="API_UpdateDashboard"></a>

**Important**  
CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html).

 Updates the specified dashboard. 

 To set a refresh schedule, CloudTrail must be granted permissions to run the `StartDashboardRefresh` operation to refresh the dashboard on your behalf. To provide permissions, run the `PutResourcePolicy` operation to attach a resource-based policy to the dashboard. For more information, see [ Resource-based policy example for a dashboard](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html#security_iam_resource-based-policy-examples-dashboards) in the * AWS CloudTrail User Guide*. 

 CloudTrail runs queries to populate the dashboard's widgets during a manual or scheduled refresh. CloudTrail must be granted permissions to run the `StartQuery` operation on your behalf. To provide permissions, run the `PutResourcePolicy` operation to attach a resource-based policy to each event data store. For more information, see [Example: Allow CloudTrail to run queries to populate a dashboard](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html#security_iam_resource-based-policy-examples-eds-dashboard) in the * AWS CloudTrail User Guide*. 

## Request Syntax
<a name="API_UpdateDashboard_RequestSyntax"></a>

```
{
   "DashboardId": "{{string}}",
   "RefreshSchedule": { 
      "Frequency": { 
         "Unit": "{{string}}",
         "Value": {{number}}
      },
      "Status": "{{string}}",
      "TimeOfDay": "{{string}}"
   },
   "TerminationProtectionEnabled": {{boolean}},
   "Widgets": [ 
      { 
         "QueryParameters": [ "{{string}}" ],
         "QueryStatement": "{{string}}",
         "ViewProperties": { 
            "{{string}}" : "{{string}}" 
         }
      }
   ]
}
```

## Request Parameters
<a name="API_UpdateDashboard_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DashboardId](#API_UpdateDashboard_RequestSyntax) **   <a name="awscloudtrail-UpdateDashboard-request-DashboardId"></a>
 The name or ARN of the dashboard.   
Type: String  
Pattern: `^[a-zA-Z0-9._/\-:]+$`   
Required: Yes

 ** [RefreshSchedule](#API_UpdateDashboard_RequestSyntax) **   <a name="awscloudtrail-UpdateDashboard-request-RefreshSchedule"></a>
 The refresh schedule configuration for the dashboard.   
Type: [RefreshSchedule](API_RefreshSchedule.md) object  
Required: No

 ** [TerminationProtectionEnabled](#API_UpdateDashboard_RequestSyntax) **   <a name="awscloudtrail-UpdateDashboard-request-TerminationProtectionEnabled"></a>
 Specifies whether termination protection is enabled for the dashboard. If termination protection is enabled, you cannot delete the dashboard until termination protection is disabled.   
Type: Boolean  
Required: No

 ** [Widgets](#API_UpdateDashboard_RequestSyntax) **   <a name="awscloudtrail-UpdateDashboard-request-Widgets"></a>
 An array of widgets for the dashboard. A custom dashboard can have a maximum of 10 widgets.   
To add new widgets, pass in an array that includes the existing widgets along with any new widgets. Run the `GetDashboard` operation to get the list of widgets for the dashboard.  
To remove widgets, pass in an array that includes the existing widgets minus the widgets you want removed.  
Type: Array of [RequestWidget](API_RequestWidget.md) objects  
Required: No

## Response Syntax
<a name="API_UpdateDashboard_ResponseSyntax"></a>

```
{
   "CreatedTimestamp": number,
   "DashboardArn": "string",
   "Name": "string",
   "RefreshSchedule": { 
      "Frequency": { 
         "Unit": "string",
         "Value": number
      },
      "Status": "string",
      "TimeOfDay": "string"
   },
   "TerminationProtectionEnabled": boolean,
   "Type": "string",
   "UpdatedTimestamp": number,
   "Widgets": [ 
      { 
         "QueryAlias": "string",
         "QueryParameters": [ "string" ],
         "QueryStatement": "string",
         "ViewProperties": { 
            "string" : "string" 
         }
      }
   ]
}
```

## Response Elements
<a name="API_UpdateDashboard_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedTimestamp](#API_UpdateDashboard_ResponseSyntax) **   <a name="awscloudtrail-UpdateDashboard-response-CreatedTimestamp"></a>
 The timestamp that shows when the dashboard was created.   
Type: Timestamp

 ** [DashboardArn](#API_UpdateDashboard_ResponseSyntax) **   <a name="awscloudtrail-UpdateDashboard-response-DashboardArn"></a>
 The ARN for the dashboard.   
Type: String  
Pattern: `^[a-zA-Z0-9._/\-:]+$` 

 ** [Name](#API_UpdateDashboard_ResponseSyntax) **   <a name="awscloudtrail-UpdateDashboard-response-Name"></a>
 The name for the dashboard.   
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9_\-]+$` 

 ** [RefreshSchedule](#API_UpdateDashboard_ResponseSyntax) **   <a name="awscloudtrail-UpdateDashboard-response-RefreshSchedule"></a>
 The refresh schedule for the dashboard, if configured.   
Type: [RefreshSchedule](API_RefreshSchedule.md) object

 ** [TerminationProtectionEnabled](#API_UpdateDashboard_ResponseSyntax) **   <a name="awscloudtrail-UpdateDashboard-response-TerminationProtectionEnabled"></a>
 Indicates whether termination protection is enabled for the dashboard.   
Type: Boolean

 ** [Type](#API_UpdateDashboard_ResponseSyntax) **   <a name="awscloudtrail-UpdateDashboard-response-Type"></a>
 The type of dashboard.   
Type: String  
Valid Values: `MANAGED | CUSTOM` 

 ** [UpdatedTimestamp](#API_UpdateDashboard_ResponseSyntax) **   <a name="awscloudtrail-UpdateDashboard-response-UpdatedTimestamp"></a>
 The timestamp that shows when the dashboard was updated.   
Type: Timestamp

 ** [Widgets](#API_UpdateDashboard_ResponseSyntax) **   <a name="awscloudtrail-UpdateDashboard-response-Widgets"></a>
 An array of widgets for the dashboard.   
Type: Array of [Widget](API_Widget.md) objects

## Errors
<a name="API_UpdateDashboard_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **   
This exception is thrown when the specified resource is not ready for an operation. This can occur when you try to run an operation on a resource before CloudTrail has time to fully load the resource, or because another operation is modifying the resource. If this exception occurs, wait a few minutes, and then try the operation again.  
HTTP Status Code: 400

 ** EventDataStoreNotFoundException **   
The specified event data store was not found.  
HTTP Status Code: 400

 ** InactiveEventDataStoreException **   
The event data store is inactive.  
HTTP Status Code: 400

 ** InsufficientEncryptionPolicyException **   
For the `CreateTrail` `PutInsightSelectors`, `UpdateTrail`, `StartQuery`, and `StartImport` operations, this exception is thrown when the policy on the S3 bucket or AWS KMS key does not have sufficient permissions for the operation.  
For all other operations, this exception is thrown when the policy for the AWS KMS key does not have sufficient permissions for the operation.  
HTTP Status Code: 400

 ** InvalidQueryStatementException **   
The query that was submitted has validation errors, or uses incorrect syntax or unsupported keywords. For more information about writing a query, see [Create or edit a query](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-create-edit-query.html) in the * AWS CloudTrail User Guide*.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
This exception is thrown when the specified resource is not found.  
HTTP Status Code: 400

 ** ServiceQuotaExceededException **   
 This exception is thrown when the quota is exceeded. For information about CloudTrail quotas, see [Service quotas](https://docs.aws.amazon.com/general/latest/gr/ct.html#limits_cloudtrail) in the * AWS General Reference*.   
HTTP Status Code: 400

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## Examples
<a name="API_UpdateDashboard_Examples"></a>

### Example
<a name="API_UpdateDashboard_Example_1"></a>

The following example adds a new widget named `TopServices` to the custom dashboard named `AccountActivityDashboard`. The widgets array includes the two widgets that were already created for the dashboard and the new widget.

```
{
  "DashboardId": "AccountActivityDashboard",
  "Widgets": [
    {
      "ViewProperties": {
        "Height": "2",
        "Width": "4",
        "Title": "TopErrors",
        "View": "Table"
      },
      "QueryStatement": "SELECT errorCode, COUNT(*) AS eventCount FROM eds WHERE eventTime > '?' AND eventTime < '?' AND (errorCode is not null) GROUP BY errorCode ORDER BY eventCount DESC LIMIT 100",
      "QueryParameters": ["$StartTime$", "$EndTime$"]
    },
    {
      "ViewProperties": {
        "Height": "2",
        "Width": "4",
        "Title": "MostActiveRegions",
        "View": "PieChart",
        "LabelColumn": "awsRegion",
        "ValueColumn": "eventCount",
        "FilterColumn": "awsRegion"
      },
      "QueryStatement": "SELECT awsRegion, COUNT(*) AS eventCount FROM eds where eventTime > '?' and eventTime < '?' GROUP BY awsRegion ORDER BY eventCount LIMIT 100",
      "QueryParameters": ["$StartTime$", "$EndTime$"]
    },
    {
      "ViewProperties": {
        "Height": "2",
        "Width": "4",
        "Title": "TopServices",
        "View": "BarChart",
        "LabelColumn": "service",
        "ValueColumn": "eventCount",
        "FilterColumn": "service",
        "Orientation": "Vertical"
      },
      "QueryStatement": "SELECT replace(eventSource, '.amazonaws.com') AS service, COUNT(*) as eventCount FROM eds WHERE eventTime > '?' AND eventTime < '?' GROUP BY eventSource ORDER BY eventCount DESC LIMIT 100",
      "QueryParameters": ["$StartTime$", "$EndTime$"]
    }
  ]
}
```

### Example
<a name="API_UpdateDashboard_Example_2"></a>

The following example disables termination protection for a custom dashboard named `AccountActivityDashboard` to allow the dashboard to be deleted. It also turns off the refresh schedule.

```
{
   "DashboardId": "AccountActivityDashboard",
   "RefreshSchedule": { 
      "Status": "DISABLED"
   },
   "TerminationProtectionEnabled": false
}
```

### Example
<a name="API_UpdateDashboard_Example_3"></a>

The following example updates the refresh schedule for a custom dashboard named `AccountActivityDashboard`.

```
{
  "DashboardId": "AccountActivityDashboard",
  "RefreshSchedule": {
    "Frequency": {
      "Unit": "HOURS",
      "Value": 6
    },
    "Status": "ENABLED"
  }
}
```

## See Also
<a name="API_UpdateDashboard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/UpdateDashboard) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/UpdateDashboard) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/UpdateDashboard) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/UpdateDashboard) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/UpdateDashboard) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/UpdateDashboard) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/UpdateDashboard) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/UpdateDashboard) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/UpdateDashboard) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/UpdateDashboard) 