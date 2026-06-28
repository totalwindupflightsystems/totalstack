---
id: "@specs/aws/fsx/docs/API_LustreRootSquashConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LustreRootSquashConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# LustreRootSquashConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_LustreRootSquashConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LustreRootSquashConfiguration
<a name="API_LustreRootSquashConfiguration"></a>

The configuration for Lustre root squash used to restrict root-level access from clients that try to access your FSx for Lustre file system as root. Use the `RootSquash` parameter to enable root squash. To learn more about Lustre root squash, see [Lustre root squash](https://docs.aws.amazon.com/fsx/latest/LustreGuide/root-squash.html).

You can also use the `NoSquashNids` parameter to provide an array of clients who are not affected by the root squash setting. These clients will access the file system as root, with unrestricted privileges.

## Contents
<a name="API_LustreRootSquashConfiguration_Contents"></a>

 ** NoSquashNids **   <a name="FSx-Type-LustreRootSquashConfiguration-NoSquashNids"></a>
When root squash is enabled, you can optionally specify an array of NIDs of clients for which root squash does not apply. A client NID is a Lustre Network Identifier used to uniquely identify a client. You can specify the NID as either a single address or a range of addresses:  
+ A single address is described in standard Lustre NID format by specifying the client’s IP address followed by the Lustre network ID (for example, `10.0.1.6@tcp`).
+ An address range is described using a dash to separate the range (for example, `10.0.[2-10].[1-255]@tcp`).
Type: Array of strings  
Array Members: Maximum number of 64 items.  
Length Constraints: Minimum length of 11. Maximum length of 43.  
Pattern: `^([0-9\[\]\-]*\.){3}([0-9\[\]\-]*)@tcp$`   
Required: No

 ** RootSquash **   <a name="FSx-Type-LustreRootSquashConfiguration-RootSquash"></a>
You enable root squash by setting a user ID (UID) and group ID (GID) for the file system in the format `UID:GID` (for example, `365534:65534`). The UID and GID values can range from `0` to `4294967294`:  
+ A non-zero value for UID and GID enables root squash. The UID and GID values can be different, but each must be a non-zero value.
+ A value of `0` (zero) for UID and GID indicates root, and therefore disables root squash.
When root squash is enabled, the user ID and group ID of a root user accessing the file system are re-mapped to the UID and GID you provide.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 21.  
Pattern: `^([0-9]{1,10}):([0-9]{1,10})$`   
Required: No

## See Also
<a name="API_LustreRootSquashConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/LustreRootSquashConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/LustreRootSquashConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/LustreRootSquashConfiguration) 