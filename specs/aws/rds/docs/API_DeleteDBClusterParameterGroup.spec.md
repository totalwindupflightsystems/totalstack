---
id: "@specs/aws/rds/docs/API_DeleteDBClusterParameterGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteDBClusterParameterGroup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DeleteDBClusterParameterGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DeleteDBClusterParameterGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteDBClusterParameterGroup
<a name="API_DeleteDBClusterParameterGroup"></a>

Deletes a specified DB cluster parameter group. The DB cluster parameter group to be deleted can't be associated with any DB clusters.

For more information on Amazon Aurora, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide*.

For more information on Multi-AZ DB clusters, see [ Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide*.

## Request Parameters
<a name="API_DeleteDBClusterParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterParameterGroupName **   
The name of the DB cluster parameter group.  
Constraints:  
+ Must be the name of an existing DB cluster parameter group.
+ You can't delete a default DB cluster parameter group.
+ Can't be associated with any DB clusters.
Type: String  
Required: Yes

## Errors
<a name="API_DeleteDBClusterParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBParameterGroupNotFound **   
 `DBParameterGroupName` doesn't refer to an existing DB parameter group.  
HTTP Status Code: 404

 ** InvalidDBParameterGroupState **   
The DB parameter group is in use or is in an invalid state. If you are attempting to delete the parameter group, you can't delete it when the parameter group is in this state.  
HTTP Status Code: 400

## Examples
<a name="API_DeleteDBClusterParameterGroup_Examples"></a>

### Example
<a name="API_DeleteDBClusterParameterGroup_Example_1"></a>

This example illustrates one usage of DeleteDBClusterParameterGroup.

#### Sample Request
<a name="API_DeleteDBClusterParameterGroup_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
    ?Action=DeleteDBClusterParameterGroup
    &DBClusterParameterGroupName=sample-cluster-pg
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20160913/us-west-2/rds/aws4_request
    &X-Amz-Date=20160913T172430Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=3f54b5ee720c2644296e98a1c0393a9abd91bc0847dfe7dd9be02ede8fd95ae5
```

#### Sample Response
<a name="API_DeleteDBClusterParameterGroup_Example_1_Response"></a>

```
<DeleteDBClusterParameterGroupResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ResponseMetadata>
    <RequestId>ee0201e1-79d6-11e6-9b94-838991bd60c6</RequestId>
  </ResponseMetadata>
</DeleteDBClusterParameterGroupResponse>
```

## See Also
<a name="API_DeleteDBClusterParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DeleteDBClusterParameterGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DeleteDBClusterParameterGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DeleteDBClusterParameterGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DeleteDBClusterParameterGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DeleteDBClusterParameterGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DeleteDBClusterParameterGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DeleteDBClusterParameterGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DeleteDBClusterParameterGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DeleteDBClusterParameterGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DeleteDBClusterParameterGroup) 