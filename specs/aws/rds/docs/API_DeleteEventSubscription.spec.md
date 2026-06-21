---
id: "@specs/aws/rds/docs/API_DeleteEventSubscription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteEventSubscription"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DeleteEventSubscription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DeleteEventSubscription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteEventSubscription
<a name="API_DeleteEventSubscription"></a>

Deletes an RDS event notification subscription.

## Request Parameters
<a name="API_DeleteEventSubscription_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SubscriptionName **   
The name of the RDS event notification subscription you want to delete.  
Type: String  
Required: Yes

## Response Elements
<a name="API_DeleteEventSubscription_ResponseElements"></a>

The following element is returned by the service.

 ** EventSubscription **   
Contains the results of a successful invocation of the `DescribeEventSubscriptions` action.  
Type: [EventSubscription](API_EventSubscription.md) object

## Errors
<a name="API_DeleteEventSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidEventSubscriptionState **   
This error can occur if someone else is modifying a subscription. You should retry the action.  
HTTP Status Code: 400

 ** SubscriptionNotFound **   
The subscription name does not exist.  
HTTP Status Code: 404

## Examples
<a name="API_DeleteEventSubscription_Examples"></a>

### Example
<a name="API_DeleteEventSubscription_Example_1"></a>

This example illustrates one usage of DeleteEventSubscription.

#### Sample Request
<a name="API_DeleteEventSubscription_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=DeleteEventSubscription
   &SignatureMethod=HmacSHA256 
   &SignatureVersion=4
   &SubscriptionName=EventSubscription04
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140423/us-east-1/rds/aws4_request
   &X-Amz-Date=20140423T203337Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=05aa834e364a9e1a279d44cc955694518fc96fff638c74faa2be45783102e785
```

#### Sample Response
<a name="API_DeleteEventSubscription_Example_1_Response"></a>

```
<DeleteEventSubscriptionResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DeleteEventSubscriptionResult>
    <EventSubscription>
      <Enabled>true</Enabled>
      <CustomerAwsId>803#########</CustomerAwsId>
      <SourceType>db-instance</SourceType>
      <Status>deleting</Status>
      <SourceIdsList>
        <SourceId>mysqldb</SourceId>
      </SourceIdsList>
      <SubscriptionCreationTime>2014-04-22 23:03:19.776</SubscriptionCreationTime>
      <CustSubscriptionId>EventSubscription04</CustSubscriptionId>
      <SnsTopicArn>arn:aws:sns:us-east-1:803#########:myawsuser-RDS</SnsTopicArn>
    </EventSubscription>
  </DeleteEventSubscriptionResult>
  <ResponseMetadata>
    <RequestId>7b4cf02a-ba25-11d3-a691-857dc0addcc9</RequestId>
  </ResponseMetadata>
</DeleteEventSubscriptionResponse>
```

## See Also
<a name="API_DeleteEventSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DeleteEventSubscription) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DeleteEventSubscription) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DeleteEventSubscription) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DeleteEventSubscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DeleteEventSubscription) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DeleteEventSubscription) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DeleteEventSubscription) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DeleteEventSubscription) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DeleteEventSubscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DeleteEventSubscription) 