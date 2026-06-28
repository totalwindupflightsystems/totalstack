"""Integration test for Lex V2 Runtime — real store."""
import pytest
import os
import importlib.util
import types

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'lexv2-runtime')

models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

LexV2RuntimeStore = models_mod.LexV2RuntimeStore
ResourceNotFoundException = models_mod.ResourceNotFoundException
SessionRecord = models_mod.SessionRecord


def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.SessionRecord = SessionRecord
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


class TestLexV2RuntimeIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = LexV2RuntimeStore()
        return self._store

    BOT = "BOT123"
    ALIAS = "ALIAS456"
    LOCALE = "en_US"
    SESSION = "session-1"

    def test_put_session_happy(self):
        handler = _load_handler('put-session')
        resp = handler(self.store, {
            "botId": self.BOT, "botAliasId": self.ALIAS,
            "localeId": self.LOCALE, "sessionId": self.SESSION,
        })
        assert resp["sessionId"] == self.SESSION

    def test_get_session_happy(self):
        put = _load_handler('put-session')
        put(self.store, {
            "botId": self.BOT, "botAliasId": self.ALIAS,
            "localeId": self.LOCALE, "sessionId": self.SESSION,
        })
        handler = _load_handler('get-session')
        resp = handler(self.store, {
            "botId": self.BOT, "botAliasId": self.ALIAS,
            "localeId": self.LOCALE, "sessionId": self.SESSION,
        })
        assert resp["sessionId"] == self.SESSION

    def test_get_session_nonexistent(self):
        handler = _load_handler('get-session')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {
                "botId": self.BOT, "botAliasId": self.ALIAS,
                "localeId": self.LOCALE, "sessionId": "nonexistent",
            })

    def test_delete_session(self):
        put = _load_handler('put-session')
        put(self.store, {
            "botId": self.BOT, "botAliasId": self.ALIAS,
            "localeId": self.LOCALE, "sessionId": "to-delete",
        })
        handler = _load_handler('delete-session')
        resp = handler(self.store, {
            "botId": self.BOT, "botAliasId": self.ALIAS,
            "localeId": self.LOCALE, "sessionId": "to-delete",
        })
        assert resp == {}

    def test_recognize_text(self):
        put = _load_handler('put-session')
        put(self.store, {
            "botId": self.BOT, "botAliasId": self.ALIAS,
            "localeId": self.LOCALE, "sessionId": self.SESSION,
        })
        handler = _load_handler('recognize-text')
        resp = handler(self.store, {
            "botId": self.BOT, "botAliasId": self.ALIAS,
            "localeId": self.LOCALE, "sessionId": self.SESSION,
            "text": "Hello bot!",
        })
        assert "messages" in resp
        assert resp["sessionId"] == self.SESSION

    def test_recognize_utterance(self):
        put = _load_handler('put-session')
        put(self.store, {
            "botId": self.BOT, "botAliasId": self.ALIAS,
            "localeId": self.LOCALE, "sessionId": self.SESSION,
        })
        handler = _load_handler('recognize-utterance')
        resp = handler(self.store, {
            "botId": self.BOT, "botAliasId": self.ALIAS,
            "localeId": self.LOCALE, "sessionId": self.SESSION,
        })
        assert resp["sessionId"] == self.SESSION
        assert resp["inputMode"] == "Speech"

    def test_start_conversation(self):
        handler = _load_handler('start-conversation')
        resp = handler(self.store, {
            "botId": self.BOT, "botAliasId": self.ALIAS,
            "localeId": self.LOCALE, "sessionId": self.SESSION,
        })
        assert resp["sessionId"] == self.SESSION

    def test_duplicate_put_overwrites(self):
        put = _load_handler('put-session')
        put(self.store, {
            "botId": self.BOT, "botAliasId": self.ALIAS,
            "localeId": self.LOCALE, "sessionId": "dup",
            "sessionState": {"state": "old"},
        })
        put(self.store, {
            "botId": self.BOT, "botAliasId": self.ALIAS,
            "localeId": self.LOCALE, "sessionId": "dup",
            "sessionState": {"state": "new"},
        })
        get = _load_handler('get-session')
        resp = get(self.store, {
            "botId": self.BOT, "botAliasId": self.ALIAS,
            "localeId": self.LOCALE, "sessionId": "dup",
        })
        assert resp["sessionState"]["state"] == "new"
