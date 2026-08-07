# TotalStack API Documentation

TotalStack is a fully functional local AWS cloud stack that emulates AWS
services (S3, Lambda, DynamoDB, etc.) for development and testing. It runs in
memory or in Docker, provides AWS-compatible APIs on `http://localhost:4566`,
and enables offline workflows, integration testing, and CI without calling
real AWS endpoints.

This document is the TotalStack-specific API and integration guide. It
complements the upstream LocalStack guides in `docs/` and the development
workflow documented in [../AGENTS.md](../AGENTS.md).

## Running the emulator

The recommended entry point is `make start` (in-memory, no Docker required):

```bash
# from the repository root (first time: make install-test)
make start
```

The emulator listens on `http://localhost:4566` (default). Verify it is up:

```bash
curl -s localhost:4566/_localstack/health
```

For the Docker-based workflow, see [../DOCKER.md](../DOCKER.md).

## Service coverage

TotalStack registers **69 AWS services**, each backed by a provider
implementation in `totalstack/services/<service>/provider.py` and wired in
`totalstack/providers.py` via the `@aws_provider` decorator:

| Aspect | Detail |
|--------|--------|
| Provider implementations | `totalstack/services/<service>/provider.py` (69 services) |
| Registration | `totalstack/providers.py` — `@aws_provider(api=..., name="totalstack")` |
| Handler decorator | `@handler` from `localstack.aws.api` (84 handlers across all providers) |
| Moto fallback | unimplemented operations fall back to Moto via `MotoFallbackDispatcher` |
| API spec source of truth | `specs/aws/<service>/` (Speclang specs; see [AGENTS.md](../AGENTS.md) for the spec → code pipeline) |

Service list (alphabetical): acm, amp, amplify, appconfig,
application-autoscaling, appmesh, appsync, athena, autoscaling, backup, batch,
bedrock, bedrock-agent, bedrock-runtime, cloudfront, cloudtrail, codeartifact,
codebuild, codedeploy, codepipeline, cognito-identity, comprehend, datasync,
dms, docdb, dynamodbstreams, ecr, efs, fis, forecast, frauddetector, fsx,
globalaccelerator, grafana, greengrassv2, identitystore, iot, iot-data,
kendra, keyspaces, lexv2-models, lexv2-runtime, lightsail, mediaconvert,
memorydb, mq, mwaa, neptune, network-firewall, opensearchserverless,
organizations, personalize, polly, quicksight, ram, rekognition, rolesanywhere,
s3tables, servicecatalog, sesv2, shield, signer, sso-admin, storagegateway,
textract, timestream-influxdb, transcribe, transfer, verifiedpermissions.

> Core services such as S3, Lambda, DynamoDB, SQS, SNS, Kinesis and
> CloudFormation are provided by the upstream LocalStack core
> (`localstack-core/`), which TotalStack builds on.

### Reference implementation: ACM

The **ACM** service (`totalstack/services/acm/provider.py`) is the reference
implementation for adding new services — see [../AGENTS.md](../AGENTS.md) and
`tests/aws/services/acm/test_acm.py` for the patterns it demonstrates
(`@handler` decorator, store-based state management, snapshot-parity testing,
PEM validation, auto-issuance).

## Integration guide

Point your AWS SDK (boto3) at the local endpoint. Credentials and region are
ignored by the emulator but must be present for the SDK:

```python
import boto3

client = boto3.client(
    "acm",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1",
)
```

Alternatively, use the `awslocal` CLI, which wraps the AWS CLI with the local
endpoint preconfigured.

### ACM walkthrough (reference implementation)

Request a certificate, list certificates, and delete it — the full lifecycle
covered by the ACM parity suite:

```python
import boto3

client = boto3.client(
    "acm",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1",
)

# Request a certificate (DNS validation; auto-issued once validated)
resp = client.request_certificate(
    DomainName="example.com",
    ValidationMethod="DNS",
    IdempotencyToken="walkthrough-001",
)
cert_arn = resp["CertificateArn"]

# List certificates (optionally filtered by key type)
listed = client.list_certificates(Includes={"keyTypes": ["RSA_2048"]})
print([c["CertificateArn"] for c in listed["CertificateSummaryList"]])

# Describe the certificate
desc = client.describe_certificate(CertificateArn=cert_arn)
print(desc["Certificate"]["Status"])  # PENDING_VALIDATION -> ISSUED

# Clean up
client.delete_certificate(CertificateArn=cert_arn)
```

The parity suite `tests/aws/services/acm/test_acm.py` runs against both the
emulator and real AWS (with `TEST_TARGET=AWS_CLOUD`), so the behavior above is
AWS-verified, including error cases (e.g. `ValidationException` on invalid PEM
input for `import_certificate`).

## Testing against TotalStack

- Run the assembled spec suite: `pytest specs/aws/.speclang/assembled/_tests`
- Run the ACM parity suite: `pytest tests/aws/services/acm/`
- Run parity tests against real AWS:
  `AWS_PROFILE=ls-sandbox TEST_TARGET=AWS_CLOUD SNAPSHOT_UPDATE=1 pytest <path>`

See [../AGENTS.md](../AGENTS.md) for test conventions (snapshot matching,
fixtures, transformers) and the development workflow.
