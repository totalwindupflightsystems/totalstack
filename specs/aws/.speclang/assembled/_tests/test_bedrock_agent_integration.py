"""Integration test for Bedrock Agent — real store."""
import pytest
import os
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'bedrock-agent')

models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

BedrockAgentStore = models_mod.BedrockAgentStore
AgentRecord = models_mod.AgentRecord
KnowledgeBaseRecord = models_mod.KnowledgeBaseRecord
DataSourceRecord = models_mod.DataSourceRecord
ResourceNotFoundException = models_mod.ResourceNotFoundException
AccessDeniedException = models_mod.AccessDeniedException
ValidationException = models_mod.ValidationException
ConflictException = models_mod.ConflictException
InternalServerException = models_mod.InternalServerException
ThrottlingException = models_mod.ThrottlingException
ServiceQuotaExceededException = models_mod.ServiceQuotaExceededException


def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    for exc in [ResourceNotFoundException, AccessDeniedException, ValidationException,
                 ConflictException, InternalServerException, ThrottlingException,
                 ServiceQuotaExceededException]:
        mod.__dict__[exc.__name__] = exc
    for rec in [AgentRecord, KnowledgeBaseRecord, DataSourceRecord]:
        mod.__dict__[rec.__name__] = rec
    spec.loader.exec_module(mod)
    skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


# ═════════════════════════════════════════════════════════════════════
# Agents
# ═════════════════════════════════════════════════════════════════════

class TestAgents:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = BedrockAgentStore()
        return self._store

    def test_create_agent_happy(self):
        handler = _load_handler('CreateAgent')
        resp = handler(self.store, {"agentName": "test-agent"})
        assert resp["agent"]["agentId"]
        assert resp["agent"]["agentName"] == "test-agent"

    def test_create_agent_with_tags(self):
        handler = _load_handler('CreateAgent')
        resp = handler(self.store, {
            "agentName": "tagged-agent",
            "tags": {"env": "test", "team": "bedrock"},
        })
        tag_handler = _load_handler('ListTagsForResource')
        tags = tag_handler(self.store, {"resourceArn": resp["agent"]["agentArn"]})
        assert len(tags["tags"]) == 2

    def test_get_agent_happy(self):
        create = _load_handler('CreateAgent')
        created = create(self.store, {"agentName": "get-me"})
        get_handler = _load_handler('GetAgent')
        resp = get_handler(self.store, {"agentId": created["agent"]["agentId"]})
        assert resp["agent"]["agentName"] == "get-me"

    def test_get_agent_not_found(self):
        handler = _load_handler('GetAgent')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"agentId": "nonexistent"})

    def test_update_agent(self):
        create = _load_handler('CreateAgent')
        created = create(self.store, {"agentName": "update-me"})
        a_id = created["agent"]["agentId"]
        update = _load_handler('UpdateAgent')
        resp = update(self.store, {
            "agentId": a_id, "agentName": "updated-name",
            "foundationModel": "anthropic.claude-v2",
            "agentResourceRoleArn": "arn:aws:iam::000000000000:role/test",
        })
        assert resp["agent"]["agentName"] == "updated-name"

    def test_delete_agent(self):
        create = _load_handler('CreateAgent')
        created = create(self.store, {"agentName": "delete-me"})
        a_id = created["agent"]["agentId"]
        handler = _load_handler('DeleteAgent')
        handler(self.store, {"agentId": a_id})
        with pytest.raises(ResourceNotFoundException):
            get_handler = _load_handler('GetAgent')
            get_handler(self.store, {"agentId": a_id})

    def test_list_agents(self):
        create = _load_handler('CreateAgent')
        create(self.store, {"agentName": "a1"})
        create(self.store, {"agentName": "a2"})
        handler = _load_handler('ListAgents')
        resp = handler(self.store, {})
        assert len(resp["agentSummaries"]) == 2

    def test_prepare_agent(self):
        create = _load_handler('CreateAgent')
        created = create(self.store, {"agentName": "prepare-me"})
        a_id = created["agent"]["agentId"]
        handler = _load_handler('PrepareAgent')
        resp = handler(self.store, {"agentId": a_id})
        assert resp["agentStatus"] == "PREPARED"
        assert resp["agentVersion"] == "1"


# ═════════════════════════════════════════════════════════════════════
# Knowledge Bases
# ═════════════════════════════════════════════════════════════════════

