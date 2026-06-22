---
id: "@specs/aws/redshift/docs/API_DescribeClusterVersions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeClusterVersions"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeClusterVersions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeClusterVersions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeClusterVersions
<a name="API_DescribeClusterVersions"></a>

Returns descriptions of the available Amazon Redshift cluster versions. You can call this operation even before creating any clusters to learn more about the Amazon Redshift versions. For more information about managing clusters, go to [Amazon Redshift Clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html) in the *Amazon Redshift Cluster Management Guide*.

## Request Parameters
<a name="API_DescribeClusterVersions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterParameterGroupFamily **   
The name of a specific cluster parameter group family to return details for.  
Constraints:  
+ Must be 1 to 255 alphanumeric characters
+ First character must be a letter
+ Cannot end with a hyphen or contain two consecutive hyphens
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ClusterVersion **   
The specific cluster version to return.  
Example: `1.0`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a [DescribeClusterVersions](#API_DescribeClusterVersions) request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
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
<a name="API_DescribeClusterVersions_ResponseElements"></a>

The following elements are returned by the service.

 **ClusterVersions.ClusterVersion.N**   
A list of `Version` elements.   
Type: Array of [ClusterVersion](API_ClusterVersion.md) objects

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `Marker` parameter and retrying the command. If the `Marker` field is empty, all response records have been retrieved for the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_DescribeClusterVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeClusterVersions_Examples"></a>

### Example
<a name="API_DescribeClusterVersions_Example_1"></a>

This example illustrates one usage of DescribeClusterVersions.

#### Sample Request
<a name="API_DescribeClusterVersions_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
    ?Action=DescribeClusterVersions
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeClusterVersions_Example_1_Response"></a>

```
<DescribeClusterVersionsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeClusterVersionsResult>
    <ClusterVersions>
      <ClusterVersion>
        <ClusterParameterGroupFamily>redshift-1.0</ClusterParameterGroupFamily>
        <Description>release db engine 1.0.54</Description>
        <ClusterVersion>1.0</ClusterVersion>
      </ClusterVersion>
    </ClusterVersions>
  </DescribeClusterVersionsResult>
  <ResponseMetadata>
    <RequestId>be41d43b-283e-11ea-8cc9-43f1872b4b75</RequestId>
  </ResponseMetadata>
</DescribeClusterVersionsResponse>
```

## See Also
<a name="API_DescribeClusterVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeClusterVersions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeClusterVersions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeClusterVersions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeClusterVersions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeClusterVersions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeClusterVersions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeClusterVersions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeClusterVersions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeClusterVersions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeClusterVersions) 