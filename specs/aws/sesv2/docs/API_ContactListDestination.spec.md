---
id: "@specs/aws/sesv2/docs/API_ContactListDestination"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ContactListDestination"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ContactListDestination

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ContactListDestination
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ContactListDestination
<a name="API_ContactListDestination"></a>

An object that contains details about the action of a contact list.

## Contents
<a name="API_ContactListDestination_Contents"></a>

 ** ContactListImportAction **   <a name="SES-Type-ContactListDestination-ContactListImportAction"></a>
>The type of action to perform on the addresses. The following are the possible values:  
+ PUT: add the addresses to the contact list. If the record already exists, it will override it with the new value.
+ DELETE: remove the addresses from the contact list.
Type: String  
Valid Values: `DELETE | PUT`   
Required: Yes

 ** ContactListName **   <a name="SES-Type-ContactListDestination-ContactListName"></a>
The name of the contact list.  
Type: String  
Required: Yes

## See Also
<a name="API_ContactListDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ContactListDestination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ContactListDestination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ContactListDestination) 