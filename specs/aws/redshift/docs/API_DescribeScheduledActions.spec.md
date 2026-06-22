---
id: "@specs/aws/redshift/docs/API_DescribeScheduledActions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeScheduledActions"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeScheduledActions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeScheduledActions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeScheduledActions
<a name="API_DescribeScheduledActions"></a>

Describes properties of scheduled actions. 

## Request Parameters
<a name="API_DescribeScheduledActions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Active **   
If true, retrieve only active scheduled actions. If false, retrieve only disabled scheduled actions.   
Type: Boolean  
Required: No

 ** EndTime **   
The end time in UTC of the scheduled action to retrieve. Only active scheduled actions that have invocations before this time are retrieved.  
Type: Timestamp  
Required: No

 **Filters.ScheduledActionFilter.N**   
List of scheduled action filters.   
Type: Array of [ScheduledActionFilter](API_ScheduledActionFilter.md) objects  
Required: No

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a [DescribeScheduledActions](#API_DescribeScheduledActions) request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `marker` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.   
Default: `100`   
Constraints: minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** ScheduledActionName **   
The name of the scheduled action to retrieve.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** StartTime **   
The start time in UTC of the scheduled actions to retrieve. Only active scheduled actions that have invocations after this time are retrieved.  
Type: Timestamp  
Required: No

 ** TargetActionType **   
The type of the scheduled actions to retrieve.   
Type: String  
Valid Values: `ResizeCluster | PauseCluster | ResumeCluster`   
Required: No

## Response Elements
<a name="API_DescribeScheduledActions_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a [DescribeScheduledActions](#API_DescribeScheduledActions) request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.

 **ScheduledActions.ScheduledAction.N**   
List of retrieved scheduled actions.   
Type: Array of [ScheduledAction](API_ScheduledAction.md) objects

## Errors
<a name="API_DescribeScheduledActions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ScheduledActionNotFound **   
The scheduled action cannot be found.   
HTTP Status Code: 400

 ** UnauthorizedOperation **   
Your account is not authorized to perform the requested operation.  
HTTP Status Code: 400

## Examples
<a name="API_DescribeScheduledActions_Examples"></a>

### Example
<a name="API_DescribeScheduledActions_Example_1"></a>

This example illustrates one usage of DescribeScheduledActions.

#### Sample Request
<a name="API_DescribeScheduledActions_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeScheduledActions
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeScheduledActions_Example_1_Response"></a>

```
<DescribeScheduledActionsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeScheduledActionsResult>
    <ScheduledActions>
      <ScheduledAction>
        <IamRole>arn:aws:iam::123456789012:role/myRedshiftRole</IamRole>
        <Schedule>at(2019-12-10T00:07:00)</Schedule>
        <ScheduledActionName>myscheduledaction</ScheduledActionName>
        <TargetAction>
          <ResizeCluster>
            <ClusterIdentifier>mycluster</ClusterIdentifier>
            <Classic>false</Classic>
            <NumberOfNodes>4</NumberOfNodes>
          </ResizeCluster>
        </TargetAction>
        <NextInvocations/>
        <State>DISABLED</State>
      </ScheduledAction>
    </ScheduledActions>
  </DescribeScheduledActionsResult>
  <ResponseMetadata>
    <RequestId>d9377e44-28d1-11ea-b6af-7126da6f11af</RequestId>
  </ResponseMetadata>
</DescribeScheduledActionsResponse>
```

## See Also
<a name="API_DescribeScheduledActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeScheduledActions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeScheduledActions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeScheduledActions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeScheduledActions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeScheduledActions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeScheduledActions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeScheduledActions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeScheduledActions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeScheduledActions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeScheduledActions) 