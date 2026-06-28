---
id: "@specs/aws/fsx/docs/API_DataRepositoryTaskFilter"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DataRepositoryTaskFilter"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DataRepositoryTaskFilter

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DataRepositoryTaskFilter
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DataRepositoryTaskFilter
<a name="API_DataRepositoryTaskFilter"></a>

(Optional) An array of filter objects you can use to filter the response of data repository tasks you will see in the response. You can filter the tasks returned in the response by one or more file system IDs, task lifecycles, and by task type. A filter object consists of a filter `Name`, and one or more `Values` for the filter.

## Contents
<a name="API_DataRepositoryTaskFilter_Contents"></a>

 ** Name **   <a name="FSx-Type-DataRepositoryTaskFilter-Name"></a>
Name of the task property to use in filtering the tasks returned in the response.  
+ Use `file-system-id` to retrieve data repository tasks for specific file systems.
+ Use `task-lifecycle` to retrieve data repository tasks with one or more specific lifecycle states, as follows: CANCELED, EXECUTING, FAILED, PENDING, and SUCCEEDED.
Type: String  
Valid Values: `file-system-id | task-lifecycle | data-repository-association-id | file-cache-id`   
Required: No

 ** Values **   <a name="FSx-Type-DataRepositoryTaskFilter-Values"></a>
Use Values to include the specific file system IDs and task lifecycle states for the filters you are using.  
Type: Array of strings  
Array Members: Maximum number of 20 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[0-9a-zA-Z\*\.\\/\?\-\_]*$`   
Required: No

## See Also
<a name="API_DataRepositoryTaskFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DataRepositoryTaskFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DataRepositoryTaskFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DataRepositoryTaskFilter) 