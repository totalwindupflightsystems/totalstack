"""Lightsail in-memory store and exception classes — TotalStack AWS emulator."""


# ╔══════════════════════════════════════════════════════════════╗
# ║                        EXCEPTIONS                           ║
# ╚══════════════════════════════════════════════════════════════╝

class ValidationException(Exception):
    """Indicates that the input is invalid or missing required fields."""
    pass


class ResourceNotFoundException(Exception):
    """The operation tried to access a nonexistent resource."""
    pass


class ResourceInUseException(Exception):
    """The resource is already in use / already exists."""
    pass


# ╔══════════════════════════════════════════════════════════════╗
# ║                        STORE                                ║
# ╚══════════════════════════════════════════════════════════════╝

class _DictStore:
    """A dict-like resource collection that handles get/set/delete patterns.

    - .method(key)          → get resource dict or None
    - .method(key, record)  → put resource dict
    - .method(record)       → put resource without key (single-arg set)
    """

    def __init__(self):
        self._data: dict[str, dict] = {}

    @staticmethod
    def _make_key(k):
        """Convert a key to a hashable type. Lists/tuples become tuples,
        strings stay strings, everything else gets str().
        """
        if isinstance(k, (list, tuple)):
            return tuple(k)
        if isinstance(k, str):
            return k
        return str(k)

    def __call__(self, *args):
        """Handle get/set/put patterns based on arg count and types."""
        if not args:
            return list(self._data.values())

        if len(args) == 1:
            arg0 = args[0]
            if isinstance(arg0, dict):
                # Store a record without key — use first value found or a generated key
                key = list(arg0.values())[0] if arg0 else "default"
                self._data[str(key)] = arg0
                return arg0
            # Get by key (may be list, tuple, etc.)
            key = self._make_key(arg0)
            return self._data.get(key)

        if len(args) == 2:
            key, record = args
            key = self._make_key(key)
            self._data[key] = record
            return record

        return None


class LightsailStore:
    """In-memory store for all Lightsail resources.

    Handlers reference store attributes like store.instances(key),
    store.disks(key), store.buckets(key), etc. — each is a dict-backed
    collection that supports get(key) and set(key, record) via __call__.
    """

    def __init__(self):
        # Core resources (backed by _DictStore instances)
        self._collections: dict[str, _DictStore] = {}

    def __getattr__(self, name: str):
        """Dynamic attribute access for store methods.

        Handles:
        - store.{resource}(key)  → get
        - store.{resource}(key, record) → put
        - store.{resource}(record) → put without key
        - store.delete_{resource}(key) → delete
        - store.get_resource(request) → generic list
        - store.execute(op_name, request) → RPC no-op
        - store.tag_resource(arn, tags) → tagging no-op
        """

        # --- delete_* pattern ---
        if name.startswith('delete_'):
            resource_name = name[7:]  # strip 'delete_' prefix
            def _delete(key):
                from collections.abc import Hashable
                k = key if isinstance(key, Hashable) else tuple(key) if isinstance(key, (list, tuple)) else str(key)
                if resource_name not in self._collections or k not in self._collections[resource_name]._data:
                    raise ResourceNotFoundException(f"Resource {key} not found")
                del self._collections[resource_name]._data[k]
                return {}
            return _delete

        # --- special methods ---
        if name == 'get_resource':
            def _get_resource(request=None):
                result = {}
                for coll_name, coll in self._collections.items():
                    result[coll_name] = list(coll._data.values())
                return result
            return _get_resource

        if name == 'execute':
            def _execute(op_name, request=None):
                # RPC-style operations — return mock success
                return {"success": True, "operation": op_name}
            return _execute

        if name == 'tag_resource':
            def _tag_resource(arn, tags):
                return {}
            return _tag_resource

        # --- default: create/return a _DictStore for the resource ---
        if name not in self._collections:
            self._collections[name] = _DictStore()
        return self._collections[name]

    # Direct attribute access for known resource names (avoids __getattr__ overhead
    # for resources referenced by handlers)
    @property
    def instances(self):
        if 'instances' not in self._collections:
            self._collections['instances'] = _DictStore()
        return self._collections['instances']

    @instances.setter
    def instances(self, value):
        pass  # no-op; prevent AttributeError from property setter

    # We need to handle the typo in generated code: "instancess" vs "instances"
    # — __getattr__ handles it dynamically, so no explicit property needed
