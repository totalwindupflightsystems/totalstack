---
id: "@specs/aws/rds/docs/API_DescribeEvents"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeEvents"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeEvents

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeEvents
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeEvents
<a name="API_DescribeEvents"></a>

Returns events related to DB instances, DB clusters, DB parameter groups, DB security groups, DB snapshots, DB cluster snapshots, and RDS Proxies for the past 14 days. Events specific to a particular DB instance, DB cluster, DB parameter group, DB security group, DB snapshot, DB cluster snapshot group, or RDS Proxy can be obtained by providing the name as a parameter.

For more information on working with events, see [Monitoring Amazon RDS events](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/working-with-events.html) in the *Amazon RDS User Guide* and [Monitoring Amazon Aurora events](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/working-with-events.html) in the *Amazon Aurora User Guide*.

**Note**  
By default, RDS returns events that were generated in the past hour.

## Request Parameters
<a name="API_DescribeEvents_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Duration **   
The number of minutes to retrieve events for.  
Default: 60  
Type: Integer  
Required: No

 ** EndTime **   
The end of the time interval for which to retrieve events, specified in ISO 8601 format. For more information about ISO 8601, go to the [ISO8601 Wikipedia page.](http://en.wikipedia.org/wiki/ISO_8601)   
Example: 2009-07-08T18:00Z  
Type: Timestamp  
Required: No

 **EventCategories.EventCategory.N**   
A list of event categories that trigger notifications for a event notification subscription.  
Type: Array of strings  
Required: No

 **Filters.Filter.N**   
This parameter isn't currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
An optional pagination token provided by a previous DescribeEvents request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** SourceIdentifier **   
The identifier of the event source for which events are returned. If not specified, then all sources are included in the response.  
Constraints:  
+ If `SourceIdentifier` is supplied, `SourceType` must also be provided.
+ If the source type is a DB instance, a `DBInstanceIdentifier` value must be supplied.
+ If the source type is a DB cluster, a `DBClusterIdentifier` value must be supplied.
+ If the source type is a DB parameter group, a `DBParameterGroupName` value must be supplied.
+ If the source type is a DB security group, a `DBSecurityGroupName` value must be supplied.
+ If the source type is a DB snapshot, a `DBSnapshotIdentifier` value must be supplied.
+ If the source type is a DB cluster snapshot, a `DBClusterSnapshotIdentifier` value must be supplied.
+ If the source type is an RDS Proxy, a `DBProxyName` value must be supplied.
+ Can't end with a hyphen or contain two consecutive hyphens.
Type: String  
Required: No

 ** SourceType **   
The event source to retrieve events for. If no value is specified, all events are returned.  
Type: String  
Valid Values: `db-instance | db-parameter-group | db-security-group | db-snapshot | db-cluster | db-cluster-snapshot | custom-engine-version | db-proxy | blue-green-deployment | db-shard-group | zero-etl`   
Required: No

 ** StartTime **   
The beginning of the time interval to retrieve events for, specified in ISO 8601 format. For more information about ISO 8601, go to the [ISO8601 Wikipedia page.](http://en.wikipedia.org/wiki/ISO_8601)   
Example: 2009-07-08T18:00Z  
Type: Timestamp  
Required: No

## Response Elements
<a name="API_DescribeEvents_ResponseElements"></a>

The following elements are returned by the service.

 **Events.Event.N**   
A list of `Event` instances.  
Type: Array of [Event](API_Event.md) objects

 ** Marker **   
An optional pagination token provided by a previous Events request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

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
https://rds.us-west-2.amazonaws.com/
   ?Action=DescribeEvents
   &Duration=1440
   &MaxRecords=100
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140421/us-west-2/rds/aws4_request
   &X-Amz-Date=20140421T194733Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=8e313cabcdbd9766c56a2886b5b298fd944e0b7cfa248953c82705fdd0374f27
```

#### Sample Response
<a name="API_DescribeEvents_Example_1_Response"></a>

```
<DescribeEventsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeEventsResult>
    <Events>
      <Event>
        <Message>Backing up DB instance</Message>
        <SourceType>db-instance</SourceType>
        <EventCategories>
          <EventCategory>backup</EventCategory>
        </EventCategories>
        <Date>2014-04-21T06:23:33.866Z</Date>
        <SourceIdentifier>mypgdbinstance</SourceIdentifier>
      </Event>
      <Event>
        <Message>Finished DB Instance backup</Message>
        <SourceType>db-instance</SourceType>
        <EventCategories>
          <EventCategory>backup</EventCategory>
        </EventCategories>
        <Date>2014-04-21T06:25:03.928Z</Date>
        <SourceIdentifier>mypgdbinstance</SourceIdentifier>
      </Event>
      <Event>
        <Message>Backing up DB instance</Message>
        <SourceType>db-instance</SourceType>
        <EventCategories>
          <EventCategory>backup</EventCategory>
        </EventCategories>
        <Date>2014-04-21T07:09:34.594Z</Date>
        <SourceIdentifier>my-mysqlexampledb4</SourceIdentifier>
      </Event>
      <Event>
        <Message>Finished DB Instance backup</Message>
        <SourceType>db-instance</SourceType>
        <EventCategories>
          <EventCategory>backup</EventCategory>
        </EventCategories>
        <Date>2014-04-21T07:11:05.640Z</Date>
        <SourceIdentifier>my-mysqlexampledb4</SourceIdentifier>
      </Event>
      <Event>
        <Message>Backing up DB instance</Message>
        <SourceType>db-instance</SourceType>
        <EventCategories>
          <EventCategory>backup</EventCategory>
        </EventCategories>
        <Date>2014-04-21T09:26:25.988Z</Date>
        <SourceIdentifier>my-oracledb1</SourceIdentifier>
      </Event>
      <Event>
        <Message>Finished DB Instance backup</Message>
        <SourceType>db-instance</SourceType>
        <EventCategories>
          <EventCategory>backup</EventCategory>
        </EventCategories>
        <Date>2014-04-21T09:28:38.048Z</Date>
        <SourceIdentifier>my-oracledb1</SourceIdentifier>
      </Event>
    </Events>
  </DescribeEventsResult>
  <ResponseMetadata>
    <RequestId>b7a8cd43-b98c-11d3-a907-5a2c468b9cb0</RequestId>
  </ResponseMetadata>
</DescribeEventsResponse>
```

## See Also
<a name="API_DescribeEvents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeEvents) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeEvents) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeEvents) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeEvents) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeEvents) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeEvents) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeEvents) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeEvents) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeEvents) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeEvents) 