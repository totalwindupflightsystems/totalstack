---
id: "@specs/aws/rds/docs/API_AddSourceIdentifierToSubscription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AddSourceIdentifierToSubscription"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# AddSourceIdentifierToSubscription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_AddSourceIdentifierToSubscription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AddSourceIdentifierToSubscription
<a name="API_AddSourceIdentifierToSubscription"></a>

Adds a source identifier to an existing RDS event notification subscription.

## Request Parameters
<a name="API_AddSourceIdentifierToSubscription_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SourceIdentifier **   
The identifier of the event source to be added.  
Constraints:  
+ If the source type is a DB instance, a `DBInstanceIdentifier` value must be supplied.
+ If the source type is a DB cluster, a `DBClusterIdentifier` value must be supplied.
+ If the source type is a DB parameter group, a `DBParameterGroupName` value must be supplied.
+ If the source type is a DB security group, a `DBSecurityGroupName` value must be supplied.
+ If the source type is a DB snapshot, a `DBSnapshotIdentifier` value must be supplied.
+ If the source type is a DB cluster snapshot, a `DBClusterSnapshotIdentifier` value must be supplied.
+ If the source type is an RDS Proxy, a `DBProxyName` value must be supplied.
Type: String  
Required: Yes

 ** SubscriptionName **   
The name of the RDS event notification subscription you want to add a source identifier to.  
Type: String  
Required: Yes

## Response Elements
<a name="API_AddSourceIdentifierToSubscription_ResponseElements"></a>

The following element is returned by the service.

 ** EventSubscription **   
Contains the results of a successful invocation of the `DescribeEventSubscriptions` action.  
Type: [EventSubscription](API_EventSubscription.md) object

## Errors
<a name="API_AddSourceIdentifierToSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** SourceNotFound **   
The requested source could not be found.  
HTTP Status Code: 404

 ** SubscriptionNotFound **   
The subscription name does not exist.  
HTTP Status Code: 404

## Examples
<a name="API_AddSourceIdentifierToSubscription_Examples"></a>

### Example
<a name="API_AddSourceIdentifierToSubscription_Example_1"></a>

This example illustrates one usage of AddSourceIdentifierToSubscription.

#### Sample Request
<a name="API_AddSourceIdentifierToSubscription_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=AddSourceIdentifierToSubscription
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &SourceIdentifier=mysqldb
   &SubscriptionName=EventSubscription04
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140422/us-east-1/rds/aws4_request
   &X-Amz-Date=20140422T230442Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=347d5e788e809cd06c50214b12750a3c39716bf65b239bb6f7ee8ff5374e2df9
```

#### Sample Response
<a name="API_AddSourceIdentifierToSubscription_Example_1_Response"></a>

```
<AddSourceIdentifierToSubscriptionResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <AddSourceIdentifierToSubscriptionResult>
    <EventSubscription>
      <SourceType>db-instance</SourceType>
      <Enabled>true</Enabled>
      <CustomerAwsId>803#########</CustomerAwsId>
      <Status>modifying</Status>
      <SourceIdsList>
        <SourceId>mysqldb</SourceId>
      </SourceIdsList>
      <SubscriptionCreationTime>2014-04-22 23:03:19.776</SubscriptionCreationTime>
      <EventCategoriesList>
        <EventCategory>creation</EventCategory>
        <EventCategory>deletion</EventCategory>
      </EventCategoriesList>
      <CustSubscriptionId>EventSubscription04</CustSubscriptionId>
      <SnsTopicArn>arn:aws:sns:us-east-1:803#########:mytopic</SnsTopicArn>
    </EventSubscription>
  </AddSourceIdentifierToSubscriptionResult>
  <ResponseMetadata>
    <RequestId>6c05f0b0-bf71-11d3-f4c6-37db295f7674</RequestId>
  </ResponseMetadata>
</AddSourceIdentifierToSubscriptionResponse>
```

## See Also
<a name="API_AddSourceIdentifierToSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/AddSourceIdentifierToSubscription) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/AddSourceIdentifierToSubscription) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/AddSourceIdentifierToSubscription) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/AddSourceIdentifierToSubscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/AddSourceIdentifierToSubscription) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/AddSourceIdentifierToSubscription) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/AddSourceIdentifierToSubscription) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/AddSourceIdentifierToSubscription) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/AddSourceIdentifierToSubscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/AddSourceIdentifierToSubscription) 