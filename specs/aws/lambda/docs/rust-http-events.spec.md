---
id: "@specs/aws/lambda/docs/rust-http-events"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS HTTP events"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# HTTP events

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/rust-http-events
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Processing HTTP events with Rust
<a name="rust-http-events"></a>

Amazon API Gateway APIs, Application Load Balancers, and [Lambda function URLs](urls-configuration.md) can send HTTP events to Lambda. You can use the [aws\_lambda\_events](https://crates.io/crates/aws_lambda_events) crate from crates.io to process events from these sources.

**Example — Handle API Gateway proxy request**  
Note the following:  
+ `use aws_lambda_events::apigw::{ApiGatewayProxyRequest, ApiGatewayProxyResponse}`: The [aws\_lambda\_events](https://crates.io/crates/aws-lambda-events) crate includes many Lambda events. To reduce compilation time, use feature flags to activate the events you need. Example: `aws_lambda_events = { version = "0.8.3", default-features = false, features = ["apigw"] }`.
+ `use http::HeaderMap`: This import requires you to add the [http](https://crates.io/crates/http) crate to your dependencies.

```
use aws_lambda_events::apigw::{ApiGatewayProxyRequest, ApiGatewayProxyResponse};
use http::HeaderMap;
use lambda_runtime::{service_fn, Error, LambdaEvent};

async fn handler(
    _event: LambdaEvent<ApiGatewayProxyRequest>,
) -> Result<ApiGatewayProxyResponse, Error> {
    let mut headers = HeaderMap::new();
    headers.insert("content-type", "text/html".parse().unwrap());
    let resp = ApiGatewayProxyResponse {
        status_code: 200,
        multi_value_headers: headers.clone(),
        is_base64_encoded: false,
        body: Some("Hello AWS Lambda HTTP request".into()),
        headers,
    };
    Ok(resp)
}

#[tokio::main]
async fn main() -> Result<(), Error> {
    lambda_runtime::run(service_fn(handler)).await
}
```

The [Rust runtime client for Lambda](https://github.com/aws/aws-lambda-rust-runtime) also provides an abstraction over these event types that allows you to work with native HTTP types, regardless of which service sends the events. The following code is equivalent to the previous example, and it works out of the box with Lambda function URLs, Application Load Balancers, and API Gateway.

**Note**  
The [lambda\_http](https://crates.io/crates/lambda_http) crate uses the [lambda\_runtime](https://crates.io/crates/lambda_runtime) crate underneath. You don't have to import `lambda_runtime` separately.

**Example — Handle HTTP requests**  

```
use lambda_http::{service_fn, Error, IntoResponse, Request, RequestExt, Response};

async fn handler(event: Request) -> Result<impl IntoResponse, Error> {
    let resp = Response::builder()
        .status(200)
        .header("content-type", "text/html")
        .body("Hello AWS Lambda HTTP request")
        .map_err(Box::new)?;
    Ok(resp)
}

#[tokio::main]
async fn main() -> Result<(), Error> {
    lambda_http::run(service_fn(handler)).await
}
```

For another example of how to use `lambda_http`, see the [http-axum code sample](https://github.com/aws/aws-lambda-rust-runtime/blob/main/examples/http-axum/src/main.rs) on the AWS Labs GitHub repository.

**Sample HTTP Lambda events for Rust**
+ [Lambda HTTP events](https://github.com/aws/aws-lambda-rust-runtime/tree/main/examples/http-basic-lambda): A Rust function that handles HTTP events.
+ [Lambda HTTP events with CORS headers](https://github.com/aws/aws-lambda-rust-runtime/blob/main/examples/http-cors): A Rust function that uses Tower to inject CORS headers.
+ [Lambda HTTP events with shared resources](https://github.com/aws/aws-lambda-rust-runtime/tree/main/examples/basic-shared-resource): A Rust function that uses shared resources initialized before the function handler is created.