"""Integration tests for LexV2 Models — 4 entities (Bot, Alias, Intent, SlotType)."""
import pytest
import os
import importlib.util
import types
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, "..", "lexv2-models")

# ── Load models.code.py ──
models_spec = importlib.util.spec_from_file_location(
    "models", os.path.join(SERVICE_DIR, "models.code.py")
)
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

LexV2ModelsStore = models_mod.LexV2ModelsStore
BotRecord = models_mod.BotRecord
BotAliasRecord = models_mod.BotAliasRecord
IntentRecord = models_mod.IntentRecord
SlotTypeRecord = models_mod.SlotTypeRecord
ResourceNotFoundException = models_mod.ResourceNotFoundException
ResourceInUseException = models_mod.ResourceInUseException
ConflictException = models_mod.ConflictException
ValidationException = models_mod.ValidationException


def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + ".code.py")
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ResourceInUseException = ResourceInUseException
    mod.ConflictException = ConflictException
    mod.ValidationException = ValidationException
    mod.BotRecord = BotRecord
    mod.BotAliasRecord = BotAliasRecord
    mod.IntentRecord = IntentRecord
    mod.SlotTypeRecord = SlotTypeRecord
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    spec.loader.exec_module(mod)
    skip_names = {"dataclass", "time", "uuid", "<lambda>"}
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith("_")
                and v.__name__ not in skip_names):
            return v
    raise RuntimeError(f"No handler found in {op_name}.code.py")


# ═══════════════════════════════════════════════════════════════════
# Bot Tests
# ═══════════════════════════════════════════════════════════════════

class TestBot:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = LexV2ModelsStore()
        return self._store

    def test_create_bot(self):
        handler = _load_handler("create-bot")
        resp = handler(self.store, {
            "botName": "my-bot",
            "roleArn": "arn:aws:iam::000000000000:role/LexRole",
            "dataPrivacy": {"childDirected": False},
            "idleSessionTTLInSeconds": 300,
        })
        assert resp["botName"] == "my-bot"
        assert "botId" in resp
        assert resp["botStatus"] == "Available"

    def test_create_bot_duplicate(self):
        handler = _load_handler("create-bot")
        req = {
            "botName": "dup-bot",
            "roleArn": "arn:aws:iam::000000000000:role/LexRole",
            "dataPrivacy": {"childDirected": False},
            "idleSessionTTLInSeconds": 300,
        }
        handler(self.store, req)
        with pytest.raises(ResourceInUseException):
            handler(self.store, req)

    def test_describe_bot(self):
        create = _load_handler("create-bot")
        describe = _load_handler("describe-bot")
        resp = create(self.store, {
            "botName": "desc-bot",
            "roleArn": "arn:aws:iam::000000000000:role/LexRole",
            "dataPrivacy": {"childDirected": False},
            "idleSessionTTLInSeconds": 300,
        })
        desc = describe(self.store, {"botId": resp["botId"]})
        assert desc["botName"] == "desc-bot"

    def test_describe_bot_not_found(self):
        handler = _load_handler("describe-bot")
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {"botId": "nonexistent"})

    def test_list_bots(self):
        create = _load_handler("create-bot")
        lst = _load_handler("list-bots")
        base = {
            "roleArn": "arn:aws:iam::000000000000:role/LexRole",
            "dataPrivacy": {"childDirected": False},
            "idleSessionTTLInSeconds": 300,
        }
        create(self.store, {**base, "botName": "bot-a"})
        create(self.store, {**base, "botName": "bot-b"})
        resp = lst(self.store, {})
        assert len(resp["botSummaries"]) >= 2

    def test_delete_bot(self):
        create = _load_handler("create-bot")
        delete = _load_handler("delete-bot")
        describe = _load_handler("describe-bot")
        resp = create(self.store, {
            "botName": "del-bot",
            "roleArn": "arn:aws:iam::000000000000:role/LexRole",
            "dataPrivacy": {"childDirected": False},
            "idleSessionTTLInSeconds": 300,
        })
        delete(self.store, {"botId": resp["botId"]})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {"botId": resp["botId"]})

    def test_update_bot(self):
        create = _load_handler("create-bot")
        update = _load_handler("update-bot")
        describe = _load_handler("describe-bot")
        resp = create(self.store, {
            "botName": "upd-bot",
            "roleArn": "arn:aws:iam::000000000000:role/LexRole",
            "dataPrivacy": {"childDirected": False},
            "idleSessionTTLInSeconds": 300,
        })
        update(self.store, {"botId": resp["botId"], "description": "updated desc"})
        desc = describe(self.store, {"botId": resp["botId"]})
        assert desc["description"] == "updated desc"


