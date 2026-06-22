---
id: "@specs/aws/timestream-influxdb/docs/Sagemaker"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Amazon SageMaker AI"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Amazon SageMaker AI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/Sagemaker
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Amazon SageMaker AI
<a name="Sagemaker"></a>

 You can use Amazon SageMaker Notebooks to integrate your machine learning models with Amazon Timestream. To help you get started, we have created a sample SageMaker Notebook that processes data from Timestream. The data is inserted into Timestream from a multi-threaded Python application continuously sending data. The source code for the sample SageMaker Notebook and the sample Python application are available in GitHub. 

1. Create a database and table following the instructions described in [Create a database](console_timestream.md#console_timestream.db.using-console) and [Create a table](console_timestream.md#console_timestream.table.using-console). 

1. Clone the GitHub repository for the [ multi-threaded Python sample application](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/tools/python/continuous-ingestor) following the instructions from [ GitHub](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

1. Clone the GitHub repository for the [sample Timestream SageMaker Notebook](https://github.com/awslabs/amazon-timestream-tools/blob/master/integrations/sagemaker) following the instructions from [ GitHub](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository). 

1. Run the application for continuously ingesting data into Timestream following the instructions in the [README](https://github.com/awslabs/amazon-timestream-tools/blob/mainline/tools/python/continuous-ingestor/README.md).

1. Follow the instructions to create an Amazon S3 bucket for Amazon SageMaker as described [here](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-config-permissions.html).

1. Create an Amazon SageMaker instance with latest boto3 installed: In addition to the instructions described [here](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-setup-working-env.html), follow the steps below: 

   1. On the **Create notebook** instance page, click on **Additional Configuration**

   1. Click on **Lifecycle configuration - *optional*** and select **Create a new lifecycle configuration**

   1. On the *Create lifecycle configuration* wizard box, do the following:

      1. Fill in a desired name to the configuration, e.g. `on-start`

      1. In Start Notebook script, copy-paste the script content from [ Github](https://github.com/aws-samples/amazon-sagemaker-notebook-instance-lifecycle-config-samples/blob/master/scripts/install-pip-package-single-environment/on-start.sh) 

      1. Replace `PACKAGE=scipy` with `PACKAGE=boto3` in the pasted script.

1. Click on **Create configuration**

1. Go to the IAM service in the AWS Management Console and find the newly created SageMaker execution role for the notebook instance.

1. Attach the IAM policy for `AmazonTimestreamFullAccess` to the execution role.
**Note**  
The `AmazonTimestreamFullAccess` IAM policy is not restricted to specific resources and is unsuitable for production use. For a production system, consider using policies that restrict access to specific resources.

1. When the status of the notebook instance is **InService**, choose **Open Jupyter** to launch a SageMaker Notebook for the instance

1.  Upload the files `timestreamquery.py` and `Timestream_SageMaker_Demo.ipynb` into the Notebook by selecting the **Upload** button

1. Choose `Timestream_SageMaker_Demo.ipynb`
**Note**  
If you see a pop up with **Kernel not found**, choose **conda\_python3** and click **Set Kernel**.

1. Modify `DB_NAME`, `TABLE_NAME`, `bucket`, and `ENDPOINT` to match the database name, table name, S3 bucket name, and region for the training models.

1. Choose the **play** icon to run the individual cells

1. When you get to the cell `Leverage Timestream to find hosts with average CPU utilization across the fleet`, ensure that the output returns at least 2 host names.
**Note**  
If there are less than 2 host names in the output, you may need to rerun the sample Python application ingesting data into Timestream with a larger number of threads and host-scale. 

1. When you get to the cell `Train a Random Cut Forest (RCF) model using the CPU utilization history`, change the `train_instance_type` based on the resource requirements for your training job

1. When you get to the cell `Deploy the model for inference`, change the `instance_type` based on the resource requirements for your inference job
**Note**  
It may take a few minutes to train the model. When the training is complete, you will see the message **Completed - Training job completed** in the output of the cell.

1. Run the cell `Stop and delete the endpoint` to clean up resources. You can also stop and delete the instance from the SageMaker console