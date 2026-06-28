"""Forecast store — time-series forecasting with Dataset, Forecast, Predictor entities.

ARN-based access (no AwsAccountId prefix). Each entity uses private dict collections
with public method accessors for generated handler compatibility.
"""
import time as _time


# ═══════════════════════════════════════════════════════════════════════════════
# Exception classes
# ═══════════════════════════════════════════════════════════════════════════════

class InvalidInputException(Exception):
    pass

class ResourceNotFoundException(Exception):
    pass

class ResourceAlreadyExistsException(Exception):
    pass

class ResourceInUseException(Exception):
    pass

class LimitExceededException(Exception):
    pass

class InvalidNextTokenException(Exception):
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# Record classes
# ═══════════════════════════════════════════════════════════════════════════════

class DatasetRecord:
    def __init__(self, DatasetName, Domain, DatasetType, Schema,
                 DataFrequency=None, EncryptionConfig=None, Tags=None,
                 DatasetArn=None, Status="ACTIVE", CreationTime=None):
        self.DatasetName = DatasetName
        self.Domain = Domain or "CUSTOM"
        self.DatasetType = DatasetType or "TARGET_TIME_SERIES"
        self.Schema = Schema or {}
        self.DataFrequency = DataFrequency
        self.EncryptionConfig = EncryptionConfig
        self.Tags = _tag_list_to_dict(Tags)
        self.DatasetArn = DatasetArn or ""
        self.Status = Status
        self.CreationTime = CreationTime or _time.time()
        self.LastModificationTime = _time.time()

    def to_dict(self):
        return {
            "DatasetArn": self.DatasetArn,
            "DatasetName": self.DatasetName,
            "Domain": self.Domain,
            "DatasetType": self.DatasetType,
            "Status": self.Status,
            "CreationTime": self.CreationTime,
            "LastModificationTime": self.LastModificationTime,
        }


class ForecastRecord:
    def __init__(self, ForecastName, PredictorArn,
                 ForecastTypes=None, Tags=None, TimeSeriesSelector=None,
                 ForecastArn=None, Status="ACTIVE", CreationTime=None):
        self.ForecastName = ForecastName
        self.PredictorArn = PredictorArn or ""
        self.ForecastTypes = ForecastTypes or []
        self.Tags = _tag_list_to_dict(Tags)
        self.TimeSeriesSelector = TimeSeriesSelector
        self.ForecastArn = ForecastArn or ""
        self.Status = Status
        self.CreationTime = CreationTime or _time.time()
        self.LastModificationTime = _time.time()

    def to_dict(self):
        return {
            "ForecastArn": self.ForecastArn,
            "ForecastName": self.ForecastName,
            "PredictorArn": self.PredictorArn,
            "Status": self.Status,
            "CreationTime": self.CreationTime,
        }


class PredictorRecord:
    def __init__(self, PredictorName, ForecastHorizon, InputDataConfig, FeaturizationConfig,
                 AlgorithmArn=None, AutoMLOverrideStrategy=None, EncryptionConfig=None,
                 EvaluationParameters=None, ForecastTypes=None, HPOConfig=None,
                 OptimizationMetric=None, PerformAutoML=None, PerformHPO=None,
                 Tags=None, TrainingParameters=None, PredictorArn=None,
                 IsAutoPredictor=False, Status="ACTIVE", CreationTime=None):
        self.PredictorName = PredictorName
        self.ForecastHorizon = ForecastHorizon or 10
        self.InputDataConfig = InputDataConfig or {}
        self.FeaturizationConfig = FeaturizationConfig or {}
        self.AlgorithmArn = AlgorithmArn
        self.AutoMLOverrideStrategy = AutoMLOverrideStrategy
        self.EncryptionConfig = EncryptionConfig
        self.EvaluationParameters = EvaluationParameters
        self.ForecastTypes = ForecastTypes or []
        self.HPOConfig = HPOConfig
        self.OptimizationMetric = OptimizationMetric
        self.PerformAutoML = PerformAutoML
        self.PerformHPO = PerformHPO
        self.Tags = _tag_list_to_dict(Tags)
        self.TrainingParameters = TrainingParameters
        self.PredictorArn = PredictorArn or ""
        self.IsAutoPredictor = IsAutoPredictor
        self.Status = Status
        self.CreationTime = CreationTime or _time.time()
        self.LastModificationTime = _time.time()

    def to_dict(self):
        return {
            "PredictorArn": self.PredictorArn,
            "PredictorName": self.PredictorName,
            "ForecastHorizon": self.ForecastHorizon,
            "Status": self.Status,
            "IsAutoPredictor": self.IsAutoPredictor,
            "CreationTime": self.CreationTime,
        }


