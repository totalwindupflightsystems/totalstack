---
id: "@specs/aws/fsx/docs/API_DurationSinceLastAccess"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DurationSinceLastAccess"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DurationSinceLastAccess

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DurationSinceLastAccess
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DurationSinceLastAccess
<a name="API_DurationSinceLastAccess"></a>

Defines the minimum amount of time since last access for a file to be eligible for release. Only files that have been exported to S3 and that were last accessed or modified before this point-in-time are eligible to be released from the Amazon FSx for Lustre file system.

## Contents
<a name="API_DurationSinceLastAccess_Contents"></a>

 ** Unit **   <a name="FSx-Type-DurationSinceLastAccess-Unit"></a>
The unit of time used by the `Value` parameter to determine if a file can be released, based on when it was last accessed. `DAYS` is the only supported value. This is a required parameter.  
Type: String  
Valid Values: `DAYS`   
Required: No

 ** Value **   <a name="FSx-Type-DurationSinceLastAccess-Value"></a>
An integer that represents the minimum amount of time (in days) since a file was last accessed in the file system. Only exported files with a `MAX(atime, ctime, mtime)` timestamp that is more than this amount of time in the past (relative to the task create time) will be released. The default of `Value` is `0`. This is a required parameter.  
If an exported file meets the last accessed time criteria, its file or directory path must also be specified in the `Paths` parameter of the [CreateDataRepositoryTask](API_CreateDataRepositoryTask.md) operation in order for the file to be released.
Type: Long  
Valid Range: Minimum value of 0.  
Required: No

## See Also
<a name="API_DurationSinceLastAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DurationSinceLastAccess) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DurationSinceLastAccess) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DurationSinceLastAccess) 