---
id: "@specs/aws/docdb/docs/API_ServerlessV2ScalingConfigurationInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ServerlessV2ScalingConfigurationInfo"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# ServerlessV2ScalingConfigurationInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_ServerlessV2ScalingConfigurationInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ServerlessV2ScalingConfigurationInfo
<a name="API_ServerlessV2ScalingConfigurationInfo"></a>

Retrieves the scaling configuration for an Amazon DocumentDB Serverless cluster.

## Contents
<a name="API_ServerlessV2ScalingConfigurationInfo_Contents"></a>

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
<a name="API_ServerlessV2ScalingConfigurationInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/ServerlessV2ScalingConfigurationInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/ServerlessV2ScalingConfigurationInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/ServerlessV2ScalingConfigurationInfo) 