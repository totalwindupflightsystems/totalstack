"""Kendra (Enterprise Search) — store and data classes."""
import uuid

class InvalidParameterException(Exception):
    pass

class ResourceNotFoundException(Exception):
    pass

class ConflictException(Exception):
    pass

class ValidationException(Exception):
    pass

class InternalServerException(Exception):
    pass

class ThrottlingException(Exception):
    pass

class AccessDeniedException(Exception):
    pass


class IndexRecord:
    def __init__(self, Name, RoleArn, Description=None, Edition=None,
                 ServerSideEncryptionConfiguration=None, tags=None):
        self.Id = uuid.uuid4().hex[:36]
        self.Name = Name
        self.RoleArn = RoleArn
        self.Description = Description or ""
        self.Edition = Edition or "ENTERPRISE_EDITION"
        self.Status = "ACTIVE"
        self.tags = {}
        if tags:
            if isinstance(tags, dict):
                self.tags = dict(tags)
            elif isinstance(tags, list):
                for t in tags:
                    self.tags[t.get("Key", t.get("key", ""))] = t.get("Value", t.get("value", ""))

    def to_dict(self):
        return {
            "Id": self.Id, "Name": self.Name, "RoleArn": self.RoleArn,
            "Description": self.Description, "Edition": self.Edition,
            "Status": self.Status,
        }


class DataSourceRecord:
    def __init__(self, IndexId, Name, Type, Configuration=None,
                 Description=None, Schedule=None, RoleArn=None,
                 tags=None, LanguageCode=None):
        self.Id = uuid.uuid4().hex[:36]
        self.IndexId = IndexId
        self.Name = Name
        self.Type = Type
        self.Description = Description or ""
        self.Status = "ACTIVE"
        self.tags = {}
        if tags:
            if isinstance(tags, dict):
                self.tags = dict(tags)
            elif isinstance(tags, list):
                for t in tags:
                    self.tags[t.get("Key", t.get("key", ""))] = t.get("Value", t.get("value", ""))

    def to_dict(self):
        return {
            "Id": self.Id, "IndexId": self.IndexId, "Name": self.Name,
            "Type": self.Type, "Description": self.Description,
            "Status": self.Status,
        }


class FaqRecord:
    def __init__(self, IndexId, Name, S3Path, RoleArn, Description=None,
                 FileFormat=None, tags=None, LanguageCode=None):
        self.Id = uuid.uuid4().hex[:36]
        self.IndexId = IndexId
        self.Name = Name
        self.S3Path = S3Path
        self.RoleArn = RoleArn
        self.Description = Description or ""
        self.Status = "ACTIVE"
        self.tags = {}
        if tags:
            if isinstance(tags, dict):
                self.tags = dict(tags)
            elif isinstance(tags, list):
                for t in tags:
                    self.tags[t.get("Key", t.get("key", ""))] = t.get("Value", t.get("value", ""))

    def to_dict(self):
        s3 = self.S3Path
        if isinstance(s3, str) and s3.startswith("s3://"):
            parts = s3[5:].split("/", 1)
            s3 = {"Bucket": parts[0], "Key": parts[1] if len(parts) > 1 else ""}
        return {
            "Id": self.Id, "IndexId": self.IndexId, "Name": self.Name,
            "S3Path": s3, "RoleArn": self.RoleArn,
            "Description": self.Description, "Status": self.Status,
        }


class ThesaurusRecord:
    def __init__(self, IndexId, Name, RoleArn, SourceS3Path, Description=None,
                 tags=None):
        self.Id = uuid.uuid4().hex[:36]
        self.IndexId = IndexId
        self.Name = Name
        self.RoleArn = RoleArn
        self.SourceS3Path = SourceS3Path
        self.Description = Description or ""
        self.Status = "ACTIVE"
        self.tags = {}
        if tags:
            if isinstance(tags, dict):
                self.tags = dict(tags)
            elif isinstance(tags, list):
                for t in tags:
                    self.tags[t.get("Key", t.get("key", ""))] = t.get("Value", t.get("value", ""))

    def to_dict(self):
        s3 = self.SourceS3Path
        if isinstance(s3, str) and s3.startswith("s3://"):
            parts = s3[5:].split("/", 1)
            s3 = {"Bucket": parts[0], "Key": parts[1] if len(parts) > 1 else ""}
        return {
            "Id": self.Id, "IndexId": self.IndexId, "Name": self.Name,
            "RoleArn": self.RoleArn, "SourceS3Path": s3,
            "Description": self.Description, "Status": self.Status,
        }


