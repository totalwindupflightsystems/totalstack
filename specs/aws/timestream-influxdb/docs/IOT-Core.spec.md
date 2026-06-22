---
id: "@specs/aws/timestream-influxdb/docs/IOT-Core"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AWS IoT Core"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# AWS IoT Core

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/IOT-Core
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# AWS IoT Core
<a name="IOT-Core"></a>

 You can collect data from IoT devices using [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/iot-gs.html) and route the data to Amazon Timestream through IoT Core rule actions. AWS IoT rule actions specify what to do when a rule is triggered. You can define actions to send data to an Amazon Timestream table, an Amazon DynamoDB database, and invoke an AWS Lambda function. 

 The Timestream action in IoT Rules is used to insert data from incoming messages directly into Timestream. The action parses the results of the [IoT Core SQL](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-reference.html) statement and stores data in Timestream. The names of the fields from returned SQL result set are used as the measure::name and the value of the field is the measure::value. 

 For example, consider the SQL statement and the sample message payload: 

```
SELECT temperature, humidity from 'iot/topic'
```

```
{
  "dataFormat": 5, 
  "rssi": -88,
  "temperature": 24.04,    
  "humidity": 43.605,    
  "pressure": 101082,    
  "accelerationX": 40,    
  "accelerationY": -20,    
  "accelerationZ": 1016,    
  "battery": 3007,    
  "txPower": 4,    
  "movementCounter": 219,    
  "device_id": 46216,
  "device_firmware_sku": 46216   
}
```

 If an IoT Core rule action for Timestream is created with the SQL statement above, two records will be added to Timestream with measure names temperature and humidity and measure values of 24.04 and 43.605, respectively. 

 You can modify the measure name of a record being added to Timestream by using the AS operator in the SELECT statement. The SQL statement below will create a record with the message name temp instead of temperature. 

 The data type of the measure are inferred from the data type of the value of the message payload. JSON data types such as integer, double, boolean, and string are mapped to Timestream data types of BIGINT, DOUBLE, BOOLEAN, and VARCHAR respectively. Data can also be forced to specific data types using the [cast()](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-functions.html#iot-sql-function-cast) function. You can specify the timestamp of the measure. If the timestamp is left blank, the time that the entry was processed is used. 

You can refer to the [ Timestream rules action documentation ](https://docs.aws.amazon.com/iot/latest/developerguide/timestream-rule-action.html) for additional details

 To create an IoT Core rule action to store data in Timestream, follow the steps below: 

**Topics**
+ [Prerequisites](#prereqs)
+ [Using the console](#using-console)
+ [Using the CLI](#using-cli)
+ [Sample application](#sample-app)
+ [Video tutorial](#video-tutorial)

## Prerequisites
<a name="prereqs"></a>

1. Create a database in Amazon Timestream using the instructions described in [Create a database](console_timestream.md#console_timestream.db.using-console).

1. Create a table in Amazon Timestream using the instructions described in [Create a table](console_timestream.md#console_timestream.table.using-console).

## Using the console
<a name="using-console"></a>

1. Use the AWS Management Console for AWS IoT Core to create a rule by clicking on **Manage** > **Messsage routing** > **Rules** followed by **Create rule**.

1. Set the rule name to a name of your choice and the SQL to the text shown below

   ```
   SELECT temperature as temp, humidity from 'iot/topic' 
   ```

1. Select Timestream from the Action list

1. Specify the Timestream database, table, and dimension names along with the role to write data into Timestream. If the role does not exist, you can create one by clicking on Create Roles

1. To test the rule, follow the instructions shown [here](https://docs.aws.amazon.com/iot/latest/developerguide/iot-ddb-rule.html#test-db-rule).

## Using the CLI
<a name="using-cli"></a>

 If you haven't installed the AWS Command Line Interface (AWS CLI), do so from [here](https://aws.amazon.com/cli/). 

1. Save the following rule payload in a JSON file called timestream\_rule.json. Replace {{arn:aws:iam::123456789012:role/TimestreamRole}} with your role arn which grants AWS IoT access to store data in Amazon Timestream

   ```
   { 
       "actions": [ 
               { 
                   "timestream": { 
                       "roleArn": "arn:aws:iam::123456789012:role/TimestreamRole", 
                       "tableName": "devices_metrics", 
                       "dimensions": [ 
                           { 
                               "name": "device_id", 
                               "value": "${clientId()}" 
                           }, 
                           { 
                               "name": "device_firmware_sku", 
                               "value": "My Static Metadata" 
                           } 
                       ], 
                       "databaseName": "record_devices" 
                   } 
               } 
       ], 
       "sql": "select * from 'iot/topic'", 
       "awsIotSqlVersion": "2016-03-23", 
       "ruleDisabled": false 
   }
   ```

1. Create a topic rule using the following command

   ```
   aws iot create-topic-rule --rule-name timestream_test --topic-rule-payload file://<path/to/timestream_rule.json> --region us-east-1 
   ```

1. Retrieve details of topic rule using the following command

   ```
   aws iot get-topic-rule --rule-name timestream_test 
   ```

1. Save the following message payload in a file called timestream\_msg.json

   ```
   {
     "dataFormat": 5, 
     "rssi": -88,
     "temperature": 24.04,    
     "humidity": 43.605,    
     "pressure": 101082,    
     "accelerationX": 40,    
     "accelerationY": -20,    
     "accelerationZ": 1016,    
     "battery": 3007,    
     "txPower": 4,    
     "movementCounter": 219,    
     "device_id": 46216,
     "device_firmware_sku": 46216   
   }
   ```

1. Test the rule using the following command

   ```
   aws iot-data publish --topic 'iot/topic' --payload file://<path/to/timestream_msg.json>
   ```

## Sample application
<a name="sample-app"></a>

 To help you get started with using Timestream with AWS IoT Core, we've created a fully functional sample application that creates the necessary artifacts in AWS IoT Core and Timestream for creating a topic rule and a sample application for publishing a data to the topic. 

1.  Clone the GitHub repository for the [sample application](https://github.com/awslabs/amazon-timestream-tools/blob/master/integrations/iot_core) for AWS IoT Core integration following the instructions from [GitHub](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

1. Follow the instructions in the [README](https://github.com/awslabs/amazon-timestream-tools/blob/master/integrations/iot_core) to use an AWS CloudFormation template to create the necessary artifacts in Amazon Timestream and AWS IoT Core and to publish sample messages to the topic.

## Video tutorial
<a name="video-tutorial"></a>

This [video](https://youtu.be/00Wersoz2Q4) explains how IoT Core works with Timestream.