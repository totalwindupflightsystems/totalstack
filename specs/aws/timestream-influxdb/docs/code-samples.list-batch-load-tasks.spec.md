---
id: "@specs/aws/timestream-influxdb/docs/code-samples.list-batch-load-tasks"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS List batch load tasks"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# List batch load tasks

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/code-samples.list-batch-load-tasks
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# List batch load tasks
<a name="code-samples.list-batch-load-tasks"></a>

You can use the following code snippets to list batch load tasks.

------
#### [  Java  ]

```
    public void listBatchLoadTasks() {
            final ListBatchLoadTasksResponse listBatchLoadTasksResponse = amazonTimestreamWrite
                            .listBatchLoadTasks(ListBatchLoadTasksRequest.builder()
                                            .maxResults(15)
                                            .build());

            for (BatchLoadTask batchLoadTask : listBatchLoadTasksResponse.batchLoadTasks()) {
                    System.out.println(batchLoadTask.taskId());
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
)

func main() {
	customResolver := aws.EndpointResolverWithOptionsFunc(func(service, region string, options ...interface{}) (aws.Endpoint, error) {
		if service == timestreamwrite.ServiceID && region == "us-west-2" {
		    return aws.Endpoint{
		        PartitionID:   "aws",
		        URL:           {{<URL>}},
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
	listBatchLoadTasksMaxResult := int32(15)
	
	response, err := client.ListBatchLoadTasks(context.TODO(), &timestreamwrite.ListBatchLoadTasksInput{
		MaxResults: &listBatchLoadTasksMaxResult,
	})

	for i, task := range response.BatchLoadTasks {
		fmt.Println(i, aws.ToString(task.TaskId))
	}
}
```

------
#### [  Python  ]

```
import boto3
from botocore.config import Config

INGEST_ENDPOINT = "{{<url>}}"
REGION = "us-west-2"
HT_TTL_HOURS = 24
CT_TTL_DAYS = 7


def print_batch_load_tasks(batch_load_tasks):
    for batch_load_task in batch_load_tasks:
        print(batch_load_task['TaskId'])


def list_batch_load_tasks(client):
    print("\nListing batch load tasks")
    try:
        response = client.list_batch_load_tasks(MaxResults=10)
        print_batch_load_tasks(response['BatchLoadTasks'])
        next_token = response.get('NextToken', None)
        while next_token:
            response = client.list_batch_load_tasks(
                NextToken=next_token, MaxResults=10)
            print_batch_load_tasks(response['BatchLoadTasks'])
            next_token = response.get('NextToken', None)
    except Exception as err:
        print("List batch load tasks failed:", err)
        raise err


if __name__ == '__main__':
    session = boto3.Session()

    write_client = session.client('timestream-write',
                                  endpoint_url=INGEST_ENDPOINT, region_name=REGION,
                                  config=Config(read_timeout=20, max_pool_connections=5000, retries={'max_attempts': 10}))

    list_batch_load_tasks(write_client)
```

------
#### [  Node.js  ]

The following snippet uses AWS SDK for JavaScript v3. For more information about how to install the client and usage, see [Timestream Write Client - AWS SDK for JavaScript v3](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-timestream-write/index.html).

For API details, see [Class DescribeBatchLoadCommand](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-timestream-write/classes/listbatchloadtaskscommand.html) and [DescribeBatchLoadTask](https://docs.aws.amazon.com/timestream/latest/developerguide/API_DescribeBatchLoadTask.html).

```
import { TimestreamWriteClient, ListBatchLoadTasksCommand } from "@aws-sdk/client-timestream-write";
const writeClient = new TimestreamWriteClient({ region: "{{<region>}}", endpoint: "{{<endpoint>}}" });

const params = {
    MaxResults: {{<15>}}
};

const command = new ListBatchLoadTasksCommand(params);

getBatchLoadTasksList(null);

async function getBatchLoadTasksList(nextToken) {
    if (nextToken) {
        params.NextToken = nextToken;
    }

    try {
        const data = await writeClient.send(command);

        data.BatchLoadTasks.forEach(function (task) {
            console.log(task.TaskId);
        });

        if (data.NextToken) {
            return getBatchLoadTasksList(data.NextToken);
        }
    } catch (error) {
        console.log("Error while listing batch load tasks", error);
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
    public class ListBatchLoadTasksExample
    {
        private readonly AmazonTimestreamWriteClient writeClient;

        public ListBatchLoadTasksExample(AmazonTimestreamWriteClient writeClient)
        {
            this.writeClient = writeClient;
        }

        public async Task ListBatchLoadTasks()
        {
            Console.WriteLine("Listing batch load tasks");

            try
            {
                var listBatchLoadTasksRequest = new ListBatchLoadTasksRequest
                {
                    MaxResults = 15
                };

                ListBatchLoadTasksResponse response = await writeClient.ListBatchLoadTasksAsync(listBatchLoadTasksRequest);

                PrintBatchLoadTasks(response.BatchLoadTasks);
                var nextToken = response.NextToken;

                while (nextToken != null)
                {
                    listBatchLoadTasksRequest.NextToken = nextToken;
                    response = await writeClient.ListBatchLoadTasksAsync(listBatchLoadTasksRequest);
                    PrintBatchLoadTasks(response.BatchLoadTasks);
                    nextToken = response.NextToken;
                }
            }
            catch (Exception e)
            {
                Console.WriteLine("List batch load tasks failed:" + e.ToString());
            }
        }

        private void PrintBatchLoadTasks(List<BatchLoadTask> tasks)
        {
            foreach (BatchLoadTask task in tasks)
                Console.WriteLine($"Task:{task.TaskId}");
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
            var example = new ListBatchLoadTasksExample(writeClient);
            await example.ListBatchLoadTasks();
        }
    }
}
```

------