---
id: "@specs/aws/appsync/docs/API_SyncConfig"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SyncConfig"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# SyncConfig

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_SyncConfig
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SyncConfig
<a name="API_SyncConfig"></a>

Describes a Sync configuration for a resolver.

Specifies which Conflict Detection strategy and Resolution strategy to use when the resolver is invoked.

## Contents
<a name="API_SyncConfig_Contents"></a>

 ** conflictDetection **   <a name="appsync-Type-SyncConfig-conflictDetection"></a>
The Conflict Detection strategy to use.  
+  **VERSION**: Detect conflicts based on object versions for this resolver.
+  **NONE**: Do not detect conflicts when invoking this resolver.
Type: String  
Valid Values: `VERSION | NONE`   
Required: No

 ** conflictHandler **   <a name="appsync-Type-SyncConfig-conflictHandler"></a>
The Conflict Resolution strategy to perform in the event of a conflict.  
+  **OPTIMISTIC\_CONCURRENCY**: Resolve conflicts by rejecting mutations when versions don't match the latest version at the server.
+  **AUTOMERGE**: Resolve conflicts with the Automerge conflict resolution strategy.
+  **LAMBDA**: Resolve conflicts with an AWS Lambda function supplied in the `LambdaConflictHandlerConfig`.
Type: String  
Valid Values: `OPTIMISTIC_CONCURRENCY | LAMBDA | AUTOMERGE | NONE`   
Required: No

 ** lambdaConflictHandlerConfig **   <a name="appsync-Type-SyncConfig-lambdaConflictHandlerConfig"></a>
The `LambdaConflictHandlerConfig` when configuring `LAMBDA` as the Conflict Handler.  
Type: [LambdaConflictHandlerConfig](API_LambdaConflictHandlerConfig.md) object  
Required: No

## See Also
<a name="API_SyncConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/SyncConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/SyncConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/SyncConfig) 