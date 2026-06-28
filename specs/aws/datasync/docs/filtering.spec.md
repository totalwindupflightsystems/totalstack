---
id: "@specs/aws/datasync/docs/filtering"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Using filters"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Using filters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/filtering
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Transferring specific files, objects, and folders by using filters
<a name="filtering"></a>

AWS DataSync lets you apply filters to include or exclude data from your source location in a transfer. For example, if you don't want to transfer temporary files that end with `.tmp`, you can create an exclude filter so that these files don't make their way to your destination location.

You can use a combination of exclude and include filters in the same transfer task. If you modify a task's filters, those changes are applied the next time you run the task.

## Filtering terms, definitions, and syntax
<a name="filter-overview"></a>

Familiarize yourself with the concepts related to DataSync filtering:

**Filter **  
The whole string that makes up a particular filter (for example, `*.tmp``|``*.temp` or `/folderA|/folderB`).  
Filters are made up of patterns delimited by using a pipe (\|). You don't need a delimiter when you add patterns in the DataSync console because you add each pattern separately.  
Filters are case sensitive. For example, filter `/folderA` won't match `/FolderA`.

**Pattern**  
A pattern within a filter. For example, `*.tmp` is a pattern that's part of the `*.tmp``|``*.temp` filter. If your filter has multiple patterns, you delimit each pattern by using a pipe (\|).

**Folders**  
+ All filters are relative to the source location path. For example, suppose that you specify `/my_source/` as the source path when you create your source location and task and specify the include filter `/transfer_this/`. In this case, DataSync transfers only the directory `/my_source/transfer_this/` and its contents.
+ To specify a folder directly under the source location, include a forward slash (/) in front of the folder name. In the example preceding, the pattern uses `/transfer_this`, not `transfer_this`.
+ DataSync interprets the following patterns the same way and matches both the folder and its content.

  `/dir` 

  `/dir/`
+ When you are transferring data from or to an Amazon S3 bucket, DataSync treats the `/` character in the object key as the equivalent of a folder on a file system.

**Special characters**  
Following are special characters for use with filtering.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/datasync/latest/userguide/filtering.html)

## Example filters
<a name="sample-filters"></a>

The following examples show common filters you can use with DataSync.

**Note**  
There are limits to how many characters you can use in a filter. For more information, see [DataSync quotas](datasync-limits.md#task-hard-limits).

**Exclude some folders from your source location**  
In some cases, you want might exclude folders in your source location to not copy them to your destination location. For example, if you have temporary work-in-progress folders, you can use something like the following filter:

`*/.temp`

To exclude folders with similar content (such as `/reports2021` and `/reports2022)`), you can use an exclude filter like the following:

`/reports*`

To exclude folders at any level in the file hierarchy, you can use an exclude filter like the following. 

`*/folder-to-exclude-1`\|`*/folder-to-exclude-2`

To exclude folders at the top level of the source location, you can use an exclude filter like the following. 

`/top-level-folder-to-exclude-1`\|`/top-level-folder-to-exclude-2`

**Include a subset of the folders on your source location**  
In some cases, your source location might be a large share and you need to transfer a subset of the folders under the root. To include specific folders, start a task execution with an include filter like the following.

`/folder-to-transfer/*`

**Exclude specific file types**  
To exclude certain file types from the transfer, you can create a task execution with an exclude filter such as `*.temp`.

**Transfer individual files you specify**  
To transfer a list of individual files, start a task execution with an include filter like the following: "`/folder/subfolder/file1.txt`\|`/folder/subfolder/file2.txt`\|`/folder/subfolder/file2.txt`"

## Creating include filters
<a name="include-filters"></a>

Include filters define the files, objects, and folders that you want DataSync to transfer. You can configure include filters when you create, edit, or start a task.

DataSync scans and transfers only files and folders that match the include filters. For example, to include a subset of your source folders, you might specify `/important_folder_1`\|`/important_folder_2`. 

**Note**  
Include filters support the wildcard (\*) character only as the rightmost character in a pattern. For example, `/documents*`\|`/code*` is supported, but `*.txt` isn't.

### Using the DataSync console
<a name="include-filters-console"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, choose **Tasks**, and then choose **Create task**.

1. Configure your task's source and destination locations.

   For more information, see [Where can I transfer my data with AWS DataSync?](working-with-locations.md)

1. For **Contents to scan**, choose **Specific files, objects, and folders**, then select **Using filters**.

1. For **Includes**, enter your filter (for example, `/important_folders` to include an important directory), then choose **Add pattern**.

1. Add other include filters as needed. 

### Using the AWS CLI
<a name="include-filters-cli"></a>

When using the AWS CLI, you must use single quotation marks (`'`) around the filter and a \| (pipe) as a delimiter if you have more than one filter.

The following example specifies two include filters `/important_folder1` and `/important_folder2` when running the `create-task` command.

```
aws datasync create-task
   --source-location-arn 'arn:aws:datasync:{{region}}:{{account-id}}:location/{{location-id}}' \
   --destination-location-arn 'arn:aws:datasync:{{region}}:{{account-id}}:location/{{location-id}}' \
   --includes FilterType=SIMPLE_PATTERN,Value='/important_folder1|/important_folder2'
```

## Creating exclude filters
<a name="exclude-filters"></a>

Exclude filters define the files, objects, and folders in your source location that you don't want DataSync to transfer. You can configure these filters when you create, edit, or start a task.

**Topics**
+ [Data excluded by default](#directories-ignored-during-transfers)

### Data excluded by default
<a name="directories-ignored-during-transfers"></a>

DataSync automatically excludes some data from being transferred:
+ `.snapshot` – DataSync ignores any path ending with `.snapshot`, which typically is used for point-in-time snapshots of a storage system's files or directories.
+ `/.aws-datasync` and `/.awssync` – DataSync creates these folders in your location to help facilitate your transfer.
+ `/.zfs` – You might see this folder with Amazon FSx for OpenZFS locations.

### Using the DataSync console
<a name="adding-exclude-filters"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, choose **Tasks**, and then choose **Create task**.

1. Configure your task's source and destination locations.

   For more information, see [Where can I transfer my data with AWS DataSync?](working-with-locations.md)

1. For **Excludes**, enter your filter (for example, `*/temp` to exclude temporary folders), then choose **Add pattern**.

1. Add other exclude filters as needed. 

1. If needed, add [include filters](#include-filters).

### Using the AWS CLI
<a name="adding-exclude-filters-cli"></a>

When using the AWS CLI, you must use single quotation marks (`'`) around the filter and a \| (pipe) as a delimiter if you have more than one filter. 

The following example specifies two exclude filters `*/temp` and `*/tmp` when running the `create-task` command.

```
aws datasync create-task \
   --source-location-arn 'arn:aws:datasync:{{region}}:{{account-id}}:location/{{location-id}}' \
   --destination-location-arn 'arn:aws:datasync:{{region}}:{{account-id}}:location/{{location-id}}' \
   --excludes FilterType=SIMPLE_PATTERN,Value='*/temp|*/tmp'
```