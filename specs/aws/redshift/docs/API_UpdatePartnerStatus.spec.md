---
id: "@specs/aws/redshift/docs/API_UpdatePartnerStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdatePartnerStatus"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# UpdatePartnerStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_UpdatePartnerStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdatePartnerStatus
<a name="API_UpdatePartnerStatus"></a>

Updates the status of a partner integration.

## Request Parameters
<a name="API_UpdatePartnerStatus_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AccountId **   
The AWS account ID that owns the cluster.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]+$`   
Required: Yes

 ** ClusterIdentifier **   
The cluster identifier of the cluster whose partner integration status is being updated.  
Type: String  
Length Constraints: Maximum length of 63.  
Pattern: `^[a-zA-Z0-9\-]+$`   
Required: Yes

 ** DatabaseName **   
The name of the database whose partner integration status is being updated.  
Type: String  
Length Constraints: Maximum length of 127.  
Pattern: `^[\p{L}_][\p{L}\p{N}@$#_]+$`   
Required: Yes

 ** PartnerName **   
The name of the partner whose integration status is being updated.  
Type: String  
Length Constraints: Maximum length of 255.  
Pattern: `^[a-zA-Z0-9\-_]+$`   
Required: Yes

 ** Status **   
The value of the updated status.  
Type: String  
Valid Values: `Active | Inactive | RuntimeFailure | ConnectionFailure`   
Required: Yes

 ** StatusMessage **   
The status message provided by the partner.  
Type: String  
Length Constraints: Maximum length of 262144.  
Pattern: `^[\x20-\x7E]+$`   
Required: No

## Response Elements
<a name="API_UpdatePartnerStatus_ResponseElements"></a>

The following elements are returned by the service.

 ** DatabaseName **   
The name of the database that receives data from the partner.  
Type: String  
Length Constraints: Maximum length of 127.  
Pattern: `^[\p{L}_][\p{L}\p{N}@$#_]+$` 

 ** PartnerName **   
The name of the partner that is authorized to send data.  
Type: String  
Length Constraints: Maximum length of 255.  
Pattern: `^[a-zA-Z0-9\-_]+$` 

## Errors
<a name="API_UpdatePartnerStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** PartnerNotFound **   
The name of the partner was not found.  
HTTP Status Code: 404

 ** UnauthorizedPartnerIntegration **   
The partner integration is not authorized.  
HTTP Status Code: 401

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## See Also
<a name="API_UpdatePartnerStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/UpdatePartnerStatus) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/UpdatePartnerStatus) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/UpdatePartnerStatus) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/UpdatePartnerStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/UpdatePartnerStatus) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/UpdatePartnerStatus) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/UpdatePartnerStatus) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/UpdatePartnerStatus) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/UpdatePartnerStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/UpdatePartnerStatus) 