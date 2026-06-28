---
id: "@specs/aws/kendra/docs/API_QueryResultItem"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS QueryResultItem"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# QueryResultItem

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_QueryResultItem
> **target_lang:** meta — documentation tier. ALL sections preserved.



# QueryResultItem
<a name="API_QueryResultItem"></a>

A single query result.

A query result contains information about a document returned by the query. This includes the original location of the document, a list of attributes assigned to the document, and relevant text from the document that satisfies the query.

## Contents
<a name="API_QueryResultItem_Contents"></a>

 ** AdditionalAttributes **   <a name="kendra-Type-QueryResultItem-AdditionalAttributes"></a>
One or more additional fields/attributes associated with the query result.  
Type: Array of [AdditionalResultAttribute](API_AdditionalResultAttribute.md) objects  
Required: No

 ** CollapsedResultDetail **   <a name="kendra-Type-QueryResultItem-CollapsedResultDetail"></a>
Provides details about a collapsed group of search results.  
Type: [CollapsedResultDetail](API_CollapsedResultDetail.md) object  
Required: No

 ** DocumentAttributes **   <a name="kendra-Type-QueryResultItem-DocumentAttributes"></a>
An array of document fields/attributes assigned to a document in the search results. For example, the document author (`_author`) or the source URI (`_source_uri`) of the document.  
Type: Array of [DocumentAttribute](API_DocumentAttribute.md) objects  
Required: No

 ** DocumentExcerpt **   <a name="kendra-Type-QueryResultItem-DocumentExcerpt"></a>
An extract of the text in the document. Contains information about highlighting the relevant terms in the excerpt.  
Type: [TextWithHighlights](API_TextWithHighlights.md) object  
Required: No

 ** DocumentId **   <a name="kendra-Type-QueryResultItem-DocumentId"></a>
The identifier for the document.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** DocumentTitle **   <a name="kendra-Type-QueryResultItem-DocumentTitle"></a>
The title of the document. Contains the text of the title and information for highlighting the relevant terms in the title.  
Type: [TextWithHighlights](API_TextWithHighlights.md) object  
Required: No

 ** DocumentURI **   <a name="kendra-Type-QueryResultItem-DocumentURI"></a>
The URI of the original location of the document.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^(https?|ftp|file):\/\/([^\s]*)`   
Required: No

 ** FeedbackToken **   <a name="kendra-Type-QueryResultItem-FeedbackToken"></a>
A token that identifies a particular result from a particular query. Use this token to provide click-through feedback for the result. For more information, see [Submitting feedback](https://docs.aws.amazon.com/kendra/latest/dg/submitting-feedback.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^\P{C}*.\P{C}*$`   
Required: No

 ** Format **   <a name="kendra-Type-QueryResultItem-Format"></a>
If the `Type` of document within the response is `ANSWER`, then it is either a `TABLE` answer or `TEXT` answer. If it's a table answer, a table excerpt is returned in `TableExcerpt`. If it's a text answer, a text excerpt is returned in `DocumentExcerpt`.  
Type: String  
Valid Values: `TABLE | TEXT`   
Required: No

 ** Id **   <a name="kendra-Type-QueryResultItem-Id"></a>
The unique identifier for the query result item id (`Id`) and the query result item document id (`DocumentId`) combined. The value of this field changes with every request, even when you have the same documents.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 73.  
Required: No

 ** ScoreAttributes **   <a name="kendra-Type-QueryResultItem-ScoreAttributes"></a>
Indicates the confidence level of Amazon Kendra providing a relevant result for the query. Each result is placed into a bin that indicates the confidence, `VERY_HIGH`, `HIGH`, `MEDIUM` and `LOW`. You can use the score to determine if a response meets the confidence needed for your application.  
The field is only set to `LOW` when the `Type` field is set to `DOCUMENT` and Amazon Kendra is not confident that the result is relevant to the query.  
Type: [ScoreAttributes](API_ScoreAttributes.md) object  
Required: No

 ** TableExcerpt **   <a name="kendra-Type-QueryResultItem-TableExcerpt"></a>
An excerpt from a table within a document.  
Type: [TableExcerpt](API_TableExcerpt.md) object  
Required: No

 ** Type **   <a name="kendra-Type-QueryResultItem-Type"></a>
The type of document within the response. For example, a response could include a question-answer that's relevant to the query.  
Type: String  
Valid Values: `DOCUMENT | QUESTION_ANSWER | ANSWER`   
Required: No

## See Also
<a name="API_QueryResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/QueryResultItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/QueryResultItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/QueryResultItem) 