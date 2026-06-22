---
id: "@specs/aws/batch/docs/API_Ulimit"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Ulimit"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# Ulimit

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_Ulimit
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Ulimit
<a name="API_Ulimit"></a>

The `ulimit` settings to pass to the container. For more information, see [Ulimit](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_Ulimit.html).

**Note**  
This object isn't applicable to jobs that are running on Fargate resources.

## Contents
<a name="API_Ulimit_Contents"></a>

 ** hardLimit **   <a name="Batch-Type-Ulimit-hardLimit"></a>
The hard limit for the `ulimit` type.   
Type: Integer  
Required: Yes

 ** name **   <a name="Batch-Type-Ulimit-name"></a>
The `type` of the `ulimit`. Valid values are: `core` \| `cpu` \| `data` \| `fsize` \| `locks` \| `memlock` \| `msgqueue` \| `nice` \| `nofile` \| `nproc` \| `rss` \| `rtprio` \| `rttime` \| `sigpending` \| `stack`.  
Type: String  
Required: Yes

 ** softLimit **   <a name="Batch-Type-Ulimit-softLimit"></a>
The soft limit for the `ulimit` type.  
Type: Integer  
Required: Yes

## See Also
<a name="API_Ulimit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/Ulimit) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/Ulimit) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/Ulimit) 