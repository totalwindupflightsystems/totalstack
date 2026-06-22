---
id: "@specs/aws/redshift/docs/API_DeleteClusterSecurityGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteClusterSecurityGroup"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DeleteClusterSecurityGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DeleteClusterSecurityGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteClusterSecurityGroup
<a name="API_DeleteClusterSecurityGroup"></a>

Deletes an Amazon Redshift security group.

**Note**  
You cannot delete a security group that is associated with any clusters. You cannot delete the default security group.

 For information about managing security groups, go to [Amazon Redshift Cluster Security Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html) in the *Amazon Redshift Cluster Management Guide*.

## Request Parameters
<a name="API_DeleteClusterSecurityGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterSecurityGroupName **   
The name of the cluster security group to be deleted.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Errors
<a name="API_DeleteClusterSecurityGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterSecurityGroupNotFound **   
The cluster security group name does not refer to an existing cluster security group.  
HTTP Status Code: 404

 ** InvalidClusterSecurityGroupState **   
The state of the cluster security group is not `available`.   
HTTP Status Code: 400

## Examples
<a name="API_DeleteClusterSecurityGroup_Examples"></a>

### Example
<a name="API_DeleteClusterSecurityGroup_Example_1"></a>

This example illustrates one usage of DeleteClusterSecurityGroup.

#### Sample Request
<a name="API_DeleteClusterSecurityGroup_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
    ?Action=DeleteClusterSecurityGroup
    &ClusterSecurityGroupName=securitygroup1
    &Version=2012-12-01
    &x-amz-algorithm=AWS4-HMAC-SHA256
    &x-amz-credential=AKIAIOSFODNN7EXAMPLE/20121208/us-east-2/redshift/aws4_request
    &x-amz-date=20121208T015926Z
    &x-amz-signedheaders=content-type;host;x-amz-date
```

#### Sample Response
<a name="API_DeleteClusterSecurityGroup_Example_1_Response"></a>

```
<DeleteClusterSecurityGroupResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <ResponseMetadata>
    <RequestId>e54e05dc-40da-11e2-955f-313c36e9e01d</RequestId>
  </ResponseMetadata>
</DeleteClusterSecurityGroupResponse>
```

## See Also
<a name="API_DeleteClusterSecurityGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DeleteClusterSecurityGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DeleteClusterSecurityGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DeleteClusterSecurityGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DeleteClusterSecurityGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DeleteClusterSecurityGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DeleteClusterSecurityGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DeleteClusterSecurityGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DeleteClusterSecurityGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DeleteClusterSecurityGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DeleteClusterSecurityGroup) 