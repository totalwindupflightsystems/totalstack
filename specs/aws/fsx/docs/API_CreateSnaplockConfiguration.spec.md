---
id: "@specs/aws/fsx/docs/API_CreateSnaplockConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateSnaplockConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateSnaplockConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateSnaplockConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateSnaplockConfiguration
<a name="API_CreateSnaplockConfiguration"></a>

Defines the SnapLock configuration when creating an FSx for ONTAP SnapLock volume. 

## Contents
<a name="API_CreateSnaplockConfiguration_Contents"></a>

 ** SnaplockType **   <a name="FSx-Type-CreateSnaplockConfiguration-SnaplockType"></a>
Specifies the retention mode of an FSx for ONTAP SnapLock volume. After it is set, it can't be changed. You can choose one of the following retention modes:   
+  `COMPLIANCE`: Files transitioned to write once, read many (WORM) on a Compliance volume can't be deleted until their retention periods expire. This retention mode is used to address government or industry-specific mandates or to protect against ransomware attacks. For more information, see [SnapLock Compliance](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-compliance.html). 
+  `ENTERPRISE`: Files transitioned to WORM on an Enterprise volume can be deleted by authorized users before their retention periods expire using privileged delete. This retention mode is used to advance an organization's data integrity and internal compliance or to test retention settings before using SnapLock Compliance. For more information, see [SnapLock Enterprise](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-enterprise.html). 
Type: String  
Valid Values: `COMPLIANCE | ENTERPRISE`   
Required: Yes

 ** AuditLogVolume **   <a name="FSx-Type-CreateSnaplockConfiguration-AuditLogVolume"></a>
Enables or disables the audit log volume for an FSx for ONTAP SnapLock volume. The default value is `false`. If you set `AuditLogVolume` to `true`, the SnapLock volume is created as an audit log volume. The minimum retention period for an audit log volume is six months.   
For more information, see [ SnapLock audit log volumes](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/how-snaplock-works.html#snaplock-audit-log-volume).   
Type: Boolean  
Required: No

 ** AutocommitPeriod **   <a name="FSx-Type-CreateSnaplockConfiguration-AutocommitPeriod"></a>
The configuration object for setting the autocommit period of files in an FSx for ONTAP SnapLock volume.   
Type: [AutocommitPeriod](API_AutocommitPeriod.md) object  
Required: No

 ** PrivilegedDelete **   <a name="FSx-Type-CreateSnaplockConfiguration-PrivilegedDelete"></a>
Enables, disables, or permanently disables privileged delete on an FSx for ONTAP SnapLock Enterprise volume. Enabling privileged delete allows SnapLock administrators to delete WORM files even if they have active retention periods. `PERMANENTLY_DISABLED` is a terminal state. If privileged delete is permanently disabled on a SnapLock volume, you can't re-enable it. The default value is `DISABLED`.   
For more information, see [Privileged delete](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-enterprise.html#privileged-delete).   
Type: String  
Valid Values: `DISABLED | ENABLED | PERMANENTLY_DISABLED`   
Required: No

 ** RetentionPeriod **   <a name="FSx-Type-CreateSnaplockConfiguration-RetentionPeriod"></a>
Specifies the retention period of an FSx for ONTAP SnapLock volume.   
Type: [SnaplockRetentionPeriod](API_SnaplockRetentionPeriod.md) object  
Required: No

 ** VolumeAppendModeEnabled **   <a name="FSx-Type-CreateSnaplockConfiguration-VolumeAppendModeEnabled"></a>
Enables or disables volume-append mode on an FSx for ONTAP SnapLock volume. Volume-append mode allows you to create WORM-appendable files and write data to them incrementally. The default value is `false`.   
For more information, see [Volume-append mode](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/worm-state.html#worm-state-append).   
Type: Boolean  
Required: No

## See Also
<a name="API_CreateSnaplockConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateSnaplockConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateSnaplockConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateSnaplockConfiguration) 