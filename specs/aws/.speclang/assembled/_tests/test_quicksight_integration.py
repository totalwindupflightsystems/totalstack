"""Integration test for QuickSight — real store + generated handlers.

Tests 4 core entities (DataSet, DataSource, Dashboard, Analysis) + tagging.
"""
import os
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'quicksight')

# Load models
models_spec = importlib.util.spec_from_file_location('models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

QuickSightStore = models_mod.QuickSightStore
DataSetRecord = models_mod.DataSetRecord
DataSourceRecord = models_mod.DataSourceRecord
DashboardRecord = models_mod.DashboardRecord
AnalysisRecord = models_mod.AnalysisRecord
AccessDeniedException = models_mod.AccessDeniedException
InvalidParameterValueException = models_mod.InvalidParameterValueException
ResourceNotFoundException = models_mod.ResourceNotFoundException
ResourceExistsException = models_mod.ResourceExistsException
ConflictException = models_mod.ConflictException
InternalFailureException = models_mod.InternalFailureException

ACCOUNT = "123456789012"


def _load_handler(op_name):
    """Load a generated .code.py handler — inject dependencies first."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception classes
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ResourceExistsException = ResourceExistsException
    mod.InvalidParameterValueException = InvalidParameterValueException
    mod.AccessDeniedException = AccessDeniedException
    mod.ConflictException = ConflictException
    mod.InternalFailureException = InternalFailureException
    # Inject record classes
    mod.DataSetRecord = DataSetRecord
    mod.DataSourceRecord = DataSourceRecord
    mod.DashboardRecord = DashboardRecord
    mod.AnalysisRecord = AnalysisRecord
    spec.loader.exec_module(mod)
    # Find handler function
    skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


# ═══════════════════════════════════════════════════════════════════════════════
# DataSet
# ═══════════════════════════════════════════════════════════════════════════════

class TestDataSet:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = QuickSightStore()
        return self._store

    def test_create_dataset_happy(self):
        h = _load_handler('create-data-set')
        resp = h(self.store, {
            "AwsAccountId": ACCOUNT, "DataSetId": "ds-001", "Name": "My Dataset",
            "PhysicalTableMap": {}, "ImportMode": "SPICE",
        })
        assert resp["DataSetId"] == "ds-001"
        assert resp["Arn"] != ""
        assert resp["Status"] == 200

    def test_create_dataset_duplicate(self):
        h = _load_handler('create-data-set')
        req = {"AwsAccountId": ACCOUNT, "DataSetId": "ds-002", "Name": "DS2",
               "PhysicalTableMap": {}, "ImportMode": "SPICE"}
        h(self.store, req)
        try:
            h(self.store, req)
            raise AssertionError("Should have raised")
        except ResourceExistsException:
            pass

    def test_describe_dataset_happy(self):
        create = _load_handler('create-data-set')
        describe = _load_handler('describe-data-set')
        create(self.store, {"AwsAccountId": ACCOUNT, "DataSetId": "ds-003", "Name": "DS3",
                            "PhysicalTableMap": {}, "ImportMode": "SPICE"})
        resp = describe(self.store, {"AwsAccountId": ACCOUNT, "DataSetId": "ds-003"})
        assert resp["DataSet"]["DataSetId"] == "ds-003"

    def test_describe_dataset_missing(self):
        describe = _load_handler('describe-data-set')
        try:
            describe(self.store, {"AwsAccountId": ACCOUNT, "DataSetId": "nonexistent"})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    def test_update_dataset_happy(self):
        create = _load_handler('create-data-set')
        update = _load_handler('update-data-set')
        create(self.store, {"AwsAccountId": ACCOUNT, "DataSetId": "ds-004", "Name": "OldName",
                            "PhysicalTableMap": {}, "ImportMode": "SPICE"})
        resp = update(self.store, {"AwsAccountId": ACCOUNT, "DataSetId": "ds-004",
                                   "Name": "NewName", "PhysicalTableMap": {}, "ImportMode": "SPICE"})
        assert resp["DataSetId"] == "ds-004"
        assert resp["Status"] == 200

    def test_delete_dataset_happy(self):
        create = _load_handler('create-data-set')
        delete = _load_handler('delete-data-set')
        describe = _load_handler('describe-data-set')
        create(self.store, {"AwsAccountId": ACCOUNT, "DataSetId": "ds-005", "Name": "DS5",
                            "PhysicalTableMap": {}, "ImportMode": "SPICE"})
        delete(self.store, {"AwsAccountId": ACCOUNT, "DataSetId": "ds-005"})
        try:
            describe(self.store, {"AwsAccountId": ACCOUNT, "DataSetId": "ds-005"})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    def test_list_datasets_happy(self):
        create = _load_handler('create-data-set')
        list_h = _load_handler('list-data-sets')
        for i in range(3):
            create(self.store, {"AwsAccountId": ACCOUNT, "DataSetId": f"ds-list-{i}",
                                "Name": f"DS{i}", "PhysicalTableMap": {}, "ImportMode": "SPICE"})
        resp = list_h(self.store, {"AwsAccountId": ACCOUNT})
        assert len(resp["DataSetSummaries"]) >= 3


# ═══════════════════════════════════════════════════════════════════════════════
# DataSource
# ═══════════════════════════════════════════════════════════════════════════════

class TestDataSource:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = QuickSightStore()
        return self._store

    def test_create_datasource_happy(self):
        h = _load_handler('create-data-source')
        resp = h(self.store, {
            "AwsAccountId": ACCOUNT, "DataSourceId": "dsc-001", "Name": "MySource",
            "Type": "ATHENA",
        })
        assert resp["DataSourceId"] == "dsc-001"
        assert resp["Arn"] != ""

    def test_create_datasource_duplicate(self):
        h = _load_handler('create-data-source')
        req = {"AwsAccountId": ACCOUNT, "DataSourceId": "dsc-002", "Name": "DS2", "Type": "ATHENA"}
        h(self.store, req)
        try:
            h(self.store, req)
            raise AssertionError()
        except ResourceExistsException:
            pass

    def test_describe_datasource_happy(self):
        create = _load_handler('create-data-source')
        describe = _load_handler('describe-data-source')
        create(self.store, {"AwsAccountId": ACCOUNT, "DataSourceId": "dsc-003",
                            "Name": "DS3", "Type": "ATHENA"})
        resp = describe(self.store, {"AwsAccountId": ACCOUNT, "DataSourceId": "dsc-003"})
        assert resp["DataSource"]["DataSourceId"] == "dsc-003"

    def test_describe_datasource_missing(self):
        describe = _load_handler('describe-data-source')
        try:
            describe(self.store, {"AwsAccountId": ACCOUNT, "DataSourceId": "nonexistent"})
            raise AssertionError()
        except ResourceNotFoundException:
            pass

    def test_update_datasource_happy(self):
        create = _load_handler('create-data-source')
        update = _load_handler('update-data-source')
        create(self.store, {"AwsAccountId": ACCOUNT, "DataSourceId": "dsc-004",
                            "Name": "OldDSC", "Type": "ATHENA"})
        resp = update(self.store, {"AwsAccountId": ACCOUNT, "DataSourceId": "dsc-004",
                                   "Name": "NewDSC"})
        assert resp["DataSourceId"] == "dsc-004"

    def test_delete_datasource_happy(self):
        create = _load_handler('create-data-source')
        delete = _load_handler('delete-data-source')
        describe = _load_handler('describe-data-source')
        create(self.store, {"AwsAccountId": ACCOUNT, "DataSourceId": "dsc-005",
                            "Name": "DS5", "Type": "ATHENA"})
        delete(self.store, {"AwsAccountId": ACCOUNT, "DataSourceId": "dsc-005"})
        try:
            describe(self.store, {"AwsAccountId": ACCOUNT, "DataSourceId": "dsc-005"})
            raise AssertionError()
        except ResourceNotFoundException:
            pass

    def test_list_datasources_happy(self):
        create = _load_handler('create-data-source')
        list_h = _load_handler('list-data-sources')
        for i in range(3):
            create(self.store, {"AwsAccountId": ACCOUNT, "DataSourceId": f"dsc-list-{i}",
                                "Name": f"DS{i}", "Type": "ATHENA"})
        resp = list_h(self.store, {"AwsAccountId": ACCOUNT})
        assert len(resp["DataSources"]) >= 3


# ═══════════════════════════════════════════════════════════════════════════════
# Dashboard
# ═══════════════════════════════════════════════════════════════════════════════

class TestDashboard:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = QuickSightStore()
        return self._store

    def test_create_dashboard_happy(self):
        h = _load_handler('create-dashboard')
        resp = h(self.store, {
            "AwsAccountId": ACCOUNT, "DashboardId": "db-001", "Name": "MyDashboard",
        })
        assert resp["DashboardId"] == "db-001"
        assert resp["Arn"] != ""

    def test_create_dashboard_duplicate(self):
        h = _load_handler('create-dashboard')
        req = {"AwsAccountId": ACCOUNT, "DashboardId": "db-002", "Name": "DB2"}
        h(self.store, req)
        try:
            h(self.store, req)
            raise AssertionError()
        except ResourceExistsException:
            pass

    def test_describe_dashboard_happy(self):
        create = _load_handler('create-dashboard')
        describe = _load_handler('describe-dashboard')
        create(self.store, {"AwsAccountId": ACCOUNT, "DashboardId": "db-003",
                            "Name": "DB3"})
        resp = describe(self.store, {"AwsAccountId": ACCOUNT, "DashboardId": "db-003"})
        assert resp["Dashboard"]["DashboardId"] == "db-003"

    def test_describe_dashboard_missing(self):
        describe = _load_handler('describe-dashboard')
        try:
            describe(self.store, {"AwsAccountId": ACCOUNT, "DashboardId": "nonexistent"})
            raise AssertionError()
        except ResourceNotFoundException:
            pass

    def test_update_dashboard_happy(self):
        create = _load_handler('create-dashboard')
        update = _load_handler('update-dashboard')
        create(self.store, {"AwsAccountId": ACCOUNT, "DashboardId": "db-004",
                            "Name": "OldDB"})
        resp = update(self.store, {"AwsAccountId": ACCOUNT, "DashboardId": "db-004",
                                   "Name": "NewDB"})
        assert resp["DashboardId"] == "db-004"

    def test_delete_dashboard_happy(self):
        create = _load_handler('create-dashboard')
        delete = _load_handler('delete-dashboard')
        describe = _load_handler('describe-dashboard')
        create(self.store, {"AwsAccountId": ACCOUNT, "DashboardId": "db-005",
                            "Name": "DB5"})
        delete(self.store, {"AwsAccountId": ACCOUNT, "DashboardId": "db-005"})
        try:
            describe(self.store, {"AwsAccountId": ACCOUNT, "DashboardId": "db-005"})
            raise AssertionError()
        except ResourceNotFoundException:
            pass

    def test_list_dashboards_happy(self):
        create = _load_handler('create-dashboard')
        list_h = _load_handler('list-dashboards')
        for i in range(3):
            create(self.store, {"AwsAccountId": ACCOUNT, "DashboardId": f"db-list-{i}",
                                "Name": f"DB{i}"})
        resp = list_h(self.store, {"AwsAccountId": ACCOUNT})
        assert len(resp["DashboardSummaryList"]) >= 3


# ═══════════════════════════════════════════════════════════════════════════════
# Analysis
# ═══════════════════════════════════════════════════════════════════════════════

class TestAnalysis:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = QuickSightStore()
        return self._store

    def test_create_analysis_happy(self):
        h = _load_handler('create-analysis')
        resp = h(self.store, {
            "AwsAccountId": ACCOUNT, "AnalysisId": "an-001", "Name": "MyAnalysis",
        })
        assert resp["AnalysisId"] == "an-001"
        assert resp["Arn"] != ""

    def test_create_analysis_duplicate(self):
        h = _load_handler('create-analysis')
        req = {"AwsAccountId": ACCOUNT, "AnalysisId": "an-002", "Name": "AN2"}
        h(self.store, req)
        try:
            h(self.store, req)
            raise AssertionError()
        except ResourceExistsException:
            pass

    def test_describe_analysis_happy(self):
        create = _load_handler('create-analysis')
        describe = _load_handler('describe-analysis')
        create(self.store, {"AwsAccountId": ACCOUNT, "AnalysisId": "an-003",
                            "Name": "AN3"})
        resp = describe(self.store, {"AwsAccountId": ACCOUNT, "AnalysisId": "an-003"})
        assert resp["Analysis"]["AnalysisId"] == "an-003"

    def test_describe_analysis_missing(self):
        describe = _load_handler('describe-analysis')
        try:
            describe(self.store, {"AwsAccountId": ACCOUNT, "AnalysisId": "nonexistent"})
            raise AssertionError()
        except ResourceNotFoundException:
            pass

    def test_update_analysis_happy(self):
        create = _load_handler('create-analysis')
        update = _load_handler('update-analysis')
        create(self.store, {"AwsAccountId": ACCOUNT, "AnalysisId": "an-004",
                            "Name": "OldAN"})
        resp = update(self.store, {"AwsAccountId": ACCOUNT, "AnalysisId": "an-004",
                                   "Name": "NewAN"})
        assert resp["AnalysisId"] == "an-004"

    def test_delete_analysis_happy(self):
        create = _load_handler('create-analysis')
        delete = _load_handler('delete-analysis')
        describe = _load_handler('describe-analysis')
        create(self.store, {"AwsAccountId": ACCOUNT, "AnalysisId": "an-005",
                            "Name": "AN5"})
        delete(self.store, {"AwsAccountId": ACCOUNT, "AnalysisId": "an-005"})
        try:
            describe(self.store, {"AwsAccountId": ACCOUNT, "AnalysisId": "an-005"})
            raise AssertionError()
        except ResourceNotFoundException:
            pass

    def test_list_analyses_happy(self):
        create = _load_handler('create-analysis')
        list_h = _load_handler('list-analyses')
        for i in range(3):
            create(self.store, {"AwsAccountId": ACCOUNT, "AnalysisId": f"an-list-{i}",
                                "Name": f"AN{i}"})
        resp = list_h(self.store, {"AwsAccountId": ACCOUNT})
        assert len(resp["AnalysisSummaryList"]) >= 3


# ═══════════════════════════════════════════════════════════════════════════════
# Tags (cross-entity via ARN)
# ═══════════════════════════════════════════════════════════════════════════════

class TestTags:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = QuickSightStore()
        return self._store

    def _create_dataset_with_arn(self):
        create = _load_handler('create-data-set')
        resp = create(self.store, {"AwsAccountId": ACCOUNT, "DataSetId": "ds-tags",
                                   "Name": "TagsDS", "PhysicalTableMap": {},
                                   "ImportMode": "SPICE"})
        return resp["Arn"]

    def test_tag_resource_happy(self):
        arn = self._create_dataset_with_arn()
        tag = _load_handler('tag-resource')
        resp = tag(self.store, {"ResourceArn": arn, "Tags": [
            {"Key": "env", "Value": "test"},
            {"Key": "project", "Value": "qs"},
        ]})
        assert resp["Status"] == 200

    def test_list_tags_for_resource_happy(self):
        arn = self._create_dataset_with_arn()
        tag = _load_handler('tag-resource')
        list_tags = _load_handler('list-tags-for-resource')
        tag(self.store, {"ResourceArn": arn, "Tags": [{"Key": "env", "Value": "prod"}]})
        resp = list_tags(self.store, {"ResourceArn": arn})
        assert len(resp["Tags"]) == 1
        assert resp["Tags"][0]["Key"] == "env"

    def test_untag_resource_happy(self):
        arn = self._create_dataset_with_arn()
        tag = _load_handler('tag-resource')
        untag = _load_handler('untag-resource')
        list_tags = _load_handler('list-tags-for-resource')
        tag(self.store, {"ResourceArn": arn, "Tags": [{"Key": "env", "Value": "test"}]})
        untag(self.store, {"ResourceArn": arn, "TagKeys": ["env"]})
        resp = list_tags(self.store, {"ResourceArn": arn})
        assert len(resp["Tags"]) == 0

    def test_tag_resource_missing_arn(self):
        tag = _load_handler('tag-resource')
        try:
            tag(self.store, {"ResourceArn": "arn:aws:quicksight:us-east-1:1234:dataset/fake",
                             "Tags": []})
            raise AssertionError()
        except ResourceNotFoundException:
            pass

    def test_list_tags_missing_arn(self):
        list_tags = _load_handler('list-tags-for-resource')
        try:
            list_tags(self.store, {"ResourceArn": "arn:aws:quicksight:us-east-1:1234:dataset/fake"})
            raise AssertionError()
        except ResourceNotFoundException:
            pass
