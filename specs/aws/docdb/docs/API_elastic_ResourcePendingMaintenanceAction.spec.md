---
id: "@specs/aws/docdb/docs/API_elastic_ResourcePendingMaintenanceAction"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ResourcePendingMaintenanceAction"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# ResourcePendingMaintenanceAction

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_elastic_ResourcePendingMaintenanceAction
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ResourcePendingMaintenanceAction
<a name="API_elastic_ResourcePendingMaintenanceAction"></a>

Provides information about a pending maintenance action for a resource.

## Contents
<a name="API_elastic_ResourcePendingMaintenanceAction_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** pendingMaintenanceActionDetails **   <a name="documentdb-Type-elastic_ResourcePendingMaintenanceAction-pendingMaintenanceActionDetails"></a>
Provides information about a pending maintenance action for a resource.  
Type: Array of [PendingMaintenanceActionDetails](API_elastic_PendingMaintenanceActionDetails.md) objects  
Required: No

 ** resourceArn **   <a name="documentdb-Type-elastic_ResourcePendingMaintenanceAction-resourceArn"></a>
The Amazon DocumentDB Amazon Resource Name (ARN) of the resource to which the pending maintenance action applies.  
Type: String  
Required: No

## See Also
<a name="API_elastic_ResourcePendingMaintenanceAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-elastic-2022-11-28/ResourcePendingMaintenanceAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-elastic-2022-11-28/ResourcePendingMaintenanceAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-elastic-2022-11-28/ResourcePendingMaintenanceAction) 