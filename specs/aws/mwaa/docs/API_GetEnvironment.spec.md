---
id: "@specs/aws/mwaa/docs/API_GetEnvironment"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetEnvironment"
status: active
depends_on:
  - "@specs/aws/mwaa/meta"
---

# GetEnvironment

> **source:** AWS Documentation
> **spec:id:** @specs/aws/mwaa/docs/API_GetEnvironment
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetEnvironment
<a name="API_GetEnvironment"></a>

Describes an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

## Request Syntax
<a name="API_GetEnvironment_RequestSyntax"></a>

```
GET /environments/{{Name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetEnvironment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_GetEnvironment_RequestSyntax) **   <a name="mwaa-GetEnvironment-request-uri-Name"></a>
The name of the Amazon MWAA environment. For example, `MyMWAAEnvironment`.  
Length Constraints: Minimum length of 1. Maximum length of 80.  
Pattern: `[a-zA-Z][0-9a-zA-Z-_]*`   
Required: Yes

## Request Body
<a name="API_GetEnvironment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Environment": { 
      "AirflowConfigurationOptions": { 
         "string" : "string" 
      },
      "AirflowVersion": "string",
      "Arn": "string",
      "CeleryExecutorQueue": "string",
      "CreatedAt": number,
      "DagS3Path": "string",
      "DatabaseVpcEndpointService": "string",
      "EndpointManagement": "string",
      "EnvironmentClass": "string",
      "ExecutionRoleArn": "string",
      "KmsKey": "string",
      "LastUpdate": { 
         "CreatedAt": number,
         "Error": { 
            "ErrorCode": "string",
            "ErrorMessage": "string"
         },
         "Source": "string",
         "Status": "string",
         "WorkerReplacementStrategy": "string"
      },
      "LoggingConfiguration": { 
         "DagProcessingLogs": { 
            "CloudWatchLogGroupArn": "string",
            "Enabled": boolean,
            "LogLevel": "string"
         },
         "SchedulerLogs": { 
            "CloudWatchLogGroupArn": "string",
            "Enabled": boolean,
            "LogLevel": "string"
         },
         "TaskLogs": { 
            "CloudWatchLogGroupArn": "string",
            "Enabled": boolean,
            "LogLevel": "string"
         },
         "WebserverLogs": { 
            "CloudWatchLogGroupArn": "string",
            "Enabled": boolean,
            "LogLevel": "string"
         },
         "WorkerLogs": { 
            "CloudWatchLogGroupArn": "string",
            "Enabled": boolean,
            "LogLevel": "string"
         }
      },
      "MaxWebservers": number,
      "MaxWorkers": number,
      "MinWebservers": number,
      "MinWorkers": number,
      "Name": "string",
      "NetworkConfiguration": { 
         "SecurityGroupIds": [ "string" ],
         "SubnetIds": [ "string" ]
      },
      "PluginsS3ObjectVersion": "string",
      "PluginsS3Path": "string",
      "RequirementsS3ObjectVersion": "string",
      "RequirementsS3Path": "string",
      "Schedulers": number,
      "ServiceRoleArn": "string",
      "SourceBucketArn": "string",
      "StartupScriptS3ObjectVersion": "string",
      "StartupScriptS3Path": "string",
      "Status": "string",
      "Tags": { 
         "string" : "string" 
      },
      "WebserverAccessMode": "string",
      "WebserverUrl": "string",
      "WebserverVpcEndpointService": "string",
      "WeeklyMaintenanceWindowStart": "string"
   }
}
```

## Response Elements
<a name="API_GetEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Environment](#API_GetEnvironment_ResponseSyntax) **   <a name="mwaa-GetEnvironment-response-Environment"></a>
An object containing all available details about the environment.  
Type: [Environment](API_Environment.md) object

## Errors
<a name="API_GetEnvironment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
InternalServerException: An internal error has occurred.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
ResourceNotFoundException: The resource is not available.  
HTTP Status Code: 404

 ** ValidationException **   
ValidationException: The provided input is not valid.  
HTTP Status Code: 400

## See Also
<a name="API_GetEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mwaa-2020-07-01/GetEnvironment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mwaa-2020-07-01/GetEnvironment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mwaa-2020-07-01/GetEnvironment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mwaa-2020-07-01/GetEnvironment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mwaa-2020-07-01/GetEnvironment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mwaa-2020-07-01/GetEnvironment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mwaa-2020-07-01/GetEnvironment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mwaa-2020-07-01/GetEnvironment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mwaa-2020-07-01/GetEnvironment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mwaa-2020-07-01/GetEnvironment) 