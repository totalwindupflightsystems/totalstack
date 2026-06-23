"""Integration tests for App Mesh — 5 entities (Mesh, VirtualNode, VirtualService,
VirtualRouter, Route) + tags. Uses real AppMeshStore from models.code.py.
"""
import pytest
import os
import importlib.util
import types
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'appmesh')

# ── Dynamic module loading ──────────────────────────────────────────

def _load_models():
    """Load models.code.py — returns the module object."""
    path = os.path.join(SERVICE_DIR, 'models.code.py')
    spec = importlib.util.spec_from_file_location('appmesh_models', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_models = _load_models()
AppMeshStore = _models.AppMeshStore
MeshRecord = _models.MeshRecord
VirtualNodeRecord = _models.VirtualNodeRecord
VirtualServiceRecord = _models.VirtualServiceRecord
VirtualRouterRecord = _models.VirtualRouterRecord
RouteRecord = _models.RouteRecord
NotFoundException = _models.NotFoundException
ConflictException = _models.ConflictException
BadRequestException = _models.BadRequestException
ResourceInUseException = _models.ResourceInUseException
TooManyTagsException = _models.TooManyTagsException


# ── Dynamic handler loading ─────────────────────────────────────────

skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}

def _load_handler(op_name):
    """Load a generated .code.py handler — returns the function."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception classes + Record classes (generated code references bare names)
    mod.NotFoundException = NotFoundException
    mod.ConflictException = ConflictException
    mod.BadRequestException = BadRequestException
    mod.ResourceInUseException = ResourceInUseException
    mod.LimitExceededException = _models.LimitExceededException
    mod.ServiceUnavailableException = _models.ServiceUnavailableException
    mod.InternalServerErrorException = _models.InternalServerErrorException
    mod.TooManyTagsException = TooManyTagsException
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    spec.loader.exec_module(mod)
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


# ── Mesh Tests ──────────────────────────────────────────────────────

class TestMeshIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AppMeshStore()
        return self._store

    def test_create_mesh_happy(self):
        handler = _load_handler('create-mesh')
        resp = handler(self.store, {"meshName": "test-mesh", "spec": {}})
        assert resp["meshName"] == "test-mesh"
        assert resp["status"]["status"] == "ACTIVE"
        assert resp["metadata"]["meshOwner"] == "000000000000"

    def test_create_mesh_duplicate(self):
        handler = _load_handler('create-mesh')
        handler(self.store, {"meshName": "dup-mesh", "spec": {}})
        with pytest.raises(ConflictException):
            handler(self.store, {"meshName": "dup-mesh", "spec": {}})

    def test_create_mesh_with_tags(self):
        handler = _load_handler('create-mesh')
        resp = handler(self.store, {
            "meshName": "tagged-mesh",
            "spec": {},
            "tags": [{"key": "env", "value": "test"}, {"key": "team", "value": "platform"}]
        })
        assert resp["meshName"] == "tagged-mesh"

    def test_describe_mesh_happy(self):
        create = _load_handler('create-mesh')
        describe = _load_handler('describe-mesh')
        create(self.store, {"meshName": "desc-mesh", "spec": {}})
        resp = describe(self.store, {"meshName": "desc-mesh"})
        assert resp["meshName"] == "desc-mesh"

    def test_describe_mesh_nonexistent(self):
        handler = _load_handler('describe-mesh')
        with pytest.raises(NotFoundException):
            handler(self.store, {"meshName": "no-such-mesh"})

    def test_list_meshes(self):
        create = _load_handler('create-mesh')
        list_h = _load_handler('list-meshes')
        create(self.store, {"meshName": "list-m1", "spec": {}})
        create(self.store, {"meshName": "list-m2", "spec": {}})
        resp = list_h(self.store, {})
        assert len(resp["meshes"]) >= 2

    def test_update_mesh_happy(self):
        create = _load_handler('create-mesh')
        update = _load_handler('update-mesh')
        create(self.store, {"meshName": "upd-mesh", "spec": {}})
        resp = update(self.store, {"meshName": "upd-mesh", "spec": {"egressFilter": {"type": "ALLOW_ALL"}}})
        assert resp["spec"]["egressFilter"]["type"] == "ALLOW_ALL"

    def test_update_mesh_nonexistent(self):
        handler = _load_handler('update-mesh')
        with pytest.raises(NotFoundException):
            handler(self.store, {"meshName": "no-such-mesh", "spec": {}})

    def test_delete_mesh_happy(self):
        create = _load_handler('create-mesh')
        delete = _load_handler('delete-mesh')
        describe = _load_handler('describe-mesh')
        create(self.store, {"meshName": "del-mesh", "spec": {}})
        delete(self.store, {"meshName": "del-mesh"})
        with pytest.raises(NotFoundException):
            describe(self.store, {"meshName": "del-mesh"})

    def test_delete_mesh_nonexistent(self):
        handler = _load_handler('delete-mesh')
        with pytest.raises(NotFoundException):
            handler(self.store, {"meshName": "no-such-mesh"})

    def test_delete_mesh_in_use(self):
        create_m = _load_handler('create-mesh')
        create_vn = _load_handler('create-virtual-node')
        delete = _load_handler('delete-mesh')
        create_m(self.store, {"meshName": "inuse-mesh", "spec": {}})
        create_vn(self.store, {"meshName": "inuse-mesh", "virtualNodeName": "vn1", "spec": {}})
        with pytest.raises(ResourceInUseException):
            delete(self.store, {"meshName": "inuse-mesh"})


# ── VirtualNode Tests ───────────────────────────────────────────────

class TestVirtualNodeIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AppMeshStore()
            import time as _t
            import uuid as _u
            create_m_mod = types.ModuleType('create_mesh_mod')
            create_m_mod.NotFoundException = NotFoundException
            create_m_mod.ConflictException = ConflictException
            create_m_mod.BadRequestException = BadRequestException
            create_m_mod.time = _t
            create_m_mod.uuid = _u
            create_m_mod.dataclass = lambda f: f
            path = os.path.join(SERVICE_DIR, 'create-mesh.code.py')
            sp = importlib.util.spec_from_file_location('_cm', path)
            m = importlib.util.module_from_spec(sp)
            m.NotFoundException = NotFoundException
            m.ConflictException = ConflictException
            m.BadRequestException = BadRequestException
            m.time = _t
            m.uuid = _u
            m.dataclass = lambda f: f
            sp.loader.exec_module(m)
            h = None
            for v in m.__dict__.values():
                if isinstance(v, types.FunctionType) and not v.__name__.startswith('_') and v.__name__ not in skip_names:
                    h = v
                    break
            h(self._store, {"meshName": "vn-mesh", "spec": {}})
        return self._store

    def test_create_virtual_node_happy(self):
        handler = _load_handler('create-virtual-node')
        resp = handler(self.store, {
            "meshName": "vn-mesh",
            "virtualNodeName": "vn1",
            "spec": {"backends": []}
        })
        assert resp["virtualNodeName"] == "vn1"
        assert resp["meshName"] == "vn-mesh"

    def test_create_virtual_node_mesh_not_found(self):
        handler = _load_handler('create-virtual-node')
        with pytest.raises(NotFoundException):
            handler(self.store, {
                "meshName": "no-such-mesh",
                "virtualNodeName": "vn2",
                "spec": {}
            })

    def test_create_virtual_node_duplicate(self):
        handler = _load_handler('create-virtual-node')
        handler(self.store, {
            "meshName": "vn-mesh",
            "virtualNodeName": "dup-vn",
            "spec": {}
        })
        with pytest.raises(ConflictException):
            handler(self.store, {
                "meshName": "vn-mesh",
                "virtualNodeName": "dup-vn",
                "spec": {}
            })

    def test_describe_virtual_node_happy(self):
        create = _load_handler('create-virtual-node')
        describe = _load_handler('describe-virtual-node')
        create(self.store, {
            "meshName": "vn-mesh",
            "virtualNodeName": "desc-vn",
            "spec": {}
        })
        resp = describe(self.store, {"meshName": "vn-mesh", "virtualNodeName": "desc-vn"})
        assert resp["virtualNodeName"] == "desc-vn"

    def test_describe_virtual_node_nonexistent(self):
        handler = _load_handler('describe-virtual-node')
        with pytest.raises(NotFoundException):
            handler(self.store, {"meshName": "vn-mesh", "virtualNodeName": "no-such-vn"})

    def test_list_virtual_nodes(self):
        create = _load_handler('create-virtual-node')
        list_h = _load_handler('list-virtual-nodes')
        create(self.store, {"meshName": "vn-mesh", "virtualNodeName": "lvn1", "spec": {}})
        create(self.store, {"meshName": "vn-mesh", "virtualNodeName": "lvn2", "spec": {}})
        resp = list_h(self.store, {"meshName": "vn-mesh"})
        assert len(resp["virtualNodes"]) >= 2

    def test_update_virtual_node_happy(self):
        create = _load_handler('create-virtual-node')
        update = _load_handler('update-virtual-node')
        create(self.store, {
            "meshName": "vn-mesh",
            "virtualNodeName": "upd-vn",
            "spec": {"backends": []}
        })
        resp = update(self.store, {
            "meshName": "vn-mesh",
            "virtualNodeName": "upd-vn",
            "spec": {"backends": [{"virtualService": {"virtualServiceName": "test.local"}}]}
        })
        assert len(resp["spec"]["backends"]) == 1

    def test_delete_virtual_node_happy(self):
        create = _load_handler('create-virtual-node')
        delete = _load_handler('delete-virtual-node')
        describe = _load_handler('describe-virtual-node')
        create(self.store, {"meshName": "vn-mesh", "virtualNodeName": "del-vn", "spec": {}})
        delete(self.store, {"meshName": "vn-mesh", "virtualNodeName": "del-vn"})
        with pytest.raises(NotFoundException):
            describe(self.store, {"meshName": "vn-mesh", "virtualNodeName": "del-vn"})


# ── VirtualService Tests ────────────────────────────────────────────

class TestVirtualServiceIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AppMeshStore()
            import time as _t
            import uuid as _u
            path = os.path.join(SERVICE_DIR, 'create-mesh.code.py')
            sp = importlib.util.spec_from_file_location('_cm2', path)
            m = importlib.util.module_from_spec(sp)
            m.NotFoundException = NotFoundException
            m.ConflictException = ConflictException
            m.BadRequestException = BadRequestException
            m.time = _t
            m.uuid = _u
            m.dataclass = lambda f: f
            sp.loader.exec_module(m)
            h = None
            for v in m.__dict__.values():
                if isinstance(v, types.FunctionType) and not v.__name__.startswith('_') and v.__name__ not in skip_names:
                    h = v
                    break
            h(self._store, {"meshName": "vs-mesh", "spec": {}})
        return self._store

    def test_create_virtual_service_happy(self):
        handler = _load_handler('create-virtual-service')
        resp = handler(self.store, {
            "meshName": "vs-mesh",
            "virtualServiceName": "vs1.local",
            "spec": {}
        })
        assert resp["virtualServiceName"] == "vs1.local"

    def test_create_virtual_service_duplicate(self):
        handler = _load_handler('create-virtual-service')
        handler(self.store, {
            "meshName": "vs-mesh",
            "virtualServiceName": "dup-vs.local",
            "spec": {}
        })
        with pytest.raises(ConflictException):
            handler(self.store, {
                "meshName": "vs-mesh",
                "virtualServiceName": "dup-vs.local",
                "spec": {}
            })

    def test_list_virtual_services(self):
        handler = _load_handler('list-virtual-services')
        resp = handler(self.store, {"meshName": "vs-mesh"})
        assert isinstance(resp["virtualServices"], list)

    def test_delete_virtual_service(self):
        create = _load_handler('create-virtual-service')
        delete = _load_handler('delete-virtual-service')
        describe = _load_handler('describe-virtual-service')
        create(self.store, {"meshName": "vs-mesh", "virtualServiceName": "del-vs.local", "spec": {}})
        delete(self.store, {"meshName": "vs-mesh", "virtualServiceName": "del-vs.local"})
        with pytest.raises(NotFoundException):
            describe(self.store, {"meshName": "vs-mesh", "virtualServiceName": "del-vs.local"})


# ── VirtualRouter Tests ─────────────────────────────────────────────

class TestVirtualRouterIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AppMeshStore()
            import time as _t
            import uuid as _u
            path = os.path.join(SERVICE_DIR, 'create-mesh.code.py')
            sp = importlib.util.spec_from_file_location('_cm3', path)
            m = importlib.util.module_from_spec(sp)
            m.NotFoundException = NotFoundException
            m.ConflictException = ConflictException
            m.BadRequestException = BadRequestException
            m.time = _t
            m.uuid = _u
            m.dataclass = lambda f: f
            sp.loader.exec_module(m)
            h = None
            for v in m.__dict__.values():
                if isinstance(v, types.FunctionType) and not v.__name__.startswith('_') and v.__name__ not in skip_names:
                    h = v
                    break
            h(self._store, {"meshName": "vr-mesh", "spec": {}})
        return self._store

    def test_create_virtual_router_happy(self):
        handler = _load_handler('create-virtual-router')
        resp = handler(self.store, {
            "meshName": "vr-mesh",
            "virtualRouterName": "vr1",
            "spec": {}
        })
        assert resp["virtualRouterName"] == "vr1"

    def test_create_virtual_router_duplicate(self):
        handler = _load_handler('create-virtual-router')
        handler(self.store, {"meshName": "vr-mesh", "virtualRouterName": "dup-vr", "spec": {}})
        with pytest.raises(ConflictException):
            handler(self.store, {"meshName": "vr-mesh", "virtualRouterName": "dup-vr", "spec": {}})

    def test_list_virtual_routers(self):
        handler = _load_handler('list-virtual-routers')
        resp = handler(self.store, {"meshName": "vr-mesh"})
        assert isinstance(resp["virtualRouters"], list)

    def test_delete_virtual_router(self):
        create = _load_handler('create-virtual-router')
        delete = _load_handler('delete-virtual-router')
        describe = _load_handler('describe-virtual-router')
        create(self.store, {"meshName": "vr-mesh", "virtualRouterName": "del-vr", "spec": {}})
        delete(self.store, {"meshName": "vr-mesh", "virtualRouterName": "del-vr"})
        with pytest.raises(NotFoundException):
            describe(self.store, {"meshName": "vr-mesh", "virtualRouterName": "del-vr"})


# ── Route Tests ─────────────────────────────────────────────────────

class TestRouteIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AppMeshStore()
            import time as _t
            import uuid as _u
            st = self._store
            # Create mesh
            path = os.path.join(SERVICE_DIR, 'create-mesh.code.py')
            sp = importlib.util.spec_from_file_location('_cm4', path)
            m = importlib.util.module_from_spec(sp)
            m.NotFoundException = NotFoundException
            m.ConflictException = ConflictException
            m.BadRequestException = BadRequestException
            m.time = _t
            m.uuid = _u
            m.dataclass = lambda f: f
            sp.loader.exec_module(m)
            h = None
            for v in m.__dict__.values():
                if isinstance(v, types.FunctionType) and not v.__name__.startswith('_') and v.__name__ not in skip_names:
                    h = v
                    break
            h(st, {"meshName": "rt-mesh", "spec": {}})
            # Create virtual router
            path2 = os.path.join(SERVICE_DIR, 'create-virtual-router.code.py')
            sp2 = importlib.util.spec_from_file_location('_cvr', path2)
            m2 = importlib.util.module_from_spec(sp2)
            m2.NotFoundException = NotFoundException
            m2.ConflictException = ConflictException
            m2.BadRequestException = BadRequestException
            m2.time = _t
            m2.uuid = _u
            m2.dataclass = lambda f: f
            sp2.loader.exec_module(m2)
            h2 = None
            for v in m2.__dict__.values():
                if isinstance(v, types.FunctionType) and not v.__name__.startswith('_') and v.__name__ not in skip_names:
                    h2 = v
                    break
            h2(st, {"meshName": "rt-mesh", "virtualRouterName": "rt-vr", "spec": {}})
        return self._store

    def test_create_route_happy(self):
        handler = _load_handler('create-route')
        resp = handler(self.store, {
            "meshName": "rt-mesh",
            "virtualRouterName": "rt-vr",
            "routeName": "rt1",
            "spec": {}
        })
        assert resp["routeName"] == "rt1"
        assert resp["virtualRouterName"] == "rt-vr"

    def test_create_route_router_not_found(self):
        handler = _load_handler('create-route')
        with pytest.raises(NotFoundException):
            handler(self.store, {
                "meshName": "rt-mesh",
                "virtualRouterName": "no-such-vr",
                "routeName": "rt2",
                "spec": {}
            })

    def test_create_route_duplicate(self):
        handler = _load_handler('create-route')
        handler(self.store, {
            "meshName": "rt-mesh",
            "virtualRouterName": "rt-vr",
            "routeName": "dup-rt",
            "spec": {}
        })
        with pytest.raises(ConflictException):
            handler(self.store, {
                "meshName": "rt-mesh",
                "virtualRouterName": "rt-vr",
                "routeName": "dup-rt",
                "spec": {}
            })

    def test_describe_route_happy(self):
        create = _load_handler('create-route')
        describe = _load_handler('describe-route')
        create(self.store, {
            "meshName": "rt-mesh",
            "virtualRouterName": "rt-vr",
            "routeName": "desc-rt",
            "spec": {}
        })
        resp = describe(self.store, {
            "meshName": "rt-mesh",
            "virtualRouterName": "rt-vr",
            "routeName": "desc-rt"
        })
        assert resp["routeName"] == "desc-rt"

    def test_list_routes(self):
        create = _load_handler('create-route')
        list_h = _load_handler('list-routes')
        create(self.store, {
            "meshName": "rt-mesh",
            "virtualRouterName": "rt-vr",
            "routeName": "lrt1",
            "spec": {}
        })
        resp = list_h(self.store, {"meshName": "rt-mesh", "virtualRouterName": "rt-vr"})
        assert len(resp["routes"]) >= 1

    def test_delete_route(self):
        create = _load_handler('create-route')
        delete = _load_handler('delete-route')
        describe = _load_handler('describe-route')
        create(self.store, {
            "meshName": "rt-mesh",
            "virtualRouterName": "rt-vr",
            "routeName": "del-rt",
            "spec": {}
        })
        delete(self.store, {
            "meshName": "rt-mesh",
            "virtualRouterName": "rt-vr",
            "routeName": "del-rt"
        })
        with pytest.raises(NotFoundException):
            describe(self.store, {
                "meshName": "rt-mesh",
                "virtualRouterName": "rt-vr",
                "routeName": "del-rt"
            })


# ── Tags Tests ──────────────────────────────────────────────────────

class TestTagsIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AppMeshStore()
            import time as _t
            import uuid as _u
            st = self._store
            path = os.path.join(SERVICE_DIR, 'create-mesh.code.py')
            sp = importlib.util.spec_from_file_location('_cm5', path)
            m = importlib.util.module_from_spec(sp)
            m.NotFoundException = NotFoundException
            m.ConflictException = ConflictException
            m.BadRequestException = BadRequestException
            m.time = _t
            m.uuid = _u
            m.dataclass = lambda f: f
            sp.loader.exec_module(m)
            h = None
            for v in m.__dict__.values():
                if isinstance(v, types.FunctionType) and not v.__name__.startswith('_') and v.__name__ not in skip_names:
                    h = v
                    break
            resp = h(st, {"meshName": "tag-mesh", "spec": {},
                          "tags": [{"key": "env", "value": "prod"}]})
            self._mesh_arn = resp["metadata"]["arn"]
        return self._store

    def test_list_tags_for_resource(self):
        handler = _load_handler('list-tags-for-resource')
        resp = handler(self.store, {"resourceArn": self._mesh_arn})
        tags = resp["tags"]
        assert {"key": "env", "value": "prod"} in tags

    def test_tag_resource(self):
        tag = _load_handler('tag-resource')
        list_tags = _load_handler('list-tags-for-resource')
        tag(self.store, {
            "resourceArn": self._mesh_arn,
            "tags": [{"key": "team", "value": "platform"}]
        })
        resp = list_tags(self.store, {"resourceArn": self._mesh_arn})
        tags = resp["tags"]
        assert {"key": "team", "value": "platform"} in tags

    def test_untag_resource(self):
        untag = _load_handler('untag-resource')
        list_tags = _load_handler('list-tags-for-resource')
        untag(self.store, {
            "resourceArn": self._mesh_arn,
            "tagKeys": ["env"]
        })
        resp = list_tags(self.store, {"resourceArn": self._mesh_arn})
        keys = [t["key"] for t in resp["tags"]]
        assert "env" not in keys
