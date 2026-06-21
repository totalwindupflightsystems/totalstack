---
id: "@specs/aws/cloudtrail/docs/API_DeleteDashboard"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteDashboard"
status: active
depends_on:
  - "@specs/aws/cloudtrail/meta"
---

# DeleteDashboard

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudtrail/docs/API_DeleteDashboard
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteDashboard
<a name="API_DeleteDashboard"></a>

**Important**  
CloudTrail Lake will no longer be open to new customers starting May 31, 2026. If you would like to use CloudTrail Lake, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [CloudTrail Lake availability change](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-service-availability-change.html).

 Deletes the specified dashboard. You cannot delete a dashboard that has termination protection enabled. 

## Request Syntax
<a name="API_DeleteDashboard_RequestSyntax"></a>

```
{
   "DashboardId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDashboard_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DashboardId](#API_DeleteDashboard_RequestSyntax) **   <a name="awscloudtrail-DeleteDashboard-request-DashboardId"></a>
 The name or ARN for the dashboard.   
Type: String  
Pattern: `^[a-zA-Z0-9._/\-:]+$`   
Required: Yes

## Response Elements
<a name="API_DeleteDashboard_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteDashboard_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **   
This exception is thrown when the specified resource is not ready for an operation. This can occur when you try to run an operation on a resource before CloudTrail has time to fully load the resource, or because another operation is modifying the resource. If this exception occurs, wait a few minutes, and then try the operation again.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
This exception is thrown when the specified resource is not found.  
HTTP Status Code: 400

 ** UnsupportedOperationException **   
This exception is thrown when the requested operation is not supported.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteDashboard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudtrail-2013-11-01/DeleteDashboard) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudtrail-2013-11-01/DeleteDashboard) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/DeleteDashboard) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudtrail-2013-11-01/DeleteDashboard) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/DeleteDashboard) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudtrail-2013-11-01/DeleteDashboard) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudtrail-2013-11-01/DeleteDashboard) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudtrail-2013-11-01/DeleteDashboard) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudtrail-2013-11-01/DeleteDashboard) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/DeleteDashboard) 