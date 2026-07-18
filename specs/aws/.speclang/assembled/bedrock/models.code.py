"""Bedrock service — stores, data classes, exception classes.

Entities:
  1. FoundationModels (read-only) — GetFoundationModel, ListFoundationModels, etc.
  2. Guardrails (CRUD + versioning)
  3. ModelCustomizationJobs (create, get, list, stop)
  4. ProvisionedModelThroughputs (CRUD)
  5. Tags — TagResource, UntagResource, ListTagsForResource
"""
import uuid
import time


# ── Exception Classes ────────────────────────────────────────────

class ResourceNotFoundException(Exception):
    """The specified resource was not found."""
    pass

class AccessDeniedException(Exception):
    """Access denied."""
    pass

class ValidationException(Exception):
    """Validation error in the request."""
    pass

class ConflictException(Exception):
    """The request conflicts with an existing resource."""
    pass

class InternalServerException(Exception):
    """Internal server error."""
    pass

class ThrottlingException(Exception):
    """Request was throttled."""
    pass

class TooManyTagsException(Exception):
    """Too many tags on the resource."""
    pass

class ServiceQuotaExceededException(Exception):
    """Service quota exceeded."""
    pass


# ── Helper Functions ─────────────────────────────────────────────

def _generate_id(prefix=""):
    return prefix + uuid.uuid4().hex[:12]

def _arn(service, resource_type, resource_id, region="us-east-1", account="000000000000"):
    return f"arn:aws:bedrock:{region}:{account}:{resource_type}/{resource_id}"

def _now_iso():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

def _tags_from_list(tags):
    """Convert AWS tag list [{key, value}] to flat dict {key: value}."""
    if not tags:
        return {}
    if isinstance(tags, dict):
        return tags
    result = {}
    for t in tags:
        k = t.get("key", t.get("Key", ""))
        v = t.get("value", t.get("Value", ""))
        if k:
            result[k] = v
    return result

def _tags_to_list(tags_dict):
    """Convert flat dict {key: value} to AWS tag list [{key, value}]."""
    if not tags_dict:
        return []
    if isinstance(tags_dict, list):
        return tags_dict
    return [{"key": str(k), "value": str(v)} for k, v in tags_dict.items()]


# ── Data Classes ─────────────────────────────────────────────────

class FoundationModelDetails:
    def __init__(self, modelArn, modelId, modelName, providerName,
                 inputModalities=None, outputModalities=None,
                 responseStreamingSupported=None,
                 customizationsSupported=None, inferenceTypesSupported=None,
                 modelLifecycle=None):
        self.modelArn = modelArn
        self.modelId = modelId
        self.modelName = modelName
        self.providerName = providerName
        self.inputModalities = inputModalities or []
        self.outputModalities = outputModalities or []
        self.responseStreamingSupported = responseStreamingSupported
        self.customizationsSupported = customizationsSupported or []
        self.inferenceTypesSupported = inferenceTypesSupported or []
        self.modelLifecycle = modelLifecycle

    def to_dict(self):
        return {
            "modelArn": self.modelArn,
            "modelId": self.modelId,
            "modelName": self.modelName,
            "providerName": self.providerName,
            "inputModalities": self.inputModalities,
            "outputModalities": self.outputModalities,
            "responseStreamingSupported": self.responseStreamingSupported,
            "customizationsSupported": self.customizationsSupported,
            "inferenceTypesSupported": self.inferenceTypesSupported,
            "modelLifecycle": self.modelLifecycle,
        }


