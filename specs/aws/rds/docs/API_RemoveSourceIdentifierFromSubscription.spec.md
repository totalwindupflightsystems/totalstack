---
id: "@specs/aws/rds/docs/API_RemoveSourceIdentifierFromSubscription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RemoveSourceIdentifierFromSubscription"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# RemoveSourceIdentifierFromSubscription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_RemoveSourceIdentifierFromSubscription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RemoveSourceIdentifierFromSubscription
<a name="API_RemoveSourceIdentifierFromSubscription"></a>

Removes a source identifier from an existing RDS event notification subscription.

## Request Parameters
<a name="API_RemoveSourceIdentifierFromSubscription_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SourceIdentifier **   
The source identifier to be removed from the subscription, such as the **DB instance identifier** for a DB instance or the name of a security group.  
Type: String  
Required: Yes

 ** SubscriptionName **   
The name of the RDS event notification subscription you want to remove a source identifier from.  
Type: String  
Required: Yes

## Response Elements
<a name="API_RemoveSourceIdentifierFromSubscription_ResponseElements"></a>

The following element is returned by the service.

 ** EventSubscription **   
Contains the results of a successful invocation of the `DescribeEventSubscriptions` action.  
Type: [EventSubscription](API_EventSubscription.md) object

## Errors
<a name="API_RemoveSourceIdentifierFromSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** SourceNotFound **   
The requested source could not be found.  
HTTP Status Code: 404

 ** SubscriptionNotFound **   
The subscription name does not exist.  
HTTP Status Code: 404

## Examples
<a name="API_RemoveSourceIdentifierFromSubscription_Examples"></a>

### Example
<a name="API_RemoveSourceIdentifierFromSubscription_Example_1"></a>

This example illustrates one usage of RemoveSourceIdentifierFromSubscription.

#### Sample Request
<a name="API_RemoveSourceIdentifierFromSubscription_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=RemoveSourceIdentifierFromSubscription
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &SourceIdentifier=si-sample
   &SubscriptionName=myawsuser-secgrp
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140428/us-east-1/rds/aws4_request
   &X-Amz-Date=20140428T222718Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=4419f0015657ee120d781849ffdc6642eeafeee42bf1d18c4b2ed8eb732f7bf8
```

#### Sample Response
<a name="API_RemoveSourceIdentifierFromSubscription_Example_1_Response"></a>

```
<RemoveSourceIdentifierFromSubscriptionResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <RemoveSourceIdentifierFromSubscriptionResult>
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
  </RemoveSourceIdentifierFromSubscriptionResult>
  <ResponseMetadata>
    <RequestId>326cdeb9-be23-11d3-91a5-a90441261bc4</RequestId>
  </ResponseMetadata>
</RemoveSourceIdentifierFromSubscriptionResponse>
```

## See Also
<a name="API_RemoveSourceIdentifierFromSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/RemoveSourceIdentifierFromSubscription) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/RemoveSourceIdentifierFromSubscription) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/RemoveSourceIdentifierFromSubscription) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/RemoveSourceIdentifierFromSubscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/RemoveSourceIdentifierFromSubscription) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/RemoveSourceIdentifierFromSubscription) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/RemoveSourceIdentifierFromSubscription) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/RemoveSourceIdentifierFromSubscription) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/RemoveSourceIdentifierFromSubscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/RemoveSourceIdentifierFromSubscription) 