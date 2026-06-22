---
id: "@specs/aws/batch/docs/API_ServiceEnvironmentOrder"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ServiceEnvironmentOrder"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ServiceEnvironmentOrder

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ServiceEnvironmentOrder
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ServiceEnvironmentOrder
<a name="API_ServiceEnvironmentOrder"></a>

Specifies the order of a service environment for a job queue. This determines the priority order when multiple service environments are associated with the same job queue.

## Contents
<a name="API_ServiceEnvironmentOrder_Contents"></a>

 ** order **   <a name="Batch-Type-ServiceEnvironmentOrder-order"></a>
The order of the service environment. Job queues with a higher priority are evaluated first when associated with the same service environment.  
Type: Integer  
Required: Yes

 ** serviceEnvironment **   <a name="Batch-Type-ServiceEnvironmentOrder-serviceEnvironment"></a>
The name or ARN of the service environment.  
Type: String  
Required: Yes

## See Also
<a name="API_ServiceEnvironmentOrder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ServiceEnvironmentOrder) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ServiceEnvironmentOrder) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ServiceEnvironmentOrder) 