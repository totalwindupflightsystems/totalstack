"""
CodePipeline store — pipelines, custom action types, webhooks, tags.
"""
import uuid


# ── Exceptions ─────────────────────────────────────────────────────
class PipelineNotFoundException(Exception):
    pass

class PipelineNameInUseException(Exception):
    pass

class InvalidPipelineStructureException(Exception):
    pass

class InvalidActionDeclarationException(Exception):
    pass

class ActionTypeNotFoundException(Exception):
    pass

class InvalidTagsException(Exception):
    pass

class TooManyTagsException(Exception):
    pass

class PipelineExecutionNotFoundException(Exception):
    pass

class WebhookNotFoundException(Exception):
    pass

class InvalidStageDeclarationException(Exception):
    pass

class InvalidWebhookAuthenticationParametersException(Exception):
    pass

class StageNotFoundException(Exception):
    pass

class InvalidJobException(Exception):
    pass

class JobNotFoundException(Exception):
    pass

class ConflictException(Exception):
    pass

class ValidationException(Exception):
    pass


# ── Data Classes ────────────────────────────────────────────────────
class PipelineExecutionRecord:
    def __init__(self, pipeline_name, execution_id=None, status="InProgress",
                 artifact_revisions=None, start_time=None, last_update_time=None):
        self.pipeline_name = pipeline_name
        self.execution_id = execution_id or str(uuid.uuid4())
        self.status = status
        self.artifact_revisions = artifact_revisions or []
        self.start_time = start_time
        self.last_update_time = last_update_time

    def to_dict(self):
        return {
            "pipelineName": self.pipeline_name,
            "pipelineExecutionId": self.execution_id,
            "status": self.status,
            "artifactRevisions": self.artifact_revisions,
        }


class PipelineRecord:
    def __init__(self, name, role_arn, stages, artifact_store=None,
                 artifact_stores=None, version=1, execution_mode="SUPERSEDED",
                 pipeline_type="V1"):
        self.name = name
        self.role_arn = role_arn
        self.stages = stages or []
        self.artifact_store = artifact_store
        self.artifact_stores = artifact_stores
        self.version = version
        self.execution_mode = execution_mode
        self.pipeline_type = pipeline_type
        self.created = None
        self.updated = None

    def to_dict(self):
        result = {
            "name": self.name,
            "roleArn": self.role_arn,
            "stages": self.stages,
            "version": self.version,
            "executionMode": self.execution_mode,
            "pipelineType": self.pipeline_type,
        }
        if self.artifact_store:
            result["artifactStore"] = self.artifact_store
        if self.artifact_stores:
            result["artifactStores"] = self.artifact_stores
        if self.created:
            result["created"] = self.created
        if self.updated:
            result["updated"] = self.updated
        return result


class CustomActionTypeRecord:
    def __init__(self, category, provider, version, owner="Custom",
                 settings=None, input_artifact_details=None,
                 output_artifact_details=None, configuration_properties=None):
        self.category = category
        self.provider = provider
        self.version = version
        self.owner = owner
        self.settings = settings
        self.input_artifact_details = input_artifact_details or {"minimumCount": 0, "maximumCount": 5}
        self.output_artifact_details = output_artifact_details or {"minimumCount": 0, "maximumCount": 5}
        self.configuration_properties = configuration_properties or []

    @property
    def id_key(self):
        return f"{self.category}/{self.provider}/{self.version}"

    def to_dict(self):
        return {
            "id": {
                "category": self.category,
                "provider": self.provider,
                "version": self.version,
                "owner": self.owner,
            },
            "settings": self.settings,
            "inputArtifactDetails": self.input_artifact_details,
            "outputArtifactDetails": self.output_artifact_details,
            "actionConfigurationProperties": self.configuration_properties,
        }


