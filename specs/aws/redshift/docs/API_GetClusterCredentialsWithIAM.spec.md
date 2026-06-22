---
id: "@specs/aws/redshift/docs/API_GetClusterCredentialsWithIAM"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetClusterCredentialsWithIAM"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# GetClusterCredentialsWithIAM

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_GetClusterCredentialsWithIAM
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetClusterCredentialsWithIAM
<a name="API_GetClusterCredentialsWithIAM"></a>

Returns a database user name and temporary password with temporary authorization to log in to an Amazon Redshift database. The database user is mapped 1:1 to the source AWS Identity and Access Management (IAM) identity. For more information about IAM identities, see [IAM Identities (users, user groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in the AWS Identity and Access Management User Guide.

The AWS Identity and Access Management (IAM) identity that runs this operation must have an IAM policy attached that allows access to all necessary actions and resources. For more information about permissions, see [Using identity-based policies (IAM policies)](https://docs.aws.amazon.com/redshift/latest/mgmt/redshift-iam-access-control-identity-based.html) in the Amazon Redshift Cluster Management Guide. 

## Request Parameters
<a name="API_GetClusterCredentialsWithIAM_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterIdentifier **   
The unique identifier of the cluster that contains the database for which you are requesting credentials.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Required: No

 ** CustomDomainName **   
The custom domain name for the IAM message cluster credentials.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** DbName **   
The name of the database for which you are requesting credentials. If the database name is specified, the IAM policy must allow access to the resource `dbname` for the specified database name. If the database name is not specified, access to all databases is allowed.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

 ** DurationSeconds **   
The number of seconds until the returned temporary password expires.  
Range: 900-3600. Default: 900.  
Type: Integer  
Required: No

## Response Elements
<a name="API_GetClusterCredentialsWithIAM_ResponseElements"></a>

The following elements are returned by the service.

 ** DbPassword **   
A temporary password that you provide when you connect to a database.  
Type: String

 ** DbUser **   
A database user name that you provide when you connect to a database. The database user is mapped 1:1 to the source IAM identity.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 127.

 ** Expiration **   
The time (UTC) when the temporary password expires. After this timestamp, a log in with the temporary password fails.  
Type: Timestamp

 ** NextRefreshTime **   
Reserved for future use.  
Type: Timestamp

## Errors
<a name="API_GetClusterCredentialsWithIAM_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_GetClusterCredentialsWithIAM_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/GetClusterCredentialsWithIAM) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/GetClusterCredentialsWithIAM) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/GetClusterCredentialsWithIAM) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/GetClusterCredentialsWithIAM) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/GetClusterCredentialsWithIAM) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/GetClusterCredentialsWithIAM) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/GetClusterCredentialsWithIAM) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/GetClusterCredentialsWithIAM) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/GetClusterCredentialsWithIAM) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/GetClusterCredentialsWithIAM) 