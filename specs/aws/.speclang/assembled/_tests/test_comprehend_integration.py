"""Integration tests for Comprehend — stateless inference + 5 entities + tags."""
import pytest
import os
import importlib.util
import types
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'comprehend')

def _load_models():
    path = os.path.join(SERVICE_DIR, 'models.code.py')
    sp = importlib.util.spec_from_file_location('comp_models', path)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m

_models = _load_models()
ComprehendStore = _models.ComprehendStore
NotFoundException = _models.NotFoundException
InvalidRequestException = _models.InvalidRequestException

sn = {'dataclass', 'time', 'uuid', '<lambda>'}

def _load_handler(name):
    path = os.path.join(SERVICE_DIR, name + '.code.py')
    sp = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(sp)
    m.NotFoundException = NotFoundException
    m.InvalidRequestException = InvalidRequestException
    m.ResourceInUseException = _models.ResourceInUseException
    m.TooManyTagsException = _models.TooManyTagsException
    m.time = _time
    m.uuid = _uuid
    m.dataclass = lambda f: f
    sp.loader.exec_module(m)
    for v in m.__dict__.values():
        if isinstance(v, types.FunctionType) and not v.__name__.startswith('_') and v.__name__ not in sn:
            return v
    return None


class TestStatelessInference:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = ComprehendStore()
        return self._store

    def test_detect_sentiment(self):
        h = _load_handler('detect-sentiment')
        r = h(self.store, {"Text": "I love AWS"})
        assert r["Sentiment"] in ("NEUTRAL", "POSITIVE", "NEGATIVE", "MIXED")

    def test_detect_entities(self):
        h = _load_handler('detect-entities')
        r = h(self.store, {"Text": "AWS is great"})
        assert "Entities" in r

    def test_detect_key_phrases(self):
        h = _load_handler('detect-key-phrases')
        r = h(self.store, {"Text": "AWS is a cloud provider"})
        assert "KeyPhrases" in r

    def test_detect_dominant_language(self):
        h = _load_handler('detect-dominant-language')
        r = h(self.store, {"Text": "Hello world"})
        assert "Languages" in r

    def test_detect_syntax(self):
        h = _load_handler('detect-syntax')
        r = h(self.store, {"Text": "AWS is great"})
        assert "SyntaxTokens" in r

    def test_detect_pii_entities(self):
        h = _load_handler('detect-pii-entities')
        r = h(self.store, {"Text": "My name is John"})
        assert "Entities" in r

    def test_classify_document(self):
        h = _load_handler('classify-document')
        r = h(self.store, {"Text": "doc text", "EndpointArn": "arn:aws:comprehend:us-east-1:000000000000:endpoint/ep1"})
        assert "Classes" in r


class TestEntityManagement:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = ComprehendStore()
        return self._store

    def test_create_and_describe_classifier(self):
        create = _load_handler('create-document-classifier')
        describe = _load_handler('describe-document-classifier')
        arn = "arn:aws:comprehend:us-east-1:000000000000:document-classifier/clf1"
        create(self.store, {"DocumentClassifierArn": arn, "DocumentClassifierName": "clf1"})
        r = describe(self.store, {"DocumentClassifierArn": arn})
        assert r["EntityRecognizerArn"] == arn

    def test_list_classifiers(self):
        h = _load_handler('list-document-classifiers')
        r = h(self.store, {})
        assert "DocumentClassifierPropertiesList" in r

    def test_delete_classifier(self):
        create = _load_handler('create-document-classifier')
        delete = _load_handler('delete-document-classifier')
        describe = _load_handler('describe-document-classifier')
        arn = "arn:aws:comprehend:us-east-1:000000000000:document-classifier/del-clf"
        create(self.store, {"DocumentClassifierArn": arn})
        delete(self.store, {"DocumentClassifierArn": arn})
        with pytest.raises(NotFoundException):
            describe(self.store, {"DocumentClassifierArn": arn})

    def test_create_and_describe_recognizer(self):
        create = _load_handler('create-entity-recognizer')
        describe = _load_handler('describe-entity-recognizer')
        arn = "arn:aws:comprehend:us-east-1:000000000000:entity-recognizer/er1"
        create(self.store, {"EntityRecognizerArn": arn, "RecognizerName": "er1"})
        r = describe(self.store, {"EntityRecognizerArn": arn})
        assert r["EntityRecognizerArn"] == arn


class TestTagsIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = ComprehendStore()
            create = _load_handler('create-endpoint')
            self._arn = "arn:aws:comprehend:us-east-1:000000000000:endpoint/tag-ep"
            create(self._store, {"EndpointArn": self._arn, "EndpointName": "tag-ep"})
        return self._store

    @property
    def arn(self):
        return self._arn

    def test_tag_resource(self):
        tag = _load_handler('tag-resource')
        lt = _load_handler('list-tags-for-resource')
        tag(self.store, {"ResourceArn": self.arn, "Tags": [{"Key": "env", "Value": "test"}]})
        r = lt(self.store, {"ResourceArn": self.arn})
        assert {"Key": "env", "Value": "test"} in r["Tags"]

    def test_untag_resource(self):
        untag = _load_handler('untag-resource')
        lt = _load_handler('list-tags-for-resource')
        untag(self.store, {"ResourceArn": self.arn, "TagKeys": ["env"]})
        r = lt(self.store, {"ResourceArn": self.arn})
        assert not any(t["Key"] == "env" for t in r["Tags"])
