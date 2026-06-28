"""Lex V2 Models Store — Bot, BotAlias, Intent, SlotType entities."""
import time as _time
import uuid as _uuid


class ResourceNotFoundException(Exception):
    pass


class ResourceInUseException(Exception):
    pass


class ConflictException(Exception):
    pass


class ValidationException(Exception):
    pass


class BotRecord:
    def __init__(self, botName, botId=None, description=None,
                 roleArn=None, dataPrivacy=None, idleSessionTTLInSeconds=None,
                 botTags=None, testBotAliasTags=None,
                 botStatus="Available", creationDateTime=None):
        self.botName = botName
        self.botId = botId or f"bot-{_uuid.uuid4().hex[:10]}"
        self.description = description
        self.roleArn = roleArn
        self.dataPrivacy = dataPrivacy
        self.idleSessionTTLInSeconds = idleSessionTTLInSeconds or 300
        self.botTags = botTags
        self.testBotAliasTags = testBotAliasTags
        self.botStatus = botStatus
        self.creationDateTime = creationDateTime or _time.time()

    def to_dict(self):
        return {
            "botName": self.botName,
            "botId": self.botId,
            "description": self.description,
            "roleArn": self.roleArn,
            "dataPrivacy": self.dataPrivacy,
            "idleSessionTTLInSeconds": self.idleSessionTTLInSeconds,
            "botStatus": self.botStatus,
            "creationDateTime": self.creationDateTime,
        }


class BotAliasRecord:
    def __init__(self, botAliasName, botId, botAliasId=None,
                 botVersion=None, botAliasLocaleSettings=None,
                 conversationLogSettings=None, sentimentAnalysisSettings=None,
                 description=None, botAliasStatus="Available",
                 creationDateTime=None):
        self.botAliasName = botAliasName
        self.botId = botId
        self.botAliasId = botAliasId or f"alias-{_uuid.uuid4().hex[:10]}"
        self.botVersion = botVersion
        self.botAliasLocaleSettings = botAliasLocaleSettings
        self.conversationLogSettings = conversationLogSettings
        self.sentimentAnalysisSettings = sentimentAnalysisSettings
        self.description = description
        self.botAliasStatus = botAliasStatus
        self.creationDateTime = creationDateTime or _time.time()

    def to_dict(self):
        return {
            "botAliasName": self.botAliasName,
            "botId": self.botId,
            "botAliasId": self.botAliasId,
            "botVersion": self.botVersion,
            "botAliasStatus": self.botAliasStatus,
            "description": self.description,
            "creationDateTime": self.creationDateTime,
        }


class IntentRecord:
    def __init__(self, intentName, botId, botVersion, localeId,
                 intentId=None, description=None,
                 sampleUtterances=None, dialogCodeHook=None,
                 fulfillmentCodeHook=None, slotPriorities=None,
                 intentConfirmationSetting=None,
                 intentClosingSetting=None,
                 inputContexts=None, outputContexts=None,
                 kendraConfiguration=None,
                 initialResponseSetting=None,
                 qIntentConfiguration=None,
                 creationDateTime=None):
        self.intentName = intentName
        self.botId = botId
        self.botVersion = botVersion
        self.localeId = localeId
        self.intentId = intentId or f"intent-{_uuid.uuid4().hex[:10]}"
        self.description = description
        self.sampleUtterances = sampleUtterances
        self.dialogCodeHook = dialogCodeHook
        self.fulfillmentCodeHook = fulfillmentCodeHook
        self.slotPriorities = slotPriorities
        self.intentConfirmationSetting = intentConfirmationSetting
        self.intentClosingSetting = intentClosingSetting
        self.inputContexts = inputContexts
        self.outputContexts = outputContexts
        self.kendraConfiguration = kendraConfiguration
        self.initialResponseSetting = initialResponseSetting
        self.qIntentConfiguration = qIntentConfiguration
        self.creationDateTime = creationDateTime or _time.time()

    def to_dict(self):
        return {
            "intentName": self.intentName,
            "intentId": self.intentId,
            "botId": self.botId,
            "botVersion": self.botVersion,
            "localeId": self.localeId,
            "description": self.description,
            "sampleUtterances": self.sampleUtterances,
            "creationDateTime": self.creationDateTime,
        }


