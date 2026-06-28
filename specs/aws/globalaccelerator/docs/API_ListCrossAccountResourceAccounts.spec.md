---
id: "@specs/aws/globalaccelerator/docs/API_ListCrossAccountResourceAccounts"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListCrossAccountResourceAccounts"
status: active
depends_on:
  - "@specs/aws/globalaccelerator/meta"
---

# ListCrossAccountResourceAccounts

> **source:** AWS Documentation
> **spec:id:** @specs/aws/globalaccelerator/docs/API_ListCrossAccountResourceAccounts
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListCrossAccountResourceAccounts
<a name="API_ListCrossAccountResourceAccounts"></a>

List the accounts that have cross-account resources.

For more information, see [ Working with cross-account attachments and resources in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/cross-account-resources.html) in the * AWS Global Accelerator Developer Guide*.

## Response Syntax
<a name="API_ListCrossAccountResourceAccounts_ResponseSyntax"></a>

```
{
   "ResourceOwnerAwsAccountIds": [ "string" ]
}
```

## Response Elements
<a name="API_ListCrossAccountResourceAccounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceOwnerAwsAccountIds](#API_ListCrossAccountResourceAccounts_ResponseSyntax) **   <a name="globalaccelerator-ListCrossAccountResourceAccounts-response-ResourceOwnerAwsAccountIds"></a>
The account IDs of principals (resource owners) in a cross-account attachment who can work with resources listed in the same attachment.  
Type: Array of strings  
Length Constraints: Fixed length of 12.  
Pattern: `^\d{12}$` 

## Errors
<a name="API_ListCrossAccountResourceAccounts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access permission.  
HTTP Status Code: 400

 ** InternalServiceErrorException **   
There was an internal error for AWS Global Accelerator.  
HTTP Status Code: 400

## See Also
<a name="API_ListCrossAccountResourceAccounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/globalaccelerator-2018-08-08/ListCrossAccountResourceAccounts) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/globalaccelerator-2018-08-08/ListCrossAccountResourceAccounts) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/globalaccelerator-2018-08-08/ListCrossAccountResourceAccounts) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/globalaccelerator-2018-08-08/ListCrossAccountResourceAccounts) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/globalaccelerator-2018-08-08/ListCrossAccountResourceAccounts) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/globalaccelerator-2018-08-08/ListCrossAccountResourceAccounts) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/globalaccelerator-2018-08-08/ListCrossAccountResourceAccounts) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/globalaccelerator-2018-08-08/ListCrossAccountResourceAccounts) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/globalaccelerator-2018-08-08/ListCrossAccountResourceAccounts) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/globalaccelerator-2018-08-08/ListCrossAccountResourceAccounts) 