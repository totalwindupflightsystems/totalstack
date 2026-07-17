"""FraudDetector store — 5 entities: Detector, Variable, Model, EventType, Rule."""
import time as _time

class ValidationException(Exception): pass
class ResourceNotFoundException(Exception): pass
class InternalServerException(Exception): pass
class ThrottlingException(Exception): pass
class AccessDeniedException(Exception): pass
class ConflictException(Exception): pass

def _tag_dict(tags):
    if not tags: return {}
    if isinstance(tags, list):
        r = {}
        for t in tags:
            r[t.get("key", "") or t.get("Key", "")] = t.get("value", "") or t.get("Value", "")
        return r
    return dict(tags)

def _arn(rtype, name):
    return f"arn:aws:frauddetector:us-east-1:123456789012:{rtype}/{name}"

class DetectorRecord:
    def __init__(self, detectorId, eventTypeName, description=None, tags=None, arn=None):
        self.detectorId = detectorId
        self.eventTypeName = eventTypeName
        self.description = description
        self.tags = _tag_dict(tags)
        self.arn = arn or _arn("detector", detectorId)
        self.createdTime = _time.time()
    def to_dict(self):
        return {"detectorId": self.detectorId, "eventTypeName": self.eventTypeName,
                "description": self.description, "createdTime": self.createdTime}

class VariableRecord:
    def __init__(self, name, dataType, dataSource, defaultValue,
                 description=None, variableType=None, tags=None):
        self.name = name
        self.dataType = dataType
        self.dataSource = dataSource
        self.defaultValue = defaultValue
        self.description = description
        self.variableType = variableType
        self.tags = _tag_dict(tags)
        self.createdTime = _time.time()
    def to_dict(self):
        return {"name": self.name, "dataType": self.dataType, "dataSource": self.dataSource,
                "defaultValue": self.defaultValue, "createdTime": self.createdTime}

class ModelRecord:
    def __init__(self, modelId, modelType, eventTypeName, description=None, tags=None):
        self.modelId = modelId
        self.modelType = modelType
        self.eventTypeName = eventTypeName
        self.description = description
        self.tags = _tag_dict(tags)
        self.createdTime = _time.time()
    def to_dict(self):
        return {"modelId": self.modelId, "modelType": self.modelType,
                "eventTypeName": self.eventTypeName, "createdTime": self.createdTime}

class EventTypeRecord:
    def __init__(self, name, eventVariables, entityTypes, description=None,
                 labels=None, eventIngestion=None, tags=None, eventOrchestration=None):
        self.name = name
        self.eventVariables = eventVariables or []
        self.entityTypes = entityTypes or []
        self.description = description
        self.labels = labels or []
        self.tags = _tag_dict(tags)
        self.eventIngestion = eventIngestion
        self.eventOrchestration = eventOrchestration
        self.createdTime = _time.time()
    def to_dict(self):
        return {"name": self.name, "eventVariables": self.eventVariables,
                "entityTypes": self.entityTypes, "createdTime": self.createdTime}

class RuleRecord:
    def __init__(self, ruleId, detectorId, expression, language, outcomes,
                 description=None, tags=None):
        self.ruleId = ruleId
        self.detectorId = detectorId
        self.expression = expression
        self.language = language or "DETECTORPL"
        self.outcomes = outcomes or []
        self.description = description
        self.tags = _tag_dict(tags)
        self.createdTime = _time.time()
    def to_dict(self):
        return {"ruleId": self.ruleId, "detectorId": self.detectorId,
                "ruleVersion": "1",
                "expression": self.expression, "language": self.language, "createdTime": self.createdTime}

