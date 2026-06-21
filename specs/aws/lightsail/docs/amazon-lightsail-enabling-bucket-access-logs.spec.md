---
id: "@specs/aws/lightsail/docs/amazon-lightsail-enabling-bucket-access-logs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Manage access logs"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Manage access logs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/amazon-lightsail-enabling-bucket-access-logs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Enable bucket access logging in Lightsail
<a name="amazon-lightsail-enabling-bucket-access-logs"></a>

Access logging provides detailed records for the requests that are made to a bucket in the Amazon Lightsail object storage service. Access logs are useful for many applications. For example, access log information can be useful in security and access audits. It can also help you learn about your customer base.

By default, Lightsail doesn't collect access logs for your buckets. When you enable logging, Lightsail delivers access logs for a source bucket to a target bucket that you choose. Both the source and target buckets must be in the same AWS Region and owned by the same account.

An access log record contains details about the requests that are made to a bucket. This information can include the request type, the resources that are specified in the request, and the time and date that the request was processed. In this guide, we show you how to enable or disable access logging for your buckets by using the Lightsail API, the AWS Command Line Interface (AWS CLI), or AWS SDKs.

For more information about logging basics, see [Bucket access logs](amazon-lightsail-bucket-access-logs.md).

**Contents**
+ [Costs for access logging](#costs-for-access-logging)
+ [Enable access logging using the AWS CLI](#enabling-access-logging)
+ [Disable access logging using the AWS CLI](#disabling-access-logging)

## Costs for access logging
<a name="costs-for-access-logging"></a>

There is no extra charge for enabling access logging on a bucket. However, log files that the system delivers to a bucket will use up storage space. You can delete the log files at any time. We do not assess data transfer charges for log file delivery when the log bucket's data transfer is within its configured monthly allowance.

Your target bucket should not have access logging enabled. You can have logs delivered to any bucket that you own that is in the same Region as the source bucket, including the source bucket itself. However, for simpler log management, we recommend that you save access logs in a different bucket.

## Enable access logging using the AWS CLI
<a name="enabling-access-logging"></a>

To enable access logging for your buckets, we recommend that you create a dedicated logging bucket in each AWS Region that you have buckets. Then have the access log delivered to that dedicated logging bucket.

Complete the following procedure to enable access logging using the AWS CLI.

**Note**  
You must install the AWS CLI and configure it for Lightsail before continuing with this procedure. For more information, see [Configure the AWS CLI to work with Lightsail](lightsail-how-to-set-up-and-configure-aws-cli.md).

1. Open a Command Prompt or Terminal window on your local computer.

1. Enter the following command to enable access logging.

   ```
   aws lightsail update-bucket --bucket-name {{SourceBucketName}} --access-log-config "{\"enabled\": true, \"destination\": \"{{TargetBucketName}}\", \"prefix\": \"{{ObjectKeyNamePrefix/}}\"}"
   ```

   In the command, replace the following example text with your own:
   + {{SourceBucketName}} - The name of the source bucket for which the access logs will be created.
   + {{TargetBucketName}} – The name of the target bucket where the access logs will be saved.
   + {{ObjectKeyNamePrefix/}} - The optional object key name prefix for the access logs. Note that the prefix must end with a forward slash (`/`).

   **Example**

   ```
   aws lightsail update-bucket --bucket-name {{amzn-s3-demo-bucket1}} --access-log-config "{\"enabled\": true, \"destination\": \"{{amzn-s3-demo-bucket2}}\", \"prefix\": \"{{logs/amzn-s3-demo-bucket1/}}\"}"
   ```

   In the example, {{amzn-s3-demo-bucket1}} is the source bucket for which access logs will be created, {{amzn-s3-demo-bucket2}} is the destination bucket where the access logs will be saved, and {{logs/amzn-s3-demo-bucket1/}} is the object key name prefix for the access logs.

   You should see a result similar to the following example after running the command. The source bucket is updated, and the access logs should begin generating and being stored on the destination bucket.  
![Access logging for a bucket enabled](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-enable-access-logging-for-a-bucket.png)

## Disabling access logging using the AWS CLI
<a name="disabling-access-logging"></a>

Complete the following procedure to disable access logging using the AWS CLI.

**Note**  
You must install the AWS CLI and configure it for Lightsail before continuing with this procedure. For more information, see [Configure the AWS CLI to work with Lightsail](lightsail-how-to-set-up-and-configure-aws-cli.md).

1. Open a Command Prompt or Terminal window on your local computer.

1. Enter the following command to disable access logging.

   ```
   aws lightsail update-bucket --bucket-name {{SourceBucketName}} --access-log-config "{\"enabled\": false}"
   ```

   In the command, replace {{SourceBucketName}} with the name of the source bucket for which to disable access logging.

   **Example**

   ```
   aws lightsail update-bucket --bucket-name {{amzn-s3-demo-bucket}} --access-log-config "{\"enabled\": false}"
   ```

   You should see a result similar to the following example after running the command.  
![Access logging for a bucket disabled](http://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-disable-access-logging-for-a-bucket.png)