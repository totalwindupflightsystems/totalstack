---
id: "@specs/aws/lambda/docs/concepts-event-driven-architectures"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Creating event-driven architectures"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Creating event-driven architectures

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/concepts-event-driven-architectures
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Creating event-driven architectures with Lambda
<a name="concepts-event-driven-architectures"></a>

An event is anything that triggers a Lambda function to run. Events can trigger a Lambda function in two ways: through direct invocation (push) and event source mappings (pull).

Many AWS services can directly invoke your Lambda functions. These services *push* events to your Lambda function. Events that trigger functions can be almost anything, from an HTTP request through API Gateway, a schedule managed by an EventBridge rule, an AWS IoT event, or an Amazon S3 event. With event source mapping, Lambda actively fetches (or *pulls*) events from a queue or stream. You configure Lambda to check for events from a supported service, and Lambda handles the polling and invocation of your function.

When passed to your function, events are structured in JSON format. The JSON structure varies depending on the service that generates it and the event type. While standard Lambda function invocations can last up to 15 minutes, Lambda is best-suited for short invocations that last one second or less. This is particularly true of event-driven architectures, where each Lambda function is treated as a microservice responsible for performing a narrow set of specific instructions.

**Note**  
Event-driven architectures communicate across different systems using networks, which introduce variable latency. For workloads that require very low latency, such as real-time trading systems, this design might not be the best choice. However, for highly scalable and available workloads, or those with unpredictable traffic patterns, event-driven architectures can provide an effective way to meet these demands.

