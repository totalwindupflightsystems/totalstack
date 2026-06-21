---
id: "@specs/aws/rds/docs/API_DescribeSourceRegions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeSourceRegions"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeSourceRegions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeSourceRegions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeSourceRegions
<a name="API_DescribeSourceRegions"></a>

Returns a list of the source AWS Regions where the current AWS Region can create a read replica, copy a DB snapshot from, or replicate automated backups from.

Use this operation to determine whether cross-Region features are supported between other Regions and your current Region. This operation supports pagination.

To return information about the Regions that are enabled for your account, or all Regions, use the EC2 operation `DescribeRegions`. For more information, see [ DescribeRegions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRegions.html) in the *Amazon EC2 API Reference*.

## Request Parameters
<a name="API_DescribeSourceRegions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Filters.Filter.N**   
This parameter isn't currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeSourceRegions` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** RegionName **   
The source AWS Region name. For example, `us-east-1`.  
Constraints:  
+ Must specify a valid AWS Region name.
Type: String  
Required: No

## Response Elements
<a name="API_DescribeSourceRegions_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

 **SourceRegions.SourceRegion.N**   
A list of `SourceRegion` instances that contains each source AWS Region that the current AWS Region can get a read replica or a DB snapshot from.  
Type: Array of [SourceRegion](API_SourceRegion.md) objects

## Errors
<a name="API_DescribeSourceRegions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeSourceRegions_Examples"></a>

### Example
<a name="API_DescribeSourceRegions_Example_1"></a>

This example illustrates one usage of DescribeSourceRegions.

#### Sample Request
<a name="API_DescribeSourceRegions_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=DescribeSourceRegions
   &MaxRecords=10
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140429/us-east-1/rds/aws4_request
   &X-Amz-Date=20140429T175351Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=9164337efa99caf850e874a1cb7ef62f3cea29d0b448b9e0e7c53b288ddffed2
```

#### Sample Response
<a name="API_DescribeSourceRegions_Example_1_Response"></a>

```
<DescribeSourceRegionsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeSourceRegionsResult>       
    <SourceRegions>
      <SourceRegion>
        <RegionName>ap-northeast-1</RegionName>
        <EndPoint>https://rds.ap-northeast-1.amazonaws.com</EndPoint>
        <Status>available</Status>       
      </SourceRegion>
      <SourceRegion>
        <RegionName>ap-southeast-2</RegionName>
        <EndPoint>https://rds.ap-southeast-2.amazonaws.com</EndPoint>
        <Status>available</Status>       
      </SourceRegion>
    </SourceRegions>
  </DescribeSourceRegionsResult>
  <ResponseMetadata>
    <RequestId>01b2685a-b978-11d3-f272-7cd6cce12cc5</RequestId>
  </ResponseMetadata>
</DescribeSourceRegionsResponse>
```

## See Also
<a name="API_DescribeSourceRegions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeSourceRegions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeSourceRegions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeSourceRegions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeSourceRegions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeSourceRegions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeSourceRegions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeSourceRegions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeSourceRegions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeSourceRegions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeSourceRegions) 