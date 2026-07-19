"""Bedrock Agent service — stores, data classes, exception classes.

Entities:
  1. Agents — CreateAgent, GetAgent, UpdateAgent, DeleteAgent, ListAgents, PrepareAgent
  2. KnowledgeBases — CRUD + List
  3. DataSources — nested under knowledgeBases (CRUD + List per KB)
  4. Tags — TagResource, UntagResource, ListTagsForResource (uses TagsMap dict format)
"""
import uuid
import time


# ── Exception Classes ────────────────────────────────────────────

class ResourceNotFoundException(Exception):
    pass

class AccessDeniedException(Exception):
    pass

class ValidationException(Exception):
    pass

class ConflictException(Exception):
    pass

class InternalServerException(Exception):
    pass

class ThrottlingException(Exception):
    pass

class ServiceQuotaExceededException(Exception):
    pass


# ── Helpers ─────────────────────────────────────────────────────

def _generate_id(prefix=""):
    return prefix + uuid.uuid4().hex[:12]

def _arn(resource_type, resource_id, region="us-east-1", account="000000000000"):
    return f"arn:aws:bedrock:{region}:{account}:{resource_type}/{resource_id}"

def _now_iso():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


# ── Data Classes ─────────────────────────────────────────────────

class AgentRecord:
    def __init__(self, agentName, foundationModel=None, agentResourceRoleArn=None,
                 instruction=None, description=None, orchestrationType="DEFAULT",
                 idleSessionTTLInSeconds=1800, customerEncryptionKeyArn=None,
                 tags=None, guardrailConfiguration=None,
                 agentCollaboration=None, clientToken=None,
                 promptOverrideConfiguration=None, memoryConfiguration=None,
                 customOrchestration=None):
        self.agentId = _generate_id()
        self.agentName = agentName
        self.agentArn = _arn("agent", self.agentId)
        self.foundationModel = foundationModel or ""
        self.agentResourceRoleArn = agentResourceRoleArn or ""
        self.instruction = instruction or ""
        self.description = description or ""
        self.orchestrationType = orchestrationType
        self.idleSessionTTLInSeconds = idleSessionTTLInSeconds
        self.customerEncryptionKeyArn = customerEncryptionKeyArn or ""
        self.guardrailConfiguration = guardrailConfiguration or {}
        self.agentCollaboration = agentCollaboration or "DISABLED"
        self.promptOverrideConfiguration = promptOverrideConfiguration or {}
        self.memoryConfiguration = memoryConfiguration or {}
        self.customOrchestration = customOrchestration or {}
        self.tags = tags or {}
        self.agentStatus = "NOT_PREPARED"
        self.agentVersion = "DRAFT"
        self.createdAt = _now_iso()
        self.updatedAt = self.createdAt
        self.preparedAt = ""
        self.failureReasons = []

    def to_dict(self):
        return {
            "agentId": self.agentId,
            "agentName": self.agentName,
            "agentArn": self.agentArn,
            "agentVersion": self.agentVersion,
            "agentStatus": self.agentStatus,
            "foundationModel": self.foundationModel,
            "agentResourceRoleArn": self.agentResourceRoleArn,
            "instruction": self.instruction,
            "description": self.description,
            "orchestrationType": self.orchestrationType,
            "idleSessionTTLInSeconds": self.idleSessionTTLInSeconds,
            "customerEncryptionKeyArn": self.customerEncryptionKeyArn,
            "guardrailConfiguration": self.guardrailConfiguration,
            "agentCollaboration": self.agentCollaboration,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
            "preparedAt": self.preparedAt,
            "failureReasons": self.failureReasons,
        }

    def to_summary(self):
        return {
            "agentId": self.agentId,
            "agentName": self.agentName,
            "agentStatus": self.agentStatus,
            "description": self.description,
            "updatedAt": self.updatedAt,
        }