# ═══════════════════════════════════════════════════════════════════
# BotAlias Tests
# ═══════════════════════════════════════════════════════════════════

class TestBotAlias:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = LexV2ModelsStore()
        return self._store

    @pytest.fixture(autouse=True)
    def create_bot(self):
        create = _load_handler("create-bot")
        self.bot = create(self.store, {
            "botName": "alias-parent-bot",
            "roleArn": "arn:aws:iam::000000000000:role/LexRole",
            "dataPrivacy": {"childDirected": False},
            "idleSessionTTLInSeconds": 300,
        })
        return self.bot

    def test_create_alias(self):
        handler = _load_handler("create-bot-alias")
        resp = handler(self.store, {
            "botAliasName": "my-alias",
            "botId": self.bot["botId"],
            "botVersion": "1",
        })
        assert resp["botAliasName"] == "my-alias"
        assert "botAliasId" in resp

    def test_create_alias_duplicate(self):
        handler = _load_handler("create-bot-alias")
        req = {
            "botAliasName": "dup-alias",
            "botId": self.bot["botId"],
            "botVersion": "1",
        }
        handler(self.store, req)
        with pytest.raises(ConflictException):
            handler(self.store, req)

    def test_describe_alias(self):
        create = _load_handler("create-bot-alias")
        describe = _load_handler("describe-bot-alias")
        create(self.store, {
            "botAliasName": "desc-alias",
            "botId": self.bot["botId"],
            "botVersion": "1",
        })
        resp = describe(self.store, {"botId": self.bot["botId"], "botAliasName": "desc-alias"})
        assert resp["botAliasName"] == "desc-alias"

    def test_list_aliases(self):
        create = _load_handler("create-bot-alias")
        lst = _load_handler("list-bot-aliases")
        create(self.store, {"botAliasName": "a1", "botId": self.bot["botId"], "botVersion": "1"})
        create(self.store, {"botAliasName": "a2", "botId": self.bot["botId"], "botVersion": "1"})
        resp = lst(self.store, {"botId": self.bot["botId"]})
        assert len(resp["botAliasSummaries"]) >= 2

    def test_delete_alias(self):
        create = _load_handler("create-bot-alias")
        delete = _load_handler("delete-bot-alias")
        describe = _load_handler("describe-bot-alias")
        create(self.store, {"botAliasName": "del-alias", "botId": self.bot["botId"], "botVersion": "1"})
        delete(self.store, {"botId": self.bot["botId"], "botAliasName": "del-alias"})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {"botId": self.bot["botId"], "botAliasName": "del-alias"})

    def test_update_alias(self):
        create = _load_handler("create-bot-alias")
        update = _load_handler("update-bot-alias")
        describe = _load_handler("describe-bot-alias")
        create(self.store, {"botAliasName": "upd-alias", "botId": self.bot["botId"], "botVersion": "1"})
        update(self.store, {"botAliasName": "upd-alias", "botId": self.bot["botId"], "description": "new desc"})
        resp = describe(self.store, {"botId": self.bot["botId"], "botAliasName": "upd-alias"})
        assert resp["description"] == "new desc"


# ═══════════════════════════════════════════════════════════════════
# Intent Tests
# ═══════════════════════════════════════════════════════════════════

