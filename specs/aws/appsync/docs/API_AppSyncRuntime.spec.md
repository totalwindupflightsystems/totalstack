---
id: "@specs/aws/appsync/docs/API_AppSyncRuntime"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AppSyncRuntime"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# AppSyncRuntime

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_AppSyncRuntime
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AppSyncRuntime
<a name="API_AppSyncRuntime"></a>

Describes a runtime used by an AWS AppSync pipeline resolver or AWS AppSync function. Specifies the name and version of the runtime to use. Note that if a runtime is specified, code must also be specified.

## Contents
<a name="API_AppSyncRuntime_Contents"></a>

 ** name **   <a name="appsync-Type-AppSyncRuntime-name"></a>
The `name` of the runtime to use. Currently, the only allowed value is `APPSYNC_JS`.  
Type: String  
Valid Values: `APPSYNC_JS`   
Required: Yes

 ** runtimeVersion **   <a name="appsync-Type-AppSyncRuntime-runtimeVersion"></a>
The `version` of the runtime to use. Currently, the only allowed version is `1.0.0`.  
Type: String  
Required: Yes

## See Also
<a name="API_AppSyncRuntime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/AppSyncRuntime) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/AppSyncRuntime) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/AppSyncRuntime) 