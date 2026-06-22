---
id: "@specs/aws/timestream-influxdb/docs/getting-started.java-v2"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Java v2"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Java v2

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/getting-started.java-v2
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Java v2
<a name="getting-started.java-v2"></a>

To get started with the [Java 2.0 SDK](https://aws.amazon.com/sdk-for-java/) and Amazon Timestream, complete the prerequisites, described below.

Once you've completed the necessary prerequisites for the Java 2.0 SDK, you can get started with the [Code samples](code-samples.md).

## Prerequisites
<a name="getting-started.java-v2.prereqs"></a>

Before you get started with Java, you must do the following:

1. Follow the AWS setup instructions in [Accessing Timestream for LiveAnalytics](accessing.md).

1. You can configure the AWS SDK as a Maven dependency as described in [ Using the SDK with Apache Maven](https://docs.aws.amazon.com/sdk-for-java/v2/developer-guide/welcome.html). 

1. Set up a Java development environment by downloading and installing the following:
   + Java SE Development Kit 8 (such as [Amazon Corretto 8](https://docs.aws.amazon.com/corretto/latest/corretto-8-ug/downloads-list.html)).
   + Java IDE (such as [Eclipse](http://www.eclipse.org) or [IntelliJ](https://www.jetbrains.com/idea/)).

      For more information, see [Getting Started with the AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html) 

## Using Apache Maven
<a name="getting-started.java-v2.with-maven"></a>

 You can use [Apache Maven ](https://maven.apache.org/) to configure and build AWS SDK for Java projects. 

**Note**  
To use Apache Maven, ensure your Java SDK and runtime are 1.8 or higher.

You can configure the AWS SDK as a Maven dependency as described in [ Using the SDK with Apache Maven](https://docs.aws.amazon.com/sdk-for-java/v2/developer-guide/welcome.html). The changes required to the pom.xml file are described [here](https://docs.aws.amazon.com/sdk-for-java/v2/migration-guide/whats-different.html#adding-v2). 

You can run compile and run your source code with the following command:

```
mvn clean compile
mvn exec:java -Dexec.mainClass=<your source code Main class>
```

**Note**  
 `<your source code Main class>` is the path to your Java source code's main class. 