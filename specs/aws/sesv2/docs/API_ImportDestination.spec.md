---
id: "@specs/aws/sesv2/docs/API_ImportDestination"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ImportDestination"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ImportDestination

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ImportDestination
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ImportDestination
<a name="API_ImportDestination"></a>

An object that contains details about the resource destination the import job is going to target.

## Contents
<a name="API_ImportDestination_Contents"></a>

 ** ContactListDestination **   <a name="SES-Type-ImportDestination-ContactListDestination"></a>
An object that contains the action of the import job towards a contact list.  
Type: [ContactListDestination](API_ContactListDestination.md) object  
Required: No

 ** SuppressionListDestination **   <a name="SES-Type-ImportDestination-SuppressionListDestination"></a>
An object that contains the action of the import job towards suppression list.  
Type: [SuppressionListDestination](API_SuppressionListDestination.md) object  
Required: No

## See Also
<a name="API_ImportDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ImportDestination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ImportDestination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ImportDestination) 