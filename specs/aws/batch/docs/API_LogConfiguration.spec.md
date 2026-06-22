---
id: "@specs/aws/batch/docs/API_LogConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS LogConfiguration"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# LogConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_LogConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# LogConfiguration
<a name="API_LogConfiguration"></a>

Log configuration options to send to a custom log driver for the container.

## Contents
<a name="API_LogConfiguration_Contents"></a>

 ** logDriver **   <a name="Batch-Type-LogConfiguration-logDriver"></a>
The log driver to use for the container. The valid values that are listed for this parameter are log drivers that the Amazon ECS container agent can communicate with by default.  
The supported log drivers are `awsfirelens`, `awslogs`, `fluentd`, `gelf`, `json-file`, `journald`, `logentries`, `syslog`, and `splunk`.  
Jobs that are running on Fargate resources are restricted to the `awslogs` and `splunk` log drivers.  
awsfirelens  
Specifies the firelens logging driver. For more information on configuring Firelens, see [Send Amazon ECS logs to an AWS service or AWS Partner](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html) in the *Amazon Elastic Container Service Developer Guide*.  
awslogs  
Specifies the Amazon CloudWatch Logs logging driver. For more information, see [Using the awslogs log driver](https://docs.aws.amazon.com/batch/latest/userguide/using_awslogs.html) in the * AWS Batch User Guide* and [Amazon CloudWatch Logs logging driver](https://docs.docker.com/config/containers/logging/awslogs/) in the Docker documentation.  
fluentd  
Specifies the Fluentd logging driver. For more information including usage and options, see [Fluentd logging driver](https://docs.docker.com/config/containers/logging/fluentd/) in the *Docker documentation*.  
gelf  
Specifies the Graylog Extended Format (GELF) logging driver. For more information including usage and options, see [Graylog Extended Format logging driver](https://docs.docker.com/config/containers/logging/gelf/) in the *Docker documentation*.  
journald  
Specifies the journald logging driver. For more information including usage and options, see [Journald logging driver](https://docs.docker.com/config/containers/logging/journald/) in the *Docker documentation*.  
json-file  
Specifies the JSON file logging driver. For more information including usage and options, see [JSON File logging driver](https://docs.docker.com/config/containers/logging/json-file/) in the *Docker documentation*.  
splunk  
Specifies the Splunk logging driver. For more information including usage and options, see [Splunk logging driver](https://docs.docker.com/config/containers/logging/splunk/) in the *Docker documentation*.  
syslog  
Specifies the syslog logging driver. For more information including usage and options, see [Syslog logging driver](https://docs.docker.com/config/containers/logging/syslog/) in the *Docker documentation*.
If you have a custom driver that's not listed earlier that you want to work with the Amazon ECS container agent, you can fork the Amazon ECS container agent project that's [available on GitHub](https://github.com/aws/amazon-ecs-agent) and customize it to work with that driver. We encourage you to submit pull requests for changes that you want to have included. However, Amazon Web Services doesn't currently support running modified copies of this software.
This parameter requires version 1.18 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`   
Type: String  
Valid Values: `json-file | syslog | journald | gelf | fluentd | awslogs | splunk | awsfirelens`   
Required: Yes

 ** options **   <a name="Batch-Type-LogConfiguration-options"></a>
The configuration options to send to the log driver. This parameter requires version 1.19 of the Docker Remote API or greater on your container instance. To check the Docker Remote API version on your container instance, log in to your container instance and run the following command: `sudo docker version | grep "Server API version"`   
Type: String to string map  
Required: No

 ** secretOptions **   <a name="Batch-Type-LogConfiguration-secretOptions"></a>
The secrets to pass to the log configuration. For more information, see [Specifying sensitive data](https://docs.aws.amazon.com/batch/latest/userguide/specifying-sensitive-data.html) in the * AWS Batch User Guide*.  
Type: Array of [Secret](API_Secret.md) objects  
Required: No

## See Also
<a name="API_LogConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/LogConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/LogConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/LogConfiguration) 