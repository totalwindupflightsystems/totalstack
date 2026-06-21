# TotalStack Service Classification

> Master strategy. Categorizes every AWS service: pure-API, OSS-wrapper, or skip.
> Drives the cron's Phase 0 behavior — OSS wrappers get BOTH AWS docs + upstream OSS docs.
> Last updated: June 2026. Cross-reference: `oss-upstream-docs.yaml`.

---

## Summary

| Category | Count | Strategy |
|----------|-------|----------|
| **Tier 1 — Done** | 19 | Already built. Maintain. |
| **Tier 2 — Pure AWS API** | ~28 | Build from AWS API Reference markdown + botocore service-2.json |
| **Tier 2 — OSS Wrapper** | ~7 | Build AWS API layer + include upstream OSS API docs for version-bump automation |
| **Tier 3 — Nice to have** | ~30 | Build when needed |
| **Tier 4 — Skip** | ~110 | Deprecated, hardware, management wrappers, ultra-niche |
| **Gray zone** | ~180 | Build if a user/customer asks, otherwise skip |
| **TOTAL worth building** | **~84** | 19 done + ~65 more |

---

## The Right Number: 80-100 Services

After auditing all ~377 services, the "right number" for TotalStack is **80-100 services**:

- **19 already done** — the table-stakes services (S3, Lambda, DynamoDB, etc.)
- **~35 Tier 2** — services that cover ~95% of CI/CD and local dev workflows
- **~30 Tier 3** — services used by some teams, built as needed
- **~110 Tier 4** — SHOULD NOT build: deprecated, hardware, management wrappers, ultra-niche
- **~180 gray zone** — everything else. Build if someone asks, otherwise don't.

Building all 377 is a waste of tokens. Nobody needs `ManagedBlockchain` or `B2BI` or `ARC Zonal Shift` in a local emulator.

---

## OSS Wrapper Services — Version-Bump Automation

For services that wrap open source tools, we store the upstream OSS API docs alongside the AWS API docs. When the upstream OSS releases a new version:

1. Update the version in `oss-upstream-docs.yaml`
2. Re-fetch the upstream OSS docs
3. SpecLang cascade regenerates code from updated docs
4. Integration tests catch regressions

No manual code changes needed — the docs ARE the spec.

### OSS Wrappers (build with upstream docs)

| AWS Service | Upstream OSS | Upstream Docs URL | Notes |
|-------------|-------------|-------------------|-------|
| **elasticache** (Redis) | Redis OSS | https://redis.io/docs/latest/ | Redis command set |
| **elasticache** (Memcached) | Memcached | https://github.com/memcached/memcached/blob/master/doc/protocol.txt | Wire protocol |
| **memorydb** | Redis OSS | https://redis.io/docs/latest/ | Durable Redis-compatible |
| **mq** (ActiveMQ) | Apache ActiveMQ | https://activemq.apache.org/components/classic/documentation/ | OpenWire/STOMP/AMQP/MQTT |
| **mq** (RabbitMQ) | RabbitMQ | https://www.rabbitmq.com/docs | AMQP 0-9-1 + HTTP API |
| **kafka** (MSK) | Apache Kafka | https://kafka.apache.org/documentation/ | Native Kafka APIs |
| **es** / **opensearch** | OpenSearch | https://docs.opensearch.org/latest/api-reference/ | REST API |
| **keyspaces** | Apache Cassandra | https://cassandra.apache.org/doc/latest/ | CQL 3.11 |
| **neptune** (Gremlin) | Apache TinkerPop | https://tinkerpop.apache.org/docs/current/reference/ | Property graph |
| **neptune** (openCypher) | openCypher | https://opencypher.org/ | Graph queries |
| **neptune** (SPARQL) | W3C SPARQL | https://www.w3.org/TR/sparql11-query/ | RDF queries |
| **emr** / **emr-serverless** | Apache Spark, Hive, Trino, Flink | Multiple (see `oss-upstream-docs.yaml`) | Big data engines |
| **mwaa** | Apache Airflow | https://airflow.apache.org/docs/ | REST API |
| **rds** (MySQL) | MySQL | https://dev.mysql.com/doc/ | Wire protocol |
| **rds** (PostgreSQL) | PostgreSQL | https://www.postgresql.org/docs/ | Wire protocol |
| **timestream-influxdb** | InfluxDB | https://docs.influxdata.com/influxdb/ | 2.x/3.x APIs |
| **amp** | Prometheus | https://prometheus.io/docs/prometheus/latest/querying/api/ | Remote write/query |
| **grafana** | Grafana | https://grafana.com/docs/grafana/latest/developer-resources/api-reference/ | HTTP API |
| **eks** | Kubernetes | https://kubernetes.io/docs/reference/ | K8s API |
| **kinesisanalytics** / **flink** | Apache Flink | https://nightlies.apache.org/flink/flink-docs-stable/ | Stream processing |
| **glue** (Spark) | Apache Spark | https://spark.apache.org/docs/latest/ | ETL engine |
| **glue** (Ray) | Ray | https://docs.ray.io/ | Distributed compute |
| **docdb** | MongoDB wire protocol | https://www.mongodb.com/docs/ | API-compatible, proprietary engine |
| **aurora** (MySQL/PostgreSQL) | MySQL / PostgreSQL wire protocol | Same as RDS above | Proprietary engine |

