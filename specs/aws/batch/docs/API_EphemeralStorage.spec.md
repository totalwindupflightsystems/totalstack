---
id: "@specs/aws/batch/docs/API_EphemeralStorage"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS EphemeralStorage"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# EphemeralStorage

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_EphemeralStorage
> **target_lang:** meta — documentation tier. ALL sections preserved.



# EphemeralStorage
<a name="API_EphemeralStorage"></a>

The amount of ephemeral storage to allocate for the task. This parameter is used to expand the total amount of ephemeral storage available, beyond the default amount, for tasks hosted on AWS Fargate.

## Contents
<a name="API_EphemeralStorage_Contents"></a>

 ** sizeInGiB **   <a name="Batch-Type-EphemeralStorage-sizeInGiB"></a>
The total amount, in GiB, of ephemeral storage to set for the task. The minimum supported value is `21` GiB and the maximum supported value is `200` GiB.  
Type: Integer  
Required: Yes

## See Also
<a name="API_EphemeralStorage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EphemeralStorage) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EphemeralStorage) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EphemeralStorage) 