---
id: "@specs/aws/redshift/docs/API_ModifyAquaConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyAquaConfiguration"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ModifyAquaConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ModifyAquaConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyAquaConfiguration
<a name="API_ModifyAquaConfiguration"></a>

This operation is retired. Calling this operation does not change AQUA configuration. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator). 

## Request Parameters
<a name="API_ModifyAquaConfiguration_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The identifier of the cluster to be modified.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** AquaConfigurationStatus **   
This parameter is retired. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).  
Type: String  
Valid Values: `enabled | disabled | auto`   
Required: No

## Response Elements
<a name="API_ModifyAquaConfiguration_ResponseElements"></a>

The following element is returned by the service.

 ** AquaConfiguration **   
This parameter is retired. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).   
Type: [AquaConfiguration](API_AquaConfiguration.md) object

## Errors
<a name="API_ModifyAquaConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_ModifyAquaConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/ModifyAquaConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/ModifyAquaConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ModifyAquaConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/ModifyAquaConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ModifyAquaConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/ModifyAquaConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/ModifyAquaConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/ModifyAquaConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/ModifyAquaConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ModifyAquaConfiguration) 