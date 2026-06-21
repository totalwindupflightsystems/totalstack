---
id: "@specs/aws/rds/docs/API_DescribeDBParameterGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBParameterGroups"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeDBParameterGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeDBParameterGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBParameterGroups
<a name="API_DescribeDBParameterGroups"></a>

Returns a list of `DBParameterGroup` descriptions. If a `DBParameterGroupName` is specified, the list will contain only the description of the specified DB parameter group.

## Request Parameters
<a name="API_DescribeDBParameterGroups_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBParameterGroupName **   
The name of a specific DB parameter group to return details for.  
Constraints:  
+ If supplied, must match the name of an existing DBClusterParameterGroup.
Type: String  
Required: No

 **Filters.Filter.N**   
This parameter isn't currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeDBParameterGroups` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeDBParameterGroups_ResponseElements"></a>

The following elements are returned by the service.

 **DBParameterGroups.DBParameterGroup.N**   
A list of `DBParameterGroup` instances.  
Type: Array of [DBParameterGroup](API_DBParameterGroup.md) objects

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

## Errors
<a name="API_DescribeDBParameterGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBParameterGroupNotFound **   
 `DBParameterGroupName` doesn't refer to an existing DB parameter group.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeDBParameterGroups_Examples"></a>

### Example
<a name="API_DescribeDBParameterGroups_Example_1"></a>

This example illustrates one usage of DescribeDBParameterGroups.

#### Sample Request
<a name="API_DescribeDBParameterGroups_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
   ?Action=DescribeDBParameterGroups
   &DBParameterGroupName=mysql-logs
   &MaxRecords=100
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140421/us-west-2/rds/aws4_request
   &X-Amz-Date=20140421T194732Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=e2753df1cb019f212057b51e8a2ac16dae05b344063355b195b560ef6e76661a
```

#### Sample Response
<a name="API_DescribeDBParameterGroups_Example_1_Response"></a>

```
<DescribeDBParameterGroupsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeDBParameterGroupsResult>
    <DBParameterGroups>
      <DBParameterGroup>
        <DBParameterGroupFamily>mysql5.1</DBParameterGroupFamily>
        <Description>Default parameter group for mysql5.1</Description>
        <DBParameterGroupName>default.mysql5.1</DBParameterGroupName>
      </DBParameterGroup>
      <DBParameterGroup>
        <DBParameterGroupFamily>mysql5.5</DBParameterGroupFamily>
        <Description>Default parameter group for mysql5.5</Description>
        <DBParameterGroupName>default.mysql5.5</DBParameterGroupName>
      </DBParameterGroup>
      <DBParameterGroup>
        <DBParameterGroupFamily>mysql5.6</DBParameterGroupFamily>
        <Description>Default parameter group for mysql5.6</Description>
        <DBParameterGroupName>default.mysql5.6</DBParameterGroupName>
      </DBParameterGroup>
    </DBParameterGroups>
  </DescribeDBParameterGroupsResult>
  <ResponseMetadata>
    <RequestId>b75d527a-b98c-11d3-f272-7cd6cce12cc5</RequestId>
  </ResponseMetadata>
</DescribeDBParameterGroupsResponse>
```

## See Also
<a name="API_DescribeDBParameterGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBParameterGroups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBParameterGroups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBParameterGroups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBParameterGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBParameterGroups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBParameterGroups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBParameterGroups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBParameterGroups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBParameterGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBParameterGroups) 