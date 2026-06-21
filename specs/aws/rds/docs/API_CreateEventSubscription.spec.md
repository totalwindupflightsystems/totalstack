---
id: "@specs/aws/rds/docs/API_CreateEventSubscription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateEventSubscription"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# CreateEventSubscription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_CreateEventSubscription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateEventSubscription
<a name="API_CreateEventSubscription"></a>

Creates an RDS event notification subscription. This operation requires a topic Amazon Resource Name (ARN) created by either the RDS console, the SNS console, or the SNS API. To obtain an ARN with SNS, you must create a topic in Amazon SNS and subscribe to the topic. The ARN is displayed in the SNS console.

You can specify the type of source (`SourceType`) that you want to be notified of and provide a list of RDS sources (`SourceIds`) that triggers the events. You can also provide a list of event categories (`EventCategories`) for events that you want to be notified of. For example, you can specify `SourceType` = `db-instance`, `SourceIds` = `mydbinstance1`, `mydbinstance2` and `EventCategories` = `Availability`, `Backup`.

If you specify both the `SourceType` and `SourceIds`, such as `SourceType` = `db-instance` and `SourceIds` = `myDBInstance1`, you are notified of all the `db-instance` events for the specified source. If you specify a `SourceType` but do not specify `SourceIds`, you receive notice of the events for that source type for all your RDS sources. If you don't specify either the SourceType or the `SourceIds`, you are notified of events generated from all RDS sources belonging to your customer account.

For more information about subscribing to an event for RDS DB engines, see [ Subscribing to Amazon RDS event notification](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html) in the *Amazon RDS User Guide*.

For more information about subscribing to an event for Aurora DB engines, see [ Subscribing to Amazon RDS event notification](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.Subscribing.html) in the *Amazon Aurora User Guide*.

## Request Parameters
<a name="API_CreateEventSubscription_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SnsTopicArn **   
The Amazon Resource Name (ARN) of the SNS topic created for event notification. SNS automatically creates the ARN when you create a topic and subscribe to it.  
RDS doesn't support FIFO (first in, first out) topics. For more information, see [Message ordering and deduplication (FIFO topics)](https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html) in the *Amazon Simple Notification Service Developer Guide*.
Type: String  
Required: Yes

 ** SubscriptionName **   
The name of the subscription.  
Constraints: The name must be less than 255 characters.  
Type: String  
Required: Yes

 ** Enabled **   
Specifies whether to activate the subscription. If the event notification subscription isn't activated, the subscription is created but not active.  
Type: Boolean  
Required: No

 **EventCategories.EventCategory.N**   
A list of event categories for a particular source type (`SourceType`) that you want to subscribe to. You can see a list of the categories for a given source type in the "Amazon RDS event categories and event messages" section of the [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Messages.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Messages.html) or the [https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.Messages.html](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.Messages.html). You can also see this list by using the `DescribeEventCategories` operation.  
Type: Array of strings  
Required: No

 **SourceIds.SourceId.N**   
The list of identifiers of the event sources for which events are returned. If not specified, then all sources are included in the response. An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens. It can't end with a hyphen or contain two consecutive hyphens.  
Constraints:  
+ If `SourceIds` are supplied, `SourceType` must also be provided.
+ If the source type is a DB instance, a `DBInstanceIdentifier` value must be supplied.
+ If the source type is a DB cluster, a `DBClusterIdentifier` value must be supplied.
+ If the source type is a DB parameter group, a `DBParameterGroupName` value must be supplied.
+ If the source type is a DB security group, a `DBSecurityGroupName` value must be supplied.
+ If the source type is a DB snapshot, a `DBSnapshotIdentifier` value must be supplied.
+ If the source type is a DB cluster snapshot, a `DBClusterSnapshotIdentifier` value must be supplied.
+ If the source type is an RDS Proxy, a `DBProxyName` value must be supplied.
Type: Array of strings  
Required: No

 ** SourceType **   
The type of source that is generating the events. For example, if you want to be notified of events generated by a DB instance, you set this parameter to `db-instance`. For RDS Proxy events, specify `db-proxy`. If this value isn't specified, all events are returned.  
Valid Values:` db-instance | db-cluster | db-parameter-group | db-security-group | db-snapshot | db-cluster-snapshot | db-proxy | zero-etl | custom-engine-version | blue-green-deployment `   
Type: String  
Required: No

 **Tags.Tag.N**   
A list of tags.  
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.   
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateEventSubscription_ResponseElements"></a>

The following element is returned by the service.

 ** EventSubscription **   
Contains the results of a successful invocation of the `DescribeEventSubscriptions` action.  
Type: [EventSubscription](API_EventSubscription.md) object

## Errors
<a name="API_CreateEventSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EventSubscriptionQuotaExceeded **   
You have reached the maximum number of event subscriptions.  
HTTP Status Code: 400

 ** SNSInvalidTopic **   
