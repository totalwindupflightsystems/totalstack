---
id: "@specs/aws/redshift/docs/API_DeregisterNamespace"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeregisterNamespace"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DeregisterNamespace

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DeregisterNamespace
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeregisterNamespace
<a name="API_DeregisterNamespace"></a>

Deregisters a cluster or serverless namespace from the AWS Glue Data Catalog.

## Request Parameters
<a name="API_DeregisterNamespace_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **ConsumerIdentifiers.member.N**   
An array containing the ID of the consumer account that you want to deregister the cluster or serverless namespace from.  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** NamespaceIdentifier **   
The unique identifier of the cluster or serverless namespace that you want to deregister.  
Type: [NamespaceIdentifierUnion](API_NamespaceIdentifierUnion.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## Response Elements
<a name="API_DeregisterNamespace_ResponseElements"></a>

The following element is returned by the service.

 ** Status **   
The registration status of the cluster or serverless namespace.  
Type: String  
Valid Values: `Registering | Deregistering` 

## Errors
<a name="API_DeregisterNamespace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** InvalidNamespaceFault **   
The namespace isn't valid because the namespace doesn't exist. Provide a valid namespace.  
HTTP Status Code: 400

## See Also
<a name="API_DeregisterNamespace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DeregisterNamespace) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DeregisterNamespace) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DeregisterNamespace) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DeregisterNamespace) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DeregisterNamespace) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DeregisterNamespace) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DeregisterNamespace) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DeregisterNamespace) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DeregisterNamespace) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DeregisterNamespace) 