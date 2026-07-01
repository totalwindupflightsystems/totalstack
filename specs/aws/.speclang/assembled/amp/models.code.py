"""AMP (Amazon Managed Service for Prometheus) — store and data classes.

Entities:
  1. Workspace — top-level workspace for Prometheus metrics
  2. Scraper — collects metrics from external sources
  3. RuleGroupsNamespace — child of workspace, holds recording/alerting rules
  4. AlertManagerDefinition — child of workspace, alerting configuration
"""

import uuid

# ── Exception Classes ─────────────────────────────────────────────

class InvalidParameterException(Exception):
    """Invalid parameter."""
    pass

class ResourceNotFoundException(Exception):
    """Resource not found."""
    pass

class ConflictException(Exception):
    """Resource already exists."""
    pass

class ServiceQuotaExceededException(Exception):
    """Service quota exceeded."""
    pass

class ThrottlingException(Exception):
    """Too many requests."""
    pass

class InternalServerException(Exception):
    """Internal server error."""
    pass

class AccessDeniedException(Exception):
    """Access denied."""
    pass

class ValidationException(Exception):
    """Validation error."""
    pass


# ── Data Classes ───────────────────────────────────────────────────

class S3Destination:
    def __init__(self, bucketName, key=None):
        self.bucketName = bucketName
        self.key = key

    def to_dict(self):
        d = {"bucketName": self.bucketName}
        if self.key:
            d["key"] = self.key
        return d


class AMPConfiguration:
    def __init__(self, workspaceArn):
        self.workspaceArn = workspaceArn

    def to_dict(self):
        return {"workspaceArn": self.workspaceArn}


class Destination:
    def __init__(self, ampConfiguration=None, s3Configuration=None):
        self.ampConfiguration = None
        self.s3Configuration = None
        if isinstance(ampConfiguration, dict):
            self.ampConfiguration = AMPConfiguration(**ampConfiguration)
        elif ampConfiguration is not None:
            self.ampConfiguration = ampConfiguration
        elif s3Configuration is not None:
            if isinstance(s3Configuration, dict):
                self.s3Configuration = S3Destination(**s3Configuration)
            else:
                self.s3Configuration = s3Configuration

    def to_dict(self):
        d = {}
        if self.ampConfiguration:
            d["ampConfiguration"] = self.ampConfiguration.to_dict()
        if self.s3Configuration:
            d["s3Configuration"] = self.s3Configuration.to_dict()
        return d


class RoleConfiguration:
    def __init__(self, sourceRoleArn=None, targetRoleArn=None):
        self.sourceRoleArn = sourceRoleArn
        self.targetRoleArn = targetRoleArn

    def to_dict(self):
        d = {}
        if self.sourceRoleArn:
            d["sourceRoleArn"] = self.sourceRoleArn
        if self.targetRoleArn:
            d["targetRoleArn"] = self.targetRoleArn
        return d


class ScrapeConfiguration:
    def __init__(self, configurationBlob=None):
        self.configurationBlob = configurationBlob

    def to_dict(self):
        d = {}
        if self.configurationBlob:
            d["configurationBlob"] = self.configurationBlob
        return d


class Source:
    def __init__(self, eksConfiguration=None):
        self.eksConfiguration = None
        if isinstance(eksConfiguration, dict):
            self.eksConfiguration = EksConfiguration(**eksConfiguration)
        elif eksConfiguration is not None:
            self.eksConfiguration = eksConfiguration

    def to_dict(self):
        d = {}
        if self.eksConfiguration:
            d["eksConfiguration"] = self.eksConfiguration.to_dict()
        return d


class EksConfiguration:
    def __init__(self, clusterArn, subnetIds=None, securityGroupIds=None):
        self.clusterArn = clusterArn
        self.subnetIds = subnetIds or []
        self.securityGroupIds = securityGroupIds or []

    def to_dict(self):
        return {
            "clusterArn": self.clusterArn,
            "subnetIds": self.subnetIds,
            "securityGroupIds": self.securityGroupIds,
        }


