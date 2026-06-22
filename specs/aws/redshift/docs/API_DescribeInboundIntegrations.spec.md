---
id: "@specs/aws/redshift/docs/API_DescribeInboundIntegrations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeInboundIntegrations"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeInboundIntegrations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeInboundIntegrations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeInboundIntegrations
<a name="API_DescribeInboundIntegrations"></a>

Returns a list of inbound integrations.

## Request Parameters
<a name="API_DescribeInboundIntegrations_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** IntegrationArn **   
The Amazon Resource Name (ARN) of the inbound integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^arn:aws[a-z\-]*:.+:[a-z0-9\-]*:[0-9]*:integration:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`   
Required: No

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a [DescribeInboundIntegrations](#API_DescribeInboundIntegrations) request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `marker` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.   
Default: `100`   
Constraints: minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** TargetArn **   
The Amazon Resource Name (ARN) of the target of an inbound integration.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:aws[a-z\-]*:redshift(-serverless)?:[a-z0-9\-]+:[0-9]{12}:(namespace\/|namespace:)[a-z0-9\-]+$`   
Required: No

## Response Elements
<a name="API_DescribeInboundIntegrations_ResponseElements"></a>

The following elements are returned by the service.

 **InboundIntegrations.InboundIntegration.N**   
A list of [InboundIntegration](API_InboundIntegration.md) instances.  
Type: Array of [InboundIntegration](API_InboundIntegration.md) objects

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `Marker` parameter and retrying the command. If the `Marker` field is empty, all response records have been retrieved for the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_DescribeInboundIntegrations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IntegrationNotFoundFault **   
The integration can't be found.  
HTTP Status Code: 404

 ** InvalidNamespaceFault **   
The namespace isn't valid because the namespace doesn't exist. Provide a valid namespace.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeInboundIntegrations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeInboundIntegrations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeInboundIntegrations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeInboundIntegrations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeInboundIntegrations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeInboundIntegrations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeInboundIntegrations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeInboundIntegrations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeInboundIntegrations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeInboundIntegrations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeInboundIntegrations) 