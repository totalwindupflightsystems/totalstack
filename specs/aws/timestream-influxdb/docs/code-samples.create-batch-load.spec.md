---
id: "@specs/aws/timestream-influxdb/docs/code-samples.create-batch-load"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create batch load task"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Create batch load task

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/code-samples.create-batch-load
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Create batch load task
<a name="code-samples.create-batch-load"></a>

You can use the following code snippets to create batch load tasks.

------
#### [  Java  ]

```
package com.example.tryit;

import java.util.Arrays;

import software.amazon.awssdk.services.timestreamwrite.model.CreateBatchLoadTaskRequest;
import software.amazon.awssdk.services.timestreamwrite.model.CreateBatchLoadTaskResponse;
import software.amazon.awssdk.services.timestreamwrite.model.DataModel;
import software.amazon.awssdk.services.timestreamwrite.model.DataModelConfiguration;
import software.amazon.awssdk.services.timestreamwrite.model.DataSourceConfiguration;
import software.amazon.awssdk.services.timestreamwrite.model.DataSourceS3Configuration;
import software.amazon.awssdk.services.timestreamwrite.model.DimensionMapping;
import software.amazon.awssdk.services.timestreamwrite.model.MultiMeasureAttributeMapping;
import software.amazon.awssdk.services.timestreamwrite.model.MultiMeasureMappings;
import software.amazon.awssdk.services.timestreamwrite.model.ReportConfiguration;
import software.amazon.awssdk.services.timestreamwrite.model.ReportS3Configuration;
import software.amazon.awssdk.services.timestreamwrite.model.ScalarMeasureValueType;
import software.amazon.awssdk.services.timestreamwrite.model.TimeUnit;
import software.amazon.awssdk.services.timestreamwrite.TimestreamWriteClient;

public class BatchLoadExample {
    public static final String DATABASE_NAME = {{<database name>}};
    public static final String TABLE_NAME = {{<table name>}};
    public static final String INPUT_BUCKET = {{<S3 location>}};
    public static final String INPUT_OBJECT_KEY_PREFIX = {{<CSV filename>}};
    public static final String REPORT_BUCKET = {{<S3 location>}};
    public static final long HT_TTL_HOURS = 24L;
    public static final long CT_TTL_DAYS = 7L;

    TimestreamWriteClient amazonTimestreamWrite;

    public BatchLoadExample(TimestreamWriteClient client) {
        this.amazonTimestreamWrite = client;
    }

    public String createBatchLoadTask() {
        System.out.println("Creating batch load task");

        CreateBatchLoadTaskRequest request = CreateBatchLoadTaskRequest.builder()
                .dataModelConfiguration(DataModelConfiguration.builder()
                        .dataModel(DataModel.builder()
                                .timeColumn("timestamp")
                                .timeUnit(TimeUnit.SECONDS)
                                .dimensionMappings(Arrays.asList(
                                        DimensionMapping.builder()
                                                .sourceColumn("vehicle")
                                                .build(),
                                        DimensionMapping.builder()
                                                .sourceColumn("registration")
                                                .destinationColumn("license")
                                                .build()))
                                .multiMeasureMappings(MultiMeasureMappings.builder()
                                        .targetMultiMeasureName("mva_measure_name")
                                        .multiMeasureAttributeMappings(Arrays.asList(
                                                MultiMeasureAttributeMapping.builder()
                                                        .sourceColumn("wgt")
                                                        .targetMultiMeasureAttributeName("weight")
                                                        .measureValueType(ScalarMeasureValueType.DOUBLE)
                                                        .build(),
                                                MultiMeasureAttributeMapping.builder()
                                                        .sourceColumn("spd")
                                                        .targetMultiMeasureAttributeName("speed")
                                                        .measureValueType(ScalarMeasureValueType.DOUBLE)
                                                        .build(),
                                                MultiMeasureAttributeMapping.builder()
                                                        .sourceColumn("fuel")
                                                        .measureValueType(ScalarMeasureValueType.DOUBLE)
                                                        .build(),
                                                MultiMeasureAttributeMapping.builder()
                                                        .sourceColumn("miles")
                                                        .measureValueType(ScalarMeasureValueType.DOUBLE)
                                                        .build()))
                                        .build())
                                .build())
                        .build())
                .dataSourceConfiguration(DataSourceConfiguration.builder()
                        .dataSourceS3Configuration(
                                DataSourceS3Configuration.builder()
                                        .bucketName(INPUT_BUCKET)
                                        .objectKeyPrefix(INPUT_OBJECT_KEY_PREFIX)
                                        .build())
                        .dataFormat("CSV")                
                        .build())
                .reportConfiguration(ReportConfiguration.builder()
                        .reportS3Configuration(ReportS3Configuration.builder()
                                .bucketName(REPORT_BUCKET)
                                .build())
                        .build())
                .targetDatabaseName(DATABASE_NAME)
                .targetTableName(TABLE_NAME)
                .build();
        try {
            final CreateBatchLoadTaskResponse createBatchLoadTaskResponse = amazonTimestreamWrite.createBatchLoadTask(request);
            String taskId = createBatchLoadTaskResponse.taskId();
            System.out.println("Successfully created batch load task: " + taskId);
            return taskId;
        } catch (Exception e) {
            System.out.println("Failed to create batch load task: " + e);
            throw e;
        }
    }
}
```

