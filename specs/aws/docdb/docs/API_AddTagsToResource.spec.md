---
id: "@specs/aws/docdb/docs/API_AddTagsToResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AddTagsToResource"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# AddTagsToResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_AddTagsToResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AddTagsToResource
<a name="API_AddTagsToResource"></a>

Adds metadata tags to an Amazon DocumentDB resource. You can use these tags with cost allocation reporting to track costs that are associated with Amazon DocumentDB resources or in a `Condition` statement in an AWS Identity and Access Management (IAM) policy for Amazon DocumentDB.

## Request Parameters
<a name="API_AddTagsToResource_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ResourceName **   
The Amazon DocumentDB resource that the tags are added to. This value is an Amazon Resource Name .  
Type: String  
Required: Yes

 **Tags.Tag.N**   
The tags to be assigned to the Amazon DocumentDB resource.  
Type: Array of [Tag](API_Tag.md) objects  
Required: Yes

## Errors
<a name="API_AddTagsToResource_Errors"></a>

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
<a name="API_AddTagsToResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/AddTagsToResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/AddTagsToResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/AddTagsToResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/AddTagsToResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/AddTagsToResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/AddTagsToResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/AddTagsToResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/AddTagsToResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/AddTagsToResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/AddTagsToResource) 