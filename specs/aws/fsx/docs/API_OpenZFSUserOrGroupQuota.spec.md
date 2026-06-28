---
id: "@specs/aws/fsx/docs/API_OpenZFSUserOrGroupQuota"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OpenZFSUserOrGroupQuota"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# OpenZFSUserOrGroupQuota

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_OpenZFSUserOrGroupQuota
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OpenZFSUserOrGroupQuota
<a name="API_OpenZFSUserOrGroupQuota"></a>

Used to configure quotas that define how much storage a user or group can use on an FSx for OpenZFS volume. For more information, see [Volume properties](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/managing-volumes.html#volume-properties) in the FSx for OpenZFS User Guide. 

## Contents
<a name="API_OpenZFSUserOrGroupQuota_Contents"></a>

 ** Id **   <a name="FSx-Type-OpenZFSUserOrGroupQuota-Id"></a>
The ID of the user or group that the quota applies to.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 2147483647.  
Required: Yes

 ** StorageCapacityQuotaGiB **   <a name="FSx-Type-OpenZFSUserOrGroupQuota-StorageCapacityQuotaGiB"></a>
The user or group's storage quota, in gibibytes (GiB).  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 2147483647.  
Required: Yes

 ** Type **   <a name="FSx-Type-OpenZFSUserOrGroupQuota-Type"></a>
Specifies whether the quota applies to a user or group.  
Type: String  
Valid Values: `USER | GROUP`   
Required: Yes

## See Also
<a name="API_OpenZFSUserOrGroupQuota_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/OpenZFSUserOrGroupQuota) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/OpenZFSUserOrGroupQuota) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/OpenZFSUserOrGroupQuota) 