---
id: "@specs/aws/lambda/docs/concepts-application-design"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Designing an application"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Designing an application

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/concepts-application-design
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Designing Lambda applications
<a name="concepts-application-design"></a>

A well-architected event-driven application uses a combination of AWS services and custom code to process and manage requests and data. This chapter focuses on Lambda-specific topics in application design. There are many important considerations for serverless architects when designing applications for busy production systems.

Many of the best practices that apply to software development and distributed systems also apply to serverless application development. The overall goal is to develop workloads that are:
+  **Reliable** – offering your end users a high level of availability. AWS serverless services are reliable because they are also designed for failure.
+  **Durable** – providing storage options that meet the durability needs of your workload.
+  **Secure** – following best practices and using the tools provided to secure access to workloads and limit the blast radius.
+  **Performant** – using computing resources efficiently and meeting the performance needs of your end users.
+  **Cost-efficient**– designing architectures that avoid unnecessary cost that can scale without overspending, and also be decommissioned without significant overhead.

The following design principles can help you build workloads that meet these goals. Not every principle may apply to every architecture, but they should guide you in general architecture decisions.

**Topics**
+ [Use services instead of custom code](#services-custom-code)
+ [Understand Lambda abstraction levels](#level-abstraction)
+ [Implement statelessness in functions](#statelessness-functions)
+ [Minimize coupling](#minimize-coupling)
+ [Build for on-demand data instead of batches](#on-demand-batches)
+ [Choose an orchestration option for complex workflows](#orchestration)
+ [Implement idempotency](#retries-failures)
+ [Use multiple AWS accounts for managing quotas](#multiple-accounts)

## Use services instead of custom code
<a name="services-custom-code"></a>

Serverless applications usually comprise several AWS services, integrated with custom code run in Lambda functions. While Lambda can be integrated with most AWS services, the services most commonly used in serverless applications are:


| Category | AWS service | 
| --- | --- | 
| Compute | AWS Lambda | 
| Data storage | Amazon S3<br />Amazon DynamoDB<br />Amazon RDS | 
| API | Amazon API Gateway | 
| Application integration | Amazon EventBridge<br />Amazon SNS<br />Amazon SQS | 
| Orchestration | Lambda durable functions<br />AWS Step Functions | 
| Streaming data and analytics | Amazon Data Firehose | 

**Note**  
Many serverless services provide replication and support for multiple Regions, including DynamoDB and Amazon S3. Lambda functions can be deployed in multiple Regions as part of a deployment pipeline, and API Gateway can be configured to support this configuration. See this [ example architecture](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/serverless-architecture-for-global-applications-ra.pdf?did=wp_card&trk=wp_card) that shows how this can be achieved.

There are many well-established, common patterns in distributed architectures that you can build yourself or implement using AWS services. For most customers, there is little commercial value in investing time to develop these patterns from scratch. When your application needs one of these patterns, use the corresponding AWS service:


| Pattern | AWS service | 
| --- | --- | 
| Queue | Amazon SQS | 
| Event bus | Amazon EventBridge | 
| Publish/subscribe (fan-out) | Amazon SNS | 
| Orchestration | Lambda durable functions<br />AWS Step Functions | 
| API | Amazon API Gateway | 
| Event streams | Amazon Kinesis | 

These services are designed to integrate with Lambda and you can use infrastructure as code (IaC) to create and discard resources in the services. You can use any of these services via the [AWS SDK](https://aws.amazon.com/tools/) without needing to install applications or configure servers. Becoming proficient with using these services via code in your Lambda functions is an important step to producing well-designed serverless applications.

## Understand Lambda abstraction levels
<a name="level-abstraction"></a>

The Lambda service limits your access to the underlying operating systems, hypervisors, and hardware running your Lambda functions. The service continuously improves and changes infrastructure to add features, reduce cost and make the service more performant. Your code should assume no knowledge of how Lambda is architected and assume no hardware affinity.

Similarly, Lambda's integrations with other services are managed by AWS, with only a small number of configuration options exposed to you. For example, when API Gateway and Lambda interact, there is no concept of load balancing since it is entirely managed by the services. You also have no direct control over which [Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) the services use when invoking functions at any point in time, or how Lambda determines when to scale up or down the number of execution environments.

This abstraction helps you focus on the integration aspects of your application, the flow of data, and the business logic where your workload provides value to your end users. Allowing the services to manage the underlying mechanics helps you develop applications more quickly with less custom code to maintain.

## Implement statelessness in functions
<a name="statelessness-functions"></a>

For standard Lambda functions, you should assume that the environment exists only for a single invocation. The function should initialize any required state when it is first started. For example, your function may require fetching data from a DynamoDB table. It should commit any permanent data changes to a durable store such as Amazon S3, DynamoDB, or Amazon SQS before exiting. It should not rely on any existing data structures or temporary files, or any internal state that would be managed by multiple invocations.

To initialize database connections and libraries, or load state, you can take advantage of [static initialization](lambda-runtime-environment.md#static-initialization). Since execution environments are reused where possible to improve performance, you can amortize the time taken to initialize these resources over multiple invocations. However, you should not store any variables or data used in the function within this global scope.

## Minimize coupling
<a name="minimize-coupling"></a>

Most architectures should prefer many, shorter functions over fewer, larger ones. The purpose of each function should be to handle the event passed into the function, with no knowledge or expectations of the overall workflow or volume of transactions. This makes the function agnostic to the source of the event with minimal coupling to other services.

Any global-scope constants that change infrequently should be implemented as environment variables to allow updates without deployments. Any secrets or sensitive information should be stored in [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) or [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) and loaded by the function. Since these resources are account-specific, you can create build pipelines across multiple accounts. The pipelines load the appropriate secrets per environment, without exposing these to developers or requiring any code changes.

## Build for on-demand data instead of batches
<a name="on-demand-batches"></a>

Many traditional systems are designed to run periodically and process batches of transactions that have built up over time. For example, a banking application may run every hour to process ATM transactions into central ledgers. In Lambda-based applications, the custom processing should be triggered by every event, allowing the service to scale up concurrency as needed, to provide near-real time processing of transactions.

While standard Lambda functions are limited to 15 minutes of execution time, Durable Functions can run for up to one year, making them suitable for longer-running processing needs. However, you should still prefer event-driven processing over batch processing when possible.

While you can run [cron](https://en.wikipedia.org/wiki/Cron) tasks in serverless applications [by using scheduled expressions](https://docs.aws.amazon.com/eventbridge/latest/userguide/scheduled-events.html) for rules in Amazon EventBridge, these should be used sparingly or as a last-resort. In any scheduled task that processes a batch, there is the potential for the volume of transactions to grow beyond what can be processed within the 15-minute Lambda duration limit. If the limitations of external systems force you to use a scheduler, you should generally schedule for the shortest reasonable recurring time period.

For example, it’s not best practice to use a batch process that triggers a Lambda function to fetch a list of new Amazon S3 objects. This is because the service may receive more new objects in between batches than can be processed within a 15-minute Lambda function.

![event driven architectures figure 10](http://docs.aws.amazon.com/lambda/latest/dg/images/event-driven-architectures-figure-10.png)


Instead, Amazon S3 should invoke the Lambda function each time a new object is put into the bucket. This approach is significantly more scalable and works in near-real time.

![event driven architectures figure 11](http://docs.aws.amazon.com/lambda/latest/dg/images/event-driven-architectures-figure-11.png)


## Choose an orchestration option for complex workflows
<a name="orchestration"></a>

Workflows that involve branching logic, different types of failure models, and retry logic typically use an orchestrator to keep track of the state of the overall execution. Don't build ad-hoc orchestration in standard Lambda functions. This results in tight coupling, complex routing code, and no automatic state recovery.

Instead, use one of these purpose-built orchestration options:
+ **[Lambda durable functions](durable-functions.md):** Application-centric orchestration using standard programming languages with automatic checkpointing, built-in retry, and execution recovery. Ideal for developers who prefer keeping workflow logic in code alongside business logic within Lambda.
+ **[AWS Step Functions](with-step-functions.md):** Visual workflow orchestration with native integrations to 220\+ AWS services. Ideal for multi-service coordination, zero-maintenance infrastructure, and visual workflow design.

For guidance on choosing between these options, see [Durable functions or Step Functions](durable-step-functions.md).

With [Step Functions](https://aws.amazon.com/step-functions/), you use state machines to manage orchestration. This extracts the error handling, routing, and branching logic from your code, replacing it with state machines declared using JSON. Apart from making workflows more robust and observable, you can also add versioning to workflows and make the state machine a codified resource that you can add to a code repository.

It’s common for simpler workflows in Lambda functions to become more complex over time. When operating a production serverless application, it’s important to identify when this is happening, so you can migrate this logic to a state machine or durable function.

## Implement idempotency
<a name="retries-failures"></a>

AWS serverless services, including Lambda, are fault-tolerant and designed to handle failures. For example, if a service invokes a Lambda function and there is a service disruption, Lambda invokes your function in a different Availability Zone. If your function throws an error, Lambda retries the invocation.

Since the same event may be received more than once, functions should be designed to be [idempotent](https://en.wikipedia.org/wiki/Idempotence). This means that receiving the same event multiple times does not change the result beyond the first time the event was received.

You can implement idempotency in Lambda functions by using a DynamoDB table to track recently processed identifiers to determine if the transaction has already been handled previously. The DynamoDB table usually implements a [Time To Live (TTL)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html) value to expire items to limit the storage space used.

## Use multiple AWS accounts for managing quotas
<a name="multiple-accounts"></a>

Many [service quotas](gettingstarted-limits.md) in AWS are set at the account level. This means that as you add more workloads, you can quickly exhaust your limits.

An effective way to solve this issue is to use multiple AWS accounts, dedicating each workload to its own account. This prevents quotas from being shared with other workloads or non-production resources.

 In addition, by using [AWS Organizations](https://aws.amazon.com/organizations/), you can centrally manage the billing, compliance, and security of these accounts. You can attach policies to groups of accounts to avoid custom scripts and manual processes.

One common approach is to provide each developer with an AWS account, and then use separate accounts for a beta deployment stage and production:

![application design figure 3](http://docs.aws.amazon.com/lambda/latest/dg/images/application-design-figure-3.png)


In this model, each developer has their own set of limits for the account, so their usage does not impact your production environment. This approach also allows developers to test Lambda functions locally on their development machines against live cloud resources in their individual accounts.