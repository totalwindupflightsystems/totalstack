---
id: "@specs/aws/opensearchserverless/docs/configure-clients-ml-commons-batch"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ML offline batch inference"
status: active
depends_on:
  - "@specs/aws/opensearchserverless/meta"
---

# ML offline batch inference

> **source:** AWS Documentation
> **spec:id:** @specs/aws/opensearchserverless/docs/configure-clients-ml-commons-batch
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using an OpenSearch Ingestion pipeline with machine learning offline batch inference
<a name="configure-clients-ml-commons-batch"></a>

Amazon OpenSearch Ingestion (OSI) pipelines support machine learning (ML) offline batch inference processing to efficiently enrich large volumes of data at low cost. Use offline batch inference whenever you have large datasets that can be processed asynchronously. Offline batch inference works with Amazon Bedrock and SageMaker models. This feature is available in all AWS Regions that support OpenSearch Ingestion with OpenSearch Service 2.17\+ domains.

**Note**  
For real-time inference processing, use [Amazon OpenSearch Service ML connectors for third-party platforms](ml-external-connector.md).

Offline batch inference processing leverages a feature of OpenSearch called ML Commons. *ML Commons* provides ML algorithms through transport and REST API calls. Those calls choose the right nodes and resources for each ML request and monitor ML tasks to ensure uptime. In this way, ML Commons allows you to leverage existing open-source ML algorithms and reduce the effort required to develop new ML features. For more information about ML Commons, see [Machine learning](https://docs.opensearch.org/latest/ml-commons-plugin/) in the OpenSearch.org documentation. 

## How it works
<a name="configure-clients-ml-commons-batch-how"></a>

You can create an offline batch inference pipeline on OpenSearch Ingestion by [adding a machine learning inference processor](https://docs.opensearch.org/latest/ingest-pipelines/processors/ml-inference/) to a pipeline. This processor enables your pipeline to connect to AI services like SageMaker to run batch inference jobs. You can configure your processor to connect to your desired AI service through the AI connectors (with [batch\_predict](https://docs.opensearch.org/latest/ml-commons-plugin/api/model-apis/batch-predict/) support) running on your target domain.

OpenSearch Ingestion uses the `ml_inference` processor with ML Commons to create offline batch inference jobs. ML Commons then uses the [batch\_predict](https://docs.opensearch.org/latest/ml-commons-plugin/api/model-apis/batch-predict/) API, which performs inference on large datasets in an offline asynchronous mode using a model deployed on external model servers in Amazon Bedrock, Amazon SageMaker, Cohere, and OpenAI. The following diagram shows an OpenSearch Ingestion pipeline that orchestrates multiple components to perform this process end to end:

![Three-pipeline architecture of batch AI inference processing.](http://docs.aws.amazon.com/opensearch-service/latest/developerguide/images/ml_processor.png)


The pipeline components work as follows:

**Pipeline 1 (Data preparation and transformation)\*:**
+ Source: Data is scanned from your external source supported by OpenSearch Ingestion.
+ Data processors: The raw data is processed and transformed to the correct format for batch inference on the integrated AI service.
+ S3 (Sink): The processed data is staged in an Amazon S3 bucket ready to serve as input for running batch inference jobs on the integrated AI service. 

**Pipeline 2 (Trigger ML batch\_inference):**
+ Source: Automated S3 event detection of new files created by output of Pipeline 1.
+ Ml\_inference processor: Processor that generates ML inferences through an asynchronous batch job. It connects to AI services through the configured AI connector that's running on your target domain.
+ Task ID: Each batch job is associated with a task ID in ml-commons for tracking and management.
+ OpenSearch ML Commons: ML Commons, which hosts the model for real-time neural search, manages the connectors to remote AI servers, and serves the APIs for batch inference and jobs management.
+ AI services: OpenSearch ML Commons interacts with AI services like Amazon Bedrock and Amazon SageMaker to perform batch inference on the data, producing predictions or insights. The results are saved asynchronously to a separate S3 file.

**Pipeline 3 (Bulk ingestion):**
+ S3 (source): The results of the batch jobs are stored in S3, which is the source of this pipeline.
+ Data transformation processors: Further processing and transformation are applied to the batch inference output before ingestion. This ensures the data is mapped correctly in the OpenSearch index.
+ OpenSearch index (Sink): The processed results are indexed into OpenSearch for storage, search, and further analysis.

**Note**  
\*The process described by Pipeline 1 is optional. If you prefer, you can skip that process and simply upload your prepared data in the S3 sink to create batch jobs.

## About the ml\_inference processor
<a name="configure-clients-ml-commons-batch-inference-processor"></a>

OpenSearch Ingestion uses a specialized integration between the S3 Scan source and ML inference processor for batch processing. The S3 Scan operates in metadata-only mode to efficiently collect S3 file information without reading the actual file contents. The `ml_inference` processor uses the S3 file URLs to coordinate with ML Commons for batch processing. This design optimizes the batch inference workflow by minimizing unnecessary data transfer during the scanning phase. You define the `ml_inference` processor using parameters. Here is an example: 

```
processor:
    - ml_inference:
        # The endpoint URL of your OpenSearch domain
        host: "{{https://AWStest-offlinebatch-123456789abcdefg.us-west-2.es.amazonaws.com}}"
        
        # Type of inference operation:
        # - batch_predict: for batch processing
        # - predict: for real-time inference
        action_type: "batch_predict"
        
        # Remote ML model service provider (Amazon Bedrock or SageMaker)
        service_name: "bedrock"
        
        # Unique identifier for the ML model
        model_id: "{{AWSTestModelID123456789abcde}}"
        
        # S3 path where batch inference results will be stored
        output_path: "s3://{{amzn-s3-demo-bucket}}/"
      
        # Supports ISO_8601 notation strings like PT20.345S or PT15M
        # These settings control how long to keep your inputs in the processor for retry on throttling errors
        retry_time_window: "PT9M"
        
        # AWS configuration settings
        aws:
            # AWS Region where the Lambda function is deployed
            region: "{{us-west-2}}"
            # IAM role ARN for Lambda function execution
            sts_role_arn: "arn:aws::iam::{{account_id}}:role/Admin"
        
        # Dead-letter queue settings for storing errors
        dlq:
          s3:
            region: us-west-2
            bucket: batch-inference-dlq
            key_path_prefix: bedrock-dlq
            sts_role_arn: arn:aws:iam::{{account_id}}:role/{{OSI-invoke-ml}}
            
        # Conditional expression that determines when to trigger the processor
        # In this case, only process when bucket matches "amzn-s3-demo-bucket"
        ml_when: /bucket == "{{amzn-s3-demo-bucket}}"
```

### Ingestion performance improvements using the ml\_inference processor
<a name="configure-clients-ml-commons-batch-ingestion-performance"></a>

The OpenSearch Ingestion `ml_inference` processor significantly enhances data ingestion performance for ML-enabled search. The processor is ideally suited for use cases requiring machine learning model-generated data, including semantic search, multimodal search, document enrichment, and query understanding. In semantic search, the processor can accelerate the creation and ingestion of large-volume, high-dimensional vectors by an order of magnitude.

The processor's offline batch inference capability offers distinct advantages over real-time model invocation. While real-time processing requires a live model server with capacity limitations, batch inference dynamically scales compute resources on demand and processes data in parallel. For example, when the OpenSearch Ingestion pipeline receives one billion source data requests, it creates 100 S3 files for ML batch inference input. The `ml_inference` processor then initiates a SageMaker batch job using 100 `ml.m4.xlarge` Amazon Elastic Compute Cloud (Amazon EC2) instances, completing the vectorization of one billion requests in 14 hours—a task that would be virtually impossible to accomplish in real-time mode.

## Configure the ml\_inference processor to ingest data requests for a semantic search
<a name="configure-clients-ml-commons-configuring"></a>

The following procedures walk you through the process of setting up and configuring the OpenSearch Ingestion `ml_inference` processor to ingest one billion data requests for semantic search using a text embedding model.

**Topics**
+ [Step 1: Create connectors and register models in OpenSearch](#configure-clients-ml-commons-configuring-create-connectors)
+ [Step 2: Create an OpenSearch Ingestion pipeline for ML offline batch inference](#configure-clients-ml-commons-configuring-pipeline)
+ [Step 3: Prepare your data for ingestion](#configure-clients-ml-commons-configuring-data)
+ [Step 4: Monitor the batch inference job](#configure-clients-ml-commons-configuring-monitor)
+ [Step 5: Run search](#configure-clients-ml-commons-configuring-semantic-search)

### Step 1: Create connectors and register models in OpenSearch
<a name="configure-clients-ml-commons-configuring-create-connectors"></a>

For the following procedure, use the ML Commons [batch\_inference\_sagemaker\_connector\_blueprint](https://github.com/opensearch-project/ml-commons/blob/main/docs/remote_inference_blueprints/batch_inference_sagemaker_connector_blueprint.md) to create a connector and model in Amazon SageMaker. If you prefer to use OpenSearch CloudFormation integration templates, see [(Alternative procedure) Step 1: Create connectors and models using an CloudFormation integration template](#configure-clients-ml-commons-configuring-create-connectors-alternative) later in this section. 

**To create connectors and register models in OpenSearch**

1. Create a Deep Java Library (DJL) ML model in SageMaker for batch transform. To view other DJL models, see [semantic\_search\_with\_CFN\_template\_for\_Sagemaker](https://github.com/opensearch-project/ml-commons/blob/main/docs/tutorials/aws/semantic_search_with_CFN_template_for_Sagemaker.md) on GitHub:

   ```
   POST https://api.sagemaker.us-east-1.amazonaws.com/CreateModel
   {
      "ExecutionRoleArn": "arn:aws:iam::123456789012:role/aos_ml_invoke_sagemaker",
      "ModelName": "DJL-Text-Embedding-Model-imageforjsonlines",
      "PrimaryContainer": { 
         "Environment": { 
            "SERVING_LOAD_MODELS" : "djl://ai.djl.huggingface.pytorch/sentence-transformers/all-MiniLM-L6-v2" 
         },
         "Image": "763104351884.dkr.ecr.us-east-1.amazonaws.com/djl-inference:0.29.0-cpu-full"
      }
   }
   ```

1. Create a connector with `batch_predict` as the new `action` type in the `actions` field:

   ```
   POST /_plugins/_ml/connectors/_create
   {
     "name": "DJL Sagemaker Connector: all-MiniLM-L6-v2",
     "version": "1",
     "description": "The connector to sagemaker embedding model all-MiniLM-L6-v2",
     "protocol": "aws_sigv4",
     "credential": {
     "roleArn": "arn:aws:iam::111122223333:role/SageMakerRole"
   },
     "parameters": {
       "region": "us-east-1",
       "service_name": "sagemaker",
       "DataProcessing": {
         "InputFilter": "$.text",
         "JoinSource": "Input",
         "OutputFilter": "$"
       },
       "MaxConcurrentTransforms": 100,
       "ModelName": "DJL-Text-Embedding-Model-imageforjsonlines",
       "TransformInput": {
         "ContentType": "application/json",
         "DataSource": {
           "S3DataSource": {
             "S3DataType": "S3Prefix",
             "S3Uri": "s3://offlinebatch/msmarcotests/"
           }
         },
         "SplitType": "Line"
       },
       "TransformJobName": "djl-batch-transform-1-billion",
       "TransformOutput": {
         "AssembleWith": "Line",
         "Accept": "application/json",
         "S3OutputPath": "s3://offlinebatch/msmarcotestsoutputs/"
       },
       "TransformResources": {
         "InstanceCount": 100,
         "InstanceType": "ml.m4.xlarge"
       },
       "BatchStrategy": "SingleRecord"
     },
     "actions": [
       {
         "action_type": "predict",
         "method": "POST",
         "headers": {
           "content-type": "application/json"
         },
         "url": "https://runtime.sagemaker.us-east-1.amazonaws.com/endpoints/OpenSearch-sagemaker-060124023703/invocations",
         "request_body": "${parameters.input}",
         "pre_process_function": "connector.pre_process.default.embedding",
         "post_process_function": "connector.post_process.default.embedding"
       },
       {
         "action_type": "batch_predict",
         "method": "POST",
         "headers": {
           "content-type": "application/json"
         },
         "url": "https://api.sagemaker.us-east-1.amazonaws.com/CreateTransformJob",
         "request_body": """{ "BatchStrategy": "${parameters.BatchStrategy}", "ModelName": "${parameters.ModelName}", "DataProcessing" : ${parameters.DataProcessing}, "MaxConcurrentTransforms": ${parameters.MaxConcurrentTransforms}, "TransformInput": ${parameters.TransformInput}, "TransformJobName" : "${parameters.TransformJobName}", "TransformOutput" : ${parameters.TransformOutput}, "TransformResources" : ${parameters.TransformResources}}"""
       },
       {
         "action_type": "batch_predict_status",
         "method": "GET",
         "headers": {
           "content-type": "application/json"
         },
         "url": "https://api.sagemaker.us-east-1.amazonaws.com/DescribeTransformJob",
         "request_body": """{ "TransformJobName" : "${parameters.TransformJobName}"}"""
       },
       {
         "action_type": "cancel_batch_predict",
         "method": "POST",
         "headers": {
           "content-type": "application/json"
         },
         "url": "https://api.sagemaker.us-east-1.amazonaws.com/StopTransformJob",
         "request_body": """{ "TransformJobName" : "${parameters.TransformJobName}"}"""
       }
     ]
   }
   ```

1. Use the returned connector ID to register the SageMaker model:

   ```
   POST /_plugins/_ml/models/_register
   {
       "name": "SageMaker model for batch",
       "function_name": "remote",
       "description": "test model",
       "connector_id": "example123456789-abcde"
   }
   ```

1. Invoke the model with the `batch_predict` action type:

   ```
   POST /_plugins/_ml/models/teHr3JABBiEvs-eod7sn/_batch_predict
   {
     "parameters": {
       "TransformJobName": "SM-offline-batch-transform"
     }
   }
   ```

   The response contains a task ID for the batch job:

   ```
   {
    "task_id": "exampleIDabdcefd_1234567",
    "status": "CREATED"
   }
   ```

1. Check the batch job status by calling the Get Task API using the task ID:

   ```
   GET /_plugins/_ml/tasks/exampleIDabdcefd_1234567
   ```

   The response contains the task status:

   ```
   {
     "model_id": "nyWbv5EB_tT1A82ZCu-e",
     "task_type": "BATCH_PREDICTION",
     "function_name": "REMOTE",
     "state": "RUNNING",
     "input_type": "REMOTE",
     "worker_node": [
       "WDZnIMcbTrGtnR4Lq9jPDw"
     ],
     "create_time": 1725496527958,
     "last_update_time": 1725496527958,
     "is_async": false,
     "remote_job": {
       "TransformResources": {
         "InstanceCount": 1,
         "InstanceType": "ml.c5.xlarge"
       },
       "ModelName": "DJL-Text-Embedding-Model-imageforjsonlines",
       "TransformOutput": {
         "Accept": "application/json",
         "AssembleWith": "Line",
         "KmsKeyId": "",
         "S3OutputPath": "s3://offlinebatch/output"
       },
       "CreationTime": 1725496531.935,
       "TransformInput": {
         "CompressionType": "None",
         "ContentType": "application/json",
         "DataSource": {
           "S3DataSource": {
             "S3DataType": "S3Prefix",
             "S3Uri": "s3://offlinebatch/sagemaker_djl_batch_input.json"
           }
         },
         "SplitType": "Line"
       },
       "TransformJobArn": "arn:aws:sagemaker:us-east-1:111122223333:transform-job/SM-offline-batch-transform15",
       "TransformJobStatus": "InProgress",
       "BatchStrategy": "SingleRecord",
       "TransformJobName": "SM-offline-batch-transform15",
       "DataProcessing": {
         "InputFilter": "$.content",
         "JoinSource": "Input",
         "OutputFilter": "$"
       }
     }
   }
   ```

#### (Alternative procedure) Step 1: Create connectors and models using an CloudFormation integration template
<a name="configure-clients-ml-commons-configuring-create-connectors-alternative"></a>

If you prefer, you can use AWS CloudFormation to automatically create all required Amazon SageMaker connectors and models for ML inference. This approach simplifies setup by using a preconfigured template available in the Amazon OpenSearch Service console. For more information, see [Using CloudFormation to set up remote inference for semantic search](cfn-template.md).

**To deploy an CloudFormation stack that creates all the required SageMaker connectors and models**

1. Open the Amazon OpenSearch Service console.

1. In the navigation pane, choose **Integrations**.

1. In the Search field, enter **SageMaker**, and then choose **Integration with text embedding models through Amazon SageMaker**.

1. Choose **Configure domain** and then choose **Configure VPC domain** or **Configure public domain**.

1. Enter information in the template fields. For **Enable Offline Batch Inference**, choose **true** to provision resources for offline batch processing.

1. Choose **Create** to create the CloudFormation stack.

1. After the stack is created, open the **Outputs** tab in the CloudFormation console Locate the **connector\_id** and **model\_id**. You will need these values later when you configure the pipeline.

### Step 2: Create an OpenSearch Ingestion pipeline for ML offline batch inference
<a name="configure-clients-ml-commons-configuring-pipeline"></a>

Use the following sample to create an OpenSearch Ingestion pipeline for ML offline batch inference. For more information about creating a pipeline for OpenSearch Ingestion, see [Creating Amazon OpenSearch Ingestion pipelines](creating-pipeline.md).

**Before you begin**

In the following sample, you specify an IAM role ARN for the `sts_role_arn` parameter. Use the following procedure to verify that this role is mapped to the backend role that has access to ml-commons in OpenSearch.

1. Navigate to the OpenSearch Dashboards plugin for your OpenSearch Service domain. You can find the dashboards endpoint on your domain dashboard on the OpenSearch Service console.

1. From the main menu choose **Security**, **Roles**, and select the **ml\_full\_access** role.

1. Choose **Mapped users**, **Manage mapping**. 

1. Under **Backend roles**, enter the ARN of the Lambda role that needs permission to call your domain. Here is an example: arn:aws:iam::{{111122223333}}:role/{{lambda-role}}

1. Select **Map** and confirm the user or role shows up under **Mapped users**.

**Sample to create an OpenSearch Ingestion pipeline for ML offline batch inference**

```
version: '2'
extension:
  osis_configuration_metadata:
    builder_type: visual
sagemaker-batch-job-pipeline:
  source:
    s3:
      acknowledgments: true
      delete_s3_objects_on_read: false
      scan:
        buckets:
          - bucket:
              name: {{name}}
              data_selection: metadata_only
              filter:
                include_prefix:
                  - sagemaker/sagemaker_djl_batch_input
                exclude_suffix:
                  - .manifest
          - bucket:
              name: {{name}}
              data_selection: data_only
              filter:
                include_prefix:
                  - sagemaker/output/
        scheduling:
          interval: PT6M
      aws:
        region: {{name}}
      default_bucket_owner: {{account_ID}}
      codec:
        ndjson:
          include_empty_objects: false
      compression: none
      workers: '1'
  processor:
    - ml_inference:
        host: "{{https://search-AWStest-offlinebatch-123456789abcdef.us-west-2.es.amazonaws.com}}"
        aws_sigv4: true
        action_type: "batch_predict"
        service_name: "sagemaker"
        model_id: "{{model_ID}}"
        output_path: "s3://{{AWStest-offlinebatch/sagemaker/output}}"
        aws:
          region: "{{us-west-2}}"
          sts_role_arn: "arn:aws:iam::{{account_ID}}:role/Admin"
        ml_when: /bucket == "{{AWStest-offlinebatch}}"
        dlq:
          s3:
            region: {{us-west-2}}
            bucket: {{batch-inference-dlq}}
            key_path_prefix: {{bedrock-dlq}}
            sts_role_arn: arn:aws:iam::{{account_ID}}:role/{{OSI-invoke-ml}}
    - copy_values:
        entries:
          - from_key: /text
            to_key: chapter
          - from_key: /SageMakerOutput
            to_key: chapter_embedding
          - delete_entries:
            with_keys:
          - text
          - SageMakerOutput
  sink:
    - opensearch:
        hosts: ["{{https://search-AWStest-offlinebatch-123456789abcdef.us-west-2.es.amazonaws.com}}"]
        aws:
          serverless: false
          region: us-west-2
        routes:
          - ml-ingest-route
        index_type: custom
        index: test-nlp-index
  routes:
    - ml-ingest-route: /chapter != null and /title != null
```

### Step 3: Prepare your data for ingestion
<a name="configure-clients-ml-commons-configuring-data"></a>

To prepare your data for ML offline batch inference processing, either prepare the data yourself using your own tools or processes or use the [OpenSearch Data Prepper](https://docs.opensearch.org/latest/data-prepper/getting-started/). Verify that the data is organized into the correct format either by using a pipeline to consume the data from your data source or by creating a machine learning dataset.

The following example uses the [MS MARCO](https://microsoft.github.io/msmarco/Datasets.html) dataset, which includes a collection of real user queries for natural language processing tasks. The dataset is structured in JSONL format, where each line represents a request sent to the ML embedding model:

```
{"_id": "1185869", "text": ")what was the immediate impact of the Paris Peace Treaties of 1947?", "metadata": {"world war 2"}}
{"_id": "1185868", "text": "_________ justice is designed to repair the harm to victim, the community and the offender caused by the offender criminal act. question 19 options:", "metadata": {"law"}}
{"_id": "597651", "text": "what is amber", "metadata": {"nothing"}}
{"_id": "403613", "text": "is autoimmune hepatitis a bile acid synthesis disorder", "metadata": {"self immune"}}
...
```

To test using the MS MARCO dataset, imagine a scenario where you construct one billion input requests distributed across 100 files, each containing 10 million requests. The files would be stored in Amazon S3 with the prefix s3://offlinebatch/sagemaker/sagemaker\_djl\_batch\_input/. The OpenSearch Ingestion pipeline would scan these 100 files simultaneously and initiate a SageMaker batch job with 100 workers for parallel processing, enabling efficient vectorization and ingestion of the one billion documents into OpenSearch.

In production environments, you can use an OpenSearch Ingestion pipeline to generate S3 files for batch inference input. The pipeline supports various [data sources](https://docs.opensearch.org/latest/data-prepper/pipelines/configuration/sources/sources/) and operates on a schedule to continuously transform source data into S3 files. These files are then automatically processed by AI servers through scheduled offline batch jobs, ensuring continuous data processing and ingestion.

### Step 4: Monitor the batch inference job
<a name="configure-clients-ml-commons-configuring-monitor"></a>

You can monitor the batch inference jobs using the SageMaker console or the AWS CLI. You can also use the Get Task API to monitor batch jobs:

```
GET /_plugins/_ml/tasks/_search
{
  "query": {
    "bool": {
      "filter": [
        {
          "term": {
            "state": "RUNNING"
          }
        }
      ]
    }
  },
  "_source": ["model_id", "state", "task_type", "create_time", "last_update_time"]
}
```

The API returns a list of active batch job tasks:

```
{
  "took": 2,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 3,
      "relation": "eq"
    },
    "max_score": 0.0,
    "hits": [
      {
        "_index": ".plugins-ml-task",
        "_id": "nyWbv5EB_tT1A82ZCu-e",
        "_score": 0.0,
        "_source": {
          "model_id": "nyWbv5EB_tT1A82ZCu-e",
          "state": "RUNNING",
          "task_type": "BATCH_PREDICTION",
          "create_time": 1725496527958,
          "last_update_time": 1725496527958
        }
      },
      {
        "_index": ".plugins-ml-task",
        "_id": "miKbv5EB_tT1A82ZCu-f",
        "_score": 0.0,
        "_source": {
          "model_id": "miKbv5EB_tT1A82ZCu-f",
          "state": "RUNNING",
          "task_type": "BATCH_PREDICTION",
          "create_time": 1725496528123,
          "last_update_time": 1725496528123
        }
      },
      {
        "_index": ".plugins-ml-task",
        "_id": "kiLbv5EB_tT1A82ZCu-g",
        "_score": 0.0,
        "_source": {
          "model_id": "kiLbv5EB_tT1A82ZCu-g",
          "state": "RUNNING",
          "task_type": "BATCH_PREDICTION",
          "create_time": 1725496529456,
          "last_update_time": 1725496529456
        }
      }
    ]
  }
}
```

### Step 5: Run search
<a name="configure-clients-ml-commons-configuring-semantic-search"></a>

After monitoring the batch inference job and confirming it completed, you can run various types of AI searches, including semantic, hybrid, conversational (with RAG), neural sparse, and multimodal. For more information about AI searches supported by OpenSearch Service, see [AI search](https://docs.opensearch.org/latest/vector-search/ai-search/index/). 

To search raw vectors, use the `knn` query type, provide the `vector` array as input, and specify the `k` number of returned results:

```
GET /my-raw-vector-index/_search
{
  "query": {
    "knn": {
      "my_vector": {
        "vector": [0.1, 0.2, 0.3],
        "k": 2
      }
    }
  }
}
```

To run an AI-powered search, use the `neural` query type. Specify the `query_text` input, the `model_id` of the embedding model you configured in the OpenSearch Ingestion pipeline, and the `k` number of returned results. To exclude embeddings from search results, specify the name of the embedding field in the `_source.excludes` parameter:

```
GET /my-ai-search-index/_search
{
  "_source": {
    "excludes": [
      "output_embedding"
    ]
  },
  "query": {
    "neural": {
      "output_embedding": {
        "query_text": "What is AI search?",
        "model_id": "mBGzipQB2gmRjlv_dOoB",
        "k": 2
      }
    }
  }
}
```