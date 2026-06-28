"""Polly service — text-to-speech. Stores lexicons and synthesis tasks.

Entities:
- Lexicon: pronunciation dictionary (name → content + attributes)
- SpeechSynthesisTask: async speech generation (task_id → task details)
"""
import uuid
import time


# ── Exception classes ──────────────────────────────────────────────

class PollyException(Exception):
    """Base exception for Polly service."""
    code = "ServiceFailureException"
    status_code = 500

    def __init__(self, message=None):
        super().__init__(message or self.__class__.code)
        self.message = message or self.__class__.code


class InvalidLexiconException(PollyException):
    code = "InvalidLexiconException"
    status_code = 400


class LexiconNotFoundException(PollyException):
    code = "LexiconNotFoundException"
    status_code = 404


class MaxLexiconsNumberExceededException(PollyException):
    code = "MaxLexiconsNumberExceededException"
    status_code = 400


class ServiceFailureException(PollyException):
    code = "ServiceFailureException"
    status_code = 500


class InvalidNextTokenException(PollyException):
    code = "InvalidNextTokenException"
    status_code = 400


class SynthesisTaskNotFoundException(PollyException):
    code = "SynthesisTaskNotFoundException"
    status_code = 404


class InvalidTaskIdException(PollyException):
    code = "InvalidTaskIdException"
    status_code = 400


class TextLengthExceededException(PollyException):
    code = "TextLengthExceededException"
    status_code = 400


class InvalidSsmlException(PollyException):
    code = "InvalidSsmlException"
    status_code = 400


class LexiconSizeExceededException(PollyException):
    code = "LexiconSizeExceededException"
    status_code = 400


class UnsupportedPlsAlphabetException(PollyException):
    code = "UnsupportedPlsAlphabetException"
    status_code = 400


class UnsupportedPlsLanguageException(PollyException):
    code = "UnsupportedPlsLanguageException"
    status_code = 400


class MaxLexemeLengthExceededException(PollyException):
    code = "MaxLexemeLengthExceededException"
    status_code = 400


class InvalidSampleRateException(PollyException):
    code = "InvalidSampleRateException"
    status_code = 400


class LanguageNotSupportedException(PollyException):
    code = "LanguageNotSupportedException"
    status_code = 400


class EngineNotSupportedException(PollyException):
    code = "EngineNotSupportedException"
    status_code = 400


class MarksNotSupportedForFormatException(PollyException):
    code = "MarksNotSupportedForFormatException"
    status_code = 400


class SsmlMarksNotSupportedForTextTypeException(PollyException):
    code = "SsmlMarksNotSupportedForTextTypeException"
    status_code = 400


class InvalidS3BucketException(PollyException):
    code = "InvalidS3BucketException"
    status_code = 400


class InvalidS3KeyException(PollyException):
    code = "InvalidS3KeyException"
    status_code = 400


class InvalidSnsTopicArnException(PollyException):
    code = "InvalidSnsTopicArnException"
    status_code = 400


MAX_LEXICONS = 100


# ── Record classes ─────────────────────────────────────────────────

class LexiconRecord:
    """Stored lexicon entry."""
    def __init__(self, Name, Content, LexiconArn=None):
        self.Name = Name
        self.Content = Content
        self.LexiconArn = LexiconArn
        self.Alphabet = "ipa"
        self.LanguageCode = "en-US"
        self.LexemesCount = 0
        self.Size = len(Content)
        self.LastModified = time.time()
        self.LexiconArn = LexiconArn or f"arn:aws:polly:us-east-1:000000000000:lexicon/{Name}"

    def to_dict(self):
        return {
            "Name": self.Name,
            "Content": self.Content,
            "LexiconArn": self.LexiconArn,
        }

    def to_attributes(self):
        return {
            "Alphabet": self.Alphabet,
            "LanguageCode": self.LanguageCode,
            "LastModified": self.LastModified,
            "LexemesCount": self.LexemesCount,
            "LexiconArn": self.LexiconArn,
            "Size": self.Size,
        }


