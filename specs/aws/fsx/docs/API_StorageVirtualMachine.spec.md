---
id: "@specs/aws/fsx/docs/API_StorageVirtualMachine"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StorageVirtualMachine"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# StorageVirtualMachine

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_StorageVirtualMachine
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StorageVirtualMachine
<a name="API_StorageVirtualMachine"></a>

Describes the Amazon FSx for NetApp ONTAP storage virtual machine (SVM) configuration.

## Contents
<a name="API_StorageVirtualMachine_Contents"></a>

 ** ActiveDirectoryConfiguration **   <a name="FSx-Type-StorageVirtualMachine-ActiveDirectoryConfiguration"></a>
Describes the Microsoft Active Directory configuration to which the SVM is joined, if applicable.  
Type: [SvmActiveDirectoryConfiguration](API_SvmActiveDirectoryConfiguration.md) object  
Required: No

 ** CreationTime **   <a name="FSx-Type-StorageVirtualMachine-CreationTime"></a>
The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.  
Type: Timestamp  
Required: No

 ** Endpoints **   <a name="FSx-Type-StorageVirtualMachine-Endpoints"></a>
The endpoints that are used to access data or to manage the SVM using the NetApp ONTAP CLI, REST API, or NetApp CloudManager. They are the `Iscsi`, `Management`, `Nfs`, and `Smb` endpoints.  
Type: [SvmEndpoints](API_SvmEndpoints.md) object  
Required: No

 ** FileSystemId **   <a name="FSx-Type-StorageVirtualMachine-FileSystemId"></a>
The globally unique ID of the file system, assigned by Amazon FSx.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fs-[0-9a-f]{8,})$`   
Required: No

 ** Lifecycle **   <a name="FSx-Type-StorageVirtualMachine-Lifecycle"></a>
Describes the SVM's lifecycle status.  
+  `CREATED` - The SVM is fully available for use.
+  `CREATING` - Amazon FSx is creating the new SVM.
+  `DELETING` - Amazon FSx is deleting an existing SVM.
+  `FAILED` - Amazon FSx was unable to create the SVM.
+  `MISCONFIGURED` - The SVM is in a failed but recoverable state.
+  `PENDING` - Amazon FSx has not started creating the SVM.
Type: String  
Valid Values: `CREATED | CREATING | DELETING | FAILED | MISCONFIGURED | PENDING`   
Required: No

 ** LifecycleTransitionReason **   <a name="FSx-Type-StorageVirtualMachine-LifecycleTransitionReason"></a>
Describes why the SVM lifecycle state changed.  
Type: [LifecycleTransitionReason](API_LifecycleTransitionReason.md) object  
Required: No

 ** Name **   <a name="FSx-Type-StorageVirtualMachine-Name"></a>
The name of the SVM, if provisioned.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 47.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,47}$`   
Required: No

 ** ResourceARN **   <a name="FSx-Type-StorageVirtualMachine-ResourceARN"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 512.  
Pattern: `^arn:(?=[^:]+:fsx:[^:]+:\d{12}:)((|(?=[a-z0-9-.]{1,63})(?!\d{1,3}(\.\d{1,3}){3})(?![^:]*-{2})(?![^:]*-\.)(?![^:]*\.-)[a-z0-9].*(?<!-)):){4}(?!/).{0,1024}$`   
Required: No

 ** RootVolumeSecurityStyle **   <a name="FSx-Type-StorageVirtualMachine-RootVolumeSecurityStyle"></a>
The security style of the root volume of the SVM.  
Type: String  
Valid Values: `UNIX | NTFS | MIXED`   
Required: No

 ** StorageVirtualMachineId **   <a name="FSx-Type-StorageVirtualMachine-StorageVirtualMachineId"></a>
The SVM's system generated unique ID.  
Type: String  
Length Constraints: Fixed length of 21.  
Pattern: `^(svm-[0-9a-f]{17,})$`   
Required: No

 ** Subtype **   <a name="FSx-Type-StorageVirtualMachine-Subtype"></a>
Describes the SVM's subtype.  
Type: String  
Valid Values: `DEFAULT | DP_DESTINATION | SYNC_DESTINATION | SYNC_SOURCE`   
Required: No

 ** Tags **   <a name="FSx-Type-StorageVirtualMachine-Tags"></a>
A list of `Tag` values, with a maximum of 50 elements.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

 ** UUID **   <a name="FSx-Type-StorageVirtualMachine-UUID"></a>
The SVM's UUID (universally unique identifier).  
Type: String  
Length Constraints: Maximum length of 36.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,36}$`   
Required: No

## See Also
<a name="API_StorageVirtualMachine_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/StorageVirtualMachine) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/StorageVirtualMachine) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/StorageVirtualMachine) 