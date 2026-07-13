---
id: "@specs/aws/lambda/docs/services-ddb-batchfailurereporting"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Batch item failures"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Batch item failures

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/services-ddb-batchfailurereporting
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Configuring partial batch response with DynamoDB and Lambda
<a name="services-ddb-batchfailurereporting"></a>

When consuming and processing streaming data from an event source, by default Lambda checkpoints to the highest sequence number of a batch only when the batch is a complete success. Lambda treats all other results as a complete failure and retries processing the batch up to the retry limit. To allow for partial successes while processing batches from a stream, turn on `ReportBatchItemFailures`. Allowing partial successes can help to reduce the number of retries on a record, though it doesn’t entirely prevent the possibility of retries in a successful record.

To turn on `ReportBatchItemFailures`, include the enum value **ReportBatchItemFailures** in the [FunctionResponseTypes](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html#lambda-CreateEventSourceMapping-request-FunctionResponseTypes) list. This list indicates which response types are enabled for your function. You can configure this list when you [create](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html) or [update](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateEventSourceMapping.html) an event source mapping.

**Note**  
Even when your function code returns partial batch failure responses, these responses will not be processed by Lambda unless the `ReportBatchItemFailures` feature is explicitly turned on for your event source mapping.

## Report syntax
<a name="streams-batchfailurereporting-syntax"></a>

When configuring reporting on batch item failures, the `StreamsEventResponse` class is returned with a list of batch item failures. You can use a `StreamsEventResponse` object to return the sequence number of the first failed record in the batch. You can also create your own custom class using the correct response syntax. The following JSON structure shows the required response syntax:

```
{ 
  "batchItemFailures": [ 
        {
            "itemIdentifier": "<SequenceNumber>"
        }
    ]
}
```

**Note**  
If the `batchItemFailures` array contains multiple items, Lambda uses the record with the lowest sequence number as the checkpoint. Lambda then retries all records starting from that checkpoint.

## Success and failure conditions
<a name="streams-batchfailurereporting-conditions"></a>

Lambda treats a batch as a complete success if you return any of the following:
+ An empty `batchItemFailure` list
+ A null `batchItemFailure` list
+ An empty `EventResponse`
+ A null `EventResponse`

Lambda treats a batch as a complete failure if you return any of the following:
+ An empty string `itemIdentifier`
+ A null `itemIdentifier`
+ An `itemIdentifier` with a bad key name

Lambda retries failures based on your retry strategy.

## Bisecting a batch
<a name="streams-batchfailurereporting-bisect"></a>

If your invocation fails and `BisectBatchOnFunctionError` is turned on, the batch is bisected regardless of your `ReportBatchItemFailures` setting.

When a partial batch success response is received and both `BisectBatchOnFunctionError` and `ReportBatchItemFailures` are turned on, the batch is bisected at the returned sequence number and Lambda retries only the remaining records.

To simplify the implementation of partial batch response logic, consider using the [Batch Processor utility](https://docs.powertools.aws.dev/lambda/python/latest/utilities/batch/) from Powertools for AWS Lambda, which automatically handles these complexities for you.

Here are some examples of function code that return the list of failed message IDs in the batch:

------
#### [ .NET ]

**SDK for .NET**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-ddb-to-lambda-with-batch-item-handling) repository. 
Reporting DynamoDB batch item failures with Lambda using .NET.  

```
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
using System.Text.Json;
using System.Text;
using Amazon.Lambda.Core;
using Amazon.Lambda.DynamoDBEvents;

// Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace AWSLambda_DDB;

public class Function
{
    public StreamsEventResponse FunctionHandler(DynamoDBEvent dynamoEvent, ILambdaContext context)

    {
        context.Logger.LogInformation($"Beginning to process {dynamoEvent.Records.Count} records...");
        List<StreamsEventResponse.BatchItemFailure> batchItemFailures = new List<StreamsEventResponse.BatchItemFailure>();
        StreamsEventResponse streamsEventResponse = new StreamsEventResponse();

        foreach (var record in dynamoEvent.Records)
        {
            try
            {
                var sequenceNumber = record.Dynamodb.SequenceNumber;
                context.Logger.LogInformation(sequenceNumber);
            }
            catch (Exception ex)
            {
                context.Logger.LogError(ex.Message);
                batchItemFailures.Add(new StreamsEventResponse.BatchItemFailure() { ItemIdentifier = record.Dynamodb.SequenceNumber });
            }
        }

        if (batchItemFailures.Count > 0)
        {
            streamsEventResponse.BatchItemFailures = batchItemFailures;
        }

        context.Logger.LogInformation("Stream processing complete.");
        return streamsEventResponse;
    }
}
```

------
#### [ Go ]

**SDK for Go V2**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-ddb-to-lambda-with-batch-item-handling) repository. 
Reporting DynamoDB batch item failures with Lambda using Go.  