class TestIntent:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = LexV2ModelsStore()
        return self._store

    def _ctx(self):
        return {"botId": "bot-abc", "botVersion": "1", "localeId": "en_US"}

    def test_create_intent(self):
        handler = _load_handler("create-intent")
        resp = handler(self.store, {
            "intentName": "GreetingIntent",
            **self._ctx(),
        })
        assert resp["intentName"] == "GreetingIntent"
        assert "intentId" in resp

    def test_create_intent_duplicate(self):
        handler = _load_handler("create-intent")
        req = {"intentName": "DupIntent", **self._ctx()}
        handler(self.store, req)
        with pytest.raises(ConflictException):
            handler(self.store, req)

    def test_describe_intent(self):
        create = _load_handler("create-intent")
        describe = _load_handler("describe-intent")
        create(self.store, {"intentName": "DescIntent", **self._ctx()})
        resp = describe(self.store, {"intentName": "DescIntent", **self._ctx()})
        assert resp["intentName"] == "DescIntent"

    def test_list_intents(self):
        create = _load_handler("create-intent")
        lst = _load_handler("list-intents")
        create(self.store, {"intentName": "IntentA", **self._ctx()})
        create(self.store, {"intentName": "IntentB", **self._ctx()})
        resp = lst(self.store, self._ctx())
        assert len(resp["intentSummaries"]) >= 2

    def test_delete_intent(self):
        create = _load_handler("create-intent")
        delete = _load_handler("delete-intent")
        describe = _load_handler("describe-intent")
        create(self.store, {"intentName": "DelIntent", **self._ctx()})
        delete(self.store, {"intentName": "DelIntent", **self._ctx()})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {"intentName": "DelIntent", **self._ctx()})

    def test_update_intent(self):
        create = _load_handler("create-intent")
        update = _load_handler("update-intent")
        describe = _load_handler("describe-intent")
        create(self.store, {"intentName": "UpdIntent", **self._ctx()})
        update(self.store, {"intentName": "UpdIntent", **self._ctx(), "description": "new"})
        resp = describe(self.store, {"intentName": "UpdIntent", **self._ctx()})
        assert resp["description"] == "new"


# ═══════════════════════════════════════════════════════════════════
# SlotType Tests
# ═══════════════════════════════════════════════════════════════════

class TestSlotType:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = LexV2ModelsStore()
        return self._store

    def _ctx(self):
        return {"botId": "bot-xyz", "botVersion": "1", "localeId": "en_US"}

    def test_create_slot_type(self):
        handler = _load_handler("create-slot-type")
        resp = handler(self.store, {
            "slotTypeName": "ColorType",
            **self._ctx(),
        })
        assert resp["slotTypeName"] == "ColorType"
        assert "slotTypeId" in resp

    def test_create_slot_type_duplicate(self):
        handler = _load_handler("create-slot-type")
        req = {"slotTypeName": "DupType", **self._ctx()}
        handler(self.store, req)
        with pytest.raises(ConflictException):
            handler(self.store, req)

    def test_describe_slot_type(self):
        create = _load_handler("create-slot-type")
        describe = _load_handler("describe-slot-type")
        create(self.store, {"slotTypeName": "DescType", **self._ctx()})
        resp = describe(self.store, {"slotTypeName": "DescType", **self._ctx()})
        assert resp["slotTypeName"] == "DescType"

    def test_list_slot_types(self):
        create = _load_handler("create-slot-type")
        lst = _load_handler("list-slot-types")
        create(self.store, {"slotTypeName": "TypeA", **self._ctx()})
        create(self.store, {"slotTypeName": "TypeB", **self._ctx()})
        resp = lst(self.store, self._ctx())
        assert len(resp["slotTypeSummaries"]) >= 2

    def test_delete_slot_type(self):
        create = _load_handler("create-slot-type")
        delete = _load_handler("delete-slot-type")
        describe = _load_handler("describe-slot-type")
        create(self.store, {"slotTypeName": "DelType", **self._ctx()})
        delete(self.store, {"slotTypeName": "DelType", **self._ctx()})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {"slotTypeName": "DelType", **self._ctx()})

    def test_update_slot_type(self):
        create = _load_handler("create-slot-type")
        update = _load_handler("update-slot-type")
        describe = _load_handler("describe-slot-type")
        create(self.store, {"slotTypeName": "UpdType", **self._ctx()})
        update(self.store, {"slotTypeName": "UpdType", **self._ctx(), "description": "updated"})
        resp = describe(self.store, {"slotTypeName": "UpdType", **self._ctx()})
        assert resp["description"] == "updated"
