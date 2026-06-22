---
id: "@specs/aws/opensearchserverless/docs/gpu-acceleration-enabling"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Enable GPU-acceleration"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Enable GPU-acceleration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/gpu-acceleration-enabling
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Enabling GPU-acceleration
<a name="gpu-acceleration-enabling"></a>

You can enable GPU-acceleration when creating or updating an OpenSearch domain or OpenSearch Serverless collection with the AWS Management Console, AWS CLI, or AWS SDK.

Once you enable GPU-acceleration on your domain or collection, this feature is enabled by default on all indexes. If you need to disable this feature at the index level, see [Creating GPU-accelerated vector indexes](gpu-acceleration-creating-indexes.md).

## Console
<a name="gpu-acceleration-console"></a>

The following procedures enable GPU-acceleration for OpenSearch domains and OpenSearch Serverless collections using the OpenSearch Serverless management console.

------
#### [ Create new domain ]

To create an OpenSearch domain with GPU-acceleration enabled, see [Creating OpenSearch Service domains](createupdatedomains.md#createdomains).

------
#### [ Edit existing domain ]

1. Open the [OpenSearch Service](https://console.aws.amazon.com/aos/home ) management console.

1. In the navigation pane, choose **Domains**.

1. Choose your domain name to open the domain details page.

1. Choose **Actions**, then **Edit domain**.

1. In the **Advanced features** section, select **Enable GPU acceleration**. Once this feature is enabled, your vector indexing operations are [accelerated](gpu-acceleration-vector-index.md#gpu-acceleration-write-operations).

1. Choose **Save changes**.

------
#### [ Create new collection ]

To create an OpenSearch Serverless collection with GPU-acceleration enabled, see [Tutorial: Getting started with Amazon OpenSearch Serverless](serverless-getting-started.md). During collection creation, ensure you select the **Vector search** collection type and enable GPU-acceleration in the vector search configuration.

------
#### [ Edit existing collection ]

1. Open the [OpenSearch Service](https://console.aws.amazon.com/aos/home ) management console.

1. In the navigation pane, choose **Collections**.

1. Choose your collection name to open the collection details page.

1. In the **Deployment options** section, **Edit** Vector GPU acceleration.

1. Disable or enable GPU acceleration.

1. Choose **Save changes**.

------

### AWS CLI
<a name="gpu-acceleration-cli"></a>

------
#### [ Create new domain ]

The following AWS CLI example creates an OpenSearch domain with GPU-acceleration enabled in US East (N. Virginia). Replace the {{text}} with that of your own configuration.

```
aws opensearch create-domain \
    --domain-name {{my-domain}} \
    --engine-version {{OpenSearch_3.1}} \
    --cluster-config InstanceType={{r6g.xlarge.search}},\
        InstanceCount={{1}},\
        DedicatedMasterEnabled={{true}},\
        DedicatedMasterCount={{3}},\
        DedicatedMasterType={{m6g.large.search}} \
    --ebs-options "EBSEnabled={{true}},\
        VolumeType={{gp3}},\
        VolumeSize={{2000}}" \
    --encryption-at-rest-options '{"Enabled":{{true}}}' \
    --aiml-options '{"ServerlessVectorAcceleration": {"Enabled": {{true}}}}' \
    --node-to-node-encryption-options '{"Enabled":{{true}}}' \
    --domain-endpoint-options '{"EnforceHTTPS":{{true}},\
        "TLSSecurityPolicy":"{{Policy-Min-TLS-1-0-2019-07}}"}' \
    --access-policies '{"Version": "2012-10-17",		 	 	 
        "Statement": [{
            "Effect": "Allow",
            "Principal": {"AWS": "*"},
            "Action": "es:*",
            "Resource": "arn:aws:es:{{us-east-1}}:{{123456789012}}:domain/{{my-domain}}/*"
        }]}' \
    --advanced-security-options '{
        "Enabled":{{true}},
        "InternalUserDatabaseEnabled":{{true}},
        "MasterUserOptions": {
            "MasterUserName":"{{USER_NAME}}",
            "MasterUserPassword":"{{PASSWORD}}"
        }}' \
    --region {{us-east-1}}
```

------
#### [ Edit existing domain ]

The following AWS CLI example enables GPU-acceleration for an existing OpenSearch domain. Replace the {{text}} with that of your own configuration.

```
aws opensearch update-domain-config \
    --domain-name {{my-domain}} \
    --cluster-config InstanceType={{r7g.16xlarge.search}},InstanceCount={{3}} \
    --aiml-options '{"ServerlessVectorAcceleration": {"Enabled": true}}'
```

------
#### [ Create new collection ]

The following AWS CLI example creates an OpenSearch Serverless collection with GPU-acceleration enabled in US East (N. Virginia). Replace the {{text}} with that of your own configuration.

```
aws opensearchserverless create-collection \
    --name "{{my-collection}}" \
    --type "VECTORSEARCH" \
    --description "{{My vector collection with GPU acceleration}}" \
    --vector-options '{"ServerlessVectorAcceleration": "{{ENABLED}}"}' \
    --region {{us-east-1}}
```

------
#### [ Edit existing collection ]

The following AWS CLI example enables GPU-acceleration for an existing OpenSearch Serverless collection. Replace the {{text}} with that of your own configuration.

```
aws opensearchserverless update-collection \
    --id {{07tjusf2h91cunochc}} \
    --vector-options '{"ServerlessVectorAcceleration": "{{ENABLED}}"}' \
    --region {{us-east-1}}
```

------