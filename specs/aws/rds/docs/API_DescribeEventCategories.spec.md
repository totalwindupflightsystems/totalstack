---
id: "@specs/aws/rds/docs/API_DescribeEventCategories"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeEventCategories"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeEventCategories

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeEventCategories
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeEventCategories
<a name="API_DescribeEventCategories"></a>

Displays a list of categories for all event source types, or, if specified, for a specified source type. You can also see this list in the "Amazon RDS event categories and event messages" section of the [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Messages.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Messages.html) or the [https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.Messages.html](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.Messages.html).

## Request Parameters
<a name="API_DescribeEventCategories_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Filters.Filter.N**   
This parameter isn't currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** SourceType **   
The type of source that is generating the events. For RDS Proxy events, specify `db-proxy`.  
Valid Values: `db-instance` \| `db-cluster` \| `db-parameter-group` \| `db-security-group` \| `db-snapshot` \| `db-cluster-snapshot` \| `db-proxy`   
Type: String  
Required: No

## Response Elements
<a name="API_DescribeEventCategories_ResponseElements"></a>

The following element is returned by the service.

 **EventCategoriesMapList.EventCategoriesMap.N**   
A list of `EventCategoriesMap` data types.  
Type: Array of [EventCategoriesMap](API_EventCategoriesMap.md) objects

## Errors
<a name="API_DescribeEventCategories_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeEventCategories_Examples"></a>

### Example
<a name="API_DescribeEventCategories_Example_1"></a>

This example illustrates one usage of DescribeEventCategories.

#### Sample Request
<a name="API_DescribeEventCategories_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
   ?Action=DescribeEventCategories
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140421/us-west-2/rds/aws4_request
   &X-Amz-Date=20140421T194732Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=6e25c542bf96fe24b28c12976ec92d2f856ab1d2a158e21c35441a736e4fde2b
```

#### Sample Response
<a name="API_DescribeEventCategories_Example_1_Response"></a>

```
<DescribeEventCategoriesResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeEventCategoriesResult>
    <EventCategoriesMapList>
      <EventCategoriesMap>
        <SourceType>db-instance</SourceType>
        <EventCategories>
          <EventCategory>backup</EventCategory>
          <EventCategory>recovery</EventCategory>
          <EventCategory>restoration</EventCategory>
          <EventCategory>failover</EventCategory>
          <EventCategory>low storage</EventCategory>
          <EventCategory>maintenance</EventCategory>
          <EventCategory>deletion</EventCategory>
          <EventCategory>availability</EventCategory>
          <EventCategory>configuration change</EventCategory>
          <EventCategory>notification</EventCategory>
          <EventCategory>failure</EventCategory>
          <EventCategory>creation</EventCategory>
        </EventCategories>
      </EventCategoriesMap>
      <EventCategoriesMap>
        <SourceType>db-security-group</SourceType>
        <EventCategories>
          <EventCategory>configuration change</EventCategory>
          <EventCategory>failure</EventCategory>
        </EventCategories>
      </EventCategoriesMap>
      <EventCategoriesMap>
        <SourceType>db-parameter-group</SourceType>
        <EventCategories>
          <EventCategory>configuration change</EventCategory>
        </EventCategories>
      </EventCategoriesMap>
      <EventCategoriesMap>
        <SourceType>db-snapshot</SourceType>
        <EventCategories>
          <EventCategory>deletion</EventCategory>
          <EventCategory>restoration</EventCategory>
          <EventCategory>notification</EventCategory>
          <EventCategory>failure</EventCategory>
          <EventCategory>creation</EventCategory>
        </EventCategories>
      </EventCategoriesMap>
    </EventCategoriesMap>
  </DescribeEventCategoriesResult>
  <ResponseMetadata>
    <RequestId>b79456f2-b98c-11d3-f272-7cd6cce12cc5</RequestId>
  </ResponseMetadata>
</DescribeEventCategoriesResponse>
```

## See Also
<a name="API_DescribeEventCategories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeEventCategories) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeEventCategories) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeEventCategories) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeEventCategories) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeEventCategories) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeEventCategories) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeEventCategories) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeEventCategories) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeEventCategories) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeEventCategories) 