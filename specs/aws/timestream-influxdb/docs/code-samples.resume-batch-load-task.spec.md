---
id: "@specs/aws/timestream-influxdb/docs/code-samples.resume-batch-load-task"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Resume batch load task"
status: active
depends_on:
  - "@specs/aws/timestream-influxdb/meta"
---

# Resume batch load task

> **source:** AWS Documentation
> **spec:id:** @specs/aws/timestream-influxdb/docs/code-samples.resume-batch-load-task
> **target_lang:** meta — documentation tier. ALL sections preserved.



For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com//timestream/latest/developerguide/timestream-for-influxdb.html).

# Resume batch load task
<a name="code-samples.resume-batch-load-task"></a>

You can use the following code snippets to resume batch load tasks.

------
#### [  Java  ]

```
    public void resumeBatchLoadTask(String taskId) {
            try {
                    amazonTimestreamWrite
                                    .resumeBatchLoadTask(ResumeBatchLoadTaskRequest.builder()
                                                    .taskId(taskId)
                                                    .build());

                    System.out.println("Successfully resumed batch load task.");
            } catch (ValidationException validationException) {
                    System.out.println(validationException.getMessage());
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
	
	response, err := client.ResumeBatchLoadTask(context.TODO(), &timestreamwrite.ResumeBatchLoadTaskInput{
		TaskId: aws.String("{{TaskId}}"),
	})

	if err != nil {
		fmt.Println("Error:")
		fmt.Println(err)
	} else {
		fmt.Println("Resume batch load task is successful")
		fmt.Println(response)
	}
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
TASK_ID = "{{<TaskId>}}"

def resume_batch_load_task(client, task_id):
    try:
        result = client.resume_batch_load_task(TaskId=task_id)
        print("Successfully resumed batch load task: ", result)
    except Exception as err:
        print("Resume batch load task failed:", err)


if __name__ == '__main__':
    session = boto3.Session()

    write_client = session.client('timestream-write', \
        endpoint_url=INGEST_ENDPOINT, region_name=REGION, \
        config=Config(read_timeout=20, max_pool_connections = 5000, retries={'max_attempts': 10}))

    resume_batch_load_task(write_client, TASK_ID)
```

------
#### [  Node.js  ]

The following snippet uses AWS SDK for JavaScript v3. For more information about how to install the client and usage, see [Timestream Write Client - AWS SDK for JavaScript v3](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-timestream-write/index.html).

For API details, see [Class CreateBatchLoadCommand](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-timestream-write/classes/describebatchloadtaskcommand.html) and [CreateBatchLoadTask](https://docs.aws.amazon.com/timestream/latest/developerguide/API_CreateBatchLoadTask.html).

```
import { TimestreamWriteClient, ResumeBatchLoadTaskCommand } from "@aws-sdk/client-timestream-write";
const writeClient = new TimestreamWriteClient({ region: "{{<region>}}", endpoint: "{{<endpoint>}}" });

const params = {
    TaskId: "{{<TaskId>}}"
};

const command = new ResumeBatchLoadTaskCommand(params);

try {
    const data = await writeClient.send(command);
    console.log("Resumed batch load task"); 
} catch (error) {
    console.log("Resume batch load task failed.", error);
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
    public class ResumeBatchLoadTaskExample
    {
        private readonly AmazonTimestreamWriteClient writeClient;

        public ResumeBatchLoadTaskExample(AmazonTimestreamWriteClient writeClient)
        {
            this.writeClient = writeClient;
        }

        public async Task ResumeBatchLoadTask(String taskId)
        {
            try
            {
                var resumeBatchLoadTaskRequest = new ResumeBatchLoadTaskRequest
                {
                    TaskId = taskId
                };
                ResumeBatchLoadTaskResponse response = await writeClient.ResumeBatchLoadTaskAsync(resumeBatchLoadTaskRequest);
                Console.WriteLine("Successfully resumed batch load task.");
            }
            catch (ResourceNotFoundException)
            {
                Console.WriteLine("Batch load task does not exist.");
            }
            catch (Exception e)
            {
                Console.WriteLine("Resume batch load task failed: " + e.ToString());
            }
        }
    }
}
```

------