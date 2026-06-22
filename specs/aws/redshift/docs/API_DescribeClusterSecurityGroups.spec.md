---
id: "@specs/aws/redshift/docs/API_DescribeClusterSecurityGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeClusterSecurityGroups"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeClusterSecurityGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeClusterSecurityGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeClusterSecurityGroups
<a name="API_DescribeClusterSecurityGroups"></a>

Returns information about Amazon Redshift security groups. If the name of a security group is specified, the response will contain only information about only that security group.

 For information about managing security groups, go to [Amazon Redshift Cluster Security Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html) in the *Amazon Redshift Cluster Management Guide*.

If you specify both tag keys and tag values in the same request, Amazon Redshift returns all security groups that match any combination of the specified keys and values. For example, if you have `owner` and `environment` for tag keys, and `admin` and `test` for tag values, all security groups that have any combination of those values are returned.

If both tag keys and values are omitted from the request, security groups are returned regardless of whether they have tag keys or values associated with them.

## Request Parameters
<a name="API_DescribeClusterSecurityGroups_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterSecurityGroupName **   
The name of a cluster security group for which you are requesting details. You must specify either the **Marker** parameter or a **ClusterSecurityGroupName** parameter, but not both.   
 Example: `securitygroup1`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a [DescribeClusterSecurityGroups](#API_DescribeClusterSecurityGroups) request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Constraints: You must specify either the **ClusterSecurityGroupName** parameter or the **Marker** parameter, but not both.   
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
A tag key or keys for which you want to return all matching cluster security groups that are associated with the specified key or keys. For example, suppose that you have security groups that are tagged with keys called `owner` and `environment`. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the security groups that have either or both of these tag keys associated with them.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **TagValues.TagValue.N**   
A tag value or values for which you want to return all matching cluster security groups that are associated with the specified tag value or values. For example, suppose that you have security groups that are tagged with values called `admin` and `test`. If you specify both of these tag values in the request, Amazon Redshift returns a response with the security groups that have either or both of these tag values associated with them.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DescribeClusterSecurityGroups_ResponseElements"></a>

The following elements are returned by the service.

 **ClusterSecurityGroups.ClusterSecurityGroup.N**   
A list of [ClusterSecurityGroup](API_ClusterSecurityGroup.md) instances.   
Type: Array of [ClusterSecurityGroup](API_ClusterSecurityGroup.md) objects

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `Marker` parameter and retrying the command. If the `Marker` field is empty, all response records have been retrieved for the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_DescribeClusterSecurityGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterSecurityGroupNotFound **   
The cluster security group name does not refer to an existing cluster security group.  
HTTP Status Code: 404

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

## Examples
<a name="API_DescribeClusterSecurityGroups_Examples"></a>

### Example
<a name="API_DescribeClusterSecurityGroups_Example_1"></a>

This example illustrates one usage of DescribeClusterSecurityGroups.

#### Sample Request
<a name="API_DescribeClusterSecurityGroups_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
    ?Action=DescribeClusterSecurityGroups
    &Version=2012-12-01
    &x-amz-algorithm=AWS4-HMAC-SHA256
    &x-amz-credential=AKIAIOSFODNN7EXAMPLE/20130123/us-east-2/redshift/aws4_request
    &x-amz-date=20130123T010237Z
    &x-amz-signedheaders=content-type;host;x-amz-date
```

#### Sample Response
<a name="API_DescribeClusterSecurityGroups_Example_1_Response"></a>

```
<DescribeClusterSecurityGroupsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeClusterSecurityGroupsResult>
    <ClusterSecurityGroups>
      <ClusterSecurityGroup>
        <EC2SecurityGroups/>
        <IPRanges>
          <IPRange>
            <CIDRIP>0.0.0.0/0</CIDRIP>
            <Status>authorized</Status>
          </IPRange>
        </IPRanges>
        <Description>default</Description>
        <ClusterSecurityGroupName>default</ClusterSecurityGroupName>
      </ClusterSecurityGroup>
      <ClusterSecurityGroup>
        <EC2SecurityGroups/>
        <IPRanges/>
        <Description>my security group</Description>
        <ClusterSecurityGroupName>securitygroup1</ClusterSecurityGroupName>
      </ClusterSecurityGroup>
    </ClusterSecurityGroups>
  </DescribeClusterSecurityGroupsResult>
  <ResponseMetadata>
    <RequestId>947a8305-64f8-11e2-bec0-17624ad140dd</RequestId>
  </ResponseMetadata>
</DescribeClusterSecurityGroupsResponse>
```

## See Also
<a name="API_DescribeClusterSecurityGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeClusterSecurityGroups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeClusterSecurityGroups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeClusterSecurityGroups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeClusterSecurityGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeClusterSecurityGroups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeClusterSecurityGroups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeClusterSecurityGroups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeClusterSecurityGroups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeClusterSecurityGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeClusterSecurityGroups) 