# ═══════════════════════════════════════════════════════════════════════════════
# Helpers
# ═══════════════════════════════════════════════════════════════════════════════

def _tag_list_to_dict(tags):
    if not tags:
        return {}
    if isinstance(tags, list):
        result = {}
        for t in tags:
            k = t.get("Key", t.get("key", ""))
            v = t.get("Value", t.get("value", ""))
            result[k] = v
        return result
    return dict(tags)


def _gen_arn(resource_type, name):
    return f"arn:aws:forecast:us-east-1:123456789012:{resource_type}/{name}"


# ═══════════════════════════════════════════════════════════════════════════════
# Forecast Store
# ═══════════════════════════════════════════════════════════════════════════════

class ForecastStore:
    def __init__(self):
        self._datasets: dict[str, DatasetRecord] = {}
        self._forecasts: dict[str, ForecastRecord] = {}
        self._predictors: dict[str, PredictorRecord] = {}

    # ---- Dataset ----

    def datasets(self, arn=None):
        if arn is not None:
            return self._datasets.get(arn)
        return list(self._datasets.values())

    def create_dataset(self, DatasetName, **kwargs):
        arn = _gen_arn("dataset", DatasetName)
        if arn in self._datasets:
            raise ResourceAlreadyExistsException(f"Dataset {arn} already exists")
        record = DatasetRecord(DatasetName=DatasetName, DatasetArn=arn, **kwargs)
        self._datasets[arn] = record
        return record

    def delete_dataset(self, DatasetArn):
        if DatasetArn not in self._datasets:
            raise ResourceNotFoundException(f"Dataset {DatasetArn} not found")
        del self._datasets[DatasetArn]

    # ---- Forecast ----

    def forecasts(self, arn=None):
        if arn is not None:
            return self._forecasts.get(arn)
        return list(self._forecasts.values())

    def create_forecast(self, ForecastName, **kwargs):
        arn = _gen_arn("forecast", ForecastName)
        if arn in self._forecasts:
            raise ResourceAlreadyExistsException(f"Forecast {arn} already exists")
        record = ForecastRecord(ForecastName=ForecastName, ForecastArn=arn, **kwargs)
        self._forecasts[arn] = record
        return record

    def delete_forecast(self, ForecastArn):
        if ForecastArn not in self._forecasts:
            raise ResourceNotFoundException(f"Forecast {ForecastArn} not found")
        del self._forecasts[ForecastArn]

    # ---- Predictor ----

    def predictors(self, arn=None):
        if arn is not None:
            return self._predictors.get(arn)
        return list(self._predictors.values())

    def create_predictor(self, PredictorName, **kwargs):
        arn = _gen_arn("predictor", PredictorName)
        if arn in self._predictors:
            raise ResourceAlreadyExistsException(f"Predictor {arn} already exists")
        record = PredictorRecord(PredictorName=PredictorName, PredictorArn=arn, **kwargs)
        self._predictors[arn] = record
        return record

    def delete_predictor(self, PredictorArn):
        if PredictorArn not in self._predictors:
            raise ResourceNotFoundException(f"Predictor {PredictorArn} not found")
        del self._predictors[PredictorArn]

    # ---- Tags (ARN-based, cross-entity) ----

    def tag_resource(self, ResourceArn, Tags):
        resource = self._find_by_arn(ResourceArn)
        if resource is None:
            raise ResourceNotFoundException(f"Resource {ResourceArn} not found")
        tag_dict = resource.Tags or {}
        for t in (Tags or []):
            k = t.get("Key", t.get("key", ""))
            v = t.get("Value", t.get("value", ""))
            tag_dict[k] = v
        resource.Tags = tag_dict

    def untag_resource(self, ResourceArn, TagKeys):
        resource = self._find_by_arn(ResourceArn)
        if resource is None:
            raise ResourceNotFoundException(f"Resource {ResourceArn} not found")
        tag_dict = resource.Tags or {}
        for k in (TagKeys or []):
            tag_dict.pop(k, None)
        resource.Tags = tag_dict

    def list_tags_for_resource(self, ResourceArn):
        resource = self._find_by_arn(ResourceArn)
        if resource is None:
            raise ResourceNotFoundException(f"Resource {ResourceArn} not found")
        return resource.Tags or {}

    def _find_by_arn(self, arn):
        if not arn:
            return None
        for rec in self._datasets.values():
            if rec.DatasetArn == arn:
                return rec
        for rec in self._forecasts.values():
            if rec.ForecastArn == arn:
                return rec
        for rec in self._predictors.values():
            if rec.PredictorArn == arn:
                return rec
        return None