------
#### [  Go  ]

```
package main

import (
	"fmt"
	"context"
	"log"
	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/timestreamwrite"
	"github.com/aws/aws-sdk-go-v2/service/timestreamwrite/types"
)

func main() {
	customResolver := aws.EndpointResolverWithOptionsFunc(func(service, region string, options ...interface{})(aws.Endpoint, error) {
		if service == timestreamwrite.ServiceID &&  region == "us-west-2" {
		    return aws.Endpoint{
		        PartitionID:   "aws",
		        URL:           <URL>,
		        SigningRegion: "us-west-2",
		    }, nil
		}
		return aws.Endpoint{}, &  aws.EndpointNotFoundError{}
	})

	cfg, err := config.LoadDefaultConfig(context.TODO(), config.WithEndpointResolverWithOptions(customResolver), config.WithRegion("us-west-2"))

	if err != nil {
  		log.Fatalf("failed to load configuration, %v", err)
	}

	client := timestreamwrite.NewFromConfig(cfg)

	response, err := client.CreateBatchLoadTask(context.TODO(), &  timestreamwrite.CreateBatchLoadTaskInput{
            TargetDatabaseName: aws.String("BatchLoadExampleDatabase"),
            TargetTableName: aws.String("BatchLoadExampleTable"),
          		RecordVersion: aws.Int64(1),
          		DataModelConfiguration: &  types.DataModelConfiguration{
                DataModel: &  types.DataModel{
                    TimeColumn: aws.String("timestamp"),
                    TimeUnit: types.TimeUnitMilliseconds,
                    DimensionMappings: []types.DimensionMapping{
                        {
                            SourceColumn: aws.String("registration"),
                            DestinationColumn: aws.String("license"),
                        },
                    },
                    MultiMeasureMappings: &  types.MultiMeasureMappings{
                        TargetMultiMeasureName: aws.String("mva_measure_name"),
                        MultiMeasureAttributeMappings: []types.MultiMeasureAttributeMapping{
                            {
                                SourceColumn: aws.String("wgt"),
                                TargetMultiMeasureAttributeName: aws.String("weight"),
                                MeasureValueType: types.ScalarMeasureValueTypeDouble,
                            },
                            {
                                SourceColumn: aws.String("spd"),
                                TargetMultiMeasureAttributeName: aws.String("speed"),
                                MeasureValueType: types.ScalarMeasureValueTypeDouble,
                            },
                            {
                                SourceColumn: aws.String("fuel_consumption"),
                                TargetMultiMeasureAttributeName: aws.String("fuel"),
                                MeasureValueType: types.ScalarMeasureValueTypeDouble,
                            },
                        },
                    },
                },
            },
          	DataSourceConfiguration: &  types.DataSourceConfiguration{
                DataSourceS3Configuration: &  types.DataSourceS3Configuration{
                    BucketName: aws.String("test-batch-load-west-2"),
                    ObjectKeyPrefix: aws.String("sample.csv"),
                },
               	DataFormat: types.BatchLoadDataFormatCsv,
            },
          	ReportConfiguration: & types.ReportConfiguration{
                ReportS3Configuration: & types.ReportS3Configuration{
                    BucketName: aws.String("test-batch-load-report-west-2"),
                    EncryptionOption: types.S3EncryptionOptionSseS3,
                },
            },
	})

	fmt.Println(aws.ToString(response.TaskId))
}
```

------
#### [  Python  ]

