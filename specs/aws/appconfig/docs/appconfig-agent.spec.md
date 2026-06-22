---
id: "@specs/aws/appconfig/docs/appconfig-agent"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS What is AWS AppConfig Agent?"
status: active
depends_on:
  - "@specs/aws/appconfig/meta"
---

# What is AWS AppConfig Agent?

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appconfig/docs/appconfig-agent
> **target_lang:** meta — documentation tier. ALL sections preserved.



# What is AWS AppConfig Agent?
<a name="appconfig-agent"></a>

AWS AppConfig Agent is an Amazon-developed and managed process for retrieving configuration data from AWS AppConfig. With the agent, you can cache configuration data locally and asynchronously poll the AWS AppConfig data plane service for updates. This caching/polling process ensures that your configuration data is always available for your application while minimizing latency and cost. The agent is not the only way to retrieve configuration data from AWS AppConfig, but it is the recommended way. The agent enhances application processing and management in the following ways: 
+ The agent calls AWS AppConfig on your behalf by using an AWS Identity and Access Management (IAM) principal and managing a local cache of configuration data. By retrieving configuration data from the local cache, your application requires fewer code updates to manage configuration data, retrieves configuration data in milliseconds, and isn't affected by network issues that can disrupt calls for such data.
+ The agent offers a native experience for retrieving and resolving AWS AppConfig feature flags. 
+ Out of the box, the agent provides best practices for caching strategies, polling intervals, and availability of local configuration data while tracking the configuration tokens needed for subsequent service calls. 
+ While running in the background, the agent periodically polls the AWS AppConfig data plane service for configuration data updates. Your application can retrieve the data by connecting to localhost on port 2772 (a customizable default port value) and calling HTTP GET to retrieve the data. 

**Note**  
AWS AppConfig Agent caches data the first time the service retrieves your configuration data. For this reason, the first call to retrieve data is slower than subsequent calls. 

The following diagram shows how AWS AppConfig Agent works.

![Diagram of how AWS AppConfig works](http://docs.aws.amazon.com/appconfig/latest/userguide/images/AppConfigAgent.png)


1. Your application requests configuration data from the agent.

1. The agent returns data from an in-memory cache.

1. The agent asynchronously polls the AWS AppConfig service for the latest configuration data on a predefined cadence. The latest configuration data is always stored in a cache in memory. 