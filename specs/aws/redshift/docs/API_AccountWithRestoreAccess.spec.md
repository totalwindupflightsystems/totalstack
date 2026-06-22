---
id: "@specs/aws/redshift/docs/API_AccountWithRestoreAccess"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AccountWithRestoreAccess"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# AccountWithRestoreAccess

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_AccountWithRestoreAccess
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AccountWithRestoreAccess
<a name="API_AccountWithRestoreAccess"></a>

Describes an AWS account authorized to restore a snapshot.

## Contents
<a name="API_AccountWithRestoreAccess_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AccountAlias **   
The identifier of an AWS support account authorized to restore a snapshot. For Support, the identifier is `amazon-redshift-support`.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** AccountId **   
The identifier of an AWS account authorized to restore a snapshot.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## See Also
<a name="API_AccountWithRestoreAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/AccountWithRestoreAccess) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/AccountWithRestoreAccess) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/AccountWithRestoreAccess) 