---
id: "@specs/aws/fsx/docs/API_OpenZFSClientConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OpenZFSClientConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# OpenZFSClientConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_OpenZFSClientConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OpenZFSClientConfiguration
<a name="API_OpenZFSClientConfiguration"></a>

Specifies who can mount an OpenZFS file system and the options available while mounting the file system.

## Contents
<a name="API_OpenZFSClientConfiguration_Contents"></a>

 ** Clients **   <a name="FSx-Type-OpenZFSClientConfiguration-Clients"></a>
A value that specifies who can mount the file system. You can provide a wildcard character (`*`), an IP address (`0.0.0.0`), or a CIDR address (`192.0.2.0/24`). By default, Amazon FSx uses the wildcard character when specifying the client.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[ -~]{1,128}$`   
Required: Yes

 ** Options **   <a name="FSx-Type-OpenZFSClientConfiguration-Options"></a>
The options to use when mounting the file system. For a list of options that you can use with Network File System (NFS), see the [exports(5) - Linux man page](https://linux.die.net/man/5/exports). When choosing your options, consider the following:  
+  `crossmnt` is used by default. If you don't specify `crossmnt` when changing the client configuration, you won't be able to see or access snapshots in your file system's snapshot directory.
+  `sync` is used by default. If you instead specify `async`, the system acknowledges writes before writing to disk. If the system crashes before the writes are finished, you lose the unwritten data. 
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 20 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[ -~]{1,128}$`   
Required: Yes

## See Also
<a name="API_OpenZFSClientConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/OpenZFSClientConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/OpenZFSClientConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/OpenZFSClientConfiguration) 