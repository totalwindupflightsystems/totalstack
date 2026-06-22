---
id: "@specs/aws/redshift/docs/API_MaintenanceTrack"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS MaintenanceTrack"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# MaintenanceTrack

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_MaintenanceTrack
> **target_lang:** meta — documentation tier. ALL sections preserved.



# MaintenanceTrack
<a name="API_MaintenanceTrack"></a>

Defines a maintenance track that determines which Amazon Redshift version to apply during a maintenance window. If the value for `MaintenanceTrack` is `current`, the cluster is updated to the most recently certified maintenance release. If the value is `trailing`, the cluster is updated to the previously certified maintenance release. 

## Contents
<a name="API_MaintenanceTrack_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** DatabaseVersion **   
The version number for the cluster release.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaintenanceTrackName **   
The name of the maintenance track. Possible values are `current` and `trailing`.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** UpdateTargets.UpdateTarget.N **   
An array of [UpdateTarget](API_UpdateTarget.md) objects to update with the maintenance track.   
Type: Array of [UpdateTarget](API_UpdateTarget.md) objects  
Required: No

## See Also
<a name="API_MaintenanceTrack_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/MaintenanceTrack) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/MaintenanceTrack) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/MaintenanceTrack) 