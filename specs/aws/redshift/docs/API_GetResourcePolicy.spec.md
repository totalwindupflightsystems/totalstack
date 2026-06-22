---
id: "@specs/aws/redshift/docs/API_GetResourcePolicy"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetResourcePolicy"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# GetResourcePolicy

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_GetResourcePolicy
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetResourcePolicy
<a name="API_GetResourcePolicy"></a>

Get the resource policy for a specified resource.

## Request Parameters
<a name="API_GetResourcePolicy_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ResourceArn **   
The Amazon Resource Name (ARN) of the resource of which its resource policy is fetched.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Response Elements
<a name="API_GetResourcePolicy_ResponseElements"></a>

The following element is returned by the service.

 ** ResourcePolicy **   
The content of the resource policy.  
Type: [ResourcePolicy](API_ResourcePolicy.md) object

## Errors
<a name="API_GetResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidPolicyFault **   
The resource policy isn't valid.  
HTTP Status Code: 400

 ** ResourceNotFoundFault **   
The resource could not be found.  
HTTP Status Code: 404

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_GetResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/GetResourcePolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/GetResourcePolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/GetResourcePolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/GetResourcePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/GetResourcePolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/GetResourcePolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/GetResourcePolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/GetResourcePolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/GetResourcePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/GetResourcePolicy) 