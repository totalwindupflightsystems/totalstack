---
id: "@specs/aws/mwaa/docs/API_LastUpdate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LastUpdate"
status: active
depends_on:
  - "@specs/aws/mwaa/meta"
---

# LastUpdate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/mwaa/docs/API_LastUpdate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LastUpdate
<a name="API_LastUpdate"></a>

Describes the status of the last update on the environment, and any errors that were encountered.

## Contents
<a name="API_LastUpdate_Contents"></a>

 ** CreatedAt **   <a name="mwaa-Type-LastUpdate-CreatedAt"></a>
The day and time of the last update on the environment.  
Type: Timestamp  
Required: No

 ** Error **   <a name="mwaa-Type-LastUpdate-Error"></a>
The error that was encountered during the last update of the environment.  
Type: [UpdateError](API_UpdateError.md) object  
Required: No

 ** Source **   <a name="mwaa-Type-LastUpdate-Source"></a>
The source of the last update to the environment. Includes internal processes by Amazon MWAA, such as an environment maintenance update.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `.+`   
Required: No

 ** Status **   <a name="mwaa-Type-LastUpdate-Status"></a>
The status of the last update on the environment.  
Type: String  
Valid Values: `SUCCESS | PENDING | FAILED`   
Required: No

 ** WorkerReplacementStrategy **   <a name="mwaa-Type-LastUpdate-WorkerReplacementStrategy"></a>
The worker replacement strategy used in the last update of the environment.  
Type: String  
Valid Values: `FORCED | GRACEFUL`   
Required: No

## See Also
<a name="API_LastUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/LastUpdate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/LastUpdate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/LastUpdate) 