class SynthesisTaskRecord:
    """Stored speech synthesis task."""
    def __init__(self, TaskId, OutputFormat, OutputS3BucketName, Text, VoiceId,
                 Engine=None, LanguageCode=None, LexiconNames=None,
                 OutputS3KeyPrefix=None, SampleRate=None, SnsTopicArn=None,
                 SpeechMarkTypes=None, TextType=None):
        self.TaskId = TaskId
        self.OutputFormat = OutputFormat
        self.OutputS3BucketName = OutputS3BucketName
        self.Text = Text
        self.VoiceId = VoiceId
        self.Engine = Engine or "standard"
        self.LanguageCode = LanguageCode or "en-US"
        self.LexiconNames = LexiconNames or []
        self.OutputS3KeyPrefix = OutputS3KeyPrefix or ""
        self.SampleRate = SampleRate or "22050"
        self.SnsTopicArn = SnsTopicArn
        self.SpeechMarkTypes = SpeechMarkTypes or []
        self.TextType = TextType or "text"
        self.TaskStatus = "completed"
        self.TaskStatusReason = ""
        self.CreationTime = time.time()
        self.RequestCharacters = len(Text)
        self.OutputUri = f"https://s3.amazonaws.com/{OutputS3BucketName}/{OutputS3KeyPrefix or ''}{TaskId}.mp3"

    def to_dict(self):
        return {
            "TaskId": self.TaskId,
            "TaskStatus": self.TaskStatus,
            "TaskStatusReason": self.TaskStatusReason,
            "OutputUri": self.OutputUri,
            "CreationTime": self.CreationTime,
            "RequestCharacters": self.RequestCharacters,
            "SnsTopicArn": self.SnsTopicArn,
            "LexiconNames": self.LexiconNames,
            "OutputFormat": self.OutputFormat,
            "SampleRate": self.SampleRate,
            "SpeechMarkTypes": self.SpeechMarkTypes,
            "TextType": self.TextType,
            "VoiceId": self.VoiceId,
            "LanguageCode": self.LanguageCode,
            "Engine": self.Engine,
        }


# ── Store class ────────────────────────────────────────────────────

