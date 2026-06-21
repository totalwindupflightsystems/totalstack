---
id: "@specs/aws/rds/docs/API_DescribeDBClusterParameterGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBClusterParameterGroups"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeDBClusterParameterGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeDBClusterParameterGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBClusterParameterGroups
<a name="API_DescribeDBClusterParameterGroups"></a>

Returns a list of `DBClusterParameterGroup` descriptions. If a `DBClusterParameterGroupName` parameter is specified, the list will contain only the description of the specified DB cluster parameter group.

For more information on Amazon Aurora, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide*.

For more information on Multi-AZ DB clusters, see [ Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide*.

## Request Parameters
<a name="API_DescribeDBClusterParameterGroups_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterParameterGroupName **   
The name of a specific DB cluster parameter group to return details for.  
Constraints:  
+ If supplied, must match the name of an existing DBClusterParameterGroup.
Type: String  
Required: No

 **Filters.Filter.N**   
This parameter isn't currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeDBClusterParameterGroups` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeDBClusterParameterGroups_ResponseElements"></a>

The following elements are returned by the service.

 **DBClusterParameterGroups.DBClusterParameterGroup.N**   
A list of DB cluster parameter groups.  
Type: Array of [DBClusterParameterGroup](API_DBClusterParameterGroup.md) objects

 ** Marker **   
An optional pagination token provided by a previous `DescribeDBClusterParameterGroups` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

## Errors
<a name="API_DescribeDBClusterParameterGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBParameterGroupNotFound **   
 `DBParameterGroupName` doesn't refer to an existing DB parameter group.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeDBClusterParameterGroups_Examples"></a>

### Example
<a name="API_DescribeDBClusterParameterGroups_Example_1"></a>

This example illustrates one usage of DescribeDBClusterParameterGroups.

#### Sample Request
<a name="API_DescribeDBClusterParameterGroups_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=DescribeDBClusterParameterGroups
   &MaxRecords=30
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20150318/us-east-1/rds/aws4_request
   &X-Amz-Date=20150318T184307Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=d9922fdf06b86b870c072b896745251ea8b52bad64bf90e30b0e46f1bb488cca
```

#### Sample Response
<a name="API_DescribeDBClusterParameterGroups_Example_1_Response"></a>

```
<DescribeDBClusterParameterGroupsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeDBClusterParameterGroupsResult>
    <DBClusterParameterGroups>
      <DBClusterParameterGroup>
        <DBParameterGroupFamily>aurora5.6</DBParameterGroupFamily>
        <Description>Default cluster parameter group for aurora5.6</Description>
        <DBClusterParameterGroupName>default.aurora5.6</DBClusterParameterGroupName>
      </DBClusterParameterGroup>
      <DBClusterParameterGroup>
        <DBParameterGroupFamily>aurora5.6</DBParameterGroupFamily>
        <Description>Sample group</Description>
        <DBClusterParameterGroupName>samplegroup</DBClusterParameterGroupName>
      </DBClusterParameterGroup>
      <DBClusterParameterGroup>
        <DBParameterGroupFamily>aurora5.6</DBParameterGroupFamily>
        <Description>Custom group</Description>
        <DBClusterParameterGroupName>custom-group</DBClusterParameterGroupName>
      </DBClusterParameterGroup>
    </DBClusterParameterGroups>
  </DescribeDBClusterParameterGroupsResult>
  <ResponseMetadata>
    <RequestId>9e6503d0-cd9e-11e4-ccf9-7528e6a28483</RequestId>
  </ResponseMetadata>
</DescribeDBClusterParameterGroupsResponse>
```

## See Also
<a name="API_DescribeDBClusterParameterGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBClusterParameterGroups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBClusterParameterGroups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBClusterParameterGroups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBClusterParameterGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBClusterParameterGroups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBClusterParameterGroups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBClusterParameterGroups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBClusterParameterGroups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBClusterParameterGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBClusterParameterGroups) 