class GuardrailRecord:
    def __init__(self, name, blockedInputMessaging, blockedOutputsMessaging,
                 description=None, topicPolicyConfig=None, contentPolicyConfig=None,
                 wordPolicyConfig=None, sensitiveInformationPolicyConfig=None,
                 contextualGroundingPolicyConfig=None,
                 automatedReasoningPolicyConfig=None,
                 crossRegionConfig=None, kmsKeyId=None, tags=None,
                 clientRequestToken=None):
        self.name = name
        self.description = description or ""
        self.blockedInputMessaging = blockedInputMessaging
        self.blockedOutputsMessaging = blockedOutputsMessaging
        self.topicPolicyConfig = topicPolicyConfig
        self.contentPolicyConfig = contentPolicyConfig
        self.wordPolicyConfig = wordPolicyConfig
        self.sensitiveInformationPolicyConfig = sensitiveInformationPolicyConfig
        self.contextualGroundingPolicyConfig = contextualGroundingPolicyConfig
        self.automatedReasoningPolicyConfig = automatedReasoningPolicyConfig
        self.crossRegionConfig = crossRegionConfig
        self.kmsKeyId = kmsKeyId or ""
        if tags:
            if isinstance(tags, list):
                tag_dict = {}
                for t in tags:
                    tag_dict[t.get("key", t.get("Key", ""))] = t.get("value", t.get("Value", ""))
                self.tags = tag_dict
            else:
                self.tags = dict(tags)
        else:
            self.tags = {}
        self.guardrailId = _generate_id()
        self.guardrailArn = _arn("bedrock", "guardrail", self.guardrailId)
        self.version = "DRAFT"
        self.status = "READY"
        self.createdAt = _now_iso()
        self.updatedAt = self.createdAt
        self.statusReasons = []
        self.failureRecommendations = []
        self.kmsKeyArn = ""
        self.topicPolicy = topicPolicyConfig
        self.contentPolicy = contentPolicyConfig
        self.wordPolicy = wordPolicyConfig
        self.sensitiveInformationPolicy = sensitiveInformationPolicyConfig
        self.contextualGroundingPolicy = contextualGroundingPolicyConfig
        self.automatedReasoningPolicy = automatedReasoningPolicyConfig
        self.crossRegionDetails = crossRegionConfig
        self.numericalVersion = 1

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "guardrailId": self.guardrailId,
            "guardrailArn": self.guardrailArn,
            "version": self.version,
            "status": self.status,
            "topicPolicy": self.topicPolicy,
            "contentPolicy": self.contentPolicy,
            "wordPolicy": self.wordPolicy,
            "sensitiveInformationPolicy": self.sensitiveInformationPolicy,
            "contextualGroundingPolicy": self.contextualGroundingPolicy,
            "automatedReasoningPolicy": self.automatedReasoningPolicy,
            "crossRegionDetails": self.crossRegionDetails,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
            "statusReasons": self.statusReasons,
            "failureRecommendations": self.failureRecommendations,
            "blockedInputMessaging": self.blockedInputMessaging,
            "blockedOutputsMessaging": self.blockedOutputsMessaging,
            "kmsKeyArn": self.kmsKeyArn,
        }

    def to_summary(self):
        return {
            "id": self.guardrailId,
            "arn": self.guardrailArn,
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }


