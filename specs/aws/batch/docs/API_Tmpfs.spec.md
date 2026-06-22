---
id: "@specs/aws/batch/docs/API_Tmpfs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tmpfs"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# Tmpfs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_Tmpfs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tmpfs
<a name="API_Tmpfs"></a>

The container path, mount options, and size of the `tmpfs` mount.

**Note**  
This object isn't applicable to jobs that are running on Fargate resources.

## Contents
<a name="API_Tmpfs_Contents"></a>

 ** containerPath **   <a name="Batch-Type-Tmpfs-containerPath"></a>
The absolute file path in the container where the `tmpfs` volume is mounted.  
Type: String  
Required: Yes

 ** size **   <a name="Batch-Type-Tmpfs-size"></a>
The size (in MiB) of the `tmpfs` volume.  
Type: Integer  
Required: Yes

 ** mountOptions **   <a name="Batch-Type-Tmpfs-mountOptions"></a>
The list of `tmpfs` volume mount options.  
Valid values: "`defaults`" \| "`ro`" \| "`rw`" \| "`suid`" \| "`nosuid`" \| "`dev`" \| "`nodev`" \| "`exec`" \| "`noexec`" \| "`sync`" \| "`async`" \| "`dirsync`" \| "`remount`" \| "`mand`" \| "`nomand`" \| "`atime`" \| "`noatime`" \| "`diratime`" \| "`nodiratime`" \| "`bind`" \| "`rbind" | "unbindable" | "runbindable" | "private" | "rprivate" | "shared" | "rshared" | "slave" | "rslave" | "relatime`" \| "`norelatime`" \| "`strictatime`" \| "`nostrictatime`" \| "`mode`" \| "`uid`" \| "`gid`" \| "`nr_inodes`" \| "`nr_blocks`" \| "`mpol`"  
Type: Array of strings  
Required: No

## See Also
<a name="API_Tmpfs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/Tmpfs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/Tmpfs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/Tmpfs) 