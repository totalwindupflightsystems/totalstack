---
id: "@specs/aws/lambda/docs/csharp-context"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Context"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Context

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/csharp-context
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using the Lambda context object to retrieve C\# function information
<a name="csharp-context"></a>

When Lambda runs your function, it passes a context object to the [handler](csharp-handler.md). This object provides properties with information about the invocation, function, and execution environment.

**Context properties**
+ `FunctionName` – The name of the Lambda function.
+ `FunctionVersion` – The [version](configuration-versions.md) of the function.
+ `InvokedFunctionArn` – The Amazon Resource Name (ARN) that's used to invoke the function. Indicates if the invoker specified a version number or alias.
+ `MemoryLimitInMB` – The amount of memory that's allocated for the function.
+ `AwsRequestId` – The identifier of the invocation request.
+ `LogGroupName` – The log group for the function.
+ `LogStreamName` – The log stream for the function instance.
+ `RemainingTime` (`TimeSpan`) – The number of milliseconds left before the execution times out.
+ `Identity` – (mobile apps) Information about the Amazon Cognito identity that authorized the request.
+ `ClientContext` – (mobile apps) Client context that's provided to Lambda by the client application.
+ `Logger` The [logger object](csharp-logging.md) for the function.

You can use information in the `ILambdaContext` object to output information about your function's invocation for monitoring purposes. The following code provides an example of how to add context information to a structured logging framework. In this example, the function adds `AwsRequestId` to the log outputs. The function also uses the `RemainingTime` property to cancel an inflight task if the Lambda function timeout is about to be reached.

```
[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace GetProductHandler;

public class Function
{
    private readonly IDatabaseRepository _repo;
    
    public Function()
    {
        this._repo = new DatabaseRepository();
    }
    
    public async Task<APIGatewayProxyResponse> FunctionHandler(APIGatewayProxyRequest request, ILambdaContext context)
    {
        Logger.AppendKey("AwsRequestId", context.AwsRequestId);
        
        var id = request.PathParameters["id"];

        using var cts = new CancellationTokenSource();
        
        try
        {
            cts.CancelAfter(context.RemainingTime.Add(TimeSpan.FromSeconds(-1)));
            
            var databaseRecord = await this._repo.GetById(id, cts.Token);
            
            return new APIGatewayProxyResponse 
            {
                StatusCode = (int)HttpStatusCode.OK,
                Body = JsonSerializer.Serialize(databaseRecord)
            };
        }
        catch (Exception ex)
        {
            return new APIGatewayProxyResponse 
            {
                StatusCode = (int)HttpStatusCode.InternalServerError,
                Body = JsonSerializer.Serialize(new { error = ex.Message })
            };
        }
        finally
        {
            cts.Cancel();
        }
    }
}
```