class ModelCustomizationJobRecord:
    def __init__(self, jobName, customModelName, roleArn, baseModelIdentifier,
                 trainingDataConfig, outputDataConfig,
                 customizationType="FINE_TUNING", clientRequestToken=None,
                 customModelKmsKeyId=None, jobTags=None, customModelTags=None,
                 validationDataConfig=None, hyperParameters=None,
                 vpcConfig=None, customizationConfig=None):
        self.jobName = jobName
        self.customModelName = customModelName
        self.roleArn = roleArn
        self.baseModelIdentifier = baseModelIdentifier
        self.trainingDataConfig = trainingDataConfig
        self.outputDataConfig = outputDataConfig
        self.customizationType = customizationType
        self.clientRequestToken = clientRequestToken or ""
        self.customModelKmsKeyId = customModelKmsKeyId or ""
        self.jobTags = _tags_from_list(jobTags)
        self.customModelTags = _tags_from_list(customModelTags)
        self.validationDataConfig = validationDataConfig
        self.hyperParameters = hyperParameters or {}
        self.vpcConfig = vpcConfig
        self.customizationConfig = customizationConfig
        self.jobArn = _arn("bedrock", "model-customization-job", _generate_id())
        self.status = "InProgress"
        self.statusDetails = {}
        self.failureMessage = ""
        self.creationTime = _now_iso()
        self.lastModifiedTime = self.creationTime
        self.endTime = ""
        self.baseModelArn = f"arn:aws:bedrock:us-east-1::foundation-model/{baseModelIdentifier}"
        self.outputModelName = customModelName
        self.outputModelArn = f"arn:aws:bedrock:us-east-1:000000000000:custom-model/{customModelName}"
        self.outputModelKmsKeyArn = ""
        self.trainingMetrics = {}
        self.validationMetrics = []

    def to_dict(self):
        return {
            "jobArn": self.jobArn,
            "jobName": self.jobName,
            "outputModelName": self.outputModelName,
            "outputModelArn": self.outputModelArn,
            "clientRequestToken": self.clientRequestToken,
            "roleArn": self.roleArn,
            "status": self.status,
            "statusDetails": self.statusDetails,
            "failureMessage": self.failureMessage,
            "creationTime": self.creationTime,
            "lastModifiedTime": self.lastModifiedTime,
            "endTime": self.endTime,
            "baseModelArn": self.baseModelArn,
            "hyperParameters": self.hyperParameters,
            "trainingDataConfig": self.trainingDataConfig,
            "validationDataConfig": self.validationDataConfig,
            "outputDataConfig": self.outputDataConfig,
            "customizationType": self.customizationType,
            "outputModelKmsKeyArn": self.outputModelKmsKeyArn,
            "trainingMetrics": self.trainingMetrics,
            "validationMetrics": self.validationMetrics,
            "vpcConfig": self.vpcConfig,
            "customizationConfig": self.customizationConfig,
        }

    def to_summary(self):
        return {
            "jobArn": self.jobArn,
            "jobName": self.jobName,
            "outputModelName": self.outputModelName,
            "outputModelArn": self.outputModelArn,
            "customizationType": self.customizationType,
            "status": self.status,
            "creationTime": self.creationTime,
            "lastModifiedTime": self.lastModifiedTime,
            "endTime": self.endTime,
            "baseModelArn": self.baseModelArn,
        }


class ProvisionedModelRecord:
    def __init__(self, modelUnits, provisionedModelName, modelId,
                 commitmentDuration=None, tags=None, clientRequestToken=None):
        self.modelUnits = modelUnits
        self.provisionedModelName = provisionedModelName
        self.modelId = modelId
        self.commitmentDuration = commitmentDuration or "OneMonth"
        self.commitmentExpirationTime = ""
        self.clientRequestToken = clientRequestToken or ""
        self.provisionedModelId = _generate_id()
        self.provisionedModelArn = _arn("bedrock", "provisioned-model", self.provisionedModelId)
        self.modelArn = f"arn:aws:bedrock:us-east-1::foundation-model/{modelId}"
        self.desiredModelArn = self.modelArn
        self.foundationModelArn = self.modelArn
        self.desiredModelUnits = modelUnits
        self.status = "InService"
        self.creationTime = _now_iso()
        self.lastModifiedTime = self.creationTime
        self.failureMessage = ""
        self.tags = _tags_from_list(tags)

    def to_dict(self):
        return {
            "modelUnits": self.modelUnits,
            "desiredModelUnits": self.desiredModelUnits,
            "provisionedModelName": self.provisionedModelName,
            "provisionedModelArn": self.provisionedModelArn,
            "modelArn": self.modelArn,
            "desiredModelArn": self.desiredModelArn,
            "foundationModelArn": self.foundationModelArn,
            "status": self.status,
            "creationTime": self.creationTime,
            "lastModifiedTime": self.lastModifiedTime,
            "failureMessage": self.failureMessage,
            "commitmentDuration": self.commitmentDuration,
            "commitmentExpirationTime": self.commitmentExpirationTime,
        }

    def to_summary(self):
        return {
            "provisionedModelName": self.provisionedModelName,
            "provisionedModelArn": self.provisionedModelArn,
            "modelArn": self.modelArn,
            "desiredModelArn": self.desiredModelArn,
            "foundationModelArn": self.foundationModelArn,
            "modelUnits": self.modelUnits,
            "desiredModelUnits": self.desiredModelUnits,
            "status": self.status,
            "commitmentDuration": self.commitmentDuration,
            "commitmentExpirationTime": self.commitmentExpirationTime,
            "creationTime": self.creationTime,
            "lastModifiedTime": self.lastModifiedTime,
        }


