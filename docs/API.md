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

> **S3 `CreateBucket` duplicate semantics (AWS parity, verified 2026-08-27).**
> Creating a bucket that already exists and is owned by the same account is
> **idempotent (HTTP 200)** when the request targets `us-east-1` with no tags —
> this matches real AWS legacy behavior. For any other region (via
> `CreateBucketConfiguration.LocationConstraint`) or when the request carries
> tags, the second create raises **`BucketAlreadyOwnedByYou` (400)**. A bucket
> owned by a different account raises `BucketAlreadyExists`. Verified live
> against a plain `make start` emulator: `us-east-1` duplicate → 200, `eu-west-1`
> duplicate → `BucketAlreadyOwnedByYou`. Code: `localstack-core/localstack/
> services/s3/provider.py` (`create_bucket`).

### Reference implementation: ACM

The **ACM** service (`totalstack/services/acm/provider.py`) is the reference
implementation for adding new services — see [../AGENTS.md](../AGENTS.md) and
`tests/aws/services/acm/test_acm.py` for the patterns it demonstrates
(`@handler` decorator, store-based state management, snapshot-parity testing,
PEM validation, auto-issuance).

## Per-service operation reference

This section is the operation-level companion to the coverage list above. For
each documented service it lists every operation the TotalStack provider
exposes, whether it is implemented by a real TotalStack handler or handled by
Moto, and the error behavior a client can expect.

Status legend:

- **Implemented** — the operation has a real `@handler` in the service
  provider (`totalstack/services/<service>/provider.py`); state is managed by
  the provider's own store (assembled Speclang models under
  `specs/aws/.speclang/assembled/<service>/`).
- **Moto fallback** — no handler exists; the operation is forwarded to Moto by
  `MotoFallbackDispatcher` (state kept in Moto, Moto error shapes surface).
- Operations with neither path are rejected with `501 Not Implemented`.

Provider selection: TotalStack providers register as the `totalstack` variant
(`plux.ini`). ACM is the default provider for its service; for other services
the runtime default may be the upstream LocalStack core provider. Select the
TotalStack variant with `PROVIDER_OVERRIDE_<SERVICE>=totalstack`, e.g.
`PROVIDER_OVERRIDE_TRANSCRIBE=totalstack make start`.

> **Known runtime caveat (auto-wired providers).** The auto-wired providers
> (dynamodbstreams, s3tables, transcribe) attach their handlers under
> operation-derived attribute names, but LocalStack's `create_dispatch_table`
> resolves handlers by function name (`_w`). As of this writing, every
> operation of these three providers fails at runtime with
> `HTTP 500 InternalError: 'TotalStack…Provider' object has no attribute
> '_w'` (verified against a live emulator). The tables below therefore
> document the implemented surface and the store-level semantics from
> `models.code.py`; for dynamodbstreams and transcribe a plain `make start`
> serves the upstream core provider instead, and ACM is fully functional.

### acm

ACM (AWS Certificate Manager) is TotalStack's reference implementation: a
hand-written provider (`totalstack/services/acm/provider.py`) backed by the
`ACMStore` in `specs/aws/.speclang/assembled/acm/models.code.py`. All 16 ACM
API operations are implemented — there is no Moto fallback. Certificates are
stored in memory; `AMAZON_ISSUED` certificates are created in
`PENDING_VALIDATION` and flip to `ISSUED` lazily (on the next read) once the
moto `ACM_VALIDATION_WAIT` window (60 s default, `MOTO_ACM_VALIDATION_WAIT`)
has elapsed since creation. Errors are raised as typed service exceptions from
`localstack.aws.api.acm` (verified live: `ResourceNotFoundException` and
`ValidationException` both return HTTP 400 with the correct code).

