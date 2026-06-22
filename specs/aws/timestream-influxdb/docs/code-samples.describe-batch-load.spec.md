---
id: "@specs/aws/timestream-influxdb/docs/code-samples.describe-batch-load"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Describe batch load task"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Describe batch load task

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/code-samples.describe-batch-load
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Describe batch load task
<a name="code-samples.describe-batch-load"></a>

You can use the following code snippets to describe batch load tasks.

------
#### [  Java  ]

```
    public void describeBatchLoadTask(String taskId) {
            final DescribeBatchLoadTaskResponse batchLoadTaskResponse = amazonTimestreamWrite
                            .describeBatchLoadTask(DescribeBatchLoadTaskRequest.builder()
                                            .taskId(taskId)
                                            .build());

            System.out.println("Task id: " + batchLoadTaskResponse.batchLoadTaskDescription().taskId());
            System.out.println("Status: " + batchLoadTaskResponse.batchLoadTaskDescription().taskStatusAsString());
            System.out.println("Records processed: "
                            + batchLoadTaskResponse.batchLoadTaskDescription().progressReport().recordsProcessed());
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
)

func main() {
	customResolver := aws.EndpointResolverWithOptionsFunc(func(service, region string, options ...interface{}) (aws.Endpoint, error) {
		if service == timestreamwrite.ServiceID && region == "us-west-2" {
		    return aws.Endpoint{
		        PartitionID:   "aws",
		        URL:           <URL>,
		        SigningRegion: "us-west-2",
		    }, nil
		}
		return aws.Endpoint{}, &aws.EndpointNotFoundError{}
	})

	cfg, err := config.LoadDefaultConfig(context.TODO(), config.WithEndpointResolverWithOptions(customResolver), config.WithRegion("us-west-2"))
	
	if err != nil {
  		log.Fatalf("failed to load configuration, %v", err)
	}

	client := timestreamwrite.NewFromConfig(cfg)
	
	response, err := client.DescribeBatchLoadTask(context.TODO(), &timestreamwrite.DescribeBatchLoadTaskInput{
		TaskId: aws.String("<TaskId>"),
	})

	fmt.Println(aws.ToString(response.BatchLoadTaskDescription.TaskId))
}
```

------
#### [  Python  ]

```
import boto3
from botocore.config import Config

INGEST_ENDPOINT="{{<url>}}"
REGION="us-west-2"
HT_TTL_HOURS = 24
CT_TTL_DAYS = 7
TASK_ID = "{{<task id>}}"

def describe_batch_load_task(client, task_id):
    try:
        result = client.describe_batch_load_task(TaskId=task_id)
        print("Successfully described batch load task: ", result)
    except Exception as err:
        print("Describe batch load task job failed:", err)


if __name__ == '__main__':
    session = boto3.Session()

    write_client = session.client('timestream-write', \
        endpoint_url=INGEST_ENDPOINT, region_name=REGION, \
        config=Config(read_timeout=20, max_pool_connections = 5000, retries={'max_attempts': 10}))

    describe_batch_load_task(write_client, TASK_ID)
```

------
#### [  Node.js  ]

The following snippet uses AWS SDK for JavaScript v3. For more information about how to install the client and usage, see [Timestream Write Client - AWS SDK for JavaScript v3](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-timestream-write/index.html).

For API details, see [Class DescribeBatchLoadCommand](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-timestream-write/classes/describebatchloadtaskcommand.html) and [DescribeBatchLoadTask](https://docs.aws.amazon.com/timestream/latest/developerguide/API_DescribeBatchLoadTask.html).

```
import { TimestreamWriteClient, DescribeBatchLoadTaskCommand } from "@aws-sdk/client-timestream-write";
const writeClient = new TimestreamWriteClient({ region: "{{<region>}}", endpoint: "{{<endpoint>}}" });

const params = {
    TaskId: "{{<TaskId>}}"
};

const command = new DescribeBatchLoadTaskCommand(params);

try {
    const data = await writeClient.send(command);
    console.log(`Batch load task has id ` + data.BatchLoadTaskDescription.TaskId);
} catch (error) {
    if (error.code === 'ResourceNotFoundException') {
        console.log("Batch load task doesn't exist.");
    } else {
        console.log("Describe batch load task failed.", error);
        throw error;
    }
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
    public class DescribeBatchLoadTaskExample
    {
        private readonly AmazonTimestreamWriteClient writeClient;

        public DescribeBatchLoadTaskExample(AmazonTimestreamWriteClient writeClient)
        {
            this.writeClient = writeClient;
        }

        public async Task DescribeBatchLoadTask(String taskId)
        {
            try
            {
                var describeBatchLoadTaskRequest = new DescribeBatchLoadTaskRequest
                {
                    TaskId = taskId
                };
                DescribeBatchLoadTaskResponse response = await writeClient.DescribeBatchLoadTaskAsync(describeBatchLoadTaskRequest);
                Console.WriteLine($"Task has id:{response.BatchLoadTaskDescription.TaskId}");
            }
            catch (ResourceNotFoundException)
            {
                Console.WriteLine("Batch load task does not exist.");
            }
            catch (Exception e)
            {
                Console.WriteLine("Describe batch load task failed:" + e.ToString());
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
            var example = new DescribeBatchLoadTaskExample(writeClient);
            await example.DescribeBatchLoadTask("<batch load task id>");
        }
    }
}
```

------