---
id: "@specs/aws/redshift/docs/API_DeleteAuthenticationProfile"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteAuthenticationProfile"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DeleteAuthenticationProfile

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DeleteAuthenticationProfile
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteAuthenticationProfile
<a name="API_DeleteAuthenticationProfile"></a>

Deletes an authentication profile.

## Request Parameters
<a name="API_DeleteAuthenticationProfile_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AuthenticationProfileName **   
The name of the authentication profile to delete.  
Type: String  
Length Constraints: Maximum length of 63.  
Pattern: `^[a-zA-Z0-9\-]+$`   
Required: Yes

## Response Elements
<a name="API_DeleteAuthenticationProfile_ResponseElements"></a>

The following element is returned by the service.

 ** AuthenticationProfileName **   
The name of the authentication profile that was deleted.  
Type: String  
Length Constraints: Maximum length of 63.  
Pattern: `^[a-zA-Z0-9\-]+$` 

## Errors
<a name="API_DeleteAuthenticationProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthenticationProfileNotFoundFault **   
The authentication profile can't be found.  
HTTP Status Code: 404

 ** InvalidAuthenticationProfileRequestFault **   
The authentication profile request is not valid. The profile name can't be null or empty. The authentication profile API operation must be available in the AWS Region.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteAuthenticationProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DeleteAuthenticationProfile) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DeleteAuthenticationProfile) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DeleteAuthenticationProfile) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DeleteAuthenticationProfile) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DeleteAuthenticationProfile) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DeleteAuthenticationProfile) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DeleteAuthenticationProfile) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DeleteAuthenticationProfile) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DeleteAuthenticationProfile) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DeleteAuthenticationProfile) 