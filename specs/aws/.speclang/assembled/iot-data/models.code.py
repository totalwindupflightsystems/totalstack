"""IoT Data Plane Store — Thing Shadow operations."""


class ResourceNotFoundException(Exception):
    pass


class InvalidRequestException(Exception):
    pass


class ConflictException(Exception):
    pass


class IoTDataStore:
    def __init__(self):
        self._shadows: dict[str, dict] = {}  # thingName -> shadow payload
        self._named_shadows: dict[str, dict] = {}  # f"{thingName}/{shadowName}" -> payload

    # ── Thing Shadow ──
    def get_thing_shadow(self, thingName, shadowName=None):
        if shadowName:
            key = f"{thingName}/{shadowName}"
            if key not in self._named_shadows:
                raise ResourceNotFoundException(f"Shadow {shadowName} not found for thing {thingName}")
            return self._named_shadows[key]
        if thingName not in self._shadows:
            raise ResourceNotFoundException(f"Shadow not found for thing {thingName}")
        return self._shadows[thingName]

    def update_thing_shadow(self, thingName, payload, shadowName=None):
        if shadowName:
            key = f"{thingName}/{shadowName}"
            self._named_shadows[key] = payload
        else:
            self._shadows[thingName] = payload
        return payload

    def delete_thing_shadow(self, thingName, shadowName=None):
        if shadowName:
            key = f"{thingName}/{shadowName}"
            if key not in self._named_shadows:
                raise ResourceNotFoundException(f"Shadow {shadowName} not found for thing {thingName}")
            del self._named_shadows[key]
        else:
            if thingName not in self._shadows:
                raise ResourceNotFoundException(f"Shadow not found for thing {thingName}")
            del self._shadows[thingName]

    def list_named_shadows_for_thing(self, thingName):
        results = []
        prefix = f"{thingName}/"
        for key in self._named_shadows:
            if key.startswith(prefix):
                results.append(key[len(prefix):])
        return results

    # ── Publish ──
    def publish(self, topic, payload, qos=0):
        return {"topic": topic, "qos": qos}

    # ── Retained Messages ──
    _retained: dict[str, dict] = {}

    def get_retained_message(self, topic):
        if topic not in IoTDataStore._retained:
            raise ResourceNotFoundException(f"No retained message for topic {topic}")
        return IoTDataStore._retained[topic]

    def list_retained_messages(self):
        return list(IoTDataStore._retained.values())

    def delete_retained_message(self, topic):
        IoTDataStore._retained.pop(topic, None)
