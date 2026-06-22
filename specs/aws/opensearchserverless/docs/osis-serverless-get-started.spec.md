---
id: "@specs/aws/opensearchserverless/docs/osis-serverless-get-started"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tutorial: Ingest data into a collection"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Tutorial: Ingest data into a collection

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/osis-serverless-get-started
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tutorial: Ingesting data into a collection using Amazon OpenSearch Ingestion
<a name="osis-serverless-get-started"></a>

This tutorial shows you how to use Amazon OpenSearch Ingestion to configure a simple pipeline and ingest data into an Amazon OpenSearch Serverless collection. A *pipeline* is a resource that OpenSearch Ingestion provisions and manages. You can use a pipeline to filter, enrich, transform, normalize, and aggregate data for downstream analytics and visualization in OpenSearch Service.

For a tutorial that demonstrates how to ingest data into a provisioned OpenSearch Service *domain*, see [Tutorial: Ingesting data into a domain using Amazon OpenSearch Ingestion](osis-get-started.md).

You'll complete the following steps in this tutorial:.

1. [Create a collection](#osis-serverless-get-started-access).

1. [Create a pipeline](#osis-serverless-get-started-pipeline).

1. [Ingest some sample data](#osis-serverless-get-started-ingest).

Within the tutorial, you'll create the following resources:
+ A collection named `ingestion-collection` that the pipeline will write to
+ A pipeline named `ingestion-pipeline-serverless`

## Required permissions
<a name="osis-serverless-get-started-permissions"></a>

To complete this tutorial, your user or role must have an attached [identity-based policy](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/security-iam-serverless.html#security-iam-serverless-id-based-policies) with the following minimum permissions. These permissions allow you to create a pipeline role and attach a policy (`iam:Create*` and `iam:Attach*`), create or modify a collection (`aoss:*`), and work with pipelines (`osis:*`).

In addition, several IAM permissions are required in order to automatically create the pipeline role and pass it to OpenSearch Ingestion so that it can write data to the collection.

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Effect":"Allow",
         "Resource":"*",
         "Action":[
            "osis:*",
            "iam:Create*",
            "iam:Attach*",
            "aoss:*"
         ]
      },
      {
         "Resource":[
            "arn:aws:iam::{{111122223333}}:role/OpenSearchIngestion-PipelineRole"
         ],
         "Effect":"Allow",
         "Action":[
            "iam:CreateRole",
            "iam:AttachRolePolicy",
            "iam:PassRole"
         ]
      }
   ]
}
```

------

## Step 1: Create a collection
<a name="osis-serverless-get-started-access"></a>

First, create a collection to ingest data into. We'll name the collection `ingestion-collection`.

1. Navigate to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. Choose **Collections** from the left navigation and choose **Create collection**.

1. In the **Serverless generation** field, choose **Switch to Classic**.

1. Name the collection **ingestion-collection**.

1. For **Security**, choose **Standard create**.

1. Under **Network access settings**, change the access type to **Public**.

1. Keep all other settings as their defaults and choose **Next**.

1. Now, configure a data acces policy for the collection. Deselect **Automatically match access policy settings**.

1. For **Definition method**, choose **JSON** and paste the following policy into the editor. This policy does two things:
   + Allows the pipeline role to write to the collection.
   + Allows you to *read* from the collection. Later, after you ingest some sample data into the pipeline, you'll query the collection to ensure that the data was successfully ingested and written to the index.

     ```
     [
       {
         "Rules": [
           {
             "Resource": [
               "index/ingestion-collection/*"
             ],
             "Permission": [
               "aoss:CreateIndex",
               "aoss:UpdateIndex",
               "aoss:DescribeIndex",
               "aoss:ReadDocument",
               "aoss:WriteDocument"
             ],
             "ResourceType": "index"
           }
         ],
         "Principal": [
           "arn:aws:iam::{{your-account-id}}:role/OpenSearchIngestion-PipelineRole",
           "arn:aws:iam::{{your-account-id}}:role/{{Admin}}"
         ],
         "Description": "Rule 1"
       }
     ]
     ```

1. Modify the `Principal` elements to include your AWS account ID. For the second principal, specify a user or role that you can use to query the collection later.

1. Choose **Next**. Name the access policy **pipeline-collection-access** and choose **Next** again.

1. Review your collection configuration and choose **Submit**.

## Step 2: Create a pipeline
<a name="osis-serverless-get-started-pipeline"></a>

Now that you have a collection, you can create a pipeline.

**To create a pipeline**

1. Within the Amazon OpenSearch Service console, choose **Pipelines** from the left navigation pane.

1. Choose **Create pipeline**.

1. Select the **Blank** pipeline, then choose **Select blueprint**.

1. In this tutorial, we'll create a simple pipeline that uses the [HTTP source](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/http-source/) plugin. The plugin accepts log data in a JSON array format. We'll specify a single OpenSearch Serverless collection as the sink, and ingest all data into the `my_logs` index.

   In the **Source** menu, choose **HTTP**. For the **Path**, enter **/logs**.

1. For simplicity in this tutorial, we'll configure public access for the pipeline. For **Source network options**, choose **Public access**. For information about configuring VPC access, see [Configuring VPC access for Amazon OpenSearch Ingestion pipelines](pipeline-security.md).

1. Choose **Next**.

1. For **Processor**, enter **Date** and choose **Add**.

1. Enable **From time received**. Leave all other settings as their defaults.

1. Choose **Next**.

1. Configure sink details. For **OpenSearch resource type**, choose **Collection (Serverless)**. Then choose the OpenSearch Service collection that you created in the previous section.

   Leave the network policy name as the default. For **Index name**, enter **my\_logs**. OpenSearch Ingestion automatically creates this index in the collection if it doesn't already exist.

1. Choose **Next**.

1. Name the pipeline **ingestion-pipeline-serverless**. Leave the capacity settings as their defaults.

1. For **Pipeline role**, select **Create and use a new service role**. The pipeline role provides the required permissions for a pipeline to write to the collection sink and read from pull-based sources. By selecting this option, you allow OpenSearch Ingestion to create the role for you, rather than manually creating it in IAM. For more information, see [Setting up roles and users in Amazon OpenSearch Ingestion](pipeline-security-overview.md).

1. For **Service role name suffix**, enter **PipelineRole**. In IAM, the role will have the format `arn:aws:iam::{{your-account-id}}:role/OpenSearchIngestion-PipelineRole`.

1. Choose **Next**. Review your pipeline configuration and choose **Create pipeline**. The pipeline takes 5–10 minutes to become active.

## Step 3: Ingest some sample data
<a name="osis-serverless-get-started-ingest"></a>

When the pipeline status is `Active`, you can start ingesting data into it. You must sign all HTTP requests to the pipeline using [Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html). Use an HTTP tool such as [Postman](https://www.getpostman.com/) or [awscurl](https://github.com/okigan/awscurl) to send some data to the pipeline. As with indexing data directly to a collection, ingesting data into a pipeline always requires either an IAM role or an [IAM access key and secret key](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html). 

**Note**  
The principal signing the request must have the `osis:Ingest` IAM permission.

First, get the ingestion URL from the **Pipeline settings** page:

![Pipeline settings page with Ingestion URL field highlighted showing the endpoint URL.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/pipeline-endpoint.png)


Then, send some sample data to the ingestion path. The following sample request uses [awscurl](https://github.com/okigan/awscurl) to send a single log file to the pipeline:

```
awscurl --service osis --region {{us-east-1}} \
    -X POST \
    -H "Content-Type: application/json" \
    -d '[{"time":"2014-08-11T11:40:13+00:00","remote_addr":"122.226.223.69","status":"404","request":"GET http://www.k2proxy.com//hello.html HTTP/1.1","http_user_agent":"Mozilla/4.0 (compatible; WOW64; SLCC2;)"}]' \
    https://{{pipeline-endpoint}}.{{us-east-1}}.osis.amazonaws.com/logs
```

You should see a `200 OK` response.

Now, query the `my_logs` index to ensure that the log entry was successfully ingested:

```
awscurl --service aoss --region {{us-east-1}} \
     -X GET \
     https://{{collection-id}}.{{us-east-1}}.aoss.amazonaws.com/my_logs/_search | json_pp
```

**Sample response**:

```
{
   "took":348,
   "timed_out":false,
   "_shards":{
      "total":0,
      "successful":0,
      "skipped":0,
      "failed":0
   },
   "hits":{
      "total":{
         "value":1,
         "relation":"eq"
      },
      "max_score":1.0,
      "hits":[
         {
            "_index":"my_logs",
            "_id":"1%3A0%3ARJgDvIcBTy5m12xrKE-y",
            "_score":1.0,
            "_source":{
               "time":"2014-08-11T11:40:13+00:00",
               "remote_addr":"122.226.223.69",
               "status":"404",
               "request":"GET http://www.k2proxy.com//hello.html HTTP/1.1",
               "http_user_agent":"Mozilla/4.0 (compatible; WOW64; SLCC2;)",
               "@timestamp":"2023-04-26T05:22:16.204Z"
            }
         }
      ]
   }
}
```

## Related resources
<a name="osis-serverless-get-started-next"></a>

This tutorial presented a simple use case of ingesting a single document over HTTP. In production scenarios, you'll configure your client applications (such as Fluent Bit, Kubernetes, or the OpenTelemetry Collector) to send data to one or more pipelines. Your pipelines will likely be more complex than the simple example in this tutorial.

To get started configuring your clients and ingesting data, see the following resources:
+ [Creating and managing pipelines](creating-pipeline.md#create-pipeline)
+ [Configuring your clients to send data to OpenSearch Ingestion](configure-client.md)
+ [Data Prepper documentation](https://opensearch.org/docs/latest/clients/data-prepper/index/)