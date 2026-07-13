---
id: "@specs/aws/lambda/docs/configuration-metadata-endpoint"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS Metadata endpoint"
status: active
depends_on:
  - "@specs/aws/lambda/meta"
---

# Metadata endpoint

> **source:** AWS Documentation
> **spec:id:** @specs/aws/lambda/docs/configuration-metadata-endpoint
> **target_lang:** meta — documentation tier. ALL sections preserved.



# Using the Lambda metadata endpoint
<a name="configuration-metadata-endpoint"></a>

The Lambda metadata endpoint lets your functions discover which Availability Zone (AZ) they are running in, enabling you to optimize latency by routing to same-AZ resources like Amazon ElastiCache and Amazon RDS endpoints, and to implement AZ-aware resilience patterns.

The endpoint returns metadata in a simple JSON format through a localhost HTTP API within the execution environment and is accessible to both runtimes and extensions.

**Topics**
+ [Getting started](#metadata-endpoint-getting-started)
+ [Understanding Availability Zone IDs](#metadata-endpoint-az-ids)
+ [API reference](#metadata-endpoint-api-reference)

## Getting started
<a name="metadata-endpoint-getting-started"></a>

[Powertools for AWS Lambda](https://docs.aws.amazon.com/powertools/) provides a utility for accessing the Lambda metadata endpoint in Python, TypeScript, Java, and .NET. The utility caches the response after the first call and handles SnapStart cache invalidation automatically.

Use the Powertools for AWS Lambda metadata utility or call the metadata endpoint directly

------
#### [ Python ]

Install the Powertools package:

```
pip install "aws-lambda-powertools"
```

Use the metadata utility in your handler:

**Example Retrieving AZ ID with Powertools (Python)**  

```
from aws_lambda_powertools.utilities.lambda_metadata import get_lambda_metadata

def handler(event, context):
    metadata = get_lambda_metadata()
    az_id = metadata.availability_zone_id  # e.g., "use1-az1"

    return {"az_id": az_id}
```

------
#### [ TypeScript ]

Install the Powertools package:

```
npm install @aws-lambda-powertools/commons
```

Use the metadata utility in your handler:

**Example Retrieving AZ ID with Powertools (TypeScript)**  

```
import { getMetadata } from '@aws-lambda-powertools/commons/utils/metadata';

const metadata = await getMetadata();

export const handler = async () => {
  const { AvailabilityZoneID: azId } = metadata;
  return azId;
};
```

------
#### [ Java ]

Add the Powertools dependency to your `pom.xml`:

```
<dependencies>
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-lambda-metadata</artifactId>
        <version>2.10.0</version>
    </dependency>
</dependencies>
```

Use the metadata client in your handler:

**Example Retrieving AZ ID with Powertools (Java)**  

```
import software.amazon.lambda.powertools.metadata.LambdaMetadata;
import software.amazon.lambda.powertools.metadata.LambdaMetadataClient;

public class App implements RequestHandler<Object, String> {

    @Override
    public String handleRequest(Object input, Context context) {
        LambdaMetadata metadata = LambdaMetadataClient.get();
        String azId = metadata.getAvailabilityZoneId(); // e.g., "use1-az1"

        return "{\"azId\": \"" + azId + "\"}";
    }
}
```

------
#### [ .NET ]

Install the Powertools package:

```
dotnet add package AWS.Lambda.Powertools.Metadata
```

Use the metadata class in your handler:

**Example Retrieving AZ ID with Powertools (.NET)**  

```
using AWS.Lambda.Powertools.Metadata;

public class Function
{
    public string Handler(object input, ILambdaContext context)
    {
        var azId = LambdaMetadata.AvailabilityZoneId;
        return $"Running in AZ: {azId}";
    }
}
```

------
#### [ All Runtimes ]

All Lambda runtimes support the metadata endpoint, including custom runtimes and container images. Use the following example to access the metadata API directly from your function using the environment variables that Lambda automatically sets in the execution environment.

**Example Accessing the metadata endpoint directly**  

```
# Variables are automatically set by Lambda
METADATA_ENDPOINT="http://${AWS_LAMBDA_METADATA_API}/2026-01-15/metadata/execution-environment"

# Make the request
RESPONSE=$(curl -s -H "Authorization: Bearer ${AWS_LAMBDA_METADATA_TOKEN}" "$METADATA_ENDPOINT")

# Parse the AZ ID
AZ_ID=$(echo "$RESPONSE" | jq -r '.AvailabilityZoneID')

echo "Function is running in AZ ID: $AZ_ID"
```

------

## Understanding Availability Zone IDs
<a name="metadata-endpoint-az-ids"></a>

AZ IDs (for example, `use1-az1`) always refer to the same physical location across all AWS accounts, while AZ names (for example, `us-east-1a`) may map to different physical infrastructure in each AWS account in certain regions. For more information, see [AZ IDs for cross-account consistency](https://docs.aws.amazon.com/global-infrastructure/latest/regions/az-ids.html).

**Converting AZ ID to AZ name:**

To convert an AZ ID to an AZ name, use the Amazon EC2 [DescribeAvailabilityZones](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html) API. To use this API, add the `ec2:DescribeAvailabilityZones` permission to your function's execution role.

## API reference
<a name="metadata-endpoint-api-reference"></a>

### Environment variables
<a name="metadata-endpoint-env-vars"></a>

Lambda automatically sets the following environment variables in every execution environment:
+ `AWS_LAMBDA_METADATA_API` – The metadata server address in the format `{ipv4_address}:{port}` (for example, `169.254.100.1:9001`).
+ `AWS_LAMBDA_METADATA_TOKEN` – A unique authentication token for the current execution environment. Lambda generates this token automatically at initialization. Include it in all metadata API requests.

### Endpoint
<a name="metadata-endpoint-url"></a>

`GET http://${AWS_LAMBDA_METADATA_API}/2026-01-15/metadata/execution-environment`

### Request
<a name="metadata-endpoint-request"></a>

**Required headers:**
+ `Authorization` – The token value from the `AWS_LAMBDA_METADATA_TOKEN` environment variable with the Bearer scheme: `Bearer <token>`. This token-based authentication provides defense in depth protection against Server-Side Request Forgery (SSRF) vulnerabilities. Each execution environment receives a unique, randomly generated token at initialization.

### Response
<a name="metadata-endpoint-response"></a>

**Status:** `200 OK`

**Content-Type:** `application/json`

**Cache-Control:** `private, max-age=43200, immutable`

The response is immutable within an execution environment. Clients should cache the response and respect the `Cache-Control` TTL. For SnapStart functions, the TTL is reduced during initialization so that clients refresh metadata after restore when the execution environment may be in a different AZ. If you use Powertools, caching and SnapStart invalidation are handled automatically.

**Body:**

```
{
  "AvailabilityZoneID": "use1-az1"
}
```

The `AvailabilityZoneID` field contains the unique identifier for the Availability Zone where the execution environment is running.

**Note**  
Additional fields may be added to the response in future updates. Clients should ignore unknown fields and not fail if new fields appear.

### Error responses
<a name="metadata-endpoint-errors"></a>
+ **401 Unauthorized** – The `Authorization` header is missing or contains an invalid token. Verify you are passing `Bearer ${AWS_LAMBDA_METADATA_TOKEN}`.
+ **405 Method Not Allowed** – Request method is not `GET`.
+ **500 Internal Server Error** – Server-side processing error.