### Borderline — OSS-compatible API but proprietary engine

| AWS Service | Compatible With | Strategy |
|-------------|-----------------|----------|
| **docdb** | MongoDB wire protocol | Build AWS API layer. MongoDB wire protocol docs inform store behavior. |
| **aurora** (MySQL/PostgreSQL) | MySQL/PostgreSQL wire protocol | Same as RDS — wire protocol compatibility, not a separate engine to emulate. |
| **dax** | DynamoDB API (NOT Memcached) | Proprietary read-through cache. NOT an OSS wrapper. Build as pure AWS API. |

---

## Tier 2 — Pure AWS API Services (build from AWS docs)

These are the services worth building next. All use the standard pipeline: AWS API Reference markdown → botocore service-2.json → SpecLang.

### Critical (8 services to unlock most users)

| # | Service | Ops | Complexity | Why |
|---|---------|-----|------------|-----|
| 1 | **rds** | ~50 | MODERATE | #1 most-requested; RDS PostgreSQL/MySQL |
| 2 | **cloudfront** | ~30 | MODERATE | CDN; S3+CloudFront is most common static hosting pattern |
| 3 | **cloudtrail** | ~15 | SIMPLE | API audit logs; critical for IAM testing |
| 4 | **cognito-identity** | ~10 | MODERATE | Identity pools; Cognito User Pools already done |
| 5 | **ecr** | ~15 | SIMPLE | Container registry; required by ECS/EKS |
| 6 | **application-autoscaling** | ~10 | SIMPLE | Dynamic scaling for ECS, DynamoDB, etc. |
| 7 | **ssm** (Parameter Store) | ~10 | SIMPLE | Parameter Store heavily used in CI/CD |
| 8 | **autoscaling** | ~15 | MODERATE | EC2 auto-scaling groups |

### High Priority (12 more)

| # | Service | Ops | Complexity | Why |
|---|---------|-----|------------|-----|
| 9 | kinesis | ~15 | COMPLEX | Real-time streaming |
| 10 | glue | ~40 | MODERATE | ETL + Data Catalog |
| 11 | efs | ~15 | MODERATE | NFS for Lambda/ECS/EC2 |
| 12 | acm | ~10 | SIMPLE | TLS certificates |
| 13 | eks | ~20 | COMPLEX | Kubernetes — but may be better as passthrough to local k8s |
| 14 | codepipeline | ~15 | MODERATE | CI/CD pipeline orchestration |
| 15 | batch | ~20 | MODERATE | Batch computing |
| 16 | docdb | ~30 | MODERATE | MongoDB API-compatible |
| 17 | sesv2 | ~20 | MODERATE | Email sending |
| 18 | s3tables | ~15 | SIMPLE | Iceberg tables |
| 19 | mq | ~20 | MODERATE | ActiveMQ/RabbitMQ |
| 20 | backup | ~15 | SIMPLE | Centralized backup |

### Medium Priority (15 more)

