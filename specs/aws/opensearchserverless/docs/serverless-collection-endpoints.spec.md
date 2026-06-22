---
id: "@specs/aws/opensearchserverless/docs/serverless-collection-endpoints"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Collection endpoints"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Collection endpoints

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/serverless-collection-endpoints
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Collection endpoints for Amazon OpenSearch Serverless
<a name="serverless-collection-endpoints"></a>

Amazon OpenSearch Serverless NextGen provides resource-based endpoints on the `on.aws` domain. You can use a per-collection endpoint to access a single collection, or a per-account endpoint to access every collection in your AWS account in a Region through one hostname. Both endpoints work over standard AWS PrivateLink – create VPC endpoints from the Amazon VPC console or with the `CreateVpcEndpoint` Amazon EC2 API.

OpenSearch Serverless Classic uses a per-collection endpoint on `aoss.amazonaws.com`.

**Topics**
+ [Endpoint types](#serverless-collection-endpoints-types)
+ [Per-collection endpoints](#serverless-per-collection-endpoint)
+ [Per-account endpoint](#serverless-per-account-endpoint)

## Endpoint types
<a name="serverless-collection-endpoints-types"></a>

OpenSearch Serverless supports the following collection endpoint formats.


**OpenSearch Serverless collection endpoint formats**  

| Endpoint type | Format | Description | 
| --- | --- | --- | 
| Per-collection (NextGen) | {{collection-id}}.aoss.{{region}}.on.aws | Identifies the collection from the hostname. One endpoint per collection. | 
| Per-account (NextGen) | {{account-id}}.aoss.{{region}}.on.aws | Identifies the collection from a request header. One endpoint serves every collection in your AWS account in a Region. | 
| Per-collection (Classic) | {{collection-id}}.{{region}}.aoss.amazonaws.com | Identifies the collection from the hostname. One endpoint per Classic collection. | 

Both NextGen endpoint formats use standard AWS PrivateLink for VPC access. For more information about creating a VPC endpoint, see [Data plane access through AWS PrivateLink](serverless-vpc.md).

In AWS Regions that support FIPS, OpenSearch Serverless also offers FIPS-compliant variants of these endpoints. For details, see [Using FIPS endpoints with OpenSearch Serverless](fips-compliance-opensearch-serverless.md#using-fips-endpoints-opensearch-serverless).

## Per-collection endpoints
<a name="serverless-per-collection-endpoint"></a>

A per-collection endpoint targets a single collection through a hostname that includes the collection ID. The endpoint is shown on the collection details page in the OpenSearch Serverless console, and returned by the [https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_BatchGetCollection.html](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_BatchGetCollection.html) API in the `collectionEndpoint` field.

Format  
+ NextGen: `{{collection-id}}.aoss.{{region}}.on.aws`
+ Classic: `{{collection-id}}.{{region}}.aoss.amazonaws.com`

The following request indexes a document into the `movies` index of collection `1tg2xudton46knx2a95g` in `us-east-1`:

```
PUT https://1tg2xudton46knx2a95g.aoss.us-east-1.on.aws/movies/_doc/1
{
  "title": "Shawshank Redemption",
  "year": 1994
}
```

## Per-account endpoint
<a name="serverless-per-account-endpoint"></a>

A per-account endpoint targets every collection in your AWS account in a Region through a single hostname. Because the hostname is the same for all collections, you identify the target collection on each request through one of these HTTP headers (at least one is required; if you include both, they must refer to the same collection):
+ `x-amz-aoss-collection-name` – the customer-assigned collection name
+ `x-amz-aoss-collection-id` – the service-generated collection ID

The per-account endpoint enables a single client to share one connection pool across many collections by switching the target collection per request through the header. This is useful for multi-tenant applications that model each tenant as a separate collection.

Use `x-amz-aoss-collection-name` so your application can route requests with names it already knows. You skip storing or looking up the service-generated collection ID.

The per-account endpoint isn't shown in the OpenSearch Serverless console. Construct it from your AWS account ID and the Region.

Format  
+ NextGen: `{{account-id}}.aoss.{{region}}.on.aws`

The following request indexes a document into the `movies` index of collection `my-collection` in account `123456789012` in `us-east-1`:

```
PUT https://123456789012.aoss.us-east-1.on.aws/movies/_doc/1
x-amz-aoss-collection-name: my-collection

{
  "title": "Shawshank Redemption",
  "year": 1994
}
```

**Note**  
The `x-amz-aoss-collection-name` and `x-amz-aoss-collection-id` headers must be SigV4-signed. AWS SDKs do this automatically.