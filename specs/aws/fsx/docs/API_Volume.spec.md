---
id: "@specs/aws/fsx/docs/API_Volume"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Volume"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# Volume

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_Volume
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Volume
<a name="API_Volume"></a>

Describes an Amazon FSx volume.

## Contents
<a name="API_Volume_Contents"></a>

 ** AdministrativeActions **   <a name="FSx-Type-Volume-AdministrativeActions"></a>
A list of administrative actions for the volume that are in process or waiting to be processed. Administrative actions describe changes to the volume that you have initiated using the `UpdateVolume` action.  
Type: Array of [AdministrativeAction](API_AdministrativeAction.md) objects  
Array Members: Maximum number of 50 items.  
Required: No

 ** CreationTime **   <a name="FSx-Type-Volume-CreationTime"></a>
The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.  
Type: Timestamp  
Required: No

 ** FileSystemId **   <a name="FSx-Type-Volume-FileSystemId"></a>
The globally unique ID of the file system, assigned by Amazon FSx.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fs-[0-9a-f]{8,})$`   
Required: No

 ** Lifecycle **   <a name="FSx-Type-Volume-Lifecycle"></a>
The lifecycle status of the volume.  
+  `AVAILABLE` - The volume is fully available for use.
+  `CREATED` - The volume has been created.
+  `CREATING` - Amazon FSx is creating the new volume.
+  `DELETING` - Amazon FSx is deleting an existing volume.
+  `FAILED` - Amazon FSx was unable to create the volume.
+  `MISCONFIGURED` - The volume is in a failed but recoverable state.
+  `PENDING` - Amazon FSx hasn't started creating the volume.
Type: String  
Valid Values: `CREATING | CREATED | DELETING | FAILED | MISCONFIGURED | PENDING | AVAILABLE`   
Required: No

 ** LifecycleTransitionReason **   <a name="FSx-Type-Volume-LifecycleTransitionReason"></a>
The reason why the volume lifecycle status changed.  
Type: [LifecycleTransitionReason](API_LifecycleTransitionReason.md) object  
Required: No

 ** Name **   <a name="FSx-Type-Volume-Name"></a>
The name of the volume.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 203.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,203}$`   
Required: No

 ** OntapConfiguration **   <a name="FSx-Type-Volume-OntapConfiguration"></a>
The configuration of an Amazon FSx for NetApp ONTAP volume.  
Type: [OntapVolumeConfiguration](API_OntapVolumeConfiguration.md) object  
Required: No

 ** OpenZFSConfiguration **   <a name="FSx-Type-Volume-OpenZFSConfiguration"></a>
The configuration of an Amazon FSx for OpenZFS volume.  
Type: [OpenZFSVolumeConfiguration](API_OpenZFSVolumeConfiguration.md) object  
Required: No

 ** ResourceARN **   <a name="FSx-Type-Volume-ResourceARN"></a>
The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify AWS resources. We require an ARN when you need to specify a resource unambiguously across all of AWS. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 512.  
Pattern: `^arn:(?=[^:]+:fsx:[^:]+:\d{12}:)((|(?=[a-z0-9-.]{1,63})(?!\d{1,3}(\.\d{1,3}){3})(?![^:]*-{2})(?![^:]*-\.)(?![^:]*\.-)[a-z0-9].*(?<!-)):){4}(?!/).{0,1024}$`   
Required: No

 ** Tags **   <a name="FSx-Type-Volume-Tags"></a>
A list of `Tag` values, with a maximum of 50 elements.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

 ** VolumeId **   <a name="FSx-Type-Volume-VolumeId"></a>
The system-generated, unique ID of the volume.  
Type: String  
Length Constraints: Fixed length of 23.  
Pattern: `^(fsvol-[0-9a-f]{17,})$`   
Required: No

 ** VolumeType **   <a name="FSx-Type-Volume-VolumeType"></a>
The type of the volume.  
Type: String  
Valid Values: `ONTAP | OPENZFS`   
Required: No

## See Also
<a name="API_Volume_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/Volume) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/Volume) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/Volume) 