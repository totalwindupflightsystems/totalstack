---
id: "@specs/aws/emr/docs/API_CreatePersistentAppUI"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreatePersistentAppUI"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# CreatePersistentAppUI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_CreatePersistentAppUI
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreatePersistentAppUI
<a name="API_CreatePersistentAppUI"></a>

Creates a persistent application user interface.

## Request Syntax
<a name="API_CreatePersistentAppUI_RequestSyntax"></a>

```
{
   "EMRContainersConfig": { 
      "JobRunId": "{{string}}"
   },
   "ProfilerType": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TargetResourceArn": "{{string}}",
   "XReferer": "{{string}}"
}
```

## Request Parameters
<a name="API_CreatePersistentAppUI_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EMRContainersConfig](#API_CreatePersistentAppUI_RequestSyntax) **   <a name="EMR-CreatePersistentAppUI-request-EMRContainersConfig"></a>
The EMR containers configuration.  
Type: [EMRContainersConfig](API_EMRContainersConfig.md) object  
Required: No

 ** [ProfilerType](#API_CreatePersistentAppUI_RequestSyntax) **   <a name="EMR-CreatePersistentAppUI-request-ProfilerType"></a>
The profiler type for the persistent application user interface.  
Type: String  
Valid Values: `SHS | TEZUI | YTS`   
Required: No

 ** [Tags](#API_CreatePersistentAppUI_RequestSyntax) **   <a name="EMR-CreatePersistentAppUI-request-Tags"></a>
Tags for the persistent application user interface.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** [TargetResourceArn](#API_CreatePersistentAppUI_RequestSyntax) **   <a name="EMR-CreatePersistentAppUI-request-TargetResourceArn"></a>
The unique Amazon Resource Name (ARN) of the target resource.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Required: Yes

 ** [XReferer](#API_CreatePersistentAppUI_RequestSyntax) **   <a name="EMR-CreatePersistentAppUI-request-XReferer"></a>
The cross reference for the persistent application user interface.  
Type: String  
Required: No

## Response Syntax
<a name="API_CreatePersistentAppUI_ResponseSyntax"></a>

```
{
   "PersistentAppUIId": "string",
   "RuntimeRoleEnabledCluster": boolean
}
```

## Response Elements
<a name="API_CreatePersistentAppUI_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PersistentAppUIId](#API_CreatePersistentAppUI_ResponseSyntax) **   <a name="EMR-CreatePersistentAppUI-response-PersistentAppUIId"></a>
The persistent application user interface identifier.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*` 

 ** [RuntimeRoleEnabledCluster](#API_CreatePersistentAppUI_ResponseSyntax) **   <a name="EMR-CreatePersistentAppUI-response-RuntimeRoleEnabledCluster"></a>
Represents if the EMR on EC2 cluster that the persisent application user interface is created for is a runtime role enabled cluster or not.  
Type: Boolean

## Errors
<a name="API_CreatePersistentAppUI_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
This exception occurs when there is an internal failure in the Amazon EMR service.    
 ** Message **   
The message associated with the exception.
HTTP Status Code: 500

 ** InvalidRequestException **   
This exception occurs when there is something wrong with user input.    
 ** ErrorCode **   
The error code associated with the exception.  
 ** Message **   
The message associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreatePersistentAppUI_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/CreatePersistentAppUI) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/CreatePersistentAppUI) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/CreatePersistentAppUI) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/CreatePersistentAppUI) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/CreatePersistentAppUI) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/CreatePersistentAppUI) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/CreatePersistentAppUI) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/CreatePersistentAppUI) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/CreatePersistentAppUI) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/CreatePersistentAppUI) 