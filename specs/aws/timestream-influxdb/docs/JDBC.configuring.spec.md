---
id: "@specs/aws/timestream-influxdb/docs/JDBC.configuring"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Configuring the JDBC driver"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Configuring the JDBC driver

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/JDBC.configuring
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Configuring the JDBC driver for Timestream for LiveAnalytics
<a name="JDBC.configuring"></a>

Follow the steps below to configure the JDBC driver. 

**Topics**
+ [Timestream for LiveAnalytics JDBC driver JARs](#w2aab7c44c37b7b7)
+ [Timestream for LiveAnalytics JDBC driver class and URL format](#w2aab7c44c37b7b9)
+ [Sample application](#w2aab7c44c37b7c11)

## Timestream for LiveAnalytics JDBC driver JARs
<a name="w2aab7c44c37b7b7"></a>

 You can obtain the Timestream for LiveAnalytics JDBC driver via direct download or by adding the driver as a Maven dependency. 
+  *As a direct download:*. To directly download the Timestream for LiveAnalytics JDBC driver, complete the following steps:

  1. Navigate to [ https://github.com/awslabs/amazon-timestream-driver-jdbc/releases ](https://github.com/awslabs/amazon-timestream-driver-jdbc/releases) 

  1. You can use `amazon-timestream-jdbc-1.0.1-shaded.jar` directly with your business intelligence tools and applications

  1. Download `amazon-timestream-jdbc-1.0.1-javadoc.jar` to a directory of your choice.

  1. In the directory where you have downloaded `amazon-timestream-jdbc-1.0.1-javadoc.jar`, run the following command to extract the Javadoc HTML files: 

     ```
     jar -xvf amazon-timestream-jdbc-1.0.1-javadoc.jar
     ```
+  *As a Maven dependency:* To add the Timestream for LiveAnalytics JDBC driver as a Maven dependency, complete the following steps:

  1. Navigate to and open your application's `pom.xml` file in an editor of your choice.

  1. Add the JDBC driver as a dependency into your application's `pom.xml` file:

     ```
     <!-- https://mvnrepository.com/artifact/software.amazon.timestream/amazon-timestream-jdbc -->
     <dependency>
         <groupId>software.amazon.timestream</groupId>
         <artifactId>amazon-timestream-jdbc</artifactId>
         <version>1.0.1</version>
     </dependency>
     ```

## Timestream for LiveAnalytics JDBC driver class and URL format
<a name="w2aab7c44c37b7b9"></a>

 The driver class for Timestream for LiveAnalytics JDBC driver is: 

```
software.amazon.timestream.jdbc.TimestreamDriver
```

 The Timestream JDBC driver requires the following JDBC URL format: 

```
jdbc:timestream:
```

 To specify database properties through the JDBC URL, use the following URL format: 

```
jdbc:timestream://
```

## Sample application
<a name="w2aab7c44c37b7c11"></a>

To help you get started with using Timestream for LiveAnalytics with JDBC, we've created a fully functional sample application in GitHub.

1. Create a database with sample data following the instructions described [here](getting-started.db-w-sample-data.md#getting-started.db-w-sample-data.using-console).

1. Clone the GitHub repository for the [sample application for JDBC](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/integrations/jdbc) following the instructions from [GitHub](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

1. Follow the instructions in the [README](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/integrations/jdbc/README.md) to get started with the sample application.