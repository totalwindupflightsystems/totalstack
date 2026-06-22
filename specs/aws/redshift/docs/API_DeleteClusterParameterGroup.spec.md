---
id: "@specs/aws/redshift/docs/API_DeleteClusterParameterGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteClusterParameterGroup"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DeleteClusterParameterGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DeleteClusterParameterGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteClusterParameterGroup
<a name="API_DeleteClusterParameterGroup"></a>

Deletes a specified Amazon Redshift parameter group.

**Note**  
You cannot delete a parameter group if it is associated with a cluster.

## Request Parameters
<a name="API_DeleteClusterParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ParameterGroupName **   
The name of the parameter group to be deleted.  
Constraints:  
+ Must be the name of an existing cluster parameter group.
+ Cannot delete a default cluster parameter group.
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Errors
<a name="API_DeleteClusterParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterParameterGroupNotFound **   
The parameter group name does not refer to an existing parameter group.  
HTTP Status Code: 404

 ** InvalidClusterParameterGroupState **   
The cluster parameter group action can not be completed because another task is in progress that involves the parameter group. Wait a few moments and try the operation again.  
HTTP Status Code: 400

## Examples
<a name="API_DeleteClusterParameterGroup_Examples"></a>

### Example
<a name="API_DeleteClusterParameterGroup_Example_1"></a>

This example illustrates one usage of DeleteClusterParameterGroup.

#### Sample Request
<a name="API_DeleteClusterParameterGroup_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DeleteClusterParameterGroup
&ParameterGroupName=myclusterparametergroup
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DeleteClusterParameterGroup_Example_1_Response"></a>

```
<DeleteClusterParameterGroupResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <ResponseMetadata>
    <RequestId>95c53381-2838-11ea-a07c-5d44c0d19e91</RequestId>
  </ResponseMetadata>
</DeleteClusterParameterGroupResponse>
```

## See Also
<a name="API_DeleteClusterParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DeleteClusterParameterGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DeleteClusterParameterGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DeleteClusterParameterGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DeleteClusterParameterGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DeleteClusterParameterGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DeleteClusterParameterGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DeleteClusterParameterGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DeleteClusterParameterGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DeleteClusterParameterGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DeleteClusterParameterGroup) 