---
id: "@specs/aws/redshift/docs/API_DeferredMaintenanceWindow"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeferredMaintenanceWindow"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DeferredMaintenanceWindow

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DeferredMaintenanceWindow
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeferredMaintenanceWindow
<a name="API_DeferredMaintenanceWindow"></a>

Describes a deferred maintenance window

## Contents
<a name="API_DeferredMaintenanceWindow_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** DeferMaintenanceEndTime **   
 A timestamp for the end of the time period when we defer maintenance.  
Type: Timestamp  
Required: No

 ** DeferMaintenanceIdentifier **   
A unique identifier for the maintenance window.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** DeferMaintenanceStartTime **   
 A timestamp for the beginning of the time period when we defer maintenance.  
Type: Timestamp  
Required: No

## See Also
<a name="API_DeferredMaintenanceWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DeferredMaintenanceWindow) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DeferredMaintenanceWindow) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DeferredMaintenanceWindow) 