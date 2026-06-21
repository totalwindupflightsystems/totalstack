---
id: "@specs/aws/rds/docs/API_RemoveTagsFromResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RemoveTagsFromResource"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# RemoveTagsFromResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_RemoveTagsFromResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RemoveTagsFromResource
<a name="API_RemoveTagsFromResource"></a>

Removes metadata tags from an Amazon RDS resource.

For an overview on tagging an Amazon RDS resource, see [Tagging Amazon RDS Resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS Resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.

## Request Parameters
<a name="API_RemoveTagsFromResource_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ResourceName **   
The Amazon RDS resource that the tags are removed from. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see [ Constructing an ARN for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing) in the *Amazon RDS User Guide.*   
Type: String  
Required: Yes

 **TagKeys.member.N**   
The tag key (name) of the tag to be removed.  
Type: Array of strings  
Required: Yes

## Errors
<a name="API_RemoveTagsFromResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BlueGreenDeploymentNotFoundFault **   
 `BlueGreenDeploymentIdentifier` doesn't refer to an existing blue/green deployment.  
HTTP Status Code: 404

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing DB cluster.  
HTTP Status Code: 404

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.  
HTTP Status Code: 404

 ** DBProxyEndpointNotFoundFault **   
The DB proxy endpoint doesn't exist.  
HTTP Status Code: 404

 ** DBProxyNotFoundFault **   
The specified proxy name doesn't correspond to a proxy owned by your AWS account in the specified AWS Region.  
HTTP Status Code: 404

 ** DBProxyTargetGroupNotFoundFault **   
The specified target group isn't available for a proxy owned by your AWS account in the specified AWS Region.  
HTTP Status Code: 404

 ** DBShardGroupNotFound **   
The specified DB shard group name wasn't found.  
HTTP Status Code: 404

 ** DBSnapshotNotFound **   
 `DBSnapshotIdentifier` doesn't refer to an existing DB snapshot.  
HTTP Status Code: 404

 ** DBSnapshotTenantDatabaseNotFoundFault **   
The specified snapshot tenant database wasn't found.  
HTTP Status Code: 404

 ** IntegrationNotFoundFault **   
The specified integration could not be found.  
HTTP Status Code: 404

 ** InvalidDBClusterEndpointStateFault **   
The requested operation can't be performed on the endpoint while the endpoint is in this state.  
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **   
The requested operation can't be performed while the cluster is in this state.  
HTTP Status Code: 400

 ** InvalidDBInstanceState **   
The DB instance isn't in a valid state.  
HTTP Status Code: 400

 ** TenantDatabaseNotFound **   
The specified tenant database wasn't found in the DB instance.  
HTTP Status Code: 404

## Examples
<a name="API_RemoveTagsFromResource_Examples"></a>

### Example
<a name="API_RemoveTagsFromResource_Example_1"></a>

This example illustrates one usage of RemoveTagsFromResource.

#### Sample Request
<a name="API_RemoveTagsFromResource_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
    ?Action=RemoveTagsFromResource
    &ResourceName=arn%3Aaws%3Ards%3Aus-west-2%3A123456789012%3Adb%3Asample
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &TagKeys.member.1=InstanceType
    &TagKeys.member.2=Owner
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20160913/us-west-2/rds/aws4_request
    &X-Amz-Date=20160913T174918Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=4c72f307a75444461bd9b9ccb7de361fec75b8adad66a52824226320d0a33ca8
```

#### Sample Response
<a name="API_RemoveTagsFromResource_Example_1_Response"></a>

```
<RemoveTagsFromResourceResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ResponseMetadata>
    <RequestId>126d40cc-79da-11e6-b8e4-29f0c684be5d</RequestId>
  </ResponseMetadata>
</RemoveTagsFromResourceResponse>
```

## See Also
<a name="API_RemoveTagsFromResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/RemoveTagsFromResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/RemoveTagsFromResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/RemoveTagsFromResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/RemoveTagsFromResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/RemoveTagsFromResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/RemoveTagsFromResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/RemoveTagsFromResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/RemoveTagsFromResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/RemoveTagsFromResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/RemoveTagsFromResource) 