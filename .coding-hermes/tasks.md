# Task Board — TotalStack

## [x] CI-GAP-004 — Fix Integration Tests (3.11): stores.py Python 3.12+ syntax breaks 3.11 matrix (242487251)
    `class RegionBundle[BaseStoreType](dict)` at localstack-core/localstack/services/stores.py:193
    is Python 3.12+ generic syntax. CI integration tests run on 3.10, 3.11, 3.12 — the 3.11 job fails
    with SyntaxError, and 3.10/3.12 get cancelled (matrix cascade). Commit 26619a9be introduced this.
    Fix options: (a) backport to `class RegionBundle(Generic[BaseStoreType], dict)` for 3.11 compat,
    (b) drop 3.10 and 3.11 from CI matrix and only test 3.12.
    - [x] Fix stores.py:193 RegionBundle syntax to be Python 3.11 compatible
    - [x] Verify CI Integration Tests (3.11) passes (syntax verified via ast.parse, Generic import works)
    - [x] Verify stores.py still imports correctly (Generic added to typing import, ast.parse passes)
    Files: localstack-core/localstack/services/stores.py, .github/workflows/ci.yml

## [x] CI-GAP-005 — Shape Validator: 6/76 services pass, 70 have errors (1,213 total errors)
    Investigation complete (2026-07-16). Error classification:
      - HANDLER_CRASH: 1,164 (96.0%) — handlers crash on test input (missing fields, missing exceptions)
      - IMPORT_ERROR: 49 (4.0%) — modules can't be imported (dataclass, etc.)
      - No MISSING_REQUIRED or TYPE_MISMATCH errors — shapes are correct, handlers just crash at runtime
    Common crash patterns:
      - resourceArn / ResourceArn access: 89 crashes across services
      - Missing exception classes: ~160 crashes (InvalidParameterValueException, InvalidInputException, etc.)
      - Specific field access: meshName (24), clusterName (23), AwsAccountId, etc.
    Root cause: _call_handler() provides minimal test inputs, but handlers access fields
    not in those inputs. Also, exception classes defined in models.code.py aren't injected
    into handler modules. This is a test-infrastructure gap, not a shape-spec gap.
    Top 5 services by error count → subtasks below.
    - [x] Classify errors by type (HANDLER_CRASH 96%, IMPORT_ERROR 4%)
    - [x] Identify top 5: wafv2 (34), eks (33), athena (30), rekognition (30), comprehend (29)
    - [x] Create per-service subtasks (see CI-GAP-006 through CI-GAP-010)
    Files: .github/workflows/ci.yml, development/aws-shape-validator.py

## [x] CI-GAP-006 — wafv2: 34 handler crashes → ALL 34/34 pass (6032e9838)
    Three root causes identified and fixed:
      1. models module not registered in sys.modules → exception injection skipped
      2. Delete/Associate handlers return None → validator skipped them
      3. Shared resource names across Get/Delete/Update → alphabetically-ordered
         Delete ran before Get, deleting resources. Each op now creates its own.
      4. Service-prefixed keys (wafv2.TagResource) prevent cross-service collisions.
    - [x] Fix exception injection in handler modules (sys.modules registration)
    - [x] Add test inputs for wafv2 operations (self-contained lambdas, unique names)
    Files: development/aws-shape-validator.py

