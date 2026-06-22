"""AppSync store — GraphQL APIs, DataSources, Resolvers, ApiKeys, Tags."""
import uuid
import time


# --- Exception classes ---

class BadRequestException(Exception):
    pass


class NotFoundException(Exception):
    pass


class ConcurrentModificationException(Exception):
    pass


class InternalFailureException(Exception):
    pass


class ApiKeyLimitExceededException(Exception):
    pass


class ApiKeyValidityOutOfBoundsException(Exception):
    pass


# --- Record classes ---

class GraphqlApiRecord:
    def __init__(self, name, authenticationType, apiId=None,
                 logConfig=None, userPoolConfig=None,
                 openIDConnectConfig=None, additionalAuthenticationProviders=None,
                 lambdaAuthorizerConfig=None, apiType=None, visibility=None,
                 introspectionConfig=None, queryDepthLimit=None,
                 resolverCountLimit=None, enhancedMetricsConfig=None,
                 tags=None, **kwargs):
        self.apiId = apiId or str(uuid.uuid4())
        self.name = name
        self.authenticationType = authenticationType
        self.arn = "arn:aws:appsync:us-east-1:000000000000:apis/" + self.apiId
        self.logConfig = logConfig
        self.userPoolConfig = userPoolConfig
        self.openIDConnectConfig = openIDConnectConfig
        self.additionalAuthenticationProviders = additionalAuthenticationProviders
        self.lambdaAuthorizerConfig = lambdaAuthorizerConfig
        self.apiType = apiType or "GRAPHQL"
        self.visibility = visibility or "GLOBAL"
        self.introspectionConfig = introspectionConfig or "ENABLED"
        self.queryDepthLimit = queryDepthLimit
        self.resolverCountLimit = resolverCountLimit
        self.enhancedMetricsConfig = enhancedMetricsConfig
        self.tags = tags or {}

    def to_dict(self):
        return {
            "apiId": self.apiId,
            "name": self.name,
            "arn": self.arn,
            "authenticationType": self.authenticationType,
            "apiType": self.apiType,
        }


class ApiKeyRecord:
    def __init__(self, apiId, id=None, description=None, expires=None, **kwargs):
        self.id = id or str(uuid.uuid4())
        self.apiId = apiId
        self.description = description or ""
        self.expires = expires or int(time.time()) + 604800
        self.created = int(time.time())

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "expires": self.expires,
            "apiId": self.apiId,
        }


class DataSourceRecord:
    def __init__(self, apiId, name, type, description=None,
                 serviceRoleArn=None, dynamodbConfig=None,
                 lambdaConfig=None, elasticsearchConfig=None,
                 openSearchServiceConfig=None, httpConfig=None,
                 relationalDatabaseConfig=None, eventBridgeConfig=None,
                 metricsConfig=None, **kwargs):
        self.apiId = apiId
        self.name = name
        self.type = type
        self.arn = "arn:aws:appsync:us-east-1:000000000000:apis/" + apiId + "/datasources/" + name
        self.description = description or ""
        self.serviceRoleArn = serviceRoleArn
        self.dynamodbConfig = dynamodbConfig
        self.lambdaConfig = lambdaConfig
        self.elasticsearchConfig = elasticsearchConfig
        self.openSearchServiceConfig = openSearchServiceConfig
        self.httpConfig = httpConfig
        self.relationalDatabaseConfig = relationalDatabaseConfig
        self.eventBridgeConfig = eventBridgeConfig
        self.metricsConfig = metricsConfig

    def to_dict(self):
        return {
            "apiId": self.apiId,
            "name": self.name,
            "type": self.type,
            "arn": self.arn,
            "description": self.description,
        }


class ResolverRecord:
    def __init__(self, apiId, typeName, fieldName, dataSourceName=None,
                 requestMappingTemplate=None, responseMappingTemplate=None,
                 kind=None, pipelineConfig=None, syncConfig=None,
                 cachingConfig=None, maxBatchSize=None, runtime=None,
                 code=None, metricsConfig=None, **kwargs):
        self.apiId = apiId
        self.typeName = typeName
        self.fieldName = fieldName
        self.arn = "arn:aws:appsync:us-east-1:000000000000:apis/" + apiId + "/types/" + typeName + "/resolvers/" + fieldName
        self.dataSourceName = dataSourceName
        self.requestMappingTemplate = requestMappingTemplate
        self.responseMappingTemplate = responseMappingTemplate
        self.kind = kind or "UNIT"
        self.pipelineConfig = pipelineConfig
        self.syncConfig = syncConfig
        self.cachingConfig = cachingConfig
        self.maxBatchSize = maxBatchSize
        self.runtime = runtime
        self.code = code
        self.metricsConfig = metricsConfig

    def to_dict(self):
        return {
            "apiId": self.apiId,
            "typeName": self.typeName,
            "fieldName": self.fieldName,
            "arn": self.arn,
            "kind": self.kind,
            "dataSourceName": self.dataSourceName,
        }


# --- Store ---