```
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
package main

import (
	"context"
	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
)

type BatchItemFailure struct {
	ItemIdentifier string `json:"ItemIdentifier"`
}

type BatchResult struct {
	BatchItemFailures []BatchItemFailure `json:"BatchItemFailures"`
}

func HandleRequest(ctx context.Context, event events.DynamoDBEvent) (*BatchResult, error) {
	var batchItemFailures []BatchItemFailure
	curRecordSequenceNumber := ""

	for _, record := range event.Records {
		// Process your record
		curRecordSequenceNumber = record.Change.SequenceNumber
	}

	if curRecordSequenceNumber != "" {
		batchItemFailures = append(batchItemFailures, BatchItemFailure{ItemIdentifier: curRecordSequenceNumber})
	}
	
	batchResult := BatchResult{
		BatchItemFailures: batchItemFailures,
	}

	return &batchResult, nil
}

func main() {
	lambda.Start(HandleRequest)
}
```

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-ddb-to-lambda-with-batch-item-handling) repository. 
Reporting DynamoDB batch item failures with Lambda using Java.  

```
// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.DynamodbEvent;
import com.amazonaws.services.lambda.runtime.events.StreamsEventResponse;
import com.amazonaws.services.lambda.runtime.events.models.dynamodb.StreamRecord;

import java.util.ArrayList;
import java.util.List;

public class ProcessDynamodbRecords implements RequestHandler<DynamodbEvent, StreamsEventResponse> {

    @Override
    public StreamsEventResponse handleRequest(DynamodbEvent input, Context context) {

        List<StreamsEventResponse.BatchItemFailure> batchItemFailures = new ArrayList<>();
        String curRecordSequenceNumber = "";

        for (DynamodbEvent.DynamodbStreamRecord dynamodbStreamRecord : input.getRecords()) {
          try {
                //Process your record
                StreamRecord dynamodbRecord = dynamodbStreamRecord.getDynamodb();
                curRecordSequenceNumber = dynamodbRecord.getSequenceNumber();
                
            } catch (Exception e) {
                /* Since we are working with streams, we can return the failed item immediately.
                   Lambda will immediately begin to retry processing from this failed item onwards. */
                batchItemFailures.add(new StreamsEventResponse.BatchItemFailure(curRecordSequenceNumber));
                return new StreamsEventResponse(batchItemFailures);
            }
        }
       
       return new StreamsEventResponse();   
    }
}
```

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-ddb-to-lambda-with-batch-item-handling) repository. 
Reporting DynamoDB batch item failures with Lambda using JavaScript.  

```
export const handler = async (event) => {
  const records = event.Records;
  let curRecordSequenceNumber = "";

  for (const record of records) {
    try {
      // Process your record
      curRecordSequenceNumber = record.dynamodb.SequenceNumber;
    } catch (e) {
      // Return failed record's sequence number
      return { batchItemFailures: [{ itemIdentifier: curRecordSequenceNumber }] };
    }
  }

  return { batchItemFailures: [] };
};
```
Reporting DynamoDB batch item failures with Lambda using TypeScript.  

```
import {
  DynamoDBBatchResponse,
  DynamoDBBatchItemFailure,
  DynamoDBStreamEvent,
} from "aws-lambda";

export const handler = async (
  event: DynamoDBStreamEvent
): Promise<DynamoDBBatchResponse> => {
  const batchItemFailures: DynamoDBBatchItemFailure[] = [];
  let curRecordSequenceNumber;

  for (const record of event.Records) {
    curRecordSequenceNumber = record.dynamodb?.SequenceNumber;

    if (curRecordSequenceNumber) {
      batchItemFailures.push({
        itemIdentifier: curRecordSequenceNumber,
      });
    }
  }

  return { batchItemFailures: batchItemFailures };
};
```

------
#### [ PHP ]

**SDK for PHP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-ddb-to-lambda-with-batch-item-handling) repository. 
Reporting DynamoDB batch item failures with Lambda using PHP.  

