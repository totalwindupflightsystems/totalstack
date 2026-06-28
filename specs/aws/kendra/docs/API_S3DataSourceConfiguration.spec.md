---
id: "@specs/aws/kendra/docs/API_S3DataSourceConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS S3DataSourceConfiguration"
status: active
depends_on:
  - "@specs/aws/kendra/meta"
---

# S3DataSourceConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/kendra/docs/API_S3DataSourceConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# S3DataSourceConfiguration
<a name="API_S3DataSourceConfiguration"></a>

Provides the configuration information to connect to an Amazon S3 bucket.

**Note**  
Amazon Kendra now supports an upgraded Amazon S3 connector.  
You must now use the [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html) object instead of the `S3DataSourceConfiguration` object to configure your connector.  
Connectors configured using the older console and API architecture will continue to function as configured. However, you won't be able to edit or update them. If you want to edit or update your connector configuration, you must create a new connector.  
We recommended migrating your connector workflow to the upgraded version. Support for connectors configured using the older architecture is scheduled to end by June 2024.

## Contents
<a name="API_S3DataSourceConfiguration_Contents"></a>

 ** BucketName **   <a name="kendra-Type-S3DataSourceConfiguration-BucketName"></a>
The name of the bucket that contains the documents.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 63.  
Pattern: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`   
Required: Yes

 ** AccessControlListConfiguration **   <a name="kendra-Type-S3DataSourceConfiguration-AccessControlListConfiguration"></a>
Provides the path to the S3 bucket that contains the user context filtering files for the data source. For the format of the file, see [Access control for S3 data sources](https://docs.aws.amazon.com/kendra/latest/dg/s3-acl.html).  
Type: [AccessControlListConfiguration](API_AccessControlListConfiguration.md) object  
Required: No

 ** DocumentsMetadataConfiguration **   <a name="kendra-Type-S3DataSourceConfiguration-DocumentsMetadataConfiguration"></a>
Document metadata files that contain information such as the document access control information, source URI, document author, and custom attributes. Each metadata file contains metadata about a single document.  
Type: [DocumentsMetadataConfiguration](API_DocumentsMetadataConfiguration.md) object  
Required: No

 ** ExclusionPatterns **   <a name="kendra-Type-S3DataSourceConfiguration-ExclusionPatterns"></a>
A list of glob patterns (patterns that can expand a wildcard pattern into a list of path names that match the given pattern) for certain file names and file types to exclude from your index. If a document matches both an inclusion and exclusion prefix or pattern, the exclusion prefix takes precendence and the document is not indexed. Examples of glob patterns include:  
+  */myapp/config/\**—All files inside config directory.
+  *\*\*/\*.png*—All .png files in all directories.
+  *\*\*/\*.{png, ico, md}*—All .png, .ico or .md files in all directories.
+  */myapp/src/\*\*/\*.ts*—All .ts files inside src directory (and all its subdirectories).
+  *\*\*/\!(\*.module).ts*—All .ts files but not .module.ts
+  *\*.png , \*.jpg*—All PNG and JPEG image files in a directory (files with the extensions .png and .jpg).
+  *\*internal\**—All files in a directory that contain 'internal' in the file name, such as 'internal', 'internal\_only', 'company\_internal'.
+  *\*\*/\*internal\**—All internal-related files in a directory and its subdirectories.
For more examples, see [Use of Exclude and Include Filters](https://docs.aws.amazon.com/cli/latest/reference/s3/#use-of-exclude-and-include-filters) in the AWS CLI Command Reference.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 250 items.  
Length Constraints: Minimum length of 1. Maximum length of 300.  
Required: No

 ** InclusionPatterns **   <a name="kendra-Type-S3DataSourceConfiguration-InclusionPatterns"></a>
A list of glob patterns (patterns that can expand a wildcard pattern into a list of path names that match the given pattern) for certain file names and file types to include in your index. If a document matches both an inclusion and exclusion prefix or pattern, the exclusion prefix takes precendence and the document is not indexed. Examples of glob patterns include:  
+  */myapp/config/\**—All files inside config directory.
+  *\*\*/\*.png*—All .png files in all directories.
+  *\*\*/\*.{png, ico, md}*—All .png, .ico or .md files in all directories.
+  */myapp/src/\*\*/\*.ts*—All .ts files inside src directory (and all its subdirectories).
+  *\*\*/\!(\*.module).ts*—All .ts files but not .module.ts
+  *\*.png , \*.jpg*—All PNG and JPEG image files in a directory (files with the extensions .png and .jpg).
+  *\*internal\**—All files in a directory that contain 'internal' in the file name, such as 'internal', 'internal\_only', 'company\_internal'.
+  *\*\*/\*internal\**—All internal-related files in a directory and its subdirectories.
For more examples, see [Use of Exclude and Include Filters](https://docs.aws.amazon.com/cli/latest/reference/s3/#use-of-exclude-and-include-filters) in the AWS CLI Command Reference.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 250 items.  
Length Constraints: Minimum length of 1. Maximum length of 300.  
Required: No

 ** InclusionPrefixes **   <a name="kendra-Type-S3DataSourceConfiguration-InclusionPrefixes"></a>
A list of S3 prefixes for the documents that should be included in the index.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 250 items.  
Length Constraints: Minimum length of 1. Maximum length of 300.  
Required: No

## See Also
<a name="API_S3DataSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kendra-2019-02-03/S3DataSourceConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kendra-2019-02-03/S3DataSourceConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kendra-2019-02-03/S3DataSourceConfiguration) 