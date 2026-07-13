---
id: "@specs/aws/lambda/docs/config-rs-write-functions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Writing functions"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Writing functions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/config-rs-write-functions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Writing response streaming-enabled Lambda functions
<a name="config-rs-write-functions"></a>

Writing the handler for response streaming functions is different than typical handler patterns. When writing streaming functions, be sure to do the following:
+ Wrap your function with the `awslambda.streamifyResponse()` decorator. The `awslambda` global object is provided by Lambda's Node.js runtime environment.
+ End the stream gracefully to ensure that all data processing is complete.

## Configuring a handler function to stream responses
<a name="config-rs-write-functions-handler"></a>

To indicate to the runtime that Lambda should stream your function's responses, you must wrap your function with the `streamifyResponse()` decorator. This tells the runtime to use the proper logic path for streaming responses and enables the function to stream responses.

The `streamifyResponse()` decorator accepts a function that accepts the following parameters:
+ `event` – Provides information about the function URL's invocation event, such as the HTTP method, query parameters, and the request body.
+ `responseStream` – Provides a writable stream.
+ `context` – Provides methods and properties with information about the invocation, function, and execution environment.

The `responseStream` object is a [Node.js `writableStream`](https://nodesource.com/blog/understanding-streams-in-nodejs/). As with any such stream, you should use the `pipeline()` method.

**Note**  
The `awslambda` global object is automatically provided by Lambda's Node.js runtime and no import is required.

**Example response streaming-enabled handler**  

```
import { pipeline } from 'node:stream/promises';
import { Readable } from 'node:stream';

export const echo = awslambda.streamifyResponse(async (event, responseStream, _context) => {
  // As an example, convert event to a readable stream.
  const requestStream = Readable.from(Buffer.from(JSON.stringify(event)));

  await pipeline(requestStream, responseStream);
});
```

While `responseStream` offers the `write()` method to write to the stream, we recommend that you use [https://nodejs.org/api/stream.html#streampipelinesource-transforms-destination-callback](https://nodejs.org/api/stream.html#streampipelinesource-transforms-destination-callback) wherever possible. Using `pipeline()` ensures that the writable stream is not overwhelmed by a faster readable stream.

## Ending the stream
<a name="config-rs-write-functions-end"></a>

Make sure that you properly end the stream before the handler returns. The `pipeline()` method handles this automatically.

For other use cases, call the `responseStream.end()` method to properly end a stream. This method signals that no more data should be written to the stream. This method isn't required if you write to the stream with `pipeline()` or `pipe()`.

Starting with Node.js 24, Lambda no longer waits for unresolved promises to complete after your handler returns or the response stream ends. If your function depends on additional asynchronous operations, such as timers or fetches, you should `await` them in your handler.

**Example ending a stream with pipeline()**  

```
import { pipeline } from 'node:stream/promises';

export const handler = awslambda.streamifyResponse(async (event, responseStream, _context) => {
  await pipeline(requestStream, responseStream);
});
```

**Example ending a stream without pipeline()**  

```
export const handler = awslambda.streamifyResponse(async (event, responseStream, _context) => {
  responseStream.write("Hello ");
  responseStream.write("world ");
  responseStream.write("from ");
  responseStream.write("Lambda!");
  responseStream.end();
});
```