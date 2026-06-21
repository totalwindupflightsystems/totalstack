---
id: "@specs/aws/rds/docs/API_DescribeIntegrations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeIntegrations"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeIntegrations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeIntegrations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeIntegrations
<a name="API_DescribeIntegrations"></a>

Describe one or more zero-ETL integrations with Amazon Redshift.

## Request Parameters
<a name="API_DescribeIntegrations_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Filters.Filter.N**   
A filter that specifies one or more resources to return.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** IntegrationIdentifier **   
The unique identifier of the integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9_:\-\/]+`   
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeIntegrations` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 340.  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeIntegrations_ResponseElements"></a>

The following elements are returned by the service.

 **Integrations.Integration.N**   
A list of integrations.  
Type: Array of [Integration](API_Integration.md) objects

 ** Marker **   
A pagination token that can be used in a later `DescribeIntegrations` request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 340.

## Errors
<a name="API_DescribeIntegrations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IntegrationNotFoundFault **   
The specified integration could not be found.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeIntegrations_Examples"></a>

### Example
<a name="API_DescribeIntegrations_Example_1"></a>

This example illustrates one usage of DescribeIntegrations.

#### Sample Request
<a name="API_DescribeIntegrations_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=DescribeIntegration
   &IntegrationIdentifier=f30acbd8-aaab-4c3c-afb5-09d51d041037
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20141031/us-east-1/rds/aws4_request
   &X-Amz-Date=20230110T005253Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=8a684aebe6d5219bb3572316a341963324d6ef339bd0dcfa5854f1a01d401214
```

#### Sample Response
<a name="API_DescribeIntegrations_Example_1_Response"></a>

```
<DescribeIntegrationsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
    <DescribeIntegrationsResult>
        <Integrations>
            <Integration>
                <SourceArn>arn:aws:rds:us-east-1:123456789012:cluster:serverless-source-cluster</SourceArn>
                <IntegrationName>my-integration</IntegrationName>
                <IntegrationCreateTime>2023-12-14T00:15:21.358Z</IntegrationCreateTime>
                <IntegrationArn>arn:aws:rds:us-east-1:123456789012:integration:f30acbd8-aaab-4c3c-afb5-09d51d041037</IntegrationArn>
                <TargetArn>arn:aws:redshift-serverless:us-east-1:123456789012:namespace/0844171c-1e01-4d9f-be52-89e6c44083e5</TargetArn>
                <Tags/>
                <CreateTime>2023-12-14T00:15:21.358Z</CreateTime>
                <KMSKeyId>arn:aws:kms:us-east-1:211223847500:key/eda7134d-cd39-4af1-b62b-ad2415b6bccc</KMSKeyId>
                <Status>creating</Status>
            </Integration>
        </Integrations>
    </DescribeIntegrationsResult>
    <ResponseMetadata>
        <RequestId>6e131503-e920-4c3d-b934-a401a69c3b24</RequestId>
    </ResponseMetadata>
</DescribeIntegrationsResponse>
```

## See Also
<a name="API_DescribeIntegrations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeIntegrations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeIntegrations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeIntegrations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeIntegrations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeIntegrations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeIntegrations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeIntegrations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeIntegrations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeIntegrations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeIntegrations) 