class SlotTypeRecord:
    def __init__(self, slotTypeName, botId, botVersion, localeId,
                 slotTypeId=None, description=None,
                 slotTypeValues=None, valueSelectionSetting=None,
                 parentSlotTypeSignature=None,
                 externalSourceSetting=None,
                 compositeSlotTypeSetting=None,
                 creationDateTime=None):
        self.slotTypeName = slotTypeName
        self.botId = botId
        self.botVersion = botVersion
        self.localeId = localeId
        self.slotTypeId = slotTypeId or f"slottype-{_uuid.uuid4().hex[:10]}"
        self.description = description
        self.slotTypeValues = slotTypeValues
        self.valueSelectionSetting = valueSelectionSetting
        self.parentSlotTypeSignature = parentSlotTypeSignature
        self.externalSourceSetting = externalSourceSetting
        self.compositeSlotTypeSetting = compositeSlotTypeSetting
        self.creationDateTime = creationDateTime or _time.time()

    def to_dict(self):
        return {
            "slotTypeName": self.slotTypeName,
            "slotTypeId": self.slotTypeId,
            "botId": self.botId,
            "botVersion": self.botVersion,
            "localeId": self.localeId,
            "description": self.description,
            "slotTypeValues": self.slotTypeValues,
            "creationDateTime": self.creationDateTime,
        }


