---
id: "@specs/aws/lambda/docs/python-testing"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Testing"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Testing

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/python-testing
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AWS Lambda function testing in Python
<a name="python-testing"></a>

**Note**  
See the [Testing functions](testing-guide.md) chapter for a complete introduction to techniques and best practices for testing serverless solutions. 

 Testing serverless functions uses traditional test types and techniques, but you must also consider testing serverless applications as a whole. Cloud-based tests will provide the **most accurate** measure of quality of both your functions and serverless applications. 

 A serverless application architecture includes managed services that provide critical application functionality through API calls. For this reason, your development cycle should include automated tests that verify functionality when your function and services interact. 

 If you do not create cloud-based tests, you could encounter issues due to differences between your local environment and the deployed environment. Your continuous integration process should run tests against a suite of resources provisioned in the cloud before promoting your code to the next deployment environment, such as QA, Staging, or Production. 

 Continue reading this short guide to learn about testing strategies for serverless applications, or visit the [Serverless Test Samples repository](https://github.com/aws-samples/serverless-test-samples) to dive in with practical examples, specific to your chosen language and runtime. 

 ![illustration showing the relationship between types of tests](http://docs.aws.amazon.com/lambda/latest/dg/images/test-type-illustration2.png) 

 For serverless testing, you will still write *unit*, *integration* and *end-to-end* tests. 
+ **Unit tests** - Tests that run against an isolated block of code. For example, verifying the business logic to calculate the delivery charge given a particular item and destination.
+ **Integration tests** - Tests involving two or more components or services that interact, typically in a cloud environment. For example, verifying a function processes events from a queue.
+ **End-to-end tests** - Tests that verify behavior across an entire application. For example, ensuring infrastructure is set up correctly and that events flow between services as expected to record a customer's order.

## Testing your serverless applications
<a name="python-testing-techniques-for-serverless-applications"></a>

 You will generally use a mix of approaches to test your serverless application code, including testing in the cloud, testing with mocks, and occasionally testing with emulators. 

### Testing in the cloud
<a name="python-testing-in-the-cloud"></a>

 Testing in the cloud is valuable for all phases of testing, including unit tests, integration tests, and end-to-end tests. You run tests against code deployed in the cloud and interacting with cloud-based services. This approach provides the **most accurate** measure of quality of your code. 

 A convenient way to debug your Lambda function in the cloud is through the console with a test event. A *test event* is a JSON input to your function. If your function does not require input, the event can be an empty JSON document `({})`. The console provides sample events for a variety of service integrations. After creating an event in the console, you can share it with your team to make testing easier and consistent. 

**Note**  
[Testing a function in the console](testing-functions.md) is a quick way to get started, but automating your test cycles ensures application quality and development speed. 

### Testing tools
<a name="python-testing-tools"></a>

 Tools and techniques exist to accelerate development feedback loops. For example, [AWS SAM Accelerate](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/accelerate.html) and [AWS CDK watch mode](https://docs.aws.amazon.com/cdk/v2/guide/cli.html#cli-deploy-watch) both decrease the time required to update cloud environments. 

[Moto](https://pypi.org/project/moto/) is a Python library for mocking AWS services and resources, so that you can test your functions with little or no modification using decorators to intercept and simulate responses. 

 The validation feature of the [Powertools for AWS Lambda (Python)](https://docs.powertools.aws.dev/lambda-python/latest/utilities/validation/) provides decorators so you can validate input events and output responses from your Python functions. 

 For more information, read the blog post [Unit Testing Lambda with Python and Mock AWS Services](https://aws.amazon.com/blogs/devops/unit-testing-aws-lambda-with-python-and-mock-aws-services/). 

 To reduce the latency involved with cloud deployment iterations, see [AWS Serverless Application Model (AWS SAM) Accelerate](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-sync.html), [AWS Cloud Development Kit (AWS CDK) watch mode](https://docs.aws.amazon.com/cdk/v2/guide/cli.html#cli-deploy-watch). These tools monitor your infrastructure and code for changes. They react to these changes by creating and deploying incremental updates automatically into your cloud environment. 

 Examples that use these tools are available in the [Python Test Samples](https://github.com/aws-samples/serverless-test-samples/tree/main/python-test-samples) code repository. 