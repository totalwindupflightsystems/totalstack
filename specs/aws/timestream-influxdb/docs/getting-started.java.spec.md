---
id: "@specs/aws/timestream-influxdb/docs/getting-started.java"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Java"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Java

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/getting-started.java
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Java
<a name="getting-started.java"></a>

To get started with the [Java 1.0 SDK](https://aws.amazon.com/sdk-for-java/) and Amazon Timestream, complete the prerequisites, described below.

Once you've completed the necessary prerequisites for the Java SDK, you can get started with the [Code samples](code-samples.md).

## Prerequisites
<a name="getting-started.java.prereqs"></a>

Before you get started with Java, you must do the following:

1. Follow the AWS setup instructions in [Accessing Timestream for LiveAnalytics](accessing.md).

1. Set up a Java development environment by downloading and installing the following:
   + Java SE Development Kit 8 (such as [Amazon Corretto 8](https://docs.aws.amazon.com/corretto/latest/corretto-8-ug/downloads-list.html)).
   + Java IDE (such as [Eclipse](http://www.eclipse.org) or [IntelliJ](https://www.jetbrains.com/idea/)).

      For more information, see [Getting Started with the AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html) 

1. Configure your AWS credentials and Region for development:
   + Set up your AWS security credentials for use with the AWS SDK for Java.
   + Set your AWS Region to determine your default Timestream for LiveAnalytics endpoint.

## Using Apache Maven
<a name="getting-started.java.with-maven"></a>

 You can use [Apache Maven ](https://maven.apache.org/) to configure and build AWS SDK for Java projects. 

**Note**  
To use Apache Maven, ensure your Java SDK and runtime are 1.8 or higher.

You can configure the AWS SDK as a Maven dependency as described in [ Using the SDK with Apache Maven](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-project-maven.html). 

You can run compile and run your source code with the following command:

```
mvn clean compile
mvn exec:java -Dexec.mainClass=<your source code Main class>
```

**Note**  
 `<your source code Main class>` is the path to your Java source code's main class. 

## Setting your AWS credentials
<a name="getting-started.java.credentials"></a>

The [AWS SDK for Java](https://aws.amazon.com/sdk-for-java) requires that you provide AWS credentials to your application at runtime. The code examples in this guide assume that you are using an AWS credentials file, as described in [Set up AWS Credentials and Region for Development](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/setup-credentials.html) in the *AWS SDK for Java Developer Guide*.

The following is an example of an AWS credentials file named `~/.aws/credentials`, where the tilde character (`~`) represents your home directory.

```
[default] 
aws_access_key_id = {{AWS access key ID goes here}} 
aws_secret_access_key = {{Secret key goes here}}
```