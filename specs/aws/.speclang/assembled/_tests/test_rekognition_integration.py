"""Integration test for Rekognition — real RekognitionStore."""
import pytest
import os
import sys
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'rekognition')

# ── Load models.code.py dynamically ──
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

RekognitionStore = models_mod.RekognitionStore
InvalidParameterException = models_mod.InvalidParameterException
ResourceNotFoundException = models_mod.ResourceNotFoundException
ResourceInUseException = models_mod.ResourceInUseException
InvalidPaginationTokenException = models_mod.InvalidPaginationTokenException
# Pull in helper functions
_generate_mock_face = models_mod._generate_mock_face


def _load_handler(op_name, globals_inject=None):
    """Load a single-handler .code.py file — returns the handler function."""
    import time as _time
    import uuid as _uuid
    
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    # Inject exception classes (generated code references them without imports)
    mod.InvalidParameterException = InvalidParameterException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ResourceInUseException = ResourceInUseException
    mod.InvalidPaginationTokenException = InvalidPaginationTokenException
    mod.AccessDeniedException = models_mod.AccessDeniedException
    mod.ThrottlingException = models_mod.ThrottlingException
    mod.InternalServerException = models_mod.InternalServerException
    mod.ServiceQuotaExceededException = models_mod.ServiceQuotaExceededException
    mod.InvalidS3ObjectException = models_mod.InvalidS3ObjectException
    mod.LimitExceededException = models_mod.LimitExceededException
    mod.ProvisionedThroughputExceededException = models_mod.ProvisionedThroughputExceededException
    # Inject standard library items used in generated code
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f  # no-op decorator
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    # Find the handler function (skip imports and Exception classes)
    handler = None
    skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
    for v in mod.__dict__.values():
        if isinstance(v, types.FunctionType) and not v.__name__.startswith('_') and v.__name__ not in skip_names:
            handler = v
            break
    return handler


def _load_module(op_name, globals_inject=None):
    """Load a generated .code.py module (returns the module object)."""
    import time as _time
    import uuid as _uuid
    
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.InvalidParameterException = InvalidParameterException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ResourceInUseException = ResourceInUseException
    mod.InvalidPaginationTokenException = InvalidPaginationTokenException
    mod.AccessDeniedException = models_mod.AccessDeniedException
    mod.ThrottlingException = models_mod.ThrottlingException
    mod.InternalServerException = models_mod.InternalServerException
    # Inject standard library items
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f  # no-op decorator
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    return mod


