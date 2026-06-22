---
id: "@specs/aws/redshift/docs/API_DescribeClusterSubnetGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeClusterSubnetGroups"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeClusterSubnetGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeClusterSubnetGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeClusterSubnetGroups
<a name="API_DescribeClusterSubnetGroups"></a>

Returns one or more cluster subnet group objects, which contain metadata about your cluster subnet groups. By default, this operation returns information about all cluster subnet groups that are defined in your AWS account.

If you specify both tag keys and tag values in the same request, Amazon Redshift returns all subnet groups that match any combination of the specified keys and values. For example, if you have `owner` and `environment` for tag keys, and `admin` and `test` for tag values, all subnet groups that have any combination of those values are returned.

If both tag keys and values are omitted from the request, subnet groups are returned regardless of whether they have tag keys or values associated with them.

## Request Parameters
<a name="API_DescribeClusterSubnetGroups_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterSubnetGroupName **   
The name of the cluster subnet group for which information is requested.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a [DescribeClusterSubnetGroups](#API_DescribeClusterSubnetGroups) request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `marker` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.   
Default: `100`   
Constraints: minimum 20, maximum 100.  
Type: Integer  
Required: No

 **TagKeys.TagKey.N**   
A tag key or keys for which you want to return all matching cluster subnet groups that are associated with the specified key or keys. For example, suppose that you have subnet groups that are tagged with keys called `owner` and `environment`. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the subnet groups that have either or both of these tag keys associated with them.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **TagValues.TagValue.N**   
A tag value or values for which you want to return all matching cluster subnet groups that are associated with the specified tag value or values. For example, suppose that you have subnet groups that are tagged with values called `admin` and `test`. If you specify both of these tag values in the request, Amazon Redshift returns a response with the subnet groups that have either or both of these tag values associated with them.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DescribeClusterSubnetGroups_ResponseElements"></a>

The following elements are returned by the service.

 **ClusterSubnetGroups.ClusterSubnetGroup.N**   
A list of [ClusterSubnetGroup](API_ClusterSubnetGroup.md) instances.   
Type: Array of [ClusterSubnetGroup](API_ClusterSubnetGroup.md) objects

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `Marker` parameter and retrying the command. If the `Marker` field is empty, all response records have been retrieved for the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_DescribeClusterSubnetGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterSubnetGroupNotFoundFault **   
The cluster subnet group name does not refer to an existing cluster subnet group.  
HTTP Status Code: 400

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

## Examples
<a name="API_DescribeClusterSubnetGroups_Examples"></a>

### Example
<a name="API_DescribeClusterSubnetGroups_Example_1"></a>

This example illustrates one usage of DescribeClusterSubnetGroups.

#### Sample Request
<a name="API_DescribeClusterSubnetGroups_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeClusterSubnetGroups
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeClusterSubnetGroups_Example_1_Response"></a>

```
<DescribeClusterSubnetGroupsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeClusterSubnetGroupsResult>
    <ClusterSubnetGroups>
      <ClusterSubnetGroup>
        <VpcId>vpc-a1abc1a1</VpcId>
        <Description>default</Description>
        <Subnets>
          <Subnet>
            <SubnetStatus>Active</SubnetStatus>
            <SubnetIdentifier>subnet-a1b23aba</SubnetIdentifier>
            <SubnetAvailabilityZone>
              <Name>us-east-2a</Name>
            </SubnetAvailabilityZone>
          </Subnet>
          <Subnet>
            <SubnetStatus>Active</SubnetStatus>
            <SubnetIdentifier>subnet-a1b23abb</SubnetIdentifier>
            <SubnetAvailabilityZone>
              <Name>us-east-2b</Name>
            </SubnetAvailabilityZone>
          </Subnet>
          <Subnet>
            <SubnetStatus>Active</SubnetStatus>
            <SubnetIdentifier>subnet-a1b23abc</SubnetIdentifier>
            <SubnetAvailabilityZone>
              <Name>us-east-2c</Name>
            </SubnetAvailabilityZone>
          </Subnet>
        </Subnets>
        <ClusterSubnetGroupName>default</ClusterSubnetGroupName>
        <SubnetGroupStatus>Complete</SubnetGroupStatus>
        <Tags/>
      </ClusterSubnetGroup>
    </ClusterSubnetGroups>
  </DescribeClusterSubnetGroupsResult>
  <ResponseMetadata>
    <RequestId>29fd403c-2832-11ea-8397-219d1980588b</RequestId>
  </ResponseMetadata>
</DescribeClusterSubnetGroupsResponse>
```

## See Also
<a name="API_DescribeClusterSubnetGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeClusterSubnetGroups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeClusterSubnetGroups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeClusterSubnetGroups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeClusterSubnetGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeClusterSubnetGroups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeClusterSubnetGroups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeClusterSubnetGroups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeClusterSubnetGroups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeClusterSubnetGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeClusterSubnetGroups) 