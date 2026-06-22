---
id: "@specs/aws/redshift/docs/API_ModifyLakehouseConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyLakehouseConfiguration"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ModifyLakehouseConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ModifyLakehouseConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyLakehouseConfiguration
<a name="API_ModifyLakehouseConfiguration"></a>

Modifies the lakehouse configuration for a cluster. This operation allows you to manage Amazon Redshift federated permissions and AWS IAM Identity Center trusted identity propagation.

## Request Parameters
<a name="API_ModifyLakehouseConfiguration_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The unique identifier of the cluster whose lakehouse configuration you want to modify.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** CatalogName **   
The name of the Glue data catalog that will be associated with the cluster enabled with Amazon Redshift federated permissions.  
Constraints:  
+ Must contain at least one lowercase letter.
+ Can only contain lowercase letters (a-z), numbers (0-9), underscores (\_), and hyphens (-).
Pattern: `^[a-z0-9_-]*[a-z]+[a-z0-9_-]*$`   
Example: `my-catalog_01`   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `^[a-z0-9_-]*[a-z]+[a-z0-9_-]*$`   
Required: No

 ** DryRun **   
A boolean value that, if `true`, validates the request without actually modifying the lakehouse configuration. Use this to check for errors before making changes.  
Type: Boolean  
Required: No

 ** LakehouseIdcApplicationArn **   
The Amazon Resource Name (ARN) of the IAM Identity Center application used for enabling AWS IAM Identity Center trusted identity propagation on a cluster enabled with Amazon Redshift federated permissions.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** LakehouseIdcRegistration **   
Modifies the AWS IAM Identity Center trusted identity propagation on a cluster enabled with Amazon Redshift federated permissions. Valid values are `Associate` or `Disassociate`.  
Type: String  
Valid Values: `Associate | Disassociate`   
Required: No

 ** LakehouseRegistration **   
Specifies whether to register or deregister the cluster with Amazon Redshift federated permissions. Valid values are `Register` or `Deregister`.  
Type: String  
Valid Values: `Register | Deregister`   
Required: No

## Response Elements
<a name="API_ModifyLakehouseConfiguration_ResponseElements"></a>

The following elements are returned by the service.

 ** CatalogArn **   
The Amazon Resource Name (ARN) of the Glue data catalog associated with the lakehouse configuration.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** ClusterIdentifier **   
The unique identifier of the cluster associated with this lakehouse configuration.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** LakehouseIdcApplicationArn **   
The Amazon Resource Name (ARN) of the IAM Identity Center application used for enabling AWS IAM Identity Center trusted identity propagation on a cluster enabled with Amazon Redshift federated permissions.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** LakehouseRegistrationStatus **   
The current status of the lakehouse registration. Indicates whether the cluster is successfully registered with the lakehouse.  
Type: String  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_ModifyLakehouseConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** DependentServiceAccessDenied **   
A dependent service denied access for the integration.  
HTTP Status Code: 403

 ** DependentServiceUnavailableFault **   
Your request cannot be completed because a dependent internal service is temporarily unavailable. Wait 30 to 60 seconds and try again.  
HTTP Status Code: 400

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** RedshiftIdcApplicationNotExists **   
The application you attempted to find doesn't exist.  
HTTP Status Code: 404

 ** UnauthorizedOperation **   
Your account is not authorized to perform the requested operation.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_ModifyLakehouseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/ModifyLakehouseConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/ModifyLakehouseConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ModifyLakehouseConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/ModifyLakehouseConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ModifyLakehouseConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/ModifyLakehouseConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/ModifyLakehouseConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/ModifyLakehouseConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/ModifyLakehouseConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ModifyLakehouseConfiguration) 