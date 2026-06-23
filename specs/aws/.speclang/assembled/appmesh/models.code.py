"""App Mesh store — 5 entities: Mesh, VirtualNode, VirtualService, VirtualRouter, Route.

Hierarchy: Mesh → VirtualNode/VirtualService/VirtualRouter; VirtualRouter → Route.
All sub-entities are scoped to a mesh. Routes are additionally scoped to a virtual router.
"""

import time as _time
import uuid as _uuid


def _short_arn(service, region, account_id, resource_type, resource_name, mesh_name=None):
    """Generate an ARN-like identifier."""
    base = f"arn:aws:{service}:{region}:{account_id}:mesh"
    if mesh_name:
        base += f"/{mesh_name}"
    base += f"/{resource_type}/{resource_name}"
    return base


def _generate_lock_token():
    return str(_uuid.uuid4())


# ── Exception classes ──────────────────────────────────────────────────

class NotFoundException(Exception):
    def __init__(self, message="Resource not found"):
        self.message = message
        super().__init__(self.message)


class ConflictException(Exception):
    def __init__(self, message="Resource already exists"):
        self.message = message
        super().__init__(self.message)


class BadRequestException(Exception):
    def __init__(self, message="Bad request"):
        self.message = message
        super().__init__(self.message)


class LimitExceededException(Exception):
    def __init__(self, message="Limit exceeded"):
        self.message = message
        super().__init__(self.message)


class ResourceInUseException(Exception):
    def __init__(self, message="Resource in use"):
        self.message = message
        super().__init__(self.message)


class TooManyTagsException(Exception):
    def __init__(self, message="Too many tags"):
        self.message = message
        super().__init__(self.message)


class ServiceUnavailableException(Exception):
    def __init__(self, message="Service unavailable"):
        self.message = message
        super().__init__(self.message)


class InternalServerErrorException(Exception):
    def __init__(self, message="Internal server error"):
        self.message = message
        super().__init__(self.message)


# ── Record classes ─────────────────────────────────────────────────────

class MeshRecord:
    def __init__(self, meshName, spec=None, tags=None):
        self.meshName = meshName
        self.spec = spec or {}
        self.tags = _normalize_tags(tags)
        self.arn = _short_arn("appmesh", "us-east-1", "000000000000", "", meshName)
        self.status = {"status": "ACTIVE"}
        self.metadata = {
            "arn": self.arn,
            "createdAt": _time.time(),
            "lastUpdatedAt": _time.time(),
            "meshOwner": "000000000000",
            "resourceOwner": "000000000000",
            "uid": str(_uuid.uuid4()),
            "version": 1,
        }

    def to_dict(self):
        return {
            "meshName": self.meshName,
            "spec": self.spec,
            "status": self.status,
            "metadata": self.metadata,
        }


class VirtualNodeRecord:
    def __init__(self, meshName, virtualNodeName, spec=None, tags=None):
        self.meshName = meshName
        self.virtualNodeName = virtualNodeName
        self.spec = spec or {}
        self.tags = _normalize_tags(tags)
        self.arn = _short_arn("appmesh", "us-east-1", "000000000000",
                              "virtualNode", virtualNodeName, meshName)
        self.status = {"status": "ACTIVE"}
        self.metadata = {
            "arn": self.arn,
            "createdAt": _time.time(),
            "lastUpdatedAt": _time.time(),
            "meshOwner": "000000000000",
            "resourceOwner": "000000000000",
            "uid": str(_uuid.uuid4()),
            "version": 1,
        }

    def to_dict(self):
        return {
            "meshName": self.meshName,
            "virtualNodeName": self.virtualNodeName,
            "spec": self.spec,
            "status": self.status,
            "metadata": self.metadata,
        }


