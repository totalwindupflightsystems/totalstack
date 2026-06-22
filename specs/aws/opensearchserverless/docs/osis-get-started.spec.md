---
id: "@specs/aws/opensearchserverless/docs/osis-get-started"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tutorial: Ingest data into a domain"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# Tutorial: Ingest data into a domain

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/osis-get-started
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tutorial: Ingesting data into a domain using Amazon OpenSearch Ingestion
<a name="osis-get-started"></a>

This tutorial shows you how to use Amazon OpenSearch Ingestion to configure a simple pipeline and ingest data into an Amazon OpenSearch Service domain. A *pipeline* is a resource that OpenSearch Ingestion provisions and manages. You can use a pipeline to filter, enrich, transform, normalize, and aggregate data for downstream analytics and visualization in OpenSearch Service.

This tutorial walks you through the basic steps to get a pipeline up and running quickly. For more comprehensive instructions, see [Creating pipelines](creating-pipeline.md#create-pipeline).

You'll complete the following steps in this tutorial:

1. [Create a domain](#osis-get-started-access).

1. [Create a pipeline](#osis-get-started-pipeline).

1. [Ingest some sample data](#osis-get-started-ingest).

Within the tutorial, you'll create the following resources:
+ A domain named `ingestion-domain` that the pipeline writes to
+ A pipeline named `ingestion-pipeline`

## Required permissions
<a name="osis-get-started-permissions"></a>

To complete this tutorial, your user or role must have an attached [identity-based policy](security-iam-serverless.md#security-iam-serverless-id-based-policies) with the following minimum permissions. These permissions allow you to create a pipeline role and attach a policy (`iam:Create*` and `iam:Attach*`), create or modify a domain (`es:*`), and work with pipelines (`osis:*`).

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
            "es:*"
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

## Step 1: Create the pipeline role
<a name="osis-get-started-role"></a>

First, create a role that the pipeline will assume in order to access the OpenSearch Service domain sink. You'll include this role within the pipeline configuration later in this tutorial.

**To create the pipeline role**

1. Open the AWS Identity and Access Management console at [https://console.aws.amazon.com/iamv2/](https://console.aws.amazon.com/iamv2/ ).

1. Choose **Policies**, and then choose **Create policy**.

1. In this tutorial, you'll ingest data into a domain called `ingestion-domain`, which you'll create in the next step. Select **JSON** and paste the following policy into the editor. Replace `{{your-account-id}}` with your account ID, and modify the Region if necessary.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "es:DescribeDomain",
               "Resource": "arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/ingestion-domain"
           },
           {
               "Effect": "Allow",
               "Action": "es:ESHttp*",
               "Resource": "arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/ingestion-domain/*"
           }
       ]
   }
   ```

------

   If you want to write data to an *existing* domain, replace `ingestion-domain` with the name of your domain.
**Note**  
For simplicity in this tutorial, we use a broad access policy. In production environments, however, we recommend that you apply a more restrictive access policy to your pipeline role. For an example policy that provides the minimum required permissions, see [Granting Amazon OpenSearch Ingestion pipelines access to domains](pipeline-domain-access.md).

1. Choose **Next**, choose **Next**, and name your policy **pipeline-policy**.

1. Choose **Create policy**.

1. Next, create a role and attach the policy to it. Choose **Roles**, and then choose **Create role**.

1. Choose **Custom trust policy** and paste the following policy into the editor:

------
#### [ JSON ]

****  

   ```
   {
      "Version":"2012-10-17",		 	 	 
      "Statement":[
         {
            "Effect":"Allow",
            "Principal":{
               "Service":"osis-pipelines.amazonaws.com"
            },
            "Action":"sts:AssumeRole"
         }
      ]
   }
   ```

------

1. Choose **Next**. Then search for and select **pipeline-policy** (which you just created).

1. Choose **Next** and name the role **PipelineRole**.

1. Choose **Create role**.

Remember the Amazon Resource Name (ARN) of the role (for example, `arn:aws:iam::{{your-account-id}}:role/PipelineRole`). You'll need it when you create your pipeline.

## Step 2: Create a domain
<a name="osis-get-started-access"></a>

First, create a domain named `ingestion-domain` to ingest data into.

Navigate to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home) and [create a domain](createupdatedomains.md) that meets the following requirements:
+ Is running OpenSearch 1.0 or later, or Elasticsearch 7.4 or later
+ Uses public access
+ Does not use fine-grained access control

**Note**  
These requirements are meant to ensure simplicity in this tutorial. In production environments, you can configure a domain with VPC access and/or use fine-grained access control. To use fine-grained access control, see [Map the pipeline role](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/pipeline-domain-access.html#pipeline-access-domain).

The domain must have an access policy that grants permission to the `OpenSearchIngestion-PipelineRole` IAM role, which OpenSearch Service will create for you in the next step. The pipeline will assume this role in order to send data to the domain sink.

Make sure that the domain has the following domain-level access policy, which grants the pipeline role access to the domain. Replace the Region and account ID with your own:

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::{{111122223333}}:role/OpenSearchIngestion-PipelineRole"
      },
      "Action": "es:*",
      "Resource": "arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/ingestion-domain/*"
    }
  ]
}
```

------

For more information about creating domain-level access policies, see [Resource-based policies](ac.md#ac-types-resource).

If you already have a domain created, modify its existing access policy to provide the above permissions to `OpenSearchIngestion-PipelineRole`.

## Step 3: Create a pipeline
<a name="osis-get-started-pipeline"></a>

Now that you have a domain, you can create a pipeline.

**To create a pipeline**

1. Within the Amazon OpenSearch Service console, choose **Pipelines** from the left navigation pane.

1. Choose **Create pipeline**.

1. Select the **Blank** pipeline, then choose **Select blueprint**.

1. In this tutorial, we'll create a simple pipeline that uses the [HTTP source](https://opensearch.org/docs/latest/data-prepper/pipelines/configuration/sources/http-source/) plugin. The plugin accepts log data in a JSON array format. We'll specify a single OpenSearch Service domain as the sink, and ingest all data into the `application_logs` index.

   In the **Source** menu, choose **HTTP**. For the **Path**, enter **/logs**.

1. For simplicity in this tutorial, we'll configure public access for the pipeline. For **Source network options**, choose **Public access**. For information about configuring VPC access, see [Configuring VPC access for Amazon OpenSearch Ingestion pipelines](pipeline-security.md).

1. Choose **Next**.

1. For **Processor**, enter **Date** and choose **Add**.

1. Enable **From time received**. Leave all other settings as their defaults.

1. Choose **Next**.

1. Configure sink details. For **OpenSearch resource type**, choose **Managed cluster**. Then choose the OpenSearch Service domain that you created in the previous section.

   For **Index name**, enter **application\_logs**. OpenSearch Ingestion automatically creates this index in the domain if it doesn't already exist.

1. Choose **Next**.

1. Name the pipeline **ingestion-pipeline**. Leave the capacity settings as their defaults.

1. For **Pipeline role**, select **Create and use a new service role**. The pipeline role provides the required permissions for a pipeline to write to the domain sink and read from pull-based sources. By selecting this option, you allow OpenSearch Ingestion to create the role for you, rather than manually creating it in IAM. For more information, see [Setting up roles and users in Amazon OpenSearch Ingestion](pipeline-security-overview.md).

1. For **Service role name suffix**, enter **PipelineRole**. In IAM, the role will have the format `arn:aws:iam::{{your-account-id}}:role/OpenSearchIngestion-PipelineRole`.

1. Choose **Next**. Review your pipeline configuration and choose **Create pipeline**. The pipeline takes 5–10 minutes to become active.

## Step 4: Ingest some sample data
<a name="osis-get-started-ingest"></a>

When the pipeline status is `Active`, you can start ingesting data into it. You must sign all HTTP requests to the pipeline using [Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html). Use an HTTP tool such as [Postman](https://www.getpostman.com/) or [awscurl](https://github.com/okigan/awscurl) to send some data to the pipeline. As with indexing data directly to a domain, ingesting data into a pipeline always requires either an IAM role or an [IAM access key and secret key](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html). 

**Note**  
The principal signing the request must have the `osis:Ingest` IAM permission.

First, get the ingestion URL from the **Pipeline settings** page:

![Pipeline settings page with Ingestion URL field highlighted showing the endpoint URL.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/pipeline-endpoint.png)


Then, ingest some sample data. The following request uses [awscurl](https://github.com/okigan/awscurl) to send a single log file to the pipeline:

```
awscurl --service osis --region {{us-east-1}} \
    -X POST \
    -H "Content-Type: application/json" \
    -d '[{"time":"2014-08-11T11:40:13+00:00","remote_addr":"122.226.223.69","status":"404","request":"GET http://www.k2proxy.com//hello.html HTTP/1.1","http_user_agent":"Mozilla/4.0 (compatible; WOW64; SLCC2;)"}]' \
    https://{{pipeline-endpoint}}.{{us-east-1}}.osis.amazonaws.com/logs
```

You should see a `200 OK` response. If you get an authentication error, it might be because you're ingesting data from a separate account than the pipeline is in. See [Fixing permissions issues](#osis-get-started-troubleshoot).

Now, query the `application_logs` index to ensure that your log entry was successfully ingested:

```
awscurl --service es --region {{us-east-1}} \
     -X GET \
     https://search-{{ingestion-domain}}.{{us-east-1}}.es.amazonaws.com/application_logs/_search | json_pp
```

**Sample response**:

```
{
   "took":984,
   "timed_out":false,
   "_shards":{
      "total":1,
      "successful":5,
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
            "_index":"application_logs",
            "_type":"_doc",
            "_id":"z6VY_IMBRpceX-DU6V4O",
            "_score":1.0,
            "_source":{
               "time":"2014-08-11T11:40:13+00:00",
               "remote_addr":"122.226.223.69",
               "status":"404",
               "request":"GET http://www.k2proxy.com//hello.html HTTP/1.1",
               "http_user_agent":"Mozilla/4.0 (compatible; WOW64; SLCC2;)",
               "@timestamp":"2022-10-21T21:00:25.502Z"
            }
         }
      ]
   }
}
```

## Fixing permissions issues
<a name="osis-get-started-troubleshoot"></a>

If you followed the steps in the tutorial and you still see authentication errors when you try to ingest data, it might be because the role that is writing to a pipeline is in a different AWS account than the pipeline itself. In this case, you need to create and [assume a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html) that specifically enables you to ingest data. For instructions, see [Providing cross-account ingestion access](configure-client.md#configure-client-cross-account).

## Related resources
<a name="osis-get-started-next"></a>

This tutorial presented a simple use case of ingesting a single document over HTTP. In production scenarios, you'll configure your client applications (such as Fluent Bit, Kubernetes, or the OpenTelemetry Collector) to send data to one or more pipelines. Your pipelines will likely be more complex than the simple example in this tutorial.

To get started configuring your clients and ingesting data, see the following resources:
+ [Creating and managing pipelines](creating-pipeline.md#create-pipeline)
+ [Configuring your clients to send data to OpenSearch Ingestion](configure-client.md)
+ [Data Prepper documentation](https://opensearch.org/docs/latest/clients/data-prepper/index/)