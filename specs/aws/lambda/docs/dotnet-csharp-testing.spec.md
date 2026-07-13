---
id: "@specs/aws/lambda/docs/dotnet-csharp-testing"
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
> **spec:id:** @specs/aws/lambda/docs/dotnet-csharp-testing
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AWS Lambda function testing in C\#
<a name="dotnet-csharp-testing"></a>

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
<a name="dotnet-csharp-testing-techniques-for-serverless-applications"></a>

 You will generally use a mix of approaches to test your serverless application code, including testing in the cloud, testing with mocks, and occasionally testing with emulators. 

### Testing in the cloud
<a name="dotnet-csharp-testing-in-the-cloud"></a>

 Testing in the cloud is valuable for all phases of testing, including unit tests, integration tests, and end-to-end tests. You run tests against code deployed in the cloud and interacting with cloud-based services. This approach provides the **most accurate** measure of quality of your code. 

 A convenient way to debug your Lambda function in the cloud is through the console with a test event. A *test event* is a JSON input to your function. If your function does not require input, the event can be an empty JSON document `({})`. The console provides sample events for a variety of service integrations. After creating an event in the console, you can share it with your team to make testing easier and consistent. 

**Note**  
[Testing a function in the console](testing-functions.md) is a quick way to get started, but automating your test cycles ensures application quality and development speed. 

### Testing tools
<a name="dotnet-csharp-testing-tools"></a>

To accelerate your development cycle, there are a number of tools and techniques you can use when testing your functions. For example, [AWS SAM Accelerate](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/using-sam-cli-sync.html) and [AWS CDK watch mode](https://docs.aws.amazon.com/cdk/v2/guide/cli.html#cli-deploy-watch) both decrease the time required to update cloud environments.

The way you define your Lambda function code makes it simple to add unit tests. Lambda requires a public, parameterless constructor to initialize your class. Introducing a second, internal constructor gives you control of the dependencies your application uses.

```
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace GetProductHandler;

public class Function
{
    private readonly IDatabaseRepository _repo;
    
    public Function(): this(null)
    {
    }
    
    internal Function(IDatabaseRepository repo)
    {
        this._repo = repo ?? new DatabaseRepository();
    }
    
    public async Task<APIGatewayProxyResponse> FunctionHandler(APIGatewayProxyRequest request)
    {
        var id = request.PathParameters["id"];
        
        var databaseRecord = await this._repo.GetById(id);
        
        return new APIGatewayProxyResponse 
        {
            StatusCode = (int)HttpStatusCode.OK,
            Body = JsonSerializer.Serialize(databaseRecord)
        };
    }
}
```

To write a test for this function, you can initialize a new instance of your `Function` class and pass in a mocked implementation of the `IDatabaseRepository`. The below examples uses `XUnit`, `Moq`, and `FluentAssertions` to write a simple test ensuring the `FunctionHandler` returns a 200 status code.

```
using Xunit;
using Moq;
using FluentAssertions;

public class FunctionTests
{
    [Fact]
    public async Task TestLambdaHandler_WhenInputIsValid_ShouldReturn200StatusCode()
    {
        // Arrange
        var mockDatabaseRepository = new Mock<IDatabaseRepository>();
        
        var functionUnderTest = new Function(mockDatabaseRepository.Object);
        
        // Act
        var response = await functionUnderTest.FunctionHandler(new APIGatewayProxyRequest());
        
        // Assert
        response.StatusCode.Should().Be(200);
    }
}
```

For more detailed examples, including examples of asynchronous tests, see the [.NET testing samples repository](https://github.com/aws-samples/serverless-test-samples/tree/main/dotnet-test-samples) on GitHub.