class FraudDetectorStore:
    def __init__(self):
        self._detectors = {}
        self._variables = {}
        self._models = {}
        self._eventtypes = {}
        self._rules = {}

    def detectors(self, detectorId=None):
        if detectorId: return self._detectors.get(detectorId)
        return list(self._detectors.values())

    def create_detector(self, detectorId, **kw):
        if detectorId in self._detectors: raise ConflictException(f"Detector {detectorId} exists")
        r = DetectorRecord(detectorId=detectorId, **kw)
        self._detectors[detectorId] = r
        return r

    def delete_detector(self, detectorId):
        if detectorId not in self._detectors: raise ResourceNotFoundException(f"Detector {detectorId} not found")
        del self._detectors[detectorId]

    def variables(self, name=None):
        if name: return self._variables.get(name)
        return list(self._variables.values())

    def create_variable(self, name, **kw):
        if name in self._variables: raise ConflictException(f"Variable {name} exists")
        r = VariableRecord(name=name, **kw)
        self._variables[name] = r
        return r

    def update_variable(self, name, **kw):
        if name not in self._variables: raise ResourceNotFoundException(f"Variable {name} not found")
        rec = self._variables[name]
        for k, v in kw.items():
            if hasattr(rec, k): setattr(rec, k, v)
        return rec

    def delete_variable(self, name):
        if name not in self._variables: raise ResourceNotFoundException(f"Variable {name} not found")
        del self._variables[name]

    def models(self, modelId=None, modelType=None):
        if modelId:
            key = f"{modelId}/{modelType or ''}"
            return self._models.get(key)
        return list(self._models.values())

    def create_model(self, modelId, modelType, **kw):
        key = f"{modelId}/{modelType}"
        if key in self._models: raise ConflictException(f"Model {key} exists")
        r = ModelRecord(modelId=modelId, modelType=modelType, **kw)
        self._models[key] = r
        return r

    def update_model(self, modelId, modelType, **kw):
        key = f"{modelId}/{modelType}"
        if key not in self._models: raise ResourceNotFoundException(f"Model {key} not found")
        rec = self._models[key]
        for k, v in kw.items():
            if hasattr(rec, k): setattr(rec, k, v)
        return rec

    def delete_model(self, modelId, modelType):
        key = f"{modelId}/{modelType}"
        if key not in self._models: raise ResourceNotFoundException(f"Model {key} not found")
        del self._models[key]

    def eventtypes(self, name=None):
        if name: return self._eventtypes.get(name)
        return list(self._eventtypes.values())

    def create_eventtype(self, name, **kw):
        if name in self._eventtypes: raise ConflictException(f"EventType {name} exists")
        r = EventTypeRecord(name=name, **kw)
        self._eventtypes[name] = r
        return r

    def delete_eventtype(self, name):
        if name not in self._eventtypes: raise ResourceNotFoundException(f"EventType {name} not found")
        del self._eventtypes[name]

    def rules(self, detectorId, ruleId=None):
        if ruleId:
            key = f"{detectorId}/{ruleId}"
            return self._rules.get(key)
        return [r for r in self._rules.values() if r.detectorId == detectorId]

    def create_rule(self, ruleId, detectorId, **kw):
        key = f"{detectorId}/{ruleId}"
        if key in self._rules: raise ConflictException(f"Rule {key} exists")
        r = RuleRecord(ruleId=ruleId, detectorId=detectorId, **kw)
        self._rules[key] = r
        return r

    def delete_rule(self, ruleId, detectorId):
        key = f"{detectorId}/{ruleId}"
        if key not in self._rules: raise ResourceNotFoundException(f"Rule {key} not found")
        del self._rules[key]

    def tag_resource(self, resourceARN, tags):
        rec = self._find_by_arn(resourceARN)
        if not rec: raise ResourceNotFoundException(f"Resource {resourceARN} not found")
        d = rec.tags or {}
        for t in (tags or []):
            k = t.get("key", "") or t.get("Key", "")
            v = t.get("value", "") or t.get("Value", "")
            d[k] = v
        rec.tags = d

    def untag_resource(self, resourceARN, tagKeys):
        rec = self._find_by_arn(resourceARN)
        if not rec: raise ResourceNotFoundException(f"Resource {resourceARN} not found")
        d = rec.tags or {}
        for k in (tagKeys or []): d.pop(k, None)
        rec.tags = d

    def list_tags_for_resource(self, resourceARN):
        rec = self._find_by_arn(resourceARN)
        if not rec: raise ResourceNotFoundException(f"Resource {resourceARN} not found")
        return rec.tags or {}

    def _find_by_arn(self, arn):
        if not arn: return None
        for recs in [self._detectors, self._variables, self._models, self._eventtypes, self._rules]:
            for rec in recs.values():
                if getattr(rec, 'arn', '') == arn:
                    return rec
        return None
