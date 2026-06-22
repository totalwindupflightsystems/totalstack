---
id: "@specs/aws/redshift/docs/API_DataShareAssociation"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DataShareAssociation"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DataShareAssociation

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DataShareAssociation
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DataShareAssociation
<a name="API_DataShareAssociation"></a>

The association of a datashare from a producer account with a data consumer. 

## Contents
<a name="API_DataShareAssociation_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** ConsumerAcceptedWrites **   
Specifies whether write operations were allowed during data share association.  
Type: Boolean  
Required: No

 ** ConsumerIdentifier **   
The name of the consumer accounts that have an association with a producer datashare.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** ConsumerRegion **   
The AWS Region of the consumer accounts that have an association with a producer datashare.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** CreatedDate **   
The creation date of the datashare that is associated.  
Type: Timestamp  
Required: No

 ** ProducerAllowedWrites **   
Specifies whether write operations were allowed during data share authorization.  
Type: Boolean  
Required: No

 ** Status **   
The status of the datashare that is associated.  
Type: String  
Valid Values: `ACTIVE | PENDING_AUTHORIZATION | AUTHORIZED | DEAUTHORIZED | REJECTED | AVAILABLE`   
Required: No

 ** StatusChangeDate **   
The status change data of the datashare that is associated.  
Type: Timestamp  
Required: No

## See Also
<a name="API_DataShareAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DataShareAssociation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DataShareAssociation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DataShareAssociation) 