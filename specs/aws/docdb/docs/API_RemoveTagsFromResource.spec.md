---
id: "@specs/aws/docdb/docs/API_RemoveTagsFromResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RemoveTagsFromResource"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# RemoveTagsFromResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_RemoveTagsFromResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RemoveTagsFromResource
<a name="API_RemoveTagsFromResource"></a>

Removes metadata tags from an Amazon DocumentDB resource.

## Request Parameters
<a name="API_RemoveTagsFromResource_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ResourceName **   
The Amazon DocumentDB resource that the tags are removed from. This value is an Amazon Resource Name (ARN).  
Type: String  
Required: Yes

 **TagKeys.member.N**   
The tag key (name) of the tag to be removed.  
Type: Array of strings  
Required: Yes

## Errors
<a name="API_RemoveTagsFromResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing cluster.   
HTTP Status Code: 404

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing instance.   
HTTP Status Code: 404

 ** DBSnapshotNotFound **   
 `DBSnapshotIdentifier` doesn't refer to an existing snapshot.   
HTTP Status Code: 404

## See Also
<a name="API_RemoveTagsFromResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/RemoveTagsFromResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/RemoveTagsFromResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/RemoveTagsFromResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/RemoveTagsFromResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/RemoveTagsFromResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/RemoveTagsFromResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/RemoveTagsFromResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/RemoveTagsFromResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/RemoveTagsFromResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/RemoveTagsFromResource) 