class TestRekognitionIntegration:

    @pytest.fixture
    def store(self):
        return RekognitionStore()

    # ── Collection Tests ──

    def test_create_collection_happy_path(self, store):
        handler = _load_handler('CreateCollection')
        response = handler(store, {"CollectionId": "test-coll"})
        assert response is not None
        assert "CollectionArn" in response or response.get("StatusCode") == 200
        assert "test-coll" in store.collections

    def test_create_collection_duplicate(self, store):
        handler = _load_handler('CreateCollection')
        handler(store, {"CollectionId": "test-coll"})
        with pytest.raises(ResourceInUseException):
            handler(store, {"CollectionId": "test-coll"})

    def test_describe_collection(self, store):
        create = _load_handler('CreateCollection')
        desc = _load_handler('DescribeCollection')
        create(store, {"CollectionId": "test-coll"})
        response = desc(store, {"CollectionId": "test-coll"})
        assert response is not None
        assert response.get("CollectionId") == "test-coll" or "CollectionId" in str(response)

    def test_describe_nonexistent_collection(self, store):
        desc = _load_handler('DescribeCollection')
        with pytest.raises(ResourceNotFoundException):
            desc(store, {"CollectionId": "nonexistent"})

    def test_list_collections(self, store):
        create = _load_handler('CreateCollection')
        list_coll = _load_handler('ListCollections')
        create(store, {"CollectionId": "coll-a"})
        create(store, {"CollectionId": "coll-b"})
        response = list_coll(store, {})
        assert response is not None
        ids = response.get("CollectionIds", [])
        assert len(ids) >= 2

    def test_delete_collection(self, store):
        create = _load_handler('CreateCollection')
        delete = _load_handler('DeleteCollection')
        desc = _load_handler('DescribeCollection')
        create(store, {"CollectionId": "test-coll"})
        response = delete(store, {"CollectionId": "test-coll"})
        assert response.get("StatusCode") == 200
        with pytest.raises(ResourceNotFoundException):
            desc(store, {"CollectionId": "test-coll"})

    # ── Face Tests ──

    def test_index_faces(self, store):
        create = _load_handler('CreateCollection')
        index = _load_handler('IndexFaces')
        create(store, {"CollectionId": "test-coll"})
        response = index(store, {"CollectionId": "test-coll", "Image": {"Bytes": "data"}})
        assert response is not None
        assert len(response.get("FaceRecords", [])) >= 1
        assert len(store.collection_faces.get("test-coll", set())) >= 1

    def test_index_faces_nonexistent_collection(self, store):
        index = _load_handler('IndexFaces')
        with pytest.raises(ResourceNotFoundException):
            index(store, {"CollectionId": "nonexistent", "Image": {"Bytes": "data"}})

    def test_list_faces(self, store):
        create = _load_handler('CreateCollection')
        index = _load_handler('IndexFaces')
        list_faces = _load_handler('ListFaces')
        create(store, {"CollectionId": "test-coll"})
        index(store, {"CollectionId": "test-coll", "Image": {"Bytes": "data"}})
        response = list_faces(store, {"CollectionId": "test-coll"})
        assert response is not None
        assert len(response.get("Faces", [])) >= 1

    def test_delete_faces(self, store):
        create = _load_handler('CreateCollection')
        index = _load_handler('IndexFaces')
        delete_faces = _load_handler('DeleteFaces')
        create(store, {"CollectionId": "test-coll"})
        resp = index(store, {"CollectionId": "test-coll", "Image": {"Bytes": "data"}})
        face_id = resp["FaceRecords"][0]["Face"]["FaceId"]
        response = delete_faces(store, {"CollectionId": "test-coll", "FaceIds": [face_id]})
        assert face_id in response.get("DeletedFaces", [])

    def test_search_faces(self, store):
        create = _load_handler('CreateCollection')
        index = _load_handler('IndexFaces')
        search = _load_handler('SearchFaces')
        create(store, {"CollectionId": "test-coll"})
        resp = index(store, {"CollectionId": "test-coll", "Image": {"Bytes": "data"}})
        face_id = resp["FaceRecords"][0]["Face"]["FaceId"]
        response = search(store, {"CollectionId": "test-coll", "FaceId": face_id})
        assert response is not None
        assert "FaceMatches" in response or "SearchedFaceId" in response

    # ── Detection Tests ──

    def test_detect_faces(self, store):
        handler = _load_handler('DetectFaces')
        response = handler(store, {"Image": {"Bytes": "data"}})
        assert response is not None
        assert "FaceDetails" in response

    def test_detect_labels(self, store):
        handler = _load_handler('DetectLabels')
        response = handler(store, {"Image": {"Bytes": "data"}})
        assert response is not None
        assert "Labels" in response

    def test_recognize_celebrities(self, store):
        handler = _load_handler('RecognizeCelebrities')
        response = handler(store, {"Image": {"Bytes": "data"}})
        assert response is not None
        assert "CelebrityFaces" in response

    # ── Async Video Tests ──

    def test_start_face_detection(self, store):
        handler = _load_handler('StartFaceDetection')
        response = handler(store, {"Video": {"S3Object": {"Bucket": "b", "Name": "v.mp4"}}})
        assert response is not None
        assert "JobId" in response
        assert response["JobId"] in store.video_jobs

    def test_get_face_detection(self, store):
        start = _load_handler('StartFaceDetection')
        get = _load_handler('GetFaceDetection')
        resp = start(store, {"Video": {"S3Object": {"Bucket": "b", "Name": "v.mp4"}}})
        job_id = resp["JobId"]
        response = get(store, {"JobId": job_id})
        assert response is not None
        assert response.get("JobStatus") == "SUCCEEDED"

    def test_get_nonexistent_job(self, store):
        handler = _load_handler('GetFaceDetection')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {"JobId": "nonexistent"})

    # ── Celebrity Tests ──

    def test_get_celebrity_info(self, store):
        handler = _load_handler('GetCelebrityInfo')
        response = handler(store, {"Id": "celebrity-1"})
        assert response is not None
        assert "Name" in response

    def test_get_celebrity_info_nonexistent(self, store):
        handler = _load_handler('GetCelebrityInfo')
        with pytest.raises(ResourceNotFoundException):
            handler(store, {"Id": "nonexistent"})

    # ── Tag Tests ──

    def test_tag_resource(self, store):
        handler = _load_handler('TagResource')
        arn = "arn:aws:rekognition:us-east-1:123456789012:collection/test"
        response = handler(store, {"ResourceArn": arn, "Tags": {"Env": "test"}})
        assert response is not None
        assert store.tags.get(arn, {}).get("Env") == "test"

    def test_list_tags_for_resource(self, store):
        tag = _load_handler('TagResource')
        list_tags = _load_handler('ListTagsForResource')
        arn = "arn:aws:rekognition:us-east-1:123456789012:collection/test"
        tag(store, {"ResourceArn": arn, "Tags": {"Env": "test"}})
        response = list_tags(store, {"ResourceArn": arn})
        assert response.get("Tags", {}).get("Env") == "test"

    def test_untag_resource(self, store):
        tag = _load_handler('TagResource')
        untag = _load_handler('UntagResource')
        list_tags = _load_handler('ListTagsForResource')
        arn = "arn:aws:rekognition:us-east-1:123456789012:collection/test"
        tag(store, {"ResourceArn": arn, "Tags": {"Env": "test"}})
        untag(store, {"ResourceArn": arn, "TagKeys": ["Env"]})
        response = list_tags(store, {"ResourceArn": arn})
        assert response.get("Tags", {}).get("Env") is None