```
<?php

# using bref/bref and bref/logger for simplicity

use Bref\Context\Context;
use Bref\Event\DynamoDb\DynamoDbEvent;
use Bref\Event\Handler as StdHandler;
use Bref\Logger\StderrLogger;

require __DIR__ . '/vendor/autoload.php';

class Handler implements StdHandler
{
    private StderrLogger $logger;
    public function __construct(StderrLogger $logger)
    {
        $this->logger = $logger;
    }

    /**
     * @throws JsonException
     * @throws \Bref\Event\InvalidLambdaEvent
     */
    public function handle(mixed $event, Context $context): array
    {
        $dynamoDbEvent = new DynamoDbEvent($event);
        $this->logger->info("Processing records");

        $records = $dynamoDbEvent->getRecords();
        $failedRecords = [];
        foreach ($records as $record) {
            try {
                $data = $record->getData();
                $this->logger->info(json_encode($data));
                // TODO: Do interesting work based on the new data
            } catch (Exception $e) {
                $this->logger->error($e->getMessage());
                // failed processing the record
                $failedRecords[] = $record->getSequenceNumber();
            }
        }
        $totalRecords = count($records);
        $this->logger->info("Successfully processed $totalRecords records");

        // change format for the response
        $failures = array_map(
            fn(string $sequenceNumber) => ['itemIdentifier' => $sequenceNumber],
            $failedRecords
        );

        return [
            'batchItemFailures' => $failures
        ];
    }
}

$logger = new StderrLogger();
return new Handler($logger);
```

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-ddb-to-lambda-with-batch-item-handling) repository. 
Reporting DynamoDB batch item failures with Lambda using Python.  

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
def handler(event, context):
    records = event.get("Records")
    curRecordSequenceNumber = ""
    
    for record in records:
        try:
            # Process your record
            curRecordSequenceNumber = record["dynamodb"]["SequenceNumber"]
        except Exception as e:
            # Return failed record's sequence number
            return {"batchItemFailures":[{"itemIdentifier": curRecordSequenceNumber}]}

    return {"batchItemFailures":[]}
```

------
#### [ Ruby ]

**SDK for Ruby**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-ddb-to-lambda-with-batch-item-handling) repository. 
Reporting DynamoDB batch item failures with Lambda using Ruby.  

```
def lambda_handler(event:, context:)
    records = event["Records"]
    cur_record_sequence_number = ""
  
    records.each do |record|
      begin
        # Process your record
        cur_record_sequence_number = record["dynamodb"]["SequenceNumber"]
      rescue StandardError => e
        # Return failed record's sequence number
        return {"batchItemFailures" => [{"itemIdentifier" => cur_record_sequence_number}]}
      end
    end
  
    {"batchItemFailures" => []}
  end
```

------
#### [ Rust ]

**SDK for Rust**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-ddb-to-lambda-with-batch-item-handling) repository. 
Reporting DynamoDB batch item failures with Lambda using Rust.  

```
use aws_lambda_events::{
    event::dynamodb::{Event, EventRecord, StreamRecord},
    streams::{DynamoDbBatchItemFailure, DynamoDbEventResponse},
};
use lambda_runtime::{run, service_fn, Error, LambdaEvent};

/// Process the stream record
fn process_record(record: &EventRecord) -> Result<(), Error> {
    let stream_record: &StreamRecord = &record.change;

    // process your stream record here...
    tracing::info!("Data: {:?}", stream_record);

    Ok(())
}

/// Main Lambda handler here...
async fn function_handler(event: LambdaEvent<Event>) -> Result<DynamoDbEventResponse, Error> {
    let mut response = DynamoDbEventResponse {
        batch_item_failures: vec![],
    };

    let records = &event.payload.records;

    if records.is_empty() {
        tracing::info!("No records found. Exiting.");
        return Ok(response);
    }

    for record in records {
        tracing::info!("EventId: {}", record.event_id);

        // Couldn't find a sequence number
        if record.change.sequence_number.is_none() {
            response.batch_item_failures.push(DynamoDbBatchItemFailure {
                item_identifier: Some("".to_string()),
            });
            return Ok(response);
        }

        // Process your record here...
        if process_record(record).is_err() {
            response.batch_item_failures.push(DynamoDbBatchItemFailure {
                item_identifier: record.change.sequence_number.clone(),
            });
            /* Since we are working with streams, we can return the failed item immediately.
            Lambda will immediately begin to retry processing from this failed item onwards. */
            return Ok(response);
        }
    }

    tracing::info!("Successfully processed {} record(s)", records.len());

    Ok(response)
}

