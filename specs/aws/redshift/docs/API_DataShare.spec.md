---
id: "@specs/aws/redshift/docs/API_DataShare"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DataShare"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DataShare

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DataShare
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DataShare
<a name="API_DataShare"></a>

## Contents
<a name="API_DataShare_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AllowPubliclyAccessibleConsumers **   
A value that specifies whether the datashare can be shared to a publicly accessible cluster.  
Type: Boolean  
Required: No

 ** DataShareArn **   
The Amazon Resource Name (ARN) of the datashare that the consumer is to use.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** DataShareAssociations.member.N **   
A value that specifies when the datashare has an association between producer and data consumers.  
Type: Array of [DataShareAssociation](API_DataShareAssociation.md) objects  
Required: No

 ** DataShareType **   
 The type of the datashare created by RegisterNamespace.  
Type: String  
Valid Values: `INTERNAL`   
Required: No

 ** ManagedBy **   
The identifier of a datashare to show its managing entity.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ProducerArn **   
The Amazon Resource Name (ARN) of the producer namespace.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## See Also
<a name="API_DataShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DataShare) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DataShare) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DataShare) 