| Operation | Status | Notable errors / behavior |
|---|---|---|
| RequestCertificate | Implemented | `LimitExceededException` past 1000 certs; creates `AMAZON_ISSUED` cert in `PENDING_VALIDATION`; DNS/EMAIL `DomainValidationOptions` (DNS emits a CNAME `ResourceRecord`); lazy auto-issuance to `ISSUED` after the validation window |
| ImportCertificate | Implemented | `ValidationException` for non-PEM certificate/private key, key/cert mismatch, expired or not-yet-valid dates, invalid chain; imported certs stored as `IMPORTED`/`ISSUED` |
| DescribeCertificate | Implemented | `ResourceNotFoundException` on unknown ARN; strips `Certificate`/`PrivateKey`/`CertificateChain`/`Tags` from the response |
| GetCertificate | Implemented | `ResourceNotFoundException` on unknown ARN; `InvalidStateException` unless status is `ISSUED` |
| ListCertificates | Implemented | Filters by `CertificateStatuses` and `Includes.keyTypes`; respects `MaxItems` (default 50) |
| DeleteCertificate | Implemented | `ResourceNotFoundException` on unknown ARN; `ResourceInUseException` while `InUseBy` is non-empty |
| ExportCertificate | Implemented | `ResourceNotFoundException` on unknown ARN; `InvalidStateException` unless `Type=PRIVATE` — no store path creates private certs, so export always errors in practice |
| RenewCertificate | Implemented | `ResourceNotFoundException` on unknown ARN; `InvalidStateException` unless `ISSUED`; resets to `PENDING_VALIDATION` with a `RenewalSummary` |
| RevokeCertificate | Implemented | `ResourceNotFoundException` on unknown ARN; sets `REVOKED`, `RevokedAt` and `RevocationReason` |
| UpdateCertificateOptions | Implemented | `ResourceNotFoundException` on unknown ARN; replaces the stored `Options` |
| AddTagsToCertificate | Implemented | `ResourceNotFoundException` on unknown ARN; `TooManyTagsException` beyond 50 tags; `InvalidTagException` for keys > 128 or values > 256 chars |
| ListTagsForCertificate | Implemented | `ResourceNotFoundException` on unknown ARN |
| RemoveTagsFromCertificate | Implemented | `ResourceNotFoundException` on unknown ARN; removes tags by `Key` |
| GetAccountConfiguration | Implemented | Returns stored `ExpiryEvents`/`OptInRegions` (empty defaults) |
| PutAccountConfiguration | Implemented | Replaces `ExpiryEvents`/`OptInRegions` |
| ResendValidationEmail | Implemented | `ResourceNotFoundException` on unknown ARN; `InvalidStateException` unless status is `PENDING_VALIDATION` |

### dynamodbstreams

DynamoDB Streams emulates the stream/shard/iterator read API over the DynamoDB
core service. The TotalStack provider is auto-wired
(`totalstack/services/dynamodbstreams/provider.py`) from the assembled store
in `specs/aws/.speclang/assembled/dynamodbstreams/models.code.py`; all 4 API
operations are implemented, none fall back to Moto. Streams are registered in
the store by the DynamoDB core service, and the store keeps a single shard per
stream with an empty record list. Note: a plain `make start` serves the
upstream LocalStack core provider for this service (that is what the parity
suite `tests/aws/services/dynamodbstreams/` exercises); select TotalStack's
variant with `PROVIDER_OVERRIDE_DYNAMODBSTREAMS=totalstack` (see caveat
above — the auto-wired variant currently 500s at runtime).

| Operation | Status | Notable errors / behavior |
|---|---|---|
| DescribeStream | Implemented | Store raises `ResourceNotFoundException` for unknown `StreamArn` (auto-wired wrapper converts exceptions to `CommonServiceException`) |
| ListStreams | Implemented | Optional `TableName` filter; returns stream summaries |
| GetShardIterator | Implemented | Store raises `ResourceNotFoundException` for unknown stream or shard; issues a fresh iterator id |
| GetRecords | Implemented | Store raises `ExpiredIteratorException` for unknown/expired iterators; otherwise returns `Records: []` with `NextShardIterator: null` (no data replay) |

### s3tables