class KnowledgeBaseRecord:
    def __init__(self, name, roleArn, knowledgeBaseConfiguration,
                 storageConfiguration=None, description=None, tags=None,
                 clientToken=None):
        self.knowledgeBaseId = _generate_id()
        self.name = name
        self.knowledgeBaseArn = _arn("knowledge-base", self.knowledgeBaseId)
        self.roleArn = roleArn
        self.knowledgeBaseConfiguration = knowledgeBaseConfiguration
        self.storageConfiguration = storageConfiguration or {}
        self.description = description or ""
        self.tags = tags or {}
        self.status = "ACTIVE"
        self.createdAt = _now_iso()
        self.updatedAt = self.createdAt
        self.failureReasons = []

    def to_dict(self):
        return {
            "knowledgeBaseId": self.knowledgeBaseId,
            "name": self.name,
            "knowledgeBaseArn": self.knowledgeBaseArn,
            "roleArn": self.roleArn,
            "knowledgeBaseConfiguration": self.knowledgeBaseConfiguration,
            "storageConfiguration": self.storageConfiguration,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
            "failureReasons": self.failureReasons,
        }

    def to_summary(self):
        return {
            "knowledgeBaseId": self.knowledgeBaseId,
            "name": self.name,
            "description": self.description,
            "status": self.status,
            "updatedAt": self.updatedAt,
        }


class DataSourceRecord:
    def __init__(self, knowledgeBaseId, name, dataSourceConfiguration,
                 description=None, dataDeletionPolicy="DELETE",
                 serverSideEncryptionConfiguration=None,
                 vectorIngestionConfiguration=None, clientToken=None):
        self.dataSourceId = _generate_id()
        self.knowledgeBaseId = knowledgeBaseId
        self.name = name
        self.dataSourceConfiguration = dataSourceConfiguration
        self.description = description or ""
        self.dataDeletionPolicy = dataDeletionPolicy
        self.serverSideEncryptionConfiguration = serverSideEncryptionConfiguration or {}
        self.vectorIngestionConfiguration = vectorIngestionConfiguration or {}
        self.status = "AVAILABLE"
        self.createdAt = _now_iso()
        self.updatedAt = self.createdAt
        self.failureReasons = []

    def to_dict(self):
        return {
            "dataSourceId": self.dataSourceId,
            "knowledgeBaseId": self.knowledgeBaseId,
            "name": self.name,
            "dataSourceConfiguration": self.dataSourceConfiguration,
            "description": self.description,
            "dataDeletionPolicy": self.dataDeletionPolicy,
            "serverSideEncryptionConfiguration": self.serverSideEncryptionConfiguration,
            "vectorIngestionConfiguration": self.vectorIngestionConfiguration,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
            "failureReasons": self.failureReasons,
        }

    def to_summary(self):
        return {
            "dataSourceId": self.dataSourceId,
            "knowledgeBaseId": self.knowledgeBaseId,
            "name": self.name,
            "description": self.description,
            "status": self.status,
            "updatedAt": self.updatedAt,
        }


# ── Bedrock Agent Store ─────────────────────────────────────────

