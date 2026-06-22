---
id: "@specs/aws/redshift/docs/API_DescribeEventCategories"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeEventCategories"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeEventCategories

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeEventCategories
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeEventCategories
<a name="API_DescribeEventCategories"></a>

Displays a list of event categories for all event source types, or for a specified source type. For a list of the event categories and source types, go to [Amazon Redshift Event Notifications](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html).

## Request Parameters
<a name="API_DescribeEventCategories_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SourceType **   
The source type, such as cluster or parameter group, to which the described event categories apply.  
Valid values: cluster, cluster-snapshot, cluster-parameter-group, cluster-security-group, and scheduled-action.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DescribeEventCategories_ResponseElements"></a>

The following element is returned by the service.

 **EventCategoriesMapList.EventCategoriesMap.N**   
A list of event categories descriptions.  
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
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeEventCategories
&SourceType=cluster
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeEventCategories_Example_1_Response"></a>

```
<DescribeEventCategoriesResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeEventCategoriesResult>
    <EventCategoriesMapList>
      <EventCategoriesMap>
        <SourceType>cluster</SourceType>
        <Events>
          <EventInfoMap>
            <Severity>INFO</Severity>
            <EventDescription>Cluster <cluster name> created at <time in UTC>.</EventDescription>
            <EventId>REDSHIFT-EVENT-2000</EventId>
            <EventCategories>
              <EventCategory>management</EventCategory>
            </EventCategories>
          </EventInfoMap>
          <EventInfoMap>
            <Severity>INFO</Severity>
            <EventDescription>Cluster <cluster name> deleted at <time in UTC>.</EventDescription>
            <EventId>REDSHIFT-EVENT-2001</EventId>
            <EventCategories>
              <EventCategory>management</EventCategory>
            </EventCategories>
          </EventInfoMap>
        </Events>
      </EventCategoriesMap>
    </EventCategoriesMapList>
  </DescribeEventCategoriesResult>
  <ResponseMetadata>
    <RequestId>5ad8a6a4-283f-11ea-a940-1b28a85fd753</RequestId>
  </ResponseMetadata>
</DescribeEventCategoriesResponse>
```

## See Also
<a name="API_DescribeEventCategories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeEventCategories) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeEventCategories) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeEventCategories) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeEventCategories) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeEventCategories) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeEventCategories) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeEventCategories) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeEventCategories) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeEventCategories) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeEventCategories) 