---
id: "@specs/aws/docdb/docs/API_elastic_PendingMaintenanceActionDetails"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PendingMaintenanceActionDetails"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# PendingMaintenanceActionDetails

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_elastic_PendingMaintenanceActionDetails
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PendingMaintenanceActionDetails
<a name="API_elastic_PendingMaintenanceActionDetails"></a>

Retrieves the details of maintenance actions that are pending.

## Contents
<a name="API_elastic_PendingMaintenanceActionDetails_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** action **   <a name="documentdb-Type-elastic_PendingMaintenanceActionDetails-action"></a>
Displays the specific action of a pending maintenance action.  
Type: String  
Required: Yes

 ** autoAppliedAfterDate **   <a name="documentdb-Type-elastic_PendingMaintenanceActionDetails-autoAppliedAfterDate"></a>
Displays the date of the maintenance window when the action is applied. The maintenance action is applied to the resource during its first maintenance window after this date. If this date is specified, any `NEXT_MAINTENANCE` `optInType` requests are ignored.  
Type: String  
Required: No

 ** currentApplyDate **   <a name="documentdb-Type-elastic_PendingMaintenanceActionDetails-currentApplyDate"></a>
Displays the effective date when the pending maintenance action is applied to the resource.  
Type: String  
Required: No

 ** description **   <a name="documentdb-Type-elastic_PendingMaintenanceActionDetails-description"></a>
Displays a description providing more detail about the maintenance action.  
Type: String  
Required: No

 ** forcedApplyDate **   <a name="documentdb-Type-elastic_PendingMaintenanceActionDetails-forcedApplyDate"></a>
Displays the date when the maintenance action is automatically applied. The maintenance action is applied to the resource on this date regardless of the maintenance window for the resource. If this date is specified, any `IMMEDIATE` `optInType` requests are ignored.  
Type: String  
Required: No

 ** optInStatus **   <a name="documentdb-Type-elastic_PendingMaintenanceActionDetails-optInStatus"></a>
Displays the type of `optInType` request that has been received for the resource.  
Type: String  
Required: No

## See Also
<a name="API_elastic_PendingMaintenanceActionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-elastic-2022-11-28/PendingMaintenanceActionDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-elastic-2022-11-28/PendingMaintenanceActionDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-elastic-2022-11-28/PendingMaintenanceActionDetails) 