**Topics**
+ [Benefits of event-driven architectures](#event-driven-benefits)
+ [Trade-offs of event-driven architectures](#event-driven-tradeoffs)
+ [Anti-patterns in Lambda-based event-driven applications](#event-driven-anti-patterns)

## Benefits of event-driven architectures
<a name="event-driven-benefits"></a>

Lambda supports two methods of invocation in event-driven architectures:

1. Direct invocation (push method): AWS services trigger Lambda functions directly. For example:
   + Amazon S3 triggers a function when a file is uploaded
   + API Gateway triggers a function when it receives an HTTP request

1. Event source mapping (pull method): Lambda retrieves events and invokes functions. For example:
   + Lambda retrieves messages from an Amazon SQS queue and invokes a function
   + Lambda reads records from a DynamoDB stream and invokes a function

Both methods contribute to the benefits of event-driven architectures, as described below.

### Replacing polling and webhooks with events
<a name="polling-webhooks-events"></a>

Many traditional architectures use polling and webhook mechanisms to communicate state between different components. Polling can be highly inefficient for fetching updates since there is a lag between new data becoming available and synchronization with downstream services. Webhooks are not always supported by other microservices that you want to integrate with. They might also require custom authorization and authentication configurations. In both cases, these integration methods are challenging to scale on-demand without additional work by development teams.

![event driven architectures figure 7](http://docs.aws.amazon.com/lambda/latest/dg/images/event-driven-architectures-figure-7.png)


Both of these mechanisms can be replaced by events, which can be filtered, routed, and pushed downstream to consuming microservices. This approach can result in less bandwidth consumption, CPU utilization, and potentially lower cost. These architectures can also reduce complexity, since each functional unit is smaller and there is often less code.

![event driven architectures figure 8](http://docs.aws.amazon.com/lambda/latest/dg/images/event-driven-architectures-figure-8.png)


Event-driven architectures can also make it easier to design near-real-time systems, helping organizations move away from batch-based processing. Events are generated at the time when state in the application changes, so the custom code of a microservice should be designed to handle the processing of a single event. Since scaling is handled by the Lambda service, this architecture can handle significant increases in traffic without changing custom code. As events scale up, so does the compute layer that processes events.

### Reducing complexity
<a name="complexity"></a>

Microservices enable developers and architects to simplify complex workflows. For example, an ecommerce monolith can be broken down into order acceptance and payment processes with separate inventory, fulfillment and accounting services. What might be complex to manage and orchestrate in a monolith becomes a series of decoupled services that communicate asynchronously with events.

![event driven architectures figure 9](http://docs.aws.amazon.com/lambda/latest/dg/images/event-driven-architectures-figure-9.png)


This approach also makes it possible to assemble services that process data at different rates. In this case, an order acceptance microservice can store high volumes of incoming orders by buffering the messages in an Amazon SQS queue.

A payment processing service, which is typically slower due to the complexity of handling payments, can take a steady stream of messages from the Amazon SQS queue. It can orchestrate complex retry and error handling logic using AWS Step Functions, and coordinate active payment workflows for hundreds of thousands of orders.

**Alternative approach:** For orchestration using standard programming languages, you can use [Lambda durable functions](durable-functions.md). Durable functions let you write the order acceptance, payment processing, and notification logic in code with automatic checkpointing and retry. This approach works well when the workflow primarily involves Lambda functions and you prefer keeping orchestration logic in code.

### Improving scalability and extensibility
<a name="scalability-extensibility"></a>

Microservices generate events that are typically published to messaging services like Amazon SNS and Amazon SQS. These behave like an elastic buffer between microservices and help handle scaling when traffic increases. Services like Amazon EventBridge can then filter and route messages depending upon the content of the event, as defined in rules. As a result, event-based applications can be more scalable and offer greater redundancy than monolithic applications.

This system is also highly extensible, allowing other teams to extend features and add functionality without impacting the order processing and payment processing microservices. By publishing events using EventBridge, this application integrates with existing systems, such as the inventory microservice, but also enables any future application to integrate as an event consumer. Producers of events have no knowledge of event consumers, which can help simplify the microservice logic.

## Trade-offs of event-driven architectures
<a name="event-driven-tradeoffs"></a>

### Variable latency
<a name="variable-latency"></a>

Unlike monolithic applications, which might process everything within the same memory space on a single device, event-driven applications communicate across networks. This design introduces variable latency. While it’s possible to engineer applications to minimize latency, monolithic applications can almost always be optimized for lower latency at the expense of scalability and availability.

Workloads that require consistent low-latency performance, such as high-frequency trading applications in banks or sub-millisecond robotics automation in warehouses, are not good candidates for event-driven architecture.

### Eventual consistency
<a name="eventual-consistency"></a>

An event represents a change in state, and with many events flowing through different services in an architecture at any given point of time, such workloads are often [eventually consistent](https://en.wikipedia.org/wiki/Eventual_consistency). This makes it more complex to process transactions, handle duplicates, or determine the exact overall state of a system.

Some workloads contain a combination of requirements that are eventually consistent (for example, total orders in the current hour) or strongly consistent (for example, current inventory). For workloads needing strong data consistency, there are architecture patterns to support this. For example:
+ DynamoDB can provide [ strongly consistent reads](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html), sometimes at a higher latency, consuming a greater throughput than the default mode. DynamoDB can also [ support transactions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/transactions.html) to help maintain data consistency.
+ You can use Amazon RDS for features needing [ACID properties](https://en.wikipedia.org/wiki/ACID), though relational databases are generally less scalable than NoSQL databases like DynamoDB. [Amazon RDS Proxy](https://aws.amazon.com/rds/proxy/) can help manage connection pooling and scaling from ephemeral consumers like Lambda functions.

Event-based architectures are usually designed around individual events instead of large batches of data. Generally, workflows are designed to manage the steps of an individual event or execution flow instead of operating on multiple events simultaneously. In serverless, real-time event processing is preferred over batch processing: batches should be replaced with many smaller incremental updates. While this can make workloads more available and scalable, it also makes it more challenging for events to have awareness of other events.

### Returning values to callers
<a name="values-callers"></a>

In many cases, event-based applications are asynchronous. This means that caller services do not wait for requests from other services before continuing with other work. This is a fundamental characteristic of event-driven architectures that enables scalability and flexibility. This means that passing return values or the result of a workflow is more complex than in synchronous execution flows.

Most Lambda invocations in production systems are [asynchronous](invocation-async.md), responding to events from services like Amazon S3 or Amazon SQS. In these cases, the success or failure of processing an event is often more important than returning a value. Features such as [dead letter queues](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html) (DLQs) in Lambda are provided to ensure you can identify and retry failed events, without needing to notify the caller.

### Debugging across services and functions
<a name="services-functions"></a>

Debugging event-driven systems is also different compared to a monolithic application. With different systems and services passing events, it's not possible to record and reproduce the exact state of multiple services when errors occur. Since each service and function invocation has separate log files, it can be more complicated to determine what happened to a specific event that caused an error.

There are three important requirements for building a successful debugging approach in event-driven systems. First, a robust logging system is critical, and this is provided across AWS services and embedded in Lambda functions by Amazon CloudWatch. Second, in these systems, it’s important to ensure that every event has a transaction identifier that is logged at each step throughout a transaction, to help when searching for logs.

Finally, it’s highly recommended to automate the parsing and analysis of logs by using a debugging and monitoring service like AWS X-Ray. This can consume logs across multiple Lambda invocations and services, making it much easier to pinpoint the root cause of issues. See [ Troubleshooting walkthrough](lambda-troubleshooting.md) for in-depth coverage of using X-Ray for troubleshooting.

## Anti-patterns in Lambda-based event-driven applications
<a name="event-driven-anti-patterns"></a>

When building event-driven architectures with Lambda, avoid the following common anti-patterns. These patterns work but can increase costs and complexity.

### The Lambda monolith
<a name="monolith"></a>

In many applications migrated from traditional servers, such as Amazon EC2 instances or Elastic Beanstalk applications, developers “lift and shift” existing code. Frequently, this results in a single Lambda function that contains all of the application logic that is triggered for all events. For a basic web application, a monolithic Lambda function would handle all API Gateway routes and integrate with all necessary downstream resources.

![event driven architectures figure 13](http://docs.aws.amazon.com/lambda/latest/dg/images/event-driven-architectures-figure-13.png)


This approach has several drawbacks:
+  **Package size** – The Lambda function might be much larger because it contains all possible code for all paths, which makes it slower for the Lambda service to run.
+  **Hard to enforce least privilege** – The function’s [execution role](lambda-intro-execution-role.md) must allow permissions to all resources needed for all paths, making the permissions very broad. This is a security concern. Many paths in the functional monolith do not need all the permissions that have been granted.
+  **Harder to upgrade** – In a production system, any upgrades to the single function are more risky and could break the entire application. Upgrading a single path in the Lambda function is an upgrade to the entire function.
+  **Harder to maintain** – It’s more difficult to have multiple developers working on the service since it’s a monolithic code repository. It also increases the cognitive burden on developers and makes it harder to create appropriate test coverage for code.
+  **Harder to reuse code** – It's harder to separate reusable libraries from monoliths, making code reuse more difficult. As you develop and support more projects, this can make it harder to support the code and scale your team’s velocity.
+  **Harder to test** – As the lines of code increase, it becomes harder to unit test all the possible combinations of inputs and entry points in the code base. It’s generally easier to implement unit testing for smaller services with less code.

The preferred alternative is to break down the monolithic Lambda function into individual microservices, mapping a single Lambda function to a single, well-defined task. In this simple web application with a few API endpoints, the resulting microservice-based architecture can be based upon the API Gateway routes.

![event driven architectures figure 14](http://docs.aws.amazon.com/lambda/latest/dg/images/event-driven-architectures-figure-14.png)


### Recursive patterns that cause runaway Lambda functions
<a name="recursive-runaway"></a>

AWS services generate events that invoke Lambda functions, and Lambda functions can send messages to AWS services. Generally, the service or resource that invokes a Lambda function should be different to the service or resource that the function outputs to. Failure to manage this can result in infinite loops.

For example, a Lambda function writes an object to an Amazon S3 object, which in turn invokes the same Lambda function via a put event. The invocation causes a second object to be written to the bucket, which invokes the same Lambda function:

![event driven architectures figure 15](http://docs.aws.amazon.com/lambda/latest/dg/images/event-driven-architectures-figure-15.png)


While the potential for infinite loops exists in most programming languages, this anti-pattern has the potential to consume more resources in serverless applications. Both Lambda and Amazon S3 automatically scale based upon traffic, so the loop can cause Lambda to scale to consume all available concurrency and Amazon S3 will continue to write objects and generate more events for Lambda.

This example uses S3, but the risk of recursive loops also exists in Amazon SNS, Amazon SQS, DynamoDB, and other services. You can use [recursive loop detection](invocation-recursion.md) to find and avoid this anti-pattern.

### Lambda functions calling Lambda functions
<a name="functions-calling-functions"></a>

Functions enable encapsulation and code re-use. Most programming languages support the concept of code synchronously calling functions within a code base. In this case, the caller waits until the function returns a response.

**Note**  
While Lambda functions directly calling other Lambda functions is generally an anti-pattern due to cost and complexity concerns, this doesn't apply to [durable functions](durable-functions.md), which are specifically designed to orchestrate multi-step workflows by invoking other functions.

When this happens on a traditional server or virtual instance, the operating system scheduler switches to other available work. Whether the CPU runs at 0% or 100% does not affect the overall cost of the application, since you are paying for the fixed cost of owning and operating a server.

This model often does not adapt well to serverless development. For example, consider a simple ecommerce application consisting of three Lambda functions that process an order:

![event driven architectures figure 16](http://docs.aws.amazon.com/lambda/latest/dg/images/event-driven-architectures-figure-16.png)


In this case, the *Create order* function calls the *Process payment* function, which in turn calls the *Create invoice* function. While this synchronous flow might work within a single application on a server, it introduces several avoidable problems in a distributed serverless architecture:
+  **Cost** – With Lambda, you pay for the duration of an invocation. In this example, while the *Create invoice* functions runs, two other functions are also running in a wait state, shown in red on the diagram.
+  **Error handling** – In nested invocations, error handling can become much more complex. For example, an error in *Create invoice* might require the *Process payment* function to reverse the charge, or it might instead retry the *Create invoice* process.
+  **Tight coupling** – Processing a payment typically takes longer than creating an invoice. In this model, the availability of the entire workflow is limited by the slowest function.
+  **Scaling** – The [concurrency](lambda-concurrency.md) of all three functions must be equal. In a busy system, this uses more concurrency than would otherwise be needed.

In serverless applications, there are two common approaches to avoid this pattern. First, use an Amazon SQS queue between Lambda functions. If a downstream process is slower than an upstream process, the queue durably persists messages and decouples the two functions. In this example, the *Create order* function would publish a message to an Amazon SQS queue, and the *Process payment* function consumes messages from the queue.

The second approach is to use AWS Step Functions. For complex processes with multiple types of failure and retry logic, Step Functions can help reduce the amount of custom code needed to orchestrate the workflow. As a result, Step Functions orchestrates the work and robustly handles errors and retries, and the Lambda functions contain only business logic.

### Synchronous waiting within a single Lambda function
<a name="synchronous-waiting"></a>

Make sure that any potentially concurrent activities are not scheduled synchronously within a single Lambda function. For example, a Lambda function might write to an S3 bucket and then write to a DynamoDB table:

![event driven architectures figure 17](http://docs.aws.amazon.com/lambda/latest/dg/images/event-driven-architectures-figure-17.png)


In this design, wait times are compounded because the activities are sequential. In cases where the second task depends on the completion of the first task, you can reduce the total waiting time and the cost of execution by have two separate Lambda functions:

![event driven architectures figure 19](http://docs.aws.amazon.com/lambda/latest/dg/images/event-driven-architectures-figure-19.png)


In this design, the first Lambda function responds immediately after putting the object to the Amazon S3 bucket. The S3 service invokes the second Lambda function, which then writes data to the DynamoDB table. This approach minimizes the total wait time in the Lambda function executions.