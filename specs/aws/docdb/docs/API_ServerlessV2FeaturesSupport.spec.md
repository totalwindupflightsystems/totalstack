---
id: "@specs/aws/docdb/docs/API_ServerlessV2FeaturesSupport"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ServerlessV2FeaturesSupport"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# ServerlessV2FeaturesSupport

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_ServerlessV2FeaturesSupport
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ServerlessV2FeaturesSupport
<a name="API_ServerlessV2FeaturesSupport"></a>

Specifies any Amazon DocumentDB Serverless properties or limits that differ between Amazon DocumentDB engine versions. You can test the values of this attribute when deciding which Amazon DocumentDB version to use in a new or upgraded cluster. You can also retrieve the version of an existing cluster and check whether that version supports certain Amazon DocumentDB Serverless features before you attempt to use those features.

## Contents
<a name="API_ServerlessV2FeaturesSupport_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** MaxCapacity **   
The maximum number of Amazon DocumentDB capacity units (DCUs) for an instance in an Amazon DocumentDB Serverless cluster. You can specify DCU values in half-step increments, such as 32, 32.5, 33, and so on.  
Type: Double  
Required: No

 ** MinCapacity **   
The minimum number of Amazon DocumentDB capacity units (DCUs) for an instance in an Amazon DocumentDB Serverless cluster. You can specify DCU values in half-step increments, such as 8, 8.5, 9, and so on.  
Type: Double  
Required: No

## See Also
<a name="API_ServerlessV2FeaturesSupport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/ServerlessV2FeaturesSupport) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/ServerlessV2FeaturesSupport) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/ServerlessV2FeaturesSupport) 