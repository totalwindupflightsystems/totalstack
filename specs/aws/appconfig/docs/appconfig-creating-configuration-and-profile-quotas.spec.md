---
id: "@specs/aws/appconfig/docs/appconfig-creating-configuration-and-profile-quotas"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Understanding configuration store quotas and limitations"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Understanding configuration store quotas and limitations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-creating-configuration-and-profile-quotas
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Understanding configuration store quotas and limitations
<a name="appconfig-creating-configuration-and-profile-quotas"></a>

Configuration stores supported by AWS AppConfig have the following quotas and limitations.


****  

|  | AWS AppConfig hosted configuration store | Amazon S3 | Systems Manager Parameter Store | AWS Secrets Manager | Systems Manager Document store | AWS CodePipeline | 
| --- | --- | --- | --- | --- | --- | --- | 
| **Configuration size limit** | 2 MB default, 4 MB maximum | 2 MB<br />Enforced by AWS AppConfig, not S3 | 4 KB (free tier) / 8 KB (advanced parameters) | 64 KB | 64 KB | 2 MB<br />Enforced by AWS AppConfig, not CodePipeline | 
| **Resource storage limit** | 1 GB | Unlimited | 10,000 parameters (free tier) / 100,000 parameters (advanced parameters) | 500,000 | 500 documents | Limited by the number of configuration profiles per application (100 profiles per application) | 
| **Server-side encryption** | Yes | [SSE-S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html), [SSE-KMS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) | Yes | Yes | No | Yes | 
| **CloudFormation support** | Yes | Not for creating or updating data | Yes | Yes | No | Yes | 
| **Pricing** | Free | See [Amazon S3 pricing](https://aws.amazon.com//s3/pricing/) | See [AWS Systems Manager pricing](https://aws.amazon.com//systems-manager/pricing/) | See [AWS Secrets Manager pricing](https://aws.amazon.com//secrets-manager/pricing/) | Free | See [AWS CodePipeline pricing](https://aws.amazon.com//codepipeline/pricing/) | 