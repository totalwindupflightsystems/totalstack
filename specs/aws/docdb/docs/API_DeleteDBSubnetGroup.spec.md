---
id: "@specs/aws/docdb/docs/API_DeleteDBSubnetGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteDBSubnetGroup"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DeleteDBSubnetGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DeleteDBSubnetGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteDBSubnetGroup
<a name="API_DeleteDBSubnetGroup"></a>

Deletes a subnet group.

**Note**  
The specified database subnet group must not be associated with any DB instances.

## Request Parameters
<a name="API_DeleteDBSubnetGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBSubnetGroupName **   
The name of the database subnet group to delete.  
You can't delete the default subnet group.
Constraints:  
Must match the name of an existing `DBSubnetGroup`. Must not be default.  
Example: `mySubnetgroup`   
Type: String  
Required: Yes

## Errors
<a name="API_DeleteDBSubnetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBSubnetGroupNotFoundFault **   
 `DBSubnetGroupName` doesn't refer to an existing subnet group.   
HTTP Status Code: 404

 ** InvalidDBSubnetGroupStateFault **   
The subnet group can't be deleted because it's in use.  
HTTP Status Code: 400

 ** InvalidDBSubnetStateFault **   
 The subnet isn't in the *available* state.   
HTTP Status Code: 400

## See Also
<a name="API_DeleteDBSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/DeleteDBSubnetGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/DeleteDBSubnetGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DeleteDBSubnetGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/DeleteDBSubnetGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DeleteDBSubnetGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/DeleteDBSubnetGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/DeleteDBSubnetGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/DeleteDBSubnetGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/DeleteDBSubnetGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DeleteDBSubnetGroup) 