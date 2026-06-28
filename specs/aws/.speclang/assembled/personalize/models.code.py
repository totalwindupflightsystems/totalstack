"""Personalize store — Dataset, Solution, Campaign."""
import time as _t

class ResourceNotFoundException(Exception):pass
class ResourceAlreadyExistsException(Exception):pass
class InvalidInputException(Exception):pass
class ResourceInUseException(Exception):pass

def _tag_dict(tags):
    if not tags: return {}
    if isinstance(tags, list):
        r = {}
        for t in tags:
            k = t.get("tagKey","") or t.get("TagKey","")
            v = t.get("tagValue","") or t.get("TagValue","")
            r[k] = v
        return r
    return dict(tags)

def _arn(t, n):
    return f"arn:aws:personalize:us-east-1:123456789012:{t}/{n}"

class DatasetRecord:
    def __init__(self, name, schemaArn, datasetGroupArn, datasetType, tags=None):
        self.name = name; self.schemaArn = schemaArn; self.datasetGroupArn = datasetGroupArn
        self.datasetType = datasetType; self.tags = _tag_dict(tags)
        self.datasetArn = _arn("dataset", name); self.createdTime = _t.time()
    def to_dict(self):
        return {"datasetArn": self.datasetArn, "name": self.name, "datasetType": self.datasetType, "status": "ACTIVE"}

class SolutionRecord:
    def __init__(self, name, datasetGroupArn, tags=None):
        self.name = name; self.datasetGroupArn = datasetGroupArn; self.tags = _tag_dict(tags)
        self.solutionArn = _arn("solution", name); self.createdTime = _t.time(); self.status = "ACTIVE"
    def to_dict(self):
        return {"solutionArn": self.solutionArn, "name": self.name, "status": "ACTIVE"}

class CampaignRecord:
    def __init__(self, name, solutionVersionArn, tags=None):
        self.name = name; self.solutionVersionArn = solutionVersionArn; self.tags = _tag_dict(tags)
        self.campaignArn = _arn("campaign", name); self.createdTime = _t.time(); self.status = "ACTIVE"
    def to_dict(self):
        return {"campaignArn": self.campaignArn, "name": self.name, "status": "ACTIVE"}

class PersonalizeStore:
    def __init__(self):
        self._datasets = {}
        self._solutions = {}
        self._campaigns = {}

    def datasets(self, arn=None):
        if arn: return self._datasets.get(arn)
        return list(self._datasets.values())

    def create_dataset(self, name, **kw):
        arn = _arn("dataset", name)
        if arn in self._datasets: raise ResourceAlreadyExistsException(f"Dataset {arn} exists")
        r = DatasetRecord(name=name, **kw)
        self._datasets[arn] = r; return r

    def update_dataset(self, datasetArn, **kw):
        if datasetArn not in self._datasets: raise ResourceNotFoundException(f"Dataset {datasetArn} not found")
        rec = self._datasets[datasetArn]
        for k, v in kw.items():
            if hasattr(rec, k): setattr(rec, k, v)
        return rec

    def delete_dataset(self, datasetArn):
        if datasetArn not in self._datasets: raise ResourceNotFoundException(f"Dataset {datasetArn} not found")
        del self._datasets[datasetArn]

    def solutions(self, arn=None):
        if arn: return self._solutions.get(arn)
        return list(self._solutions.values())

    def create_solution(self, name, **kw):
        arn = _arn("solution", name)
        if arn in self._solutions: raise ResourceAlreadyExistsException(f"Solution {arn} exists")
        r = SolutionRecord(name=name, **kw)
        self._solutions[arn] = r; return r

    def delete_solution(self, solutionArn):
        if solutionArn not in self._solutions: raise ResourceNotFoundException(f"Solution {solutionArn} not found")
        del self._solutions[solutionArn]

    def campaigns(self, arn=None):
        if arn: return self._campaigns.get(arn)
        return list(self._campaigns.values())

    def create_campaign(self, name, **kw):
        arn = _arn("campaign", name)
        if arn in self._campaigns: raise ResourceAlreadyExistsException(f"Campaign {arn} exists")
        r = CampaignRecord(name=name, **kw)
        self._campaigns[arn] = r; return r

    def update_campaign(self, campaignArn, **kw):
        if campaignArn not in self._campaigns: raise ResourceNotFoundException(f"Campaign {campaignArn} not found")
        rec = self._campaigns[campaignArn]
        for k, v in kw.items():
            if hasattr(rec, k): setattr(rec, k, v)
        return rec

    def delete_campaign(self, campaignArn):
        if campaignArn not in self._campaigns: raise ResourceNotFoundException(f"Campaign {campaignArn} not found")
        del self._campaigns[campaignArn]

    def _find(self, arn):
        if not arn: return None
        for recs in [self._datasets, self._solutions, self._campaigns]:
            for r in recs.values():
                if (hasattr(r, 'datasetArn') and r.datasetArn == arn) or \
                   (hasattr(r, 'solutionArn') and r.solutionArn == arn) or \
                   (hasattr(r, 'campaignArn') and r.campaignArn == arn):
                    return r
        return None

    def tag_resource(self, resourceArn, tags):
        rec = self._find(resourceArn)
        if not rec: raise ResourceNotFoundException(f"Resource {resourceArn} not found")
        d = rec.tags or {}
        for t in (tags or []):
            k = t.get("tagKey","") or t.get("TagKey","")
            v = t.get("tagValue","") or t.get("TagValue","")
            d[k] = v
        rec.tags = d

    def untag_resource(self, resourceArn, tagKeys):
        rec = self._find(resourceArn)
        if not rec: raise ResourceNotFoundException(f"Resource {resourceArn} not found")
        d = rec.tags or {}
        for k in (tagKeys or []): d.pop(k, None)
        rec.tags = d

    def list_tags_for_resource(self, resourceArn):
        rec = self._find(resourceArn)
        if not rec: raise ResourceNotFoundException(f"Resource {resourceArn} not found")
        return rec.tags or {}