class VirtualServiceRecord:
    def __init__(self, meshName, virtualServiceName, spec=None, tags=None):
        self.meshName = meshName
        self.virtualServiceName = virtualServiceName
        self.spec = spec or {}
        self.tags = _normalize_tags(tags)
        self.arn = _short_arn("appmesh", "us-east-1", "000000000000",
                              "virtualService", virtualServiceName, meshName)
        self.status = {"status": "ACTIVE"}
        self.metadata = {
            "arn": self.arn,
            "createdAt": _time.time(),
            "lastUpdatedAt": _time.time(),
            "meshOwner": "000000000000",
            "resourceOwner": "000000000000",
            "uid": str(_uuid.uuid4()),
            "version": 1,
        }

    def to_dict(self):
        return {
            "meshName": self.meshName,
            "virtualServiceName": self.virtualServiceName,
            "spec": self.spec,
            "status": self.status,
            "metadata": self.metadata,
        }


class VirtualRouterRecord:
    def __init__(self, meshName, virtualRouterName, spec=None, tags=None):
        self.meshName = meshName
        self.virtualRouterName = virtualRouterName
        self.spec = spec or {}
        self.tags = _normalize_tags(tags)
        self.arn = _short_arn("appmesh", "us-east-1", "000000000000",
                              "virtualRouter", virtualRouterName, meshName)
        self.status = {"status": "ACTIVE"}
        self.metadata = {
            "arn": self.arn,
            "createdAt": _time.time(),
            "lastUpdatedAt": _time.time(),
            "meshOwner": "000000000000",
            "resourceOwner": "000000000000",
            "uid": str(_uuid.uuid4()),
            "version": 1,
        }

    def to_dict(self):
        return {
            "meshName": self.meshName,
            "virtualRouterName": self.virtualRouterName,
            "spec": self.spec,
            "status": self.status,
            "metadata": self.metadata,
        }


class RouteRecord:
    def __init__(self, meshName, virtualRouterName, routeName, spec=None, tags=None):
        self.meshName = meshName
        self.virtualRouterName = virtualRouterName
        self.routeName = routeName
        self.spec = spec or {}
        self.tags = _normalize_tags(tags)
        self.arn = _short_arn("appmesh", "us-east-1", "000000000000",
                              "route", routeName, meshName)
        self.status = {"status": "ACTIVE"}
        self.metadata = {
            "arn": self.arn,
            "createdAt": _time.time(),
            "lastUpdatedAt": _time.time(),
            "meshOwner": "000000000000",
            "resourceOwner": "000000000000",
            "uid": str(_uuid.uuid4()),
            "version": 1,
        }

    def to_dict(self):
        return {
            "meshName": self.meshName,
            "virtualRouterName": self.virtualRouterName,
            "routeName": self.routeName,
            "spec": self.spec,
            "status": self.status,
            "metadata": self.metadata,
        }


def _normalize_tags(tags):
    """Convert AWS tag list to flat dict."""
    if not tags:
        return {}
    if isinstance(tags, dict):
        return dict(tags)
    if isinstance(tags, list):
        result = {}
        for t in tags:
            key = t.get("key", t.get("Key", ""))
            value = t.get("value", t.get("Value", ""))
            result[key] = value
        return result
    return {}


# ── Store class ────────────────────────────────────────────────────────

