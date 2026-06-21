---
id: "@specs/aws/rds/docs/API_DescribeDBClusterParameters"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBClusterParameters"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeDBClusterParameters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeDBClusterParameters
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBClusterParameters
<a name="API_DescribeDBClusterParameters"></a>

Returns the detailed parameter list for a particular DB cluster parameter group.

For more information on Amazon Aurora, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide*.

For more information on Multi-AZ DB clusters, see [ Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide*.

## Request Parameters
<a name="API_DescribeDBClusterParameters_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterParameterGroupName **   
The name of a specific DB cluster parameter group to return parameter details for.  
Constraints:  
+ If supplied, must match the name of an existing DBClusterParameterGroup.
Type: String  
Required: Yes

 **Filters.Filter.N**   
A filter that specifies one or more DB cluster parameters to describe.  
The only supported filter is `parameter-name`. The results list only includes information about the DB cluster parameters with these names.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeDBClusterParameters` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** Source **   
A specific source to return parameters for.  
Valid Values:  
+  `engine-default` 
+  `system` 
+  `user` 
Type: String  
Required: No

## Response Elements
<a name="API_DescribeDBClusterParameters_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
An optional pagination token provided by a previous `DescribeDBClusterParameters` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

 **Parameters.Parameter.N**   
Provides a list of parameters for the DB cluster parameter group.  
Type: Array of [Parameter](API_Parameter.md) objects

## Errors
<a name="API_DescribeDBClusterParameters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBParameterGroupNotFound **   
 `DBParameterGroupName` doesn't refer to an existing DB parameter group.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeDBClusterParameters_Examples"></a>

### Example
<a name="API_DescribeDBClusterParameters_Example_1"></a>

This example illustrates one usage of DescribeDBClusterParameters.

#### Sample Request
<a name="API_DescribeDBClusterParameters_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
    ?Action=DescribeDBClusterParameters
    &DBClusterParameterGroupName=default.aurora5.6
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20151231/us-west-2/rds/aws4_request
    &X-Amz-Date=20151231T225813Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=cf8b9ab9c4a36bbb5f5043209b1985784a226d132ed61a5c35163c40506e83f7
```

#### Sample Response
<a name="API_DescribeDBClusterParameters_Example_1_Response"></a>

```
<DescribeDBClusterParametersResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeDBClusterParametersResult>
    <Parameters>
      <Parameter>
        <ApplyMethod>pending-reboot</ApplyMethod>
        <DataType>integer</DataType>
        <Source>engine-default</Source>
        <IsModifiable>true</IsModifiable>
        <Description>Intended for use with master-to-master replication, and can be used to control the operation of AUTO_INCREMENT columns</Description>
        <ApplyType>dynamic</ApplyType>
        <AllowedValues>1-65535</AllowedValues>
        <ParameterName>auto_increment_increment</ParameterName>
      </Parameter>
      <Parameter>
        <ApplyMethod>pending-reboot</ApplyMethod>
        <DataType>integer</DataType>
        <Source>engine-default</Source>
        <IsModifiable>true</IsModifiable>
        <Description>Determines the starting point for the AUTO_INCREMENT column value</Description>
        <ApplyType>dynamic</ApplyType>
        <AllowedValues>1-65535</AllowedValues>
        <ParameterName>auto_increment_offset</ParameterName>
      </Parameter>
      <Parameter>
        <ApplyMethod>pending-reboot</ApplyMethod>
        <DataType>string</DataType>
        <Source>engine-default</Source>
        <IsModifiable>true</IsModifiable>
        <Description>When enabled, this variable causes the master to write a checksum for each event in the binary log.</Description>
        <ApplyType>dynamic</ApplyType>
        <AllowedValues>NONE,CRC32</AllowedValues>
        <ParameterName>binlog_checksum</ParameterName>
      </Parameter>
      <Parameter>
        <ParameterValue>OFF</ParameterValue>
        <ApplyMethod>pending-reboot</ApplyMethod>
        <DataType>string</DataType>
        <Source>system</Source>
        <IsModifiable>true</IsModifiable>
        <Description>Binary logging format for replication</Description>
        <ApplyType>dynamic</ApplyType>
        <AllowedValues>ROW,STATEMENT,MIXED,OFF</AllowedValues>
        <ParameterName>binlog_format</ParameterName>
      </Parameter>
      <Parameter>
        <ApplyMethod>pending-reboot</ApplyMethod>
        <DataType>string</DataType>
        <Source>engine-default</Source>
        <IsModifiable>false</IsModifiable>
        <Description>Whether the server logs full or minimal rows with row-based replication.</Description>
        <ApplyType>dynamic</ApplyType>
        <AllowedValues>full,minimal,noblob</AllowedValues>
        <ParameterName>binlog_row_image</ParameterName>
      </Parameter>
    </Parameters>
  </DescribeDBClusterParametersResult>
  <ResponseMetadata>
    <RequestId>c4e42d91-cb92-11e5-895a-99e063757579</RequestId>
  </ResponseMetadata>
</DescribeDBClusterParametersResponse>
```

## See Also
<a name="API_DescribeDBClusterParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBClusterParameters) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBClusterParameters) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBClusterParameters) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBClusterParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBClusterParameters) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBClusterParameters) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBClusterParameters) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBClusterParameters) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBClusterParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBClusterParameters) 