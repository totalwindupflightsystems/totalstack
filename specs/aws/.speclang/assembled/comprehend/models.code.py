"""Comprehend store — stateless inference + 5 managed entities."""
import time as _time

def _normalize_tags(tags):
    if not tags: return {}
    if isinstance(tags, dict): return dict(tags)
    if isinstance(tags, list):
        r = {}
        for t in tags:
            k = t.get("key", t.get("Key", ""))
            v = t.get("value", t.get("Value", ""))
            r[k] = v
        return r
    return {}

def _arn(resource_type, name):
    return f"arn:aws:comprehend:us-east-1:000000000000:{resource_type}/{name}"


class NotFoundException(Exception):
    def __init__(self, m="Not found"): self.message = m; super().__init__(m)

class ResourceInUseException(Exception):
    def __init__(self, m="In use"): self.message = m; super().__init__(m)

class InvalidRequestException(Exception):
    def __init__(self, m="Invalid"): self.message = m; super().__init__(m)

class TooManyTagsException(Exception):
    def __init__(self, m="Too many tags"): self.message = m; super().__init__(m)


class EntityRecord:
    def __init__(self, name, entity_type, **kw):
        self.arn = _arn(entity_type, name)
        self.entityName = name
        self.entityType = entity_type
        _status_map = {
            'dataset': 'COMPLETED',
            'document-classifier': 'TRAINED',
            'endpoint': 'IN_SERVICE',
            'entity-recognizer': 'TRAINED',
            'flywheel': 'ACTIVE',
        }
        self.status = _status_map.get(entity_type, 'ACTIVE')
        self.createTime = _time.time()
        for k, v in kw.items():
            if v is not None: setattr(self, k, v)

    def to_dict(self):
        d = {
            'dataset': {"DatasetArn": self.arn, "Status": self.status, "CreationTime": self.createTime},
            'document-classifier': {"DocumentClassifierArn": self.arn, "Status": self.status},
            'endpoint': {"EndpointArn": self.arn, "Status": self.status, "CreationTime": self.createTime},
            'entity-recognizer': {"EntityRecognizerArn": self.arn, "Status": self.status},
            'flywheel': {"FlywheelArn": self.arn, "Status": self.status},
        }.get(self.entityType, {"EntityRecognizerArn": self.arn, "Status": self.status})
        return d


class ComprehendStore:
    def __init__(self):
        self._entities = {}  # arn → record
        self._tags = {}

    # ── Managed entities (DocumentClassifier, EntityRecognizer, Endpoint, Flywheel, Dataset) ──

    def create_entity(self, arn_key, name, entity_type, **kw):
        record = EntityRecord(name, entity_type, **kw)
        record.arn = arn_key or _arn(entity_type.replace("-", ""), name)
        self._entities[record.arn] = record
        return record

    def describe_entity(self, arn):
        r = self._entities.get(arn)
        if not r: raise NotFoundException(f"{arn} not found")
        return r

    def list_entities(self, entity_type=None):
        result = []
        for r in self._entities.values():
            if entity_type is None or r.entityType == entity_type:
                result.append(r.to_dict())
        return result

    def delete_entity(self, arn):
        if arn not in self._entities: raise NotFoundException(f"{arn} not found")
        return self._entities.pop(arn)

    def update_entity(self, arn, **kw):
        r = self._entities.get(arn)
        if not r: raise NotFoundException(f"{arn} not found")
        for k, v in kw.items():
            if v is not None: setattr(r, k, v)
        return r

    # ── Stateless inference (returns mock results) ──

    def detect_sentiment(self, text, languageCode="en"):
        return {"Sentiment": "NEUTRAL", "SentimentScore": {"Positive": 0.3, "Negative": 0.2, "Neutral": 0.4, "Mixed": 0.1}}

    def detect_entities(self, text, languageCode="en"):
        return {"Entities": [{"Text": "AWS", "Type": "ORGANIZATION", "Score": 0.99, "BeginOffset": 0, "EndOffset": 3}]}

    def detect_key_phrases(self, text, languageCode="en"):
        return {"KeyPhrases": [{"Text": text.split()[0] if text else "sample", "Score": 0.99, "BeginOffset": 0, "EndOffset": len(text.split()[0]) if text else 6}]}

    def detect_dominant_language(self, text):
        return {"Languages": [{"LanguageCode": "en", "Score": 0.99}]}

    def detect_syntax(self, text, languageCode="en"):
        return {"SyntaxTokens": [{"Text": "AWS", "PartOfSpeech": {"Tag": "NOUN", "Score": 0.99}, "BeginOffset": 0, "EndOffset": 3}]}

    def detect_pii_entities(self, text, languageCode="en"):
        return {"Entities": []}

    def detect_targeted_sentiment(self, text, languageCode="en"):
        return {"Entities": []}

    def detect_toxic_content(self, textSegments):
        return {"ResultList": [{"Toxicity": 0.01, "Labels": []}]}

    def classify_document(self, text, endpointArn):
        return {"Classes": [{"Name": "class-a", "Score": 0.9}]}

    def contains_pii_entities(self, text, languageCode="en"):
        return {"Labels": []}

    # ── Tags ──

    def tag_resource(self, arn, tags):
        n = _normalize_tags(tags)
        if not n: return
        existing = self._tags.get(arn, {})
        existing.update(n)
        self._tags[arn] = existing

    def untag_resource(self, arn, tagKeys):
        e = self._tags.get(arn, {})
        for k in tagKeys: e.pop(k, None)
        self._tags[arn] = e

    def list_tags_for_resource(self, arn):
        tags = self._tags.get(arn, {})
        return {"Tags": [{"Key": k, "Value": v} for k, v in tags.items()]}
