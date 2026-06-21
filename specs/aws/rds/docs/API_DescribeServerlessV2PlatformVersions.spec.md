---
id: "@specs/aws/rds/docs/API_DescribeServerlessV2PlatformVersions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeServerlessV2PlatformVersions"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeServerlessV2PlatformVersions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeServerlessV2PlatformVersions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeServerlessV2PlatformVersions
<a name="API_DescribeServerlessV2PlatformVersions"></a>

Describes the properties of specific platform versions for Aurora Serverless v2.

## Request Parameters
<a name="API_DescribeServerlessV2PlatformVersions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DefaultOnly **   
Specifies whether to return only the default platform versions for each engine. The default platform version is the version used for new DB clusters.  
Type: Boolean  
Required: No

 ** Engine **   
The database engine to return platform version details for.  
Valid Values:  
+  `aurora-mysql` 
+  `aurora-postgresql` 
Type: String  
Required: No

 **Filters.Filter.N**   
This parameter isn't currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** IncludeAll **   
Specifies whether to also include platform versions which are no longer in use.  
Type: Boolean  
Required: No

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more than the `MaxRecords` value is available, a pagination token called a marker is included in the response so you can retrieve the remaining results.  
Default: 20  
Constraints: Minimum 1, maximum 200.  
Type: Integer  
Required: No

 ** ServerlessV2PlatformVersion **   
A specific platform version to return details for.  
Example: `3`   
Type: String  
Required: No

## Response Elements
<a name="API_DescribeServerlessV2PlatformVersions_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

 **ServerlessV2PlatformVersions.member.N**   
A list of `ServerlessV2PlatformVersionInfo` elements.  
Type: Array of [ServerlessV2PlatformVersionInfo](API_ServerlessV2PlatformVersionInfo.md) objects

## Errors
<a name="API_DescribeServerlessV2PlatformVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeServerlessV2PlatformVersions_Examples"></a>

### Example
<a name="API_DescribeServerlessV2PlatformVersions_Example_1"></a>

This example illustrates one usage of DescribeServerlessV2PlatformVersions.

#### Sample Request
<a name="API_DescribeServerlessV2PlatformVersions_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
    ?Action=DescribeServerlessV2PlatformVersions
    &MaxRecords=3
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20260331/us-east-1/rds/aws4_request
    &X-Amz-Date=20260331T003734Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=a9be10ebb18697cfb30621749934561405d97a3e836a749e92080dda950dbdfb
```

#### Sample Response
<a name="API_DescribeServerlessV2PlatformVersions_Example_1_Response"></a>

```
<DescribeServerlessV2PlatformVersionsResponse>
  <DescribeServerlessV2PlatformVersionsResult>
    <ServerlessV2PlatformVersions>
      <member>
        <IsDefault>true</IsDefault>
        <ServerlessV2PlatformVersionDescription>
          Version 4 offering scaling up to 256 ACUs, and performance improvement up to 30% compared to version 3
        </ServerlessV2PlatformVersionDescription>
        <Engine>aurora-postgresql</Engine>
        <ServerlessV2FeaturesSupport>
        <MaxCapacity>256.0</MaxCapacity>
        <MinCapacity>0.0</MinCapacity>
        </ServerlessV2FeaturesSupport>
        <ServerlessV2PlatformVersion>4</ServerlessV2PlatformVersion>
        <Status>enabled</Status>
      </member>
      <member>
        <IsDefault>false</IsDefault>
        <ServerlessV2PlatformVersionDescription>
          Version 3 offering scaling up to 256 ACUs, and performance improvement up to 30% compared to version 2
        </ServerlessV2PlatformVersionDescription>
        <Engine>aurora-postgresql</Engine>
        <ServerlessV2FeaturesSupport>
        <MaxCapacity>256.0</MaxCapacity>
        <MinCapacity>0.0</MinCapacity>
        </ServerlessV2FeaturesSupport>
        <ServerlessV2PlatformVersion>3</ServerlessV2PlatformVersion>
        <Status>enabled</Status>
      </member>
      <member>
        <IsDefault>false</IsDefault>
        <ServerlessV2PlatformVersionDescription>
          Version 2 offering scaling up to 256 ACUs
        </ServerlessV2PlatformVersionDescription>
        <Engine>aurora-postgresql</Engine>
        <ServerlessV2FeaturesSupport>
        <MaxCapacity>256.0</MaxCapacity>
        <MinCapacity>0.0</MinCapacity>
        </ServerlessV2FeaturesSupport>
        <ServerlessV2PlatformVersion>2</ServerlessV2PlatformVersion>
        <Status>enabled</Status>
      </member>
    </ServerlessV2PlatformVersions>
    <Marker>dGhpcyBpcyBhbiBleGFtcGxlIG1hcmtlcg==</Marker>
  </DescribeServerlessV2PlatformVersionsResult>
  <ResponseMetadata>
    <RequestId>a1da1a67-9f9a-43d0-975c-5800dc1b1f59</RequestId>
  </ResponseMetadata>
</DescribeServerlessV2PlatformVersionsResponse>
```

## See Also
<a name="API_DescribeServerlessV2PlatformVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeServerlessV2PlatformVersions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeServerlessV2PlatformVersions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeServerlessV2PlatformVersions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeServerlessV2PlatformVersions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeServerlessV2PlatformVersions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeServerlessV2PlatformVersions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeServerlessV2PlatformVersions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeServerlessV2PlatformVersions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeServerlessV2PlatformVersions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeServerlessV2PlatformVersions) 