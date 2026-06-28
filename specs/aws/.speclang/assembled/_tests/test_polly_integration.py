"""Integration test for Polly — real LocalStack store."""
import pytest
import os
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'polly')

# Load models module dynamically
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

PollyStore = models_mod.PollyStore
LexiconRecord = models_mod.LexiconRecord
SynthesisTaskRecord = models_mod.SynthesisTaskRecord
InvalidLexiconException = models_mod.InvalidLexiconException
LexiconNotFoundException = models_mod.LexiconNotFoundException
ServiceFailureException = models_mod.ServiceFailureException
SynthesisTaskNotFoundException = models_mod.SynthesisTaskNotFoundException
InvalidTaskIdException = models_mod.InvalidTaskIdException
MaxLexiconsNumberExceededException = models_mod.MaxLexiconsNumberExceededException
LexiconSizeExceededException = models_mod.LexiconSizeExceededException


def _load_handler(op_name):
    """Load a single-handler .code.py file — returns the handler function."""
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.InvalidLexiconException = InvalidLexiconException
    mod.LexiconNotFoundException = LexiconNotFoundException
    mod.ServiceFailureException = ServiceFailureException
    mod.SynthesisTaskNotFoundException = SynthesisTaskNotFoundException
    mod.InvalidTaskIdException = InvalidTaskIdException
    mod.MaxLexiconsNumberExceededException = MaxLexiconsNumberExceededException
    mod.LexiconSizeExceededException = LexiconSizeExceededException
    mod.LexiconRecord = LexiconRecord
    mod.SynthesisTaskRecord = SynthesisTaskRecord
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


class TestLexiconIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = PollyStore()
        return self._store

    def test_put_lexicon_happy(self):
        handler = _load_handler('put-lexicon')
        response = handler(self.store, {
            "Name": "test-lexicon",
            "Content": "<lexicon><lexeme><grapheme>test</grapheme></lexeme></lexicon>",
        })
        assert response == {}

    def test_put_lexicon_duplicate_overwrites(self):
        handler = _load_handler('put-lexicon')
        handler(self.store, {
            "Name": "dup-lexicon",
            "Content": "<lexicon><lexeme><grapheme>dup</grapheme></lexeme></lexicon>",
        })
        response = handler(self.store, {
            "Name": "dup-lexicon",
            "Content": "<lexicon><lexeme><grapheme>overwritten</grapheme></lexeme></lexicon>",
        })
        assert response == {}

    def test_put_lexicon_missing_name(self):
        handler = _load_handler('put-lexicon')
        with pytest.raises(KeyError):
            handler(self.store, {"Content": "x"})

    def test_put_lexicon_missing_content(self):
        handler = _load_handler('put-lexicon')
        with pytest.raises(KeyError):
            handler(self.store, {"Name": "x"})

    def test_get_lexicon_happy(self):
        put_handler = _load_handler('put-lexicon')
        put_handler(self.store, {
            "Name": "readable",
            "Content": "<lexicon><lexeme><grapheme>readable</grapheme></lexeme></lexicon>",
        })
        handler = _load_handler('get-lexicon')
        response = handler(self.store, {"Name": "readable"})
        assert response is not None
        assert "Lexicon" in response
        assert "LexiconAttributes" in response
        assert response["Lexicon"]["Name"] == "readable"

    def test_get_lexicon_nonexistent(self):
        handler = _load_handler('get-lexicon')
        with pytest.raises(LexiconNotFoundException):
            handler(self.store, {"Name": "nonexistent"})

    def test_list_lexicons(self):
        put_handler = _load_handler('put-lexicon')
        put_handler(self.store, {
            "Name": "l1",
            "Content": "<lexicon><lexeme><grapheme>l1</grapheme></lexeme></lexicon>",
        })
        put_handler(self.store, {
            "Name": "l2",
            "Content": "<lexicon><lexeme><grapheme>l2</grapheme></lexeme></lexicon>",
        })
        handler = _load_handler('list-lexicons')
        response = handler(self.store, {})
        assert len(response["Lexicons"]) == 2
        assert response["NextToken"] is None

    def test_list_lexicons_empty(self):
        handler = _load_handler('list-lexicons')
        response = handler(self.store, {})
        assert response["Lexicons"] == []

    def test_delete_lexicon_happy(self):
        put_handler = _load_handler('put-lexicon')
        put_handler(self.store, {
            "Name": "todelete",
            "Content": "<lexicon><lexeme><grapheme>todel</grapheme></lexeme></lexicon>",
        })
        handler = _load_handler('delete-lexicon')
        response = handler(self.store, {"Name": "todelete"})
        assert response == {}

    def test_delete_lexicon_nonexistent(self):
        handler = _load_handler('delete-lexicon')
        with pytest.raises(LexiconNotFoundException):
            handler(self.store, {"Name": "nonexistent"})


class TestDescribeVoicesIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = PollyStore()
        return self._store

    def test_describe_voices_all(self):
        handler = _load_handler('describe-voices')
        response = handler(self.store, {})
        assert "Voices" in response
        assert len(response["Voices"]) >= 2

    def test_describe_voices_filter_language(self):
        handler = _load_handler('describe-voices')
        response = handler(self.store, {"LanguageCode": "en-GB"})
        assert len(response["Voices"]) == 2
        assert all(v["LanguageCode"] == "en-GB" for v in response["Voices"])


class TestSynthesizeSpeechIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = PollyStore()
        return self._store

    def test_synthesize_speech_happy(self):
        handler = _load_handler('synthesize-speech')
        response = handler(self.store, {
            "OutputFormat": "mp3",
            "Text": "Hello world",
            "VoiceId": "Joanna",
        })
        assert "AudioStream" in response
        assert "ContentType" in response
        assert response["ContentType"] == "audio/mpeg"

    def test_synthesize_speech_ogg(self):
        handler = _load_handler('synthesize-speech')
        response = handler(self.store, {
            "OutputFormat": "ogg_vorbis",
            "Text": "Hello",
            "VoiceId": "Matthew",
        })
        assert response["ContentType"] == "audio/ogg"

    def test_synthesize_speech_missing_format(self):
        handler = _load_handler('synthesize-speech')
        with pytest.raises(KeyError):
            handler(self.store, {"Text": "x", "VoiceId": "Joanna"})

    def test_synthesize_speech_missing_text(self):
        handler = _load_handler('synthesize-speech')
        with pytest.raises(KeyError):
            handler(self.store, {"OutputFormat": "mp3", "VoiceId": "Joanna"})


class TestSynthesisTaskIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = PollyStore()
        return self._store

    def test_start_task_happy(self):
        handler = _load_handler('start-speech-synthesis-task')
        response = handler(self.store, {
            "OutputFormat": "mp3",
            "OutputS3BucketName": "test-bucket",
            "Text": "Hello world",
            "VoiceId": "Joanna",
        })
        assert "SynthesisTask" in response
        task = response["SynthesisTask"]
        assert task["TaskStatus"] == "completed"
        assert task["OutputFormat"] == "mp3"
        assert task["VoiceId"] == "Joanna"
        assert "TaskId" in task

    def test_start_task_with_options(self):
        handler = _load_handler('start-speech-synthesis-task')
        response = handler(self.store, {
            "OutputFormat": "ogg_vorbis",
            "OutputS3BucketName": "my-bucket",
            "OutputS3KeyPrefix": "audio/",
            "Text": "Testing",
            "VoiceId": "Amy",
            "SampleRate": "24000",
            "TextType": "ssml",
        })
        task = response["SynthesisTask"]
        assert task["SampleRate"] == "24000"
        assert task["TextType"] == "ssml"

    def test_get_task_happy(self):
        start_handler = _load_handler('start-speech-synthesis-task')
        started = start_handler(self.store, {
            "OutputFormat": "mp3",
            "OutputS3BucketName": "test-bucket",
            "Text": "Hello",
            "VoiceId": "Joanna",
        })
        task_id = started["SynthesisTask"]["TaskId"]

        get_handler = _load_handler('get-speech-synthesis-task')
        response = get_handler(self.store, {"TaskId": task_id})
        assert response["SynthesisTask"]["TaskId"] == task_id

    def test_get_task_nonexistent(self):
        handler = _load_handler('get-speech-synthesis-task')
        with pytest.raises(SynthesisTaskNotFoundException):
            handler(self.store, {"TaskId": "nonexistent-id"})

    def test_list_tasks(self):
        start_handler = _load_handler('start-speech-synthesis-task')
        start_handler(self.store, {
            "OutputFormat": "mp3",
            "OutputS3BucketName": "test-bucket",
            "Text": "Task 1",
            "VoiceId": "Joanna",
        })
        start_handler(self.store, {
            "OutputFormat": "mp3",
            "OutputS3BucketName": "test-bucket",
            "Text": "Task 2",
            "VoiceId": "Matthew",
        })

        list_handler = _load_handler('list-speech-synthesis-tasks')
        response = list_handler(self.store, {})
        assert len(response["SynthesisTasks"]) == 2

    def test_list_tasks_empty(self):
        handler = _load_handler('list-speech-synthesis-tasks')
        response = handler(self.store, {})
        assert response["SynthesisTasks"] == []
