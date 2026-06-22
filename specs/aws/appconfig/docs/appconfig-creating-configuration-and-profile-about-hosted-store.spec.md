---
id: "@specs/aws/appconfig/docs/appconfig-creating-configuration-and-profile-about-hosted-store"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Understanding the AWS AppConfig hosted configuration store"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Understanding the AWS AppConfig hosted configuration store

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-creating-configuration-and-profile-about-hosted-store
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Understanding the AWS AppConfig hosted configuration store
<a name="appconfig-creating-configuration-and-profile-about-hosted-store"></a>

AWS AppConfig includes an internal or hosted configuration store. Configurations must be 2 MB or smaller. The AWS AppConfig hosted configuration store provides the following benefits over other configuration store options. 
+ You don't need to set up and configure other services such as Amazon Simple Storage Service (Amazon S3) or Parameter Store.
+ You don't need to configure AWS Identity and Access Management (IAM) permissions to use the configuration store.
+ You can store configurations in YAML, JSON, or as text documents.
+ There is no cost to use the store.
+ You can create a configuration and add it to the store when you create a configuration profile.