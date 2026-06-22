---
id: "@specs/aws/appsync/docs/API_BadRequestDetail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BadRequestDetail"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# BadRequestDetail

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_BadRequestDetail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BadRequestDetail
<a name="API_BadRequestDetail"></a>

Provides further details for the reason behind the bad request. For reason type `CODE_ERROR`, the detail will contain a list of code errors.

## Contents
<a name="API_BadRequestDetail_Contents"></a>

 ** codeErrors **   <a name="appsync-Type-BadRequestDetail-codeErrors"></a>
Contains the list of errors in the request.  
Type: Array of [CodeError](API_CodeError.md) objects  
Required: No

## See Also
<a name="API_BadRequestDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/BadRequestDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/BadRequestDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/BadRequestDetail) 