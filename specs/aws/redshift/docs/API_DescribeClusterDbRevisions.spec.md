---
id: "@specs/aws/redshift/docs/API_DescribeClusterDbRevisions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeClusterDbRevisions"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeClusterDbRevisions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeClusterDbRevisions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeClusterDbRevisions
<a name="API_DescribeClusterDbRevisions"></a>

Returns an array of `ClusterDbRevision` objects.

## Request Parameters
<a name="API_DescribeClusterDbRevisions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
A unique identifier for a cluster whose `ClusterDbRevisions` you are requesting. This parameter is case sensitive. All clusters defined for an account are returned by default.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Marker **   
An optional parameter that specifies the starting point for returning a set of response records. When the results of a `DescribeClusterDbRevisions` request exceed the value specified in `MaxRecords`, Amazon Redshift returns a value in the `marker` field of the response. You can retrieve the next set of response records by providing the returned `marker` value in the `marker` parameter and retrying the request.   
Constraints: You can specify either the `ClusterIdentifier` parameter, or the `marker` parameter, but not both.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in the `marker` field of the response. You can retrieve the next set of response records by providing the returned `marker` value in the `marker` parameter and retrying the request.   
Default: 100  
Constraints: minimum 20, maximum 100.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeClusterDbRevisions_ResponseElements"></a>

The following elements are returned by the service.

 **ClusterDbRevisions.ClusterDbRevision.N**   
A list of revisions.  
Type: Array of [ClusterDbRevision](API_ClusterDbRevision.md) objects

 ** Marker **   
A string representing the starting point for the next set of revisions. If a value is returned in a response, you can retrieve the next set of revisions by providing the value in the `marker` parameter and retrying the command. If the `marker` field is empty, all revisions have already been returned.  
Type: String  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_DescribeClusterDbRevisions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

## Examples
<a name="API_DescribeClusterDbRevisions_Examples"></a>

### Example
<a name="API_DescribeClusterDbRevisions_Example_1"></a>

This example illustrates one usage of DescribeClusterDbRevisions.

#### Sample Request
<a name="API_DescribeClusterDbRevisions_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeClusterDbRevisions
&ClusterIdentifier=mycluster
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeClusterDbRevisions_Example_1_Response"></a>

```
<DescribeClusterDbRevisionsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeClusterDbRevisionsResult>
    <ClusterDbRevisions>
      <ClusterDbRevision>
        <DatabaseRevisionReleaseDate>2019-12-23T19:11:37.360Z</DatabaseRevisionReleaseDate>
        <ClusterIdentifier>mycluster</ClusterIdentifier>
        <RevisionTargets/>
        <CurrentDatabaseRevision>11978</CurrentDatabaseRevision>
      </ClusterDbRevision>
    </ClusterDbRevisions>
  </DescribeClusterDbRevisionsResult>
  <ResponseMetadata>
    <RequestId>28c11f9d-283e-11ea-8cc9-43f1872b4b75</RequestId>
  </ResponseMetadata>
</DescribeClusterDbRevisionsResponse>
```

## See Also
<a name="API_DescribeClusterDbRevisions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeClusterDbRevisions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeClusterDbRevisions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeClusterDbRevisions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeClusterDbRevisions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeClusterDbRevisions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeClusterDbRevisions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeClusterDbRevisions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeClusterDbRevisions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeClusterDbRevisions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeClusterDbRevisions) 