# ── Record Classes ─────────────────────────────────────────────────

class WorkspaceRecord:
    def __init__(self, alias=None, kmsKeyArn=None, tags=None):
        self.workspaceId = "ws-" + uuid.uuid4().hex[:17]
        self.arn = f"arn:aws:prometheus:us-east-1:000000000000:workspace/{self.workspaceId}"
        self.alias = alias or ""
        self.kmsKeyArn = kmsKeyArn or ""
        self.status = "ACTIVE"
        self.createdAt = None
        self.tags = {}
        if tags:
            if isinstance(tags, dict):
                self.tags = dict(tags)
            elif isinstance(tags, list):
                for t in tags:
                    k = t.get("key", t.get("Key", ""))
                    v = t.get("value", t.get("Value", ""))
                    if k:
                        self.tags[k] = v

    def to_dict(self):
        return {
            "workspaceId": self.workspaceId,
            "arn": self.arn,
            "alias": self.alias,
            "kmsKeyArn": self.kmsKeyArn,
            "status": {"statusCode": self.status},
            "createdAt": self.createdAt,
            "tags": self.tags,
        }


class ScraperRecord:
    def __init__(self, alias=None, destination=None, roleConfiguration=None,
                 scrapeConfiguration=None, source=None, tags=None):
        self.scraperId = "s-" + uuid.uuid4().hex[:17]
        self.arn = f"arn:aws:prometheus:us-east-1:000000000000:scraper/{self.scraperId}"
        self.alias = alias or ""
        if isinstance(destination, dict):
            self.destination = Destination(**destination)
        elif destination is not None:
            self.destination = destination
        else:
            self.destination = None
        if isinstance(roleConfiguration, dict):
            self.roleConfiguration = RoleConfiguration(**roleConfiguration)
        elif roleConfiguration is not None:
            self.roleConfiguration = roleConfiguration
        else:
            self.roleConfiguration = None
        if isinstance(scrapeConfiguration, dict):
            self.scrapeConfiguration = ScrapeConfiguration(**scrapeConfiguration)
        elif scrapeConfiguration is not None:
            self.scrapeConfiguration = scrapeConfiguration
        else:
            self.scrapeConfiguration = None
        if isinstance(source, dict):
            self.source = Source(**source)
        elif source is not None:
            self.source = source
        else:
            self.source = None
        self.status = "ACTIVE"
        self.createdAt = None
        self.tags = {}
        if tags:
            if isinstance(tags, dict):
                self.tags = dict(tags)
            elif isinstance(tags, list):
                for t in tags:
                    k = t.get("key", t.get("Key", ""))
                    v = t.get("value", t.get("Value", ""))
                    if k:
                        self.tags[k] = v

    def to_dict(self):
        d = {
            "scraperId": self.scraperId,
            "arn": self.arn,
            "alias": self.alias,
            "status": {"statusCode": self.status},
            "createdAt": self.createdAt,
            "tags": self.tags,
        }
        if self.destination:
            d["destination"] = self.destination.to_dict()
        if self.roleConfiguration:
            d["roleConfiguration"] = self.roleConfiguration.to_dict()
        if self.scrapeConfiguration:
            d["scrapeConfiguration"] = self.scrapeConfiguration.to_dict()
        if self.source:
            d["source"] = self.source.to_dict()
        return d


class RuleGroupsNamespaceRecord:
    def __init__(self, name, data, tags=None):
        self.name = name
        self.arn = f"arn:aws:prometheus:us-east-1:000000000000:rulegroupsnamespace/{name}"
        self.data = data
        self.status = "ACTIVE"
        self.createdAt = None
        self.tags = {}
        if tags:
            if isinstance(tags, dict):
                self.tags = dict(tags)
            elif isinstance(tags, list):
                for t in tags:
                    k = t.get("key", t.get("Key", ""))
                    v = t.get("value", t.get("Value", ""))
                    if k:
                        self.tags[k] = v

    def to_dict(self):
        return {
            "name": self.name,
            "arn": self.arn,
            "data": self.data,
            "status": self.status,
            "createdAt": self.createdAt,
            "tags": self.tags,
        }