# ── Bedrock Store ────────────────────────────────────────────────

class BedrockStore:
    """Store for Bedrock service — greenfield, all from scratch."""

    def __init__(self):
        self._guardrails: dict = {}
        self._guardrail_versions: dict = {}  # guardrailId -> [versioned copies]
        self._customization_jobs: dict = {}
        self._provisioned_models: dict = {}  # provisionedModelId -> record
        self._tags: dict = {}  # arn -> {key: value}

    # ── Foundation Models (read-only) ────────────────────────────

    def get_foundation_model(self, modelIdentifier: str):
        """Get details for a single foundation model."""
        models = self._list_foundation_models()
        for m in models:
            if m.modelId == modelIdentifier or m.modelArn == modelIdentifier:
                return m
        raise ResourceNotFoundException(
            f"Foundation model {modelIdentifier} not found")

    def list_foundation_models(self, byProvider=None, byCustomizationType=None,
                               byOutputModality=None, byInferenceType=None):
        models = self._list_foundation_models()
        if byProvider:
            models = [m for m in models if m.providerName == byProvider]
        if byOutputModality:
            models = [m for m in models if byOutputModality in m.outputModalities]
        return models

    def get_foundation_model_availability(self, modelId: str):
        model = self.get_foundation_model(modelId)
        return {
            "modelId": model.modelId,
            "agreementAvailability": {"status": "AVAILABLE"},
            "authorizationStatus": "AUTHORIZED",
            "entitlementAvailability": "AVAILABLE",
            "regionAvailability": "AVAILABLE",
        }

    @staticmethod
    def _list_foundation_models():
        return [
            FoundationModelDetails(
                modelArn="arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-v2",
                modelId="anthropic.claude-v2", modelName="Claude V2",
                providerName="Anthropic",
                inputModalities=["TEXT"], outputModalities=["TEXT"],
                responseStreamingSupported=True,
                customizationsSupported=["FINE_TUNING"],
                inferenceTypesSupported=["ON_DEMAND", "PROVISIONED"],
                modelLifecycle={"status": "ACTIVE"}),
            FoundationModelDetails(
                modelArn="arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-sonnet",
                modelId="anthropic.claude-3-sonnet-20240229-v1:0", modelName="Claude 3 Sonnet",
                providerName="Anthropic",
                inputModalities=["TEXT", "IMAGE"], outputModalities=["TEXT"],
                responseStreamingSupported=True,
                customizationsSupported=[],
                inferenceTypesSupported=["ON_DEMAND", "PROVISIONED"],
                modelLifecycle={"status": "ACTIVE"}),
            FoundationModelDetails(
                modelArn="arn:aws:bedrock:us-east-1::foundation-model/meta.llama3-70b",
                modelId="meta.llama3-70b-instruct-v1:0", modelName="Llama 3 70B",
                providerName="Meta",
                inputModalities=["TEXT"], outputModalities=["TEXT"],
                responseStreamingSupported=True,
                customizationsSupported=["FINE_TUNING"],
                inferenceTypesSupported=["ON_DEMAND", "PROVISIONED"],
                modelLifecycle={"status": "ACTIVE"}),
        ]

    # ── Guardrails ────────────────────────────────────────────────

    def create_guardrail(self, request: dict):
        name = request["name"]
        blockedInputMessaging = request["blockedInputMessaging"]
        blockedOutputsMessaging = request["blockedOutputsMessaging"]
        record = GuardrailRecord(
            name=name,
            blockedInputMessaging=blockedInputMessaging,
            blockedOutputsMessaging=blockedOutputsMessaging,
            description=request.get("description"),
            topicPolicyConfig=request.get("topicPolicyConfig"),
            contentPolicyConfig=request.get("contentPolicyConfig"),
            wordPolicyConfig=request.get("wordPolicyConfig"),
            sensitiveInformationPolicyConfig=request.get("sensitiveInformationPolicyConfig"),
            contextualGroundingPolicyConfig=request.get("contextualGroundingPolicyConfig"),
            automatedReasoningPolicyConfig=request.get("automatedReasoningPolicyConfig"),
            crossRegionConfig=request.get("crossRegionConfig"),
            kmsKeyId=request.get("kmsKeyId"),
            tags=request.get("tags"),
            clientRequestToken=request.get("clientRequestToken"))
        self._guardrails[record.guardrailId] = record
        if record.tags:
            self._tags[record.guardrailArn] = record.tags
        return record

    def get_guardrail(self, guardrailIdentifier: str, guardrailVersion=None):
        record = self._guardrails.get(guardrailIdentifier)
        if not record:
            raise ResourceNotFoundException(
                f"Guardrail {guardrailIdentifier} not found")
        return record

    def update_guardrail(self, request: dict):
        guardrailIdentifier = request["guardrailIdentifier"]
        record = self.get_guardrail(guardrailIdentifier)
        record.name = request.get("name", record.name)
        record.description = request.get("description", record.description)
        record.blockedInputMessaging = request.get("blockedInputMessaging", record.blockedInputMessaging)
        record.blockedOutputsMessaging = request.get("blockedOutputsMessaging", record.blockedOutputsMessaging)
        for cfg in ["topicPolicyConfig", "contentPolicyConfig", "wordPolicyConfig",
                     "sensitiveInformationPolicyConfig", "contextualGroundingPolicyConfig",
                     "automatedReasoningPolicyConfig", "crossRegionConfig"]:
            if cfg in request:
                setattr(record, cfg[0:1].lower() + cfg[1:], request[cfg])
        if "kmsKeyId" in request:
            record.kmsKeyId = request["kmsKeyId"]
        record.version = "DRAFT"
        record.updatedAt = _now_iso()
        return record

    def delete_guardrail(self, guardrailIdentifier: str, guardrailVersion=None):
        record = self.get_guardrail(guardrailIdentifier)
        del self._guardrails[guardrailIdentifier]
        self._tags.pop(record.guardrailArn, None)
        return {}

    def create_guardrail_version(self, guardrailIdentifier: str,
                                  description=None, clientRequestToken=None):
        record = self.get_guardrail(guardrailIdentifier)
        version_copy = GuardrailRecord.__new__(GuardrailRecord)
        version_copy.__dict__.update(record.__dict__)
        version_copy.numericalVersion = record.numericalVersion
        record.numericalVersion += 1
        if not self._guardrail_versions.get(guardrailIdentifier):
            self._guardrail_versions[guardrailIdentifier] = []
        self._guardrail_versions[guardrailIdentifier].append(version_copy)
        record.version = str(version_copy.numericalVersion)
        return record

    def list_guardrails(self, guardrailIdentifier=None, maxResults=None, nextToken=None):
        items = list(self._guardrails.values())
        if guardrailIdentifier:
            items = [r for r in items if r.guardrailId == guardrailIdentifier]
        return {"guardrails": [r.to_summary() for r in items], "nextToken": nextToken}

    # ── Model Customization Jobs ─────────────────────────────────

    def create_model_customization_job(self, request: dict):
        jobName = request["jobName"]
        record = ModelCustomizationJobRecord(
            jobName=jobName,
            customModelName=request["customModelName"],
            roleArn=request["roleArn"],
            baseModelIdentifier=request["baseModelIdentifier"],
            trainingDataConfig=request["trainingDataConfig"],
            outputDataConfig=request["outputDataConfig"],
            customizationType=request.get("customizationType", "FINE_TUNING"),
            clientRequestToken=request.get("clientRequestToken"),
            customModelKmsKeyId=request.get("customModelKmsKeyId"),
            jobTags=request.get("jobTags"),
            customModelTags=request.get("customModelTags"),
            validationDataConfig=request.get("validationDataConfig"),
            hyperParameters=request.get("hyperParameters"),
            vpcConfig=request.get("vpcConfig"),
            customizationConfig=request.get("customizationConfig"))
        self._customization_jobs[record.jobArn] = record
        return record

    def get_model_customization_job(self, jobIdentifier: str):
        record = self._customization_jobs.get(jobIdentifier)
        if not record:
            raise ResourceNotFoundException(
                f"Model customization job {jobIdentifier} not found")
        return record

    def stop_model_customization_job(self, jobIdentifier: str):
        record = self.get_model_customization_job(jobIdentifier)
        record.status = "Stopping"
        return {}

    def list_model_customization_jobs(self, creationTimeAfter=None,
                                       creationTimeBefore=None, statusEquals=None,
                                       nameContains=None, maxResults=None,
                                       nextToken=None, sortBy=None, sortOrder=None):
        items = list(self._customization_jobs.values())
        if statusEquals:
            items = [r for r in items if r.status == statusEquals]
        if nameContains:
            items = [r for r in items if nameContains in r.jobName]
        return {"modelCustomizationJobSummaries": [r.to_summary() for r in items],
                "nextToken": nextToken}

    # ── Provisioned Model Throughput ─────────────────────────────

    def create_provisioned_model_throughput(self, request: dict):
        record = ProvisionedModelRecord(
            modelUnits=request["modelUnits"],
            provisionedModelName=request["provisionedModelName"],
            modelId=request["modelId"],
            commitmentDuration=request.get("commitmentDuration"),
            tags=request.get("tags"),
            clientRequestToken=request.get("clientRequestToken"))
        self._provisioned_models[record.provisionedModelId] = record
        if record.tags:
            self._tags[record.provisionedModelArn] = record.tags
        return record

    def get_provisioned_model_throughput(self, provisionedModelId: str):
        record = self._provisioned_models.get(provisionedModelId)
        if not record:
            raise ResourceNotFoundException(
                f"Provisioned model {provisionedModelId} not found")
        return record

    def update_provisioned_model_throughput(self, provisionedModelId: str,
                                              desiredProvisionedModelName=None,
                                              desiredModelId=None):
        record = self.get_provisioned_model_throughput(provisionedModelId)
        if desiredProvisionedModelName:
            record.provisionedModelName = desiredProvisionedModelName
        if desiredModelId:
            record.modelId = desiredModelId
            record.desiredModelArn = f"arn:aws:bedrock:us-east-1::foundation-model/{desiredModelId}"
        record.lastModifiedTime = _now_iso()
        return {}

    def delete_provisioned_model_throughput(self, provisionedModelId: str):
        record = self.get_provisioned_model_throughput(provisionedModelId)
        del self._provisioned_models[provisionedModelId]
        self._tags.pop(record.provisionedModelArn, None)
        return {}

    def list_provisioned_model_throughputs(self, creationTimeAfter=None,
                                            creationTimeBefore=None, statusEquals=None,
                                            modelArnEquals=None, nameContains=None,
                                            maxResults=None, nextToken=None,
                                            sortBy=None, sortOrder=None):
        items = list(self._provisioned_models.values())
        if statusEquals:
            items = [r for r in items if r.status == statusEquals]
        if nameContains:
            items = [r for r in items if nameContains in r.provisionedModelName]
        return {"provisionedModelSummaries": [r.to_summary() for r in items],
                "nextToken": nextToken}

    # ── Tags ─────────────────────────────────────────────────────

    def tag_resource(self, resourceARN: str, tags: list):
        if resourceARN not in self._tags:
            self._tags[resourceARN] = {}
        for t in tags:
            k = t.get("key", t.get("Key", ""))
            v = t.get("value", t.get("Value", ""))
            self._tags[resourceARN][k] = v
        return {}

    def untag_resource(self, resourceARN: str, tagKeys: list):
        if resourceARN in self._tags:
            for k in tagKeys:
                self._tags[resourceARN].pop(k, None)
        return {}

    def list_tags_for_resource(self, resourceARN: str):
        tags_dict = self._tags.get(resourceARN, {})
        return {"tags": _tags_to_list(tags_dict)}
