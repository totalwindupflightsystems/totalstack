"""Integration test for FraudDetector — 5 entities + tags."""
import os
import importlib.util
import types

AD = os.path.dirname(__file__)
SD = os.path.join(AD, '..', 'frauddetector')

ms = importlib.util.spec_from_file_location('models', os.path.join(SD, 'models.code.py'))
mm = importlib.util.module_from_spec(ms)
ms.loader.exec_module(mm)
FS = mm.FraudDetectorStore
VE = mm.ValidationException
RN = mm.ResourceNotFoundException
CE = mm.ConflictException

def _h(op):
    p = os.path.join(SD, op + '.code.py')
    s = importlib.util.spec_from_file_location(op, p)
    m = importlib.util.module_from_spec(s)
    m.ValidationException = VE
    m.ResourceNotFoundException = RN
    m.ConflictException = CE
    for cls in [mm.DetectorRecord, mm.VariableRecord, mm.ModelRecord, mm.EventTypeRecord, mm.RuleRecord]:
        setattr(m, cls.__name__, cls)
    s.loader.exec_module(m)
    sk = {'dataclass', 'time', 'uuid', '<lambda>'}
    for v in m.__dict__.values():
        if isinstance(v, types.FunctionType) and not v.__name__.startswith('_') and v.__name__ not in sk:
            return v
    raise RuntimeError(f"No handler found in {op}")


class TestDetector:
    _s = None
    @property
    def store(self):
        if self._s is None: self._s = FS()
        return self._s

    def test_put(self):
        _h('put-detector')(self.store, {"detectorId": "d1", "eventTypeName": "fraud"})
        assert self.store.detectors("d1") is not None

    def test_duplicate(self):
        _h('put-detector')(self.store, {"detectorId": "d2", "eventTypeName": "f"})
        try:
            _h('put-detector')(self.store, {"detectorId": "d2", "eventTypeName": "f"})
            raise AssertionError()
        except CE: pass

    def test_describe(self):
        _h('put-detector')(self.store, {"detectorId": "d3", "eventTypeName": "f"})
        r = _h('describe-detector')(self.store, {"detectorId": "d3"})
        assert r["detectorId"] == "d3"

    def test_describe_missing(self):
        try: _h('describe-detector')(self.store, {"detectorId": "x"})
        except RN: pass
        else: raise AssertionError()

    def test_list(self):
        for i in range(2):
            _h('put-detector')(self.store, {"detectorId": f"dl{i}", "eventTypeName": "f"})
        r = _h('get-detectors')(self.store, {})
        assert len(r["detectors"]) >= 2

    def test_delete(self):
        _h('put-detector')(self.store, {"detectorId": "d5", "eventTypeName": "f"})
        _h('delete-detector')(self.store, {"detectorId": "d5"})
        try: _h('describe-detector')(self.store, {"detectorId": "d5"})
        except RN: pass
        else: raise AssertionError()


class TestVariable:
    _s = None
    @property
    def store(self):
        if self._s is None: self._s = FS()
        return self._s

    def test_crud(self):
        c = _h('create-variable'); d = _h('delete-variable'); g = _h('get-variables'); u = _h('update-variable')
        c(self.store, {"name": "v1", "dataType": "STRING", "dataSource": "EVENT", "defaultValue": "x"})
        assert self.store.variables("v1") is not None
        u(self.store, {"name": "v1", "defaultValue": "y"})
        assert len(g(self.store, {})["variables"]) >= 1
        d(self.store, {"name": "v1"})
        assert self.store.variables("v1") is None

    def test_duplicate(self):
        c = _h('create-variable')
        c(self.store, {"name": "v2", "dataType": "STRING", "dataSource": "EVENT", "defaultValue": "x"})
        try: c(self.store, {"name": "v2", "dataType": "STRING", "dataSource": "EVENT", "defaultValue": "x"})
        except CE: pass
        else: raise AssertionError()


class TestModel:
    _s = None
    @property
    def store(self):
        if self._s is None: self._s = FS()
        return self._s

    def test_crud(self):
        c = _h('create-model'); d = _h('delete-model'); g = _h('get-models')
        c(self.store, {"modelId": "m1", "modelType": "ONLINE_FRAUD_INSIGHTS", "eventTypeName": "f"})
        assert len(g(self.store, {})["models"]) >= 1
        d(self.store, {"modelId": "m1", "modelType": "ONLINE_FRAUD_INSIGHTS"})

    def test_duplicate(self):
        c = _h('create-model')
        c(self.store, {"modelId": "m2", "modelType": "ONLINE_FRAUD_INSIGHTS", "eventTypeName": "f"})
        try: c(self.store, {"modelId": "m2", "modelType": "ONLINE_FRAUD_INSIGHTS", "eventTypeName": "f"})
        except CE: pass
        else: raise AssertionError()


class TestEventType:
    _s = None
    @property
    def store(self):
        if self._s is None: self._s = FS()
        return self._s

    def test_crud(self):
        c = _h('put-event-type'); d = _h('delete-event-type'); g = _h('get-event-types')
        c(self.store, {"name": "et1", "eventVariables": ["amount"], "entityTypes": ["user"]})
        assert len(g(self.store, {})["eventTypes"]) >= 1
        d(self.store, {"name": "et1"})

    def test_duplicate(self):
        c = _h('put-event-type')
        c(self.store, {"name": "et2", "eventVariables": [], "entityTypes": []})
        try: c(self.store, {"name": "et2", "eventVariables": [], "entityTypes": []})
        except CE: pass
        else: raise AssertionError()


class TestRule:
    _s = None
    @property
    def store(self):
        if self._s is None: self._s = FS()
        return self._s

    def test_crud(self):
        c = _h('create-rule'); r = _h('get-rules'); d = _h('delete-rule')
        c(self.store, {"ruleId": "r1", "detectorId": "d1", "expression": "1==1",
                       "language": "DETECTORPL", "outcomes": ["approved"]})
        rules = r(self.store, {"detectorId": "d1"})
        assert len(rules["rules"]) >= 1
        d(self.store, {"rule": "d1/r1"})

    def test_duplicate(self):
        c = _h('create-rule')
        c(self.store, {"ruleId": "r2", "detectorId": "d2", "expression": "1==1",
                       "language": "DETECTORPL", "outcomes": ["approved"]})
        try: c(self.store, {"ruleId": "r2", "detectorId": "d2", "expression": "1==1",
                            "language": "DETECTORPL", "outcomes": ["approved"]})
        except CE: pass
        else: raise AssertionError()


class TestTags:
    _s = None
    @property
    def store(self):
        if self._s is None: self._s = FS()
        return self._s

    def _make_detector(self):
        _h('put-detector')(self.store, {"detectorId": "dt", "eventTypeName": "f",
                                         "tags": [{"key": "k", "value": "v"}]})

    def test_tag(self):
        self._make_detector()
        tag = _h('tag-resource'); lst = _h('list-tags-for-resource'); ut = _h('untag-resource')
        arn = "arn:aws:frauddetector:us-east-1:123456789012:detector/dt"
        tag(self.store, {"resourceARN": arn, "tags": [{"key": "e", "value": "t"}]})
        r = lst(self.store, {"resourceARN": arn})
        assert len(r["tags"]) >= 1
        ut(self.store, {"resourceARN": arn, "tagKeys": ["k", "e"]})
        r = lst(self.store, {"resourceARN": arn})
        assert len(r["tags"]) == 0
