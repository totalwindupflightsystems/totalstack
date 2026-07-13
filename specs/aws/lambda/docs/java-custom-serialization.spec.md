---
id: "@specs/aws/lambda/docs/java-custom-serialization"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Custom serialization"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Custom serialization

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/java-custom-serialization
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Customize serialization for Lambda Java functions
<a name="java-custom-serialization"></a>

The Lambda [Java managed runtimes](lambda-java.md#java-runtimes) support custom serialization for JSON events. Custom serialization can simplify your code and potentially improve performance.

**Topics**
+ [When to use custom serialization](#custom-serialization-use-cases)
+ [Implementing custom serialization](#implement-custom-serialization)
+ [Testing custom serialization](#test-custom-serialization)

## When to use custom serialization
<a name="custom-serialization-use-cases"></a>

When your Lambda function is invoked, the input event data needs to be deserialized into a Java object, and the output from your function needs to be serialized back into a format that can be returned as the function's response. The Lambda Java managed runtimes provide default serialization and deserialization capabilities that work well for handling event payloads from various AWS services, such as Amazon API Gateway and Amazon Simple Queue Service (Amazon SQS). To work with these service integration events in your function, add the [aws-java-lambda-events](https://mvnrepository.com/artifact/com.amazonaws/aws-lambda-java-events) dependency to your project. This AWS library contains Java objects representing these service integration events.

You can also use your own objects to represent the event JSON that you pass to your Lambda function. The managed runtime attempts to serialize the JSON to a new instance of your object with its default behavior. If the default serializer doesn’t have the desired behavior for your use case, use custom serialization.

For example, assume that your function handler expects a `Vehicle` class as input, with the following structure:

```
public class Vehicle {
    private String vehicleType;
    private long vehicleId;
}
```

However, the JSON event payload looks like this:

```
{
    "vehicle-type": "car",
    "vehicleID": 123
}
```

In this scenario, the default serialization in the managed runtime expects the JSON property names to match the camel case Java class property names (`vehicleType`, `vehicleId`). Because the property names in the JSON event aren't in camel case (`vehicle-type`, `vehicleID`), you must use custom serialization.

## Implementing custom serialization
<a name="implement-custom-serialization"></a>

Use a [Service Provider Interface](https://docs.oracle.com/javase/tutorial/sound/SPI-intro.html) to load a serializer of your choice instead of the managed runtime’s default serialization logic. You can serialize your JSON event payloads directly into Java objects, using the standard `RequestHandler` interface.

**To use custom serialization in your Lambda Java function**

1. Add the [aws-lambda-java-core](https://mvnrepository.com/artifact/com.amazonaws/aws-lambda-java-core) library as a dependency. This library includes the [CustomPojoSerializer](https://github.com/aws/aws-lambda-java-libs/blob/main/aws-lambda-java-core/src/main/java/com/amazonaws/services/lambda/runtime/CustomPojoSerializer.java) interface, along with other interface definitions for working with Java in Lambda.

1. Create a file named `com.amazonaws.services.lambda.runtime.CustomPojoSerializer` in the `src/main/resources/META-INF/services/` directory of your project.

1. In this file, specify the fully qualified name of your custom serializer implementation, which must implement the `CustomPojoSerializer` interface. Example:

   ```
   com.mycompany.vehicles.CustomLambdaSerialzer
   ```

1. Implement the `CustomPojoSerializer` interface to provide your custom serialization logic.

1. Use the standard `RequestHandler` interface in your Lambda function. The managed runtime will use your custom serializer.

For more examples of how to implement custom serialization using popular libraries such as fastJson, Gson, Moshi, and jackson-jr, see the [custom-serialization](https://github.com/aws/aws-lambda-java-libs/tree/main/samples/custom-serialization) sample in the AWS GitHub repository.

## Testing custom serialization
<a name="test-custom-serialization"></a>

Test your function to make sure that your serialization and deserialization logic is working as expected. You can use the AWS Serverless Application Model Command Line Interface (AWS SAM CLI) to emulate the invocation of your Lambda payload. This can help you quickly test and iterate on your function as you introduce a custom serializer.

1. Create a file with the JSON event payload that you would like to invoke your function with then call the AWS SAM CLI.

1. Run the [sam local invoke](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-invoke.html ) command to invoke your function locally. Example:

   ```
   sam local invoke -e src/test/resources/event.json
   ```

For more information, see [Locally invoke Lambda functions with AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-invoke.html).