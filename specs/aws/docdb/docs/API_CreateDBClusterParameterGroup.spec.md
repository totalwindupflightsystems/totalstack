---
id: "@specs/aws/docdb/docs/API_CreateDBClusterParameterGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDBClusterParameterGroup"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# CreateDBClusterParameterGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_CreateDBClusterParameterGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDBClusterParameterGroup
<a name="API_CreateDBClusterParameterGroup"></a>

Creates a new cluster parameter group.

Parameters in a cluster parameter group apply to all of the instances in a cluster.

A cluster parameter group is initially created with the default parameters for the database engine used by instances in the cluster. In Amazon DocumentDB, you cannot make modifications directly to the `default.docdb3.6` cluster parameter group. If your Amazon DocumentDB cluster is using the default cluster parameter group and you want to modify a value in it, you must first [ create a new parameter group](https://docs.aws.amazon.com/documentdb/latest/devguide/cluster_parameter_group-create.html) or [ copy an existing parameter group](https://docs.aws.amazon.com/documentdb/latest/devguide/cluster_parameter_group-copy.html), modify it, and then apply the modified parameter group to your cluster. For the new cluster parameter group and associated settings to take effect, you must then reboot the instances in the cluster without failover. For more information, see [ Modifying Amazon DocumentDB Cluster Parameter Groups](https://docs.aws.amazon.com/documentdb/latest/devguide/cluster_parameter_group-modify.html). 

## Request Parameters
<a name="API_CreateDBClusterParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterParameterGroupName **   
The name of the cluster parameter group.  
Constraints:  
+ Must not match the name of an existing `DBClusterParameterGroup`.
This value is stored as a lowercase string.
Type: String  
Required: Yes

 ** DBParameterGroupFamily **   
The cluster parameter group family name.  
Type: String  
Required: Yes

 ** Description **   
The description for the cluster parameter group.  
Type: String  
Required: Yes

 **Tags.Tag.N**   
The tags to be assigned to the cluster parameter group.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateDBClusterParameterGroup_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterParameterGroup **   
Detailed information about a cluster parameter group.   
Type: [DBClusterParameterGroup](API_DBClusterParameterGroup.md) object

## Errors
<a name="API_CreateDBClusterParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBParameterGroupAlreadyExists **   
A parameter group with the same name already exists.  
HTTP Status Code: 400

 ** DBParameterGroupQuotaExceeded **   
This request would cause you to exceed the allowed number of parameter groups.  
HTTP Status Code: 400

## See Also
<a name="API_CreateDBClusterParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/CreateDBClusterParameterGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/CreateDBClusterParameterGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/CreateDBClusterParameterGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/CreateDBClusterParameterGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/CreateDBClusterParameterGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/CreateDBClusterParameterGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/CreateDBClusterParameterGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/CreateDBClusterParameterGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/CreateDBClusterParameterGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/CreateDBClusterParameterGroup) 