class PollyStore:
    """In-memory store for Polly resources."""

    def __init__(self):
        self._lexicons = {}  # name → LexiconRecord
        self._synthesis_tasks = {}  # task_id → SynthesisTaskRecord
        self._counter = 0

    def _next_id(self):
        self._counter += 1
        return self._counter

    # ── Lexicon operations ──────────────────────────────────────

    def lexicons(self, name=None):
        """Method-style accessor — returns single or all."""
        if name is not None:
            return self._lexicons.get(name)
        return list(self._lexicons.values())

    def put_lexicon(self, Name, Content):
        """Create or update a lexicon."""
        existing = self._lexicons.get(Name)
        if existing is None and len(self._lexicons) >= MAX_LEXICONS:
            raise MaxLexiconsNumberExceededException(
                f"Max lexicons ({MAX_LEXICONS}) exceeded")
        if len(Content) > 4096:
            raise LexiconSizeExceededException("Lexicon content exceeds 4096 bytes")
        record = LexiconRecord(Name=Name, Content=Content)
        self._lexicons[Name] = record
        return {}

    def get_lexicon(self, Name):
        """Get a lexicon by name."""
        record = self._lexicons.get(Name)
        if record is None:
            raise LexiconNotFoundException(f"Lexicon '{Name}' not found")
        return {
            "Lexicon": record.to_dict(),
            "LexiconAttributes": record.to_attributes(),
        }

    def list_lexicons(self, NextToken=None):
        """List all lexicons."""
        items = list(self._lexicons.values())
        result = []
        for r in items:
            result.append({
                "Name": r.Name,
                "Attributes": r.to_attributes(),
            })
        return {
            "Lexicons": result,
            "NextToken": None,
        }

    def delete_lexicon(self, Name):
        """Delete a lexicon."""
        if Name not in self._lexicons:
            raise LexiconNotFoundException(f"Lexicon '{Name}' not found")
        del self._lexicons[Name]
        return {}

    # ── DescribeVoices ──────────────────────────────────────────

    def describe_voices(self, Engine=None, LanguageCode=None,
                        IncludeAdditionalLanguageCodes=None, NextToken=None):
        """Return available voices (mock list)."""
        voices = [
            {"Id": "Joanna", "Name": "Joanna", "Gender": "Female",
             "LanguageCode": "en-US", "SupportedEngines": ["standard", "neural"]},
            {"Id": "Matthew", "Name": "Matthew", "Gender": "Male",
             "LanguageCode": "en-US", "SupportedEngines": ["standard", "neural"]},
            {"Id": "Amy", "Name": "Amy", "Gender": "Female",
             "LanguageCode": "en-GB", "SupportedEngines": ["standard"]},
            {"Id": "Brian", "Name": "Brian", "Gender": "Male",
             "LanguageCode": "en-GB", "SupportedEngines": ["standard"]},
            {"Id": "Mizuki", "Name": "Mizuki", "Gender": "Female",
             "LanguageCode": "ja-JP", "SupportedEngines": ["standard"]},
            {"Id": "Takumi", "Name": "Takumi", "Gender": "Male",
             "LanguageCode": "ja-JP", "SupportedEngines": ["standard"]},
        ]
        if LanguageCode:
            voices = [v for v in voices if v["LanguageCode"] == LanguageCode]
        if Engine:
            voices = [v for v in voices if Engine in v["SupportedEngines"]]
        return {
            "Voices": voices,
            "NextToken": None,
        }

    # ── SynthesizeSpeech ────────────────────────────────────────

    def synthesize_speech(self, OutputFormat, Text, VoiceId,
                          Engine=None, LanguageCode=None, LexiconNames=None,
                          SampleRate=None, SpeechMarkTypes=None, TextType=None):
        """Synthesize speech synchronously (mock — returns empty audio)."""
        if len(Text) > 3000:
            raise TextLengthExceededException("Text exceeds maximum length")
        # Mock audio data
        audio_data = b"\x00" * 1024  # 1KB mock audio
        content_type = {
            "mp3": "audio/mpeg",
            "ogg_vorbis": "audio/ogg",
            "pcm": "audio/pcm",
            "json": "application/json",
        }.get(OutputFormat, "audio/mpeg")
        return {
            "AudioStream": audio_data,
            "ContentType": content_type,
            "RequestCharacters": len(Text),
        }

    # ── Synthesis task operations ───────────────────────────────

    def synthesis_tasks(self, task_id=None):
        """Method-style accessor — returns single or all."""
        if task_id is not None:
            return self._synthesis_tasks.get(task_id)
        return list(self._synthesis_tasks.values())

    def start_speech_synthesis_task(self, OutputFormat, OutputS3BucketName,
                                    Text, VoiceId, **kwargs):
        """Start an async speech synthesis task."""
        if len(Text) > 100000:
            raise TextLengthExceededException("Text exceeds maximum length")
        task_id = str(uuid.uuid4())
        record = SynthesisTaskRecord(
            TaskId=task_id,
            OutputFormat=OutputFormat,
            OutputS3BucketName=OutputS3BucketName,
            Text=Text,
            VoiceId=VoiceId,
            **{k: v for k, v in kwargs.items()
               if k in ("Engine", "LanguageCode", "LexiconNames",
                        "OutputS3KeyPrefix", "SampleRate", "SnsTopicArn",
                        "SpeechMarkTypes", "TextType")})
        self._synthesis_tasks[task_id] = record
        return {"SynthesisTask": record.to_dict()}

    def get_speech_synthesis_task(self, TaskId):
        """Get a synthesis task by ID."""
        record = self._synthesis_tasks.get(TaskId)
        if record is None:
            raise SynthesisTaskNotFoundException(
                f"Synthesis task '{TaskId}' not found")
        return {"SynthesisTask": record.to_dict()}

    def list_speech_synthesis_tasks(self, MaxResults=None, NextToken=None,
                                    Status=None):
        """List synthesis tasks."""
        tasks = list(self._synthesis_tasks.values())
        if Status:
            tasks = [t for t in tasks if t.TaskStatus == Status]
        if MaxResults:
            tasks = tasks[:MaxResults]
        return {
            "SynthesisTasks": [t.to_dict() for t in tasks],
            "NextToken": None,
        }
