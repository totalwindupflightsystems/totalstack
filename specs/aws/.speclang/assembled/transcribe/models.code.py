"""Transcribe service — speech-to-text. Stores vocabularies, filters, transcription jobs, and language models."""
import time


class TranscribeException(Exception):
    code = "InternalFailureException"
    def __init__(self, message=None):
        super().__init__(message or self.code)
        self.message = message or self.code


class BadRequestException(TranscribeException):
    code = "BadRequestException"

class LimitExceededException(TranscribeException):
    code = "LimitExceededException"

class InternalFailureException(TranscribeException):
    code = "InternalFailureException"

class NotFoundException(TranscribeException):
    code = "NotFoundException"

class ConflictException(TranscribeException):
    code = "ConflictException"


# ── Record classes ─────────────────────────────────────────────────

class VocabularyRecord:
    def __init__(self, VocabularyName, LanguageCode,
                 Phrases=None, VocabularyFileUri=None,
                 DataAccessRoleArn=None, Tags=None):
        self.VocabularyName = VocabularyName
        self.LanguageCode = LanguageCode
        self.Phrases = Phrases or []
        self.VocabularyFileUri = VocabularyFileUri or ""
        self.DataAccessRoleArn = DataAccessRoleArn or ""
        self.VocabularyState = "READY"
        self.LastModifiedTime = time.time()
        self.FailureReason = ""
        self.Tags = Tags or []

    def to_dict(self):
        return {
            "VocabularyName": self.VocabularyName,
            "LanguageCode": self.LanguageCode,
            "VocabularyState": self.VocabularyState,
            "LastModifiedTime": self.LastModifiedTime,
            "FailureReason": self.FailureReason,
        }


class VocabularyFilterRecord:
    def __init__(self, VocabularyFilterName, LanguageCode,
                 Words=None, VocabularyFilterFileUri=None,
                 DataAccessRoleArn=None, Tags=None):
        self.VocabularyFilterName = VocabularyFilterName
        self.LanguageCode = LanguageCode
        self.Words = Words or []
        self.VocabularyFilterFileUri = VocabularyFilterFileUri or ""
        self.DataAccessRoleArn = DataAccessRoleArn or ""
        self.LastModifiedTime = time.time()
        self.Tags = Tags or []

    def to_dict(self):
        return {
            "VocabularyFilterName": self.VocabularyFilterName,
            "LanguageCode": self.LanguageCode,
            "LastModifiedTime": self.LastModifiedTime,
            "Words": self.Words,
        }


class TranscriptionJobRecord:
    def __init__(self, TranscriptionJobName, LanguageCode=None,
                 Media=None, OutputBucketName=None, OutputKey=None,
                 MediaFormat=None, MediaSampleRateHertz=None,
                 Settings=None, Tags=None, **kwargs):
        self.TranscriptionJobName = TranscriptionJobName
        self.LanguageCode = LanguageCode or "en-US"
        self.Media = Media or {}
        self.OutputBucketName = OutputBucketName or ""
        self.OutputKey = OutputKey or ""
        self.MediaFormat = MediaFormat or "mp3"
        self.MediaSampleRateHertz = MediaSampleRateHertz or 44100
        self.TranscriptionJobStatus = "COMPLETED"
        self.CreationTime = time.time()
        self.CompletionTime = time.time()
        self.Tags = Tags or []

    def to_dict(self):
        return {
            "TranscriptionJobName": self.TranscriptionJobName,
            "TranscriptionJobStatus": self.TranscriptionJobStatus,
            "LanguageCode": self.LanguageCode,
            "MediaFormat": self.MediaFormat,
            "Media": self.Media,
            "CreationTime": self.CreationTime,
            "CompletionTime": self.CompletionTime,
            "MediaSampleRateHertz": self.MediaSampleRateHertz,
        }


