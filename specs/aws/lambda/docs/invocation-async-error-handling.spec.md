---
id: "@specs/aws/lambda/docs/invocation-async-error-handling"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Error handling"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Error handling

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/invocation-async-error-handling
> **target_lang:** meta — documentation tier. ALL sections preserved.



# How Lambda handles errors and retries with asynchronous invocation
<a name="invocation-async-error-handling"></a>

Lambda manages your function's asynchronous event queue and attempts to retry on errors. If the function returns an error, by default Lambda attempts to run it two more times, with a one-minute wait between the first two attempts, and two minutes between the second and third attempts. Function errors include errors returned by the function's code and errors returned by the function's runtime, such as timeouts.

If the function doesn't have enough concurrency available to process all events, additional requests are throttled. For throttling errors (429) and system errors (500-series), Lambda returns the event to the queue and attempts to run the function again for up to 6 hours by default. The retry interval increases exponentially from 1 second after the first attempt to a maximum of 5 minutes. If the queue contains many entries, Lambda increases the retry interval and reduces the rate at which it reads events from the queue.

Even if your function doesn't return an error, it's possible for it to receive the same event from Lambda multiple times because the queue itself is eventually consistent. If the function can't keep up with incoming events, events might also be deleted from the queue without being sent to the function. Ensure that your function code gracefully handles duplicate events, and that you have enough concurrency available to handle all invocations.

When the queue is very long, new events might age out before Lambda has a chance to send them to your function. When an event expires or fails all processing attempts, Lambda discards it. You can [configure error handling](invocation-async-configuring.md) for a function to reduce the number of retries that Lambda performs, or to discard unprocessed events more quickly. To capture discarded events, [configure a dead-letter queue](invocation-async-retain-records.md#invocation-dlq) for the function. To capture records of failed invocations (such as timeouts or runtime errors), [create an on-failure destination](invocation-async-retain-records.md#invocation-async-destinations). 