---
id: "@specs/aws/lambda/docs/with-s3-example"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Tutorial: Use an S3 trigger"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Tutorial: Use an S3 trigger

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/with-s3-example
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Tutorial: Using an Amazon S3 trigger to invoke a Lambda function
<a name="with-s3-example"></a>

In this tutorial, you use the console to create a Lambda function and configure a trigger for an Amazon Simple Storage Service (Amazon S3) bucket. Every time that you add an object to your Amazon S3 bucket, your function runs and outputs the object type to Amazon CloudWatch Logs.

![Data flow between an S3 bucket, a Lambda function, and CloudWatch Logs](http://docs.aws.amazon.com/lambda/latest/dg/images/services-s3-example/s3_tut_config.png)


This tutorial demonstrates how to:

1. Create an Amazon S3 bucket.

1. Create a Lambda function that returns the object type of objects in an Amazon S3 bucket.

1. Configure a Lambda trigger that invokes your function when objects are uploaded to your bucket.

1. Test your function, first with a dummy event, and then using the trigger.

By completing these steps, you’ll learn how to configure a Lambda function to run whenever objects are added to or deleted from an Amazon S3 bucket. You can complete this tutorial using only the AWS Management Console.

## Create an Amazon S3 bucket
<a name="with-s3-example-create-bucket"></a>

![First step: Create the Amazon S3 bucket](http://docs.aws.amazon.com/lambda/latest/dg/images/services-s3-example/s3trigger_tut_steps1.png)


**To create an Amazon S3 bucket**

1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3) and select the **General purpose buckets** page.

1. Select the AWS Region closest to your geographical location. You can change your region using the drop-down list at the top of the screen. Later in the tutorial, you must create your Lambda function in the same Region.  
![Image showing drop down region menu in S3 console](http://docs.aws.amazon.com/lambda/latest/dg/images/console_region_select.png)

1. Choose **Create bucket**.

1. Under **General configuration**, do the following:

   1. For **Bucket type**, ensure **General purpose** is selected.

   1. For **Bucket name**, enter a globally unique name that meets the Amazon S3 [Bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html). Bucket names can contain only lower case letters, numbers, dots (.), and hyphens (-).

1. Leave all other options set to their default values and choose **Create bucket**.

## Upload a test object to your bucket
<a name="with-s3-example-upload-test-object"></a>

![Next step: Upload a test object](http://docs.aws.amazon.com/lambda/latest/dg/images/services-s3-example/s3trigger_tut_steps2.png)


**To upload a test object**

1. Open the [Buckets](https://console.aws.amazon.com/s3/buckets) page of the Amazon S3 console and choose the bucket you created during the previous step.

1. Choose **Upload**.

1. Choose **Add files** and select the object that you want to upload. You can select any file (for example, `HappyFace.jpg`).

1. Choose **Open**, then choose **Upload**.

Later in the tutorial, you’ll test your Lambda function using this object.

## Create a permissions policy
<a name="with-s3-example-create-policy"></a>

![Next step: Create the permissions policy for Lambda](http://docs.aws.amazon.com/lambda/latest/dg/images/services-s3-example/s3trigger_tut_steps3.png)


Create a permissions policy that allows Lambda to get objects from an Amazon S3 bucket and to write to Amazon CloudWatch Logs. 

**To create the policy**

1. Open the [Policies page](https://console.aws.amazon.com/iam/home#/policies) of the IAM console.

1. Choose **Create Policy**.

1. Choose the **JSON** tab, and then paste the following custom policy into the JSON editor.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "logs:PutLogEvents",
                   "logs:CreateLogGroup",
                   "logs:CreateLogStream"
               ],
               "Resource": "arn:aws:logs:*:*:*"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "s3:GetObject"
               ],
               "Resource": "arn:aws:s3:::*/*"
           }
       ]
   }
   ```

------

1. Choose **Next: Tags**.

1. Choose **Next: Review**.

1. Under **Review policy**, for the policy **Name**, enter **s3-trigger-tutorial**.

1. Choose **Create policy**.

## Create an execution role
<a name="with-s3-example-create-role"></a>

![Next step: Create the execution role](http://docs.aws.amazon.com/lambda/latest/dg/images/services-s3-example/s3trigger_tut_steps4.png)


An [execution role](lambda-intro-execution-role.md) is an AWS Identity and Access Management (IAM) role that grants a Lambda function permission to access AWS services and resources. In this step, create an execution role using the permissions policy that you created in the previous step.

**To create an execution role and attach your custom permissions policy**

1. Open the [Roles page](https://console.aws.amazon.com/iam/home#/roles) of the IAM console.

1. Choose **Create role**.

1. For the type of trusted entity, choose **AWS service**, then for the use case, choose **Lambda**.

1. Choose **Next**.

1. In the policy search box, enter **s3-trigger-tutorial**.

1. In the search results, select the policy that you created (`s3-trigger-tutorial`), and then choose **Next**.

1. Under **Role details**, for the **Role name**, enter **lambda-s3-trigger-role**, then choose **Create role**.

## Create the Lambda function
<a name="with-s3-example-create-function"></a>

![Next step: Create the Lambda function](http://docs.aws.amazon.com/lambda/latest/dg/images/services-s3-example/s3trigger_tut_steps5.png)


Create a Lambda function in the console using the Python 3.14 runtime.

**To create the Lambda function**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Make sure you're working in the same AWS Region you created your Amazon S3 bucket in. You can change your Region using the drop-down list at the top of the screen.  
![Image showing drop down region menu in Lambda console](http://docs.aws.amazon.com/lambda/latest/dg/images/console_region_select.png)

1. Choose **Create function**.

1. Choose **Author from scratch**

1. Under **Basic information**, do the following:

   1. For **Function name**, enter `s3-trigger-tutorial`

   1. For **Runtime**, choose **Python 3.14**.

   1. For **Architecture**, choose **x86\_64**.

1. In the **Change default execution role** tab, do the following:

   1. Expand the tab, then choose **Use an existing role**.

   1. Select the `lambda-s3-trigger-role` you created earlier.

1. Choose **Create function**.

## Deploy the function code
<a name="with-s3-example-deploy-code"></a>

![Next step: Deploy the function code](http://docs.aws.amazon.com/lambda/latest/dg/images/services-s3-example/s3trigger_tut_steps6.png)


This tutorial uses the Python 3.14 runtime, but we’ve also provided example code files for other runtimes. You can select the tab in the following box to see the code for the runtime you’re interested in.

The Lambda function retrieves the key name of the uploaded object and the name of the bucket from the `event` parameter it receives from Amazon S3. The function then uses the [get\_object](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/get_object.html) method from the AWS SDK for Python (Boto3) to retrieve the object's metadata, including the content type (MIME type) of the uploaded object.

**To deploy the function code**

1. Choose the **Python** tab in the following box and copy the code.

------
#### [ .NET ]

**SDK for .NET**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-s3-to-lambda) repository. 
Consuming an S3 event with Lambda using .NET.  

   ```
   // Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
   // SPDX-License-Identifier: Apache-2.0
   ﻿using System.Threading.Tasks;
   using Amazon.Lambda.Core;
   using Amazon.S3;
   using System;
   using Amazon.Lambda.S3Events;
   using System.Web;
   
   // Assembly attribute to enable the Lambda function's JSON input to be converted into a .NET class.
   [assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]
   
   namespace S3Integration
   {
       public class Function
       {
           private static AmazonS3Client _s3Client;
           public Function() : this(null)
           {
           }
   
           internal Function(AmazonS3Client s3Client)
           {
               _s3Client = s3Client ?? new AmazonS3Client();
           }
   
           public async Task<string> Handler(S3Event evt, ILambdaContext context)
           {
               try
               {
                   if (evt.Records.Count <= 0)
                   {
                       context.Logger.LogLine("Empty S3 Event received");
                       return string.Empty;
                   }
   
                   var bucket = evt.Records[0].S3.Bucket.Name;
                   var key = HttpUtility.UrlDecode(evt.Records[0].S3.Object.Key);
   
                   context.Logger.LogLine($"Request is for {bucket} and {key}");
   
                   var objectResult = await _s3Client.GetObjectAsync(bucket, key);
   
                   context.Logger.LogLine($"Returning {objectResult.Key}");
   
                   return objectResult.Key;
               }
               catch (Exception e)
               {
                   context.Logger.LogLine($"Error processing request - {e.Message}");
   
                   return string.Empty;
               }
           }
       }
   }
   ```

------
#### [ Go ]

**SDK for Go V2**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-s3-to-lambda) repository. 
Consuming an S3 event with Lambda using Go.  

   ```
   // Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
   // SPDX-License-Identifier: Apache-2.0
   package main
   
   import (
   	"context"
   	"log"
   
   	"github.com/aws/aws-lambda-go/events"
   	"github.com/aws/aws-lambda-go/lambda"
   	"github.com/aws/aws-sdk-go-v2/config"
   	"github.com/aws/aws-sdk-go-v2/service/s3"
   )
   
   func handler(ctx context.Context, s3Event events.S3Event) error {
   	sdkConfig, err := config.LoadDefaultConfig(ctx)
   	if err != nil {
   		log.Printf("failed to load default config: %s", err)
   		return err
   	}
   	s3Client := s3.NewFromConfig(sdkConfig)
   
   	for _, record := range s3Event.Records {
   		bucket := record.S3.Bucket.Name
   		key := record.S3.Object.URLDecodedKey
   		headOutput, err := s3Client.HeadObject(ctx, &s3.HeadObjectInput{
   			Bucket: &bucket,
   			Key:    &key,
   		})
   		if err != nil {
   			log.Printf("error getting head of object %s/%s: %s", bucket, key, err)
   			return err
   		}
   		log.Printf("successfully retrieved %s/%s of type %s", bucket, key, *headOutput.ContentType)
   	}
   
   	return nil
   }
   
   func main() {
   	lambda.Start(handler)
   }
   ```

------
#### [ Java ]

**SDK for Java 2.x**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-s3-to-lambda) repository. 
Consuming an S3 event with Lambda using Java.  

   ```
   // Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
   // SPDX-License-Identifier: Apache-2.0
   package example;
   
   import software.amazon.awssdk.services.s3.model.HeadObjectRequest;
   import software.amazon.awssdk.services.s3.model.HeadObjectResponse;
   import software.amazon.awssdk.services.s3.S3Client;
   
   import com.amazonaws.services.lambda.runtime.Context;
   import com.amazonaws.services.lambda.runtime.RequestHandler;
   import com.amazonaws.services.lambda.runtime.events.S3Event;
   import com.amazonaws.services.lambda.runtime.events.models.s3.S3EventNotification.S3EventNotificationRecord;
   
   import org.slf4j.Logger;
   import org.slf4j.LoggerFactory;
   
   public class Handler implements RequestHandler<S3Event, String> {
       private static final Logger logger = LoggerFactory.getLogger(Handler.class);
       @Override
       public String handleRequest(S3Event s3event, Context context) {
           try {
             S3EventNotificationRecord record = s3event.getRecords().get(0);
             String srcBucket = record.getS3().getBucket().getName();
             String srcKey = record.getS3().getObject().getUrlDecodedKey();
   
             S3Client s3Client = S3Client.builder().build();
             HeadObjectResponse headObject = getHeadObject(s3Client, srcBucket, srcKey);
   
             logger.info("Successfully retrieved " + srcBucket + "/" + srcKey + " of type " + headObject.contentType());
   
             return "Ok";
           } catch (Exception e) {
             throw new RuntimeException(e);
           }
       }
   
       private HeadObjectResponse getHeadObject(S3Client s3Client, String bucket, String key) {
           HeadObjectRequest headObjectRequest = HeadObjectRequest.builder()
                   .bucket(bucket)
                   .key(key)
                   .build();
           return s3Client.headObject(headObjectRequest);
       }
   }
   ```

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-s3-to-lambda) repository. 
Consuming an S3 event with Lambda using JavaScript.  

   ```
   import { S3Client, HeadObjectCommand } from "@aws-sdk/client-s3";
   
   const client = new S3Client();
   
   export const handler = async (event, context) => {
   
       // Get the object from the event and show its content type
       const bucket = event.Records[0].s3.bucket.name;
       const key = decodeURIComponent(event.Records[0].s3.object.key.replace(/\+/g, ' '));
   
       try {
           const { ContentType } = await client.send(new HeadObjectCommand({
               Bucket: bucket,
               Key: key,
           }));
   
           console.log('CONTENT TYPE:', ContentType);
           return ContentType;
   
       } catch (err) {
           console.log(err);
           const message = `Error getting object ${key} from bucket ${bucket}. Make sure they exist and your bucket is in the same region as this function.`;
           console.log(message);
           throw new Error(message);
       }
   };
   ```
Consuming an S3 event with Lambda using TypeScript.  

   ```
   // Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
   // SPDX-License-Identifier: Apache-2.0
   import { S3Event } from 'aws-lambda';
   import { S3Client, HeadObjectCommand } from '@aws-sdk/client-s3';
   
   const s3 = new S3Client({ region: process.env.AWS_REGION });
   
   export const handler = async (event: S3Event): Promise<string | undefined> => {
     // Get the object from the event and show its content type
     const bucket = event.Records[0].s3.bucket.name;
     const key = decodeURIComponent(event.Records[0].s3.object.key.replace(/\+/g, ' '));
     const params = {
       Bucket: bucket,
       Key: key,
     };
     try {
       const { ContentType } = await s3.send(new HeadObjectCommand(params));
       console.log('CONTENT TYPE:', ContentType);
       return ContentType;
     } catch (err) {
       console.log(err);
       const message = `Error getting object ${key} from bucket ${bucket}. Make sure they exist and your bucket is in the same region as this function.`;
       console.log(message);
       throw new Error(message);
     }
   };
   ```

------
#### [ PHP ]

**SDK for PHP**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-s3-to-lambda) repository. 
Consuming an S3 event with Lambda using PHP.  

   ```
   <?php
   
   use Bref\Context\Context;
   use Bref\Event\S3\S3Event;
   use Bref\Event\S3\S3Handler;
   use Bref\Logger\StderrLogger;
   
   require __DIR__ . '/vendor/autoload.php';
   
   
   class Handler extends S3Handler 
   {
       private StderrLogger $logger;
       public function __construct(StderrLogger $logger)
       {
           $this->logger = $logger;
       }
       
       public function handleS3(S3Event $event, Context $context) : void
       {
           $this->logger->info("Processing S3 records");
   
           // Get the object from the event and show its content type
           $records = $event->getRecords();
           
           foreach ($records as $record) 
           {
               $bucket = $record->getBucket()->getName();
               $key = urldecode($record->getObject()->getKey());
   
               try {
                   $fileSize = urldecode($record->getObject()->getSize());
                   echo "File Size: " . $fileSize . "\n";
                   // TODO: Implement your custom processing logic here
               } catch (Exception $e) {
                   echo $e->getMessage() . "\n";
                   echo 'Error getting object ' . $key . ' from bucket ' . $bucket . '. Make sure they exist and your bucket is in the same region as this function.' . "\n";
                   throw $e;
               }
           }
       }
   }
   
   $logger = new StderrLogger();
   return new Handler($logger);
   ```

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-s3-to-lambda) repository. 
Consuming an S3 event with Lambda using Python.  

   ```
   # Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
   # SPDX-License-Identifier: Apache-2.0
   import json
   import urllib.parse
   import boto3
   
   print('Loading function')
   
   s3 = boto3.client('s3')
   
   
   def lambda_handler(event, context):
       #print("Received event: " + json.dumps(event, indent=2))
   
       # Get the object from the event and show its content type
       bucket = event['Records'][0]['s3']['bucket']['name']
       key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
       try:
           response = s3.get_object(Bucket=bucket, Key=key)
           print("CONTENT TYPE: " + response['ContentType'])
           return response['ContentType']
       except Exception as e:
           print(e)
           print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
           raise e
   ```

------
#### [ Ruby ]

**SDK for Ruby**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-s3-to-lambda) repository. 
Consuming an S3 event with Lambda using Ruby.  

   ```
   require 'json'
   require 'uri'
   require 'aws-sdk'
   
   puts 'Loading function'
   
   def lambda_handler(event:, context:)
     s3 = Aws::S3::Client.new(region: 'region') # Your AWS region
     # puts "Received event: #{JSON.dump(event)}"
   
     # Get the object from the event and show its content type
     bucket = event['Records'][0]['s3']['bucket']['name']
     key = URI.decode_www_form_component(event['Records'][0]['s3']['object']['key'], Encoding::UTF_8)
     begin
       response = s3.get_object(bucket: bucket, key: key)
       puts "CONTENT TYPE: #{response.content_type}"
       return response.content_type
     rescue StandardError => e
       puts e.message
       puts "Error getting object #{key} from bucket #{bucket}. Make sure they exist and your bucket is in the same region as this function."
       raise e
     end
   end
   ```

------
#### [ Rust ]

**SDK for Rust**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [Serverless examples](https://github.com/aws-samples/serverless-snippets/tree/main/integration-s3-to-lambda) repository. 
Consuming an S3 event with Lambda using Rust.  

   ```
   // Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
   // SPDX-License-Identifier: Apache-2.0
   use aws_lambda_events::event::s3::S3Event;
   use aws_sdk_s3::{Client};
   use lambda_runtime::{run, service_fn, Error, LambdaEvent};
   
   
   /// Main function
   #[tokio::main]
   async fn main() -> Result<(), Error> {
       tracing_subscriber::fmt()
           .with_max_level(tracing::Level::INFO)
           .with_target(false)
           .without_time()
           .init();
   
       // Initialize the AWS SDK for Rust
       let config = aws_config::load_from_env().await;
       let s3_client = Client::new(&config);
   
       let res = run(service_fn(|request: LambdaEvent<S3Event>| {
           function_handler(&s3_client, request)
       })).await;
   
       res
   }
   
   async fn function_handler(
       s3_client: &Client,
       evt: LambdaEvent<S3Event>
   ) -> Result<(), Error> {
       tracing::info!(records = ?evt.payload.records.len(), "Received request from SQS");
   
       if evt.payload.records.len() == 0 {
           tracing::info!("Empty S3 event received");
       }
   
       let bucket = evt.payload.records[0].s3.bucket.name.as_ref().expect("Bucket name to exist");
       let key = evt.payload.records[0].s3.object.key.as_ref().expect("Object key to exist");
   
       tracing::info!("Request is for {} and object {}", bucket, key);
   
       let s3_get_object_result = s3_client
           .get_object()
           .bucket(bucket)
           .key(key)
           .send()
           .await;
   
       match s3_get_object_result {
           Ok(_) => tracing::info!("S3 Get Object success, the s3GetObjectResult contains a 'body' property of type ByteStream"),
           Err(_) => tracing::info!("Failure with S3 Get Object request")
       }
   
       Ok(())
   }
   ```

------

1. In the **Code source** pane on the Lambda console, paste the code into the code editor, replacing the code that Lambda created.

1. In the **DEPLOY** section, choose **Deploy** to update your function's code:  
![Deploy button in the Lambda console code editor](http://docs.aws.amazon.com/lambda/latest/dg/images/getting-started-tutorial/deploy-console.png)

## Create the Amazon S3 trigger
<a name="with-s3-example-create-trigger"></a>

![Next step: Create the S3 trigger](http://docs.aws.amazon.com/lambda/latest/dg/images/services-s3-example/s3trigger_tut_steps7.png)


**To create the Amazon S3 trigger**

1. In the **Function overview** pane, choose **Add trigger**.  
![Lambda console Function overview section.](http://docs.aws.amazon.com/lambda/latest/dg/images/overview-trigger.png)

1. Select **S3**.

1. Under **Bucket**, select the bucket you created earlier in the tutorial.

1. Under **Event types**, be sure that **All object create events** is selected.

1. Under **Recursive invocation**, select the check box to acknowledge that using the same Amazon S3 bucket for input and output is not recommended.

1. Choose **Add**.

**Note**  
When you create an Amazon S3 trigger for a Lambda function using the Lambda console, Amazon S3 configures an [event notification](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html) on the bucket you specify. Before configuring this event notification, Amazon S3 performs a series of checks to confirm that the event destination exists and has the required IAM policies. Amazon S3 also performs these tests on any other event notifications configured for that bucket.  
Because of this check, if the bucket has previously configured event destinations for resources that no longer exist, or for resources that don't have the required permissions policies, Amazon S3 won't be able to create the new event notification. You'll see the following error message indicating that your trigger couldn't be created:  

```
An error occurred when creating the trigger: Unable to validate the following destination configurations.
```
You can see this error if you previously configured a trigger for another Lambda function using the same bucket, and you have since deleted the function or modified its permissions policies.

## Test your Lambda function with a dummy event
<a name="with-s3-example-test-dummy-event"></a>

![Tutorial workflow diagram showing you are in the testing step testing with a dummy event](http://docs.aws.amazon.com/lambda/latest/dg/images/services-s3-example/s3trigger_tut_steps8.png)


**To test the Lambda function with a dummy event**

1. In the Lambda console page for your function, choose the **Test** tab.  
![Lambda console Test tab.](http://docs.aws.amazon.com/lambda/latest/dg/images/test-tab.png)

1. For **Event name**, enter `MyTestEvent`.

1. In the **Event JSON**, paste the following test event. Be sure to replace these values:
   + Replace `us-east-1` with the region you created your Amazon S3 bucket in.
   + Replace both instances of `amzn-s3-demo-bucket` with the name of your own Amazon S3 bucket.
   + Replace `test%2FKey` with the name of the test object you uploaded to your bucket earlier (for example, `HappyFace.jpg`).

   ```
   {
     "Records": [
       {
         "eventVersion": "2.0",
         "eventSource": "aws:s3",
         "awsRegion": "{{us-east-1}}",
         "eventTime": "1970-01-01T00:00:00.000Z",
         "eventName": "ObjectCreated:Put",
         "userIdentity": {
           "principalId": "EXAMPLE"
         },
         "requestParameters": {
           "sourceIPAddress": "127.0.0.1"
         },
         "responseElements": {
           "x-amz-request-id": "EXAMPLE123456789",
           "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
         },
         "s3": {
           "s3SchemaVersion": "1.0",
           "configurationId": "testConfigRule",
           "bucket": {
             "name": "{{amzn-s3-demo-bucket}}",
             "ownerIdentity": {
               "principalId": "EXAMPLE"
             },
             "arn": "arn:aws:s3:::{{amzn-s3-demo-bucket}}"
           },
           "object": {
             "key": "{{test%2Fkey}}",
             "size": 1024,
             "eTag": "0123456789abcdef0123456789abcdef",
             "sequencer": "0A1B2C3D4E5F678901"
           }
         }
       }
     ]
   }
   ```

1. Choose **Save**.

1. Choose **Test**.

1. If your function runs successfully, you’ll see output similar to the following in the **Execution results** tab.

   ```
   Response
   "image/jpeg"
   
   Function Logs
   START RequestId: 12b3cae7-5f4e-415e-93e6-416b8f8b66e6 Version: $LATEST
   2021-02-18T21:40:59.280Z    12b3cae7-5f4e-415e-93e6-416b8f8b66e6    INFO    INPUT BUCKET AND KEY:  { Bucket: 'amzn-s3-demo-bucket', Key: 'HappyFace.jpg' }
   2021-02-18T21:41:00.215Z    12b3cae7-5f4e-415e-93e6-416b8f8b66e6    INFO    CONTENT TYPE: image/jpeg
   END RequestId: 12b3cae7-5f4e-415e-93e6-416b8f8b66e6
   REPORT RequestId: 12b3cae7-5f4e-415e-93e6-416b8f8b66e6    Duration: 976.25 ms    Billed Duration: 977 ms    Memory Size: 128 MB    Max Memory Used: 90 MB    Init Duration: 430.47 ms        
   
   Request ID
   12b3cae7-5f4e-415e-93e6-416b8f8b66e6
   ```

### Test the Lambda function with the Amazon S3 trigger
<a name="with-s3-example-test-s3-trigger"></a>

![Tutorial workflow diagram showing you are in the testing step testing using the S3 trigger](http://docs.aws.amazon.com/lambda/latest/dg/images/services-s3-example/s3trigger_tut_steps9.png)


To test your function with the configured trigger, upload an object to your Amazon S3 bucket using the console. To verify that your Lambda function ran as expected, use CloudWatch Logs to view your function’s output.

**To upload an object to your Amazon S3 bucket**

1. Open the [Buckets](https://console.aws.amazon.com/s3/buckets) page of the Amazon S3 console and choose the bucket that you created earlier.

1. Choose **Upload**.

1. Choose **Add files** and use the file selector to choose an object you want to upload. This object can be any file you choose.

1. Choose **Open**, then choose **Upload**.

**To verify the function invocation using CloudWatch Logs**

1. Open the [CloudWatch](https://console.aws.amazon.com/cloudwatch/home) console.

1. Make sure you're working in the same AWS Region you created your Lambda function in. You can change your Region using the drop-down list at the top of the screen.  
![Image showing drop down region menu in Lambda console](http://docs.aws.amazon.com/lambda/latest/dg/images/console_region_select.png)

1. Choose **Logs**, then choose **Log groups**.

1. Choose the log group for your function (`/aws/lambda/s3-trigger-tutorial`).

1. Under **Log streams**, choose the most recent log stream.

1. If your function was invoked correctly in response to your Amazon S3 trigger, you’ll see output similar to the following. The `CONTENT TYPE` you see depends on the type of file you uploaded to your bucket.

   ```
   2022-05-09T23:17:28.702Z	0cae7f5a-b0af-4c73-8563-a3430333cc10	INFO	CONTENT TYPE: {{image/jpeg}}
   ```

## Clean up your resources
<a name="cleanup"></a>

You can now delete the resources that you created for this tutorial, unless you want to retain them. By deleting AWS resources that you're no longer using, you prevent unnecessary charges to your AWS account.

**To delete the Lambda function**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Select the function that you created.

1. Choose **Actions**, **Delete**.

1. Type **confirm** in the text input field and choose **Delete**.

**To delete the execution role**

1. Open the [Roles page](https://console.aws.amazon.com/iam/home#/roles) of the IAM console.

1. Select the execution role that you created.

1. Choose **Delete**.

1. Enter the name of the role in the text input field and choose **Delete**.

**To delete the S3 bucket**

1. Open the [Amazon S3 console.](https://console.aws.amazon.com//s3/home#)

1. Select the bucket you created.

1. Choose **Delete**.

1. Enter the name of the bucket in the text input field.

1. Choose **Delete bucket**.

## Next steps
<a name="next-steps"></a>

In [Tutorial: Using an Amazon S3 trigger to create thumbnail images](with-s3-tutorial.md), the Amazon S3 trigger invokes a function that creates a thumbnail image for each image file that is uploaded to a bucket. This tutorial requires a moderate level of AWS and Lambda domain knowledge. It demonstrates how to create resources using the AWS Command Line Interface (AWS CLI) and how to create a .zip file archive deployment package for the function and its dependencies.