class TestKnowledgeBases:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = BedrockAgentStore()
        return self._store

    def test_create_kb_happy(self):
        handler = _load_handler('CreateKnowledgeBase')
        resp = handler(self.store, {
            "name": "test-kb",
            "roleArn": "arn:aws:iam::000000000000:role/BedrockRole",
            "knowledgeBaseConfiguration": {"type": "VECTOR", "vectorKnowledgeBaseConfiguration": {"embeddingModelArn": "arn:aws:bedrock:us-east-1::foundation-model/test"}},
        })
        assert resp["knowledgeBase"]["knowledgeBaseId"]

    def test_get_kb_happy(self):
        create = _load_handler('CreateKnowledgeBase')
        created = create(self.store, {
            "name": "get-kb",
            "roleArn": "arn:aws:iam::000000000000:role/BedrockRole",
            "knowledgeBaseConfiguration": {"type": "VECTOR"},
        })
        get_handler = _load_handler('GetKnowledgeBase')
        resp = get_handler(self.store, {"knowledgeBaseId": created["knowledgeBase"]["knowledgeBaseId"]})
        assert resp["knowledgeBase"]["name"] == "get-kb"

    def test_get_kb_not_found(self):
        handler = _load_handler('GetKnowledgeBase')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"knowledgeBaseId": "nonexistent"})

    def test_update_kb(self):
        create = _load_handler('CreateKnowledgeBase')
        created = create(self.store, {
            "name": "update-kb",
            "roleArn": "arn:aws:iam::000000000000:role/BedrockRole",
            "knowledgeBaseConfiguration": {"type": "VECTOR"},
        })
        kb_id = created["knowledgeBase"]["knowledgeBaseId"]
        update = _load_handler('UpdateKnowledgeBase')
        resp = update(self.store, {
            "knowledgeBaseId": kb_id, "name": "updated-kb",
            "roleArn": "arn:aws:iam::000000000000:role/BedrockRole",
            "knowledgeBaseConfiguration": {"type": "VECTOR"},
        })
        assert resp["knowledgeBase"]["name"] == "updated-kb"

    def test_delete_kb(self):
        create = _load_handler('CreateKnowledgeBase')
        created = create(self.store, {
            "name": "delete-kb",
            "roleArn": "arn:aws:iam::000000000000:role/BedrockRole",
            "knowledgeBaseConfiguration": {"type": "VECTOR"},
        })
        kb_id = created["knowledgeBase"]["knowledgeBaseId"]
        handler = _load_handler('DeleteKnowledgeBase')
        resp = handler(self.store, {"knowledgeBaseId": kb_id})
        assert resp["knowledgeBaseId"] == kb_id
        assert resp["status"] == "DELETING"

    def test_list_kbs(self):
        create = _load_handler('CreateKnowledgeBase')
        create(self.store, {
            "name": "kb1",
            "roleArn": "arn:aws:iam::000000000000:role/BedrockRole",
            "knowledgeBaseConfiguration": {"type": "VECTOR"},
        })
        create(self.store, {
            "name": "kb2",
            "roleArn": "arn:aws:iam::000000000000:role/BedrockRole",
            "knowledgeBaseConfiguration": {"type": "VECTOR"},
        })
        handler = _load_handler('ListKnowledgeBases')
        resp = handler(self.store, {})
        assert len(resp["knowledgeBaseSummaries"]) == 2


# ═════════════════════════════════════════════════════════════════════
# Data Sources (nested under KB)
# ═════════════════════════════════════════════════════════════════════

