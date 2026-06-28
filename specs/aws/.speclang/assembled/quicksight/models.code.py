"""QuickSight store — BI emulation with DataSet, DataSource, Dashboard, Analysis entities.

All resources are scoped by AwsAccountId. Each entity has a private dict collection
with a public method accessor for generated handler compatibility.
"""
import time as _time


# ═══════════════════════════════════════════════════════════════════════════════
# Exception classes — match AWS error codes
# ═══════════════════════════════════════════════════════════════════════════════

class AccessDeniedException(Exception):
    pass

class InvalidParameterValueException(Exception):
    pass

class ResourceNotFoundException(Exception):
    pass

class ResourceExistsException(Exception):
    pass

class ConflictException(Exception):
    pass

class LimitExceededException(Exception):
    pass

class UnsupportedUserEditionException(Exception):
    pass

class InternalFailureException(Exception):
    pass

class InvalidNextTokenException(Exception):
    pass

class ThrottlingException(Exception):
    pass


# ═══════════════════════════════════════════════════════════════════════════════
# Record classes — one per entity
# ═══════════════════════════════════════════════════════════════════════════════

class DataSetRecord:
    def __init__(self, AwsAccountId, DataSetId, Name, PhysicalTableMap, ImportMode,
                 ColumnGroups=None, ColumnLevelPermissionRules=None,
                 DataPrepConfiguration=None, DataSetUsageConfiguration=None,
                 DatasetParameters=None, FieldFolders=None, FolderArns=None,
                 LogicalTableMap=None, PerformanceConfiguration=None,
                 Permissions=None, RowLevelPermissionDataSet=None,
                 RowLevelPermissionTagConfiguration=None,
                 SemanticModelConfiguration=None, Tags=None, UseAs=None,
                 Arn=None, Status=200):
        self.AwsAccountId = AwsAccountId
        self.DataSetId = DataSetId
        self.Name = Name
        self.PhysicalTableMap = PhysicalTableMap or {}
        self.ImportMode = ImportMode or "SPICE"
        self.ColumnGroups = ColumnGroups or []
        self.ColumnLevelPermissionRules = ColumnLevelPermissionRules or []
        self.DataPrepConfiguration = DataPrepConfiguration
        self.DataSetUsageConfiguration = DataSetUsageConfiguration
        self.DatasetParameters = DatasetParameters or []
        self.FieldFolders = FieldFolders or {}
        self.FolderArns = FolderArns or []
        self.LogicalTableMap = LogicalTableMap or {}
        self.PerformanceConfiguration = PerformanceConfiguration
        self.Permissions = Permissions or []
        self.RowLevelPermissionDataSet = RowLevelPermissionDataSet
        self.RowLevelPermissionTagConfiguration = RowLevelPermissionTagConfiguration
        self.SemanticModelConfiguration = SemanticModelConfiguration
        self.Tags = _tag_list_to_dict(Tags)
        self.UseAs = UseAs
        self.Arn = Arn or ""
        self.Status = Status
        self.CreatedTime = _time.time()

    def to_dict(self):
        return {
            "Arn": self.Arn,
            "DataSetId": self.DataSetId,
            "Name": self.Name,
            "ImportMode": self.ImportMode,
            "Status": self.Status,
            "CreatedTime": self.CreatedTime,
        }


class DataSourceRecord:
    def __init__(self, AwsAccountId, DataSourceId, Name, Type,
                 Credentials=None, DataSourceParameters=None,
                 FolderArns=None, Permissions=None, SslProperties=None,
                 Tags=None, VpcConnectionProperties=None,
                 Arn=None, CreationStatus="CREATION_SUCCESSFUL", Status=200):
        self.AwsAccountId = AwsAccountId
        self.DataSourceId = DataSourceId
        self.Name = Name
        self.Type = Type or "ATHENA"
        self.Credentials = Credentials
        self.DataSourceParameters = DataSourceParameters or {}
        self.FolderArns = FolderArns or []
        self.Permissions = Permissions or []
        self.SslProperties = SslProperties
        self.Tags = _tag_list_to_dict(Tags)
        self.VpcConnectionProperties = VpcConnectionProperties
        self.Arn = Arn or ""
        self.CreationStatus = CreationStatus
        self.Status = Status
        self.CreatedTime = _time.time()

    def to_dict(self):
        return {
            "Arn": self.Arn,
            "DataSourceId": self.DataSourceId,
            "Name": self.Name,
            "Type": self.Type,
            "CreationStatus": self.CreationStatus,
            "Status": self.Status,
        }


