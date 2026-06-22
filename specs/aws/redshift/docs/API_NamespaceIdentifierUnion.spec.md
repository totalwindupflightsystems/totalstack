---
id: "@specs/aws/redshift/docs/API_NamespaceIdentifierUnion"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS NamespaceIdentifierUnion"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# NamespaceIdentifierUnion

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_NamespaceIdentifierUnion
> **target_lang:** meta — documentation tier. ALL sections preserved.



# NamespaceIdentifierUnion
<a name="API_NamespaceIdentifierUnion"></a>

Object to store union of values for a provisioned cluster or serverless namespace’s identifier.

## Contents
<a name="API_NamespaceIdentifierUnion_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ProvisionedIdentifier **   
The identifier for a provisioned cluster.  
Type: [ProvisionedIdentifier](API_ProvisionedIdentifier.md) object  
Required: No

 ** ServerlessIdentifier **   
The identifier for a serverless namespace.  
Type: [ServerlessIdentifier](API_ServerlessIdentifier.md) object  
Required: No

## See Also
<a name="API_NamespaceIdentifierUnion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/NamespaceIdentifierUnion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/NamespaceIdentifierUnion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/NamespaceIdentifierUnion) 