class LanguageModelRecord:
    def __init__(self, ModelName, LanguageCode, BaseModelName,
                 InputDataConfig, Tags=None):
        self.ModelName = ModelName
        self.LanguageCode = LanguageCode
        self.BaseModelName = BaseModelName
        self.InputDataConfig = InputDataConfig
        self.ModelStatus = "COMPLETED"
        self.CreationTime = time.time()
        self.LastModifiedTime = time.time()
        self.Tags = Tags or []

    def to_dict(self):
        return {
            "ModelName": self.ModelName,
            "LanguageCode": self.LanguageCode,
            "BaseModelName": self.BaseModelName,
            "ModelStatus": self.ModelStatus,
            "InputDataConfig": self.InputDataConfig,
            "CreationTime": self.CreationTime,
            "LastModifiedTime": self.LastModifiedTime,
        }


# ── Store class ────────────────────────────────────────────────────

class TranscribeStore:
    def __init__(self):
        self._vocabularies = {}
        self._vocabulary_filters = {}
        self._transcription_jobs = {}
        self._language_models = {}

    # ── Vocabulary ────────────────────────────────────────────────

    def vocabularies(self, name=None):
        if name is not None:
            return self._vocabularies.get(name)
        return list(self._vocabularies.values())

    def create_vocabulary(self, VocabularyName, LanguageCode, **kwargs):
        if VocabularyName in self._vocabularies:
            raise ConflictException(f"Vocabulary '{VocabularyName}' already exists")
        record = VocabularyRecord(VocabularyName=VocabularyName, LanguageCode=LanguageCode, **kwargs)
        self._vocabularies[VocabularyName] = record
        return record.to_dict()

    def get_vocabulary(self, VocabularyName):
        r = self._vocabularies.get(VocabularyName)
        if r is None:
            raise NotFoundException(f"Vocabulary '{VocabularyName}' not found")
        return r.to_dict()

    def update_vocabulary(self, VocabularyName, LanguageCode, **kwargs):
        r = self._vocabularies.get(VocabularyName)
        if r is None:
            raise NotFoundException(f"Vocabulary '{VocabularyName}' not found")
        r.LanguageCode = LanguageCode
        for k, v in kwargs.items():
            if hasattr(r, k):
                setattr(r, k, v)
        r.LastModifiedTime = time.time()
        return r.to_dict()

    def delete_vocabulary(self, VocabularyName):
        if VocabularyName not in self._vocabularies:
            raise NotFoundException(f"Vocabulary '{VocabularyName}' not found")
        del self._vocabularies[VocabularyName]
        return {}

    def list_vocabularies(self, NextToken=None, MaxResults=None,
                          StateEquals=None, NameContains=None):
        items = list(self._vocabularies.values())
        if StateEquals:
            items = [i for i in items if i.VocabularyState == StateEquals]
        if NameContains:
            items = [i for i in items if NameContains in i.VocabularyName]
        return {"Vocabularies": [i.to_dict() for i in items], "NextToken": None}

    # ── VocabularyFilter ──────────────────────────────────────────

    def vocabulary_filters(self, name=None):
        if name is not None:
            return self._vocabulary_filters.get(name)
        return list(self._vocabulary_filters.values())

    def create_vocabulary_filter(self, VocabularyFilterName, LanguageCode, **kwargs):
        if VocabularyFilterName in self._vocabulary_filters:
            raise ConflictException(f"Filter '{VocabularyFilterName}' already exists")
        record = VocabularyFilterRecord(VocabularyFilterName=VocabularyFilterName,
                                        LanguageCode=LanguageCode, **kwargs)
        self._vocabulary_filters[VocabularyFilterName] = record
        return record.to_dict()

    def get_vocabulary_filter(self, VocabularyFilterName):
        r = self._vocabulary_filters.get(VocabularyFilterName)
        if r is None:
            raise NotFoundException(f"Filter '{VocabularyFilterName}' not found")
        return r.to_dict()

    def update_vocabulary_filter(self, VocabularyFilterName, **kwargs):
        r = self._vocabulary_filters.get(VocabularyFilterName)
        if r is None:
            raise NotFoundException(f"Filter '{VocabularyFilterName}' not found")
        for k, v in kwargs.items():
            if hasattr(r, k):
                setattr(r, k, v)
        r.LastModifiedTime = time.time()
        return r.to_dict()

    def delete_vocabulary_filter(self, VocabularyFilterName):
        if VocabularyFilterName not in self._vocabulary_filters:
            raise NotFoundException(f"Filter '{VocabularyFilterName}' not found")
        del self._vocabulary_filters[VocabularyFilterName]
        return {}

    def list_vocabulary_filters(self, NextToken=None, MaxResults=None,
                                NameContains=None):
        items = list(self._vocabulary_filters.values())
        if NameContains:
            items = [i for i in items if NameContains in i.VocabularyFilterName]
        return {"VocabularyFilters": [i.to_dict() for i in items], "NextToken": None}

    # ── TranscriptionJob ──────────────────────────────────────────

    def transcription_jobs(self, name=None):
        if name is not None:
            return self._transcription_jobs.get(name)
        return list(self._transcription_jobs.values())

    def start_transcription_job(self, TranscriptionJobName, Media,
                                LanguageCode=None, **kwargs):
        if TranscriptionJobName in self._transcription_jobs:
            raise ConflictException(f"Job '{TranscriptionJobName}' already exists")
        record = TranscriptionJobRecord(
            TranscriptionJobName=TranscriptionJobName,
            LanguageCode=LanguageCode,
            Media=Media,
            **{k: v for k, v in kwargs.items()
               if k in ("OutputBucketName", "OutputKey", "MediaFormat",
                        "MediaSampleRateHertz", "Settings", "Tags")})
        self._transcription_jobs[TranscriptionJobName] = record
        return {"TranscriptionJob": record.to_dict()}

    def get_transcription_job(self, TranscriptionJobName):
        r = self._transcription_jobs.get(TranscriptionJobName)
        if r is None:
            raise NotFoundException(f"Job '{TranscriptionJobName}' not found")
        return {"TranscriptionJob": r.to_dict()}

    def list_transcription_jobs(self, Status=None, JobNameContains=None,
                                NextToken=None, MaxResults=None):
        items = list(self._transcription_jobs.values())
        if Status:
            items = [i for i in items if i.TranscriptionJobStatus == Status]
        if JobNameContains:
            items = [i for i in items if JobNameContains in i.TranscriptionJobName]
        return {"TranscriptionJobs": [i.to_dict() for i in items], "NextToken": None}

    def delete_transcription_job(self, TranscriptionJobName):
        if TranscriptionJobName in self._transcription_jobs:
            del self._transcription_jobs[TranscriptionJobName]
        return {}

    # ── LanguageModel ─────────────────────────────────────────────

    def language_models(self, name=None):
        if name is not None:
            return self._language_models.get(name)
        return list(self._language_models.values())

    def create_language_model(self, LanguageCode, BaseModelName, ModelName,
                              InputDataConfig, Tags=None):
        if ModelName in self._language_models:
            raise ConflictException(f"Model '{ModelName}' already exists")
        record = LanguageModelRecord(
            LanguageCode=LanguageCode, BaseModelName=BaseModelName,
            ModelName=ModelName, InputDataConfig=InputDataConfig, Tags=Tags)
        self._language_models[ModelName] = record
        return record.to_dict()

    def describe_language_model(self, ModelName):
        r = self._language_models.get(ModelName)
        if r is None:
            raise NotFoundException(f"Model '{ModelName}' not found")
        return r.to_dict()

    def list_language_models(self, StatusEquals=None, NameContains=None,
                             NextToken=None, MaxResults=None):
        items = list(self._language_models.values())
        if StatusEquals:
            items = [i for i in items if i.ModelStatus == StatusEquals]
        if NameContains:
            items = [i for i in items if NameContains in i.ModelName]
        return {"Models": [i.to_dict() for i in items], "NextToken": None}

    def delete_language_model(self, ModelName):
        if ModelName in self._language_models:
            del self._language_models[ModelName]
        return {}