class TestDataSources:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = BedrockAgentStore()
        return self._store

    @pytest.fixture
    def kb_id(self):
        create_kb = _load_handler('CreateKnowledgeBase')
        resp = create_kb(self.store, {
            "name": "ds-parent-kb",
            "roleArn": "arn:aws:iam::000000000000:role/BedrockRole",
            "knowledgeBaseConfiguration": {"type": "VECTOR"},
        })
        return resp["knowledgeBase"]["knowledgeBaseId"]

    def test_create_ds_happy(self, kb_id):
        handler = _load_handler('CreateDataSource')
        resp = handler(self.store, {
            "knowledgeBaseId": kb_id,
            "name": "test-ds",
            "dataSourceConfiguration": {
                "s3Configuration": {"bucketArn": "arn:aws:s3:::test-bucket"},
                "type": "S3",
            },
        })
        assert resp["dataSource"]["dataSourceId"]

    def test_get_ds(self, kb_id):
        create = _load_handler('CreateDataSource')
        created = create(self.store, {
            "knowledgeBaseId": kb_id, "name": "get-ds",
            "dataSourceConfiguration": {"s3Configuration": {"bucketArn": "arn:aws:s3:::test"}, "type": "S3"},
        })
        get_handler = _load_handler('GetDataSource')
        resp = get_handler(self.store, {
            "knowledgeBaseId": kb_id,
            "dataSourceId": created["dataSource"]["dataSourceId"],
        })
        assert resp["dataSource"]["name"] == "get-ds"

    def test_get_ds_not_found(self, kb_id):
        handler = _load_handler('GetDataSource')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"knowledgeBaseId": kb_id, "dataSourceId": "nonexistent"})

    def test_update_ds(self, kb_id):
        create = _load_handler('CreateDataSource')
        created = create(self.store, {
            "knowledgeBaseId": kb_id, "name": "update-ds",
            "dataSourceConfiguration": {"s3Configuration": {"bucketArn": "arn:aws:s3:::test"}, "type": "S3"},
        })
        ds_id = created["dataSource"]["dataSourceId"]
        update = _load_handler('UpdateDataSource')
        resp = update(self.store, {
            "knowledgeBaseId": kb_id, "dataSourceId": ds_id,
            "name": "updated-ds",
            "dataSourceConfiguration": {"s3Configuration": {"bucketArn": "arn:aws:s3:::test"}, "type": "S3"},
        })
        assert resp["dataSource"]["name"] == "updated-ds"

    def test_delete_ds(self, kb_id):
        create = _load_handler('CreateDataSource')
        created = create(self.store, {
            "knowledgeBaseId": kb_id, "name": "delete-ds",
            "dataSourceConfiguration": {"s3Configuration": {"bucketArn": "arn:aws:s3:::test"}, "type": "S3"},
        })
        ds_id = created["dataSource"]["dataSourceId"]
        handler = _load_handler('DeleteDataSource')
        resp = handler(self.store, {"knowledgeBaseId": kb_id, "dataSourceId": ds_id})
        assert resp["dataSourceId"] == ds_id
        assert resp["status"] == "DELETING"

    def test_list_ds(self, kb_id):
        create = _load_handler('CreateDataSource')
        create(self.store, {
            "knowledgeBaseId": kb_id, "name": "ds1",
            "dataSourceConfiguration": {"s3Configuration": {"bucketArn": "arn:aws:s3:::test"}, "type": "S3"},
        })
        create(self.store, {
            "knowledgeBaseId": kb_id, "name": "ds2",
            "dataSourceConfiguration": {"s3Configuration": {"bucketArn": "arn:aws:s3:::test"}, "type": "S3"},
        })
        handler = _load_handler('ListDataSources')
        resp = handler(self.store, {"knowledgeBaseId": kb_id})
        assert len(resp["dataSourceSummaries"]) == 2


# ═════════════════════════════════════════════════════════════════════
# Tags
# ═════════════════════════════════════════════════════════════════════

class TestTags:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = BedrockAgentStore()
        return self._store

    def test_tag_resource(self):
        handler = _load_handler('TagResource')
        handler(self.store, {
            "resourceArn": "arn:aws:bedrock:us-east-1:000000000000:agent/test",
            "tags": {"env": "prod", "owner": "team-a"},
        })
        list_handler = _load_handler('ListTagsForResource')
        resp = list_handler(self.store, {
            "resourceArn": "arn:aws:bedrock:us-east-1:000000000000:agent/test"
        })
        assert resp["tags"] == {"env": "prod", "owner": "team-a"}

    def test_untag_resource(self):
        handler = _load_handler('TagResource')
        handler(self.store, {
            "resourceArn": "arn:aws:bedrock:us-east-1:000000000000:agent/test2",
            "tags": {"env": "test", "temp": "yes"},
        })
        untag = _load_handler('UntagResource')
        untag(self.store, {
            "resourceArn": "arn:aws:bedrock:us-east-1:000000000000:agent/test2",
            "tagKeys": ["temp"],
        })
        list_handler = _load_handler('ListTagsForResource')
        resp = list_handler(self.store, {
            "resourceArn": "arn:aws:bedrock:us-east-1:000000000000:agent/test2"
        })
        assert resp["tags"] == {"env": "test"}

    def test_list_tags_empty(self):
        handler = _load_handler('ListTagsForResource')
        resp = handler(self.store, {"resourceArn": "arn:aws:bedrock:us-east-1:000000000000:agent/none"})
        assert resp["tags"] == {}
