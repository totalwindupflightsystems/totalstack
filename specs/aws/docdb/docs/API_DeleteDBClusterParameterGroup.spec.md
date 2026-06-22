---
id: "@specs/aws/docdb/docs/API_DeleteDBClusterParameterGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteDBClusterParameterGroup"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DeleteDBClusterParameterGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DeleteDBClusterParameterGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteDBClusterParameterGroup
<a name="API_DeleteDBClusterParameterGroup"></a>

Deletes a specified cluster parameter group. The cluster parameter group to be deleted can't be associated with any clusters.

## Request Parameters
<a name="API_DeleteDBClusterParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterParameterGroupName **   
The name of the cluster parameter group.  
Constraints:  
+ Must be the name of an existing cluster parameter group.
+ You can't delete a default cluster parameter group.
+ Cannot be associated with any clusters.
Type: String  
Required: Yes

## Errors
<a name="API_DeleteDBClusterParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBParameterGroupNotFound **   
 `DBParameterGroupName` doesn't refer to an existing parameter group.   
HTTP Status Code: 404

 ** InvalidDBParameterGroupState **   
The parameter group is in use, or it is in a state that is not valid. If you are trying to delete the parameter group, you can't delete it when the parameter group is in this state.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteDBClusterParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/DeleteDBClusterParameterGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/DeleteDBClusterParameterGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DeleteDBClusterParameterGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/DeleteDBClusterParameterGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DeleteDBClusterParameterGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/DeleteDBClusterParameterGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/DeleteDBClusterParameterGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/DeleteDBClusterParameterGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/DeleteDBClusterParameterGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DeleteDBClusterParameterGroup) 