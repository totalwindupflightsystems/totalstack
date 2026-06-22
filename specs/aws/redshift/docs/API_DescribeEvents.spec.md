---
id: "@specs/aws/redshift/docs/API_DescribeEvents"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeEvents"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeEvents

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeEvents
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeEvents
<a name="API_DescribeEvents"></a>

Returns events related to clusters, security groups, snapshots, and parameter groups for the past 14 days. Events specific to a particular cluster, security group, snapshot or parameter group can be obtained by providing the name as a parameter. By default, the past hour of events are returned.

## Request Parameters
<a name="API_DescribeEvents_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Duration **   
The number of minutes prior to the time of the request for which to retrieve events. For example, if the request is sent at 18:00 and you specify a duration of 60, then only events which have occurred after 17:00 will be returned.  
Default: `60`   
Type: Integer  
Required: No

 ** EndTime **   
The end of the time interval for which to retrieve events, specified in ISO 8601 format. For more information about ISO 8601, go to the [ISO8601 Wikipedia page.](http://en.wikipedia.org/wiki/ISO_8601)   
Example: `2009-07-08T18:00Z`   
Type: Timestamp  
Required: No

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a [DescribeEvents](#API_DescribeEvents) request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `marker` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.   
Default: `100`   
Constraints: minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** SourceIdentifier **   
The identifier of the event source for which events will be returned. If this parameter is not specified, then all sources are included in the response.  
Constraints:  
If *SourceIdentifier* is supplied, *SourceType* must also be provided.  
+ Specify a cluster identifier when *SourceType* is `cluster`.
+ Specify a cluster security group name when *SourceType* is `cluster-security-group`.
+ Specify a cluster parameter group name when *SourceType* is `cluster-parameter-group`.
+ Specify a cluster snapshot identifier when *SourceType* is `cluster-snapshot`.
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SourceType **   
The event source to retrieve events for. If no value is specified, all events are returned.  
Constraints:  
If *SourceType* is supplied, *SourceIdentifier* must also be provided.  
+ Specify `cluster` when *SourceIdentifier* is a cluster identifier.
+ Specify `cluster-security-group` when *SourceIdentifier* is a cluster security group name.
+ Specify `cluster-parameter-group` when *SourceIdentifier* is a cluster parameter group name.
+ Specify `cluster-snapshot` when *SourceIdentifier* is a cluster snapshot identifier.
Type: String  
Valid Values: `cluster | cluster-parameter-group | cluster-security-group | cluster-snapshot | scheduled-action`   
Required: No

 ** StartTime **   
The beginning of the time interval to retrieve events for, specified in ISO 8601 format. For more information about ISO 8601, go to the [ISO8601 Wikipedia page.](http://en.wikipedia.org/wiki/ISO_8601)   
Example: `2009-07-08T18:00Z`   
Type: Timestamp  
Required: No

## Response Elements
<a name="API_DescribeEvents_ResponseElements"></a>

The following elements are returned by the service.

 **Events.Event.N**   
A list of `Event` instances.   
Type: Array of [Event](API_Event.md) objects

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `Marker` parameter and retrying the command. If the `Marker` field is empty, all response records have been retrieved for the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_DescribeEvents_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeEvents_Examples"></a>

### Example
<a name="API_DescribeEvents_Example_1"></a>

This example illustrates one usage of DescribeEvents.

#### Sample Request
<a name="API_DescribeEvents_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeEvents
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeEvents_Example_1_Response"></a>

```
<DescribeEventsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeEventsResult>
    <Events>
      <Event>
        <Date>2019-12-26T23:36:48.457Z</Date>
        <Severity>INFO</Severity>
        <EventId>REDSHIFT-EVENT-1004</EventId>
        <SourceIdentifier>myclusterparametergroup</SourceIdentifier>
        <SourceType>cluster-parameter-group</SourceType>
        <EventCategories>
          <EventCategory>configuration</EventCategory>
        </EventCategories>
        <Message>Cluster parameter group 'myclusterparametergroup' was deleted at 2019-12-26 23:36 UTC.</Message>
      </Event>
      <Event>
        <Date>2019-12-26T23:40:00.753Z</Date>
        <Severity>INFO</Severity>
        <EventId>REDSHIFT-EVENT-2011</EventId>
        <SourceIdentifier>mysnapshotid</SourceIdentifier>
        <SourceType>cluster-snapshot</SourceType>
        <EventCategories>
          <EventCategory>management</EventCategory>
        </EventCategories>
        <Message>The cluster snapshot 'mysnapshotid' for Amazon Redshift cluster 'mycluster' was deleted at 2019-12-26 23:40 UTC.</Message>
      </Event>
      <Event>
        <Date>2019-12-26T23:42:43.247Z</Date>
        <Severity>INFO</Severity>
        <EventId>REDSHIFT-EVENT-2001</EventId>
        <SourceIdentifier>mycluster</SourceIdentifier>
        <SourceType>cluster</SourceType>
        <EventCategories>
          <EventCategory>management</EventCategory>
        </EventCategories>
        <Message>Amazon Redshift cluster 'mycluster' has been deleted at 2019-12-26 23:42 UTC. A final snapshot was not saved.</Message>
      </Event>
      <Event>
        <Date>2019-12-26T23:55:04.170Z</Date>
        <Severity>INFO</Severity>
        <EventId>REDSHIFT-EVENT-3614</EventId>
        <SourceIdentifier>myscheduledaction</SourceIdentifier>
        <SourceType>scheduled-action</SourceType>
        <EventCategories>
          <EventCategory>management</EventCategory>
        </EventCategories>
        <Message>The scheduled action 'myscheduledaction' was created at 2019-12-26 23:55 UTC. The first invocation is scheduled at 2019-12-31 00:00 UTC.</Message>
      </Event>
      <Event>
        <Date>2019-12-26T23:55:19.846Z</Date>
        <Severity>INFO</Severity>
        <EventId>REDSHIFT-EVENT-3627</EventId>
        <SourceIdentifier>myscheduledaction</SourceIdentifier>
        <SourceType>scheduled-action</SourceType>
        <EventCategories>
          <EventCategory>management</EventCategory>
        </EventCategories>
        <Message>Scheduled action 'myscheduledaction' was deleted at 2019-12-26 23:55 UTC.</Message>
      </Event>
      <Event>
        <Date>2019-12-27T00:16:36.767Z</Date>
        <Severity>INFO</Severity>
        <EventId>REDSHIFT-EVENT-2000</EventId>
        <SourceIdentifier>mycluster</SourceIdentifier>
        <SourceType>cluster</SourceType>
        <EventCategories>
          <EventCategory>management</EventCategory>
        </EventCategories>
        <Message>Amazon Redshift cluster 'mycluster' has been created at 2019-12-27 00:16 UTC and is ready for use.</Message>
      </Event>
    </Events>
  </DescribeEventsResult>
  <ResponseMetadata>
    <RequestId>eb82309b-283f-11ea-9caa-c956bec1ce87</RequestId>
  </ResponseMetadata>
</DescribeEventsResponse>
```

## See Also
<a name="API_DescribeEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeEvents) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeEvents) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeEvents) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeEvents) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeEvents) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeEvents) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeEvents) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeEvents) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeEvents) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeEvents) 