---
id: "@specs/aws/redshift/docs/API_DescribeNodeConfigurationOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeNodeConfigurationOptions"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeNodeConfigurationOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeNodeConfigurationOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeNodeConfigurationOptions
<a name="API_DescribeNodeConfigurationOptions"></a>

Returns properties of possible node configurations such as node type, number of nodes, and disk usage for the specified action type.

## Request Parameters
<a name="API_DescribeNodeConfigurationOptions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ActionType **   
The action type to evaluate for possible node configurations. Specify "restore-cluster" to get configuration combinations based on an existing snapshot. Specify "recommend-node-config" to get configuration recommendations based on an existing cluster or snapshot. Specify "resize-cluster" to get configuration combinations for elastic resize based on an existing cluster.   
Type: String  
Valid Values: `restore-cluster | recommend-node-config | resize-cluster`   
Required: Yes

 ** ClusterIdentifier **   
The identifier of the cluster to evaluate for possible node configurations.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **Filter.NodeConfigurationOptionsFilter.N**   
A set of name, operator, and value items to filter the results.  
Type: Array of [NodeConfigurationOptionsFilter](API_NodeConfigurationOptionsFilter.md) objects  
Required: No

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a [DescribeNodeConfigurationOptions](#API_DescribeNodeConfigurationOptions) request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `marker` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.   
Default: `500`   
Constraints: minimum 100, maximum 500.  
Type: Integer  
Required: No

 ** OwnerAccount **   
The AWS account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SnapshotArn **   
The Amazon Resource Name (ARN) of the snapshot associated with the message to describe node configuration.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** SnapshotIdentifier **   
The identifier of the snapshot to evaluate for possible node configurations.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DescribeNodeConfigurationOptions_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `Marker` parameter and retrying the command. If the `Marker` field is empty, all response records have been retrieved for the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.

 **NodeConfigurationOptionList.NodeConfigurationOption.N**   
A list of valid node configurations.  
Type: Array of [NodeConfigurationOption](API_NodeConfigurationOption.md) objects

## Errors
<a name="API_DescribeNodeConfigurationOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessToSnapshotDenied **   
The owner of the specified snapshot has not authorized your account to access the snapshot.  
HTTP Status Code: 400

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** ClusterSnapshotNotFound **   
The snapshot identifier does not refer to an existing cluster snapshot.  
HTTP Status Code: 404

 ** InvalidClusterSnapshotState **   
The specified cluster snapshot is not in the `available` state, or other accounts are authorized to access the snapshot.   
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## Examples
<a name="API_DescribeNodeConfigurationOptions_Examples"></a>

### Example
<a name="API_DescribeNodeConfigurationOptions_Example_1"></a>

This example illustrates one usage of DescribeNodeConfigurationOptions.

#### Sample Request
<a name="API_DescribeNodeConfigurationOptions_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeNodeConfigurationOptions
&ActionType=restore-cluster
&SnapshotIdentifier=mysnapshotid
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeNodeConfigurationOptions_Example_1_Response"></a>

```
<DescribeNodeConfigurationOptionsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeNodeConfigurationOptionsResult>
    <NodeConfigurationOptionList>
      <NodeConfigurationOption>
        <EstimatedDiskUtilizationPercent>0.01</EstimatedDiskUtilizationPercent>
        <NumberOfNodes>2</NumberOfNodes>
        <NodeType>dc2.large</NodeType>
      </NodeConfigurationOption>
      <NodeConfigurationOption>
        <EstimatedDiskUtilizationPercent>0.01</EstimatedDiskUtilizationPercent>
        <NumberOfNodes>4</NumberOfNodes>
        <NodeType>dc2.large</NodeType>
      </NodeConfigurationOption>
      <NodeConfigurationOption>
        <EstimatedDiskUtilizationPercent>0.01</EstimatedDiskUtilizationPercent>
        <NumberOfNodes>2</NumberOfNodes>
        <NodeType>ra3.4xlarge</NodeType>
      </NodeConfigurationOption>
      <NodeConfigurationOption>
        <EstimatedDiskUtilizationPercent>0.01</EstimatedDiskUtilizationPercent>
        <NumberOfNodes>4</NumberOfNodes>
        <NodeType>ra3.4xlarge</NodeType>
      </NodeConfigurationOption>
    </NodeConfigurationOptionList>
  </DescribeNodeConfigurationOptionsResult>
  <ResponseMetadata>
    <RequestId>ed601e39-28cc-11ea-a940-1b28a85fd753</RequestId>
  </ResponseMetadata>
</DescribeNodeConfigurationOptionsResponse>
```

## See Also
<a name="API_DescribeNodeConfigurationOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeNodeConfigurationOptions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeNodeConfigurationOptions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeNodeConfigurationOptions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeNodeConfigurationOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeNodeConfigurationOptions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeNodeConfigurationOptions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeNodeConfigurationOptions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeNodeConfigurationOptions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeNodeConfigurationOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeNodeConfigurationOptions) 