class DashboardRecord:
    def __init__(self, AwsAccountId, DashboardId, Name,
                 DashboardPublishOptions=None, Definition=None,
                 FolderArns=None, LinkEntities=None, LinkSharingConfiguration=None,
                 Parameters=None, Permissions=None, SourceEntity=None,
                 Tags=None, ThemeArn=None, ValidationStrategy=None,
                 VersionDescription=None, Arn=None, VersionArn=None,
                 CreationStatus="CREATION_SUCCESSFUL", Status=200):
        self.AwsAccountId = AwsAccountId
        self.DashboardId = DashboardId
        self.Name = Name
        self.DashboardPublishOptions = DashboardPublishOptions
        self.Definition = Definition
        self.FolderArns = FolderArns or []
        self.LinkEntities = LinkEntities or []
        self.LinkSharingConfiguration = LinkSharingConfiguration
        self.Parameters = Parameters
        self.Permissions = Permissions or []
        self.SourceEntity = SourceEntity
        self.Tags = _tag_list_to_dict(Tags)
        self.ThemeArn = ThemeArn
        self.ValidationStrategy = ValidationStrategy
        self.VersionDescription = VersionDescription
        self.Arn = Arn or ""
        self.VersionArn = VersionArn or ""
        self.CreationStatus = CreationStatus
        self.Status = Status
        self.CreatedTime = _time.time()

    def to_dict(self):
        return {
            "Arn": self.Arn,
            "DashboardId": self.DashboardId,
            "Name": self.Name,
            "VersionArn": self.VersionArn,
            "CreationStatus": self.CreationStatus,
            "Status": self.Status,
        }


class AnalysisRecord:
    def __init__(self, AwsAccountId, AnalysisId, Name,
                 Definition=None, FolderArns=None, Parameters=None,
                 Permissions=None, SourceEntity=None, Tags=None,
                 ThemeArn=None, ValidationStrategy=None,
                 Arn=None, CreationStatus="CREATION_SUCCESSFUL", Status=200):
        self.AwsAccountId = AwsAccountId
        self.AnalysisId = AnalysisId
        self.Name = Name
        self.Definition = Definition
        self.FolderArns = FolderArns or []
        self.Parameters = Parameters
        self.Permissions = Permissions or []
        self.SourceEntity = SourceEntity
        self.Tags = _tag_list_to_dict(Tags)
        self.ThemeArn = ThemeArn
        self.ValidationStrategy = ValidationStrategy
        self.Arn = Arn or ""
        self.CreationStatus = CreationStatus
        self.Status = Status
        self.CreatedTime = _time.time()

    def to_dict(self):
        return {
            "Arn": self.Arn,
            "AnalysisId": self.AnalysisId,
            "Name": self.Name,
            "CreationStatus": self.CreationStatus,
            "Status": self.Status,
        }


# ═══════════════════════════════════════════════════════════════════════════════
# Helpers
# ═══════════════════════════════════════════════════════════════════════════════

def _tag_list_to_dict(tags):
    """Convert AWS tag list-of-dicts to flat dict."""
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


def _gen_arn(service, region, account_id, resource_type, resource_id):
    return f"arn:aws:{service}:{region}:{account_id}:{resource_type}/{resource_id}"


# ═══════════════════════════════════════════════════════════════════════════════
# QuickSight Store
# ═══════════════════════════════════════════════════════════════════════════════

