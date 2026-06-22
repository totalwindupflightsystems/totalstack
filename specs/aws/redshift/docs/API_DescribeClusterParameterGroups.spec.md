---
id: "@specs/aws/redshift/docs/API_DescribeClusterParameterGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeClusterParameterGroups"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeClusterParameterGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeClusterParameterGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeClusterParameterGroups
<a name="API_DescribeClusterParameterGroups"></a>

Returns a list of Amazon Redshift parameter groups, including parameter groups you created and the default parameter group. For each parameter group, the response includes the parameter group name, description, and parameter group family name. You can optionally specify a name to retrieve the description of a specific parameter group.

 For more information about parameters and parameter groups, go to [Amazon Redshift Parameter Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) in the *Amazon Redshift Cluster Management Guide*.

If you specify both tag keys and tag values in the same request, Amazon Redshift returns all parameter groups that match any combination of the specified keys and values. For example, if you have `owner` and `environment` for tag keys, and `admin` and `test` for tag values, all parameter groups that have any combination of those values are returned.

If both tag keys and values are omitted from the request, parameter groups are returned regardless of whether they have tag keys or values associated with them.

## Request Parameters
<a name="API_DescribeClusterParameterGroups_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a [DescribeClusterParameterGroups](#API_DescribeClusterParameterGroups) request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `marker` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.   
Default: `100`   
Constraints: minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** ParameterGroupName **   
The name of a specific parameter group for which to return details. By default, details about all parameter groups and the default parameter group are returned.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **TagKeys.TagKey.N**   
A tag key or keys for which you want to return all matching cluster parameter groups that are associated with the specified key or keys. For example, suppose that you have parameter groups that are tagged with keys called `owner` and `environment`. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the parameter groups that have either or both of these tag keys associated with them.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **TagValues.TagValue.N**   
A tag value or values for which you want to return all matching cluster parameter groups that are associated with the specified tag value or values. For example, suppose that you have parameter groups that are tagged with values called `admin` and `test`. If you specify both of these tag values in the request, Amazon Redshift returns a response with the parameter groups that have either or both of these tag values associated with them.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DescribeClusterParameterGroups_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `Marker` parameter and retrying the command. If the `Marker` field is empty, all response records have been retrieved for the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.

 **ParameterGroups.ClusterParameterGroup.N**   
A list of [ClusterParameterGroup](API_ClusterParameterGroup.md) instances. Each instance describes one cluster parameter group.   
Type: Array of [ClusterParameterGroup](API_ClusterParameterGroup.md) objects

## Errors
<a name="API_DescribeClusterParameterGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterParameterGroupNotFound **   
The parameter group name does not refer to an existing parameter group.  
HTTP Status Code: 404

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

## Examples
<a name="API_DescribeClusterParameterGroups_Examples"></a>

### Example
<a name="API_DescribeClusterParameterGroups_Example_1"></a>

This example illustrates one usage of DescribeClusterParameterGroups.

#### Sample Request
<a name="API_DescribeClusterParameterGroups_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeClusterParameterGroups
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeClusterParameterGroups_Example_1_Response"></a>

```
<DescribeClusterParameterGroupsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeClusterParameterGroupsResult>
    <ParameterGroups>
      <ClusterParameterGroup>
        <ParameterGroupName>default.redshift-1.0</ParameterGroupName>
        <Description>Default parameter group for redshift-1.0</Description>
        <ParameterGroupFamily>redshift-1.0</ParameterGroupFamily>
        <Tags/>
      </ClusterParameterGroup>
      <ClusterParameterGroup>
        <ParameterGroupName>myclusterparametergroup</ParameterGroupName>
        <Description>My first cluster parameter group</Description>
        <ParameterGroupFamily>redshift-1.0</ParameterGroupFamily>
        <Tags/>
      </ClusterParameterGroup>
    </ParameterGroups>
  </DescribeClusterParameterGroupsResult>
  <ResponseMetadata>
    <RequestId>71d08207-2831-11ea-9939-5fccefa818c0</RequestId>
  </ResponseMetadata>
</DescribeClusterParameterGroupsResponse>
```

## See Also
<a name="API_DescribeClusterParameterGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeClusterParameterGroups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeClusterParameterGroups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeClusterParameterGroups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeClusterParameterGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeClusterParameterGroups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeClusterParameterGroups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeClusterParameterGroups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeClusterParameterGroups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeClusterParameterGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeClusterParameterGroups) 