S3 Tables emulates Iceberg table buckets, namespaces and tables. The TotalStack
provider is auto-wired (`totalstack/services/s3tables/provider.py`) from the
assembled store in `specs/aws/.speclang/assembled/s3tables/models.code.py`;
20 of the ~49 boto3 operations are implemented and none fall back to Moto
(there is no upstream core support and no Moto backend for s3tables). The
remaining boto3 operations (table bucket/table policies, data-transfer
access, etc.) are not served at all (`501`). Because the service is not in the
upstream AWS catalog, `scripts/patch-catalog.py` must be run once so the
runtime accepts s3tables requests — otherwise they are rejected with
`501 InternalFailure: the s3tables service is not supported by this version of
LocalStack` (verified live). Store error classes (`ConflictException`,
`NotFoundException`, …) are plain exceptions converted to
`CommonServiceException` by the auto-wired wrapper.

| Operation | Status | Notable errors / behavior |
|---|---|---|
| CreateTableBucket | Implemented | `ConflictException` on duplicate name; stores tags/encryption |
| GetTableBucket | Implemented | `NotFoundException` for unknown bucket ARN |
| DeleteTableBucket | Implemented | `NotFoundException` for unknown bucket ARN; cascades namespaces, tables, tags, encryption |
| ListTableBuckets | Implemented | `prefix`/`maxBuckets` filters; summaries only |
| CreateNamespace | Implemented | `NotFoundException` for unknown bucket; `ConflictException` on duplicate namespace |
| GetNamespace | Implemented | `NotFoundException` for unknown namespace |
| DeleteNamespace | Implemented | `NotFoundException` for unknown namespace |
| ListNamespaces | Implemented | `NotFoundException` for unknown bucket; `prefix`/`maxNamespaces` filters |
| CreateTable | Implemented | `NotFoundException` for unknown bucket or namespace; `ConflictException` on duplicate table |
| GetTable | Implemented | `NotFoundException` for unknown table |
| DeleteTable | Implemented | `NotFoundException` for unknown table |
| ListTables | Implemented | `NotFoundException` for unknown bucket; `prefix`/`maxTables` filters |
| RenameTable | Implemented | `NotFoundException` for unknown source table; `ConflictException` if the new name is taken |
| GetTableEncryption | Implemented | `NotFoundException` for unknown table; defaults `sseAlgorithm` to `AES256` |
| GetTableBucketEncryption | Implemented | `NotFoundException` for unknown bucket; defaults `sseAlgorithm` to `AES256` |
| GetTableMaintenanceConfiguration | Implemented | `NotFoundException` for unknown table; empty configuration default |
| GetTableBucketMaintenanceConfiguration | Implemented | `NotFoundException` for unknown bucket; empty configuration default |
| TagResource | Implemented | Upserts the tag map; no resource existence check |
| UntagResource | Implemented | Removes tag keys; no resource existence check |
| ListTagsForResource | Implemented | Returns the tag list; no resource existence check |

### transcribe

Transcribe emulates speech-to-text job and vocabulary management. The
TotalStack provider is auto-wired (`totalstack/services/transcribe/provider.py`)
from the assembled store in `specs/aws/.speclang/assembled/transcribe/models.code.py`:
18 of the 43 API operations are implemented (vocabularies, vocabulary filters,
transcription jobs, language models); the remaining 25 (Call Analytics,
Medical Scribe/Transcription, tagging) are Moto fallback. Transcription jobs
"complete" immediately with status `COMPLETED` — no real transcription is
performed and no output is produced. Store error classes (`ConflictException`,
`NotFoundException`, `BadRequestException`, …) are plain exceptions converted
to `CommonServiceException` by the auto-wired wrapper. Note: a plain
`make start` serves the upstream LocalStack core provider (moto + vosk) for
this service — that is what the parity suite `tests/aws/services/transcribe/`
exercises; select TotalStack's variant with
`PROVIDER_OVERRIDE_TRANSCRIBE=totalstack` (see caveat above — the auto-wired
variant currently 500s at runtime).

