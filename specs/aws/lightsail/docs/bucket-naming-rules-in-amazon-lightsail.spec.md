---
id: "@specs/aws/lightsail/docs/bucket-naming-rules-in-amazon-lightsail"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Naming rules"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# Naming rules

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/bucket-naming-rules-in-amazon-lightsail
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Follow bucket naming requirements for Lightsail object storage
<a name="bucket-naming-rules-in-amazon-lightsail"></a>

When you create a bucket in the Amazon Lightsail object storage service, you must give it a name. The name of the bucket is part of the URL that your customers will use when accessing objects that are stored in the bucket. For example, if you name your bucket `amzn-s3-demo-bucket` in the `us-east-1` AWS Region, the URL for your bucket is `amzn-s3-demo-bucket.s3.us-east-1.amazonaws.com`. You cannot change the name of your bucket after you create it. Keep in mind that your customers are able to see the bucket name that you specify. For more information about the Lightsail object storage service, see [Object storage](buckets-in-amazon-lightsail.md). For more information about creating buckets, see [Create a bucket](amazon-lightsail-creating-buckets.md).

Bucket names must be DNS-compliant. Because of this, the following rules apply for naming buckets in Lightsail:
+ Bucket names must be between 3 and 54 characters long.
+ Bucket names can consist only of lowercase letters, numbers, and hyphens (-).
+ Bucket names must begin and end with a letter or number.
+ Hyphens (-) can separate words, but cannot be specified consecutively. For example, `doc-example-bucket` is allowed but `doc--example--bucket` isn't.
+ Bucket names must be unique within the `aws` (Standard Regions) partition, including buckets in Amazon Simple Storage Service (Amazon S3).
+ Bucket names must not start with the prefix `amzn-s3-demo-`. 
+ Bucket names must not start with the prefix `sthree-`.
+ Bucket names must not start with the prefix `sthree-configurator`.
+ Bucket names must not end with the suffix `-s3alias`.

## Example bucket names
<a name="example-bucket-names"></a>

The following example bucket names are valid and follow the recommended naming guidelines:
+ `docexamplebucket1`
+ `log-delivery-march-2020`
+ `my-hosted-content`

The following example bucket names are not allowed:
+ `doc.example.bucket` (contains periods)
+ `doc--example--bucket` (contains two consecutive hyphens)
+ `doc-example-bucket-` (ends with a hyphen)