---
id: "@specs/aws/lambda/docs/python-handler"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Handler"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Handler

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/python-handler
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Define Lambda function handler in Python
<a name="python-handler"></a>

The Lambda function *handler* is the method in your function code that processes events. When your function is invoked, Lambda runs the handler method. Your function runs until the handler returns a response, exits, or times out.

This page describes how to work with Lambda function handlers in Python, including naming conventions, valid handler signatures, and code best practices. This page also includes an example of a Python Lambda function that takes in information about an order, produces a text file receipt, and puts this file in an Amazon Simple Storage Service (Amazon S3) bucket.

**Topics**
+ [Example Python Lambda function code](#python-handler-example)
+ [Handler naming conventions](#python-handler-naming)
+ [Using the Lambda event object](#python-handler-event)
+ [Accessing and using the Lambda context object](#python-handler-context)
+ [Valid handler signatures for Python handlers](#python-handler-signature)
+ [Returning a value](#python-handler-return)
+ [Using the AWS SDK for Python (Boto3) in your handler](#python-handler-sdk)
+ [Accessing environment variables](#python-handler-env-vars)
+ [Code best practices for Python Lambda functions](#python-handler-best-practices)

## Example Python Lambda function code
<a name="python-handler-example"></a>

The following example Python Lambda function code takes in information about an order, produces a text file receipt, and puts this file in an Amazon S3 bucket:

**Example Python Lambda function**  

```
import json
import os
import logging
import boto3

# Initialize the S3 client outside of the handler
s3_client = boto3.client('s3')

# Initialize the logger
logger = logging.getLogger()
logger.setLevel("INFO")

def upload_receipt_to_s3(bucket_name, key, receipt_content):
    """Helper function to upload receipt to S3"""
    
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=key,
            Body=receipt_content
        )
    except Exception as e:
        logger.error(f"Failed to upload receipt to S3: {str(e)}")
        raise

def lambda_handler(event, context):
    """
    Main Lambda handler function
    Parameters:
        event: Dict containing the Lambda function event data
        context: Lambda runtime context
    Returns:
        Dict containing status message
    """
    try:
        # Parse the input event
        order_id = event['Order_id']
        amount = event['Amount']
        item = event['Item']
        
        # Access environment variables
        bucket_name = os.environ.get('RECEIPT_BUCKET')
        if not bucket_name:
            raise ValueError("Missing required environment variable RECEIPT_BUCKET")

        # Create the receipt content and key destination
        receipt_content = (
            f"OrderID: {order_id}\n"
            f"Amount: ${amount}\n"
            f"Item: {item}"
        )
        key = f"receipts/{order_id}.txt"

        # Upload the receipt to S3
        upload_receipt_to_s3(bucket_name, key, receipt_content)

        logger.info(f"Successfully processed order {order_id} and stored receipt in S3 bucket {bucket_name}")
        
        return {
            "statusCode": 200,
            "message": "Receipt processed successfully"
        }

    except Exception as e:
        logger.error(f"Error processing order: {str(e)}")
        raise
```

This file contains the following sections of code:
+ `import` block: Use this block to include libraries that your Lambda function requires.
+ Global initialization of SDK client and logger: Including initialization code outside of the handler takes advantage of [execution environment](lambda-runtime-environment.md) re-use to improve the performance of your function. See [Code best practices for Python Lambda functions](#python-handler-best-practices) to learn more.
+ `def upload_receipt_to_s3(bucket_name, key, receipt_content):` This is a helper function that's called by the main `lambda_handler` function.
+ `def lambda_handler(event, context):` This is the **main handler function** for your code, which contains your main application logic. When Lambda invokes your function handler, the [Lambda runtime](concepts-basics.md#gettingstarted-concepts-runtime) passes two arguments to the function, the [event object](#python-handler-event) that contains data for your function to process and the [context object](#python-handler-context) that contains information about the function invocation.

## Handler naming conventions
<a name="python-handler-naming"></a>

The function handler name defined at the time that you create a Lambda function is derived from:
+ The name of the file in which the Lambda handler function is located.
+ The name of the Python handler function.

In the example above, if the file is named `lambda_function.py`, the handler would be specified as `lambda_function.lambda_handler`. This is the default handler name given to functions you create using the Lambda console.

If you create a function in the console using a different file name or function handler name, you must edit the default handler name.

**To change the function handler name (console)**

1. Open the [Functions](https://console.aws.amazon.com/lambda/home#/functions) page of the Lambda console and choose your function.

1. Choose the **Code** tab.

1. Scroll down to the **Runtime settings** pane and choose **Edit**.

1. In **Handler**, enter the new name for your function handler.

1. Choose **Save**.

## Using the Lambda event object
<a name="python-handler-event"></a>

When Lambda invokes your function, it passes an [event object](concepts-basics.md#gettingstarted-concepts-event) argument to the function handler. JSON objects are the most common event format for Lambda functions. In the code example in the previous section, the function expects an input in the following format:

```
{
    "Order_id": "12345",
    "Amount": 199.99,
    "Item": "Wireless Headphones"
}
```

If your function is invoked by another AWS service, the input event is also a JSON object. The exact format of the event object depends on the service that's invoking your function. To see the event format for a particular service, refer to the appropriate page in the [Invoking Lambda with events from other AWS services](lambda-services.md) chapter.

If the input event is in the form of a JSON object, the Lambda runtime converts the object to a Python dictionary. To assign values in the input JSON to variables in your code, use the standard Python dictionary methods as illustrated in the example code.

You can also pass data into your function as a JSON array, or as any of the other valid JSON data types. The following table defines how the Python runtime converts these JSON types.


| JSON data type | Python data type | 
| --- | --- | 
| object | dictionary (dict) | 
| array | list (list) | 
| number | integer (int) or floating point number (float) | 
| string | string (str) | 
| Boolean | Boolean (bool) | 
| null | NoneType (NoneType) | 

## Accessing and using the Lambda context object
<a name="python-handler-context"></a>

The Lambda context object contains information about the function invocation and execution environment. Lambda passes the context object to your function automatically when it's invoked. You can use the context object to output information about your function's invocation for monitoring purposes.

The context object is a Python class that's defined in the [Lambda runtime interface client](https://github.com/aws/aws-lambda-python-runtime-interface-client/blob/main/awslambdaric/lambda_context.py). To return the value of any of the context object properties, use the corresponding method on the context object. For example, the following code snippet assigns the value of the `aws_request_id` property (the identifier for the invocation request) to a variable named `request`. 

```
request = context.aws_request_id
```

To learn more about using the Lambda context object, and to see a complete list of the available methods and properties, see [Using the Lambda context object to retrieve Python function information](python-context.md).

## Valid handler signatures for Python handlers
<a name="python-handler-signature"></a>

When defining your handler function in Python, the function must take two arguments. The first of these arguments is the Lambda [event object](#python-handler-event) and the second one is the Lambda [context object](#python-handler-context). By convention, these input arguments are usually named `event` and `context`, but you can give them any names you wish. If you declare your handler function with a single input argument, Lambda will raise an error when it attempts to run your function. The most common way to declare a handler function in Python is as follows:

```
def lambda_handler(event, context):
```

You can also use Python type hints in your function declaration, as shown in the following example:

```
from typing import Dict, Any
      
def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
```

To use specific AWS typing for events generated by other AWS services and for the context object, add the `aws-lambda-typing` package to your function's deployment package. You can install this library in your development environment by running `pip install aws-lambda-typing`. The following code snippet shows how to use AWS-specific type hints. In this example, the expected event is an Amazon S3 event.

```
from aws_lambda_typing.events import S3Event
from aws_lambda_typing.context import Context
from typing import Dict, Any

def lambda_handler(event: S3Event, context: Context) -> Dict[str, Any]:
```

You can't use the Python `async` function type for your handler function.

## Returning a value
<a name="python-handler-return"></a>

Optionally, a handler can return a value, which must be JSON serializable. Common return types include `dict`, `list`, `str`, `int`, `float`, and `bool`.

What happens to the returned value depends on the [invocation type](lambda-invocation.md) and the [service](lambda-services.md) that invoked the function. For example:
+ If you use the `RequestResponse` invocation type to [invoke a Lambda function synchronously](invocation-sync.md), Lambda returns the result of the Python function call to the client invoking the Lambda function (in the HTTP response to the invocation request, serialized into JSON). For example, AWS Lambda console uses the `RequestResponse` invocation type, so when you invoke the function on the console, the console will display the returned value.
+ If the handler returns objects that can't be serialized by `json.dumps`, the runtime returns an error.
+ If the handler returns `None`, as Python functions without a `return` statement implicitly do, the runtime returns `null`.
+ If you use the `Event` invocation type (an [asynchronous invocation](invocation-async.md)), the value is discarded.

In the example code, the handler returns the following Python dictionary:

```
{
  "statusCode": 200,
  "message": "Receipt processed successfully"
}
```

The Lambda runtime serializes this dictionary and returns it to the client that invoked the function as a JSON string.

**Note**  
In Python 3.9 and later releases, Lambda includes the requestId of the invocation in the error response.

## Using the AWS SDK for Python (Boto3) in your handler
<a name="python-handler-sdk"></a>

Often, you'll use Lambda functions to interact with other AWS services and resources. The simplest way to interface with these resources is to use the AWS SDK for Python (Boto3). All [supported Lambda Python runtimes](lambda-runtimes.md#runtimes-supported) include a version of the SDK for Python. However, we strongly recommend that you include the SDK in your function's deployment package if your code needs to use it. Including the SDK in your deployment package gives you full control over your dependencies and reduces the risk of version misalignment issues with other libraries. See [Runtime dependencies in Python](python-package.md#python-package-dependencies) and [Backward compatibility](runtimes-update.md#runtime-update-compatibility) to learn more.

To use the SDK for Python in your Lambda function, add the following statement to the import block at the beginning of your function code:

```
import boto3
```

Use the `pip install` command to add the `boto3` library to your function's deployment package. For detailed instructions on how to add dependencies to a .zip deployment package, see [Creating a .zip deployment package with dependencies](python-package.md#python-package-create-dependencies). To learn more about adding dependencies to Lambda functions deployed as container images, see [Creating an image from a base image](python-image.md#python-image-create) or [Creating an image from an alternative base image](python-image.md#python-alt-create).

When using `boto3` in your code, you don't need to provide any credentials to initialize a client. For example, in the example code, we use the following line of code to initialize an Amazon S3 client:

```
# Initialize the S3 client outside of the handler
s3_client = boto3.client('s3')
```

With Python, Lambda automatically creates environment variables with credentials. The `boto3` SDK checks your function's environment variables for these credentials during initialization.

## Accessing environment variables
<a name="python-handler-env-vars"></a>

In your handler code, you can reference [environment variables](configuration-envvars.md) by using the `os.environ.get` method. In the example code, we reference the defined `RECEIPT_BUCKET` environment variable using the following line of code:

```
# Access environment variables
bucket_name = os.environ.get('RECEIPT_BUCKET')
```

Don't forget to include an `import os` statement in the import block at the beginning of your code.

## Code best practices for Python Lambda functions
<a name="python-handler-best-practices"></a>

Adhere to the guidelines in the following list to use best coding practices when building your Lambda functions:
+ **Separate the Lambda handler from your core logic.** This allows you to make a more unit-testable function. For example, in Python, this may look like: 

  ```
  def lambda_handler(event, context):
      foo = event['foo']
      bar = event['bar']      
      result = my_lambda_function(foo, bar)
  
  def my_lambda_function(foo, bar):
      // MyLambdaFunction logic here
  ```
+ **Control the dependencies in your function's deployment package.** The AWS Lambda execution environment contains a number of libraries. For the Node.js and Python runtimes, these include the AWS SDKs. To enable the latest set of features and security updates, Lambda will periodically update these libraries. These updates may introduce subtle changes to the behavior of your Lambda function. To have full control of the dependencies your function uses, package all of your dependencies with your deployment package.
+ **Minimize the complexity of your dependencies.** Prefer simpler frameworks that load quickly on [execution environment](lambda-runtime-environment.md) startup.
+ **Minimize your deployment package size to its runtime necessities. ** This will reduce the amount of time that it takes for your deployment package to be downloaded and unpacked ahead of invocation.

**Take advantage of execution environment reuse to improve the performance of your function.** Initialize SDK clients and database connections outside of the function handler, and cache static assets locally in the `/tmp` directory. Subsequent invocations processed by the same instance of your function can reuse these resources. This saves cost by reducing function run time.

To avoid potential data leaks across invocations, don’t use the execution environment to store user data, events, or other information with security implications. If your function relies on a mutable state that can’t be stored in memory within the handler, consider creating a separate function or separate versions of a function for each user.

**Use a keep-alive directive to maintain persistent connections.** Lambda purges idle connections over time. Attempting to reuse an idle connection when invoking a function will result in a connection error. To maintain your persistent connection, use the keep-alive directive associated with your runtime. For an example, see [Reusing Connections with Keep-Alive in Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/node-reusing-connections.html).

**Use [environment variables](configuration-envvars.md) to pass operational parameters to your function.** For example, if you are writing to an Amazon S3 bucket, instead of hard-coding the bucket name you are writing to, configure the bucket name as an environment variable.

**Avoid using recursive invocations** in your Lambda function, where the function invokes itself or initiates a process that may invoke the function again. This could lead to unintended volume of function invocations and escalated costs. If you see an unintended volume of invocations, set the function reserved concurrency to `0` immediately to throttle all invocations to the function, while you update the code.

**Do not use non-documented, non-public APIs** in your Lambda function code. For AWS Lambda managed runtimes, Lambda periodically applies security and functional updates to Lambda's internal APIs. These internal API updates may be backwards-incompatible, leading to unintended consequences such as invocation failures if your function has a dependency on these non-public APIs. See [the API reference](https://docs.aws.amazon.com/lambda/latest/api/welcome.html) for a list of publicly available APIs.

**Write idempotent code.** Writing idempotent code for your functions ensures that duplicate events are handled the same way. Your code should properly validate events and gracefully handle duplicate events. For more information, see [How do I make my Lambda function idempotent?](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-idempotent/).