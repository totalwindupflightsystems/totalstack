"""Integration test for Transcribe — real LocalStack store."""
import pytest
import os
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'transcribe')

models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

TranscribeStore = models_mod.TranscribeStore
BadRequestException = models_mod.BadRequestException
NotFoundException = models_mod.NotFoundException
ConflictException = models_mod.ConflictException
LimitExceededException = models_mod.LimitExceededException
InternalFailureException = models_mod.InternalFailureException
VocabularyRecord = models_mod.VocabularyRecord
VocabularyFilterRecord = models_mod.VocabularyFilterRecord
TranscriptionJobRecord = models_mod.TranscriptionJobRecord
LanguageModelRecord = models_mod.LanguageModelRecord


def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.BadRequestException = BadRequestException
    mod.NotFoundException = NotFoundException
    mod.ConflictException = ConflictException
    mod.LimitExceededException = LimitExceededException
    mod.InternalFailureException = InternalFailureException
    mod.VocabularyRecord = VocabularyRecord
    mod.VocabularyFilterRecord = VocabularyFilterRecord
    mod.TranscriptionJobRecord = TranscriptionJobRecord
    mod.LanguageModelRecord = LanguageModelRecord
    spec.loader.exec_module(mod)
    skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


class TestVocabularyIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = TranscribeStore()
        return self._store

    def test_create_vocabulary_happy(self):
        handler = _load_handler('create-vocabulary')
        resp = handler(self.store, {
            "VocabularyName": "test-vocab",
            "LanguageCode": "en-US",
        })
        assert resp["VocabularyName"] == "test-vocab"
        assert resp["VocabularyState"] == "READY"

    def test_create_vocabulary_duplicate(self):
        handler = _load_handler('create-vocabulary')
        handler(self.store, {
            "VocabularyName": "dup-vocab",
            "LanguageCode": "en-US",
        })
        with pytest.raises(ConflictException):
            handler(self.store, {
                "VocabularyName": "dup-vocab",
                "LanguageCode": "en-US",
            })

    def test_get_vocabulary_happy(self):
        create = _load_handler('create-vocabulary')
        create(self.store, {"VocabularyName": "get-me", "LanguageCode": "en-US"})
        handler = _load_handler('get-vocabulary')
        resp = handler(self.store, {"VocabularyName": "get-me"})
        assert resp["VocabularyName"] == "get-me"

    def test_get_vocabulary_nonexistent(self):
        handler = _load_handler('get-vocabulary')
        with pytest.raises(NotFoundException):
            handler(self.store, {"VocabularyName": "nonexistent"})

    def test_update_vocabulary(self):
        create = _load_handler('create-vocabulary')
        create(self.store, {"VocabularyName": "update-me", "LanguageCode": "en-US"})
        handler = _load_handler('update-vocabulary')
        resp = handler(self.store, {
            "VocabularyName": "update-me",
            "LanguageCode": "en-GB",
        })
        assert resp["LanguageCode"] == "en-GB"

    def test_list_vocabularies(self):
        create = _load_handler('create-vocabulary')
        create(self.store, {"VocabularyName": "l1", "LanguageCode": "en-US"})
        create(self.store, {"VocabularyName": "l2", "LanguageCode": "es-ES"})
        handler = _load_handler('list-vocabularies')
        resp = handler(self.store, {})
        assert len(resp["Vocabularies"]) == 2

    def test_delete_vocabulary(self):
        create = _load_handler('create-vocabulary')
        create(self.store, {"VocabularyName": "to-delete", "LanguageCode": "en-US"})
        handler = _load_handler('delete-vocabulary')
        resp = handler(self.store, {"VocabularyName": "to-delete"})
        assert resp == {}

    def test_delete_vocabulary_nonexistent(self):
        handler = _load_handler('delete-vocabulary')
        with pytest.raises(NotFoundException):
            handler(self.store, {"VocabularyName": "nonexistent"})


class TestVocabularyFilterIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = TranscribeStore()
        return self._store

    def test_create_filter_happy(self):
        handler = _load_handler('create-vocabulary-filter')
        resp = handler(self.store, {
            "VocabularyFilterName": "test-filter",
            "LanguageCode": "en-US",
            "Words": ["badword1", "badword2"],
        })
        assert resp["VocabularyFilterName"] == "test-filter"

    def test_create_filter_duplicate(self):
        handler = _load_handler('create-vocabulary-filter')
        handler(self.store, {
            "VocabularyFilterName": "dup-filter",
            "LanguageCode": "en-US",
        })
        with pytest.raises(ConflictException):
            handler(self.store, {
                "VocabularyFilterName": "dup-filter",
                "LanguageCode": "en-US",
            })

    def test_get_filter_happy(self):
        create = _load_handler('create-vocabulary-filter')
        create(self.store, {"VocabularyFilterName": "gf", "LanguageCode": "en-US"})
        handler = _load_handler('get-vocabulary-filter')
        resp = handler(self.store, {"VocabularyFilterName": "gf"})
        assert resp["VocabularyFilterName"] == "gf"

    def test_get_filter_nonexistent(self):
        handler = _load_handler('get-vocabulary-filter')
        with pytest.raises(NotFoundException):
            handler(self.store, {"VocabularyFilterName": "nonexistent"})

    def test_update_filter(self):
        create = _load_handler('create-vocabulary-filter')
        create(self.store, {"VocabularyFilterName": "uf", "LanguageCode": "en-US"})
        handler = _load_handler('update-vocabulary-filter')
        resp = handler(self.store, {
            "VocabularyFilterName": "uf",
            "Words": ["updated"],
        })
        assert resp["Words"] == ["updated"]

    def test_list_filters(self):
        create = _load_handler('create-vocabulary-filter')
        create(self.store, {"VocabularyFilterName": "f1", "LanguageCode": "en-US"})
        create(self.store, {"VocabularyFilterName": "f2", "LanguageCode": "en-US"})
        handler = _load_handler('list-vocabulary-filters')
        resp = handler(self.store, {})
        assert len(resp["VocabularyFilters"]) == 2

    def test_delete_filter(self):
        create = _load_handler('create-vocabulary-filter')
        create(self.store, {"VocabularyFilterName": "tdf", "LanguageCode": "en-US"})
        handler = _load_handler('delete-vocabulary-filter')
        resp = handler(self.store, {"VocabularyFilterName": "tdf"})
        assert resp == {}


class TestTranscriptionJobIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = TranscribeStore()
        return self._store

    def test_start_job_happy(self):
        handler = _load_handler('start-transcription-job')
        resp = handler(self.store, {
            "TranscriptionJobName": "test-job",
            "Media": {"MediaFileUri": "s3://bucket/audio.mp3"},
        })
        job = resp["TranscriptionJob"]
        assert job["TranscriptionJobName"] == "test-job"
        assert job["TranscriptionJobStatus"] == "COMPLETED"

    def test_start_job_duplicate(self):
        handler = _load_handler('start-transcription-job')
        handler(self.store, {
            "TranscriptionJobName": "dup-job",
            "Media": {"MediaFileUri": "s3://bucket/a.mp3"},
        })
        with pytest.raises(ConflictException):
            handler(self.store, {
                "TranscriptionJobName": "dup-job",
                "Media": {"MediaFileUri": "s3://bucket/b.mp3"},
            })

    def test_get_job_happy(self):
        start = _load_handler('start-transcription-job')
        start(self.store, {
            "TranscriptionJobName": "gj",
            "Media": {"MediaFileUri": "s3://bucket/x.mp3"},
        })
        handler = _load_handler('get-transcription-job')
        resp = handler(self.store, {"TranscriptionJobName": "gj"})
        assert resp["TranscriptionJob"]["TranscriptionJobName"] == "gj"

    def test_get_job_nonexistent(self):
        handler = _load_handler('get-transcription-job')
        with pytest.raises(NotFoundException):
            handler(self.store, {"TranscriptionJobName": "nonexistent"})

    def test_list_jobs(self):
        start = _load_handler('start-transcription-job')
        start(self.store, {
            "TranscriptionJobName": "j1",
            "Media": {"MediaFileUri": "s3://bucket/a.mp3"},
        })
        start(self.store, {
            "TranscriptionJobName": "j2",
            "Media": {"MediaFileUri": "s3://bucket/b.mp3"},
        })
        handler = _load_handler('list-transcription-jobs')
        resp = handler(self.store, {})
        assert len(resp["TranscriptionJobs"]) == 2

    def test_delete_job(self):
        start = _load_handler('start-transcription-job')
        start(self.store, {
            "TranscriptionJobName": "tdj",
            "Media": {"MediaFileUri": "s3://bucket/x.mp3"},
        })
        handler = _load_handler('delete-transcription-job')
        resp = handler(self.store, {"TranscriptionJobName": "tdj"})
        assert resp == {}


class TestLanguageModelIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = TranscribeStore()
        return self._store

    def test_create_model_happy(self):
        handler = _load_handler('create-language-model')
        resp = handler(self.store, {
            "LanguageCode": "en-US",
            "BaseModelName": "NarrowBand",
            "ModelName": "test-model",
            "InputDataConfig": {
                "S3Uri": "s3://bucket/train/",
                "TuningDataS3Uri": "s3://bucket/tune/",
                "DataAccessRoleArn": "arn:aws:iam::123456789012:role/TranscribeRole",
            },
        })
        assert resp["ModelName"] == "test-model"
        assert resp["ModelStatus"] == "COMPLETED"

    def test_create_model_duplicate(self):
        handler = _load_handler('create-language-model')
        handler(self.store, {
            "LanguageCode": "en-US",
            "BaseModelName": "NarrowBand",
            "ModelName": "dup-model",
            "InputDataConfig": {"S3Uri": "s3://bucket/train/"},
        })
        with pytest.raises(ConflictException):
            handler(self.store, {
                "LanguageCode": "en-US",
                "BaseModelName": "NarrowBand",
                "ModelName": "dup-model",
                "InputDataConfig": {"S3Uri": "s3://bucket/train/"},
            })

    def test_describe_model_happy(self):
        create = _load_handler('create-language-model')
        create(self.store, {
            "LanguageCode": "en-US",
            "BaseModelName": "NarrowBand",
            "ModelName": "dm",
            "InputDataConfig": {"S3Uri": "s3://bucket/train/"},
        })
        handler = _load_handler('describe-language-model')
        resp = handler(self.store, {"ModelName": "dm"})
        assert resp["ModelName"] == "dm"

    def test_describe_model_nonexistent(self):
        handler = _load_handler('describe-language-model')
        with pytest.raises(NotFoundException):
            handler(self.store, {"ModelName": "nonexistent"})

    def test_list_models(self):
        create = _load_handler('create-language-model')
        create(self.store, {
            "LanguageCode": "en-US",
            "BaseModelName": "NarrowBand",
            "ModelName": "m1",
            "InputDataConfig": {"S3Uri": "s3://bucket/train/"},
        })
        create(self.store, {
            "LanguageCode": "en-US",
            "BaseModelName": "NarrowBand",
            "ModelName": "m2",
            "InputDataConfig": {"S3Uri": "s3://bucket/train/"},
        })
        handler = _load_handler('list-language-models')
        resp = handler(self.store, {})
        assert len(resp["Models"]) == 2

    def test_delete_model(self):
        create = _load_handler('create-language-model')
        create(self.store, {
            "LanguageCode": "en-US",
            "BaseModelName": "NarrowBand",
            "ModelName": "tdm",
            "InputDataConfig": {"S3Uri": "s3://bucket/train/"},
        })
        handler = _load_handler('delete-language-model')
        resp = handler(self.store, {"ModelName": "tdm"})
        assert resp == {}
