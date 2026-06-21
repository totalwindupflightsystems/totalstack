---
id: "@specs/aws/rds/docs/API_ListTagsForResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTagsForResource"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# ListTagsForResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_ListTagsForResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Lists all tags on an Amazon RDS resource.

For an overview on tagging an Amazon RDS resource, see [Tagging Amazon RDS Resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS Resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.

## Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ResourceName **   
The Amazon RDS resource with tags to be listed. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see [ Constructing an ARN for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing) in the *Amazon RDS User Guide*.  
Type: String  
Required: Yes

 **Filters.Filter.N**   
This parameter isn't currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

The following element is returned by the service.

 **TagList.Tag.N**   
List of tags returned by the `ListTagsForResource` operation.  
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_ListTagsForResource_Errors"></a>

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

 ** TenantDatabaseNotFound **   
The specified tenant database wasn't found in the DB instance.  
HTTP Status Code: 404

## Examples
<a name="API_ListTagsForResource_Examples"></a>

### Example
<a name="API_ListTagsForResource_Example_1"></a>

This example illustrates one usage of ListTagsForResource.

#### Sample Request
<a name="API_ListTagsForResource_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
    ?Action=ListTagsForResource
    &ResourceName=arn%3Aaws%3Ards%3Aus-west-2%3A12345678910%3Adb%3Asample-sql
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20160304/us-west-2/rds/aws4_request
    &X-Amz-Date=20160304T205529Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=ad333e422a92110b6340a28a684f0ed78606cc48b29b25682df0173e04b93b85
```

#### Sample Response
<a name="API_ListTagsForResource_Example_1_Response"></a>

```
<ListTagsForResourceResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ListTagsForResourceResult>
    <TagList>
      <Tag>
        <Value>development-team</Value>
        <Key>owner</Key>
      </Tag>
      <Tag>
        <Value>test</Value>
        <Key>environment</Key>
      </Tag>
    </TagList>
  </ListTagsForResourceResult>
  <ResponseMetadata>
    <RequestId>71217a3c-e24b-11e5-a5e9-cad172f9e6c1</RequestId>
  </ResponseMetadata>
</ListTagsForResourceResponse>
```

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/ListTagsForResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/ListTagsForResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ListTagsForResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/ListTagsForResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ListTagsForResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/ListTagsForResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/ListTagsForResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/ListTagsForResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/ListTagsForResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ListTagsForResource) 