#[tokio::main]
async fn main() -> Result<(), Error> {
    tracing_subscriber::fmt()
        .with_max_level(tracing::Level::INFO)
        // disable printing the name of the module in every log line.
        .with_target(false)
        // disabling time is handy because CloudWatch will add the ingestion time.
        .without_time()
        .init();

    run(service_fn(function_handler)).await
}
```

------

## Using Powertools for AWS Lambda batch processor
<a name="services-ddb-batchfailurereporting-powertools"></a>

The batch processor utility from Powertools for AWS Lambda automatically handles partial batch response logic, reducing the complexity of implementing batch failure reporting. Here are examples using the batch processor:

**Python**  
For complete examples and setup instructions, see the [batch processor documentation](https://docs.powertools.aws.dev/lambda/python/latest/utilities/batch/).
Processing DynamoDB stream records with AWS Lambda batch processor.  

```
import json
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.batch import BatchProcessor, EventType, process_partial_response
from aws_lambda_powertools.utilities.data_classes import DynamoDBStreamEvent
from aws_lambda_powertools.utilities.typing import LambdaContext

processor = BatchProcessor(event_type=EventType.DynamoDBStreams)
logger = Logger()

def record_handler(record):
    logger.info(record)
    # Your business logic here
    # Raise an exception to mark this record as failed
    
def lambda_handler(event, context: LambdaContext):
    return process_partial_response(
        event=event, 
        record_handler=record_handler, 
        processor=processor,
        context=context
    )
```

**TypeScript**  
For complete examples and setup instructions, see the [batch processor documentation](https://docs.aws.amazon.com/powertools/typescript/latest/features/batch/).
Processing DynamoDB stream records with AWS Lambda batch processor.  

```
import { BatchProcessor, EventType, processPartialResponse } from '@aws-lambda-powertools/batch';
import { Logger } from '@aws-lambda-powertools/logger';
import type { DynamoDBStreamEvent, Context } from 'aws-lambda';

const processor = new BatchProcessor(EventType.DynamoDBStreams);
const logger = new Logger();

const recordHandler = async (record: any): Promise<void> => {
    logger.info('Processing record', { record });
    // Your business logic here
    // Throw an error to mark this record as failed
};

export const handler = async (event: DynamoDBStreamEvent, context: Context) => {
    return processPartialResponse(event, recordHandler, processor, {
        context,
    });
};
```

**Java**  
For complete examples and setup instructions, see the [batch processor documentation](https://docs.powertools.aws.dev/lambda/java/latest/utilities/batch/).
Processing DynamoDB stream records with AWS Lambda batch processor.  

```
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.DynamodbEvent;
import com.amazonaws.services.lambda.runtime.events.StreamsEventResponse;
import software.amazon.lambda.powertools.batch.BatchMessageHandlerBuilder;
import software.amazon.lambda.powertools.batch.handler.BatchMessageHandler;

public class DynamoDBStreamBatchHandler implements RequestHandler<DynamodbEvent, StreamsEventResponse> {

    private final BatchMessageHandler<DynamodbEvent, StreamsEventResponse> handler;

    public DynamoDBStreamBatchHandler() {
        handler = new BatchMessageHandlerBuilder()
                .withDynamoDbBatchHandler()
                .buildWithRawMessageHandler(this::processMessage);
    }

    @Override
    public StreamsEventResponse handleRequest(DynamodbEvent ddbEvent, Context context) {
        return handler.processBatch(ddbEvent, context);
    }

    private void processMessage(DynamodbEvent.DynamodbStreamRecord dynamodbStreamRecord, Context context) {
        // Process the change record
    }
}
```

**.NET**  
For complete examples and setup instructions, see the [batch processor documentation](https://docs.aws.amazon.com/powertools/dotnet/utilities/batch-processing/).
Processing DynamoDB stream records with AWS Lambda batch processor.  

```
using System;
using System.Threading;
using System.Threading.Tasks;
using Amazon.Lambda.Core;
using Amazon.Lambda.DynamoDBEvents;
using Amazon.Lambda.Serialization.SystemTextJson;
using AWS.Lambda.Powertools.BatchProcessing;

[assembly: LambdaSerializer(typeof(DefaultLambdaJsonSerializer))]

namespace HelloWorld;

public class Customer
{
    public string? CustomerId { get; set; }
    public string? Name { get; set; }
    public string? Email { get; set; }
    public DateTime CreatedAt { get; set; }
}

internal class TypedDynamoDbRecordHandler : ITypedRecordHandler<Customer> 
{
    public async Task<RecordHandlerResult> HandleAsync(Customer customer, CancellationToken cancellationToken)
    {
        if (string.IsNullOrEmpty(customer.Email)) 
        {
            throw new ArgumentException("Customer email is required");
        }

        return await Task.FromResult(RecordHandlerResult.None); 
    }
}

public class Function
{
    [BatchProcessor(TypedRecordHandler = typeof(TypedDynamoDbRecordHandler))]
    public BatchItemFailuresResponse HandlerUsingTypedAttribute(DynamoDBEvent _)
    {
        return TypedDynamoDbStreamBatchProcessor.Result.BatchItemFailuresResponse; 
    }
}
```