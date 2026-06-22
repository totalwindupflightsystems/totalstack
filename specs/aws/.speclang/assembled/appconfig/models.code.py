"""AppConfig store — Applications, ConfigurationProfiles, Environments, Tags."""
import uuid


class BadRequestException(Exception):
    pass


class ResourceNotFoundException(Exception):
    pass


class ConflictException(Exception):
    pass


class InternalServerException(Exception):
    pass


class ServiceQuotaExceededException(Exception):
    pass


class ApplicationRecord:
    def __init__(self, name, id=None, description=None, **kwargs):
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.description = description or ""

    def to_dict(self):
        return {"id": self.id, "name": self.name, "description": self.description}


class ConfigurationProfileRecord:
    def __init__(self, applicationId, name, locationUri, id=None,
                 description=None, retrievalRoleArn=None, validators=None,
                 type=None, kmsKeyIdentifier=None, **kwargs):
        self.id = id or str(uuid.uuid4())
        self.applicationId = applicationId
        self.name = name
        self.locationUri = locationUri
        self.description = description or ""
        self.retrievalRoleArn = retrievalRoleArn
        self.validators = validators
        self.type = type or "AWS.Freeform"
        self.kmsKeyIdentifier = kmsKeyIdentifier

    def to_dict(self):
        return {"id": self.id, "applicationId": self.applicationId,
                "name": self.name, "locationUri": self.locationUri,
                "description": self.description, "type": self.type}


class EnvironmentRecord:
    def __init__(self, applicationId, name, id=None, description=None,
                 monitors=None, **kwargs):
        self.id = id or str(uuid.uuid4())
        self.applicationId = applicationId
        self.name = name
        self.description = description or ""
        self.monitors = monitors
        self.state = "READY_FOR_DEPLOYMENT"

    def to_dict(self):
        return {"id": self.id, "applicationId": self.applicationId,
                "name": self.name, "description": self.description,
                "state": self.state}


class AppConfigStore:
    def __init__(self):
        self._applications = {}
        self._config_profiles = {}
        self._environments = {}
        self._tags = {}

    # --- Applications ---

    def create_application(self, name, description=None, **kwargs):
        record = ApplicationRecord(name=name, description=description)
        self._applications[record.id] = record
        return record.to_dict()

    def get_application(self, applicationId, **kwargs):
        if applicationId not in self._applications:
            raise ResourceNotFoundException("App not found: " + applicationId)
        return self._applications[applicationId].to_dict()

    def list_applications(self, **kwargs):
        return {"items": [a.to_dict() for a in self._applications.values()]}

    def update_application(self, applicationId, name=None, description=None, **kwargs):
        if applicationId not in self._applications:
            raise ResourceNotFoundException("App not found: " + applicationId)
        r = self._applications[applicationId]
        if name is not None:
            r.name = name
        if description is not None:
            r.description = description
        return r.to_dict()

    def delete_application(self, applicationId, **kwargs):
        if applicationId not in self._applications:
            raise ResourceNotFoundException("App not found: " + applicationId)
        del self._applications[applicationId]
        return {}

    # --- Configuration Profiles ---

    def create_configuration_profile(self, applicationId, name, locationUri, **kwargs):
        record = ConfigurationProfileRecord(applicationId=applicationId,
                                             name=name,
                                             locationUri=locationUri, **kwargs)
        self._config_profiles[record.id] = record
        return record.to_dict()

    def get_configuration_profile(self, applicationId, configurationProfileId, **kwargs):
        if configurationProfileId not in self._config_profiles:
            raise ResourceNotFoundException("Profile not found: " + configurationProfileId)
        return self._config_profiles[configurationProfileId].to_dict()

    def list_configuration_profiles(self, applicationId, **kwargs):
        items = [p.to_dict() for p in self._config_profiles.values()
                 if p.applicationId == applicationId]
        return {"items": items}

    def update_configuration_profile(self, applicationId, configurationProfileId, **kwargs):
        if configurationProfileId not in self._config_profiles:
            raise ResourceNotFoundException("Profile not found: " + configurationProfileId)
        r = self._config_profiles[configurationProfileId]
        for k, v in kwargs.items():
            if hasattr(r, k) and v is not None:
                setattr(r, k, v)
        return r.to_dict()

    def delete_configuration_profile(self, applicationId, configurationProfileId, **kwargs):
        if configurationProfileId not in self._config_profiles:
            raise ResourceNotFoundException("Profile not found: " + configurationProfileId)
        del self._config_profiles[configurationProfileId]
        return {}

    # --- Environments ---

    def create_environment(self, applicationId, name, **kwargs):
        record = EnvironmentRecord(applicationId=applicationId, name=name, **kwargs)
        self._environments[record.id] = record
        return record.to_dict()

    def get_environment(self, applicationId, environmentId, **kwargs):
        if environmentId not in self._environments:
            raise ResourceNotFoundException("Env not found: " + environmentId)
        return self._environments[environmentId].to_dict()

    def list_environments(self, applicationId, **kwargs):
        items = [e.to_dict() for e in self._environments.values()
                 if e.applicationId == applicationId]
        return {"items": items}

    def update_environment(self, applicationId, environmentId, **kwargs):
        if environmentId not in self._environments:
            raise ResourceNotFoundException("Env not found: " + environmentId)
        r = self._environments[environmentId]
        for k, v in kwargs.items():
            if hasattr(r, k) and v is not None:
                setattr(r, k, v)
        return r.to_dict()

    def delete_environment(self, applicationId, environmentId, **kwargs):
        if environmentId not in self._environments:
            raise ResourceNotFoundException("Env not found: " + environmentId)
        del self._environments[environmentId]
        return {}

    # --- Tags ---

    def tag_resource(self, resourceArn, tags, **kwargs):
        flat = self._tags.get(resourceArn, {})
        if isinstance(tags, list):
            for t in tags:
                k = t.get("key", t.get("Key", ""))
                v = t.get("value", t.get("Value", ""))
                flat[k] = v
        else:
            flat.update(tags)
        self._tags[resourceArn] = flat
        return {}

    def untag_resource(self, resourceArn, tagKeys, **kwargs):
        if resourceArn in self._tags:
            for k in tagKeys:
                self._tags[resourceArn].pop(k, None)
        return {}

    def list_tags_for_resource(self, resourceArn, **kwargs):
        return {"tags": dict(self._tags.get(resourceArn, {}))}