class AlertManagerDefinitionRecord:
    def __init__(self, data):
        self.data = data
        self.status = "ACTIVE"
        self.createdAt = None

    def to_dict(self):
        return {
            "data": self.data,
            "status": self.status,
            "createdAt": self.createdAt,
        }


# ── Store ──────────────────────────────────────────────────────────

class AMPStore:
    """AMP (Amazon Managed Prometheus) store."""

    def __init__(self):
        self._workspaces = {}          # workspaceId → WorkspaceRecord
        self._scrapers = {}            # scraperId → ScraperRecord
        self._rule_groups = {}         # workspaceId → {name: RuleGroupsNamespaceRecord}
        self._alert_managers = {}      # workspaceId → AlertManagerDefinitionRecord

    # ── Workspace ──────────────────────────────────────────────

    def workspaces(self, workspaceId=None):
        """Method-style accessor for generated handlers."""
        if workspaceId is not None:
            return self._workspaces.get(workspaceId)
        return list(self._workspaces.values())

    def create_workspace(self, alias=None, clientToken=None,
                          kmsKeyArn=None, tags=None):
        record = WorkspaceRecord(alias=alias, kmsKeyArn=kmsKeyArn, tags=tags)
        self._workspaces[record.workspaceId] = record
        self._rule_groups[record.workspaceId] = {}
        self._alert_managers[record.workspaceId] = None
        return record.to_dict()

    def describe_workspace(self, workspaceId):
        r = self._workspaces.get(workspaceId)
        if r is None:
            raise ResourceNotFoundException(f"Workspace {workspaceId} not found")
        return r.to_dict()

    def delete_workspace(self, workspaceId):
        if workspaceId not in self._workspaces:
            raise ResourceNotFoundException(f"Workspace {workspaceId} not found")
        del self._workspaces[workspaceId]
        self._rule_groups.pop(workspaceId, None)
        self._alert_managers.pop(workspaceId, None)
        return {}

    def list_workspaces(self, alias=None, maxResults=None, nextToken=None):
        wss = list(self._workspaces.values())
        if alias:
            wss = [w for w in wss if w.alias == alias]
        if maxResults:
            wss = wss[:maxResults]
        return {"workspaces": [w.to_dict() for w in wss]}

    def update_workspace_alias(self, workspaceId, alias=None):
        r = self._workspaces.get(workspaceId)
        if r is None:
            raise ResourceNotFoundException(f"Workspace {workspaceId} not found")
        r.alias = alias or ""
        return {}

    # ── Scraper ─────────────────────────────────────────────────

    def scrapers(self, scraperId=None):
        if scraperId is not None:
            return self._scrapers.get(scraperId)
        return list(self._scrapers.values())

    def create_scraper(self, alias=None, destination=None, roleConfiguration=None,
                       scrapeConfiguration=None, source=None, clientToken=None,
                       tags=None):
        record = ScraperRecord(
            alias=alias,
            destination=destination,
            roleConfiguration=roleConfiguration,
            scrapeConfiguration=scrapeConfiguration,
            source=source,
            tags=tags,
        )
        self._scrapers[record.scraperId] = record
        return record.to_dict()

    def describe_scraper(self, scraperId):
        r = self._scrapers.get(scraperId)
        if r is None:
            raise ResourceNotFoundException(f"Scraper {scraperId} not found")
        return r.to_dict()

    def delete_scraper(self, scraperId):
        if scraperId not in self._scrapers:
            raise ResourceNotFoundException(f"Scraper {scraperId} not found")
        del self._scrapers[scraperId]
        return {}

    def list_scrapers(self, filters=None, maxResults=None, nextToken=None):
        scs = list(self._scrapers.values())
        if filters:
            for f in filters:
                if f.get("workspaceId"):
                    scs = [s for s in scs
                            if s.destination and s.destination.ampConfiguration
                            and s.destination.ampConfiguration.workspaceArn.endswith(f["workspaceId"])]
        if maxResults:
            scs = scs[:maxResults]
        return {"scrapers": [s.to_dict() for s in scs]}

    def update_scraper(self, scraperId, alias=None, destination=None,
                       roleConfiguration=None, scrapeConfiguration=None):
        r = self._scrapers.get(scraperId)
        if r is None:
            raise ResourceNotFoundException(f"Scraper {scraperId} not found")
        if alias is not None:
            r.alias = alias
        if destination is not None:
            if isinstance(destination, dict):
                r.destination = Destination(**destination)
            else:
                r.destination = destination
        if roleConfiguration is not None:
            if isinstance(roleConfiguration, dict):
                r.roleConfiguration = RoleConfiguration(**roleConfiguration)
            else:
                r.roleConfiguration = roleConfiguration
        if scrapeConfiguration is not None:
            if isinstance(scrapeConfiguration, dict):
                r.scrapeConfiguration = ScrapeConfiguration(**scrapeConfiguration)
            else:
                r.scrapeConfiguration = scrapeConfiguration
        return r.to_dict()

    def get_default_scraper_configuration(self):
        return {"configuration": "default-scraper-config"}

    # ── Rule Groups Namespace ───────────────────────────────────

    def rule_groups_namespace(self, workspaceId, name=None):
        rg = self._rule_groups.get(workspaceId, {})
        if name is not None:
            return rg.get(name)
        return list(rg.values())

    def create_rule_groups_namespace(self, workspaceId, name, data,
                                      clientToken=None, tags=None):
        if workspaceId not in self._workspaces:
            raise ResourceNotFoundException(f"Workspace {workspaceId} not found")
        rg = self._rule_groups.get(workspaceId, {})
        if name in rg:
            raise ConflictException(f"RuleGroupsNamespace {name} already exists")
        record = RuleGroupsNamespaceRecord(name=name, data=data, tags=tags)
        self._rule_groups[workspaceId][name] = record
        return record.to_dict()

    def describe_rule_groups_namespace(self, workspaceId, name):
        if workspaceId not in self._workspaces:
            raise ResourceNotFoundException(f"Workspace {workspaceId} not found")
        r = self._rule_groups.get(workspaceId, {}).get(name)
        if r is None:
            raise ResourceNotFoundException(f"RuleGroupsNamespace {name} not found")
        return r.to_dict()

    def delete_rule_groups_namespace(self, workspaceId, name):
        if workspaceId not in self._workspaces:
            raise ResourceNotFoundException(f"Workspace {workspaceId} not found")
        rg = self._rule_groups.get(workspaceId, {})
        if name not in rg:
            raise ResourceNotFoundException(f"RuleGroupsNamespace {name} not found")
        del rg[name]
        return {}

    def list_rule_groups_namespaces(self, workspaceId, name=None,
                                      maxResults=None, nextToken=None):
        if workspaceId not in self._workspaces:
            raise ResourceNotFoundException(f"Workspace {workspaceId} not found")
        rgs = list(self._rule_groups.get(workspaceId, {}).values())
        if name:
            rgs = [r for r in rgs if r.name == name]
        if maxResults:
            rgs = rgs[:maxResults]
        return {"ruleGroupsNamespaces": [r.to_dict() for r in rgs]}

    def put_rule_groups_namespace(self, workspaceId, name, data,
                                    clientToken=None):
        if workspaceId not in self._workspaces:
            raise ResourceNotFoundException(f"Workspace {workspaceId} not found")
        record = RuleGroupsNamespaceRecord(name=name, data=data)
        self._rule_groups[workspaceId][name] = record
        return record.to_dict()

    # ── Alert Manager Definition ────────────────────────────────

    def alert_manager_definition(self, workspaceId):
        r = self._alert_managers.get(workspaceId)
        if r is None:
            raise ResourceNotFoundException("AlertManagerDefinition not found")
        return r

    def create_alert_manager_definition(self, workspaceId, data,
                                          clientToken=None):
        if workspaceId not in self._workspaces:
            raise ResourceNotFoundException(f"Workspace {workspaceId} not found")
        if self._alert_managers.get(workspaceId):
            raise ConflictException("AlertManagerDefinition already exists")
        record = AlertManagerDefinitionRecord(data=data)
        self._alert_managers[workspaceId] = record
        return record.to_dict()

    def describe_alert_manager_definition(self, workspaceId):
        if workspaceId not in self._workspaces:
            raise ResourceNotFoundException(f"Workspace {workspaceId} not found")
        r = self._alert_managers.get(workspaceId)
        if r is None:
            raise ResourceNotFoundException("AlertManagerDefinition not found")
        return r.to_dict()

    def delete_alert_manager_definition(self, workspaceId):
        if workspaceId not in self._workspaces:
            raise ResourceNotFoundException(f"Workspace {workspaceId} not found")
        if not self._alert_managers.get(workspaceId):
            raise ResourceNotFoundException("AlertManagerDefinition not found")
        self._alert_managers[workspaceId] = None
        return {}

    def put_alert_manager_definition(self, workspaceId, data,
                                       clientToken=None):
        if workspaceId not in self._workspaces:
            raise ResourceNotFoundException(f"Workspace {workspaceId} not found")
        record = AlertManagerDefinitionRecord(data=data)
        self._alert_managers[workspaceId] = record
        return record.to_dict()

    # ── Tags ────────────────────────────────────────────────────

    def list_tags_for_resource(self, resourceArn):
        # Walk all collections to find tags by ARN
        for ws in self._workspaces.values():
            if ws.arn == resourceArn:
                return {"tags": ws.tags}
        for sr in self._scrapers.values():
            if sr.arn == resourceArn:
                return {"tags": sr.tags}
        for rg_map in self._rule_groups.values():
            for rg in rg_map.values():
                if rg.arn == resourceArn:
                    return {"tags": rg.tags}
        raise ResourceNotFoundException(f"Resource {resourceArn} not found")

    def tag_resource(self, resourceArn, tags):
        if isinstance(tags, list):
            tag_dict = {}
            for t in tags:
                k = t.get("key", t.get("Key", ""))
                v = t.get("value", t.get("Value", ""))
                if k:
                    tag_dict[k] = v
            tags = tag_dict
        # Walk all collections
        for ws in self._workspaces.values():
            if ws.arn == resourceArn:
                ws.tags.update(tags)
                return {}
        for sr in self._scrapers.values():
            if sr.arn == resourceArn:
                sr.tags.update(tags)
                return {}
        for rg_map in self._rule_groups.values():
            for rg in rg_map.values():
                if rg.arn == resourceArn:
                    rg.tags.update(tags)
                    return {}
        raise ResourceNotFoundException(f"Resource {resourceArn} not found")

    def untag_resource(self, resourceArn, tagKeys):
        for ws in self._workspaces.values():
            if ws.arn == resourceArn:
                for k in tagKeys:
                    ws.tags.pop(k, None)
                return {}
        for sr in self._scrapers.values():
            if sr.arn == resourceArn:
                for k in tagKeys:
                    sr.tags.pop(k, None)
                return {}
        for rg_map in self._rule_groups.values():
            for rg in rg_map.values():
                if rg.arn == resourceArn:
                    for k in tagKeys:
                        rg.tags.pop(k, None)
                    return {}
        raise ResourceNotFoundException(f"Resource {resourceArn} not found")
