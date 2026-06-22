---
id: "@specs/aws/redshift/docs/API_DescribeEventSubscriptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeEventSubscriptions"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeEventSubscriptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeEventSubscriptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeEventSubscriptions
<a name="API_DescribeEventSubscriptions"></a>

Lists descriptions of all the Amazon Redshift event notification subscriptions for a customer account. If you specify a subscription name, lists the description for that subscription.

If you specify both tag keys and tag values in the same request, Amazon Redshift returns all event notification subscriptions that match any combination of the specified keys and values. For example, if you have `owner` and `environment` for tag keys, and `admin` and `test` for tag values, all subscriptions that have any combination of those values are returned.

If both tag keys and values are omitted from the request, subscriptions are returned regardless of whether they have tag keys or values associated with them.

## Request Parameters
<a name="API_DescribeEventSubscriptions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a DescribeEventSubscriptions request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `marker` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.   
Default: `100`   
Constraints: minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** SubscriptionName **   
The name of the Amazon Redshift event notification subscription to be described.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **TagKeys.TagKey.N**   
A tag key or keys for which you want to return all matching event notification subscriptions that are associated with the specified key or keys. For example, suppose that you have subscriptions that are tagged with keys called `owner` and `environment`. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the subscriptions that have either or both of these tag keys associated with them.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **TagValues.TagValue.N**   
A tag value or values for which you want to return all matching event notification subscriptions that are associated with the specified tag value or values. For example, suppose that you have subscriptions that are tagged with values called `admin` and `test`. If you specify both of these tag values in the request, Amazon Redshift returns a response with the subscriptions that have either or both of these tag values associated with them.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DescribeEventSubscriptions_ResponseElements"></a>

The following elements are returned by the service.

 **EventSubscriptionsList.EventSubscription.N**   
A list of event subscriptions.  
Type: Array of [EventSubscription](API_EventSubscription.md) objects

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `Marker` parameter and retrying the command. If the `Marker` field is empty, all response records have been retrieved for the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_DescribeEventSubscriptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

 ** SubscriptionNotFound **   
An Amazon Redshift event notification subscription with the specified name does not exist.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeEventSubscriptions_Examples"></a>

### Example
<a name="API_DescribeEventSubscriptions_Example_1"></a>

This example illustrates one usage of DescribeEventSubscriptions.

#### Sample Request
<a name="API_DescribeEventSubscriptions_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeEventSubscriptions
&SubscriptionName=mysubscription
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeEventSubscriptions_Example_1_Response"></a>

```
<DescribeEventSubscriptionsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeEventSubscriptionsResult>
    <EventSubscriptionsList>
      <EventSubscription>
        <Severity>ERROR</Severity>
        <CustSubscriptionId>mysubscription</CustSubscriptionId>
        <SnsTopicArn>arn:aws:sns:us-east-2:123456789012:MySNStopic</SnsTopicArn>
        <SourceIdsList/>
        <EventCategoriesList/>
        <SubscriptionCreationTime>2019-12-27T00:27:43.748Z</SubscriptionCreationTime>
        <Enabled>true</Enabled>
        <Tags/>
        <Status>active</Status>
        <CustomerAwsId>123456789012</CustomerAwsId>
      </EventSubscription>
    </EventSubscriptionsList>
  </DescribeEventSubscriptionsResult>
  <ResponseMetadata>
    <RequestId>b80f1c37-283f-11ea-9caa-c956bec1ce87</RequestId>
  </ResponseMetadata>
</DescribeEventSubscriptionsResponse>
```

## See Also
<a name="API_DescribeEventSubscriptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeEventSubscriptions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeEventSubscriptions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeEventSubscriptions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeEventSubscriptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeEventSubscriptions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeEventSubscriptions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeEventSubscriptions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeEventSubscriptions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeEventSubscriptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeEventSubscriptions) 