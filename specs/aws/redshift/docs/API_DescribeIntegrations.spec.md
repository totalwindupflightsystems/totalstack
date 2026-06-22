---
id: "@specs/aws/redshift/docs/API_DescribeIntegrations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeIntegrations"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeIntegrations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeIntegrations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeIntegrations
<a name="API_DescribeIntegrations"></a>

Describes one or more zero-ETL or S3 event integrations with Amazon Redshift.

## Request Parameters
<a name="API_DescribeIntegrations_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Filters.DescribeIntegrationsFilter.N**   
A filter that specifies one or more resources to return.  
Type: Array of [DescribeIntegrationsFilter](API_DescribeIntegrationsFilter.md) objects  
Required: No

 ** IntegrationArn **   
The unique identifier of the integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^arn:aws[a-z\-]*:redshift:[a-z0-9\-]*:[0-9]*:integration:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`   
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeIntegrations` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `marker` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.   
Default: `100`   
Constraints: minimum 20, maximum 100.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeIntegrations_ResponseElements"></a>

The following elements are returned by the service.

 **Integrations.Integration.N**   
List of integrations that are described.  
Type: Array of [Integration](API_Integration.md) objects

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `Marker` parameter and retrying the command. If the `Marker` field is empty, all response records have been retrieved for the request.  
Type: String  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_DescribeIntegrations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IntegrationNotFoundFault **   
The integration can't be found.  
HTTP Status Code: 404

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeIntegrations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeIntegrations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeIntegrations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeIntegrations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeIntegrations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeIntegrations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeIntegrations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeIntegrations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeIntegrations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeIntegrations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeIntegrations) 