---
id: "@specs/aws/emr/docs/API_GetAutoTerminationPolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetAutoTerminationPolicy"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# GetAutoTerminationPolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_GetAutoTerminationPolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetAutoTerminationPolicy
<a name="API_GetAutoTerminationPolicy"></a>

Returns the auto-termination policy for an Amazon EMR cluster.

## Request Syntax
<a name="API_GetAutoTerminationPolicy_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetAutoTerminationPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_GetAutoTerminationPolicy_RequestSyntax) **   <a name="EMR-GetAutoTerminationPolicy-request-ClusterId"></a>
Specifies the ID of the Amazon EMR cluster for which the auto-termination policy will be fetched.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

## Response Syntax
<a name="API_GetAutoTerminationPolicy_ResponseSyntax"></a>

```
{
   "AutoTerminationPolicy": { 
      "IdleTimeout": number
   }
}
```

## Response Elements
<a name="API_GetAutoTerminationPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutoTerminationPolicy](#API_GetAutoTerminationPolicy_ResponseSyntax) **   <a name="EMR-GetAutoTerminationPolicy-response-AutoTerminationPolicy"></a>
Specifies the auto-termination policy that is attached to an Amazon EMR cluster.   
Type: [AutoTerminationPolicy](API_AutoTerminationPolicy.md) object

## Errors
<a name="API_GetAutoTerminationPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetAutoTerminationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/GetAutoTerminationPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/GetAutoTerminationPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/GetAutoTerminationPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/GetAutoTerminationPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/GetAutoTerminationPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/GetAutoTerminationPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/GetAutoTerminationPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/GetAutoTerminationPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/GetAutoTerminationPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/GetAutoTerminationPolicy) 