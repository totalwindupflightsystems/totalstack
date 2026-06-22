---
id: "@specs/aws/opensearchserverless/docs/serverless-comparison"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Comparing OpenSearch Service and OpenSearch Serverless"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Comparing OpenSearch Service and OpenSearch Serverless

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-comparison
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Comparing OpenSearch Service and OpenSearch Serverless
<a name="serverless-comparison"></a>

In OpenSearch Serverless, some concepts and features are different than their corresponding feature for a provisioned OpenSearch Service domain. For example, one important difference is that OpenSearch Serverless doesn't have the concept of a cluster or node.

The following table describes how important features and concepts in OpenSearch Serverless differ from the equivalent feature in a provisioned OpenSearch Service domain.


| Feature | OpenSearch Service | OpenSearch Serverless | 
| --- | --- | --- | 
| **Domains versus collections** | Indexes are held in *domains*, which are pre-provisioned OpenSearch clusters.<br />For more information, see [Creating and managing Amazon OpenSearch Service domains](createupdatedomains.md). | Indexes are held in *collections*, which are logical groupings of indexes that represent a specific workload or use case.<br />For more information, see [Managing Amazon OpenSearch Serverless collections](serverless-manage.md). | 
| **Node types and capacity management** | You build a cluster with node types that meet your cost and performance specifications. You must calculate your own storage requirements and choose an instance type for your domain.<br />For more information, see [Sizing Amazon OpenSearch Service domains](sizing-domains.md). | OpenSearch Serverless automatically scales and provisions additional compute units for your account based on your capacity usage.<br />For more information, see [Managing capacity limits for Amazon OpenSearch Serverless](serverless-scaling.md). | 
| **Billing** | You pay for each hour of use of an EC2 instance and for the cumulative size of any EBS storage volumes attached to your instances.<br />For more information, see [Pricing for Amazon OpenSearch Service](what-is.md#pricing). | You're charged in OCU-hours for compute for data ingestion, compute for search and query, and storage retained in S3.<br />For more information, see [Amazon OpenSearch Service pricing](https://aws.amazon.com/opensearch-service/pricing/). | 
| **Encryption** | Encryption at rest is *optional* for domains.<br />For more information, see [Encryption of data at rest for Amazon OpenSearch Service](encryption-at-rest.md). | Encryption at rest is *required* for collections.<br />For more information, see [Encryption in Amazon OpenSearch Serverless](serverless-encryption.md). | 
| **Data access control** | Access to the data within domains is determined by IAM policies and [fine-grained access control](fgac.md). | Access to data within collections is determined by [data access policies](serverless-data-access.md). | 
| Supported OpenSearch operations | OpenSearch Service supports a subset of all of the OpenSearch API operations.<br />For more information, see [Supported operations in Amazon OpenSearch Service](supported-operations.md). | OpenSearch Serverless supports a different subset of OpenSearch API operations.<br />For more information, see [Supported operations and plugins in Amazon OpenSearch Serverless](serverless-genref.md). | 
| Dashboards sign-in | Sign in with a username and password.<br />For more information, see [Accessing OpenSearch Dashboards as the master user](fgac.md#fgac-dashboards). | If you're logged into the AWS console and navigate to your Dashboard URL, you'll automatically log in.<br />For more information, see [Accessing OpenSearch Dashboards](serverless-dashboards.md). | 
| APIs | Interact programmatically with OpenSearch Service using the [OpenSearch Service API operations](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/Welcome.html). | Interact programmatically with OpenSearch Serverless using the [OpenSearch Serverless API operations](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/Welcome.html). | 
| Network access | Network settings for a domain apply to the domain endpoint as well as the OpenSearch Dashboards endpoint. Network access for both is tightly coupled. | Network settings for the domain endpoint and the OpenSearch Dashboards endpoint are decoupled. You can choose to not configure network access for OpenSearch Dashboards.<br />For more information, see [Network access for Amazon OpenSearch Serverless](serverless-network.md). | 
| Signing requests | Use the OpenSearch high and low-level REST clients to sign requests. Specify the service name as `es`. | At this time, OpenSearch Serverless supports a subset of clients that OpenSearch Service supports.<br />When you sign requests, specify the service name as `aoss`. The `x-amz-content-sha256` header is required. For more information, see [Signing HTTP requests with other clients](serverless-clients.md#serverless-signing). | 
| OpenSearch version upgrades | You manually upgrade your domains as new versions of OpenSearch become available. You're responsible for ensuring that your domain meets the upgrade requirements, and that you've addressed any breaking changes. | OpenSearch Serverless automatically upgrades your collections to new OpenSearch versions. Upgrades don't necessarily happen as soon as a new version is available. | 
| Service software updates | You manually apply service software updates to your domain as they become available. | OpenSearch Serverless automatically updates your collections to consume the latest bug fixes, features, and performance improvements. | 
| VPC access | You can [provision your domain within a VPC](vpc.md).<br />You can also create additional [OpenSearch Service-managed VPC endpoints](vpc-interface-endpoints.md) to access the domain. | You create one or more [OpenSearch Serverless-managed VPC endpoints](serverless-vpc.md) for your account. Then, you include these endpoints within [network policies](serverless-network.md). | 
| SAML authentication | You enable SAML authentication on a per-domain basis.<br />For more information, see [SAML authentication for OpenSearch Dashboards](saml.md). | You configure one or more SAML providers at the account level, then you include the associated user and group IDs within data access policies.<br />For more information, see [SAML authentication for Amazon OpenSearch Serverless](serverless-saml.md). | 
| Transport Layer Security (TLS) | OpenSearch Service supports TLS 1.2, but we recommend that you use TLS 1.3. | OpenSearch Serverless supports TLS 1.2, but we recommend that you use TLS 1.3. | 