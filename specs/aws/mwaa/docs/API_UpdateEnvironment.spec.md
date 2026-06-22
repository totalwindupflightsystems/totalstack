---
id: "@specs/aws/mwaa/docs/API_UpdateEnvironment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateEnvironment"
status: active
depends_on:
  - "@specs/aws/mwaa/meta"
---

# UpdateEnvironment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/mwaa/docs/API_UpdateEnvironment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateEnvironment
<a name="API_UpdateEnvironment"></a>

Updates an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

## Request Syntax
<a name="API_UpdateEnvironment_RequestSyntax"></a>

```
PATCH /environments/{{Name}} HTTP/1.1
Content-type: application/json

{
   "AirflowConfigurationOptions": { 
      "{{string}}" : "{{string}}" 
   },
   "AirflowVersion": "{{string}}",
   "DagS3Path": "{{string}}",
   "EnvironmentClass": "{{string}}",
   "ExecutionRoleArn": "{{string}}",
   "LoggingConfiguration": { 
      "DagProcessingLogs": { 
         "Enabled": {{boolean}},
         "LogLevel": "{{string}}"
      },
      "SchedulerLogs": { 
         "Enabled": {{boolean}},
         "LogLevel": "{{string}}"
      },
      "TaskLogs": { 
         "Enabled": {{boolean}},
         "LogLevel": "{{string}}"
      },
      "WebserverLogs": { 
         "Enabled": {{boolean}},
         "LogLevel": "{{string}}"
      },
      "WorkerLogs": { 
         "Enabled": {{boolean}},
         "LogLevel": "{{string}}"
      }
   },
   "MaxWebservers": {{number}},
   "MaxWorkers": {{number}},
   "MinWebservers": {{number}},
   "MinWorkers": {{number}},
   "NetworkConfiguration": { 
      "SecurityGroupIds": [ "{{string}}" ]
   },
   "PluginsS3ObjectVersion": "{{string}}",
   "PluginsS3Path": "{{string}}",
   "RequirementsS3ObjectVersion": "{{string}}",
   "RequirementsS3Path": "{{string}}",
   "Schedulers": {{number}},
   "SourceBucketArn": "{{string}}",
   "StartupScriptS3ObjectVersion": "{{string}}",
   "StartupScriptS3Path": "{{string}}",
   "WebserverAccessMode": "{{string}}",
   "WeeklyMaintenanceWindowStart": "{{string}}",
   "WorkerReplacementStrategy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-uri-Name"></a>
The name of your Amazon MWAA environment. For example, `MyMWAAEnvironment`.  
Length Constraints: Minimum length of 1. Maximum length of 80.  
Pattern: `[a-zA-Z][0-9a-zA-Z-_]*`   
Required: Yes

## Request Body
<a name="API_UpdateEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AirflowConfigurationOptions](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-AirflowConfigurationOptions"></a>
A list of key-value pairs containing the Apache Airflow configuration options you want to attach to your environment. For more information, refer to [Apache Airflow configuration options](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variables.html).  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 64.  
Key Pattern: `[a-z]+([a-z0-9._]*[a-z0-9_]+)?`   
Value Length Constraints: Minimum length of 1. Maximum length of 65536.  
Value Pattern: `[ -~]+`   
Required: No

 ** [AirflowVersion](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-AirflowVersion"></a>
The Apache Airflow version for your environment. To upgrade your environment, specify a newer version of Apache Airflow supported by Amazon MWAA. To downgrade your environment, specify an older version of Apache Airflow supported by Amazon MWAA.  
Before you upgrade or downgrade an environment, make sure your requirements, DAGs, plugins, and other resources used in your workflows are compatible with the new Apache Airflow version. For more information about updating your resources, see [Upgrading and downgrading an Amazon MWAA environment](https://docs.aws.amazon.com/mwaa/latest/userguide/upgrading-environment.html).  
Valid values: `2.7.2`, `2.8.1`, `2.9.2`, `2.10.1`, `2.10.3`, `2.11.0`, and `3.0.6`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32.  
Pattern: `[0-9a-z.]+`   
Required: No

 ** [DagS3Path](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-DagS3Path"></a>
The relative path to the DAGs folder on your Amazon S3 bucket. For example, `dags`. For more information, refer to [Adding or updating DAGs](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-folder.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `.*`   
Required: No

 ** [EnvironmentClass](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-EnvironmentClass"></a>
The environment class type. Valid values: `mw1.micro`, `mw1.small`, `mw1.medium`, `mw1.large`, `mw1.xlarge`, and `mw1.2xlarge`. For more information, refer to [Amazon MWAA environment class](https://docs.aws.amazon.com/mwaa/latest/userguide/environment-class.html).   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

 ** [ExecutionRoleArn](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-ExecutionRoleArn"></a>
The Amazon Resource Name (ARN) of the execution role in IAM that allows MWAA to access AWS resources in your environment. For example, `arn:aws:iam::123456789:role/my-execution-role`. For more information, refer to [Amazon MWAA Execution role](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-create-role.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `arn:aws(-[a-z]+)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`   
Required: No

 ** [LoggingConfiguration](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-LoggingConfiguration"></a>
The Apache Airflow log types to send to CloudWatch Logs.  
Type: [LoggingConfigurationInput](API_LoggingConfigurationInput.md) object  
Required: No

 ** [MaxWebservers](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-MaxWebservers"></a>
 The maximum number of web servers that you want to run in your environment. Amazon MWAA scales the number of Apache Airflow web servers up to the number you specify for `MaxWebservers` when you interact with your Apache Airflow environment using Apache Airflow REST API, or the Apache Airflow CLI. For example, in scenarios where your workload requires network calls to the Apache Airflow REST API with a high transaction-per-second (TPS) rate, Amazon MWAA will increase the number of web servers up to the number set in `MaxWebserers`. As TPS rates decrease Amazon MWAA disposes of the additional web servers, and scales down to the number set in `MinxWebserers`.   
Valid values: For environments larger than mw1.micro, accepts values from `2` to `5`. Defaults to `2` for all environment sizes except mw1.micro, which defaults to `1`.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** [MaxWorkers](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-MaxWorkers"></a>
The maximum number of workers that you want to run in your environment. MWAA scales the number of Apache Airflow workers up to the number you specify in the `MaxWorkers` field. For example, `20`. When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the one worker that is included with your environment, or the number you specify in `MinWorkers`.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** [MinWebservers](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-MinWebservers"></a>
 The minimum number of web servers that you want to run in your environment. Amazon MWAA scales the number of Apache Airflow web servers up to the number you specify for `MaxWebservers` when you interact with your Apache Airflow environment using Apache Airflow REST API, or the Apache Airflow CLI. As the transaction-per-second rate, and the network load, decrease, Amazon MWAA disposes of the additional web servers, and scales down to the number set in `MinxWebserers`.   
Valid values: For environments larger than mw1.micro, accepts values from `2` to `5`. Defaults to `2` for all environment sizes except mw1.micro, which defaults to `1`.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** [MinWorkers](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-MinWorkers"></a>
The minimum number of workers that you want to run in your environment. MWAA scales the number of Apache Airflow workers up to the number you specify in the `MaxWorkers` field. When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the worker count you specify in the `MinWorkers` field. For example, `2`.  
Type: Integer  
Valid Range: Minimum value of 1.  
Required: No

 ** [NetworkConfiguration](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-NetworkConfiguration"></a>
The VPC networking components used to secure and enable network traffic between the AWS resources for your environment. For more information, refer to [About networking on Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html).  
Type: [UpdateNetworkConfigurationInput](API_UpdateNetworkConfigurationInput.md) object  
Required: No

 ** [PluginsS3ObjectVersion](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-PluginsS3ObjectVersion"></a>
The version of the plugins.zip file on your Amazon S3 bucket. You must specify a version each time a `plugins.zip` file is updated. For more information, refer to [How S3 Versioning works](https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

 ** [PluginsS3Path](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-PluginsS3Path"></a>
The relative path to the `plugins.zip` file on your Amazon S3 bucket. For example, `plugins.zip`. If specified, then the plugins.zip version is required. For more information, refer to [Installing custom plugins](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `.*`   
Required: No

 ** [RequirementsS3ObjectVersion](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-RequirementsS3ObjectVersion"></a>
The version of the requirements.txt file on your Amazon S3 bucket. You must specify a version each time a `requirements.txt` file is updated. For more information, refer to [How S3 Versioning works](https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

 ** [RequirementsS3Path](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-RequirementsS3Path"></a>
The relative path to the `requirements.txt` file on your Amazon S3 bucket. For example, `requirements.txt`. If specified, then a file version is required. For more information, refer to [Installing Python dependencies](https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `.*`   
Required: No

 ** [Schedulers](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-Schedulers"></a>
The number of Apache Airflow schedulers to run in your Amazon MWAA environment.  
Type: Integer  
Valid Range: Maximum value of 5.  
Required: No

 ** [SourceBucketArn](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-SourceBucketArn"></a>
The Amazon Resource Name (ARN) of the Amazon S3 bucket where your DAG code and supporting files are stored. For example, `arn:aws:s3:::my-airflow-bucket-unique-name`. For more information, refer to [Create an Amazon S3 bucket for Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-s3-bucket.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `arn:aws(-[a-z]+)?:s3:::[a-z0-9.\-]+`   
Required: No

 ** [StartupScriptS3ObjectVersion](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-StartupScriptS3ObjectVersion"></a>
 The version of the startup shell script in your Amazon S3 bucket. You must specify the [version ID](https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html) that Amazon S3 assigns to the file every time you update the script.   
 Version IDs are Unicode, UTF-8 encoded, URL-ready, opaque strings that are no more than 1,024 bytes long. The following is an example:   
 `3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo`   
 For more information, refer to [Using a startup script](https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html).   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

 ** [StartupScriptS3Path](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-StartupScriptS3Path"></a>
The relative path to the startup shell script in your Amazon S3 bucket. For example, `s3://mwaa-environment/startup.sh`.  
 Amazon MWAA runs the script as your environment starts, and before running the Apache Airflow process. You can use this script to install dependencies, modify Apache Airflow configuration options, and set environment variables. For more information, refer to [Using a startup script](https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html).   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `.*`   
