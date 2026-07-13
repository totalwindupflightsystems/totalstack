---
id: "@specs/aws/lambda/docs/scaling-behavior"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Scaling behavior"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Scaling behavior

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/scaling-behavior
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Lambda scaling behavior
<a name="scaling-behavior"></a>

As your function receives more requests, Lambda automatically scales up the number of execution environments to handle these requests until your account reaches its concurrency quota. However, to protect against over-scaling in response to sudden bursts of traffic, Lambda limits how fast your functions can scale. This ** concurrency scaling rate** is the maximum rate at which functions in your account can scale in response to increased requests. (That is, how quickly Lambda can create new execution environments.) The concurrency scaling rate differs from the account-level concurrency limit, which is the total amount of concurrency available to your functions.

## Concurrency scaling rate
<a name="scaling-rate"></a>

**In each AWS Region, and for each function, your concurrency scaling rate is 1,000 execution environment instances every 10 seconds (or 10,000 requests per second every 10 seconds).** In other words, every 10 seconds, Lambda can allocate at most 1,000 additional execution environment instances, or accommodate 10,000 additional requests per second, to each of your functions.

Usually, you don't need to worry about this limitation. Lambda's scaling rate is sufficient for most use cases.

Importantly, the concurrency scaling rate is a function-level limit. This means that each function in your account can scale independently of other functions.

**Note**  
In practice, Lambda makes a best attempt to refill your concurrency scaling rate continuously over time, rather than in one single refill of 1,000 units every 10 seconds.

Lambda doesn't accrue unused portions of your concurrency scaling rate. This means that at any instant in time, your scaling rate is always 1,000 concurrency units at maximum. For example, if you don't use any of your available 1,000 concurrency units in a 10-second interval, you won't accrue 1,000 additional units in the next 10-second interval. Your concurrency scaling rate is still 1,000 in the next 10-second interval.

As long as your function continues to receive increasing numbers of requests, then Lambda scales at the fastest rate available to you, up to your account's concurrency limit. You can limit the amount of concurrency that individual functions can use by [configuring reserved concurrency](configuration-concurrency.md). If requests come in faster than your function can scale, or if your function is at maximum concurrency, then additional requests fail with a throttling error (429 status code).