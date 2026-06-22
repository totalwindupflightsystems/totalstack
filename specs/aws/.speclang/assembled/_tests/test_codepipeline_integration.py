"""Integration tests for CodePipeline — real store, generated handlers."""
import pytest
import os
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'codepipeline')

# ── Load models.code.py ──────────────────────────────────────────────
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

CodePipelineStore = models_mod.CodePipelineStore
PipelineRecord = models_mod.PipelineRecord
CustomActionTypeRecord = models_mod.CustomActionTypeRecord
PipelineExecutionRecord = models_mod.PipelineExecutionRecord
PipelineNotFoundException = models_mod.PipelineNotFoundException
PipelineNameInUseException = models_mod.PipelineNameInUseException
ActionTypeNotFoundException = models_mod.ActionTypeNotFoundException
ConflictException = models_mod.ConflictException
PipelineExecutionNotFoundException = models_mod.PipelineExecutionNotFoundException
StageNotFoundException = models_mod.StageNotFoundException
InvalidTagsException = models_mod.InvalidTagsException
TooManyTagsException = models_mod.TooManyTagsException

# ── Helper: load handler ─────────────────────────────────────────────
def _load_handler(op_name):
    """Load a single-handler .code.py file — injects exceptions, records, stdlib."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exceptions
    mod.PipelineNotFoundException = PipelineNotFoundException
    mod.PipelineNameInUseException = PipelineNameInUseException
    mod.ActionTypeNotFoundException = ActionTypeNotFoundException
    mod.ConflictException = ConflictException
    mod.PipelineExecutionNotFoundException = PipelineExecutionNotFoundException
    mod.StageNotFoundException = StageNotFoundException
    mod.InvalidTagsException = InvalidTagsException
    mod.TooManyTagsException = TooManyTagsException
    # Inject record classes
    mod.PipelineRecord = PipelineRecord
    mod.CustomActionTypeRecord = CustomActionTypeRecord
    mod.PipelineExecutionRecord = PipelineExecutionRecord
    spec.loader.exec_module(mod)
    # Find handler (not injected globals)
    skip_names = {'PipelineNotFoundException', 'PipelineNameInUseException',
                  'ActionTypeNotFoundException', 'ConflictException',
                  'PipelineExecutionNotFoundException', 'StageNotFoundException',
                  'InvalidTagsException', 'TooManyTagsException',
                  'PipelineRecord', 'CustomActionTypeRecord', 'PipelineExecutionRecord'}
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    if handler is None:
        raise RuntimeError(f"No handler found in {op_name}.code.py")
    return handler


# ── Helpers ──────────────────────────────────────────────────────────
def _pipeline_def(name="test-pipeline"):
    return {
        "name": name,
        "roleArn": "arn:aws:iam::000000000000:role/test-role",
        "artifactStore": {
            "type": "S3",
            "location": "test-bucket",
        },
        "stages": [
            {
                "name": "Source",
                "actions": [
                    {
                        "name": "SourceAction",
                        "actionTypeId": {
                            "category": "Source",
                            "owner": "AWS",
                            "provider": "CodeCommit",
                            "version": "1",
                        },
                        "outputArtifacts": [{"name": "SourceOutput"}],
                        "configuration": {"BranchName": "main", "RepositoryName": "test-repo"},
                        "runOrder": 1,
                    },
                ],
            },
            {
                "name": "Build",
                "actions": [
                    {
                        "name": "BuildAction",
                        "actionTypeId": {
                            "category": "Build",
                            "owner": "AWS",
                            "provider": "CodeBuild",
                            "version": "1",
                        },
                        "inputArtifacts": [{"name": "SourceOutput"}],
                        "outputArtifacts": [{"name": "BuildOutput"}],
                        "configuration": {"ProjectName": "test-project"},
                        "runOrder": 1,
                    },
                ],
            },
        ],
    }


# ═══════════════════════════════════════════════════════════════════════
# Pipeline CRUD
# ═══════════════════════════════════════════════════════════════════════

class TestPipelineCRUD:
    @pytest.fixture
    def store(self):
        return CodePipelineStore()

    # ── Create ────────────────────────────────────────────────────────

    def test_create_pipeline_happy(self, store):
        handler = _load_handler('CreatePipeline')
        response = handler(store, {"pipeline": _pipeline_def("p1")})
        assert response is not None
        assert "name" in response

    def test_create_pipeline_with_tags(self, store):
        handler = _load_handler('CreatePipeline')
        response = handler(store, {
            "pipeline": _pipeline_def("p-tagged"),
            "tags": [{"Key": "env", "Value": "test"}],
        })
        assert response["name"] == "p-tagged"

    def test_create_duplicate_fails(self, store):
        handler = _load_handler('CreatePipeline')
        handler(store, {"pipeline": _pipeline_def("p-dup")})
        with pytest.raises(PipelineNameInUseException):
            handler(store, {"pipeline": _pipeline_def("p-dup")})

    def test_create_missing_pipeline(self, store):
        handler = _load_handler('CreatePipeline')
        with pytest.raises(KeyError):
            handler(store, {})

    # ── Get ──────────────────────────────────────────────────────────

    def test_get_pipeline_happy(self, store):
        create = _load_handler('CreatePipeline')
        get = _load_handler('GetPipeline')
        create(store, {"pipeline": _pipeline_def("p-get")})
        response = get(store, {"name": "p-get"})
        assert "name" in response
        assert "roleArn" in response
        assert "metadata" in response
        assert "pipelineArn" in response["metadata"]

    def test_get_pipeline_nonexistent(self, store):
        handler = _load_handler('GetPipeline')
        with pytest.raises(PipelineNotFoundException):
            handler(store, {"name": "no-such-pipeline"})

    # ── List ─────────────────────────────────────────────────────────

    def test_list_pipelines_empty(self, store):
        handler = _load_handler('ListPipelines')
        response = handler(store, {})
        assert "pipelines" in response
        assert len(response["pipelines"]) == 0

    def test_list_pipelines_with_items(self, store):
        create = _load_handler('CreatePipeline')
        list_handler = _load_handler('ListPipelines')
        create(store, {"pipeline": _pipeline_def("p-a")})
        create(store, {"pipeline": _pipeline_def("p-b")})
        response = list_handler(store, {})
        assert len(response["pipelines"]) == 2

    # ── Update ───────────────────────────────────────────────────────

    def test_update_pipeline_happy(self, store):
        create = _load_handler('CreatePipeline')
        update = _load_handler('UpdatePipeline')
        get = _load_handler('GetPipeline')
        create(store, {"pipeline": _pipeline_def("p-upd")})
        new_def = _pipeline_def("p-upd")
        new_def["roleArn"] = "arn:aws:iam::000000000000:role/updated-role"
        update(store, {"pipeline": new_def})
        response = get(store, {"name": "p-upd"})
        assert response["roleArn"] == "arn:aws:iam::000000000000:role/updated-role"

    def test_update_pipeline_nonexistent(self, store):
        handler = _load_handler('UpdatePipeline')
        with pytest.raises(PipelineNotFoundException):
            handler(store, {"pipeline": _pipeline_def("no-such")})

    # ── Delete ────────────────────────────────────────────────────────

    def test_delete_pipeline_happy(self, store):
        create = _load_handler('CreatePipeline')
        delete = _load_handler('DeletePipeline')
        get = _load_handler('GetPipeline')
        create(store, {"pipeline": _pipeline_def("p-del")})
        delete(store, {"name": "p-del"})
        with pytest.raises(PipelineNotFoundException):
            get(store, {"name": "p-del"})

    def test_delete_pipeline_nonexistent(self, store):
        handler = _load_handler('DeletePipeline')
        with pytest.raises(PipelineNotFoundException):
            handler(store, {"name": "no-such"})


# ═══════════════════════════════════════════════════════════════════════
# Pipeline Executions
# ═══════════════════════════════════════════════════════════════════════

class TestPipelineExecutions:
    @pytest.fixture
    def store(self):
        s = CodePipelineStore()
        # Pre-create a pipeline
        s.create_pipeline(
            **_pipeline_def("p-exec")["pipeline"]
            if "pipeline" in _pipeline_def("p-exec")
            else _pipeline_def("p-exec"))
        return s

    @pytest.fixture
    def store_with_pipeline(self):
        s = CodePipelineStore()
        pd = _pipeline_def("p-exec2")
        s.create_pipeline(
            name=pd["name"],
            role_arn=pd["roleArn"],
            stages=pd["stages"],
            artifact_store=pd.get("artifactStore"),
        )
        return s

    def test_start_execution_happy(self, store_with_pipeline):
        handler = _load_handler('StartPipelineExecution')
        response = handler(store_with_pipeline, {"name": "p-exec2"})
        assert "pipelineExecutionId" in response
        assert response["pipelineExecutionId"] is not None

    def test_start_execution_nonexistent_pipeline(self, store_with_pipeline):
        handler = _load_handler('StartPipelineExecution')
        with pytest.raises(PipelineNotFoundException):
            handler(store_with_pipeline, {"name": "no-such"})

    def test_get_execution_happy(self, store_with_pipeline):
        start = _load_handler('StartPipelineExecution')
        get_ex = _load_handler('GetPipelineExecution')
        result = start(store_with_pipeline, {"name": "p-exec2"})
        ex_id = result["pipelineExecutionId"]
        response = get_ex(store_with_pipeline, {
            "pipelineName": "p-exec2",
            "pipelineExecutionId": ex_id,
        })
        assert "pipelineExecution" in response
        assert response["pipelineExecution"]["status"] == "InProgress"

    def test_list_executions(self, store_with_pipeline):
        start = _load_handler('StartPipelineExecution')
        list_ex = _load_handler('ListPipelineExecutions')
        start(store_with_pipeline, {"name": "p-exec2"})
        start(store_with_pipeline, {"name": "p-exec2"})
        response = list_ex(store_with_pipeline, {"pipelineName": "p-exec2"})
        assert len(response["pipelineExecutionSummaries"]) == 2

    def test_stop_execution_happy(self, store_with_pipeline):
        start = _load_handler('StartPipelineExecution')
        stop = _load_handler('StopPipelineExecution')
        get_ex = _load_handler('GetPipelineExecution')
        result = start(store_with_pipeline, {"name": "p-exec2"})
        ex_id = result["pipelineExecutionId"]
        stop(store_with_pipeline, {
            "pipelineName": "p-exec2",
            "pipelineExecutionId": ex_id,
        })
        response = get_ex(store_with_pipeline, {
            "pipelineName": "p-exec2",
            "pipelineExecutionId": ex_id,
        })
        assert response["pipelineExecution"]["status"] == "Stopped"

    def test_stop_execution_nonexistent(self, store_with_pipeline):
        handler = _load_handler('StopPipelineExecution')
        with pytest.raises(PipelineExecutionNotFoundException):
            handler(store_with_pipeline, {
                "pipelineName": "p-exec2",
                "pipelineExecutionId": "nonexistent-id",
            })

    def test_get_pipeline_state(self, store_with_pipeline):
        handler = _load_handler('GetPipelineState')
        response = handler(store_with_pipeline, {"name": "p-exec2"})
        assert response["pipelineName"] == "p-exec2"
        assert "stageStates" in response
        assert len(response["stageStates"]) == 2


# ═══════════════════════════════════════════════════════════════════════
# Custom Action Types
# ═══════════════════════════════════════════════════════════════════════

class TestCustomActionTypes:
    @pytest.fixture
    def store(self):
        return CodePipelineStore()

    def _action_type_req(self, category="Test", provider="TestProvider", version="1"):
        return {
            "category": category,
            "provider": provider,
            "version": version,
            "inputArtifactDetails": {"minimumCount": 0, "maximumCount": 5},
            "outputArtifactDetails": {"minimumCount": 0, "maximumCount": 5},
        }

    def test_create_action_type_happy(self, store):
        handler = _load_handler('CreateCustomActionType')
        response = handler(store, self._action_type_req())
        assert "actionType" in response
        at = response["actionType"]
        assert at["id"]["category"] == "Test"
        assert at["id"]["provider"] == "TestProvider"
        assert at["id"]["version"] == "1"

    def test_create_duplicate_fails(self, store):
        handler = _load_handler('CreateCustomActionType')
        handler(store, self._action_type_req())
        with pytest.raises(ConflictException):
            handler(store, self._action_type_req())

    def test_get_action_type_happy(self, store):
        create = _load_handler('CreateCustomActionType')
        get_at = _load_handler('GetActionType')
        create(store, self._action_type_req())
        response = get_at(store, {
            "category": "Test",
            "owner": "Custom",
            "provider": "TestProvider",
            "version": "1",
        })
        assert response["actionType"]["id"]["category"] == "Test"

    def test_get_action_type_nonexistent(self, store):
        handler = _load_handler('GetActionType')
        with pytest.raises(ActionTypeNotFoundException):
            handler(store, {
                "category": "Test",
                "owner": "Custom",
                "provider": "Nonexistent",
                "version": "1",
            })

    def test_list_action_types(self, store):
        create = _load_handler('CreateCustomActionType')
        list_at = _load_handler('ListActionTypes')
        create(store, self._action_type_req("Cat1", "Prov1", "1"))
        create(store, self._action_type_req("Cat2", "Prov2", "1"))
        response = list_at(store, {})
        assert len(response["actionTypes"]) == 2

    def test_delete_action_type_happy(self, store):
        create = _load_handler('CreateCustomActionType')
        delete = _load_handler('DeleteCustomActionType')
        get_at = _load_handler('GetActionType')
        create(store, self._action_type_req())
        delete(store, {"category": "Test", "provider": "TestProvider", "version": "1"})
        with pytest.raises(ActionTypeNotFoundException):
            get_at(store, {
                "category": "Test",
                "owner": "Custom",
                "provider": "TestProvider",
                "version": "1",
            })

    def test_update_action_type_happy(self, store):
        create = _load_handler('CreateCustomActionType')
        update = _load_handler('UpdateActionType')
        get_at = _load_handler('GetActionType')
        create(store, self._action_type_req())
        update(store, {
            "actionType": {
                "id": {"category": "Test", "provider": "TestProvider", "version": "1"},
                "settings": {"entityUrlTemplate": "https://example.com"},
                "inputArtifactDetails": {"minimumCount": 1, "maximumCount": 5},
                "outputArtifactDetails": {"minimumCount": 0, "maximumCount": 5},
            }
        })
        response = get_at(store, {
            "category": "Test",
            "owner": "Custom",
            "provider": "TestProvider",
            "version": "1",
        })
        assert response["actionType"]["inputArtifactDetails"]["minimumCount"] == 1

    def test_update_action_type_nonexistent(self, store):
        handler = _load_handler('UpdateActionType')
        with pytest.raises(ActionTypeNotFoundException):
            handler(store, {
                "actionType": {
                    "id": {"category": "X", "provider": "Y", "version": "1"},
                }
            })


# ═══════════════════════════════════════════════════════════════════════
# Stage Transitions
# ═══════════════════════════════════════════════════════════════════════

class TestStageTransitions:
    @pytest.fixture
    def store(self):
        s = CodePipelineStore()
        pd = _pipeline_def("p-trans")
        s.create_pipeline(
            name=pd["name"],
            role_arn=pd["roleArn"],
            stages=pd["stages"],
            artifact_store=pd.get("artifactStore"),
        )
        return s

    def test_disable_stage_transition(self, store):
        handler = _load_handler('DisableStageTransition')
        handler(store, {
            "pipelineName": "p-trans",
            "stageName": "Source",
            "transitionType": "Inbound",
            "reason": "testing",
        })
        state_handler = _load_handler('GetPipelineState')
        state = state_handler(store, {"name": "p-trans"})
        assert len(state["stageStates"]) >= 1

    def test_enable_stage_transition(self, store):
        disable = _load_handler('DisableStageTransition')
        enable = _load_handler('EnableStageTransition')
        disable(store, {
            "pipelineName": "p-trans",
            "stageName": "Source",
            "transitionType": "Inbound",
            "reason": "testing",
        })
        enable(store, {
            "pipelineName": "p-trans",
            "stageName": "Source",
            "transitionType": "Inbound",
        })
        # Should not raise
        assert True

    def test_disable_nonexistent_pipeline(self, store):
        handler = _load_handler('DisableStageTransition')
        with pytest.raises(PipelineNotFoundException):
            handler(store, {
                "pipelineName": "no-such",
                "stageName": "Source",
                "transitionType": "Inbound",
                "reason": "testing",
            })

    def test_disable_nonexistent_stage(self, store):
        handler = _load_handler('DisableStageTransition')
        with pytest.raises(StageNotFoundException):
            handler(store, {
                "pipelineName": "p-trans",
                "stageName": "NoSuchStage",
                "transitionType": "Inbound",
                "reason": "testing",
            })


# ═══════════════════════════════════════════════════════════════════════
# Tags
# ═══════════════════════════════════════════════════════════════════════

class TestTags:
    @pytest.fixture
    def store(self):
        s = CodePipelineStore()
        pd = _pipeline_def("p-tags")
        s.create_pipeline(
            name=pd["name"],
            role_arn=pd["roleArn"],
            stages=pd["stages"],
            artifact_store=pd.get("artifactStore"),
        )
        return s

    def test_tag_resource_happy(self, store):
        handler = _load_handler('TagResource')
        handler(store, {
            "resourceArn": "arn:aws:codepipeline:us-east-1:000000000000:pipeline/p-tags",
            "tags": [{"Key": "env", "Value": "prod"}, {"Key": "team", "Value": "platform"}],
        })
        list_handler = _load_handler('ListTagsForResource')
        response = list_handler(store, {
            "resourceArn": "arn:aws:codepipeline:us-east-1:000000000000:pipeline/p-tags",
        })
        tags = response["tags"]
        assert len(tags) == 2

    def test_list_tags_empty(self, store):
        handler = _load_handler('ListTagsForResource')
        response = handler(store, {
            "resourceArn": "arn:aws:codepipeline:us-east-1:000000000000:pipeline/p-tags",
        })
        assert response["tags"] == []

    def test_untag_resource(self, store):
        tag = _load_handler('TagResource')
        untag = _load_handler('UntagResource')
        list_tags = _load_handler('ListTagsForResource')
        arn = "arn:aws:codepipeline:us-east-1:000000000000:pipeline/p-tags"
        tag(store, {"resourceArn": arn, "tags": [{"Key": "env", "Value": "prod"}]})
        untag(store, {"resourceArn": arn, "tagKeys": ["env"]})
        response = list_tags(store, {"resourceArn": arn})
        assert len(response["tags"]) == 0

    def test_tag_resource_empty_tags(self, store):
        handler = _load_handler('TagResource')
        with pytest.raises(InvalidTagsException):
            handler(store, {
                "resourceArn": "arn:aws:codepipeline:us-east-1:000000000000:pipeline/p-tags",
                "tags": [],
            })
