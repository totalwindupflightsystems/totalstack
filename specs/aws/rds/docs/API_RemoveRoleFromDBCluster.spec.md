---
id: "@specs/aws/rds/docs/API_RemoveRoleFromDBCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RemoveRoleFromDBCluster"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# RemoveRoleFromDBCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_RemoveRoleFromDBCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RemoveRoleFromDBCluster
<a name="API_RemoveRoleFromDBCluster"></a>

Removes the asssociation of an AWS Identity and Access Management (IAM) role from a DB cluster.

For more information on Amazon Aurora DB clusters, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide*.

For more information on Multi-AZ DB clusters, see [ Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide.* 

## Request Parameters
<a name="API_RemoveRoleFromDBCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The name of the DB cluster to disassociate the IAM role from.  
Type: String  
Required: Yes

 ** RoleArn **   
The Amazon Resource Name (ARN) of the IAM role to disassociate from the Aurora DB cluster, for example `arn:aws:iam::123456789012:role/AuroraAccessRole`.  
Type: String  
Required: Yes

 ** FeatureName **   
The name of the feature for the DB cluster that the IAM role is to be disassociated from. For information about supported feature names, see [DBEngineVersion](API_DBEngineVersion.md).  
Type: String  
Required: No

## Errors
<a name="API_RemoveRoleFromDBCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

 ** DBClusterRoleNotFound **   
The specified IAM role Amazon Resource Name (ARN) isn't associated with the specified DB cluster.  
HTTP Status Code: 404

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

## Examples
<a name="API_RemoveRoleFromDBCluster_Examples"></a>

### Example
<a name="API_RemoveRoleFromDBCluster_Example_1"></a>

This example illustrates one usage of RemoveRoleFromDBCluster.

#### Sample Request
<a name="API_RemoveRoleFromDBCluster_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
    ?Action=RemoveRoleFromDBCluster
    &DBClusterIdentifier=sample-cluster
    &RoleArn=arn%3Aaws%3Aiam%3A%3A123456789012%3Arole%2Fsample-role
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20161012/us-east-1/rds/aws4_request
    &X-Amz-Date=20161012T204525Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=cd7d5005d56a505b4e2a878c297e6f8a3cc26b19a335ede018ba41f3185c92a2
```

#### Sample Response
<a name="API_RemoveRoleFromDBCluster_Example_1_Response"></a>

```
<RemoveRoleFromDBClusterResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ResponseMetadata>
    <RequestId>ccfca75a-90bc-11e6-8533-cd6377e421f8</RequestId>
  </ResponseMetadata>
</RemoveRoleFromDBClusterResponse>
```

## See Also
<a name="API_RemoveRoleFromDBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/RemoveRoleFromDBCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/RemoveRoleFromDBCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/RemoveRoleFromDBCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/RemoveRoleFromDBCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/RemoveRoleFromDBCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/RemoveRoleFromDBCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/RemoveRoleFromDBCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/RemoveRoleFromDBCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/RemoveRoleFromDBCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/RemoveRoleFromDBCluster) 