---
id: "@specs/aws/kendra/docs/API_DataSourceConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DataSourceConfiguration"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# DataSourceConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_DataSourceConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DataSourceConfiguration
<a name="API_DataSourceConfiguration"></a>

Provides the configuration information for an Amazon Kendra data source.

## Contents
<a name="API_DataSourceConfiguration_Contents"></a>

 ** AlfrescoConfiguration **   <a name="kendra-Type-DataSourceConfiguration-AlfrescoConfiguration"></a>
 *This member has been deprecated.*   
Provides the configuration information to connect to Alfresco as your data source.  
Support for `AlfrescoConfiguration` ended May 2023. We recommend migrating to or using the Alfresco data source template schema / [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html) API.
Type: [AlfrescoConfiguration](API_AlfrescoConfiguration.md) object  
Required: No

 ** BoxConfiguration **   <a name="kendra-Type-DataSourceConfiguration-BoxConfiguration"></a>
Provides the configuration information to connect to Box as your data source.  
Type: [BoxConfiguration](API_BoxConfiguration.md) object  
Required: No

 ** ConfluenceConfiguration **   <a name="kendra-Type-DataSourceConfiguration-ConfluenceConfiguration"></a>
Provides the configuration information to connect to Confluence as your data source.  
Type: [ConfluenceConfiguration](API_ConfluenceConfiguration.md) object  
Required: No

 ** DatabaseConfiguration **   <a name="kendra-Type-DataSourceConfiguration-DatabaseConfiguration"></a>
Provides the configuration information to connect to a database as your data source.  
Type: [DatabaseConfiguration](API_DatabaseConfiguration.md) object  
Required: No

 ** FsxConfiguration **   <a name="kendra-Type-DataSourceConfiguration-FsxConfiguration"></a>
Provides the configuration information to connect to Amazon FSx as your data source.  
Amazon Kendra now supports an upgraded Amazon FSx Windows connector.  
You must now use the [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html) object instead of the `FsxConfiguration` object to configure your connector.  
Connectors configured using the older console and API architecture will continue to function as configured. However, you won't be able to edit or update them. If you want to edit or update your connector configuration, you must create a new connector.  
We recommended migrating your connector workflow to the upgraded version. Support for connectors configured using the older architecture is scheduled to end by June 2024.
Type: [FsxConfiguration](API_FsxConfiguration.md) object  
Required: No

 ** GitHubConfiguration **   <a name="kendra-Type-DataSourceConfiguration-GitHubConfiguration"></a>
Provides the configuration information to connect to GitHub as your data source.  
Amazon Kendra now supports an upgraded GitHub connector.  
You must now use the [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html) object instead of the `GitHubConfiguration` object to configure your connector.  
Connectors configured using the older console and API architecture will continue to function as configured. However, you won’t be able to edit or update them. If you want to edit or update your connector configuration, you must create a new connector.  
We recommended migrating your connector workflow to the upgraded version. Support for connectors configured using the older architecture is scheduled to end by June 2024.
Type: [GitHubConfiguration](API_GitHubConfiguration.md) object  
Required: No

 ** GoogleDriveConfiguration **   <a name="kendra-Type-DataSourceConfiguration-GoogleDriveConfiguration"></a>
Provides the configuration information to connect to Google Drive as your data source.  
Type: [GoogleDriveConfiguration](API_GoogleDriveConfiguration.md) object  
Required: No

 ** JiraConfiguration **   <a name="kendra-Type-DataSourceConfiguration-JiraConfiguration"></a>
Provides the configuration information to connect to Jira as your data source.  
Type: [JiraConfiguration](API_JiraConfiguration.md) object  
Required: No

 ** OneDriveConfiguration **   <a name="kendra-Type-DataSourceConfiguration-OneDriveConfiguration"></a>
Provides the configuration information to connect to Microsoft OneDrive as your data source.  
Type: [OneDriveConfiguration](API_OneDriveConfiguration.md) object  
Required: No

 ** QuipConfiguration **   <a name="kendra-Type-DataSourceConfiguration-QuipConfiguration"></a>
Provides the configuration information to connect to Quip as your data source.  
Type: [QuipConfiguration](API_QuipConfiguration.md) object  
Required: No

 ** S3Configuration **   <a name="kendra-Type-DataSourceConfiguration-S3Configuration"></a>
Provides the configuration information to connect to an Amazon S3 bucket as your data source.  
Amazon Kendra now supports an upgraded Amazon S3 connector.  
You must now use the [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html) object instead of the `S3DataSourceConfiguration` object to configure your connector.  
Connectors configured using the older console and API architecture will continue to function as configured. However, you won't be able to edit or update them. If you want to edit or update your connector configuration, you must create a new connector.  
We recommended migrating your connector workflow to the upgraded version. Support for connectors configured using the older architecture is scheduled to end by June 2024.
Type: [S3DataSourceConfiguration](API_S3DataSourceConfiguration.md) object  
Required: No

 ** SalesforceConfiguration **   <a name="kendra-Type-DataSourceConfiguration-SalesforceConfiguration"></a>
Provides the configuration information to connect to Salesforce as your data source.  
Type: [SalesforceConfiguration](API_SalesforceConfiguration.md) object  
Required: No

 ** ServiceNowConfiguration **   <a name="kendra-Type-DataSourceConfiguration-ServiceNowConfiguration"></a>
Provides the configuration information to connect to ServiceNow as your data source.  
Type: [ServiceNowConfiguration](API_ServiceNowConfiguration.md) object  
Required: No

 ** SharePointConfiguration **   <a name="kendra-Type-DataSourceConfiguration-SharePointConfiguration"></a>
Provides the configuration information to connect to Microsoft SharePoint as your data source.  
Type: [SharePointConfiguration](API_SharePointConfiguration.md) object  
Required: No

 ** SlackConfiguration **   <a name="kendra-Type-DataSourceConfiguration-SlackConfiguration"></a>
Provides the configuration information to connect to Slack as your data source.  
Amazon Kendra now supports an upgraded Slack connector.  
You must now use the [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html) object instead of the `SlackConfiguration` object to configure your connector.  
Connectors configured using the older console and API architecture will continue to function as configured. However, you won't be able to edit or update them. If you want to edit or update your connector configuration, you must create a new connector.  
We recommended migrating your connector workflow to the upgraded version. Support for connectors configured using the older architecture is scheduled to end by June 2024.
Type: [SlackConfiguration](API_SlackConfiguration.md) object  
Required: No

 ** TemplateConfiguration **   <a name="kendra-Type-DataSourceConfiguration-TemplateConfiguration"></a>
Provides a template for the configuration information to connect to your data source.  
Type: [TemplateConfiguration](API_TemplateConfiguration.md) object  
Required: No

 ** WebCrawlerConfiguration **   <a name="kendra-Type-DataSourceConfiguration-WebCrawlerConfiguration"></a>
Provides the configuration information required for Amazon Kendra Web Crawler.  
Type: [WebCrawlerConfiguration](API_WebCrawlerConfiguration.md) object  
Required: No

 ** WorkDocsConfiguration **   <a name="kendra-Type-DataSourceConfiguration-WorkDocsConfiguration"></a>
Provides the configuration information to connect to WorkDocs as your data source.  
Type: [WorkDocsConfiguration](API_WorkDocsConfiguration.md) object  
Required: No

## See Also
<a name="API_DataSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/DataSourceConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/DataSourceConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/DataSourceConfiguration) 