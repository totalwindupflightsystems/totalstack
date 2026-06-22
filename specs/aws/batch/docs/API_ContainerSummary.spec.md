---
id: "@specs/aws/batch/docs/API_ContainerSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ContainerSummary"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ContainerSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ContainerSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ContainerSummary
<a name="API_ContainerSummary"></a>

An object that represents summary details of a container within a job.

## Contents
<a name="API_ContainerSummary_Contents"></a>

 ** exitCode **   <a name="Batch-Type-ContainerSummary-exitCode"></a>
The exit code to return upon completion.  
Type: Integer  
Required: No

 ** reason **   <a name="Batch-Type-ContainerSummary-reason"></a>
A short (255 max characters) human-readable string to provide additional details for a running or stopped container.  
Type: String  
Required: No

## See Also
<a name="API_ContainerSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ContainerSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ContainerSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ContainerSummary) 