class LexV2ModelsStore:
    def __init__(self):
        self._bots: dict[str, BotRecord] = {}
        self._bot_aliases: dict[str, dict[str, BotAliasRecord]] = {}  # botId -> {aliasName: record}
        self._intents: dict[str, dict[str, IntentRecord]] = {}  # botId+version+locale -> {intentName: record}
        self._slot_types: dict[str, dict[str, SlotTypeRecord]] = {}

    # ── Bot CRUD ──
    def create_bot(self, **kwargs):
        name = kwargs["botName"]
        for r in self._bots.values():
            if r.botName == name:
                raise ResourceInUseException(f"Bot {name} already exists")
        record = BotRecord(**kwargs)
        self._bots[record.botId] = record
        return record.to_dict()

    def describe_bot(self, botId):
        record = self._bots.get(botId)
        if not record:
            raise ResourceNotFoundException(f"Bot {botId} not found")
        return record.to_dict()

    def list_bots(self, **kwargs):
        return [r.to_dict() for r in self._bots.values()]

    def delete_bot(self, botId):
        if botId not in self._bots:
            raise ResourceNotFoundException(f"Bot {botId} not found")
        del self._bots[botId]
        self._bot_aliases.pop(botId, None)

    def update_bot(self, **kwargs):
        bot_id = kwargs["botId"]
        record = self._bots.get(bot_id)
        if not record:
            raise ResourceNotFoundException(f"Bot {bot_id} not found")
        for key in ("botName", "description", "roleArn", "dataPrivacy", "idleSessionTTLInSeconds"):
            if key in kwargs:
                setattr(record, key, kwargs[key])
        return record.to_dict()

    # ── BotAlias CRUD ──
    def create_bot_alias(self, **kwargs):
        bot_id = kwargs["botId"]
        name = kwargs["botAliasName"]
        if bot_id not in self._bots:
            raise ResourceNotFoundException(f"Bot {bot_id} not found")
        aliases = self._bot_aliases.setdefault(bot_id, {})
        if name in aliases:
            raise ConflictException(f"Alias {name} already exists for bot {bot_id}")
        record = BotAliasRecord(**kwargs)
        aliases[name] = record
        return record.to_dict()

    def describe_bot_alias(self, botId, botAliasName):
        aliases = self._bot_aliases.get(botId, {})
        record = aliases.get(botAliasName)
        if not record:
            raise ResourceNotFoundException(f"Alias {botAliasName} not found for bot {botId}")
        return record.to_dict()

    def list_bot_aliases(self, botId, **kwargs):
        return [r.to_dict() for r in self._bot_aliases.get(botId, {}).values()]

    def delete_bot_alias(self, botId, botAliasName):
        aliases = self._bot_aliases.get(botId, {})
        if botAliasName not in aliases:
            raise ResourceNotFoundException(f"Alias {botAliasName} not found")
        del aliases[botAliasName]

    def update_bot_alias(self, **kwargs):
        bot_id = kwargs["botId"]
        name = kwargs["botAliasName"]
        aliases = self._bot_aliases.get(bot_id, {})
        record = aliases.get(name)
        if not record:
            raise ResourceNotFoundException(f"Alias {name} not found")
        for key in ("botAliasLocaleSettings", "conversationLogSettings",
                     "sentimentAnalysisSettings", "description", "botVersion"):
            if key in kwargs:
                setattr(record, key, kwargs[key])
        return record.to_dict()

    # ── Intent CRUD ──
    def _intent_key(self, botId, botVersion, localeId):
        return f"{botId}/{botVersion}/{localeId}"

    def create_intent(self, **kwargs):
        bot_id = kwargs["botId"]
        key = self._intent_key(bot_id, kwargs["botVersion"], kwargs["localeId"])
        name = kwargs["intentName"]
        intents = self._intents.setdefault(key, {})
        if name in intents:
            raise ConflictException(f"Intent {name} already exists")
        record = IntentRecord(**kwargs)
        intents[name] = record
        return record.to_dict()

    def describe_intent(self, intentName, botId, botVersion, localeId):
        key = self._intent_key(botId, botVersion, localeId)
        record = self._intents.get(key, {}).get(intentName)
        if not record:
            raise ResourceNotFoundException(f"Intent {intentName} not found")
        return record.to_dict()

    def list_intents(self, botId, botVersion, localeId, **kwargs):
        key = self._intent_key(botId, botVersion, localeId)
        return [r.to_dict() for r in self._intents.get(key, {}).values()]

    def delete_intent(self, intentName, botId, botVersion, localeId):
        key = self._intent_key(botId, botVersion, localeId)
        intents = self._intents.get(key, {})
        if intentName not in intents:
            raise ResourceNotFoundException(f"Intent {intentName} not found")
        del intents[intentName]

    def update_intent(self, **kwargs):
        bot_id = kwargs["botId"]
        key = self._intent_key(bot_id, kwargs["botVersion"], kwargs["localeId"])
        name = kwargs["intentName"]
        record = self._intents.get(key, {}).get(name)
        if not record:
            raise ResourceNotFoundException(f"Intent {name} not found")
        for k in ("description", "sampleUtterances", "dialogCodeHook",
                   "fulfillmentCodeHook", "slotPriorities"):
            if k in kwargs:
                setattr(record, k, kwargs[k])
        return record.to_dict()

    # ── SlotType CRUD ──
    def _slot_type_key(self, botId, botVersion, localeId):
        return f"{botId}/{botVersion}/{localeId}"

    def create_slot_type(self, **kwargs):
        bot_id = kwargs["botId"]
        key = self._slot_type_key(bot_id, kwargs["botVersion"], kwargs["localeId"])
        name = kwargs["slotTypeName"]
        types = self._slot_types.setdefault(key, {})
        if name in types:
            raise ConflictException(f"SlotType {name} already exists")
        record = SlotTypeRecord(**kwargs)
        types[name] = record
        return record.to_dict()

    def describe_slot_type(self, slotTypeName, botId, botVersion, localeId):
        key = self._slot_type_key(botId, botVersion, localeId)
        record = self._slot_types.get(key, {}).get(slotTypeName)
        if not record:
            raise ResourceNotFoundException(f"SlotType {slotTypeName} not found")
        return record.to_dict()

    def list_slot_types(self, botId, botVersion, localeId, **kwargs):
        key = self._slot_type_key(botId, botVersion, localeId)
        return [r.to_dict() for r in self._slot_types.get(key, {}).values()]

    def delete_slot_type(self, slotTypeName, botId, botVersion, localeId):
        key = self._slot_type_key(botId, botVersion, localeId)
        types = self._slot_types.get(key, {})
        if slotTypeName not in types:
            raise ResourceNotFoundException(f"SlotType {slotTypeName} not found")
        del types[slotTypeName]

    def update_slot_type(self, **kwargs):
        bot_id = kwargs["botId"]
        key = self._slot_type_key(bot_id, kwargs["botVersion"], kwargs["localeId"])
        name = kwargs["slotTypeName"]
        record = self._slot_types.get(key, {}).get(name)
        if not record:
            raise ResourceNotFoundException(f"SlotType {name} not found")
        for k in ("description", "slotTypeValues", "valueSelectionSetting",
                   "parentSlotTypeSignature"):
            if k in kwargs:
                setattr(record, k, kwargs[k])
        return record.to_dict()