Required: No

 ** [WebserverAccessMode](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-WebserverAccessMode"></a>
The Apache Airflow *Web server* access mode. For more information, refer to [Apache Airflow access modes](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-networking.html).  
If set to `PUBLIC_AND_PRIVATE`, creates both a public network load balancer (NLB) for browser access and a private VPC endpoint (VPCE) for worker-to-webserver communication. This mode is only available for Apache Airflow version 3.2 and later.  
Type: String  
Valid Values: `PRIVATE_ONLY | PUBLIC_ONLY | PUBLIC_AND_PRIVATE`   
Required: No

 ** [WeeklyMaintenanceWindowStart](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-WeeklyMaintenanceWindowStart"></a>
The day and time of the week in Coordinated Universal Time (UTC) 24-hour standard time to start weekly maintenance updates of your environment in the following format: `DAY:HH:MM`. For example: `TUE:03:30`. You can specify a start time in 30 minute increments only.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 9.  
Pattern: `.*(MON|TUE|WED|THU|FRI|SAT|SUN):([01]\d|2[0-3]):(00|30).*`   
Required: No

 ** [WorkerReplacementStrategy](#API_UpdateEnvironment_RequestSyntax) **   <a name="mwaa-UpdateEnvironment-request-WorkerReplacementStrategy"></a>
The worker replacement strategy to use when updating the environment.  
You can select one of the following strategies:  
+  **Forced -** Stops and replaces Apache Airflow workers without waiting for tasks to complete before an update.
+  **Graceful -** Allows Apache Airflow workers to complete running tasks for up to 12 hours during an update before they're stopped and replaced.
Type: String  
Valid Values: `FORCED | GRACEFUL`   
Required: No

## Response Syntax
<a name="API_UpdateEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string"
}
```

## Response Elements
<a name="API_UpdateEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateEnvironment_ResponseSyntax) **   <a name="mwaa-UpdateEnvironment-response-Arn"></a>
The Amazon Resource Name (ARN) of the Amazon MWAA environment. For example, `arn:aws:airflow:us-east-1:123456789012:environment/MyMWAAEnvironment`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1224.  
Pattern: `arn:aws(-[a-z]+)?:airflow:[a-z0-9\-]+:\d{12}:environment/\w+.*` 

## Errors
<a name="API_UpdateEnvironment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
InternalServerException: An internal error has occurred.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
ResourceNotFoundException: The resource is not available.  
HTTP Status Code: 404

 ** ServiceUnavailableException **   
ServiceUnavailableException: The service is currently unavailable.  
HTTP Status Code: 503

 ** ValidationException **   
ValidationException: The provided input is not valid.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mwaa-2020-07-01/UpdateEnvironment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mwaa-2020-07-01/UpdateEnvironment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/UpdateEnvironment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mwaa-2020-07-01/UpdateEnvironment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/UpdateEnvironment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mwaa-2020-07-01/UpdateEnvironment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mwaa-2020-07-01/UpdateEnvironment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mwaa-2020-07-01/UpdateEnvironment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mwaa-2020-07-01/UpdateEnvironment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/UpdateEnvironment) 