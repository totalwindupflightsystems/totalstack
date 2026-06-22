---
id: "@specs/aws/docdb/docs/API_DescribeEventSubscriptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeEventSubscriptions"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DescribeEventSubscriptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DescribeEventSubscriptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeEventSubscriptions
<a name="API_DescribeEventSubscriptions"></a>

Lists all the subscription descriptions for a customer account. The description for a subscription includes `SubscriptionName`, `SNSTopicARN`, `CustomerID`, `SourceType`, `SourceID`, `CreationTime`, and `Status`.

If you specify a `SubscriptionName`, lists the description for that subscription.

## Request Parameters
<a name="API_DescribeEventSubscriptions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Filters.Filter.N**   
This parameter is not currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
 The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** SubscriptionName **   
The name of the Amazon DocumentDB event notification subscription that you want to describe.  
Type: String  
Required: No

## Response Elements
<a name="API_DescribeEventSubscriptions_ResponseElements"></a>

The following elements are returned by the service.

 **EventSubscriptionsList.EventSubscription.N**   
A list of event subscriptions.  
Type: Array of [EventSubscription](API_EventSubscription.md) objects

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

## Errors
<a name="API_DescribeEventSubscriptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** SubscriptionNotFound **   
The subscription name does not exist.   
HTTP Status Code: 404

## See Also
<a name="API_DescribeEventSubscriptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/DescribeEventSubscriptions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/DescribeEventSubscriptions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DescribeEventSubscriptions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/DescribeEventSubscriptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DescribeEventSubscriptions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeEventSubscriptions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/DescribeEventSubscriptions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/DescribeEventSubscriptions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/DescribeEventSubscriptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DescribeEventSubscriptions) 