class QuickSightStore:
    def __init__(self):
        self._datasets: dict[str, DataSetRecord] = {}
        self._datasources: dict[str, DataSourceRecord] = {}
        self._dashboards: dict[str, DashboardRecord] = {}
        self._analyses: dict[str, AnalysisRecord] = {}

    # ---- DataSet ----

    def datasets(self, account_id=None, dataset_id=None):
        """Method-style accessor for generated handlers."""
        if dataset_id is not None:
            key = f"{account_id}/{dataset_id}"
            return self._datasets.get(key)
        if account_id is not None:
            prefix = f"{account_id}/"
            return [r for k, r in self._datasets.items() if k.startswith(prefix)]
        return list(self._datasets.values())

    def create_dataset(self, AwsAccountId, DataSetId, **kwargs):
        key = f"{AwsAccountId}/{DataSetId}"
        if key in self._datasets:
            raise ResourceExistsException(f"DataSet {DataSetId} already exists")
        arn = _gen_arn("quicksight", "us-east-1", AwsAccountId, "dataset", DataSetId)
        record = DataSetRecord(AwsAccountId=AwsAccountId, DataSetId=DataSetId,
                               Arn=arn, **kwargs)
        self._datasets[key] = record
        return record

    def update_dataset(self, AwsAccountId, DataSetId, **kwargs):
        key = f"{AwsAccountId}/{DataSetId}"
        if key not in self._datasets:
            raise ResourceNotFoundException(f"DataSet {DataSetId} not found")
        record = self._datasets[key]
        for k, v in kwargs.items():
            if hasattr(record, k):
                setattr(record, k, v)
        return record

    def delete_dataset(self, AwsAccountId, DataSetId):
        key = f"{AwsAccountId}/{DataSetId}"
        if key not in self._datasets:
            raise ResourceNotFoundException(f"DataSet {DataSetId} not found")
        del self._datasets[key]

    # ---- DataSource ----

    def datasources(self, account_id=None, datasource_id=None):
        if datasource_id is not None:
            key = f"{account_id}/{datasource_id}"
            return self._datasources.get(key)
        if account_id is not None:
            prefix = f"{account_id}/"
            return [r for k, r in self._datasources.items() if k.startswith(prefix)]
        return list(self._datasources.values())

    def create_datasource(self, AwsAccountId, DataSourceId, **kwargs):
        key = f"{AwsAccountId}/{DataSourceId}"
        if key in self._datasources:
            raise ResourceExistsException(f"DataSource {DataSourceId} already exists")
        arn = _gen_arn("quicksight", "us-east-1", AwsAccountId, "datasource", DataSourceId)
        record = DataSourceRecord(AwsAccountId=AwsAccountId, DataSourceId=DataSourceId,
                                  Arn=arn, **kwargs)
        self._datasources[key] = record
        return record

    def update_datasource(self, AwsAccountId, DataSourceId, **kwargs):
        key = f"{AwsAccountId}/{DataSourceId}"
        if key not in self._datasources:
            raise ResourceNotFoundException(f"DataSource {DataSourceId} not found")
        record = self._datasources[key]
        for k, v in kwargs.items():
            if hasattr(record, k):
                setattr(record, k, v)
        return record

    def delete_datasource(self, AwsAccountId, DataSourceId):
        key = f"{AwsAccountId}/{DataSourceId}"
        if key not in self._datasources:
            raise ResourceNotFoundException(f"DataSource {DataSourceId} not found")
        del self._datasources[key]

    # ---- Dashboard ----

    def dashboards(self, account_id=None, dashboard_id=None):
        if dashboard_id is not None:
            key = f"{account_id}/{dashboard_id}"
            return self._dashboards.get(key)
        if account_id is not None:
            prefix = f"{account_id}/"
            return [r for k, r in self._dashboards.items() if k.startswith(prefix)]
        return list(self._dashboards.values())

    def create_dashboard(self, AwsAccountId, DashboardId, **kwargs):
        key = f"{AwsAccountId}/{DashboardId}"
        if key in self._dashboards:
            raise ResourceExistsException(f"Dashboard {DashboardId} already exists")
        arn = _gen_arn("quicksight", "us-east-1", AwsAccountId, "dashboard", DashboardId)
        record = DashboardRecord(AwsAccountId=AwsAccountId, DashboardId=DashboardId,
                                 Arn=arn, VersionArn=arn, **kwargs)
        self._dashboards[key] = record
        return record

    def update_dashboard(self, AwsAccountId, DashboardId, **kwargs):
        key = f"{AwsAccountId}/{DashboardId}"
        if key not in self._dashboards:
            raise ResourceNotFoundException(f"Dashboard {DashboardId} not found")
        record = self._dashboards[key]
        for k, v in kwargs.items():
            if hasattr(record, k):
                setattr(record, k, v)
        return record

    def delete_dashboard(self, AwsAccountId, DashboardId):
        key = f"{AwsAccountId}/{DashboardId}"
        if key not in self._dashboards:
            raise ResourceNotFoundException(f"Dashboard {DashboardId} not found")
        del self._dashboards[key]

    # ---- Analysis ----

    def analyses(self, account_id=None, analysis_id=None):
        if analysis_id is not None:
            key = f"{account_id}/{analysis_id}"
            return self._analyses.get(key)
        if account_id is not None:
            prefix = f"{account_id}/"
            return [r for k, r in self._analyses.items() if k.startswith(prefix)]
        return list(self._analyses.values())

    def create_analysis(self, AwsAccountId, AnalysisId, **kwargs):
        key = f"{AwsAccountId}/{AnalysisId}"
        if key in self._analyses:
            raise ResourceExistsException(f"Analysis {AnalysisId} already exists")
        arn = _gen_arn("quicksight", "us-east-1", AwsAccountId, "analysis", AnalysisId)
        record = AnalysisRecord(AwsAccountId=AwsAccountId, AnalysisId=AnalysisId,
                                Arn=arn, **kwargs)
        self._analyses[key] = record
        return record

    def update_analysis(self, AwsAccountId, AnalysisId, **kwargs):
        key = f"{AwsAccountId}/{AnalysisId}"
        if key not in self._analyses:
            raise ResourceNotFoundException(f"Analysis {AnalysisId} not found")
        record = self._analyses[key]
        for k, v in kwargs.items():
            if hasattr(record, k):
                setattr(record, k, v)
        return record

    def delete_analysis(self, AwsAccountId, AnalysisId, **kwargs):
        key = f"{AwsAccountId}/{AnalysisId}"
        if key not in self._analyses:
            raise ResourceNotFoundException(f"Analysis {AnalysisId} not found")
        del self._analyses[key]

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
            if rec.Arn == arn:
                return rec
        for rec in self._datasources.values():
            if rec.Arn == arn:
                return rec
        for rec in self._dashboards.values():
            if rec.Arn == arn:
                return rec
        for rec in self._analyses.values():
            if rec.Arn == arn:
                return rec
        return None
