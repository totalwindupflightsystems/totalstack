"""Integration test for Personalize — 3 entities + tags."""
import os
import importlib.util
import types
AD = os.path.dirname(__file__)
SD = os.path.join(AD, '..', 'personalize')
ms = importlib.util.spec_from_file_location('models', os.path.join(SD, 'models.code.py'))
mm = importlib.util.module_from_spec(ms)
ms.loader.exec_module(mm)
FS = mm.PersonalizeStore
RN = mm.ResourceNotFoundException
RE = mm.ResourceAlreadyExistsException
DA = "arn:aws:personalize:us-east-1:123456789012:dataset/"
SA = "arn:aws:personalize:us-east-1:123456789012:solution/"
CA = "arn:aws:personalize:us-east-1:123456789012:campaign/"

def _h(op):
    p = os.path.join(SD, op + '.code.py')
    s = importlib.util.spec_from_file_location(op, p)
    m = importlib.util.module_from_spec(s)
    m.ResourceNotFoundException = RN
    m.ResourceAlreadyExistsException = RE
    for cls in [mm.DatasetRecord, mm.SolutionRecord, mm.CampaignRecord]:
        setattr(m, cls.__name__, cls)
    s.loader.exec_module(m)
    sk = {'dataclass', 'time', 'uuid', '<lambda>'}
    for v in m.__dict__.values():
        if isinstance(v, types.FunctionType) and not v.__name__.startswith('_') and v.__name__ not in sk:
            return v

class TestDataset:
    _s = None
    @property
    def store(self):
        if self._s is None: self._s = FS()
        return self._s

    def test_create(self):
        r = _h('create-dataset')(self.store, {"name": "ds1", "schemaArn": "arn:s", "datasetGroupArn": "arn:g", "datasetType": "Interactions"})
        assert r["datasetArn"] == DA + "ds1"

    def test_duplicate(self):
        c = _h('create-dataset')
        c(self.store, {"name": "ds2", "schemaArn": "arn:s", "datasetGroupArn": "arn:g", "datasetType": "Interactions"})
        try: c(self.store, {"name": "ds2", "schemaArn": "arn:s", "datasetGroupArn": "arn:g", "datasetType": "Interactions"})
        except RE: pass
        else: raise AssertionError()

    def test_describe(self):
        _h('create-dataset')(self.store, {"name": "ds3", "schemaArn": "arn:s", "datasetGroupArn": "arn:g", "datasetType": "Interactions"})
        r = _h('describe-dataset')(self.store, {"datasetArn": DA + "ds3"})
        assert r["name"] == "ds3"

    def test_describe_missing(self):
        try: _h('describe-dataset')(self.store, {"datasetArn": DA + "x"})
        except RN: pass
        else: raise AssertionError()

    def test_list(self):
        c = _h('create-dataset')
        for i in range(2): c(self.store, {"name": f"dl{i}", "schemaArn": "arn:s", "datasetGroupArn": "arn:g", "datasetType": "Interactions"})
        r = _h('list-datasets')(self.store, {})
        assert len(r["datasets"]) >= 2

    def test_delete(self):
        c = _h('create-dataset'); d = _h('delete-dataset')
        c(self.store, {"name": "ds5", "schemaArn": "arn:s", "datasetGroupArn": "arn:g", "datasetType": "Interactions"})
        d(self.store, {"datasetArn": DA + "ds5"})
        try: _h('describe-dataset')(self.store, {"datasetArn": DA + "ds5"})
        except RN: pass
        else: raise AssertionError()

class TestSolution:
    _s = None
    @property
    def store(self):
        if self._s is None: self._s = FS()
        return self._s

    def test_crud(self):
        c = _h('create-solution'); d = _h('delete-solution'); lst = _h('list-solutions')
        c(self.store, {"name": "s1", "datasetGroupArn": "arn:g"})
        assert len(lst(self.store, {})["solutions"]) >= 1
        d(self.store, {"solutionArn": SA + "s1"})

    def test_describe_missing(self):
        try: _h('describe-solution')(self.store, {"solutionArn": SA + "x"})
        except RN: pass
        else: raise AssertionError()

class TestCampaign:
    _s = None
    @property
    def store(self):
        if self._s is None: self._s = FS()
        return self._s

    def test_crud(self):
        c = _h('create-campaign'); u = _h('update-campaign'); d = _h('delete-campaign'); lst = _h('list-campaigns')
        c(self.store, {"name": "c1", "solutionVersionArn": "arn:sv"})
        assert len(lst(self.store, {})["campaigns"]) >= 1
        u(self.store, {"campaignArn": CA + "c1"})
        d(self.store, {"campaignArn": CA + "c1"})

class TestTags:
    _s = None
    @property
    def store(self):
        if self._s is None: self._s = FS()
        return self._s

    def test_tag_roundtrip(self):
        _h('create-dataset')(self.store, {"name": "dt", "schemaArn": "arn:s", "datasetGroupArn": "arn:g", "datasetType": "Interactions", "tags": [{"tagKey": "k", "tagValue": "v"}]})
        t = _h('tag-resource'); lst = _h('list-tags-for-resource'); u = _h('untag-resource')
        t(self.store, {"resourceArn": DA + "dt", "tags": [{"tagKey": "e", "tagValue": "t"}]})
        r = lst(self.store, {"resourceArn": DA + "dt"})
        assert len(r["tags"]) >= 1
        u(self.store, {"resourceArn": DA + "dt", "tagKeys": ["k", "e"]})
        r = lst(self.store, {"resourceArn": DA + "dt"})
        assert len(r["tags"]) == 0