```
import boto3
from botocore.config import Config

INGEST_ENDPOINT = "{{<URL>}}"
REGION = "us-west-2"
HT_TTL_HOURS = 24
CT_TTL_DAYS = 7
DATABASE_NAME = "{{<database name>}}"
TABLE_NAME = "{{<table name>}}"
INPUT_BUCKET_NAME = "{{<S3 location>}}"
INPUT_OBJECT_KEY_PREFIX = "{{<CSV file name>}}"
REPORT_BUCKET_NAME = "{{<S3 location>}}"


def create_batch_load_task(client, database_name, table_name, input_bucket_name, input_object_key_prefix, report_bucket_name):
    try:
        result = client.create_batch_load_task(TargetDatabaseName=database_name, TargetTableName=table_name,
                                               DataModelConfiguration={"DataModel": {
                                                   "TimeColumn": "timestamp",
                                                   "TimeUnit": "SECONDS",
                                                   "DimensionMappings": [
                                                       {
                                                           "SourceColumn": "vehicle"
                                                       },
                                                       {
                                                           "SourceColumn": "registration",
                                                           "DestinationColumn": "license"
                                                       }
                                                   ],
                                                   "MultiMeasureMappings": {
                                                       "TargetMultiMeasureName": "metrics",
                                                       "MultiMeasureAttributeMappings": [
                                                           {
                                                               "SourceColumn": "wgt",
                                                               "MeasureValueType": "DOUBLE"
                                                           },
                                                           {
                                                               "SourceColumn": "spd",
                                                               "MeasureValueType": "DOUBLE"
                                                           },
                                                           {
                                                               "SourceColumn": "fuel_consumption",
                                                               "TargetMultiMeasureAttributeName": "fuel",
                                                               "MeasureValueType": "DOUBLE"
                                                           },
                                                           {
                                                               "SourceColumn": "miles",
                                                               "MeasureValueType": "DOUBLE"
                                                           }
                                                       ]}
                                               }
                                               },
                                               DataSourceConfiguration={
                                                   "DataSourceS3Configuration": {
                                                       "BucketName": input_bucket_name,
                                                       "ObjectKeyPrefix": input_object_key_prefix
                                                   },
                                                   "DataFormat": "CSV"
                                               },
                                               ReportConfiguration={
                                                   "ReportS3Configuration": {
                                                       "BucketName":  report_bucket_name,
                                                       "EncryptionOption": "SSE_S3"
                                                   }
                                               }
                                               )

        task_id = result["TaskId"]
        print("Successfully created batch load task: ", task_id)
        return task_id
    except Exception as err:
        print("Create batch load task job failed:", err)
        return None


if __name__ == '__main__':
    session = boto3.Session()

    write_client = session.client('timestream-write',
                                  endpoint_url=INGEST_ENDPOINT, region_name=REGION,
                                  config=Config(read_timeout=20, max_pool_connections=5000, retries={'max_attempts': 10}))

    task_id = create_batch_load_task(write_client, DATABASE_NAME, TABLE_NAME,
                                     INPUT_BUCKET_NAME, INPUT_OBJECT_KEY_PREFIX, REPORT_BUCKET_NAME)
```

------
#### [  Node.js  ]

The following snippet uses AWS SDK for JavaScript v3. For more information about how to install the client and usage, see [Timestream Write Client - AWS SDK for JavaScript v3](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-timestream-write/index.html).

