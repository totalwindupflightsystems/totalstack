---
id: "@specs/aws/fsx/docs/API_FileSystemEndpoints"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FileSystemEndpoints"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# FileSystemEndpoints

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_FileSystemEndpoints
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FileSystemEndpoints
<a name="API_FileSystemEndpoints"></a>

An Amazon FSx for NetApp ONTAP file system has the following endpoints that are used to access data or to manage the file system using the NetApp ONTAP CLI, REST API, or NetApp SnapMirror.

## Contents
<a name="API_FileSystemEndpoints_Contents"></a>

 ** Intercluster **   <a name="FSx-Type-FileSystemEndpoints-Intercluster"></a>
An endpoint for managing your file system by setting up NetApp SnapMirror with other ONTAP systems.  
Type: [FileSystemEndpoint](API_FileSystemEndpoint.md) object  
Required: No

 ** Management **   <a name="FSx-Type-FileSystemEndpoints-Management"></a>
An endpoint for managing your file system using the NetApp ONTAP CLI and NetApp ONTAP API.  
Type: [FileSystemEndpoint](API_FileSystemEndpoint.md) object  
Required: No

## See Also
<a name="API_FileSystemEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/FileSystemEndpoints) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/FileSystemEndpoints) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/FileSystemEndpoints) 