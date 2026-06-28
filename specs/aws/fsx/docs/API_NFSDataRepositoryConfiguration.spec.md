---
id: "@specs/aws/fsx/docs/API_NFSDataRepositoryConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NFSDataRepositoryConfiguration"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# NFSDataRepositoryConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_NFSDataRepositoryConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NFSDataRepositoryConfiguration
<a name="API_NFSDataRepositoryConfiguration"></a>

The configuration for a data repository association that links an Amazon File Cache resource to an NFS data repository.

## Contents
<a name="API_NFSDataRepositoryConfiguration_Contents"></a>

 ** Version **   <a name="FSx-Type-NFSDataRepositoryConfiguration-Version"></a>
The version of the NFS (Network File System) protocol of the NFS data repository. Currently, the only supported value is `NFS3`, which indicates that the data repository must support the NFSv3 protocol.  
Type: String  
Valid Values: `NFS3`   
Required: Yes

 ** AutoExportPolicy **   <a name="FSx-Type-NFSDataRepositoryConfiguration-AutoExportPolicy"></a>
This parameter is not supported for Amazon File Cache.  
Type: [AutoExportPolicy](API_AutoExportPolicy.md) object  
Required: No

 ** DnsIps **   <a name="FSx-Type-NFSDataRepositoryConfiguration-DnsIps"></a>
A list of up to 2 IP addresses of DNS servers used to resolve the NFS file system domain name. The provided IP addresses can either be the IP addresses of a DNS forwarder or resolver that the customer manages and runs inside the customer VPC, or the IP addresses of the on-premises DNS servers.  
Type: Array of strings  
Array Members: Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 45.  
Pattern: `(^((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))$|^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$)`   
Required: No

## See Also
<a name="API_NFSDataRepositoryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/NFSDataRepositoryConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/NFSDataRepositoryConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/NFSDataRepositoryConfiguration) 