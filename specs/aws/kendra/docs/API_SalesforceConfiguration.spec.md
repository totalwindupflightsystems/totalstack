---
id: "@specs/aws/kendra/docs/API_SalesforceConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS SalesforceConfiguration"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# SalesforceConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_SalesforceConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# SalesforceConfiguration
<a name="API_SalesforceConfiguration"></a>

Provides the configuration information to connect to Salesforce as your data source.

## Contents
<a name="API_SalesforceConfiguration_Contents"></a>

 ** SecretArn **   <a name="kendra-Type-SalesforceConfiguration-SecretArn"></a>
The Amazon Resource Name (ARN) of an AWS Secrets Managersecret that contains the key/value pairs required to connect to your Salesforce instance. The secret must contain a JSON structure with the following keys:  
+ authenticationUrl - The OAUTH endpoint that Amazon Kendra connects to get an OAUTH token. 
+ consumerKey - The application public key generated when you created your Salesforce application.
+ consumerSecret - The application private key generated when you created your Salesforce application.
+ password - The password associated with the user logging in to the Salesforce instance.
+ securityToken - The token associated with the user logging in to the Salesforce instance.
+ username - The user name of the user logging in to the Salesforce instance.
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1284.  
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`   
Required: Yes

 ** ServerUrl **   <a name="kendra-Type-SalesforceConfiguration-ServerUrl"></a>
The instance URL for the Salesforce site that you want to index.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `^(https?|ftp|file):\/\/([^\s]*)`   
Required: Yes

 ** ChatterFeedConfiguration **   <a name="kendra-Type-SalesforceConfiguration-ChatterFeedConfiguration"></a>
Configuration information for Salesforce chatter feeds.  
Type: [SalesforceChatterFeedConfiguration](API_SalesforceChatterFeedConfiguration.md) object  
Required: No

 ** CrawlAttachments **   <a name="kendra-Type-SalesforceConfiguration-CrawlAttachments"></a>
Indicates whether Amazon Kendra should index attachments to Salesforce objects.  
Type: Boolean  
Required: No

 ** ExcludeAttachmentFilePatterns **   <a name="kendra-Type-SalesforceConfiguration-ExcludeAttachmentFilePatterns"></a>
A list of regular expression patterns to exclude certain documents in your Salesforce. Documents that match the patterns are excluded from the index. Documents that don't match the patterns are included in the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index.  
The pattern is applied to the name of the attached file.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 250 items.  
Length Constraints: Minimum length of 1. Maximum length of 300.  
Required: No

 ** IncludeAttachmentFilePatterns **   <a name="kendra-Type-SalesforceConfiguration-IncludeAttachmentFilePatterns"></a>
A list of regular expression patterns to include certain documents in your Salesforce. Documents that match the patterns are included in the index. Documents that don't match the patterns are excluded from the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isn't included in the index.  
The pattern is applied to the name of the attached file.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 250 items.  
Length Constraints: Minimum length of 1. Maximum length of 300.  
Required: No

 ** KnowledgeArticleConfiguration **   <a name="kendra-Type-SalesforceConfiguration-KnowledgeArticleConfiguration"></a>
Configuration information for the knowledge article types that Amazon Kendra indexes. Amazon Kendra indexes standard knowledge articles and the standard fields of knowledge articles, or the custom fields of custom knowledge articles, but not both.  
Type: [SalesforceKnowledgeArticleConfiguration](API_SalesforceKnowledgeArticleConfiguration.md) object  
Required: No

 ** StandardObjectAttachmentConfiguration **   <a name="kendra-Type-SalesforceConfiguration-StandardObjectAttachmentConfiguration"></a>
Configuration information for processing attachments to Salesforce standard objects.   
Type: [SalesforceStandardObjectAttachmentConfiguration](API_SalesforceStandardObjectAttachmentConfiguration.md) object  
Required: No

 ** StandardObjectConfigurations **   <a name="kendra-Type-SalesforceConfiguration-StandardObjectConfigurations"></a>
Configuration of the Salesforce standard objects that Amazon Kendra indexes.  
Type: Array of [SalesforceStandardObjectConfiguration](API_SalesforceStandardObjectConfiguration.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 17 items.  
Required: No

## See Also
<a name="API_SalesforceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/SalesforceConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/SalesforceConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/SalesforceConfiguration) 