"""Lex V2 Runtime — chatbot runtime. Manages sessions and processes user input."""
import time


class LexV2RuntimeException(Exception):
    code = "InternalServerException"
    def __init__(self, message=None):
        super().__init__(message or self.code)
        self.message = message or self.code


class AccessDeniedException(LexV2RuntimeException):
    code = "AccessDeniedException"

class ResourceNotFoundException(LexV2RuntimeException):
    code = "ResourceNotFoundException"

class ValidationException(LexV2RuntimeException):
    code = "ValidationException"

class ThrottlingException(LexV2RuntimeException):
    code = "ThrottlingException"

class InternalServerException(LexV2RuntimeException):
    code = "InternalServerException"

class ConflictException(LexV2RuntimeException):
    code = "ConflictException"

class DependencyFailedException(LexV2RuntimeException):
    code = "DependencyFailedException"

class BadGatewayException(LexV2RuntimeException):
    code = "BadGatewayException"


class SessionRecord:
    def __init__(self, sessionId, botId, botAliasId, localeId,
                 sessionState=None, messages=None, requestAttributes=None):
        self.sessionId = sessionId
        self.botId = botId
        self.botAliasId = botAliasId
        self.localeId = localeId
        self.sessionState = sessionState or {}
        self.messages = messages or []
        self.requestAttributes = requestAttributes or {}
        self.lastModified = time.time()

    def to_dict(self):
        return {
            "sessionId": self.sessionId,
            "sessionState": self.sessionState,
            "messages": self.messages,
            "interpretations": [],
        }


class LexV2RuntimeStore:
    def __init__(self):
        self._sessions = {}

    def sessions(self, session_id=None):
        if session_id is not None:
            return self._sessions.get(session_id)
        return list(self._sessions.values())

    def put_session(self, botId, botAliasId, localeId, sessionId,
                    sessionState=None, messages=None, requestAttributes=None,
                    responseContentType=None):
        session_key = f"{botId}/{botAliasId}/{localeId}/{sessionId}"
        record = SessionRecord(
            sessionId=sessionId, botId=botId, botAliasId=botAliasId,
            localeId=localeId, sessionState=sessionState,
            messages=messages, requestAttributes=requestAttributes)
        self._sessions[session_key] = record
        return record.to_dict()

    def get_session(self, botId, botAliasId, localeId, sessionId):
        session_key = f"{botId}/{botAliasId}/{localeId}/{sessionId}"
        record = self._sessions.get(session_key)
        if record is None:
            raise ResourceNotFoundException(f"Session '{sessionId}' not found")
        return record.to_dict()

    def delete_session(self, botId, botAliasId, localeId, sessionId):
        session_key = f"{botId}/{botAliasId}/{localeId}/{sessionId}"
        if session_key in self._sessions:
            del self._sessions[session_key]
        return {}

    def recognize_text(self, botId, botAliasId, localeId, sessionId, text,
                       sessionState=None, requestAttributes=None):
        session_key = f"{botId}/{botAliasId}/{localeId}/{sessionId}"
        record = self._sessions.get(session_key)
        if record is None:
            record = SessionRecord(
                sessionId=sessionId, botId=botId, botAliasId=botAliasId,
                localeId=localeId)
        if sessionState:
            record.sessionState = sessionState
        record.messages.append({"content": text, "contentType": "PlainText"})
        record.lastModified = time.time()
        self._sessions[session_key] = record
        return {
            "messages": [{"content": f"Echo: {text}", "contentType": "PlainText"}],
            "sessionState": record.sessionState,
            "interpretations": [],
            "sessionId": sessionId,
        }

    def recognize_utterance(self, botId, botAliasId, localeId, sessionId,
                            inputStream=None, requestAttributes=None,
                            sessionState=None, responseContentType=None):
        session_key = f"{botId}/{botAliasId}/{localeId}/{sessionId}"
        record = self._sessions.get(session_key)
        if record is None:
            record = SessionRecord(
                sessionId=sessionId, botId=botId, botAliasId=botAliasId,
                localeId=localeId)
        record.lastModified = time.time()
        self._sessions[session_key] = record
        return {
            "inputMode": "Speech",
            "contentType": "text/plain; charset=utf-8",
            "messages": "",
            "interpretations": "",
            "sessionState": record.sessionState,
            "requestAttributes": record.requestAttributes,
            "sessionId": sessionId,
            "inputTranscript": "",
        }

    def start_conversation(self, botId, botAliasId, localeId, sessionId,
                           conversationMode=None):
        session_key = f"{botId}/{botAliasId}/{localeId}/{sessionId}"
        record = SessionRecord(
            sessionId=sessionId, botId=botId, botAliasId=botAliasId,
            localeId=localeId)
        self._sessions[session_key] = record
        return {"sessionId": sessionId}
