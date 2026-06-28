---
id: "@specs/aws/fsx/docs/API_SvmEndpoints"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SvmEndpoints"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# SvmEndpoints

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_SvmEndpoints
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SvmEndpoints
<a name="API_SvmEndpoints"></a>

An Amazon FSx for NetApp ONTAP storage virtual machine (SVM) has the following endpoints that are used to access data or to manage the SVM using the NetApp ONTAP CLI, REST API, or NetApp CloudManager.

## Contents
<a name="API_SvmEndpoints_Contents"></a>

 ** Iscsi **   <a name="FSx-Type-SvmEndpoints-Iscsi"></a>
An endpoint for connecting using the Internet Small Computer Systems Interface (iSCSI) protocol.  
Type: [SvmEndpoint](API_SvmEndpoint.md) object  
Required: No

 ** Management **   <a name="FSx-Type-SvmEndpoints-Management"></a>
An endpoint for managing SVMs using the NetApp ONTAP CLI, NetApp ONTAP API, or NetApp CloudManager.  
Type: [SvmEndpoint](API_SvmEndpoint.md) object  
Required: No

 ** Nfs **   <a name="FSx-Type-SvmEndpoints-Nfs"></a>
An endpoint for connecting using the Network File System (NFS) protocol.  
Type: [SvmEndpoint](API_SvmEndpoint.md) object  
Required: No

 ** Smb **   <a name="FSx-Type-SvmEndpoints-Smb"></a>
An endpoint for connecting using the Server Message Block (SMB) protocol.  
Type: [SvmEndpoint](API_SvmEndpoint.md) object  
Required: No

## See Also
<a name="API_SvmEndpoints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/SvmEndpoints) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/SvmEndpoints) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/SvmEndpoints) 