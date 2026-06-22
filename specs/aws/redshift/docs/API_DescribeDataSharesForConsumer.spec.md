---
id: "@specs/aws/redshift/docs/API_DescribeDataSharesForConsumer"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDataSharesForConsumer"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeDataSharesForConsumer

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeDataSharesForConsumer
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDataSharesForConsumer
<a name="API_DescribeDataSharesForConsumer"></a>

Returns a list of datashares where the account identifier being called is a consumer account identifier.

## Request Parameters
<a name="API_DescribeDataSharesForConsumer_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ConsumerArn **   
The Amazon Resource Name (ARN) of the consumer namespace that returns in the list of datashares.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a [DescribeDataSharesForConsumer](#API_DescribeDataSharesForConsumer) request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `marker` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.   
Type: Integer  
Required: No

 ** Status **   
An identifier giving the status of a datashare in the consumer cluster. If this field is specified, Amazon Redshift returns the list of datashares that have the specified status.  
Type: String  
Valid Values: `ACTIVE | AVAILABLE`   
Required: No

## Response Elements
<a name="API_DescribeDataSharesForConsumer_ResponseElements"></a>

The following elements are returned by the service.

 **DataShares.member.N**   
Shows the results of datashares available for consumers.  
Type: Array of [DataShare](API_DataShare.md) objects

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a [DescribeDataSharesForConsumer](#API_DescribeDataSharesForConsumer) request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_DescribeDataSharesForConsumer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidNamespaceFault **   
The namespace isn't valid because the namespace doesn't exist. Provide a valid namespace.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeDataSharesForConsumer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeDataSharesForConsumer) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeDataSharesForConsumer) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeDataSharesForConsumer) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeDataSharesForConsumer) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeDataSharesForConsumer) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeDataSharesForConsumer) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeDataSharesForConsumer) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeDataSharesForConsumer) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeDataSharesForConsumer) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeDataSharesForConsumer) 