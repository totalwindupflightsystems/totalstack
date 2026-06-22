---
id: "@specs/aws/batch/docs/API_ShareAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ShareAttributes"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ShareAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ShareAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ShareAttributes
<a name="API_ShareAttributes"></a>

Specifies the weights for the share identifiers for the fair-share policy. Share identifiers that aren't included have a default weight of `1.0`.

## Contents
<a name="API_ShareAttributes_Contents"></a>

 ** shareIdentifier **   <a name="Batch-Type-ShareAttributes-shareIdentifier"></a>
A share identifier or share identifier prefix. If the string ends with an asterisk (\*), this entry specifies the weight factor to use for share identifiers that start with that prefix. The list of share identifiers in a fair-share policy can't overlap. For example, you can't have one that specifies a `shareIdentifier` of `UserA*` and another that specifies a `shareIdentifier` of `UserA1`.  
There can be no more than 500 share identifiers active in a job queue.  
The string is limited to 255 alphanumeric characters, and can be followed by an asterisk (\*).  
Type: String  
Required: Yes

 ** weightFactor **   <a name="Batch-Type-ShareAttributes-weightFactor"></a>
The weight factor for the share identifier. The default value is 1.0. A lower value has a higher priority for compute resources. For example, jobs that use a share identifier with a weight factor of 0.125 (1/8) get 8 times the compute resources of jobs that use a share identifier with a weight factor of 1.  
The smallest supported value is 0.0001, and the largest supported value is 999.9999.  
Type: Float  
Required: No

## See Also
<a name="API_ShareAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ShareAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ShareAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ShareAttributes) 