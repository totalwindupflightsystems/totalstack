---
id: "@specs/aws/redshift/docs/API_DeleteRedshiftIdcApplication"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteRedshiftIdcApplication"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DeleteRedshiftIdcApplication

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DeleteRedshiftIdcApplication
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteRedshiftIdcApplication
<a name="API_DeleteRedshiftIdcApplication"></a>

Deletes an Amazon Redshift IAM Identity Center application.

## Request Parameters
<a name="API_DeleteRedshiftIdcApplication_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** RedshiftIdcApplicationArn **   
The ARN for a deleted Amazon Redshift IAM Identity Center application.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Errors
<a name="API_DeleteRedshiftIdcApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependentServiceAccessDenied **   
A dependent service denied access for the integration.  
HTTP Status Code: 403

 ** DependentServiceUnavailableFault **   
Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.  
HTTP Status Code: 400

 ** RedshiftIdcApplicationNotExists **   
The application you attempted to find doesn't exist.  
HTTP Status Code: 404

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteRedshiftIdcApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DeleteRedshiftIdcApplication) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DeleteRedshiftIdcApplication) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DeleteRedshiftIdcApplication) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DeleteRedshiftIdcApplication) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DeleteRedshiftIdcApplication) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DeleteRedshiftIdcApplication) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DeleteRedshiftIdcApplication) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DeleteRedshiftIdcApplication) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DeleteRedshiftIdcApplication) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DeleteRedshiftIdcApplication) 