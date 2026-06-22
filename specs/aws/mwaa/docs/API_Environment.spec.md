---
id: "@specs/aws/mwaa/docs/API_Environment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Environment"
status: active
depends_on:
  - "@specs/aws/mwaa/meta"
---

# Environment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/mwaa/docs/API_Environment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Environment
<a name="API_Environment"></a>

Describes an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

## Contents
<a name="API_Environment_Contents"></a>

 ** AirflowConfigurationOptions **   <a name="mwaa-Type-Environment-AirflowConfigurationOptions"></a>
A list of key-value pairs containing the Apache Airflow configuration options attached to your environment. For more information, refer to [Apache Airflow configuration options](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variables.html).  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 64.  
Key Pattern: `[a-z]+([a-z0-9._]*[a-z0-9_]+)?`   
Value Length Constraints: Minimum length of 1. Maximum length of 65536.  
Value Pattern: `[ -~]+`   
Required: No

 ** AirflowVersion **   <a name="mwaa-Type-Environment-AirflowVersion"></a>
The Apache Airflow version on your environment.  
Valid values: `2.7.2`, `2.8.1`, `2.9.2`, `2.10.1`, `2.10.3`, `2.11.0`, and `3.0.6`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32.  
Pattern: `[0-9a-z.]+`   
Required: No

 ** Arn **   <a name="mwaa-Type-Environment-Arn"></a>
The Amazon Resource Name (ARN) of the Amazon MWAA environment.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `arn:aws(-[a-z]+)?:airflow:[a-z0-9\-]+:\d{12}:environment/\w+.*`   
Required: No

 ** CeleryExecutorQueue **   <a name="mwaa-Type-Environment-CeleryExecutorQueue"></a>
The queue ARN for the environment's [Celery Executor](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/executor/celery.html). Amazon MWAA uses a Celery Executor to distribute tasks across multiple workers. When you create an environment in a shared VPC, you must provide access to the Celery Executor queue from your VPC.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `arn:aws(-[a-z]+)?:sqs:[a-z0-9\-]+:\d{12}:[a-zA-Z_0-9+=,.@\-_/]+`   
Required: No

 ** CreatedAt **   <a name="mwaa-Type-Environment-CreatedAt"></a>
The day and time the environment was created.  
Type: Timestamp  
Required: No

 ** DagS3Path **   <a name="mwaa-Type-Environment-DagS3Path"></a>
