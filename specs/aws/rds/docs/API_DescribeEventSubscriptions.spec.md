---
id: "@specs/aws/rds/docs/API_DescribeEventSubscriptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeEventSubscriptions"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeEventSubscriptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeEventSubscriptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeEventSubscriptions
<a name="API_DescribeEventSubscriptions"></a>

Lists all the subscription descriptions for a customer account. The description for a subscription includes `SubscriptionName`, `SNSTopicARN`, `CustomerID`, `SourceType`, `SourceID`, `CreationTime`, and `Status`.

If you specify a `SubscriptionName`, lists the description for that subscription.

## Request Parameters
<a name="API_DescribeEventSubscriptions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Filters.Filter.N**   
This parameter isn't currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords` .  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** SubscriptionName **   
The name of the RDS event notification subscription you want to describe.  
Type: String  
Required: No

## Response Elements
<a name="API_DescribeEventSubscriptions_ResponseElements"></a>

The following elements are returned by the service.

 **EventSubscriptionsList.EventSubscription.N**   
A list of EventSubscriptions data types.  
Type: Array of [EventSubscription](API_EventSubscription.md) objects

 ** Marker **   
An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

## Errors
<a name="API_DescribeEventSubscriptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** SubscriptionNotFound **   
The subscription name does not exist.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeEventSubscriptions_Examples"></a>

### Example
<a name="API_DescribeEventSubscriptions_Example_1"></a>

This example illustrates one usage of DescribeEventSubscriptions.

#### Sample Request
<a name="API_DescribeEventSubscriptions_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=DescribeEventSubscriptions
   &MaxRecords=100
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140428/us-east-1/rds/aws4_request
   &X-Amz-Date=20140428T161907Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=4208679fe967783a1a149c826199080a066085d5a88227a80c6c0cadb3e8c0d4
```

#### Sample Response
<a name="API_DescribeEventSubscriptions_Example_1_Response"></a>

```
<DescribeEventSubscriptionsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeEventSubscriptionsResult>
    <EventSubscriptionsList>
      <EventSubscription>
        <Enabled>true</Enabled>
        <CustomerAwsId>802#########</CustomerAwsId>
        <SourceType>db-instance</SourceType>
        <Status>active</Status>
        <SourceIdsList>
          <SourceId>mysqldb-rr</SourceId>
          <SourceId>mysqldb</SourceId>
        </SourceIdsList>
        <SubscriptionCreationTime>2014-04-25 22:01:46.327</SubscriptionCreationTime>
        <EventCategoriesList>
          <EventCategory>creation</EventCategory>
          <EventCategory>deletion</EventCategory>
          <EventCategory>configuration change</EventCategory>
          <EventCategory>low storage</EventCategory>
        </EventCategoriesList>
        <CustSubscriptionId>myawsuser-instance</CustSubscriptionId>
        <SnsTopicArn>arn:aws:sns:us-east-1:802#########:myawsuser-RDS</SnsTopicArn>
      </EventSubscription>
      <EventSubscription>
        <Enabled>true</Enabled>
        <CustomerAwsId>802#########</CustomerAwsId>
        <SourceType>db-parameter-group</SourceType>
        <Status>active</Status>
        <SourceIdsList>
          <SourceId>mydbparametergroup00</SourceId>
        </SourceIdsList>
        <SubscriptionCreationTime>2014-04-25 21:44:44.68</SubscriptionCreationTime>
        <EventCategoriesList>
          <EventCategory>configuration change</EventCategory>
        </EventCategoriesList>
        <CustSubscriptionId>myawsuser-paramgrp</CustSubscriptionId>
        <SnsTopicArn>arn:aws:sns:us-east-1:802#########:myawsuser-RDS</SnsTopicArn>
      </EventSubscription>
      <EventSubscription>
        <Enabled>true</Enabled>
        <CustomerAwsId>802#########</CustomerAwsId>
        <SourceType>db-security-group</SourceType>
        <Status>active</Status>
        <SubscriptionCreationTime>2014-04-25 21:43:25.542</SubscriptionCreationTime>
        <EventCategoriesList>
          <EventCategory>configuration change</EventCategory>
          <EventCategory>failure</EventCategory>
        </EventCategoriesList>
        <CustSubscriptionId>myawsuser-secgrp</CustSubscriptionId>
        <SnsTopicArn>arn:aws:sns:us-east-1:802#########:myawsuser-RDS</SnsTopicArn>
      </EventSubscription>
      <EventSubscription>
        <Enabled>true</Enabled>
        <CustomerAwsId>802#########</CustomerAwsId>
        <SourceType>db-snapshot</SourceType>
        <Status>active</Status>
        <SubscriptionCreationTime>2014-04-25 21:41:24.405</SubscriptionCreationTime>
        <EventCategoriesList>
          <EventCategory>creation</EventCategory>
          <EventCategory>failure</EventCategory>
          <EventCategory>deletion</EventCategory>
        </EventCategoriesList>
        <CustSubscriptionId>myawsuser-snapshot</CustSubscriptionId>
        <SnsTopicArn>arn:aws:sns:us-east-1:802#########:myawsuser-RDS</SnsTopicArn>
      </EventSubscription>
    </EventSubscriptionsList>
  </DescribeEventSubscriptionsResult>
  <ResponseMetadata>
    <RequestId>c2c6da4e-bde9-11d3-fe11-33d33a9bb7e3</RequestId>
  </ResponseMetadata>
</DescribeEventSubscriptionsResponse>
```

## See Also
<a name="API_DescribeEventSubscriptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeEventSubscriptions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeEventSubscriptions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeEventSubscriptions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeEventSubscriptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeEventSubscriptions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeEventSubscriptions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeEventSubscriptions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeEventSubscriptions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeEventSubscriptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeEventSubscriptions) 