---
id: "@specs/aws/lightsail/docs/cors-how-evaluation-works"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS How Lightsail evaluates CORS configurations"
status: active
depends_on:
  - "@specs/aws/lightsail/meta"
---

# How Lightsail evaluates CORS configurations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lightsail/docs/cors-how-evaluation-works
> **target_lang:** meta — documentation tier. ALL sections preserved.



# How Lightsail evaluates CORS configurations
<a name="cors-how-evaluation-works"></a>

When Lightsail object storage receives a preflight request from a browser, it evaluates the CORS configuration for the bucket and uses the first CORS rule that matches the incoming browser request to enable a cross-origin request. For a rule to match, the following conditions must be met:
+ The `Origin` header in the request must match an origin in the `AllowedOrigins` element.
+ The HTTP method specified in the `Access-Control-Request-Method` header must match a method in the `AllowedMethods` element.
+ The headers listed in the `Access-Control-Request-Headers` header must match headers in the `AllowedHeaders` element.

**Note**  
Bucket permissions continue to apply when you enable CORS on your bucket. CORS configuration only determines whether the browser allows the cross-origin request to proceed. For more information, see [Control access to Lightsail buckets and objects](amazon-lightsail-understanding-bucket-permissions.md).

## Elements of a CORS configuration
<a name="cors-configuration-elements"></a>

A CORS configuration is a JSON document that contains an array of CORS rules. Each rule defines which origins are allowed to access the bucket, which HTTP methods are permitted, and other configuration options.

The following elements can be included in a CORS rule:

**allowedOrigins**  
Specifies the origins that are allowed to access the bucket. You can use wildcards (\*) to allow all origins, or specify specific domains like `https://example.com`.

**allowedMethods**  
Specifies the HTTP methods that are allowed for the specified origins. Valid values include GET, PUT, POST, DELETE, and HEAD.

**allowedHeaders**  
Specifies which headers are allowed in a preflight OPTIONS request through the Access-Control-Request-Headers header.

**exposeHeaders**  
Specifies which headers in the response can be accessed by the client application.

**id**  
A unique identifier for the CORS rule.

**maxAgeSeconds**  
Specifies the amount of time in seconds that the browser can cache the response for a preflight request.

For more information about these parameters, see [BucketCorsRule](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_BucketCorsRule.html) in the *Amazon Lightsail API Reference*.