"""Integration test for Forecast — real store + generated handlers.

Tests 3 entities: Dataset, Forecast, Predictor + tagging. ARN-based access.
"""
import os
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'forecast')

# Load models
models_spec = importlib.util.spec_from_file_location('models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

ForecastStore = models_mod.ForecastStore
DatasetRecord = models_mod.DatasetRecord
ForecastRecord = models_mod.ForecastRecord
PredictorRecord = models_mod.PredictorRecord
InvalidInputException = models_mod.InvalidInputException
ResourceNotFoundException = models_mod.ResourceNotFoundException
ResourceAlreadyExistsException = models_mod.ResourceAlreadyExistsException
ResourceInUseException = models_mod.ResourceInUseException
LimitExceededException = models_mod.LimitExceededException


def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ResourceAlreadyExistsException = ResourceAlreadyExistsException
    mod.InvalidInputException = InvalidInputException
    mod.ResourceInUseException = ResourceInUseException
    mod.LimitExceededException = LimitExceededException
    mod.DatasetRecord = DatasetRecord
    mod.ForecastRecord = ForecastRecord
    mod.PredictorRecord = PredictorRecord
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


DS_ARN = "arn:aws:forecast:us-east-1:123456789012:dataset/"
FC_ARN = "arn:aws:forecast:us-east-1:123456789012:forecast/"
PR_ARN = "arn:aws:forecast:us-east-1:123456789012:predictor/"


# ═══════════════════════════════════════════════════════════════════════════════
# Dataset
# ═══════════════════════════════════════════════════════════════════════════════

class TestDataset:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = ForecastStore()
        return self._store

    def test_create_dataset_happy(self):
        h = _load_handler('create-dataset')
        resp = h(self.store, {"DatasetName": "ds1", "Domain": "CUSTOM",
                              "DatasetType": "TARGET_TIME_SERIES", "Schema": {}})
        assert resp["DatasetArn"] == DS_ARN + "ds1"

    def test_create_dataset_duplicate(self):
        h = _load_handler('create-dataset')
        req = {"DatasetName": "ds2", "Domain": "CUSTOM", "DatasetType": "TARGET_TIME_SERIES", "Schema": {}}
        h(self.store, req)
        try:
            h(self.store, req)
            raise AssertionError("Should have raised")
        except ResourceAlreadyExistsException:
            pass

    def test_describe_dataset_happy(self):
        create = _load_handler('create-dataset')
        describe = _load_handler('describe-dataset')
        create(self.store, {"DatasetName": "ds3", "Domain": "CUSTOM", "DatasetType": "TARGET_TIME_SERIES", "Schema": {}})
        resp = describe(self.store, {"DatasetArn": DS_ARN + "ds3"})
        assert resp["DatasetName"] == "ds3"

    def test_describe_dataset_missing(self):
        describe = _load_handler('describe-dataset')
        try:
            describe(self.store, {"DatasetArn": DS_ARN + "nonexistent"})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    def test_delete_dataset_happy(self):
        create = _load_handler('create-dataset')
        delete = _load_handler('delete-dataset')
        describe = _load_handler('describe-dataset')
        create(self.store, {"DatasetName": "ds5", "Domain": "CUSTOM", "DatasetType": "TARGET_TIME_SERIES", "Schema": {}})
        delete(self.store, {"DatasetArn": DS_ARN + "ds5"})
        try:
            describe(self.store, {"DatasetArn": DS_ARN + "ds5"})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    def test_list_datasets_happy(self):
        create = _load_handler('create-dataset')
        list_h = _load_handler('list-datasets')
        for i in range(3):
            create(self.store, {"DatasetName": f"ds-list-{i}", "Domain": "CUSTOM",
                                "DatasetType": "TARGET_TIME_SERIES", "Schema": {}})
        resp = list_h(self.store, {})
        assert len(resp["Datasets"]) >= 3


# ═══════════════════════════════════════════════════════════════════════════════
# Forecast
# ═══════════════════════════════════════════════════════════════════════════════

class TestForecast:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = ForecastStore()
        return self._store

    def test_create_forecast_happy(self):
        h = _load_handler('create-forecast')
        resp = h(self.store, {"ForecastName": "fc1", "PredictorArn": PR_ARN + "p1"})
        assert resp["ForecastArn"] == FC_ARN + "fc1"

    def test_create_forecast_duplicate(self):
        h = _load_handler('create-forecast')
        req = {"ForecastName": "fc2", "PredictorArn": PR_ARN + "p1"}
        h(self.store, req)
        try:
            h(self.store, req)
            raise AssertionError("Should have raised")
        except ResourceAlreadyExistsException:
            pass

    def test_describe_forecast_happy(self):
        create = _load_handler('create-forecast')
        describe = _load_handler('describe-forecast')
        create(self.store, {"ForecastName": "fc3", "PredictorArn": PR_ARN + "p1"})
        resp = describe(self.store, {"ForecastArn": FC_ARN + "fc3"})
        assert resp["ForecastName"] == "fc3"

    def test_describe_forecast_missing(self):
        describe = _load_handler('describe-forecast')
        try:
            describe(self.store, {"ForecastArn": FC_ARN + "nonexistent"})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    def test_delete_forecast_happy(self):
        create = _load_handler('create-forecast')
        delete = _load_handler('delete-forecast')
        describe = _load_handler('describe-forecast')
        create(self.store, {"ForecastName": "fc5", "PredictorArn": PR_ARN + "p1"})
        delete(self.store, {"ForecastArn": FC_ARN + "fc5"})
        try:
            describe(self.store, {"ForecastArn": FC_ARN + "fc5"})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    def test_list_forecasts_happy(self):
        create = _load_handler('create-forecast')
        list_h = _load_handler('list-forecasts')
        for i in range(2):
            create(self.store, {"ForecastName": f"fc-list-{i}", "PredictorArn": PR_ARN + "p1"})
        resp = list_h(self.store, {})
        assert len(resp["Forecasts"]) >= 2


# ═══════════════════════════════════════════════════════════════════════════════
# Predictor
# ═══════════════════════════════════════════════════════════════════════════════

class TestPredictor:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = ForecastStore()
        return self._store

    def test_create_predictor_happy(self):
        h = _load_handler('create-predictor')
        resp = h(self.store, {"PredictorName": "p1", "ForecastHorizon": 10,
                              "InputDataConfig": {}, "FeaturizationConfig": {}})
        assert resp["PredictorArn"] == PR_ARN + "p1"

    def test_create_predictor_duplicate(self):
        h = _load_handler('create-predictor')
        req = {"PredictorName": "p2", "ForecastHorizon": 10,
               "InputDataConfig": {}, "FeaturizationConfig": {}}
        h(self.store, req)
        try:
            h(self.store, req)
            raise AssertionError("Should have raised")
        except ResourceAlreadyExistsException:
            pass

    def test_describe_predictor_happy(self):
        create = _load_handler('create-predictor')
        describe = _load_handler('describe-predictor')
        create(self.store, {"PredictorName": "p3", "ForecastHorizon": 10,
                            "InputDataConfig": {}, "FeaturizationConfig": {}})
        resp = describe(self.store, {"PredictorArn": PR_ARN + "p3"})
        assert resp["PredictorName"] == "p3"

    def test_describe_predictor_missing(self):
        describe = _load_handler('describe-predictor')
        try:
            describe(self.store, {"PredictorArn": PR_ARN + "nonexistent"})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    def test_delete_predictor_happy(self):
        create = _load_handler('create-predictor')
        delete = _load_handler('delete-predictor')
        describe = _load_handler('describe-predictor')
        create(self.store, {"PredictorName": "p5", "ForecastHorizon": 10,
                            "InputDataConfig": {}, "FeaturizationConfig": {}})
        delete(self.store, {"PredictorArn": PR_ARN + "p5"})
        try:
            describe(self.store, {"PredictorArn": PR_ARN + "p5"})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass

    def test_list_predictors_happy(self):
        create = _load_handler('create-predictor')
        list_h = _load_handler('list-predictors')
        for i in range(2):
            create(self.store, {"PredictorName": f"p-list-{i}", "ForecastHorizon": 10,
                                "InputDataConfig": {}, "FeaturizationConfig": {}})
        resp = list_h(self.store, {})
        assert len(resp["Predictors"]) >= 2


# ═══════════════════════════════════════════════════════════════════════════════
# Tags
# ═══════════════════════════════════════════════════════════════════════════════

class TestTags:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = ForecastStore()
        return self._store

    def _create_dataset_arn(self):
        create = _load_handler('create-dataset')
        resp = create(self.store, {"DatasetName": "ds-tags", "Domain": "CUSTOM",
                                   "DatasetType": "TARGET_TIME_SERIES", "Schema": {}})
        return resp["DatasetArn"]

    def test_tag_resource_happy(self):
        arn = self._create_dataset_arn()
        tag = _load_handler('tag-resource')
        tag(self.store, {"ResourceArn": arn, "Tags": [{"Key": "env", "Value": "test"}]})

    def test_list_tags_for_resource(self):
        arn = self._create_dataset_arn()
        tag = _load_handler('tag-resource')
        list_tags = _load_handler('list-tags-for-resource')
        tag(self.store, {"ResourceArn": arn, "Tags": [{"Key": "env", "Value": "prod"}]})
        resp = list_tags(self.store, {"ResourceArn": arn})
        assert len(resp["Tags"]) == 1

    def test_untag_resource_happy(self):
        arn = self._create_dataset_arn()
        tag = _load_handler('tag-resource')
        untag = _load_handler('untag-resource')
        list_tags = _load_handler('list-tags-for-resource')
        tag(self.store, {"ResourceArn": arn, "Tags": [{"Key": "env", "Value": "test"}]})
        untag(self.store, {"ResourceArn": arn, "TagKeys": ["env"]})
        resp = list_tags(self.store, {"ResourceArn": arn})
        assert len(resp["Tags"]) == 0

    def test_tag_missing_arn(self):
        tag = _load_handler('tag-resource')
        try:
            tag(self.store, {"ResourceArn": DS_ARN + "fake", "Tags": []})
            raise AssertionError("Should have raised")
        except ResourceNotFoundException:
            pass