| # | Service | Ops | Complexity | Why |
|---|---------|-----|------------|-----|
| 21 | redshift | ~40 | MODERATE | Data warehousing |
| 22 | elasticache | ~30 | MODERATE | Redis/Memcached (OSS wrapper — needs upstream docs) |
| 23 | emr | ~30 | COMPLEX | Big data (OSS wrapper) |
| 24 | mwaa | ~20 | MODERATE | Managed Airflow (OSS wrapper) |
| 25 | kafka | ~30 | COMPLEX | MSK (OSS wrapper — needs Kafka docs) |
| 26 | es / opensearch | ~20 | MODERATE | OSS wrapper |
| 27 | appsync | ~20 | MODERATE | GraphQL |
| 28 | appconfig | ~10 | SIMPLE | Feature flags |
| 29 | bedrock | ~30 | MODERATE | AI/ML foundation models |
| 30 | bedrock-agent | ~15 | MODERATE | AI agents |
| 31 | bedrock-runtime | ~5 | SIMPLE | Model invocation |
| 32 | memorydb | ~20 | MODERATE | Redis-compatible DB (OSS wrapper) |
| 33 | keyspaces | ~20 | MODERATE | Cassandra (OSS wrapper) |
| 34 | timestream-influxdb | ~15 | MODERATE | InfluxDB (OSS wrapper) |
| 35 | grafana | ~15 | SIMPLE | Grafana (OSS wrapper) |

---

## Tier 3 — Nice to Have (build as needed, ~30 services)

| Service | Category | Notes |
|---------|----------|-------|
| appmesh | Networking | Service mesh |
| amplify | Frontend | Hosting + CI/CD |
| sagemaker | ML | Very complex; rarely tested locally |
| comprehend | AI/ML | NLP service |
| polly | AI/ML | Text-to-speech |
| transcribe | AI/ML | Speech-to-text |
| lexv2-models / lexv2-runtime | AI/ML | Chatbot |
| iot / iot-data | IoT | Device management |
| greengrassv2 | IoT | Edge runtime |
| fis | Resilience | Chaos engineering |
| dms | Migration | Database migration |
| transfer | Storage | SFTP/FTPS (already done?) |
| ram | IAM | Cross-account sharing |
| sso-admin / identitystore | IAM | Enterprise SSO |
| fsx | Storage | Managed file systems |
| globalaccelerator | Networking | Network optimization |
| network-firewall | Networking | Network filtering |
| datasync | Migration | Data transfer |
| storagegateway | Storage | On-prem bridge |
| verifiedpermissions | Security | Cedar policy engine |
| signer | Security | Code signing |
| rolesanywhere | Security | IAM roles anywhere |
| amp | Monitoring | Prometheus (OSS wrapper) |
| kendra | AI/ML | Enterprise search |
| quicksight | Analytics | BI dashboard |
| forecast | AI/ML | Time-series forecasting |
| frauddetector | AI/ML | Fraud detection |
| personalize | AI/ML | Recommendation engine |
| proton | DevOps | Service templates |
| connect | Call center | Contact center |

---

## Tier 4 — SKIP (~110 services)

### A. Deprecated / End of Life (~55)

`sdb` (SimpleDB), `cloudsearch`, `cloud9`, `forecast`, `datapipeline`, `codecommit` (Jun 2025), `codestar-connections`, `codestar-notifications`, `cognito-sync`, `iot-events`, `simspaceweaver`, `panorama`, `voice-id`, `inspector` (classic), `clouddirectory`, `codecatalyst`, `importexport`, `snowball`, `machinelearning`, `workdocs`, `worklink`, `opsworks`, `deepcomposer`, `deeplens`, `elastictranscoder`, `mediastore`, `lookoutequipment` (Metrics/Vision), `nimble`, `sumerian`, `lumberyard`, `mobile`, `serverlessrepo`, `sms`, `iotanalytics`, `iot1click`, `iotthingsgraph`, `iotfleethub`, `glacier`, `waf` (Classic), `evidently`, `kinesisanalytics` (SQL), `lakeformation` (Governed Tables), `bugbust`, `private5g`, `datasync-discovery`, `nice-enginframe`, `mainframe-modernization`, `robomaker`, `snowmobile`, `timestream` (LiveAnalytics, Oct 2025)

### B. Physical Hardware Required (~9)

`snowball`, `outposts`, `groundstation`, `braket`, `devicefarm`, `directconnect`, `interconnect`, `gamelift` (real-time servers; management plane could be built but emulating game servers is infeasible)

### C. Management Plane Wrappers (~14)

