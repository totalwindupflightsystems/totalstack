---
id: "@specs/aws/redshift/docs/API_ModifyAuthenticationProfile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyAuthenticationProfile"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ModifyAuthenticationProfile

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ModifyAuthenticationProfile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyAuthenticationProfile
<a name="API_ModifyAuthenticationProfile"></a>

Modifies an authentication profile.

## Request Parameters
<a name="API_ModifyAuthenticationProfile_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AuthenticationProfileContent **   
The new content of the authentication profile in JSON format. The maximum length of the JSON string is determined by a quota for your account.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** AuthenticationProfileName **   
The name of the authentication profile to replace.  
Type: String  
Length Constraints: Maximum length of 63.  
Pattern: `^[a-zA-Z0-9\-]+$`   
Required: Yes

## Response Elements
<a name="API_ModifyAuthenticationProfile_ResponseElements"></a>

The following elements are returned by the service.

 ** AuthenticationProfileContent **   
The updated content of the authentication profile in JSON format.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** AuthenticationProfileName **   
The name of the authentication profile that was replaced.  
Type: String  
Length Constraints: Maximum length of 63.  
Pattern: `^[a-zA-Z0-9\-]+$` 

## Errors
<a name="API_ModifyAuthenticationProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthenticationProfileNotFoundFault **   
The authentication profile can't be found.  
HTTP Status Code: 404

 ** AuthenticationProfileQuotaExceededFault **   
The size or number of authentication profiles has exceeded the quota. The maximum length of the JSON string and maximum number of authentication profiles is determined by a quota for your account.  
HTTP Status Code: 400

 ** InvalidAuthenticationProfileRequestFault **   
The authentication profile request is not valid. The profile name can't be null or empty. The authentication profile API operation must be available in the AWS Region.  
HTTP Status Code: 400

## See Also
<a name="API_ModifyAuthenticationProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/ModifyAuthenticationProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/ModifyAuthenticationProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ModifyAuthenticationProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/ModifyAuthenticationProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ModifyAuthenticationProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/ModifyAuthenticationProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/ModifyAuthenticationProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/ModifyAuthenticationProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/ModifyAuthenticationProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ModifyAuthenticationProfile) 