SNS has responded that there is a problem with the SNS topic specified.  
HTTP Status Code: 400

 ** SNSNoAuthorization **   
You do not have permission to publish to the SNS topic ARN.  
HTTP Status Code: 400

 ** SNSTopicArnNotFound **   
The SNS topic ARN does not exist.  
HTTP Status Code: 404

 ** SourceNotFound **   
The requested source could not be found.  
HTTP Status Code: 404

 ** SubscriptionAlreadyExist **   
The supplied subscription name already exists.  
HTTP Status Code: 400

 ** SubscriptionCategoryNotFound **   
The supplied category does not exist.  
HTTP Status Code: 404

## Examples
<a name="API_CreateEventSubscription_Examples"></a>

### Example
<a name="API_CreateEventSubscription_Example_1"></a>

This example illustrates one usage of CreateEventSubscription.

#### Sample Request
<a name="API_CreateEventSubscription_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=CreateEventSubscription
   &Enabled=true
   &EventCategories.member.1=failure
   &EventCategories.member.2=configuration%20change
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &SnsTopicArn=arn%3Aaws%3Asns%3Aus-east-1%3A802#########%3Amytopic
   &SourceType=db-security-group
   &SubscriptionName=myawsuser-secgrp
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140425/us-east-1/rds/aws4_request
   &X-Amz-Date=20140425T214325Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=7045960f6ab15609571fb05278004256e186b7633ab2a3ae46826d7713e0b461
```

#### Sample Response
<a name="API_CreateEventSubscription_Example_1_Response"></a>

```
<CreateEventSubscriptionResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <CreateEventSubscriptionResult>
    <EventSubscription>
      <SourceType>db-security-group</SourceType>
      <Enabled>true</Enabled>
      <CustomerAwsId>803#########</CustomerAwsId>
      <Status>creating</Status>
      <SubscriptionCreationTime>Fri Apr 25 21:43:25 UTC 2014</SubscriptionCreationTime>
      <EventCategoriesList>
        <EventCategory>configuration change</EventCategory>
        <EventCategory>failure</EventCategory>
      </EventCategoriesList>
      <CustSubscriptionId>myawsuser-secgrp</CustSubscriptionId>
      <SnsTopicArn>arn:aws:sns:us-east-1:802#########:mytopic</SnsTopicArn>
    </EventSubscription>
  </CreateEventSubscriptionResult>
  <ResponseMetadata>
    <RequestId>f15e9dc3-bbb1-11d3-f4c6-37db295f7674</RequestId>
  </ResponseMetadata>
</CreateEventSubscriptionResponse>
```

### Example
<a name="API_CreateEventSubscription_Example_2"></a>

This example illustrates one usage of CreateEventSubscription.

#### Sample Request
<a name="API_CreateEventSubscription_Example_2_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=CreateEventSubscription
   &Enabled=true
   &EventCategories.member.1=creation
   &EventCategories.member.2=deletion
   &EventCategories.member.3=failover
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &SnsTopicArn=arn%3Aaws%3Asns%3Aus-east-1%3A802#########%3Amytopic
   &SourceType=db-instance
   &SubscriptionName=myawsuser-inst
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140429/us-east-1/rds/aws4_request
   &X-Amz-Date=20140429T184410Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=1e1879f20ef3aec07135d69cc192426bf1cc5c42fc9d1acc7726bcd93155fb71
```

#### Sample Response
<a name="API_CreateEventSubscription_Example_2_Response"></a>

```
<CreateEventSubscriptionResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <CreateEventSubscriptionResult>
    <EventSubscription>
      <SourceType>db-instance</SourceType>
      <Enabled>true</Enabled>
      <CustomerAwsId>803#########</CustomerAwsId>
      <Status>creating</Status>
      <SubscriptionCreationTime>Tue Apr 29 18:44:10 UTC 2014</SubscriptionCreationTime>
      <EventCategoriesList>
        <EventCategory>creation</EventCategory>
        <EventCategory>deletion</EventCategory>
        <EventCategory>failover</EventCategory>
      </EventCategoriesList>
      <CustSubscriptionId>myawsuser-inst</CustSubscriptionId>
      <SnsTopicArn>arn:aws:sns:us-east-1:802#########:mytopic</SnsTopicArn>
    </EventSubscription>
  </CreateEventSubscriptionResult>
  <ResponseMetadata>
    <RequestId>30feb307-bebd-11d3-f4c6-37db295f7674</RequestId>
  </ResponseMetadata>
</CreateEventSubscriptionResponse>
```

## See Also
<a name="API_CreateEventSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/CreateEventSubscription) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/CreateEventSubscription) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CreateEventSubscription) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/CreateEventSubscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CreateEventSubscription) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/CreateEventSubscription) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/CreateEventSubscription) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/CreateEventSubscription) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/CreateEventSubscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CreateEventSubscription) 