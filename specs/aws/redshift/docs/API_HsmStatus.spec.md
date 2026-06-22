---
id: "@specs/aws/redshift/docs/API_HsmStatus"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HsmStatus"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# HsmStatus

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_HsmStatus
> **target_lang:** meta — documentation tier. ALL sections preserved.



# HsmStatus
<a name="API_HsmStatus"></a>

Describes the status of changes to HSM settings.

## Contents
<a name="API_HsmStatus_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** HsmClientCertificateIdentifier **   
Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** HsmConfigurationIdentifier **   
Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Status **   
Reports whether the Amazon Redshift cluster has finished applying any HSM settings changes specified in a modify cluster command.  
Values: active, applying  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## See Also
<a name="API_HsmStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/HsmStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/HsmStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/HsmStatus) 