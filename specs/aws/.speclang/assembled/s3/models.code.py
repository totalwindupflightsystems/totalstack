"""S3 store and exceptions — TotalStack AWS emulator."""


class S3Exception(Exception):
    """Base S3 exception."""
    pass


class NoSuchBucket(S3Exception):
    """The specified bucket does not exist."""
    pass


class BucketAlreadyExists(S3Exception):
    """The requested bucket name is not available."""
    pass


class NoSuchKey(S3Exception):
    """The specified key does not exist."""
    pass


class BucketAlreadyOwnedByYou(S3Exception):
    """The bucket exists and is owned by you."""
    pass


class S3Store:
    """In-memory store for S3 resources."""

    def __init__(self):
        self._buckets: dict[str, dict] = {}       # bucket_name → {config, objects}
        self._objects: dict[str, dict] = {}       # "bucket/key" → {data, metadata}
        self._multipart_uploads: dict[str, dict] = {}  # upload_id → {parts, metadata}

    def create_bucket(self, name: str, config: dict = None) -> dict:
        if name in self._buckets:
            raise BucketAlreadyOwnedByYou(f"Bucket {name} already exists")
        bucket = {
            'Name': name,
            'CreationDate': '',
            'objects': {},
            'config': config or {},
        }
        self._buckets[name] = bucket
        return bucket

    def buckets(self, name: str = None):
        """Method-style accessor for generated handlers. Returns bucket or raises."""
        if name is not None:
            if name not in self._buckets:
                return None
            return self._buckets[name]
        return list(self._buckets.values())

    def get_bucket(self, name: str) -> dict:
        if name not in self._buckets:
            raise NoSuchBucket(f"Bucket {name} not found")
        return self._buckets[name]

    def list_buckets(self) -> list:
        return list(self._buckets.values())

    def delete_bucket(self, name: str):
        if name not in self._buckets:
            raise NoSuchBucket(f"Bucket {name} not found")
        del self._buckets[name]

    def objects(self, key: str = None):
        """Method-style accessor for generated handlers. Returns object or raises."""
        if key is not None:
            parts = key.split('/', 1)
            if len(parts) == 2:
                return self.get_object(parts[0], parts[1])
            return self._objects.get(key)
        return list(self._objects.values())

    def put_object(self, bucket: str, key: str, data: bytes = b'', metadata: dict = None) -> dict:
        if bucket not in self._buckets:
            raise NoSuchBucket(f"Bucket {bucket} not found")
        obj_key = f"{bucket}/{key}"
        obj = {
            'Key': key,
            'Bucket': bucket,
            'Size': len(data),
            'Data': data,
            'Metadata': metadata or {},
        }
        self._objects[obj_key] = obj
        self._buckets[bucket]['objects'][key] = obj
        return obj

    def get_object(self, bucket: str, key: str) -> dict:
        obj_key = f"{bucket}/{key}"
        if bucket not in self._buckets:
            raise NoSuchBucket(f"Bucket {bucket} not found")
        if obj_key not in self._objects:
            raise NoSuchKey(f"Key {key} not found in bucket {bucket}")
        return self._objects[obj_key]

    def delete_object(self, bucket: str, key: str):
        obj_key = f"{bucket}/{key}"
        if obj_key in self._objects:
            del self._objects[obj_key]
        if bucket in self._buckets and key in self._buckets[bucket]['objects']:
            del self._buckets[bucket]['objects'][key]

    def list_objects(self, bucket: str) -> list:
        if bucket not in self._buckets:
            raise NoSuchBucket(f"Bucket {bucket} not found")
        return list(self._buckets[bucket]['objects'].values())