| Operation | Status | Notable errors / behavior |
|---|---|---|
| CreateVocabulary | Implemented | `ConflictException` on duplicate name |
| GetVocabulary | Implemented | `NotFoundException` for unknown vocabulary |
| UpdateVocabulary | Implemented | `NotFoundException` for unknown vocabulary; updates fields and `LastModifiedTime` |
| DeleteVocabulary | Implemented | `NotFoundException` for unknown vocabulary |
| ListVocabularies | Implemented | `StateEquals`/`NameContains` filters |
| CreateVocabularyFilter | Implemented | `ConflictException` on duplicate filter name |
| GetVocabularyFilter | Implemented | `NotFoundException` for unknown filter |
| UpdateVocabularyFilter | Implemented | `NotFoundException` for unknown filter; updates fields and `LastModifiedTime` |
| DeleteVocabularyFilter | Implemented | `NotFoundException` for unknown filter |
| ListVocabularyFilters | Implemented | `NameContains` filter |
| StartTranscriptionJob | Implemented | `ConflictException` on duplicate job name; jobs complete immediately with status `COMPLETED` (no real transcription) |
| GetTranscriptionJob | Implemented | `NotFoundException` for unknown job |
| ListTranscriptionJobs | Implemented | `Status`/`JobNameContains` filters |
| DeleteTranscriptionJob | Implemented | Idempotent — deleting a missing job is a no-op |
| CreateLanguageModel | Implemented | `ConflictException` on duplicate model name |
| DescribeLanguageModel | Implemented | `NotFoundException` for unknown model |
| ListLanguageModels | Implemented | `StatusEquals`/`NameContains` filters |
| DeleteLanguageModel | Implemented | Idempotent — deleting a missing model is a no-op |
| CreateCallAnalyticsCategory | Moto fallback | State kept in Moto; Moto error shapes |
| CreateMedicalVocabulary | Moto fallback | State kept in Moto; Moto error shapes |
| DeleteCallAnalyticsCategory | Moto fallback | State kept in Moto; Moto error shapes |
| DeleteCallAnalyticsJob | Moto fallback | State kept in Moto; Moto error shapes |
| DeleteMedicalScribeJob | Moto fallback | State kept in Moto; Moto error shapes |
| DeleteMedicalTranscriptionJob | Moto fallback | State kept in Moto; Moto error shapes |
| DeleteMedicalVocabulary | Moto fallback | State kept in Moto; Moto error shapes |
| GetCallAnalyticsCategory | Moto fallback | State kept in Moto; Moto error shapes |
| GetCallAnalyticsJob | Moto fallback | State kept in Moto; Moto error shapes |
| GetMedicalScribeJob | Moto fallback | State kept in Moto; Moto error shapes |
| GetMedicalTranscriptionJob | Moto fallback | State kept in Moto; Moto error shapes |
| GetMedicalVocabulary | Moto fallback | State kept in Moto; Moto error shapes |
| ListCallAnalyticsCategories | Moto fallback | State kept in Moto; Moto error shapes |
| ListCallAnalyticsJobs | Moto fallback | State kept in Moto; Moto error shapes |
| ListMedicalScribeJobs | Moto fallback | State kept in Moto; Moto error shapes |
| ListMedicalTranscriptionJobs | Moto fallback | State kept in Moto; Moto error shapes |
| ListMedicalVocabularies | Moto fallback | State kept in Moto; Moto error shapes |
| ListTagsForResource | Moto fallback | State kept in Moto; Moto error shapes |
| StartCallAnalyticsJob | Moto fallback | State kept in Moto; Moto error shapes |
| StartMedicalScribeJob | Moto fallback | State kept in Moto; Moto error shapes |
| StartMedicalTranscriptionJob | Moto fallback | State kept in Moto; Moto error shapes |
| TagResource | Moto fallback | State kept in Moto; Moto error shapes |
| UntagResource | Moto fallback | State kept in Moto; Moto error shapes |
| UpdateCallAnalyticsCategory | Moto fallback | State kept in Moto; Moto error shapes |
| UpdateMedicalVocabulary | Moto fallback | State kept in Moto; Moto error shapes |

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
