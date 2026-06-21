---
id: "@specs/aws/rds/docs/API_AddRoleToDBCluster"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AddRoleToDBCluster"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# AddRoleToDBCluster

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_AddRoleToDBCluster
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AddRoleToDBCluster
<a name="API_AddRoleToDBCluster"></a>

Associates an AWS Identity and Access Management (IAM) role with a DB cluster.

## Request Parameters
<a name="API_AddRoleToDBCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The name of the DB cluster to associate the IAM role with.  
Type: String  
Required: Yes

 ** RoleArn **   
The Amazon Resource Name (ARN) of the IAM role to associate with the Aurora DB cluster, for example `arn:aws:iam::123456789012:role/AuroraAccessRole`.  
Type: String  
Required: Yes

 ** FeatureName **   
The name of the feature for the DB cluster that the IAM role is to be associated with. For information about supported feature names, see [DBEngineVersion](API_DBEngineVersion.md).  
Type: String  
Required: No

## Errors
<a name="API_AddRoleToDBCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

 ** DBClusterRoleAlreadyExists **   
The specified IAM role Amazon Resource Name (ARN) is already associated with the specified DB cluster.  
HTTP Status Code: 400

 ** DBClusterRoleQuotaExceeded **   
You have exceeded the maximum number of IAM roles that can be associated with the specified DB cluster.  
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

## Examples
<a name="API_AddRoleToDBCluster_Examples"></a>

### Example
<a name="API_AddRoleToDBCluster_Example_1"></a>

This example illustrates one usage of AddRoleToDBCluster.

#### Sample Request
<a name="API_AddRoleToDBCluster_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
    ?Action=AddRoleToDBCluster
    &DBClusterIdentifier=sample-cluster
    &RoleArn=arn%3Aaws%3Aiam%3A%3A123456789012%3Arole%2Fsample-role
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20161012/us-east-1/rds/aws4_request
    &X-Amz-Date=20161012T204524Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=d73c069210f98e5377851fa4c4ab2fdd53e8bd5d5f02f4f8ef15d4daa5b04567
```

#### Sample Response
<a name="API_AddRoleToDBCluster_Example_1_Response"></a>

```
<AddRoleToDBClusterResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ResponseMetadata>
    <RequestId>ccccbdb6-90bc-11e6-8533-cd6447e421f8</RequestId>
  </ResponseMetadata>
</AddRoleToDBClusterResponse>
```

## See Also
<a name="API_AddRoleToDBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/AddRoleToDBCluster) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/AddRoleToDBCluster) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/AddRoleToDBCluster) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/AddRoleToDBCluster) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/AddRoleToDBCluster) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/AddRoleToDBCluster) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/AddRoleToDBCluster) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/AddRoleToDBCluster) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/AddRoleToDBCluster) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/AddRoleToDBCluster) 