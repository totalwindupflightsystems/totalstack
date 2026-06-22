---
id: "@specs/aws/docdb/docs/API_DescribeEventCategories"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeEventCategories"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# DescribeEventCategories

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_DescribeEventCategories
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeEventCategories
<a name="API_DescribeEventCategories"></a>

Displays a list of categories for all event source types, or, if specified, for a specified source type. 

## Request Parameters
<a name="API_DescribeEventCategories_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Filters.Filter.N**   
This parameter is not currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** SourceType **   
The type of source that is generating the events.  
Valid values: `db-instance`, `db-parameter-group`, `db-security-group`   
Type: String  
Required: No

## Response Elements
<a name="API_DescribeEventCategories_ResponseElements"></a>

The following element is returned by the service.

 **EventCategoriesMapList.EventCategoriesMap.N**   
A list of event category maps.  
Type: Array of [EventCategoriesMap](API_EventCategoriesMap.md) objects

## Errors
<a name="API_DescribeEventCategories_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeEventCategories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/DescribeEventCategories) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/DescribeEventCategories) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/DescribeEventCategories) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/DescribeEventCategories) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/DescribeEventCategories) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/DescribeEventCategories) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/DescribeEventCategories) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/DescribeEventCategories) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/DescribeEventCategories) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/DescribeEventCategories) 