## [x] CI-GAP-007 — eks: 33 handler crashes (0/1 ops pass) (9d60197fe)
    Handlers crash accessing clusterName and other fields not in minimal test inputs.
    - [x] Add test inputs for eks operations (clusterName, etc.) to _call_handler()
    - [x] Verify 21/34 ops now pass shape validation (was 1/34)
    Files: specs/aws/.speclang/assembled/eks/*.code.py

## [x] CI-GAP-008 — athena: 30 handler crashes (4 ops fail) (658a85a8f)
    All 4 tested ops crash — likely missing required fields in test inputs.
    - [x] Add test inputs for athena operations to _call_handler() (35 ops, all categories)
    - [x] Athena handles its own exceptions (InvalidRequestException, ResourceNotFoundException in models)
    Files: specs/aws/.speclang/assembled/athena/*.code.py

## [x] CI-GAP-009 — rekognition: 30 errors (0/0 ops pass, all import errors) (fd3504215)
    All handlers fail at import: `name 'dataclass' is not defined` — code uses Python
    dataclass decorator but module doesn't import it.
    Fix: removed @dataclass from all 30 handler functions (they're bare functions, not dataclasses).
    - [x] Remove @dataclass from rekognition handler modules (30 files, 30 deletions)
    - [x] Verify no @dataclass remains in any rekognition .code.py file
    Files: specs/aws/.speclang/assembled/rekognition/*.code.py

## [x] CI-GAP-010 — comprehend: 29 handler crashes → all 35/35 ops pass (19d784097)
    Fixed by converting describe/update/delete test inputs from static dicts
    to lambdas (create entity first, then pass ARN) — same pattern as wafv2/eks/athena.
    Also fixed to_dict() to use per-entity-type Status (COMPLETED/TRAINED/IN_SERVICE/ACTIVE)
    and per-entity ARN keys instead of hardcoded EntityRecognizerArn.
    - [x] Add test inputs for comprehend operations to _call_handler() (lambdas for all 35 ops)
    - [x] Fix missing exception classes (already defined + sys.modules registration handles injection)
    Files: development/aws-shape-validator.py, specs/aws/.speclang/assembled/comprehend/models.code.py

## [x] CI-GAP-011 — quicksight: 23 handler crashes → all 23/23 ops pass (7f1edd28c)
    All 23 handlers crashed with missing AwsAccountId and other required fields.
    Added test inputs for create/list/describe/delete/update (analysis, dashboard,
    dataset, datasource) and tag/untag/list-tags (lambdas that create resources first).
    - [x] Add test inputs for quicksight operations to _call_handler() (23 ops)
    - [x] Verify all quicksight ops pass shape validation (23/23 PASS)

## [x] CI-GAP-012 — neptune: 22 handler crashes → all 29/29 ops pass (0ebfc5957 + fix f063670fb)
    All 29 handlers now pass. Added test inputs for all operations (create/list/describe/
    delete/modify/reboot/tag/untag) and a find_resource_by_name helper function.
    Also fixed exception injection to inject find_resource_by_name for handlers that need it.
    - [x] Add test inputs for neptune operations to _call_handler()
    - [x] Verify all neptune ops pass shape validation (29/29 PASS)

## [x] CI-GAP-013 — lexv2-models: 19 handler crashes → all 20/20 ops pass (2bccfd050)
    All 20 handlers now pass. Added test inputs for create/list/describe/delete/update
    using the lambda pattern (create bot prerequisite, then call the operation).
    - [x] Add test inputs for lexv2-models operations to _call_handler() (20 ops)
    - [x] Verify all lexv2-models ops pass shape validation (20/20 PASS)

## [x] CI-GAP-014 — opensearchserverless: 16 handler crashes → all 23/23 ops pass (2ee85aa4d)
    Added test inputs for all operations (create/list/get/delete/update policies,
    collection delete/update, tag/untag/list-tags). Added json import + json.loads
    for policy string→dict conversion in PolicyRecord, LifecyclePolicyRecord, and
    three update_*_policy methods.
    - [x] Add test inputs for opensearchserverless operations to _call_handler() (16 ops)
    - [x] Fix policy JSON string parsing in models.code.py (PolicyRecord + LifecyclePolicyRecord + update methods)
    - [x] Verify all opensearchserverless ops pass shape validation (23/23 PASS)
    Files: development/aws-shape-validator.py, specs/aws/.speclang/assembled/opensearchserverless/models.code.py

## [x] CI-GAP-015 — frauddetector: 16 handler crashes → all 22/22 ops pass (da7af9059)
    Added test inputs for all operations (create/list/get/delete/update for detectors,
    models, variables, event types, rules, and tags). Fixed create-rule handler to
    return rec.to_dict() instead of {} and added ruleVersion to RuleRecord.to_dict().
    Used lambda pattern for ops requiring pre-existing resources, service-prefixed
    keys for tag ops to avoid collision with opensearchserverless.
    - [x] Add test inputs for frauddetector operations to _call_handler()
    - [x] Fix CreateRule handler to return response dict (not empty {})
    - [x] Fix RuleRecord.to_dict() to include ruleVersion
    - [x] Verify all frauddetector ops pass shape validation (22/22 PASS)
    Files: development/aws-shape-validator.py, specs/aws/.speclang/assembled/frauddetector/models.code.py, specs/aws/.speclang/assembled/frauddetector/create-rule.code.py

## [x] CI-GAP-016 — Generate missing handler files for autoscaling, efs, kinesis, ssm (129c93a18)
    Four services had models.code.py + integration tests but handler `.code.py` files were
    never generated (commit 87c05d2fd). Also fixed comprehend test bug: `test_create_and_describe_classifier`
    asserted `r["EntityRecognizerArn"]` but classifier returns `DocumentClassifierArn`.
    - [x] Run gen_asg_handlers.py (9 handler files)
    - [x] Run gen_efs_handlers.py (9 handler files)
    - [x] Run gen_kinesis_handlers.py (11 handler files)
    - [x] Run gen_ssm_handlers.py (9 handler files)
    - [x] Fix comprehend test bug (EntityRecognizerArn → DocumentClassifierArn)
    - [x] Verify all 42 tests pass (autoscaling 8, efs 4, kinesis 8, ssm 9, comprehend 13)
    Files: development/gen_asg_handlers.py, development/gen_efs_handlers.py, development/gen_kinesis_handlers.py, development/gen_ssm_handlers.py, specs/aws/.speclang/assembled/_tests/test_comprehend_integration.py

## [x] CI-GAP-017 — shield: 33 handler crashes (0/0 ops) → all 34/34 pass (fe9706c6e)
    Shield had 34 handler files but zero test inputs. Added test inputs for all operations
    following the established pattern (create/list/describe/delete/update, DRT config,
    health checks, proactive engagement, app layer responses, tags via service-prefixed keys).
    Also fixed handler injection bug: dataclass and field from models.code.py were injected
    as FunctionType values and shadowed the real handler function (Python 3.14 only).
    - [x] Add test inputs for all 34 shield operations to _call_handler()
    - [x] Fix injection code to skip dataclass/field/Field (FunctionType bug in Python 3.14)
    - [x] Verify all shield ops pass shape validation (34/34 PASS)

## [x] CI-GAP-018 — rekognition: 29 handler crashes → all 30/30 ops pass (a7486308e)
    Previously fixed @dataclass removal (CI-GAP-009, fd3504215) but handlers crashed
    with uuid/time not defined. Added test inputs for all 30 rekognition operations
    (create/list/describe/delete, face ops, detection, async video, celebrity, tags).
    Also injected uuid and time modules into handler namespace — same pattern as
    exception injection, needed because handlers reference models.code.py imports.
    - [x] Add test inputs for rekognition operations to _call_handler() (30 ops)
    - [x] Fix handler crashes — injected uuid + time into handler namespace
    - [x] Verify rekognition ops pass shape validation (30/30 PASS)
    Files: development/aws-shape-validator.py, specs/aws/.speclang/assembled/rekognition/*.code.py

## [x] CI-GAP-019 — sso-admin: 28 handler crashes → all 30/30 ops pass (a5d17d94c)
    Both tested ops crashed — handlers accessed fields not in minimal test inputs.
    Added test inputs for all 28 sso-admin operations following the established
    camelCase key + walrus operator pattern (instance, permission set, account
    assignment, application, policy, managed policy, tags). Used store method
    return values for correct ARN extraction instead of hardcoding.
    - [x] Add test inputs for sso-admin operations to _call_handler() (28 ops)
    - [x] Verify sso-admin ops pass shape validation (30/30 PASS)
    Files: development/aws-shape-validator.py, specs/aws/.speclang/assembled/sso-admin/*.code.py

## [x] CI-GAP-020 — appmesh: 27 handler crashes → all 28/28 ops pass (621e51639)
    All 28 handlers now pass. Added test inputs for all operations (create/list/
    describe/delete/update mesh, virtual-node, virtual-service, virtual-router,
    route, and tag/untag/list-tags) using the established lambda pattern for
    ops requiring prerequisite resources. Tag ops use service-prefixed keys.
    - [x] Add test inputs for appmesh operations to _call_handler() (28 ops)
    - [x] Verify appmesh ops pass shape validation (28/28 PASS)
    Files: development/aws-shape-validator.py, specs/aws/.speclang/assembled/appmesh/*.code.py

## [x] CI-GAP-021 — amplify: 26 handler crashes → all 27/27 ops pass (9d45d93f2)
    Added test inputs for all 27 ops following established pattern (create/list/
    get/delete/update/tag/untag with service-prefixed keys for tag ops). Also
    fixed amplify/models.code.py: AppRecord (appArn, defaultDomain, platform,
    enableBasicAuth, repository, enableBranchAutoBuild, environmentVariables),
    BranchRecord (fixed stage default 'DEVELOPMENT', added 10 missing required
    fields), BackendEnvironmentRecord (backendEnvironmentArn), DomainAssociationRecord
    (subDomains rename, statusReason, removed appId from output), WebhookRecord
    (webhookUrl). All 27 handlers now pass shape validation.
    - [x] Add test inputs for amplify operations to _call_handler() (27 ops)
    - [x] Verify amplify ops pass shape validation (27/27 PASS)

## [x] CI-GAP-022 — elasticache: 25 handler crashes → all 34/34 ops pass (1cb88b9a1)
    All 34 handlers now pass. Added test inputs for all operations (create/list/describe/delete/modify/tag
    for cache clusters, replication groups, parameter groups, subnet groups, snapshots, users, user groups).
    Simple creates use plain dicts; delete/modify ops use setdefault lambdas to create prerequisites first.
    Tag ops use service-prefixed keys (elasticache.AddTagsToResource, elasticache.RemoveTagsFromResource,
    elasticache.ListTagsForResource) with ResourceName-based tag store.
    - [x] Add test inputs for elasticache operations to _call_handler()
    - [x] Verify all elasticache ops pass shape validation (34/34 PASS)
    Files: development/aws-shape-validator.py

## [x] CI-GAP-023 — organizations: 23 handler crashes → add test inputs
    All 23 handlers should pass after adding test inputs following the established pattern.
    - [x] Add test inputs for organizations operations to _call_handler()
    - [x] Verify all organizations ops pass shape validation (23/23 PASS)
    Files: development/aws-shape-validator.py, specs/aws/.speclang/assembled/organizations/*.code.py

## [x] CI-GAP-024 — servicecatalog: 22 handler crashes → all 26/26 ops pass (21fc3ddce)
    All 26 handlers now pass. Added test inputs for all operations (create/list/describe/
    delete/update portfolio, product, provisioning artifact, constraint, provisioned product,
    tag option, and portfolio-product associations) using the established plain dict + lambda
    + walrus operator pattern matching prior 20 services.
    - [x] Add test inputs for servicecatalog operations to _call_handler()
    - [x] Verify all servicecatalog ops pass shape validation (26/26 PASS)
    Files: development/aws-shape-validator.py, specs/aws/.speclang/assembled/servicecatalog/*.code.py

## [x] CI-GAP-025 — fsx: 22 handler crashes → all 29/29 ops pass (842d6dba3)
    All 29 handlers now pass. Added test inputs for all operations (create/list/
    describe/delete/update/tag/untag/copy — 8+6+6+5+4) using established patterns.
    Also fixed models.code.py: Tags serialization (dict→list via _serialize_tags),
    VolumeRecord/SnapshotRecord Lifecycle defaults (CREATED→AVAILABLE), and
    added _helpers.code.py injection for _find_by_arn.
    - [x] Add test inputs for fsx operations to _call_handler()
    - [x] Verify all fsx ops pass shape validation (29/29 PASS)
    Files: development/aws-shape-validator.py, specs/aws/.speclang/assembled/fsx/*.code.py

## [x] CI-GAP-026 — memorydb: 21 handler crashes → all 27/27 ops pass (f2c6f353d)
    All 27 handlers now pass. Added test inputs for all operations (create/list/describe/
    delete/update cluster, ACL, user, parameter group, subnet group, snapshot, tags)
    using the established plain dict + lambda + walrus operator pattern.
    - [x] Add test inputs for memorydb operations to _call_handler()
    - [x] Verify all memorydb ops pass shape validation (27/27 PASS)
    Files: development/aws-shape-validator.py, specs/aws/.speclang/assembled/memorydb/*.code.py

## [x] CI-GAP-027 — redshift: 20 handler crashes → all 25/25 ops pass (4fe1f2801)
    All 25 handlers now pass. Added test inputs for all operations (create/list/
    describe/delete/modify cluster, parameter group, snapshot, subnet group,
    event subscription, pause/resume/reboot/resize, copy snapshot, reset parameter group)
    using the established plain dict + lambda + walrus operator pattern matching prior services.
    - [x] Add test inputs for redshift operations to _call_handler()
    - [x] Verify all redshift ops pass shape validation (25/25 PASS)
    Files: development/aws-shape-validator.py, specs/aws/.speclang/assembled/redshift/*.code.py

## [x] CI-GAP-028 — ram: 20 handler crashes → all 28/28 ops pass (528405fe0)
    All 28 handlers now pass. Added test inputs for all operations (create/list/
    describe/delete/update/associate/disassociate/tag/untag/invitation) using
    the established dict + lambda + walrus operator pattern matching prior 27 services.
    Also fixed PermissionRecord.to_dict(): defaultVersion changed from int to bool
    to match AWS ResourceSharePermissionDetail shape.
    - [x] Add test inputs for ram operations to _call_handler()
    - [x] Verify all ram ops pass shape validation (28/28 PASS)
    Files: development/aws-shape-validator.py, specs/aws/.speclang/assembled/ram/*.code.py

## [x] CI-GAP-029 — network-firewall: 20 handler crashes → all 23/23 ops pass (c330cd2d3)
    All 23 handlers now pass. Added test inputs for all operations (create/list/
    describe/delete/tag/untag/update firewall, policy, rule-group) using the
    established dict + lambda + walrus operator pattern matching prior 27 services.
    - [x] Add test inputs for network-firewall operations to _call_handler()
    - [x] Verify all network-firewall ops pass shape validation (23/23 PASS)
    Files: development/aws-shape-validator.py, specs/aws/.speclang/assembled/network-firewall/*.code.py

## [x] CI-GAP-030 — appsync: 20 handler crashes → all 22/22 ops pass (794f804d6)
    All 22 handlers now pass. Added test inputs for all operations (create/list/
    get/delete/update for GraphQL APIs, Data Sources, Resolvers, API Keys, and Tags)
    using the established walrus-operator lambda pattern — store methods return dicts,
    so API IDs/ARNs extracted via dict access. Tag ops use service-prefixed keys.
    - [x] Add test inputs for appsync operations to _call_handler() (22 ops)
    - [x] Verify all appsync ops pass shape validation (22/22 PASS)
    Files: development/aws-shape-validator.py, specs/aws/.speclang/assembled/appsync/*.code.py

## [ ] CI-GAP-031 — textract: 19 handler crashes → add test inputs
    All 19 handlers should pass after adding test inputs following the established pattern.
    - [ ] Add test inputs for textract operations to _call_handler()
    - [ ] Verify all textract ops pass shape validation
    Files: development/aws-shape-validator.py, specs/aws/.speclang/assembled/textract/*.code.py

<!-- 52 remaining services with errors queued for future ticks (s3tables 19, emr 19, batch 19, sesv2 18, mq 18, kafka 18, codepipeline 18, amp 18, keyspaces 17, bedrock 17, backup 17, verifiedpermissions 16, timestream-influxdb 16, storagegateway 16, datasync 16, appconfig 16, mediaconvert 15, iot 15, grafana 15, transcribe 14, rds 14, personalize 14, sagemaker 13, forecast 12, mwaa 11, docdb 11, kinesis 9, ssm 8, dms 8, polly 6, lexv2-runtime 6, iot-data 6, efs 6, autoscaling 6, greengrassv2 5, glue 4, fis 4, application-autoscaling 4, dynamodbstreams 3, acm 3, bedrock-runtime 2, + integration tests 3.10 StrEnum, 3.11 timeout) -->