`controltower`, `servicecatalog-appregistry`, `resource-groups`, `support`, `account`, `ce` (Cost Explorer), `trustedadvisor`, `license-manager`, `budgets`, `compute-optimizer`, `bcm-pricing-calculator`, `cur` (Cost & Usage Report), `health`, `iq`

### D. Ultra-Niche (<0.1% adoption, ~30)

`managedblockchain`, `kendra-ranking`, `comprehendmedical`, `healthlake`, `healthimaging`, `omics`, `connect-*` (call center suite), `appflow`, `b2bi`, `supplychain`, `deadline`, `finspace`, `entityresolution`, `cleanrooms`, `dataexchange`, `datazone`, `databrew`, `customer-profiles`, `chime-*`, `wickr`, `workmail`, `proton`, `iottwinmaker`, `iotsitewise`, `iotfleetwise`, `arc-zonal-shift`, `arc-region-switch`, `tnb` (Telco Network Builder)

---

## Gray Zone (~180 services)

Everything not listed above. These are services that:
- Aren't widely used enough to be Tier 2/3
- Aren't deprecated/hardware/wrapper enough to be Tier 4
- Could be built if a user asks, but there's no reason to pre-build them

Examples: `apprunner`, `appstream`, `amplifybackend`, `apigatewaymanagementapi`, `apigatewayv2`, `backup-gateway`, `chatbot`, `devops-guru`, `dlm`, `drs`, `ds`, `ebs`, `ecr-public`, `elasticbeanstalk`, `elb` / `elbv2` (maybe Tier 2?), `fms`, `fsx`, `guardduty`, `imagebuilder`, `inspector2`, `ivs`, `kafkaconnect`, `lex-models`, `license-manager-linux-subscriptions`, `lightsail` (already done), `macie2`, `mediaconnect`, `medialive`, `mediapackage*`, `mediatailor`, `networkmanager`, `osis`, `payment-cryptography`, `pipes`, `proton`, `qbusiness`, `qconnect`, `rds-data`, `redshift-data`, `redshift-serverless`, `resiliencehub`, `route53-recovery-*`, `route53domains`, `route53profiles`, `rum`, `s3outposts`, `sagemaker-*`, `savingsplans`, `schemas`, `securityhub`, `securitylake`, `service-quotas`, `servicediscovery`, `signer`, `snow-device-management`, `ssm-contacts`, `ssm-incidents`, `ssm-sap`, `sso`, `synthetics`, `timestream-query`, `timestream-write`, `vpc-lattice`, `wellarchitected`, `workspaces*`, and many more.

---

## Cron Job Integration

The `totalstack-service-builder` cron must check this classification before building:

```
Phase 0 — CLASSIFY
  1. Look up service in SERVICE-CLASSIFICATION.md
  2. If TIER 4 → skip, mark as "skipped" in queue
  3. If OSS WRAPPER → download AWS API docs + upstream OSS docs
  4. If PURE API → download AWS API docs only
  5. Proceed to Phase 1 (markdown extraction)
```

### OSS Wrapper Cron Behavior

For OSS-wrapped services, Phase 1 downloads BOTH:
1. AWS API Reference markdown (like all services)
2. Upstream OSS API docs from the URL in `oss-upstream-docs.yaml`

Both go into `specs/aws/{service}/docs/` with different prefixes:
- `API_{Op}.spec.md` — AWS management plane operations
- `UPSTREAM_{Project}_{Version}.spec.md` — upstream OSS API reference

When a version bump happens:
1. Human updates the version in `oss-upstream-docs.yaml`
2. Next cron run detects the version change
3. Re-downloads upstream docs for the new version
4. SpecLang cascade regenerates code from updated docs
5. Integration tests pass → commit → done

No code changes. Just doc version bumps.

---

## Sources

1. LocalStack v4.14.0 source code analysis (35 ASF providers, 2 forward_request, 21 moto fallback)
2. Datadog State of Serverless (top 10 services = 89% of API calls)
3. AWS Service Lifecycle announcements (Jul 2024, May 2025, Oct 2025)
4. AWS API Reference markdown availability (200+ services)
5. Botocore service-2.json analysis (all ~377 AWS services)
6. OSS upstream API docs research (25+ clear wrappers identified)
7. Community demand analysis (Reddit, GitHub, LocalStack issues)
8. Jeff Barr AWS blog (deprecated services official announcements)