class AppMeshStore:
    def __init__(self):
        self._meshes = {}
        self._virtual_nodes = {}
        self._virtual_services = {}
        self._virtual_routers = {}
        self._routes = {}
        self._tags = {}
        self._account_id = "000000000000"
        self._region = "us-east-1"

    # ── Mesh ────────────────────────────────────────────────────────

    def meshes(self, name=None):
        if name is not None:
            return self._meshes.get(name)
        return list(self._meshes.values())

    def create_mesh(self, meshName, spec=None, tags=None):
        if meshName in self._meshes:
            raise ConflictException(f"Mesh {meshName} already exists")
        record = MeshRecord(meshName, spec, tags)
        self._meshes[meshName] = record
        if record.tags:
            self._tags[record.arn] = record.tags
        return record

    def describe_mesh(self, meshName, meshOwner=None):
        record = self._meshes.get(meshName)
        if not record:
            raise NotFoundException(f"Mesh {meshName} not found")
        return record

    def list_meshes(self, limit=None, nextToken=None):
        all_meshes = list(self._meshes.values())
        result = [m.to_dict() for m in all_meshes]
        return {"meshes": result, "nextToken": None}

    def delete_mesh(self, meshName):
        if meshName not in self._meshes:
            raise NotFoundException(f"Mesh {meshName} not found")
        # Check for sub-resources
        for key in list(self._virtual_nodes.keys()):
            m, _ = key
            if m == meshName:
                raise ResourceInUseException(f"Mesh {meshName} has virtual nodes")
        for key in list(self._virtual_services.keys()):
            m, _ = key
            if m == meshName:
                raise ResourceInUseException(f"Mesh {meshName} has virtual services")
        for key in list(self._virtual_routers.keys()):
            m, _ = key
            if m == meshName:
                raise ResourceInUseException(f"Mesh {meshName} has virtual routers")
        record = self._meshes.pop(meshName)
        return record

    def update_mesh(self, meshName, spec=None):
        record = self._meshes.get(meshName)
        if not record:
            raise NotFoundException(f"Mesh {meshName} not found")
        if spec is not None:
            record.spec = spec
        record.metadata["lastUpdatedAt"] = _time.time()
        record.metadata["version"] += 1
        return record

    # ── VirtualNode ─────────────────────────────────────────────────

    def virtual_nodes(self, meshName=None, virtualNodeName=None):
        if virtualNodeName is not None and meshName is not None:
            return self._virtual_nodes.get((meshName, virtualNodeName))
        if meshName is not None:
            return [v for k, v in self._virtual_nodes.items() if k[0] == meshName]
        return list(self._virtual_nodes.values())

    def create_virtual_node(self, meshName, virtualNodeName, spec, tags=None, meshOwner=None):
        if meshName not in self._meshes:
            raise NotFoundException(f"Mesh {meshName} not found")
        key = (meshName, virtualNodeName)
        if key in self._virtual_nodes:
            raise ConflictException(f"VirtualNode {virtualNodeName} already exists in mesh {meshName}")
        record = VirtualNodeRecord(meshName, virtualNodeName, spec, tags)
        self._virtual_nodes[key] = record
        if record.tags:
            self._tags[record.arn] = record.tags
        return record

    def describe_virtual_node(self, meshName, virtualNodeName, meshOwner=None):
        record = self._virtual_nodes.get((meshName, virtualNodeName))
        if not record:
            raise NotFoundException(f"VirtualNode {virtualNodeName} not found in mesh {meshName}")
        return record

    def list_virtual_nodes(self, meshName, limit=None, nextToken=None, meshOwner=None):
        nodes = [v.to_dict() for k, v in self._virtual_nodes.items() if k[0] == meshName]
        return {"virtualNodes": nodes, "nextToken": None}

    def delete_virtual_node(self, meshName, virtualNodeName, meshOwner=None):
        key = (meshName, virtualNodeName)
        if key not in self._virtual_nodes:
            raise NotFoundException(f"VirtualNode {virtualNodeName} not found in mesh {meshName}")
        record = self._virtual_nodes.pop(key)
        return record

    def update_virtual_node(self, meshName, virtualNodeName, spec, meshOwner=None):
        key = (meshName, virtualNodeName)
        record = self._virtual_nodes.get(key)
        if not record:
            raise NotFoundException(f"VirtualNode {virtualNodeName} not found in mesh {meshName}")
        if spec is not None:
            record.spec = spec
        record.metadata["lastUpdatedAt"] = _time.time()
        record.metadata["version"] += 1
        return record

    # ── VirtualService ──────────────────────────────────────────────

    def virtual_services(self, meshName=None, virtualServiceName=None):
        if virtualServiceName is not None and meshName is not None:
            return self._virtual_services.get((meshName, virtualServiceName))
        if meshName is not None:
            return [v for k, v in self._virtual_services.items() if k[0] == meshName]
        return list(self._virtual_services.values())

    def create_virtual_service(self, meshName, virtualServiceName, spec, tags=None, meshOwner=None):
        if meshName not in self._meshes:
            raise NotFoundException(f"Mesh {meshName} not found")
        key = (meshName, virtualServiceName)
        if key in self._virtual_services:
            raise ConflictException(f"VirtualService {virtualServiceName} already exists in mesh {meshName}")
        record = VirtualServiceRecord(meshName, virtualServiceName, spec, tags)
        self._virtual_services[key] = record
        if record.tags:
            self._tags[record.arn] = record.tags
        return record

    def describe_virtual_service(self, meshName, virtualServiceName, meshOwner=None):
        record = self._virtual_services.get((meshName, virtualServiceName))
        if not record:
            raise NotFoundException(f"VirtualService {virtualServiceName} not found in mesh {meshName}")
        return record

    def list_virtual_services(self, meshName, limit=None, nextToken=None, meshOwner=None):
        services = [v.to_dict() for k, v in self._virtual_services.items() if k[0] == meshName]
        return {"virtualServices": services, "nextToken": None}

    def delete_virtual_service(self, meshName, virtualServiceName, meshOwner=None):
        key = (meshName, virtualServiceName)
        if key not in self._virtual_services:
            raise NotFoundException(f"VirtualService {virtualServiceName} not found in mesh {meshName}")
        record = self._virtual_services.pop(key)
        return record

    def update_virtual_service(self, meshName, virtualServiceName, spec, meshOwner=None):
        key = (meshName, virtualServiceName)
        record = self._virtual_services.get(key)
        if not record:
            raise NotFoundException(f"VirtualService {virtualServiceName} not found in mesh {meshName}")
        if spec is not None:
            record.spec = spec
        record.metadata["lastUpdatedAt"] = _time.time()
        record.metadata["version"] += 1
        return record

    # ── VirtualRouter ───────────────────────────────────────────────

    def virtual_routers(self, meshName=None, virtualRouterName=None):
        if virtualRouterName is not None and meshName is not None:
            return self._virtual_routers.get((meshName, virtualRouterName))
        if meshName is not None:
            return [v for k, v in self._virtual_routers.items() if k[0] == meshName]
        return list(self._virtual_routers.values())

    def create_virtual_router(self, meshName, virtualRouterName, spec, tags=None, meshOwner=None):
        if meshName not in self._meshes:
            raise NotFoundException(f"Mesh {meshName} not found")
        key = (meshName, virtualRouterName)
        if key in self._virtual_routers:
            raise ConflictException(f"VirtualRouter {virtualRouterName} already exists in mesh {meshName}")
        record = VirtualRouterRecord(meshName, virtualRouterName, spec, tags)
        self._virtual_routers[key] = record
        if record.tags:
            self._tags[record.arn] = record.tags
        return record

    def describe_virtual_router(self, meshName, virtualRouterName, meshOwner=None):
        record = self._virtual_routers.get((meshName, virtualRouterName))
        if not record:
            raise NotFoundException(f"VirtualRouter {virtualRouterName} not found in mesh {meshName}")
        return record

    def list_virtual_routers(self, meshName, limit=None, nextToken=None, meshOwner=None):
        routers = [v.to_dict() for k, v in self._virtual_routers.items() if k[0] == meshName]
        return {"virtualRouters": routers, "nextToken": None}

    def delete_virtual_router(self, meshName, virtualRouterName, meshOwner=None):
        key = (meshName, virtualRouterName)
        if key not in self._virtual_routers:
            raise NotFoundException(f"VirtualRouter {virtualRouterName} not found in mesh {meshName}")
        # Check for routes
        for rkey in list(self._routes.keys()):
            m, vr, _ = rkey
            if m == meshName and vr == virtualRouterName:
                raise ResourceInUseException(f"VirtualRouter {virtualRouterName} has routes")
        record = self._virtual_routers.pop(key)
        return record

    def update_virtual_router(self, meshName, virtualRouterName, spec, meshOwner=None):
        key = (meshName, virtualRouterName)
        record = self._virtual_routers.get(key)
        if not record:
            raise NotFoundException(f"VirtualRouter {virtualRouterName} not found in mesh {meshName}")
        if spec is not None:
            record.spec = spec
        record.metadata["lastUpdatedAt"] = _time.time()
        record.metadata["version"] += 1
        return record

    # ── Route ───────────────────────────────────────────────────────

    def routes(self, meshName=None, virtualRouterName=None, routeName=None):
        if routeName is not None:
            key = (meshName, virtualRouterName, routeName)
            return self._routes.get(key)
        if virtualRouterName is not None:
            return [v for k, v in self._routes.items()
                    if k[0] == meshName and k[1] == virtualRouterName]
        if meshName is not None:
            return [v for k, v in self._routes.items() if k[0] == meshName]
        return list(self._routes.values())

    def create_route(self, meshName, virtualRouterName, routeName, spec, tags=None, meshOwner=None):
        if meshName not in self._meshes:
            raise NotFoundException(f"Mesh {meshName} not found")
        if (meshName, virtualRouterName) not in self._virtual_routers:
            raise NotFoundException(f"VirtualRouter {virtualRouterName} not found in mesh {meshName}")
        key = (meshName, virtualRouterName, routeName)
        if key in self._routes:
            raise ConflictException(f"Route {routeName} already exists in router {virtualRouterName}")
        record = RouteRecord(meshName, virtualRouterName, routeName, spec, tags)
        self._routes[key] = record
        if record.tags:
            self._tags[record.arn] = record.tags
        return record

    def describe_route(self, meshName, virtualRouterName, routeName, meshOwner=None):
        key = (meshName, virtualRouterName, routeName)
        record = self._routes.get(key)
        if not record:
            raise NotFoundException(f"Route {routeName} not found in router {virtualRouterName}")
        return record

    def list_routes(self, meshName, virtualRouterName, limit=None, nextToken=None, meshOwner=None):
        result = [v.to_dict() for k, v in self._routes.items()
                  if k[0] == meshName and k[1] == virtualRouterName]
        return {"routes": result, "nextToken": None}

    def delete_route(self, meshName, virtualRouterName, routeName, meshOwner=None):
        key = (meshName, virtualRouterName, routeName)
        if key not in self._routes:
            raise NotFoundException(f"Route {routeName} not found in router {virtualRouterName}")
        record = self._routes.pop(key)
        return record

    def update_route(self, meshName, virtualRouterName, routeName, spec, meshOwner=None):
        key = (meshName, virtualRouterName, routeName)
        record = self._routes.get(key)
        if not record:
            raise NotFoundException(f"Route {routeName} not found in router {virtualRouterName}")
        if spec is not None:
            record.spec = spec
        record.metadata["lastUpdatedAt"] = _time.time()
        record.metadata["version"] += 1
        return record

    # ── Tags ────────────────────────────────────────────────────────

    def tag_resource(self, resourceArn, tags):
        normalized = _normalize_tags(tags)
        if not normalized:
            return
        existing = self._tags.get(resourceArn, {})
        existing.update(normalized)
        self._tags[resourceArn] = existing

    def untag_resource(self, resourceArn, tagKeys):
        existing = self._tags.get(resourceArn, {})
        for key in tagKeys:
            existing.pop(key, None)
        self._tags[resourceArn] = existing

    def list_tags_for_resource(self, resourceArn):
        tags = self._tags.get(resourceArn, {})
        return {"tags": [{"key": k, "value": v} for k, v in tags.items()]}
