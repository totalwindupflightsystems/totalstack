---
id: "@specs/aws/docdb/docs/API_ResourcePendingMaintenanceActions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ResourcePendingMaintenanceActions"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# ResourcePendingMaintenanceActions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_ResourcePendingMaintenanceActions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ResourcePendingMaintenanceActions
<a name="API_ResourcePendingMaintenanceActions"></a>

Represents the output of [ApplyPendingMaintenanceAction](API_ApplyPendingMaintenanceAction.md). 

## Contents
<a name="API_ResourcePendingMaintenanceActions_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** PendingMaintenanceActionDetails.PendingMaintenanceAction.N **   
A list that provides details about the pending maintenance actions for the resource.  
Type: Array of [PendingMaintenanceAction](API_PendingMaintenanceAction.md) objects  
Required: No

 ** ResourceIdentifier **   
The Amazon Resource Name (ARN) of the resource that has pending maintenance actions.  
Type: String  
Required: No

## See Also
<a name="API_ResourcePendingMaintenanceActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/ResourcePendingMaintenanceActions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/ResourcePendingMaintenanceActions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/ResourcePendingMaintenanceActions) 