---
id: "@specs/aws/fsx/docs/API_UpdateSnaplockConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateSnaplockConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# UpdateSnaplockConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_UpdateSnaplockConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateSnaplockConfiguration
<a name="API_UpdateSnaplockConfiguration"></a>

Updates the SnapLock configuration for an existing FSx for ONTAP volume. 

## Contents
<a name="API_UpdateSnaplockConfiguration_Contents"></a>

 ** AuditLogVolume **   <a name="FSx-Type-UpdateSnaplockConfiguration-AuditLogVolume"></a>
Enables or disables the audit log volume for an FSx for ONTAP SnapLock volume. The default value is `false`. If you set `AuditLogVolume` to `true`, the SnapLock volume is created as an audit log volume. The minimum retention period for an audit log volume is six months.   
For more information, see [ SnapLock audit log volumes](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/how-snaplock-works.html#snaplock-audit-log-volume).   
Type: Boolean  
Required: No

 ** AutocommitPeriod **   <a name="FSx-Type-UpdateSnaplockConfiguration-AutocommitPeriod"></a>
The configuration object for setting the autocommit period of files in an FSx for ONTAP SnapLock volume.   
Type: [AutocommitPeriod](API_AutocommitPeriod.md) object  
Required: No

 ** PrivilegedDelete **   <a name="FSx-Type-UpdateSnaplockConfiguration-PrivilegedDelete"></a>
Enables, disables, or permanently disables privileged delete on an FSx for ONTAP SnapLock Enterprise volume. Enabling privileged delete allows SnapLock administrators to delete write once, read many (WORM) files even if they have active retention periods. `PERMANENTLY_DISABLED` is a terminal state. If privileged delete is permanently disabled on a SnapLock volume, you can't re-enable it. The default value is `DISABLED`.   
For more information, see [Privileged delete](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-enterprise.html#privileged-delete).   
Type: String  
Valid Values: `DISABLED | ENABLED | PERMANENTLY_DISABLED`   
Required: No

 ** RetentionPeriod **   <a name="FSx-Type-UpdateSnaplockConfiguration-RetentionPeriod"></a>
Specifies the retention period of an FSx for ONTAP SnapLock volume.   
Type: [SnaplockRetentionPeriod](API_SnaplockRetentionPeriod.md) object  
Required: No

 ** VolumeAppendModeEnabled **   <a name="FSx-Type-UpdateSnaplockConfiguration-VolumeAppendModeEnabled"></a>
Enables or disables volume-append mode on an FSx for ONTAP SnapLock volume. Volume-append mode allows you to create WORM-appendable files and write data to them incrementally. The default value is `false`.   
For more information, see [Volume-append mode](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/worm-state.html#worm-state-append).   
Type: Boolean  
Required: No

## See Also
<a name="API_UpdateSnaplockConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateSnaplockConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateSnaplockConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateSnaplockConfiguration) 