# ── Store ──────────────────────────────────────────────────────────
class CodePipelineStore:
    def __init__(self):
        self._pipelines: dict[str, PipelineRecord] = {}
        self._custom_action_types: dict[str, CustomActionTypeRecord] = {}
        self._pipeline_executions: dict[str, list[PipelineExecutionRecord]] = {}
        self._tags: dict[str, list[dict]] = {}  # arn → [{key, value}]
        self._webhooks: dict[str, dict] = {}
        self._stage_transitions: dict[str, dict] = {}  # (pipeline, stage) → enabled/disabled/reason
        self._pipeline_states: dict[str, dict] = {}

    @staticmethod
    def _build_arn(service, resource_type, name):
        return f"arn:aws:{service}:us-east-1:000000000000:{resource_type}/{name}"

    # ── Pipeline CRUD ───────────────────────────────────────────────
    def pipelines(self, name=None):
        if name is not None:
            return self._pipelines.get(name)
        return list(self._pipelines.values())

    def create_pipeline(self, name, role_arn, stages, artifact_store=None,
                        artifact_stores=None, execution_mode="SUPERSEDED",
                        pipeline_type="V1", tags=None):
        if name in self._pipelines:
            raise PipelineNameInUseException(f"Pipeline '{name}' already exists")
        record = PipelineRecord(
            name=name, role_arn=role_arn, stages=stages,
            artifact_store=artifact_store, artifact_stores=artifact_stores,
            execution_mode=execution_mode, pipeline_type=pipeline_type,
        )
        self._pipelines[name] = record
        self._pipeline_states[name] = {}
        if tags:
            arn = self._build_arn("codepipeline", "pipeline", name)
            self._tags[arn] = list(tags)
        return record.to_dict()

    def get_pipeline(self, name):
        record = self._pipelines.get(name)
        if not record:
            raise PipelineNotFoundException(f"Pipeline '{name}' not found")
        result = record.to_dict()
        # Include metadata
        metadata = {
            "pipelineArn": self._build_arn("codepipeline", "pipeline", name),
        }
        if name in self._pipeline_states and self._pipeline_states[name]:
            metadata["pipelineState"] = self._pipeline_states[name]
        result["metadata"] = metadata
        return result

    def update_pipeline(self, name, pipeline_obj):
        record = self._pipelines.get(name)
        if not record:
            raise PipelineNotFoundException(f"Pipeline '{name}' not found")
        # pipeline_obj is a dict with the new pipeline definition
        record.role_arn = pipeline_obj.get("roleArn", record.role_arn)
        record.stages = pipeline_obj.get("stages", record.stages)
        record.artifact_store = pipeline_obj.get("artifactStore", record.artifact_store)
        record.artifact_stores = pipeline_obj.get("artifactStores", record.artifact_stores)
        record.execution_mode = pipeline_obj.get("executionMode", record.execution_mode)
        record.pipeline_type = pipeline_obj.get("pipelineType", record.pipeline_type)
        record.version += 1
        return record.to_dict()

    def delete_pipeline(self, name):
        if name not in self._pipelines:
            raise PipelineNotFoundException(f"Pipeline '{name}' not found")
        del self._pipelines[name]
        if name in self._pipeline_executions:
            del self._pipeline_executions[name]
        arn = self._build_arn("codepipeline", "pipeline", name)
        if arn in self._tags:
            del self._tags[arn]
        return {}

    def list_pipelines(self, next_token=None, max_results=None):
        items = []
        for name, record in self._pipelines.items():
            items.append({
                "name": record.name,
                "version": record.version,
                "pipelineType": record.pipeline_type,
                "executionMode": record.execution_mode,
                "created": record.created,
                "updated": record.updated,
            })
        start = int(next_token) if next_token else 0
        end = start + max_results if max_results else len(items)
        result = {"pipelines": items[start:end]}
        if end < len(items):
            result["nextToken"] = str(end)
        return result

    # ── Pipeline Executions ──────────────────────────────────────────
    def start_pipeline_execution(self, name, client_request_token=None,
                                  source_revision=None, variables=None):
        record = self._pipelines.get(name)
        if not record:
            raise PipelineNotFoundException(f"Pipeline '{name}' not found")
        execution = PipelineExecutionRecord(pipeline_name=name)
        if name not in self._pipeline_executions:
            self._pipeline_executions[name] = []
        self._pipeline_executions[name].append(execution)
        self._pipeline_states[name] = {"status": "InProgress",
                                        "currentStage": record.stages[0].get("name", "") if record.stages else ""}
        return {"pipelineExecutionId": execution.execution_id}

    def stop_pipeline_execution(self, pipeline_name, pipeline_execution_id, abandon=False, reason=None):
        if pipeline_name not in self._pipeline_executions:
            raise PipelineExecutionNotFoundException(
                f"Execution '{pipeline_execution_id}' not found for pipeline '{pipeline_name}'")
        for ex in self._pipeline_executions[pipeline_name]:
            if ex.execution_id == pipeline_execution_id:
                ex.status = "Abandoned" if abandon else "Stopped"
                return {"pipelineExecutionId": pipeline_execution_id}
        raise PipelineExecutionNotFoundException(
            f"Execution '{pipeline_execution_id}' not found for pipeline '{pipeline_name}'")

    def get_pipeline_execution(self, pipeline_name, pipeline_execution_id):
        if pipeline_name not in self._pipeline_executions:
            raise PipelineExecutionNotFoundException(
                f"Execution '{pipeline_execution_id}' not found")
        for ex in self._pipeline_executions[pipeline_name]:
            if ex.execution_id == pipeline_execution_id:
                return {"pipelineExecution": ex.to_dict()}
        raise PipelineExecutionNotFoundException(
            f"Execution '{pipeline_execution_id}' not found")

    def list_pipeline_executions(self, pipeline_name, next_token=None, max_results=None):
        executions = self._pipeline_executions.get(pipeline_name, [])
        items = [ex.to_dict() for ex in executions]
        start = int(next_token) if next_token else 0
        end = start + max_results if max_results else len(items)
        result = {"pipelineExecutionSummaries": items[start:end]}
        if end < len(items):
            result["nextToken"] = str(end)
        return result

    def get_pipeline_state(self, name):
        """
        Returns the state of the pipeline — stages, actions, transitions.
        """
        record = self._pipelines.get(name)
        if not record:
            raise PipelineNotFoundException(f"Pipeline '{name}' not found")
        self._pipeline_states.get(name, {})  # no-op: state tracking
        stage_states = []
        for stage in record.stages:
            stage_name = stage.get("name", "")
            stage_state = {
                "stageName": stage_name,
                "inboundTransition": self._stage_transitions.get(f"{name}/{stage_name}", {}),
                "actionStates": [],
            }
            for action in stage.get("actions", []):
                action_name = action.get("name", "")
                stage_state["actionStates"].append({
                    "actionName": action_name,
                    "currentRevision": {},
                    "latestExecution": {},
                    "entityUrl": "",
                })
            stage_states.append(stage_state)

        return {
            "pipelineName": name,
            "pipelineVersion": record.version,
            "stageStates": stage_states,
            "created": record.created,
            "updated": record.updated,
        }

    # ── Custom Action Types ──────────────────────────────────────────
    def action_types(self, key=None):
        if key is not None:
            return self._custom_action_types.get(key)
        return list(self._custom_action_types.values())

    def create_custom_action_type(self, category, provider, version,
                                   input_artifact_details, output_artifact_details,
                                   settings=None, configuration_properties=None,
                                   tags=None):
        record = CustomActionTypeRecord(
            category=category, provider=provider, version=version,
            settings=settings, input_artifact_details=input_artifact_details,
            output_artifact_details=output_artifact_details,
            configuration_properties=configuration_properties,
        )
        key = record.id_key
        if key in self._custom_action_types:
            raise ConflictException(f"Action type '{key}' already exists")
        self._custom_action_types[key] = record
        if tags:
            arn = self._build_arn("codepipeline", "actiontype", f"{category}/{provider}/{version}")
            self._tags[arn] = list(tags)
        return {"actionType": record.to_dict()}

    def get_action_type(self, category, owner, provider, version):
        key = f"{category}/{provider}/{version}"
        record = self._custom_action_types.get(key)
        if not record or record.owner != owner:
            raise ActionTypeNotFoundException(f"Action type '{key}' not found")
        return {"actionType": record.to_dict()}

    def delete_custom_action_type(self, category, provider, version):
        key = f"{category}/{provider}/{version}"
        if key not in self._custom_action_types:
            raise ActionTypeNotFoundException(f"Action type '{key}' not found")
        del self._custom_action_types[key]
        return {}

    def update_action_type(self, action_type):
        cat = action_type.get("id", {}).get("category", "")
        prov = action_type.get("id", {}).get("provider", "")
        ver = action_type.get("id", {}).get("version", "")
        key = f"{cat}/{prov}/{ver}"
        record = self._custom_action_types.get(key)
        if not record:
            raise ActionTypeNotFoundException(f"Action type '{key}' not found")
        if "settings" in action_type:
            record.settings = action_type["settings"]
        if "inputArtifactDetails" in action_type:
            record.input_artifact_details = action_type["inputArtifactDetails"]
        if "outputArtifactDetails" in action_type:
            record.output_artifact_details = action_type["outputArtifactDetails"]
        if "actionConfigurationProperties" in action_type:
            record.configuration_properties = action_type["actionConfigurationProperties"]
        return {}

    def list_action_types(self, action_owner_filter=None, next_token=None, region_filter=None):
        items = []
        for key, record in self._custom_action_types.items():
            if action_owner_filter and record.owner != action_owner_filter:
                continue
            items.append(record.to_dict())
        start = int(next_token) if next_token else 0
        end = start + 100  # reasonable page size
        result = {"actionTypes": items[start:end]}
        if end < len(items):
            result["nextToken"] = str(end)
        return result

    # ── Tags ──────────────────────────────────────────────────────────
    def tag_resource(self, resource_arn, tags):
        if not tags:
            raise InvalidTagsException("At least one tag is required")
        if len(tags) > 50:
            raise TooManyTagsException("Maximum 50 tags allowed")
        if resource_arn not in self._tags:
            self._tags[resource_arn] = []
        existing_keys = {t["Key"] for t in self._tags[resource_arn]}
        for tag in tags:
            if tag["Key"] in existing_keys:
                # Update existing tag
                for t in self._tags[resource_arn]:
                    if t["Key"] == tag["Key"]:
                        t["Value"] = tag["Value"]
                        break
            else:
                self._tags[resource_arn].append({"Key": tag["Key"], "Value": tag["Value"]})
        return {}

    def untag_resource(self, resource_arn, tag_keys):
        if resource_arn not in self._tags:
            return {}
        self._tags[resource_arn] = [
            t for t in self._tags[resource_arn]
            if t["Key"] not in tag_keys
        ]
        return {}

    def list_tags_for_resource(self, resource_arn, next_token=None, max_results=None):
        tags = self._tags.get(resource_arn, [])
        result = {"tags": list(tags)}
        return result

    # ── Stage Transitions ────────────────────────────────────────────
    def disable_stage_transition(self, pipeline_name, stage_name, transition_type, reason):
        record = self._pipelines.get(pipeline_name)
        if not record:
            raise PipelineNotFoundException(f"Pipeline '{pipeline_name}' not found")
        stage_names = [s.get("name", "") for s in record.stages]
        if stage_name not in stage_names:
            raise StageNotFoundException(f"Stage '{stage_name}' not found")
        key = f"{pipeline_name}/{stage_name}"
        self._stage_transitions[key] = {
            "enabled": False,
            "lastChangedBy": "system",
            "reason": reason or "",
        }
        return {}

    def enable_stage_transition(self, pipeline_name, stage_name, transition_type):
        record = self._pipelines.get(pipeline_name)
        if not record:
            raise PipelineNotFoundException(f"Pipeline '{pipeline_name}' not found")
        stage_names = [s.get("name", "") for s in record.stages]
        if stage_name not in stage_names:
            raise StageNotFoundException(f"Stage '{stage_name}' not found")
        key = f"{pipeline_name}/{stage_name}"
        self._stage_transitions[key] = {
            "enabled": True,
            "lastChangedBy": "system",
            "reason": "",
        }
        return {}
