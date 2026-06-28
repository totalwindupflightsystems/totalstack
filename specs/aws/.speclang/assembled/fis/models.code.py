"""FIS Store — ExperimentTemplate, Experiment, Action entities."""
import time as _time
import uuid as _uuid


class ResourceNotFoundException(Exception):
    pass


class ConflictException(Exception):
    pass


class ValidationException(Exception):
    pass


class ExperimentTemplateRecord:
    def __init__(self, id=None, description=None, roleArn=None, actions=None,
                 stopConditions=None, targets=None, tags=None,
                 creationTime=None):
        self.id = id or f"EXT-{_uuid.uuid4().hex[:10]}"
        self.description = description or ""
        self.roleArn = roleArn or ""
        self.actions = actions or {}
        self.stopConditions = stopConditions or []
        self.targets = targets or {}
        self.tags = tags or {}
        self.creationTime = creationTime or _time.time()

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "roleArn": self.roleArn,
            "actions": self.actions,
            "stopConditions": self.stopConditions,
            "targets": self.targets,
            "tags": self.tags,
            "creationTime": self.creationTime,
        }


class ExperimentRecord:
    def __init__(self, id=None, experimentTemplateId=None,
                 status="running", startTime=None):
        self.id = id or f"EXP-{_uuid.uuid4().hex[:10]}"
        self.experimentTemplateId = experimentTemplateId
        self.status = status
        self.startTime = startTime or _time.time()

    def to_dict(self):
        return {
            "id": self.id,
            "experimentTemplateId": self.experimentTemplateId,
            "status": self.status,
            "startTime": self.startTime,
        }


class FISStore:
    def __init__(self):
        self._templates: dict[str, ExperimentTemplateRecord] = {}
        self._experiments: dict[str, ExperimentRecord] = {}

    # ── ExperimentTemplate ──
    def create_experiment_template(self, **kwargs):
        record = ExperimentTemplateRecord(**kwargs)
        self._templates[record.id] = record
        return record.to_dict()

    def describe_experiment_template(self, id):
        record = self._templates.get(id)
        if not record:
            raise ResourceNotFoundException(f"Template {id} not found")
        return record.to_dict()

    def list_experiment_templates(self, **kwargs):
        return [r.to_dict() for r in self._templates.values()]

    def delete_experiment_template(self, id):
        if id not in self._templates:
            raise ResourceNotFoundException(f"Template {id} not found")
        del self._templates[id]

    def update_experiment_template(self, **kwargs):
        tid = kwargs["id"]
        record = self._templates.get(tid)
        if not record:
            raise ResourceNotFoundException(f"Template {tid} not found")
        for key in ("description", "actions", "stopConditions", "targets", "roleArn"):
            if key in kwargs:
                setattr(record, key, kwargs[key])
        return record.to_dict()

    # ── Experiment ──
    def start_experiment(self, **kwargs):
        record = ExperimentRecord(**kwargs)
        self._experiments[record.id] = record
        return record.to_dict()

    def describe_experiment(self, id):
        record = self._experiments.get(id)
        if not record:
            raise ResourceNotFoundException(f"Experiment {id} not found")
        return record.to_dict()

    def list_experiments(self, **kwargs):
        return [r.to_dict() for r in self._experiments.values()]

    def stop_experiment(self, id):
        record = self._experiments.get(id)
        if not record:
            raise ResourceNotFoundException(f"Experiment {id} not found")
        record.status = "stopped"
        return record.to_dict()

    def delete_experiment(self, id):
        if id not in self._experiments:
            raise ResourceNotFoundException(f"Experiment {id} not found")
        del self._experiments[id]
