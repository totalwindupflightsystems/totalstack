---
id: "@specs/aws/appconfig/docs/appconfig-integration-containers-agent-retrieving-data"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Retrieving configuration data for applications running in Amazon ECS and Amazon EKS"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# Retrieving configuration data for applications running in Amazon ECS and Amazon EKS

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-integration-containers-agent-retrieving-data
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Retrieving configuration data for applications running in Amazon ECS and Amazon EKS
<a name="appconfig-integration-containers-agent-retrieving-data"></a>

You can retrieve configuration data from AWS AppConfig Agent for applications running in Amazon ECS and Amazon EKS by using an HTTP localhost call. The following examples use `curl` with an HTTP client. You can call the agent using any available HTTP client supported by your application language or available libraries.

**Note**  
To retrieve configuration data if your application uses a forward slash, for example "test-backend/test-service", you will need to use URL encoding.

**To retrieve the full content of any deployed configuration**

```
$ curl "http://localhost:2772/applications/{{application_name}}/environments/{{environment_name}}/configurations/{{configuration_name}}"
```

**To retrieve a single flag and its attributes from an AWS AppConfig configuration of type `Feature Flag`**

```
$ curl "http://localhost:2772/applications/{{application_name}}/environments/{{environment_name}}/configurations/{{configuration_name}}?flag={{flag_name}}"
```

**To access multiple flags and their attributes from an AWS AppConfig configuration of type `Feature Flag`**

```
$ curl "http://localhost:2772/applications/{{application_name}}/environments/{{environment_name}}/configurations/{{configuration_name}}?flag={{flag_name_one}}&flag={{flag_name_two}}"
```

The call returns configuration metadata in HTTP headers, including the configuration version, content type, and configuration version label (if applicable). The body of the agent response contains the configuration content. Here is an example:

```
HTTP/1.1 200 OK
Configuration-Version: 1
Content-Type: application/json
Date: Tue, 18 Feb 2025 20:20:16 GMT
Content-Length: 31

My test config
```