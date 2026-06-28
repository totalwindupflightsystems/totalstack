---
id: "@specs/aws/fsx/docs/API_FileCacheNFSConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FileCacheNFSConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# FileCacheNFSConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_FileCacheNFSConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FileCacheNFSConfiguration
<a name="API_FileCacheNFSConfiguration"></a>

The configuration for an NFS data repository association (DRA) created during the creation of the Amazon File Cache resource.

## Contents
<a name="API_FileCacheNFSConfiguration_Contents"></a>

 ** Version **   <a name="FSx-Type-FileCacheNFSConfiguration-Version"></a>
The version of the NFS (Network File System) protocol of the NFS data repository. The only supported value is `NFS3`, which indicates that the data repository must support the NFSv3 protocol.  
Type: String  
Valid Values: `NFS3`   
Required: Yes

 ** DnsIps **   <a name="FSx-Type-FileCacheNFSConfiguration-DnsIps"></a>
A list of up to 2 IP addresses of DNS servers used to resolve the NFS file system domain name. The provided IP addresses can either be the IP addresses of a DNS forwarder or resolver that the customer manages and runs inside the customer VPC, or the IP addresses of the on-premises DNS servers.  
Type: Array of strings  
Array Members: Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 45.  
Pattern: `(^((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$)`   
Required: No

## See Also
<a name="API_FileCacheNFSConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/FileCacheNFSConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/FileCacheNFSConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/FileCacheNFSConfiguration) 