class AppSyncStore:
    def __init__(self):
        self._apis = {}
        self._api_keys = {}
        self._data_sources = {}
        self._resolvers = {}
        self._tags = {}

    # --- GraphQL APIs ---

    def create_graphql_api(self, name, authenticationType, **kwargs):
        record = GraphqlApiRecord(name=name, authenticationType=authenticationType, **kwargs)
        self._apis[record.apiId] = record
        return {"graphqlApi": record.to_dict()}

    def get_graphql_api(self, apiId, **kwargs):
        if apiId not in self._apis:
            raise NotFoundException("API not found: " + apiId)
        return {"graphqlApi": self._apis[apiId].to_dict()}

    def list_graphql_apis(self, **kwargs):
        items = [a.to_dict() for a in self._apis.values()]
        return {"graphqlApis": items}

    def update_graphql_api(self, apiId, name, authenticationType, **kwargs):
        if apiId not in self._apis:
            raise NotFoundException("API not found: " + apiId)
        record = self._apis[apiId]
        record.name = name
        record.authenticationType = authenticationType
        for k, v in kwargs.items():
            if hasattr(record, k) and v is not None:
                setattr(record, k, v)
        return {"graphqlApi": record.to_dict()}

    def delete_graphql_api(self, apiId, **kwargs):
        if apiId not in self._apis:
            raise NotFoundException("API not found: " + apiId)
        del self._apis[apiId]
        return {}

    # --- API Keys ---

    def create_api_key(self, apiId, description=None, expires=None, **kwargs):
        if apiId not in self._apis:
            raise NotFoundException("API not found: " + apiId)
        record = ApiKeyRecord(apiId=apiId, description=description,
                              expires=expires)
        self._api_keys[record.id] = record
        return {"apiKey": record.to_dict()}

    def list_api_keys(self, apiId, **kwargs):
        items = [k.to_dict() for k in self._api_keys.values()
                 if k.apiId == apiId]
        return {"apiKeys": items}

    def update_api_key(self, apiId, id, description=None, expires=None, **kwargs):
        if id not in self._api_keys:
            raise NotFoundException("API key not found: " + id)
        record = self._api_keys[id]
        if description is not None:
            record.description = description
        if expires is not None:
            record.expires = expires
        return {"apiKey": record.to_dict()}

    def delete_api_key(self, apiId, id, **kwargs):
        if id not in self._api_keys:
            raise NotFoundException("API key not found: " + id)
        del self._api_keys[id]
        return {}

    # --- Data Sources ---

    def _ds_key(self, apiId, name):
        return apiId + ":" + name

    def create_data_source(self, apiId, name, type, **kwargs):
        key = self._ds_key(apiId, name)
        if key in self._data_sources:
            raise ConcurrentModificationException("Data source exists: " + key)
        record = DataSourceRecord(apiId=apiId, name=name, type=type, **kwargs)
        self._data_sources[key] = record
        return {"dataSource": record.to_dict()}

    def get_data_source(self, apiId, name, **kwargs):
        key = self._ds_key(apiId, name)
        if key not in self._data_sources:
            raise NotFoundException("Data source not found: " + key)
        return {"dataSource": self._data_sources[key].to_dict()}

    def list_data_sources(self, apiId, **kwargs):
        items = [d.to_dict() for d in self._data_sources.values()
                 if d.apiId == apiId]
        return {"dataSources": items}

    def update_data_source(self, apiId, name, type, **kwargs):
        key = self._ds_key(apiId, name)
        if key not in self._data_sources:
            raise NotFoundException("Data source not found: " + key)
        record = self._data_sources[key]
        record.type = type
        for k, v in kwargs.items():
            if hasattr(record, k) and v is not None:
                setattr(record, k, v)
        return {"dataSource": record.to_dict()}

    def delete_data_source(self, apiId, name, **kwargs):
        key = self._ds_key(apiId, name)
        if key not in self._data_sources:
            raise NotFoundException("Data source not found: " + key)
        del self._data_sources[key]
        return {}

    # --- Resolvers ---

    def _rslv_key(self, apiId, typeName, fieldName):
        return apiId + ":" + typeName + ":" + fieldName

    def create_resolver(self, apiId, typeName, fieldName, **kwargs):
        key = self._rslv_key(apiId, typeName, fieldName)
        if key in self._resolvers:
            raise ConcurrentModificationException("Resolver exists: " + key)
        record = ResolverRecord(apiId=apiId, typeName=typeName,
                                fieldName=fieldName, **kwargs)
        self._resolvers[key] = record
        return {"resolver": record.to_dict()}

    def get_resolver(self, apiId, typeName, fieldName, **kwargs):
        key = self._rslv_key(apiId, typeName, fieldName)
        if key not in self._resolvers:
            raise NotFoundException("Resolver not found: " + key)
        return {"resolver": self._resolvers[key].to_dict()}

    def list_resolvers(self, apiId, typeName, **kwargs):
        prefix = apiId + ":" + typeName + ":"
        items = [r.to_dict() for k, r in self._resolvers.items()
                 if k.startswith(prefix)]
        return {"resolvers": items}

    def update_resolver(self, apiId, typeName, fieldName, **kwargs):
        key = self._rslv_key(apiId, typeName, fieldName)
        if key not in self._resolvers:
            raise NotFoundException("Resolver not found: " + key)
        record = self._resolvers[key]
        for k, v in kwargs.items():
            if hasattr(record, k) and v is not None:
                setattr(record, k, v)
        return {"resolver": record.to_dict()}

    def delete_resolver(self, apiId, typeName, fieldName, **kwargs):
        key = self._rslv_key(apiId, typeName, fieldName)
        if key not in self._resolvers:
            raise NotFoundException("Resolver not found: " + key)
        del self._resolvers[key]
        return {}

    # --- Tags ---

    def tag_resource(self, resourceArn, tags, **kwargs):
        flat = self._tags.get(resourceArn, {})
        if isinstance(tags, dict):
            flat.update(tags)
        else:
            for t in tags:
                k = t.get("key", t.get("Key", ""))
                v = t.get("value", t.get("Value", ""))
                flat[k] = v
        self._tags[resourceArn] = flat
        return {}

    def untag_resource(self, resourceArn, tagKeys, **kwargs):
        if resourceArn in self._tags:
            for k in tagKeys:
                self._tags[resourceArn].pop(k, None)
        return {}

    def list_tags_for_resource(self, resourceArn, **kwargs):
        flat = self._tags.get(resourceArn, {})
        return {"tags": dict(flat)}
