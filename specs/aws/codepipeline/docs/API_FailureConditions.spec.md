---
id: "@specs/aws/codepipeline/docs/API_FailureConditions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS FailureConditions"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# FailureConditions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_FailureConditions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# FailureConditions
<a name="API_FailureConditions"></a>

The configuration that specifies the result, such as rollback, to occur upon stage failure. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html). 

## Contents
<a name="API_FailureConditions_Contents"></a>

 ** conditions **   <a name="CodePipeline-Type-FailureConditions-conditions"></a>
The conditions that are configured as failure conditions. For more information about conditions, see [Stage conditions](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-conditions.html) and [How do stage conditions work?](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-how-it-works-conditions.html).  
Type: Array of [Condition](API_Condition.md) objects  
Array Members: Fixed number of 1 item.  
Required: No

 ** result **   <a name="CodePipeline-Type-FailureConditions-result"></a>
The specified result for when the failure conditions are met, such as rolling back the stage.  
Type: String  
Valid Values: `ROLLBACK | FAIL | RETRY | SKIP`   
Required: No

 ** retryConfiguration **   <a name="CodePipeline-Type-FailureConditions-retryConfiguration"></a>
The retry configuration specifies automatic retry for a failed stage, along with the configured retry mode.  
Type: [RetryConfiguration](API_RetryConfiguration.md) object  
Required: No

## See Also
<a name="API_FailureConditions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/FailureConditions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/FailureConditions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/FailureConditions) 