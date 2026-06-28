---
id: "@specs/aws/datasync/docs/transferring-with-manifest"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Using a manifest"
status: active
depends_on:
  - "@specs/aws/datasync/meta"
---

# Using a manifest

> **source:** AWS Documentation
> **spec:id:** @specs/aws/datasync/docs/transferring-with-manifest
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Transferring specific files or objects by using a manifest
<a name="transferring-with-manifest"></a>

A *manifest* is a list of files or objects that you want AWS DataSync to transfer. For example, instead of having to transfer everything in an S3 bucket with potentially millions of objects, DataSync transfers only the objects that you list in your manifest.

Manifests are similar to [filters](filtering.md) but let you identify exactly which files or objects to transfer instead of data that matches a filter pattern.

**Note**  
The maximum allowable size for a manifest file with Enhanced mode tasks is 20 GB.

## Creating your manifest
<a name="transferring-with-manifest-create"></a>

A manifest is a comma-separated values (CSV)-formatted file that lists the files or objects in your source location that you want DataSync to transfer. If your source is an S3 bucket, you can also include which version of an object to transfer.

**Topics**
+ [Guidelines](#transferring-with-manifest-guidelines)
+ [Example manifests](#manifest-examples)

### Guidelines
<a name="transferring-with-manifest-guidelines"></a>

Use these guidelines to help you create a manifest that works with DataSync.

------
#### [ Do ]
+ Specify the full path of each file or object that you want to transfer.

  You can't specify only a directory or folder with the intention of transferring all of its contents. For these situations, consider using an [include filter](filtering.md) instead of a manifest.
+ Make sure that each file or object path is relative to the mount path, folder, directory, or prefix that you specified when configuring your DataSync source location.

  For example, let's say you [configure an S3 location](create-s3-location.md#create-s3-location-how-to) with a prefix named `photos`. That prefix includes an object `my-picture.png` that you want to transfer. In the manifest, you then only need to specify the object (`my-picture.png`) instead of the prefix and object (`photos/my-picture.png`).
+ To specify Amazon S3 object version IDs, separate the object's path and version ID by using a comma.

  The following example shows a manifest entry with two fields. The first field includes an object named `picture1.png`. The second field is separated by a comma and includes a version ID of `111111`:

  ```
  picture1.png,111111
  ```
+ Use quotes in the following situations:
  + When a path contains special characters (commas, quotes, and line endings):

    `"filename,with,commas.txt"`
  + When a path spans multiple lines:

    ```
    "this
    is
    a
    filename.txt"
    ```
  + When a path includes quotes:

    `filename""with""quotes.txt`

    This represents a path named `filename"with"quotes.txt`.

  These quote rules also apply to version ID fields. In general, if a manifest field has a quote, you must escape it with another quote.
+ Separate each file or object entry with a new line.

  You can separate lines by using Linux (line feed or carriage return) or Windows (carriage return followed by a line feed) style line breaks.
+ Save your manifest (for example, `my-manifest.csv` or `my-manifest.txt`).
+ Upload the manifest to an S3 bucket that [DataSync can access](#transferring-with-manifest-access).

  This bucket doesn't have to be in the same AWS Region or account where you're using DataSync.

------
#### [ Don't ]
+ Specify only a directory or folder with the intention of transferring all of its contents.

  A manifest can only include full paths to the files or objects that you want to transfer. If you configure your source location to use a specific mount path, folder, directory, or prefix, you don't have to include that in your manifest.
+ Specify a file or object path that exceeds 4,096 characters.
+ Specify a file path, object path, or Amazon S3 object version ID that exceeds 1,024 bytes.
+ Specify duplicate file or object paths.
+ Include an object version ID if your source location isn't an S3 bucket.
+ Include more than two fields in a manifest entry.

  An entry can include only a file or object path and (if applicable) an Amazon S3 object version ID.
+ Include characters that don't conform to UTF-8 encoding.
+ Include unintentional spaces in your entry fields outside of quotes.

------

### Example manifests
<a name="manifest-examples"></a>

Use these examples to help you create a manifest that works with DataSync. 

**Manifest with full file or object paths**  
The following example shows a manifest with full file or object paths to transfer.  

```
photos/picture1.png
photos/picture2.png
photos/picture3.png
```

**Manifest with only object keys**  
The following example shows a manifest with objects to transfer from an Amazon S3 source location. Since the [location is configured](create-s3-location.md#create-s3-location-how-to) with the prefix `photos`, only the object keys are specified.  

```
picture1.png
picture2.png
picture3.png
```

**Manifest with object paths and version IDs**  
The first two entries in the following manifest example include specific Amazon S3 object versions to transfer.  

```
photos/picture1.png,111111
photos/picture2.png,121212
photos/picture3.png
```

**Manifest with UTF-8 characters**  
The following example shows a manifest with files that include UTF-8 characters.  

```
documents/résumé1.pdf
documents/résumé2.pdf
documents/résumé3.pdf
```

## Providing DataSync access to your manifest
<a name="transferring-with-manifest-access"></a>

You need an AWS Identity and Access Management (IAM) role that gives DataSync access to your manifest in its S3 bucket. This role must include the following permissions:
+ `s3:GetObject`
+ `s3:GetObjectVersion`

You can generate this role automatically in the DataSync console or create the role yourself.

**Note**  
If your manifest is in a different AWS account, you must create this role manually.

### Creating the IAM role automatically
<a name="creating-manfiest-role-automatically"></a>

When creating or starting a transfer task in the console, DataSync can create an IAM role for you with the `s3:GetObject` and `s3:GetObjectVersion` permissions that you need to access your manifest.

**Required permissions to automatically create the role**  
To automatically create the role, make sure that the role that you're using to access the DataSync console has the following permissions:  
+ `iam:CreateRole`
+ `iam:CreatePolicy`
+ `iam:AttachRolePolicy`

### Creating the IAM role (same account)
<a name="creating-manfiest-role-automatically-same-account"></a>

You can manually create the IAM role that DataSync needs to access your manifest. The following instructions assume that you're in the same AWS account where you use DataSync and your manifest's S3 bucket is located. 

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the left navigation pane, under **Access management**, choose **Roles**, and then choose **Create role**.

1. On the **Select trusted entity** page, for **Trusted entity type**, choose **AWS service**.

1. For **Use case**, choose **DataSync** in the dropdown list and select **DataSync**. Choose **Next**.

1. On the **Add permissions** page, choose **Next**. Give your role a name and choose **Create role**.

1. On the **Roles** page, search for the role that you just created and choose its name.

1. On the role's details page, choose the **Permissions** tab. Choose **Add permissions** then **Create inline policy**.

1. Choose the **JSON** tab and paste the following sample policy into the policy editor:

   ```
   {
       "Version": "2012-10-17",
       "Statement": [{
           "Sid": "DataSyncAccessManifest",
           "Effect": "Allow",
           "Action": [
               "s3:GetObject",
               "s3:GetObjectVersion"
           ],
           "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/{{my-manifest.csv}}"
       }]
   }
   ```

1. In the sample policy that you just pasted, replace the following values with your own:

   1. Replace `{{amzn-s3-demo-bucket}}` with the name of the S3 bucket that's hosting your manifest.

   1. Replace `{{my-manifest.csv}}` with the file name of your manifest.

1. Choose **Next**. Give your policy a name and choose **Create policy**.

1. (Recommended) To prevent the [cross-service confused deputy problem](cross-service-confused-deputy-prevention.md), do the following:

   1. On the role's details page, choose the **Trust relationships** tab. Choose **Edit trust policy**.

   1. Update the trust policy by using the following example, which includes the `aws:SourceArn` and `aws:SourceAccount` global condition context keys:

      ```
      {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                  "Service": "datasync.amazonaws.com"
              },
              "Action": "sts:AssumeRole",
              "Condition": {
                  "StringEquals": {
                  "aws:SourceAccount": "{{555555555555}}"
                  },
                  "ArnLike": {
                  "aws:SourceArn": "arn:aws:datasync:{{us-east-1}}:{{555555555555}}:*"
                  }
              }
            }
        ]
      }
      ```
      + Replace each instance `{{account-id}}` with the AWS account ID where you're using DataSync.
      + Replace `{{region}}` with the AWS Region where you're using DataSync.

   1. Choose **Update policy**.

You've created an IAM role that allows DataSync to access your manifest. Specify this role when [creating](#manifest-creating-task) or [starting](#manifest-starting-task) your task.

### Creating the IAM role (different account)
<a name="creating-manfiest-role-automatically-different-account"></a>

If your manifest is in an S3 bucket that belongs to a different AWS account, you must manually create the IAM role that DataSync uses to access the manifest. Then, in the AWS account where your manifest is located, you need to include the role in the S3 bucket policy.

#### Creating the role
<a name="creating-manfiest-role-automatically-different-account-1"></a>

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the left navigation pane, under **Access management**, choose **Roles**, and then choose **Create role**.

1. On the **Select trusted entity** page, for **Trusted entity type**, choose **AWS service**.

1. For **Use case**, choose **DataSync** in the dropdown list and select **DataSync**. Choose **Next**.

1. On the **Add permissions** page, choose **Next**. Give your role a name and choose **Create role**.

1. On the **Roles** page, search for the role that you just created and choose its name.

1. On the role's details page, choose the **Permissions** tab. Choose **Add permissions** then **Create inline policy**.

1. Choose the **JSON** tab and paste the following sample policy into the policy editor:

   ```
   {
       "Version": "2012-10-17",
       "Statement": [{
           "Sid": "DataSyncAccessManifest",
           "Effect": "Allow",
           "Action": [
               "s3:GetObject",
               "s3:GetObjectVersion"
           ],
           "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/{{my-manifest.csv}}"
       }]
   }
   ```

1. In the sample policy that you just pasted, replace the following values with your own:

   1. Replace `{{amzn-s3-demo-bucket}}` with the name of the S3 bucket that's hosting your manifest.

   1. Replace `{{my-manifest.csv}}` with the file name of your manifest.

1. Choose **Next**. Give your policy a name and choose **Create policy**.

1. (Recommended) To prevent the [cross-service confused deputy problem](cross-service-confused-deputy-prevention.md), do the following:

   1. On the role's details page, choose the **Trust relationships** tab. Choose **Edit trust policy**.

   1. Update the trust policy by using the following example, which includes the `aws:SourceArn` and `aws:SourceAccount` global condition context keys:

      ```
      {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                  "Service": "datasync.amazonaws.com"
              },
              "Action": "sts:AssumeRole",
              "Condition": {
                  "StringEquals": {
                  "aws:SourceAccount": "{{000000000000}}"
                  },
                  "ArnLike": {
                  "aws:SourceArn": "arn:aws:datasync:{{us-east-1}}:{{000000000000}}:*"
                  }
              }
           }
        ]
      }
      ```
      + Replace each instance of `{{account-id}}` with the AWS account ID where you're using DataSync.
      + Replace `{{region}}` with the AWS Region where you're using DataSync.

   1. Choose **Update policy**.

You created the IAM role that you can include in your S3 bucket policy.

#### Updating your S3 bucket policy with the role
<a name="creating-manfiest-role-automatically-different-account-2"></a>

Once you've created the IAM role, you must add it to the S3 bucket policy in the other AWS account where your manifest is located.

1. In the AWS Management Console, switch over to the account with your manfiest's S3 bucket.

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. On the bucket's detail page, choose the **Permissions** tab.

1. Under **Bucket policy**, choose **Edit** and do the following to modify your S3 bucket policy:

   1. Update what's in the editor to include the following policy statements:

      ```
      {
        "Version": "2012-10-17",
        "Statement": [
          {
            "Sid": "DataSyncAccessManifestBucket",
            "Effect": "Allow",
            "Action": [
              "s3:GetObject",
              "s3:GetObjectVersion"
            ],
            "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}"
          }
        ]
      }
      ```

   1. Replace `{{account-id}}` with the AWS account ID for the account that you're using DataSync with.

   1. Replace `{{datasync-role}}` with the IAM role that you just created that allows DataSync to access your manifest.

   1. Replace `{{amzn-s3-demo-bucket}}` with the name of the S3 bucket that's hosting your manifest in the other AWS account.

1. Choose **Save changes**.

You've created an IAM role that allows DataSync to access your manifest in the other account. Specify this role when [creating](#manifest-creating-task) or [starting](#manifest-starting-task) your task.

## Specifying your manifest when creating a task
<a name="manifest-creating-task"></a>

You can specify the manifest that you want DataSync to use when creating a task.

### Using the DataSync console
<a name="manifest-creating-task-console"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, choose **Tasks**, and then choose **Create task**.

1. Configure your task's source and destination locations.

   For more information, see [Where can I transfer my data with AWS DataSync?](working-with-locations.md)

1. For **Contents to scan**, choose **Specific files, objects, and folders**, then select **Using a manifest**.

1. For **S3 URI**, choose your manifest that's hosted on an S3 bucket.

   Alternatively, you can enter the URI (for example, `s3://bucket/prefix/my-manifest.csv`).

1. For **Object version**, choose the version of the manifest that you want DataSync to use.

   By default, DataSync uses the latest version of the object.

1. For **Manifest access role**, do one of the following:
   + Choose **Autogenerate** for DataSync to automatically create an IAM role with the permissions required to access your manifest in its S3 bucket.
   + Choose an existing IAM role that can access your manifest.

   For more information, see [Providing DataSync access to your manifest](#transferring-with-manifest-access).

1. Configure any other task settings you need, then choose **Next**.

1. Choose **Create task**.

### Using the AWS CLI
<a name="manifest-creating-task-cli"></a>

1. Copy the following `create-task` command:

   ```
   aws datasync create-task \
     --source-location-arn arn:aws:datasync:{{us-east-1}}:{{123456789012}}:location/loc-12345678abcdefgh \
     --destination-location-arn arn:aws:datasync:{{us-east-1}}:{{123456789012}}:location/loc-abcdefgh12345678 \
     --manifest-config {
         "Source": {
           "S3": {
               "ManifestObjectPath": "{{s3-object-key-of-manifest}}",
               "BucketAccessRoleArn": "{{bucket-iam-role}}",
               "S3BucketArn": "{{amzn-s3-demo-bucket-arn}}",
               "ManifestObjectVersionId": "{{manifest-version-to-use}}" 
           }
         }
     }
   ```

1. For the `--source-location-arn` parameter, specify the Amazon Resource Name (ARN) of the location that you're transferring data from.

1. For the `--destination-location-arn` parameter, specify the ARN of the location that you're transferring data to.

1. For the `--manifest-config` parameter, do the following:
   + `ManifestObjectPath` – Specify the S3 object key of your manifest.
   + `BucketAccessRoleArn` – Specify the IAM role that allows DataSync to access your manifest in its S3 bucket.

     For more information, see [Providing DataSync access to your manifest](#transferring-with-manifest-access).
   + `S3BucketArn` – Specify the ARN of the S3 bucket that's hosting your manifest.
   + `ManifestObjectVersionId` – Specify the version of the manifest that you want DataSync to use.

     By default, DataSync uses the latest version of the object.

1. Run the `create-task` command to create your task.

When you're ready, you can [start your transfer task](run-task.md).

## Specifying your manifest when starting a task
<a name="manifest-starting-task"></a>

You can specify the manifest that you want DataSync to use when executing a task.

### Using the DataSync console
<a name="manifest-starting-task-console"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, choose **Tasks**, and then choose the task that you want to start.

1. In the task overview page, choose **Start**, and then choose **Start with overriding options**.

1. For **Contents to scan**, choose **Specific files, objects, and folders**, then select **Using a manifest**.

1. For **S3 URI**, choose your manifest that's hosted on an S3 bucket.

   Alternatively, you can enter the URI (for example, `s3://bucket/prefix/my-manifest.csv`).

1. For **Object version**, choose the version of the manifest that you want DataSync to use.

   By default, DataSync uses the latest version of the object.

1. For **Manifest access role**, do one of the following:
   + Choose **Autogenerate** for DataSync to automatically create an IAM role to access your manifest in its S3 bucket.
   + Choose an existing IAM role that can access your manifest.

   For more information, see [Providing DataSync access to your manifest](#transferring-with-manifest-access).

1. Choose **Start** to begin your transfer.

### Using the AWS CLI
<a name="manifest-starting-task-cli"></a>

1. Copy the following `start-task-execution` command:

   ```
   aws datasync start-task-execution \
     --task-arn arn:aws:datasync:{{us-east-1}}:{{123456789012}}:task/task-12345678abcdefgh \
     --manifest-config {
         "Source": {
           "S3": {
               "ManifestObjectPath": "{{s3-object-key-of-manifest}}",
               "BucketAccessRoleArn": "{{bucket-iam-role}}",
               "S3BucketArn": "{{amzn-s3-demo-bucket-arn}}",
               "ManifestObjectVersionId": "{{manifest-version-to-use}}" 
           }
         }
     }
   ```

1. For the `--task-arn` parameter, specify the Amazon Resource Name (ARN) of the task that you're starting.

1. For the `--manifest-config` parameter, do the following:
   + `ManifestObjectPath` – Specify the S3 object key of your manifest.
   + `BucketAccessRoleArn` – Specify the IAM role that allows DataSync to access your manifest in its S3 bucket.

     For more information, see [Providing DataSync access to your manifest](#transferring-with-manifest-access).
   + `S3BucketArn` – Specify the ARN of the S3 bucket that's hosting your manifest.
   + `ManifestObjectVersionId` – Specify the version of the manifest that you want DataSync to use.

     By default, DataSync uses the latest version of the object.

1. Run the `start-task-execution` command to begin your transfer.

## Limitations
<a name="transferring-with-manifest-limitations"></a>
+ You can't use a manifest together with [filters](filtering.md).
+ You can't specify only a directory or folder with the intention of transferring all of its contents. For these situations, consider using an [include filter](filtering.md) instead of a manifest.
+ You can't use the **Keep deleted files** task option (`PreserveDeletedFiles` in the [API](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html#DataSync-Type-Options-PreserveDeletedFiles)) to [maintain files or objects in the destination that aren't in the source](configure-metadata.md). DataSync only transfers what's listed in your manifest and doesn't delete anything in the destination.

## Troubleshooting
<a name="manifests-troubleshooting"></a>

**Errors related to `HeadObject` or `GetObjectTagging`**  
If you're transferring objects with specific version IDs from an S3 bucket, you might see an error related to `HeadObject` or `GetObjectTagging`. For example, here's an error related to `GetObjectTagging`:

```
[WARN] Failed to read metadata for file {{/picture1.png}} (versionId: {{111111}}): S3 Get Object Tagging Failed
[ERROR] S3 Exception: op=GetObjectTagging {{photos/picture1.png}}, code=403, type=15, exception=AccessDenied, 
msg=Access Denied req-hdrs: content-type=application/xml, x-amz-api-version=2006-03-01 rsp-hdrs: content-type=application/xml, 
date=Wed, 07 Feb 2024 20:16:14 GMT, server=AmazonS3, transfer-encoding=chunked, 
x-amz-id-2=IOWQ4fDEXAMPLEQM+ey7N9WgVhSnQ6JEXAMPLEZb7hSQDASK+Jd1vEXAMPLEa3Km, x-amz-request-id=79104EXAMPLEB723
```

If you see either of these errors, validate that the IAM role that DataSync uses to access your S3 source location has the following permissions:
+ `s3:GetObjectVersion`
+ `s3:GetObjectVersionTagging`

If you need to update your role with these permissions, see [Creating an IAM role for DataSync to access your Amazon S3 location](create-s3-location.md#create-role-manually).

**Error: `ManifestFileDoesNotExist`**  
This error indicates that a file within the manifest was not found at the source. Review the [guidelines](#transferring-with-manifest-guidelines) for creating a manifest.

## Next steps
<a name="manifests-next-steps"></a>

If you haven't already, [start your task](run-task.md). Otherwise, [monitor your task's activity](monitoring-overview.md).