For API details, see [Class CreateBatchLoadCommand](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-timestream-write/classes/createbatchloadtaskcommand.html) and [CreateBatchLoadTask](https://docs.aws.amazon.com/timestream/latest/developerguide/API_CreateBatchLoadTask.html).

```
import { TimestreamWriteClient, CreateBatchLoadTaskCommand } from "@aws-sdk/client-timestream-write";
const writeClient = new TimestreamWriteClient({ region: "us-west-2", endpoint: "https://gamma-ingest-cell3.timestream.us-west-2.amazonaws.com" });

const params = {
    TargetDatabaseName: "BatchLoadExampleDatabase",
    TargetTableName: "BatchLoadExampleTable",
	RecordVersion: 1,
	DataModelConfiguration: {
		DataModel: {
			TimeColumn: "timestamp",
            TimeUnit: "MILLISECONDS",
            DimensionMappings: [
                {
                    SourceColumn: "registration",
                    DestinationColumn: "license"
                }
            ],
            MultiMeasureMappings: {
                TargetMultiMeasureName: "mva_measure_name",
                MultiMeasureAttributeMappings: [
                    {
                        SourceColumn: "wgt",
                        TargetMultiMeasureAttributeName: "weight",
                        MeasureValueType: "DOUBLE"
                    },
                    {
                        SourceColumn: "spd",
                        TargetMultiMeasureAttributeName: "speed",
                        MeasureValueType: "DOUBLE"
                    },
                    {
                        SourceColumn: "fuel_consumption",
                        TargetMultiMeasureAttributeName: "fuel",
                        MeasureValueType: "DOUBLE"
                    }
                ]
            }
        }
    },
	DataSourceConfiguration: {
        DataSourceS3Configuration: {
            BucketName: "test-batch-load-west-2",
            ObjectKeyPrefix: "sample.csv"
        },
        DataFormat: "CSV"
    },
    ReportConfiguration: {
        ReportS3Configuration: {
            BucketName: "test-batch-load-report-west-2",
            EncryptionOption: "SSE_S3"
        }
    }
};

const command = new CreateBatchLoadTaskCommand(params);

try {
    const data = await writeClient.send(command);
    console.log(`Created batch load task ` + data.TaskId);
} catch (error) {
	console.log("Error creating table. ", error);
	throw error;
}
```

------
#### [  .NET  ]

```
using System;
using System.IO;
using System.Collections.Generic;
using Amazon.TimestreamWrite;
using Amazon.TimestreamWrite.Model;
using System.Threading.Tasks;

namespace TimestreamDotNetSample
{
    public class CreateBatchLoadTaskExample
    {
        public const string DATABASE_NAME = "<database name>";
        public const string TABLE_NAME = "<table name>";
        public const string INPUT_BUCKET = "<input bucket name>";
        public const string INPUT_OBJECT_KEY_PREFIX = "<CSV file name>";
        public const string REPORT_BUCKET = "<report bucket name>";
        public const long HT_TTL_HOURS = 24L;
        public const long CT_TTL_DAYS = 7L;
        private readonly AmazonTimestreamWriteClient writeClient;

        public CreateBatchLoadTaskExample(AmazonTimestreamWriteClient writeClient)
        {
            this.writeClient = writeClient;
        }

        public async Task CreateBatchLoadTask()
        {
            try
            {
                var createBatchLoadTaskRequest = new CreateBatchLoadTaskRequest
                {
                    DataModelConfiguration = new DataModelConfiguration
                    {
                        DataModel = new DataModel
                        {
                            TimeColumn = "timestamp",
                            TimeUnit = TimeUnit.SECONDS,
                            DimensionMappings = new List<DimensionMapping>()
                            {
                                new()
                                {
                                        SourceColumn = "vehicle"
                                },
                                new()
                                {
                                        SourceColumn = "registration",
                                        DestinationColumn = "license"
                                }
                            },
                            MultiMeasureMappings = new MultiMeasureMappings
                            {
                                TargetMultiMeasureName = "mva_measure_name",
                                MultiMeasureAttributeMappings = new List<MultiMeasureAttributeMapping>()
                                {
                                        new()
                                        {
                                                SourceColumn = "wgt",
                                                TargetMultiMeasureAttributeName = "weight",
                                                MeasureValueType = ScalarMeasureValueType.DOUBLE
                                        },
                                        new()
                                        {
                                                SourceColumn = "spd",
                                                TargetMultiMeasureAttributeName = "speed",
                                                MeasureValueType = ScalarMeasureValueType.DOUBLE
                                        },
                                        new()
                                        {
                                                SourceColumn = "fuel",
                                                TargetMultiMeasureAttributeName = "fuel",
                                                MeasureValueType = ScalarMeasureValueType.DOUBLE
                                        },
                                        new()
                                        {
                                                SourceColumn = "miles",
                                                TargetMultiMeasureAttributeName = "miles",
                                                MeasureValueType = ScalarMeasureValueType.DOUBLE
                                        }
                                }
                            }
                        }
                    },
                    DataSourceConfiguration = new DataSourceConfiguration
                    {
                        DataSourceS3Configuration = new DataSourceS3Configuration
                        {
                            BucketName = INPUT_BUCKET,
                            ObjectKeyPrefix = INPUT_OBJECT_KEY_PREFIX
                        },
                        DataFormat = "CSV"
                    },
                    ReportConfiguration = new ReportConfiguration
                    {
                        ReportS3Configuration = new ReportS3Configuration
                        {
                            BucketName = REPORT_BUCKET
                        }
                    },
                    TargetDatabaseName = DATABASE_NAME,
                    TargetTableName = TABLE_NAME
                };

                CreateBatchLoadTaskResponse response = await writeClient.CreateBatchLoadTaskAsync(createBatchLoadTaskRequest);
                Console.WriteLine($"Task created: " + response.TaskId);
            }
            catch (Exception e)
            {
                Console.WriteLine("Create batch load task failed:" + e.ToString());
            }
        }
    }
}
```

```
using Amazon.TimestreamWrite;
using Amazon.TimestreamWrite.Model;
using Amazon;
using Amazon.TimestreamQuery;
using System.Threading.Tasks;
using System;
using CommandLine;
static class Constants
{

}
namespace TimestreamDotNetSample
{
    class MainClass
    {
        public class Options
        {

        }
        public static void Main(string[] args)
        {
            Parser.Default.ParseArguments<Options>(args)
                .WithParsed<Options>(o => {
                    MainAsync().GetAwaiter().GetResult();
                });
        }

        static async Task MainAsync()
        {
            var writeClientConfig = new AmazonTimestreamWriteConfig
            {
                ServiceURL =  "<service URL>",
                Timeout = TimeSpan.FromSeconds(20),
                MaxErrorRetry = 10
            };
            
            var writeClient = new AmazonTimestreamWriteClient(writeClientConfig);
            var example = new CreateBatchLoadTaskExample(writeClient);
            await example.CreateBatchLoadTask();
        }
    }
}
```

------