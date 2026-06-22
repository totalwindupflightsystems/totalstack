---
id: "@specs/aws/opensearchserverless/docs/managedomains-awsresourcetagging-cli"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tagging domains (AWS CLI)"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Tagging domains (AWS CLI)

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/managedomains-awsresourcetagging-cli
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tagging domains (AWS CLI)
<a name="managedomains-awsresourcetagging-cli"></a>

You can create resource tags using the AWS CLI with the **--add-tags** command. 

**Syntax**

`add-tags --arn=<domain_arn> --tag-list Key=<key>,Value=<value>`


****  

| Parameter | Description | 
| --- | --- | 
| --arn | Amazon resource name for the OpenSearch Service domain to which the tag is attached. | 
| --tag-list | Set of space-separated key-value pairs in the following format: Key=<key>,Value=<value> | 

**Example**

The following example creates two tags for the *logs* domain:

```
aws opensearch add-tags --arn arn:aws:es:us-east-1:379931976431:domain/logs --tag-list Key=service,Value=OpenSearch Key=instances,Value=m3.2xlarge
```

You can remove tags from an OpenSearch Service domain using the **--remove-tags** command. 

** Syntax **

`remove-tags --arn=<domain_arn> --tag-keys Key=<key>,Value=<value>`


****  

| Parameter | Description | 
| --- | --- | 
| --arn | Amazon Resource Name (ARN) for the OpenSearch Service domain to which the tag is attached. | 
| --tag-keys | Set of space-separated key-value pairs that you want to remove from the OpenSearch Service domain. | 

**Example**

The following example removes two tags from the *logs* domain that were created in the preceding example:

```
aws opensearch remove-tags --arn arn:aws:es:us-east-1:379931976431:domain/logs --tag-keys service instances
```

You can view the existing tags for an OpenSearch Service domain with the **--list-tags** command:

**Syntax**

`list-tags --arn=<domain_arn>`


****  

| Parameter | Description | 
| --- | --- | 
| --arn | Amazon Resource Name (ARN) for the OpenSearch Service domain to which the tags are attached. | 

**Example**

The following example lists all resource tags for the *logs* domain:

```
aws opensearch list-tags --arn arn:aws:es:us-east-1:379931976431:domain/logs
```