The relative path to the DAGs folder in your Amazon S3 bucket. For example, `s3://mwaa-environment/dags`. For more information, refer to [Adding or updating DAGs](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-folder.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `.*`   
Required: No

 ** DatabaseVpcEndpointService **   <a name="mwaa-Type-Environment-DatabaseVpcEndpointService"></a>
The VPC endpoint for the environment's Amazon RDS database.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `([a-z.-]+)?com\.amazonaws\.vpce\.[a-z0-9\-]+\.[a-zA-Z_0-9+=,.@\-_/]+`   
Required: No

 ** EndpointManagement **   <a name="mwaa-Type-Environment-EndpointManagement"></a>
Defines whether the VPC endpoints configured for the environment are created, and managed, by the customer or by Amazon MWAA. If set to `SERVICE`, Amazon MWAA will create and manage the required VPC endpoints in your VPC. If set to `CUSTOMER`, you must create, and manage, the VPC endpoints in your VPC.  
Type: String  
Valid Values: `CUSTOMER | SERVICE`   
Required: No

 ** EnvironmentClass **   <a name="mwaa-Type-Environment-EnvironmentClass"></a>
The environment class type. Valid values: `mw1.micro`, `mw1.small`, `mw1.medium`, `mw1.large`, `mw1.xlarge`, and `mw1.2xlarge`. For more information, refer to [Amazon MWAA environment class](https://docs.aws.amazon.com/mwaa/latest/userguide/environment-class.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

 ** ExecutionRoleArn **   <a name="mwaa-Type-Environment-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the execution role in IAM that allows MWAA to access AWS resources in your environment. For example, `arn:aws:iam::123456789:role/my-execution-role`. For more information, refer to [Amazon MWAA Execution role](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-create-role.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `arn:aws(-[a-z]+)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`   
Required: No

 ** KmsKey **   <a name="mwaa-Type-Environment-KmsKey"></a>
The AWS KMS encryption key used to encrypt the data in your environment.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `(((arn:aws(-[a-z]+)?:kms:[a-z]{2}-[a-z]+-\d:\d+:)?key\/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}|(arn:aws(-[a-z]+)?:kms:[a-z]{2}-[a-z]+-\d:\d+:)?alias/.+)`   
Required: No

 ** LastUpdate **   <a name="mwaa-Type-Environment-LastUpdate"></a>
The status of the last update on the environment.  
Type: [LastUpdate](API_LastUpdate.md) object  
Required: No

 ** LoggingConfiguration **   <a name="mwaa-Type-Environment-LoggingConfiguration"></a>
The Apache Airflow logs published to CloudWatch Logs.  
Type: [LoggingConfiguration](API_LoggingConfiguration.md) object  
Required: No

 ** MaxWebservers **   <a name="mwaa-Type-Environment-MaxWebservers"></a>
 The maximum number of web servers that you want to run in your environment. Amazon MWAA scales the number of Apache Airflow web servers up to the number you specify for `MaxWebservers` when you interact with your Apache Airflow environment using Apache Airflow REST API, or the Apache Airflow CLI. For example, in scenarios where your workload requires network calls to the Apache Airflow REST API with a high transaction-per-second (TPS) rate, Amazon MWAA will increase the number of web servers up to the number set in `MaxWebserers`. As TPS rates decrease Amazon MWAA disposes of the additional web servers, and scales down to the number set in `MinxWebserers`.   
Valid values: For environments larger than mw1.micro, accepts values from `2` to `5`. Defaults to `2` for all environment sizes except mw1.micro, which defaults to `1`.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** MaxWorkers **   <a name="mwaa-Type-Environment-MaxWorkers"></a>
The maximum number of workers that run in your environment. For example, `20`.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** MinWebservers **   <a name="mwaa-Type-Environment-MinWebservers"></a>
 The minimum number of web servers that you want to run in your environment. Amazon MWAA scales the number of Apache Airflow web servers up to the number you specify for `MaxWebservers` when you interact with your Apache Airflow environment using Apache Airflow REST API, or the Apache Airflow CLI. As the transaction-per-second rate, and the network load, decrease, Amazon MWAA disposes of the additional web servers, and scales down to the number set in `MinxWebserers`.   
Valid values: For environments larger than mw1.micro, accepts values from `2` to `5`. Defaults to `2` for all environment sizes except mw1.micro, which defaults to `1`.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** MinWorkers **   <a name="mwaa-Type-Environment-MinWorkers"></a>
The minimum number of workers that run in your environment. For example, `2`.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** Name **   <a name="mwaa-Type-Environment-Name"></a>
The name of the Amazon MWAA environment. For example, `MyMWAAEnvironment`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 80.  
Pattern: `[a-zA-Z][0-9a-zA-Z-_]*`   
Required: No

 ** NetworkConfiguration **   <a name="mwaa-Type-Environment-NetworkConfiguration"></a>
Describes the VPC networking components used to secure and enable network traffic between the AWS resources for your environment. For more information, refer to [About networking on Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html).  
Type: [NetworkConfiguration](API_NetworkConfiguration.md) object  
Required: No

 ** PluginsS3ObjectVersion **   <a name="mwaa-Type-Environment-PluginsS3ObjectVersion"></a>
The version of the `plugins.zip` file in your Amazon S3 bucket. You must specify the [version ID](https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html) that Amazon S3 assigns to the file.  
 Version IDs are Unicode, UTF-8 encoded, URL-ready, opaque strings that are no more than 1,024 bytes long. The following is an example:   
 `3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo`   
For more information, refer to [Installing custom plugins](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

 ** PluginsS3Path **   <a name="mwaa-Type-Environment-PluginsS3Path"></a>
The relative path to the file in your Amazon S3 bucket. For example, `s3://mwaa-environment/plugins.zip`. For more information, refer to [Installing custom plugins](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `.*`   
Required: No

 ** RequirementsS3ObjectVersion **   <a name="mwaa-Type-Environment-RequirementsS3ObjectVersion"></a>
The version of the `requirements.txt ` file on your Amazon S3 bucket. You must specify the [version ID](https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html) that Amazon S3 assigns to the file.  
 Version IDs are Unicode, UTF-8 encoded, URL-ready, opaque strings that are no more than 1,024 bytes long. The following is an example:   
 `3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo`   
 For more information, refer to [Installing Python dependencies](https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html).   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

 ** RequirementsS3Path **   <a name="mwaa-Type-Environment-RequirementsS3Path"></a>
The relative path to the `requirements.txt` file in your Amazon S3 bucket. For example, `s3://mwaa-environment/requirements.txt`. For more information, refer to [Installing Python dependencies](https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `.*`   
Required: No

 ** Schedulers **   <a name="mwaa-Type-Environment-Schedulers"></a>
The number of Apache Airflow schedulers that run in your Amazon MWAA environment.  
Type: Integer  
Valid Range: Maximum value of 5.  
Required: No

 ** ServiceRoleArn **   <a name="mwaa-Type-Environment-ServiceRoleArn"></a>
The Amazon Resource Name (ARN) for the service-linked role of the environment. For more information, refer to [Amazon MWAA Service-linked role](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-slr.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `arn:aws(-[a-z]+)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`   
Required: No

 ** SourceBucketArn **   <a name="mwaa-Type-Environment-SourceBucketArn"></a>
The Amazon Resource Name (ARN) of the Amazon S3 bucket where your DAG code and supporting files are stored. For example, `arn:aws:s3:::my-airflow-bucket-unique-name`. For more information, refer to [Create an Amazon S3 bucket for Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-s3-bucket.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `arn:aws(-[a-z]+)?:s3:::[a-z0-9.\-]+`   
Required: No

 ** StartupScriptS3ObjectVersion **   <a name="mwaa-Type-Environment-StartupScriptS3ObjectVersion"></a>
The version of the startup shell script in your Amazon S3 bucket. You must specify the [version ID](https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html) that Amazon S3 assigns to the file.  
 Version IDs are Unicode, UTF-8 encoded, URL-ready, opaque strings that are no more than 1,024 bytes long. The following is an example:   
 `3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo`   
 For more information, refer to [Using a startup script](https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html).   
Type: String  
Required: No

 ** StartupScriptS3Path **   <a name="mwaa-Type-Environment-StartupScriptS3Path"></a>
The relative path to the startup shell script in your Amazon S3 bucket. For example, `s3://mwaa-environment/startup.sh`.  
 Amazon MWAA runs the script as your environment starts, and before running the Apache Airflow process. You can use this script to install dependencies, modify Apache Airflow configuration options, and set environment variables. For more information, refer to [Using a startup script](https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html).   
Type: String  
Required: No

 ** Status **   <a name="mwaa-Type-Environment-Status"></a>
The status of the Amazon MWAA environment.  
Valid values:  
+  `CREATING` - The request to create the environment is in progress.
+  `CREATING_SNAPSHOT` - The request to update environment details, or upgrade the environment version, is in progress and Amazon MWAA is creating a storage volume snapshot of the Amazon RDS database cluster associated with the environment. A database snapshot is a backup created at a specific point in time. Amazon MWAA uses snapshots to recover environment metadata if the process to update or upgrade an environment fails.
+  `CREATE_FAILED` - The request to create the environment failed and the environment was not created.
+  `AVAILABLE` - The request was successful and the environment is ready to use.
+  `PENDING` - The request was successful, but the process to create the environment is paused until you create the required VPC endpoints in your VPC. After you create the VPC endpoints, the process resumes.
+  `UPDATING` - The request to update the environment is in progress.
+  `ROLLING_BACK` - The request to update environment details or upgrade the environment version failed and Amazon MWAA is restoring the environment using the latest storage volume snapshot.
+  `DELETING` - The request to delete the environment is in progress.
+  `DELETED` - The request to delete the environment is complete, and the environment has been deleted.
+  `UNAVAILABLE` - The request failed, but the environment did not return to its previous state and is not stable.
+  `UPDATE_FAILED` - The request to update the environment failed and the environment was restored to its previous state successfully and is ready to use.
+  `MAINTENANCE` - The environment is undergoing maintenance. Depending on the type of work Amazon MWAA is performing, your environment might be unavailable during this process. Note that as part of the maintenance work, Amazon MWAA performs [UpdateEnvironment](API_UpdateEnvironment.md) with a `GRACEFUL` [https://docs.aws.amazon.com/mwaa/latest/API/API_UpdateEnvironment.html#mwaa-UpdateEnvironment-request-WorkerReplacementStrategy](https://docs.aws.amazon.com/mwaa/latest/API/API_UpdateEnvironment.html#mwaa-UpdateEnvironment-request-WorkerReplacementStrategy).
You can review our troubleshooting guide for a list of common errors and their solutions. For more information, refer to [Amazon MWAA troubleshooting](https://docs.aws.amazon.com/mwaa/latest/userguide/troubleshooting.html).  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | AVAILABLE | UPDATING | DELETING | DELETED | UNAVAILABLE | UPDATE_FAILED | ROLLING_BACK | CREATING_SNAPSHOT | PENDING | MAINTENANCE`   
Required: No

 ** Tags **   <a name="mwaa-Type-Environment-Tags"></a>
The key-value tag pairs associated to your environment. For example, `"Environment": "Staging"`. For more information, refer to [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Value Length Constraints: Minimum length of 1. Maximum length of 256.  
Value Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-@]*)`   
Required: No

 ** WebserverAccessMode **   <a name="mwaa-Type-Environment-WebserverAccessMode"></a>
The Apache Airflow *web server* access mode. For more information, refer to [Apache Airflow access modes](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-networking.html).  
If set to `PUBLIC_AND_PRIVATE`, creates both a public network load balancer (NLB) for browser access and a private VPC endpoint (VPCE) for worker-to-webserver communication. This mode is only available for Apache Airflow version 3.2 and later.  
Type: String  
Valid Values: `PRIVATE_ONLY | PUBLIC_ONLY | PUBLIC_AND_PRIVATE`   
Required: No

 ** WebserverUrl **   <a name="mwaa-Type-Environment-WebserverUrl"></a>
The Apache Airflow *web server* host name for the Amazon MWAA environment. For more information, refer to [Accessing the Apache Airflow UI](https://docs.aws.amazon.com/mwaa/latest/userguide/access-airflow-ui.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `https://.+`   
Required: No

 ** WebserverVpcEndpointService **   <a name="mwaa-Type-Environment-WebserverVpcEndpointService"></a>
The VPC endpoint for the environment's web server.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `([a-z.-]+)?com\.amazonaws\.vpce\.[a-z0-9\-]+\.[a-zA-Z_0-9+=,.@\-_/]+`   
Required: No

 ** WeeklyMaintenanceWindowStart **   <a name="mwaa-Type-Environment-WeeklyMaintenanceWindowStart"></a>
The day and time of the week in Coordinated Universal Time (UTC) 24-hour standard time that weekly maintenance updates are scheduled. For example: `TUE:03:30`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 9.  
Pattern: `.*(MON|TUE|WED|THU|FRI|SAT|SUN):([01]\d|2[0-3]):(00|30).*`   
Required: No

## See Also
<a name="API_Environment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/Environment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/Environment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/Environment) 