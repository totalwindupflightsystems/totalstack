---
id: "@specs/aws/kendra/docs/API_GitHubDocumentCrawlProperties"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GitHubDocumentCrawlProperties"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# GitHubDocumentCrawlProperties

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_GitHubDocumentCrawlProperties
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GitHubDocumentCrawlProperties
<a name="API_GitHubDocumentCrawlProperties"></a>

Provides the configuration information to include certain types of GitHub content. You can configure to index repository files only, or also include issues and pull requests, comments, and comment attachments.

## Contents
<a name="API_GitHubDocumentCrawlProperties_Contents"></a>

 ** CrawlIssue **   <a name="kendra-Type-GitHubDocumentCrawlProperties-CrawlIssue"></a>
 `TRUE` to index all issues within a repository.  
Type: Boolean  
Required: No

 ** CrawlIssueComment **   <a name="kendra-Type-GitHubDocumentCrawlProperties-CrawlIssueComment"></a>
 `TRUE` to index all comments on issues.  
Type: Boolean  
Required: No

 ** CrawlIssueCommentAttachment **   <a name="kendra-Type-GitHubDocumentCrawlProperties-CrawlIssueCommentAttachment"></a>
 `TRUE` to include all comment attachments for issues.  
Type: Boolean  
Required: No

 ** CrawlPullRequest **   <a name="kendra-Type-GitHubDocumentCrawlProperties-CrawlPullRequest"></a>
 `TRUE` to index all pull requests within a repository.  
Type: Boolean  
Required: No

 ** CrawlPullRequestComment **   <a name="kendra-Type-GitHubDocumentCrawlProperties-CrawlPullRequestComment"></a>
 `TRUE` to index all comments on pull requests.  
Type: Boolean  
Required: No

 ** CrawlPullRequestCommentAttachment **   <a name="kendra-Type-GitHubDocumentCrawlProperties-CrawlPullRequestCommentAttachment"></a>
 `TRUE` to include all comment attachments for pull requests.  
Type: Boolean  
Required: No

 ** CrawlRepositoryDocuments **   <a name="kendra-Type-GitHubDocumentCrawlProperties-CrawlRepositoryDocuments"></a>
 `TRUE` to index all files with a repository.  
Type: Boolean  
Required: No

## See Also
<a name="API_GitHubDocumentCrawlProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/GitHubDocumentCrawlProperties) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/GitHubDocumentCrawlProperties) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/GitHubDocumentCrawlProperties) 