class ExperienceRecord:
    def __init__(self, IndexId, Name, RoleArn=None, Configuration=None,
                 Description=None, tags=None):
        self.Id = uuid.uuid4().hex[:36]
        self.IndexId = IndexId
        self.Name = Name
        self.RoleArn = RoleArn or ""
        self.Description = Description or ""
        self.Status = "ACTIVE"
        self.tags = {}
        if tags:
            if isinstance(tags, dict):
                self.tags = dict(tags)
            elif isinstance(tags, list):
                for t in tags:
                    self.tags[t.get("Key", t.get("key", ""))] = t.get("Value", t.get("value", ""))

    def to_dict(self):
        return {
            "Id": self.Id, "IndexId": self.IndexId, "Name": self.Name,
            "RoleArn": self.RoleArn, "Description": self.Description,
            "Status": self.Status,
        }


class KendraStore:
    def __init__(self):
        self._indices = {}
        self._data_sources = {}
        self._faqs = {}
        self._thesauri = {}
        self._experiences = {}

    # ── Index ──
    def indices(self, indexId=None):
        if indexId is not None:
            return self._indices.get(indexId)
        return list(self._indices.values())

    def create_index(self, Name, RoleArn, **kwargs):
        r = IndexRecord(Name=Name, RoleArn=RoleArn, **kwargs)
        self._indices[r.Id] = r
        self._data_sources[r.Id] = {}
        self._faqs[r.Id] = {}
        self._thesauri[r.Id] = {}
        self._experiences[r.Id] = {}
        return r.to_dict()

    def describe_index(self, Id):
        r = self._indices.get(Id)
        if r is None:
            raise ResourceNotFoundException(f"Index {Id} not found")
        return r.to_dict()

    def delete_index(self, Id):
        if Id not in self._indices:
            raise ResourceNotFoundException(f"Index {Id} not found")
        del self._indices[Id]
        self._data_sources.pop(Id, None)
        self._faqs.pop(Id, None)
        self._thesauri.pop(Id, None)
        self._experiences.pop(Id, None)
        return {}

    def list_indices(self, MaxResults=None, NextToken=None):
        idxs = list(self._indices.values())
        if MaxResults:
            idxs = idxs[:MaxResults]
        return {"IndexConfigurationSummaryItems": []}

    def update_index(self, Id, Name=None, Description=None, RoleArn=None, **kwargs):
        r = self._indices.get(Id)
        if r is None:
            raise ResourceNotFoundException(f"Index {Id} not found")
        if Name is not None:
            r.Name = Name
        if Description is not None:
            r.Description = Description
        if RoleArn is not None:
            r.RoleArn = RoleArn
        return {}

    # ── DataSource ──
    def data_sources(self, indexId, dataSourceId=None):
        ds = self._data_sources.get(indexId, {})
        if dataSourceId is not None:
            return ds.get(dataSourceId)
        return list(ds.values())

    def create_data_source(self, IndexId, Name, Type, **kwargs):
        if IndexId not in self._indices:
            raise ResourceNotFoundException(f"Index {IndexId} not found")
        r = DataSourceRecord(IndexId=IndexId, Name=Name, Type=Type, **kwargs)
        self._data_sources[IndexId][r.Id] = r
        return r.to_dict()

    def describe_data_source(self, Id, IndexId):
        r = self._data_sources.get(IndexId, {}).get(Id)
        if r is None:
            raise ResourceNotFoundException(f"DataSource {Id} not found")
        return r.to_dict()

    def delete_data_source(self, Id, IndexId):
        ds = self._data_sources.get(IndexId, {})
        if Id not in ds:
            raise ResourceNotFoundException(f"DataSource {Id} not found")
        del ds[Id]
        return {}

    def list_data_sources(self, IndexId, MaxResults=None, NextToken=None):
        ds = list(self._data_sources.get(IndexId, {}).values())
        if MaxResults:
            ds = ds[:MaxResults]
        return {"SummaryItems": [d.to_dict() for d in ds]}

    def update_data_source(self, Id, IndexId, Name=None, Description=None, **kwargs):
        r = self._data_sources.get(IndexId, {}).get(Id)
        if r is None:
            raise ResourceNotFoundException(f"DataSource {Id} not found")
        if Name is not None:
            r.Name = Name
        if Description is not None:
            r.Description = Description
        return {}

    # ── Faq ──
    def faqs(self, indexId, faqId=None):
        fs = self._faqs.get(indexId, {})
        if faqId is not None:
            return fs.get(faqId)
        return list(fs.values())

    def create_faq(self, IndexId, Name, S3Path, RoleArn, **kwargs):
        if IndexId not in self._indices:
            raise ResourceNotFoundException(f"Index {IndexId} not found")
        r = FaqRecord(IndexId=IndexId, Name=Name, S3Path=S3Path, RoleArn=RoleArn, **kwargs)
        self._faqs[IndexId][r.Id] = r
        return r.to_dict()

    def describe_faq(self, Id, IndexId):
        r = self._faqs.get(IndexId, {}).get(Id)
        if r is None:
            raise ResourceNotFoundException(f"Faq {Id} not found")
        return r.to_dict()

    def delete_faq(self, Id, IndexId):
        fs = self._faqs.get(IndexId, {})
        if Id not in fs:
            raise ResourceNotFoundException(f"Faq {Id} not found")
        del fs[Id]
        return {}

    def list_faqs(self, IndexId, MaxResults=None, NextToken=None):
        fs = list(self._faqs.get(IndexId, {}).values())
        if MaxResults:
            fs = fs[:MaxResults]
        return {"FaqSummaryItems": [f.to_dict() for f in fs]}

    # ── Thesaurus ──
    def thesauri(self, indexId, thesaurusId=None):
        ts = self._thesauri.get(indexId, {})
        if thesaurusId is not None:
            return ts.get(thesaurusId)
        return list(ts.values())

    def create_thesaurus(self, IndexId, Name, RoleArn, SourceS3Path, **kwargs):
        if IndexId not in self._indices:
            raise ResourceNotFoundException(f"Index {IndexId} not found")
        r = ThesaurusRecord(IndexId=IndexId, Name=Name, RoleArn=RoleArn, SourceS3Path=SourceS3Path, **kwargs)
        self._thesauri[IndexId][r.Id] = r
        return r.to_dict()

    def describe_thesaurus(self, Id, IndexId):
        r = self._thesauri.get(IndexId, {}).get(Id)
        if r is None:
            raise ResourceNotFoundException(f"Thesaurus {Id} not found")
        return r.to_dict()

    def delete_thesaurus(self, Id, IndexId):
        ts = self._thesauri.get(IndexId, {})
        if Id not in ts:
            raise ResourceNotFoundException(f"Thesaurus {Id} not found")
        del ts[Id]
        return {}

    def list_thesauri(self, IndexId, MaxResults=None, NextToken=None):
        ts = list(self._thesauri.get(IndexId, {}).values())
        if MaxResults:
            ts = ts[:MaxResults]
        return {"ThesaurusSummaryItems": [t.to_dict() for t in ts]}

    # ── Experience ──
    def experiences(self, indexId, experienceId=None):
        es = self._experiences.get(indexId, {})
        if experienceId is not None:
            return es.get(experienceId)
        return list(es.values())

    def create_experience(self, IndexId, Name, **kwargs):
        if IndexId not in self._indices:
            raise ResourceNotFoundException(f"Index {IndexId} not found")
        r = ExperienceRecord(IndexId=IndexId, Name=Name, **kwargs)
        self._experiences[IndexId][r.Id] = r
        return r.to_dict()

    def describe_experience(self, Id, IndexId):
        r = self._experiences.get(IndexId, {}).get(Id)
        if r is None:
            raise ResourceNotFoundException(f"Experience {Id} not found")
        return r.to_dict()

    def delete_experience(self, Id, IndexId):
        es = self._experiences.get(IndexId, {})
        if Id not in es:
            raise ResourceNotFoundException(f"Experience {Id} not found")
        del es[Id]
        return {}

    def list_experiences(self, IndexId, MaxResults=None, NextToken=None):
        es = list(self._experiences.get(IndexId, {}).values())
        if MaxResults:
            es = es[:MaxResults]
        return {"SummaryItems": [e.to_dict() for e in es]}

    # ── Tags ──
    def list_tags_for_resource(self, ResourceARN):
        for idx in self._indices.values():
            if idx.Id in ResourceARN:
                return {"Tags": [{"Key": k, "Value": v} for k, v in idx.tags.items()]}
        raise ResourceNotFoundException(f"Resource {ResourceARN} not found")

    def tag_resource(self, ResourceARN, Tags):
        for idx in self._indices.values():
            if idx.Id in ResourceARN:
                if isinstance(Tags, list):
                    for t in Tags:
                        idx.tags[t.get("Key", t.get("key", ""))] = t.get("Value", t.get("value", ""))
                return {}
        raise ResourceNotFoundException(f"Resource {ResourceARN} not found")

    def untag_resource(self, ResourceARN, TagKeys):
        for idx in self._indices.values():
            if idx.Id in ResourceARN:
                for k in TagKeys:
                    idx.tags.pop(k, None)
                return {}
        raise ResourceNotFoundException(f"Resource {ResourceARN} not found")

    # ── Query ──
    def query(self, IndexId, QueryText, **kwargs):
        if IndexId not in self._indices:
            raise ResourceNotFoundException(f"Index {IndexId} not found")
        return {"QueryId": uuid.uuid4().hex, "ResultItems": [], "TotalNumberOfResults": 0}
