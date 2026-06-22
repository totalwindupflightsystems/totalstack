---
id: "@specs/aws/redshift/docs/API_ClusterParameterStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ClusterParameterStatus"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ClusterParameterStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ClusterParameterStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ClusterParameterStatus
<a name="API_ClusterParameterStatus"></a>

Describes the status of a parameter group.

## Contents
<a name="API_ClusterParameterStatus_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** ParameterApplyErrorDescription **   
The error that prevented the parameter from being applied to the database.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ParameterApplyStatus **   
The status of the parameter that indicates whether the parameter is in sync with the database, waiting for a cluster reboot, or encountered an error when being applied.  
The following are possible statuses and descriptions.  
+  `in-sync`: The parameter value is in sync with the database.
+  `pending-reboot`: The parameter value will be applied after the cluster reboots.
+  `applying`: The parameter value is being applied to the database.
+  `invalid-parameter`: Cannot apply the parameter value because it has an invalid value or syntax.
+  `apply-deferred`: The parameter contains static property changes. The changes are deferred until the cluster reboots.
+  `apply-error`: Cannot connect to the cluster. The parameter change will be applied after the cluster reboots.
+  `unknown-error`: Cannot apply the parameter change right now. The change will be applied after the cluster reboots.
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ParameterName **   
The name of the parameter.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## See Also
<a name="API_ClusterParameterStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ClusterParameterStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ClusterParameterStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ClusterParameterStatus) 