---
id: "@specs/aws/lambda/docs/getting-started"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Create your first function"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Create your first function

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/getting-started
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Create your first Lambda function
<a name="getting-started"></a>

To get started with Lambda, use the Lambda console to create a function. In a few minutes, you can create and deploy a function and test it in the console.

As you carry out the tutorial, you'll learn some fundamental Lambda concepts, like how to pass arguments to your function using the Lambda *event object*. You'll also learn how to return log outputs from your function, and how to view your function's invocation logs in Amazon CloudWatch Logs.

To keep things simple, you create your function using either the Python or Node.js runtime. With these interpreted languages, you can edit function code directly in the console's built-in code editor. With compiled languages like Java and C\#, you must create a deployment package on your local build machine and upload it to Lambda. To learn about deploying functions to Lambda using other runtimes, see the links in the [Additional resources and next steps](#getting-started-more-resources) section.

**Tip**  
To learn how to build **serverless solutions**, check out the [Serverless Developer Guide](https://docs.aws.amazon.com/serverless/latest/devguide/).

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com//accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Create a Lambda function with the console
<a name="getting-started-create-function"></a>

In this example, your function takes a JSON object containing two integer values labeled `"length"` and `"width"`. The function multiplies these values to calculate an area and returns this as a JSON string.

Your function also prints the calculated area, along with the name of its CloudWatch log group. Later in the tutorial, you’ll learn to use [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) to view records of your functions’ invocation.

**To create a Hello world Lambda function with the console**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose **Create function**.

1. Select **Author from scratch**.

1. In the **Basic information** pane, for **Function name**, enter `myLambdaFunction`.

1. For **Runtime**, choose either **Node.js 24** or **Python 3.14**.

1. Leave **architecture** set to **x86\_64**, and then choose **Create function**.

In addition to a simple function that returns the message `Hello from Lambda!`, Lambda also creates an [execution role](lambda-intro-execution-role.md) for your function. An execution role is an AWS Identity and Access Management (IAM) role that grants a Lambda function permission to access AWS services and resources. For your function, the role that Lambda creates grants basic permissions to write to CloudWatch Logs.

Use the console's built-in code editor to replace the Hello world code that Lambda created with your own function code.

------
#### [ Node.js ]

**To modify the code in the console**

1. Choose the **Code** tab.

   In the console's built-in code editor, you should see the function code that Lambda created. If you don't see the **index.mjs** tab in the code editor, select **index.mjs** in the file explorer as shown on the following diagram.  
![Diagram showing the console code editor and the index.mjs file in the file explorer](http://docs.aws.amazon.com/lambda/latest/dg/images/getting-started-tutorial/nodejs_code_editor.png)

1. Paste the following code into the **index.mjs** tab, replacing the code that Lambda created.

   ```
   export const handler = async (event, context) => {
     
     const length = event.length;
     const width = event.width;
     let area = calculateArea(length, width);
     console.log(`The area is ${area}`);
           
     console.log('CloudWatch log group: ', context.logGroupName);
     
     let data = {
       "area": area,
     };
       return JSON.stringify(data);
       
     function calculateArea(length, width) {
       return length * width;
     }
   };
   ```

1. In the **DEPLOY** section, choose **Deploy** to update your function's code:  
![Deploy button in the Lambda console code editor](http://docs.aws.amazon.com/lambda/latest/dg/images/getting-started-tutorial/deploy-console.png)

**Understanding your function code**  
Before you move to the next step, let's take a moment to look at the function code and understand some key Lambda concepts.
+ The Lambda handler:

  Your Lambda function contains a Node.js function named `handler`. A Lambda function in Node.js can contain more than one Node.js function, but the *handler* function is always the entry point to your code. When your function is invoked, Lambda runs this method. 

  When you created your Hello world function using the console, Lambda automatically set the name of the handler method for your function to `handler`. Be sure not to edit the name of this Node.js function. If you do, Lambda won’t be able to run your code when you invoke your function.

  To learn more about the Lambda handler in Node.js, see [Define Lambda function handler in Node.js](nodejs-handler.md).
+ The Lambda event object:

  The function `handler` takes two arguments, `event` and `context`. An *event* in Lambda is a JSON formatted document that contains data for your function to process.

  If your function is invoked by another AWS service, the event object contains information about the event that caused the invocation. For example, if your function is invoked when an object is uploaded to an Amazon Simple Storage Service (Amazon S3) bucket, the event contains the name of the bucket and the object key.

  In this example, you’ll create an event in the console by entering a JSON formatted document with two key-value pairs.
+ The Lambda context object:

  The second argument that your function takes is `context`. Lambda passes the *context object* to your function automatically. The context object contains information about the function invocation and execution environment.

  You can use the context object to output information about your function's invocation for monitoring purposes. In this example, your function uses the `logGroupName` parameter to output the name of its CloudWatch log group.

  To learn more about the Lambda context object in Node.js, see [Using the Lambda context object to retrieve Node.js function information](nodejs-context.md).
+ Logging in Lambda:

  With Node.js, you can use console methods like `console.log` and `console.error` to send information to your function's log. The example code uses `console.log` statements to output the calculated area and the name of the function's CloudWatch Logs group. You can also use any logging library that writes to `stdout` or `stderr`. 

  To learn more, see [Log and monitor Node.js Lambda functions](nodejs-logging.md). To learn about logging in other runtimes, see the 'Building with' pages for the runtimes you're interested in.

------
#### [ Python ]

**To modify the code in the console**

1. Choose the **Code** tab.

   In the console's built-in code editor, you should see the function code that Lambda created. If you don't see the **lambda\_function.py** tab in the code editor, select **lambda\_function.py** in the file explorer as shown on the following diagram.  
![Diagram showing the console code editor and the lambda_function.py file in the file explorer](http://docs.aws.amazon.com/lambda/latest/dg/images/getting-started-tutorial/python_code_editor.png)

1. Paste the following code into the **lambda\_function.py** tab, replacing the code that Lambda created.

   ```
   import json
   import logging
   
   logger = logging.getLogger()
   logger.setLevel(logging.INFO)
   
   def lambda_handler(event, context):
       
       # Get the length and width parameters from the event object. The 
       # runtime converts the event object to a Python dictionary
       length = event['length']
       width = event['width']
       
       area = calculate_area(length, width)
       print(f"The area is {area}")
           
       logger.info(f"CloudWatch logs group: {context.log_group_name}")
       
       # return the calculated area as a JSON string
       data = {"area": area}
       return json.dumps(data)
       
   def calculate_area(length, width):
       return length*width
   ```

1. In the **DEPLOY** section, choose **Deploy** to update your function's code:  
![Deploy button in the Lambda console code editor](http://docs.aws.amazon.com/lambda/latest/dg/images/getting-started-tutorial/deploy-console.png)

**Understanding your function code**  
Before you move to the next step, let's take a moment to look at the function code and understand some key Lambda concepts.
+ The Lambda handler:

  Your Lambda function contains a Python function named `lambda_handler`. A Lambda function in Python can contain more than one Python function, but the *handler* function is always the entry point to your code. When your function is invoked, Lambda runs this method. 

  When you created your Hello world function using the console, Lambda automatically set the name of the handler method for your function to `lambda_handler`. Be sure not to edit the name of this Python function. If you do, Lambda won’t be able to run your code when you invoke your function.

  To learn more about the Lambda handler in Python, see [Define Lambda function handler in Python](python-handler.md).
+ The Lambda event object:

  The function `lambda_handler` takes two arguments, `event` and `context`. An *event* in Lambda is a JSON formatted document that contains data for your function to process.

  If your function is invoked by another AWS service, the event object contains information about the event that caused the invocation. For example, if your function is invoked when an object is uploaded to an Amazon Simple Storage Service (Amazon S3) bucket, the event contains the name of the bucket and the object key.

  In this example, you’ll create an event in the console by entering a JSON formatted document with two key-value pairs.
+ The Lambda context object:

  The second argument that your function takes is `context`. Lambda passes the *context object* to your function automatically. The context object contains information about the function invocation and execution environment.

  You can use the context object to output information about your function's invocation for monitoring purposes. In this example, your function uses the `log_group_name` parameter to output the name of its CloudWatch log group.

  To learn more about the Lambda context object in Python, see [Using the Lambda context object to retrieve Python function information](python-context.md).
+ Logging in Lambda:

  With Python, you can use either a `print` statement or a Python logging library to send information to your function's log. To illustrate the difference in what's captured, the example code uses both methods. In a production application, we recommend that you use a logging library.

  To learn more, see [Log and monitor Python Lambda functions](python-logging.md). To learn about logging in other runtimes, see the 'Building with' pages for the runtimes you're interested in.

------

## Invoke the Lambda function using the console code editor
<a name="get-started-invoke-manually"></a>

To invoke your function using the Lambda console code editor, create a test event to send to your function. The event is a JSON formatted document containing two key-value pairs with the keys `"length"` and `"width"`.

**To create the test event**

1. In the **TEST EVENTS** section of the console code editor, choose **Create test event**.  
![Create test event button in the Lambda console code editor](http://docs.aws.amazon.com/lambda/latest/dg/images/getting-started-tutorial/test-event.png)

1. For **Event Name**, enter **myTestEvent**.

1. In the **Event JSON** section, replace the default JSON with the following:

   ```
   {
     "length": 6,
     "width": 7
   }
   ```

1. Choose **Save**.

**To test your function and view invocation records**

In the **TEST EVENTS** section of the console code editor, choose the run icon next to your test event:

![Run test event button in the Lambda console code editor](http://docs.aws.amazon.com/lambda/latest/dg/images/getting-started-tutorial/run-test-event.png)


When your function finishes running, the response and function logs are displayed in the **OUTPUT** tab. You should see results similar to the following:

------
#### [ Node.js ]

```
Status: Succeeded
Test Event Name: myTestEvent

Response
"{\"area\":42}"

Function Logs
START RequestId: 5c012b0a-18f7-4805-b2f6-40912935034a Version: $LATEST
2024-08-31T23:39:45.313Z	5c012b0a-18f7-4805-b2f6-40912935034a	INFO	The area is 42
2024-08-31T23:39:45.331Z	5c012b0a-18f7-4805-b2f6-40912935034a	INFO	CloudWatch log group:  /aws/lambda/myLambdaFunction
END RequestId: 5c012b0a-18f7-4805-b2f6-40912935034a
REPORT RequestId: 5c012b0a-18f7-4805-b2f6-40912935034a	Duration: 20.67 ms	Billed Duration: 21 ms	Memory Size: 128 MB	Max Memory Used: 66 MB	Init Duration: 163.87 ms

Request ID
5c012b0a-18f7-4805-b2f6-40912935034a
```

------
#### [ Python ]

```
Status: Succeeded
Test Event Name: myTestEvent

Response
"{\"area\": 42}"

Function Logs
START RequestId: 2d0b1579-46fb-4bf7-a6e1-8e08840eae5b Version: $LATEST
The area is 42
[INFO]	2024-08-31T23:43:26.428Z	2d0b1579-46fb-4bf7-a6e1-8e08840eae5b	CloudWatch logs group: /aws/lambda/myLambdaFunction
END RequestId: 2d0b1579-46fb-4bf7-a6e1-8e08840eae5b
REPORT RequestId: 2d0b1579-46fb-4bf7-a6e1-8e08840eae5b	Duration: 1.42 ms	Billed Duration: 2 ms	Memory Size: 128 MB	Max Memory Used: 39 MB	Init Duration: 123.74 ms

Request ID
2d0b1579-46fb-4bf7-a6e1-8e08840eae5b
```

------

When you invoke your function outside of the Lambda console, you must use CloudWatch Logs to view your function's execution results.

**To view your function's invocation records in CloudWatch Logs**

1. Open the [Log groups](https://console.aws.amazon.com/cloudwatch/home#logs:) page of the CloudWatch console.

1. Choose the log group for your function (`/aws/lambda/myLambdaFunction`). This is the log group name that your function printed to the console.

1. Scroll down and choose the **Log stream** for the function invocations you want to look at.  
![List of log streams for a Lambda function.](http://docs.aws.amazon.com/lambda/latest/dg/images/log-stream.png)

   You should see output similar to the following:

------
#### [ Node.js ]

   ```
   INIT_START Runtime Version: nodejs:22.v13    Runtime Version ARN: arn:aws:lambda:us-west-2::runtime:e3aaabf6b92ef8755eaae2f4bfdcb7eb8c4536a5e044900570a42bdba7b869d9
   START RequestId: aba6c0fc-cf99-49d7-a77d-26d805dacd20 Version: $LATEST
   2024-08-23T22:04:15.809Z    5c012b0a-18f7-4805-b2f6-40912935034a  INFO	The area is 42
   2024-08-23T22:04:15.810Z    aba6c0fc-cf99-49d7-a77d-26d805dacd20  INFO  CloudWatch log group:  /aws/lambda/myLambdaFunction
   END RequestId: aba6c0fc-cf99-49d7-a77d-26d805dacd20
   REPORT RequestId: aba6c0fc-cf99-49d7-a77d-26d805dacd20    Duration: 17.77 ms    Billed Duration: 18 ms    Memory Size: 128 MB    Max Memory Used: 67 MB    Init Duration: 178.85 ms
   ```

------
#### [ Python ]

   ```
   INIT_START Runtime Version: python:3.13.v16    Runtime Version ARN: arn:aws:lambda:us-west-2::runtime:ca202755c87b9ec2b58856efb7374b4f7b655a0ea3deb1d5acc9aee9e297b072
   START RequestId: 9d4096ee-acb3-4c25-be10-8a210f0a9d8e Version: $LATEST
   The area is 42
   [INFO]	2024-09-01T00:05:22.464Z	9315ab6b-354a-486e-884a-2fb2972b7d84	CloudWatch logs group: /aws/lambda/myLambdaFunction
   END RequestId: 9d4096ee-acb3-4c25-be10-8a210f0a9d8e 
   REPORT RequestId: 9d4096ee-acb3-4c25-be10-8a210f0a9d8e    Duration: 1.15 ms    Billed Duration: 2 ms    Memory Size: 128 MB    Max Memory Used: 40 MB
   ```

------

## Clean up
<a name="gettingstarted-cleanup"></a>

When you're finished working with the example function, delete it. You can also delete the log group that stores the function's logs, and the [execution role](lambda-intro-execution-role.md) that the console created.

**To delete the Lambda function**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Select the function that you created.

1. Choose **Actions**, **Delete**.

1. Type **confirm** in the text input field and choose **Delete**.

**To delete the log group**

1. Open the [Log groups](https://console.aws.amazon.com/cloudwatch/home#logs:) page of the CloudWatch console.

1. Select the function's log group (`/aws/lambda/myLambdaFunction`).

1. Choose **Actions**, **Delete log group(s)**.

1. In the **Delete log group(s)** dialog box, choose **Delete**.

**To delete the execution role**

1. Open the [Roles page](https://console.aws.amazon.com/iam/home?#/roles) of the AWS Identity and Access Management (IAM) console.

1. Select the function's execution role (for example, `myLambdaFunction-role-{{31exxmpl}}`).

1. Choose **Delete**.

1. In the **Delete role** dialog box, enter the role name, and then choose **Delete**.

## Additional resources and next steps
<a name="getting-started-more-resources"></a>

Now that you’ve created and tested a simple Lambda function using the console, take these next steps:
+ Learn to add dependencies to your function and deploy it using a .zip deployment package. Choose your preferred language from the following links.

------
#### [ Node.js ]

  [Deploy Node.js Lambda functions with .zip file archives](nodejs-package.md)

------
#### [ Typescript ]

  [Deploy transpiled TypeScript code in Lambda with .zip file archives](typescript-package.md)

------
#### [ Python ]

  [Working with .zip file archives for Python Lambda functions](python-package.md)

------
#### [ Ruby ]

  [Deploy Ruby Lambda functions with .zip file archives](ruby-package.md)

------
#### [ Java ]

  [Deploy Java Lambda functions with .zip or JAR file archives](java-package.md)

------
#### [ Go ]

  [Deploy Go Lambda functions with .zip file archives](golang-package.md)

------
#### [ C\# ]

  [Build and deploy C\# Lambda functions with .zip file archives](csharp-package.md)

------
+ To learn how to invoke a Lambda function using another AWS service, see [Tutorial: Using an Amazon S3 trigger to invoke a Lambda function](with-s3-example.md).
+ Choose one of the following tutorials for more complex examples of using Lambda with other AWS services.
  + [Tutorial: Using Lambda with API Gateway](services-apigateway-tutorial.md): Create an Amazon API Gateway REST API that invokes a Lambda function.
  + [Using a Lambda function to access an Amazon RDS database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-lambda-tutorial.html): Use a Lambda function to write data to an Amazon Relational Database Service (Amazon RDS) database through RDS Proxy.
  + [Using an Amazon S3 trigger to create thumbnail images](with-s3-tutorial.md): Use a Lambda function to create a thumbnail every time an image file is uploaded to an Amazon S3 bucket.