class BedrockAgentStore:
    def __init__(self):
        self._agents: dict = {}
        self._knowledge_bases: dict = {}
        self._data_sources: dict = {}  # {kb_id: {ds_id: DataSourceRecord}}
        self._tags: dict = {}  # arn -> dict of tags

    # ── Agents ────────────────────────────────────────────────

    def create_agent(self, request: dict):
        tags = request.get("tags", {})
        if isinstance(tags, list):
            tag_dict = {}
            for t in tags:
                tag_dict[t.get("key", t.get("Key", ""))] = t.get("value", t.get("Value", ""))
            tags = tag_dict
        record = AgentRecord(
            agentName=request["agentName"],
            foundationModel=request.get("foundationModel"),
            agentResourceRoleArn=request.get("agentResourceRoleArn"),
            instruction=request.get("instruction"),
            description=request.get("description"),
            orchestrationType=request.get("orchestrationType", "DEFAULT"),
            idleSessionTTLInSeconds=request.get("idleSessionTTLInSeconds", 1800),
            customerEncryptionKeyArn=request.get("customerEncryptionKeyArn"),
            tags=tags,
            guardrailConfiguration=request.get("guardrailConfiguration"),
            agentCollaboration=request.get("agentCollaboration"),
            clientToken=request.get("clientToken"),
            promptOverrideConfiguration=request.get("promptOverrideConfiguration"),
            memoryConfiguration=request.get("memoryConfiguration"),
            customOrchestration=request.get("customOrchestration"))
        self._agents[record.agentId] = record
        if record.tags:
            self._tags[record.agentArn] = record.tags
        return record

    def get_agent(self, agentId: str):
        rec = self._agents.get(agentId)
        if not rec:
            raise ResourceNotFoundException(f"Agent {agentId} not found")
        return rec

    def update_agent(self, request: dict):
        agentId = request["agentId"]
        rec = self.get_agent(agentId)
        rec.agentName = request["agentName"]
        rec.foundationModel = request.get("foundationModel", rec.foundationModel)
        rec.agentResourceRoleArn = request.get("agentResourceRoleArn", rec.agentResourceRoleArn)
        rec.instruction = request.get("instruction", rec.instruction)
        rec.description = request.get("description", rec.description)
        rec.idleSessionTTLInSeconds = request.get("idleSessionTTLInSeconds", rec.idleSessionTTLInSeconds)
        if "customerEncryptionKeyArn" in request:
            rec.customerEncryptionKeyArn = request["customerEncryptionKeyArn"]
        if "guardrailConfiguration" in request:
            rec.guardrailConfiguration = request["guardrailConfiguration"]
        if "agentCollaboration" in request:
            rec.agentCollaboration = request["agentCollaboration"]
        rec.updatedAt = _now_iso()
        return rec

    def delete_agent(self, agentId: str, skipResourceInUseCheck=None):
        rec = self.get_agent(agentId)
        del self._agents[agentId]
        self._tags.pop(rec.agentArn, None)
        return {"agentId": agentId, "agentStatus": "DELETING"}

    def list_agents(self, maxResults=None, nextToken=None):
        items = list(self._agents.values())
        return {"agentSummaries": [r.to_summary() for r in items], "nextToken": nextToken}

    def prepare_agent(self, agentId: str):
        rec = self.get_agent(agentId)
        rec.agentStatus = "PREPARED"
        rec.agentVersion = "1"
        rec.preparedAt = _now_iso()
        return rec

    # ── Knowledge Bases ──────────────────────────────────────

    def create_knowledge_base(self, request: dict):
        tags = request.get("tags", {})
        if isinstance(tags, list):
            tag_dict = {}
            for t in tags:
                tag_dict[t.get("key", t.get("Key", ""))] = t.get("value", t.get("Value", ""))
            tags = tag_dict
        record = KnowledgeBaseRecord(
            name=request["name"],
            roleArn=request["roleArn"],
            knowledgeBaseConfiguration=request["knowledgeBaseConfiguration"],
            storageConfiguration=request.get("storageConfiguration"),
            description=request.get("description"),
            tags=tags,
            clientToken=request.get("clientToken"))
        self._knowledge_bases[record.knowledgeBaseId] = record
        if record.tags:
            self._tags[record.knowledgeBaseArn] = record.tags
        return record

    def get_knowledge_base(self, knowledgeBaseId: str):
        rec = self._knowledge_bases.get(knowledgeBaseId)
        if not rec:
            raise ResourceNotFoundException(f"Knowledge base {knowledgeBaseId} not found")
        return rec

    def update_knowledge_base(self, request: dict):
        kbId = request["knowledgeBaseId"]
        rec = self.get_knowledge_base(kbId)
        rec.name = request["name"]
        rec.roleArn = request["roleArn"]
        rec.knowledgeBaseConfiguration = request["knowledgeBaseConfiguration"]
        if "description" in request:
            rec.description = request["description"]
        if "storageConfiguration" in request:
            rec.storageConfiguration = request["storageConfiguration"]
        rec.updatedAt = _now_iso()
        return rec

    def delete_knowledge_base(self, knowledgeBaseId: str):
        rec = self.get_knowledge_base(knowledgeBaseId)
        del self._knowledge_bases[knowledgeBaseId]
        self._tags.pop(rec.knowledgeBaseArn, None)
        return {"knowledgeBaseId": knowledgeBaseId, "status": "DELETING"}

    def list_knowledge_bases(self, maxResults=None, nextToken=None):
        items = list(self._knowledge_bases.values())
        return {"knowledgeBaseSummaries": [r.to_summary() for r in items],
                "nextToken": nextToken}

    # ── Data Sources ─────────────────────────────────────────

    def create_data_source(self, request: dict):
        kbId = request["knowledgeBaseId"]
        self.get_knowledge_base(kbId)  # verify KB exists
        record = DataSourceRecord(
            knowledgeBaseId=kbId,
            name=request["name"],
            dataSourceConfiguration=request["dataSourceConfiguration"],
            description=request.get("description"),
            dataDeletionPolicy=request.get("dataDeletionPolicy", "DELETE"),
            serverSideEncryptionConfiguration=request.get("serverSideEncryptionConfiguration"),
            vectorIngestionConfiguration=request.get("vectorIngestionConfiguration"),
            clientToken=request.get("clientToken"))
        if kbId not in self._data_sources:
            self._data_sources[kbId] = {}
        self._data_sources[kbId][record.dataSourceId] = record
        return record

    def get_data_source(self, knowledgeBaseId: str, dataSourceId: str):
        kb = self._data_sources.get(knowledgeBaseId, {})
        rec = kb.get(dataSourceId)
        if not rec:
            raise ResourceNotFoundException(f"DataSource {dataSourceId} not found")
        return rec

    def update_data_source(self, request: dict):
        kbId = request["knowledgeBaseId"]
        dsId = request["dataSourceId"]
        rec = self.get_data_source(kbId, dsId)
        rec.name = request["name"]
        rec.dataSourceConfiguration = request["dataSourceConfiguration"]
        if "description" in request:
            rec.description = request["description"]
        if "dataDeletionPolicy" in request:
            rec.dataDeletionPolicy = request["dataDeletionPolicy"]
        rec.updatedAt = _now_iso()
        return rec

    def delete_data_source(self, knowledgeBaseId: str, dataSourceId: str):
        self.get_data_source(knowledgeBaseId, dataSourceId)  # verify exists
        del self._data_sources[knowledgeBaseId][dataSourceId]
        return {"knowledgeBaseId": knowledgeBaseId, "dataSourceId": dataSourceId,
                "status": "DELETING"}

    def list_data_sources(self, knowledgeBaseId: str, maxResults=None, nextToken=None):
        kb = self._data_sources.get(knowledgeBaseId, {})
        items = list(kb.values())
        return {"dataSourceSummaries": [r.to_summary() for r in items],
                "nextToken": nextToken}

    # ── Tags ─────────────────────────────────────────────────

    def tag_resource(self, resourceARN: str, tags):
        if isinstance(tags, list):
            tag_dict = {}
            for t in tags:
                tag_dict[t.get("key", t.get("Key", ""))] = t.get("value", t.get("Value", ""))
            tags = tag_dict
        if resourceARN not in self._tags:
            self._tags[resourceARN] = {}
        self._tags[resourceARN].update(tags)
        return {}

    def untag_resource(self, resourceARN: str, tagKeys):
        if resourceARN in self._tags:
            for k in tagKeys:
                self._tags[resourceARN].pop(k, None)
        return {}

    def list_tags_for_resource(self, resourceARN: str):
        return {"tags": self._tags.get(resourceARN, {})}
