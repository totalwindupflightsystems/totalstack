---
id: "@specs/aws/kendra/docs/API_DocumentInfo"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DocumentInfo"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# DocumentInfo

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_DocumentInfo
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DocumentInfo
<a name="API_DocumentInfo"></a>

Identifies a document for which to retrieve status information

## Contents
<a name="API_DocumentInfo_Contents"></a>

 ** DocumentId **   <a name="kendra-Type-DocumentInfo-DocumentId"></a>
The identifier of the document.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: Yes

 ** Attributes **   <a name="kendra-Type-DocumentInfo-Attributes"></a>
Attributes that identify a specific version of a document to check.  
The only valid attributes are:  
+ version
+ datasourceId
+ jobExecutionId
The attributes follow these rules:  
+  `dataSourceId` and `jobExecutionId` must be used together.
+  `version` is ignored if `dataSourceId` and `jobExecutionId` are not provided.
+ If `dataSourceId` and `jobExecutionId` are provided, but `version` is not, the version defaults to "0".
Type: Array of [DocumentAttribute](API_DocumentAttribute.md) objects  
Required: No

## See Also
<a name="API_DocumentInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/DocumentInfo) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/DocumentInfo) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/DocumentInfo) 