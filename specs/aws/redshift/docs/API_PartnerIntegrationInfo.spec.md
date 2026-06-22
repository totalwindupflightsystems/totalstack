---
id: "@specs/aws/redshift/docs/API_PartnerIntegrationInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PartnerIntegrationInfo"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# PartnerIntegrationInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_PartnerIntegrationInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PartnerIntegrationInfo
<a name="API_PartnerIntegrationInfo"></a>

Describes a partner integration.

## Contents
<a name="API_PartnerIntegrationInfo_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** CreatedAt **   
The date (UTC) that the partner integration was created.  
Type: Timestamp  
Required: No

 ** DatabaseName **   
The name of the database that receives data from a partner.  
Type: String  
Length Constraints: Maximum length of 127.  
Pattern: `^[\p{L}_][\p{L}\p{N}@$#_]+$`   
Required: No

 ** PartnerName **   
The name of the partner.  
Type: String  
Length Constraints: Maximum length of 255.  
Pattern: `^[a-zA-Z0-9\-_]+$`   
Required: No

 ** Status **   
The partner integration status.  
Type: String  
Valid Values: `Active | Inactive | RuntimeFailure | ConnectionFailure`   
Required: No

 ** StatusMessage **   
The status message provided by the partner.  
Type: String  
Length Constraints: Maximum length of 262144.  
Pattern: `^[\x20-\x7E]+$`   
Required: No

 ** UpdatedAt **   
The date (UTC) that the partner integration status was last updated by the partner.  
Type: Timestamp  
Required: No

## See Also
<a name="API_PartnerIntegrationInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/PartnerIntegrationInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/PartnerIntegrationInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/PartnerIntegrationInfo) 