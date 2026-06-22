---
id: "@specs/aws/redshift/docs/API_CreateAuthenticationProfile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAuthenticationProfile"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# CreateAuthenticationProfile

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_CreateAuthenticationProfile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAuthenticationProfile
<a name="API_CreateAuthenticationProfile"></a>

Creates an authentication profile with the specified parameters.

## Request Parameters
<a name="API_CreateAuthenticationProfile_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AuthenticationProfileContent **   
The content of the authentication profile in JSON format. The maximum length of the JSON string is determined by a quota for your account.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** AuthenticationProfileName **   
The name of the authentication profile to be created.  
Type: String  
Length Constraints: Maximum length of 63.  
Pattern: `^[a-zA-Z0-9\-]+$`   
Required: Yes

## Response Elements
<a name="API_CreateAuthenticationProfile_ResponseElements"></a>

The following elements are returned by the service.

 ** AuthenticationProfileContent **   
The content of the authentication profile in JSON format.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** AuthenticationProfileName **   
The name of the authentication profile that was created.  
Type: String  
Length Constraints: Maximum length of 63.  
Pattern: `^[a-zA-Z0-9\-]+$` 

## Errors
<a name="API_CreateAuthenticationProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthenticationProfileAlreadyExistsFault **   
The authentication profile already exists.  
HTTP Status Code: 400

 ** AuthenticationProfileQuotaExceededFault **   
The size or number of authentication profiles has exceeded the quota. The maximum length of the JSON string and maximum number of authentication profiles is determined by a quota for your account.  
HTTP Status Code: 400

 ** InvalidAuthenticationProfileRequestFault **   
The authentication profile request is not valid. The profile name can't be null or empty. The authentication profile API operation must be available in the AWS Region.  
HTTP Status Code: 400

## See Also
<a name="API_CreateAuthenticationProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/CreateAuthenticationProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/CreateAuthenticationProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/CreateAuthenticationProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/CreateAuthenticationProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/CreateAuthenticationProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/CreateAuthenticationProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/CreateAuthenticationProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/CreateAuthenticationProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/CreateAuthenticationProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/CreateAuthenticationProfile) 