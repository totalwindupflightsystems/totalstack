"""Integration test for RolesAnywhere — real store."""
import pytest
import os
import types
import importlib.util
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'rolesanywhere')

models_spec = importlib.util.spec_from_file_location('models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

RolesAnywhereStore = models_mod.RolesAnywhereStore
ResourceNotFoundException = models_mod.ResourceNotFoundException
ValidationException = models_mod.ValidationException

skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}


def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ValidationException = ValidationException
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    spec.loader.exec_module(mod)
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


class TestProfile:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = RolesAnywhereStore()
        return self._store

    def test_create_profile_happy(self):
        handler = _load_handler('CreateProfile')
        resp = handler(self.store, {"name": "test-profile", "roleArns": ["arn:aws:iam::123:role/test"]})
        assert "profile" in resp
        assert resp["profile"]["name"] == "test-profile"
        assert resp["profile"]["enabled"] is True
        assert resp["profile"]["roleArns"] == ["arn:aws:iam::123:role/test"]

    def test_create_profile_with_tags(self):
        handler = _load_handler('CreateProfile')
        resp = handler(self.store, {
            "name": "tagged-profile",
            "roleArns": ["arn:aws:iam::123:role/x"],
            "tags": [{"key": "env", "value": "test"}],
        })
        assert resp["profile"]["tags"]["env"] == "test"

    def test_get_profile_happy(self):
        create = _load_handler('CreateProfile')
        resp = create(self.store, {"name": "get-prof", "roleArns": []})
        pid = resp["profile"]["profileId"]

        get_h = _load_handler('GetProfile')
        resp2 = get_h(self.store, {"profileId": pid})
        assert resp2["profile"]["name"] == "get-prof"

    def test_get_profile_not_found(self):
        get_h = _load_handler('GetProfile')
        with pytest.raises(ResourceNotFoundException):
            get_h(self.store, {"profileId": "nonexistent"})

    def test_update_profile(self):
        create = _load_handler('CreateProfile')
        resp = create(self.store, {"name": "upd-prof", "roleArns": ["arn:old"]})
        pid = resp["profile"]["profileId"]

        upd = _load_handler('UpdateProfile')
        resp2 = upd(self.store, {"profileId": pid, "name": "updated-name", "roleArns": ["arn:new"]})
        assert resp2["profile"]["name"] == "updated-name"
        assert resp2["profile"]["roleArns"] == ["arn:new"]

    def test_update_profile_not_found(self):
        upd = _load_handler('UpdateProfile')
        with pytest.raises(ResourceNotFoundException):
            upd(self.store, {"profileId": "nonexistent", "name": "x"})

    def test_delete_profile(self):
        create = _load_handler('CreateProfile')
        resp = create(self.store, {"name": "del-prof", "roleArns": []})
        pid = resp["profile"]["profileId"]

        delete_h = _load_handler('DeleteProfile')
        delete_h(self.store, {"profileId": pid})

        get_h = _load_handler('GetProfile')
        with pytest.raises(ResourceNotFoundException):
            get_h(self.store, {"profileId": pid})

    def test_delete_profile_not_found(self):
        delete_h = _load_handler('DeleteProfile')
        with pytest.raises(ResourceNotFoundException):
            delete_h(self.store, {"profileId": "nonexistent"})

    def test_disable_enable_profile(self):
        create = _load_handler('CreateProfile')
        resp = create(self.store, {"name": "toggle-prof", "roleArns": []})
        pid = resp["profile"]["profileId"]

        disable = _load_handler('DisableProfile')
        resp2 = disable(self.store, {"profileId": pid})
        assert resp2["profile"]["enabled"] is False

        enable = _load_handler('EnableProfile')
        resp3 = enable(self.store, {"profileId": pid})
        assert resp3["profile"]["enabled"] is True

    def test_list_profiles(self):
        create = _load_handler('CreateProfile')
        create(self.store, {"name": "list-1", "roleArns": []})
        create(self.store, {"name": "list-2", "roleArns": []})

        list_h = _load_handler('ListProfiles')
        resp = list_h(self.store, {})
        assert len(resp["profiles"]) >= 2


class TestTrustAnchor:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = RolesAnywhereStore()
        return self._store

    def test_create_trust_anchor(self):
        handler = _load_handler('CreateTrustAnchor')
        resp = handler(self.store, {
            "name": "test-ta",
            "source": {"sourceType": "CERTIFICATE_BUNDLE"},
        })
        assert "trustAnchor" in resp
        assert resp["trustAnchor"]["name"] == "test-ta"

    def test_get_trust_anchor(self):
        create = _load_handler('CreateTrustAnchor')
        resp = create(self.store, {"name": "get-ta", "source": {"sourceType": "CERTIFICATE_BUNDLE"}})
        tid = resp["trustAnchor"]["trustAnchorId"]

        get_h = _load_handler('GetTrustAnchor')
        resp2 = get_h(self.store, {"trustAnchorId": tid})
        assert resp2["trustAnchor"]["name"] == "get-ta"

    def test_get_trust_anchor_not_found(self):
        get_h = _load_handler('GetTrustAnchor')
        with pytest.raises(ResourceNotFoundException):
            get_h(self.store, {"trustAnchorId": "nonexistent"})

    def test_update_trust_anchor(self):
        create = _load_handler('CreateTrustAnchor')
        resp = create(self.store, {"name": "upd-ta", "source": {"sourceType": "CERTIFICATE_BUNDLE"}})
        tid = resp["trustAnchor"]["trustAnchorId"]

        upd = _load_handler('UpdateTrustAnchor')
        resp2 = upd(self.store, {"trustAnchorId": tid, "name": "updated-ta"})
        assert resp2["trustAnchor"]["name"] == "updated-ta"

    def test_disable_enable_trust_anchor(self):
        create = _load_handler('CreateTrustAnchor')
        resp = create(self.store, {"name": "toggle-ta", "source": {"sourceType": "CERTIFICATE_BUNDLE"}})
        tid = resp["trustAnchor"]["trustAnchorId"]

        disable = _load_handler('DisableTrustAnchor')
        resp2 = disable(self.store, {"trustAnchorId": tid})
        assert resp2["trustAnchor"]["enabled"] is False

        enable = _load_handler('EnableTrustAnchor')
        resp3 = enable(self.store, {"trustAnchorId": tid})
        assert resp3["trustAnchor"]["enabled"] is True

    def test_delete_trust_anchor(self):
        create = _load_handler('CreateTrustAnchor')
        resp = create(self.store, {"name": "del-ta", "source": {"sourceType": "CERTIFICATE_BUNDLE"}})
        tid = resp["trustAnchor"]["trustAnchorId"]

        delete_h = _load_handler('DeleteTrustAnchor')
        delete_h(self.store, {"trustAnchorId": tid})

        get_h = _load_handler('GetTrustAnchor')
        with pytest.raises(ResourceNotFoundException):
            get_h(self.store, {"trustAnchorId": tid})

    def test_list_trust_anchors(self):
        create = _load_handler('CreateTrustAnchor')
        create(self.store, {"name": "ta-1", "source": {"sourceType": "CERTIFICATE_BUNDLE"}})
        create(self.store, {"name": "ta-2", "source": {"sourceType": "CERTIFICATE_BUNDLE"}})

        list_h = _load_handler('ListTrustAnchors')
        resp = list_h(self.store, {})
        assert len(resp["trustAnchors"]) >= 2


class TestCrl:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = RolesAnywhereStore()
        return self._store

    def test_import_crl(self):
        handler = _load_handler('ImportCrl')
        resp = handler(self.store, {
            "name": "test-crl",
            "crlData": "base64-encoded-crl-data",
        })
        assert "crl" in resp
        assert resp["crl"]["name"] == "test-crl"

    def test_get_crl(self):
        import_h = _load_handler('ImportCrl')
        resp = import_h(self.store, {"name": "get-crl", "crlData": "data"})
        cid = resp["crl"]["crlId"]

        get_h = _load_handler('GetCrl')
        resp2 = get_h(self.store, {"crlId": cid})
        assert resp2["crl"]["name"] == "get-crl"

    def test_get_crl_not_found(self):
        get_h = _load_handler('GetCrl')
        with pytest.raises(ResourceNotFoundException):
            get_h(self.store, {"crlId": "nonexistent"})

    def test_update_crl(self):
        import_h = _load_handler('ImportCrl')
        resp = import_h(self.store, {"name": "upd-crl", "crlData": "old"})
        cid = resp["crl"]["crlId"]

        upd = _load_handler('UpdateCrl')
        resp2 = upd(self.store, {"crlId": cid, "name": "updated-crl"})
        assert resp2["crl"]["name"] == "updated-crl"

    def test_delete_crl(self):
        import_h = _load_handler('ImportCrl')
        resp = import_h(self.store, {"name": "del-crl", "crlData": "data"})
        cid = resp["crl"]["crlId"]

        delete_h = _load_handler('DeleteCrl')
        delete_h(self.store, {"crlId": cid})

        get_h = _load_handler('GetCrl')
        with pytest.raises(ResourceNotFoundException):
            get_h(self.store, {"crlId": cid})

    def test_disable_enable_crl(self):
        import_h = _load_handler('ImportCrl')
        resp = import_h(self.store, {"name": "toggle-crl", "crlData": "data"})
        cid = resp["crl"]["crlId"]

        disable = _load_handler('DisableCrl')
        resp2 = disable(self.store, {"crlId": cid})
        assert resp2["crl"]["enabled"] is False

        enable = _load_handler('EnableCrl')
        resp3 = enable(self.store, {"crlId": cid})
        assert resp3["crl"]["enabled"] is True

    def test_list_crls(self):
        import_h = _load_handler('ImportCrl')
        import_h(self.store, {"name": "crl-1", "crlData": "d1"})
        import_h(self.store, {"name": "crl-2", "crlData": "d2"})

        list_h = _load_handler('ListCrls')
        resp = list_h(self.store, {})
        assert len(resp["crls"]) >= 2


class TestAttributeMappingNotification:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = RolesAnywhereStore()
        return self._store

    def _create_profile(self):
        create = _load_handler('CreateProfile')
        resp = create(self.store, {"name": "attr-prof", "roleArns": []})
        return resp["profile"]["profileId"]

    def test_put_attribute_mapping(self):
        pid = self._create_profile()
        handler = _load_handler('PutAttributeMapping')
        resp = handler(self.store, {
            "profileId": pid,
            "certificateField": "CN",
            "mappingRules": [{"field": "subject.CN"}],
        })
        assert resp["profileId"] == pid

    def test_delete_attribute_mapping(self):
        pid = self._create_profile()
        put_h = _load_handler('PutAttributeMapping')
        put_h(self.store, {"profileId": pid, "certificateField": "CN", "mappingRules": []})

        del_h = _load_handler('DeleteAttributeMapping')
        del_h(self.store, {"profileId": pid, "certificateField": "CN"})

    def test_put_notification_settings(self):
        handler = _load_handler('PutNotificationSettings')
        resp = handler(self.store, {"enabled": True, "channel": "ALL", "threshold": 0, "eventTypes": []})
        assert resp["enabled"] is True

    def test_reset_notification_settings(self):
        put_h = _load_handler('PutNotificationSettings')
        put_h(self.store, {"enabled": True})

        reset_h = _load_handler('ResetNotificationSettings')
        reset_h(self.store, {})


class TestTags:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = RolesAnywhereStore()
        return self._store

    def _create_profile(self):
        create = _load_handler('CreateProfile')
        resp = create(self.store, {"name": "tag-prof", "roleArns": []})
        return resp["profile"]["profileArn"]

    def test_tag_and_list(self):
        arn = self._create_profile()
        tag_h = _load_handler('TagResource')
        tag_h(self.store, {"resourceArn": arn, "tags": [{"key": "team", "value": "platform"}]})

        list_h = _load_handler('ListTagsForResource')
        resp = list_h(self.store, {"resourceArn": arn})
        assert resp["tags"]["team"] == "platform"

    def test_untag(self):
        arn = self._create_profile()
        tag_h = _load_handler('TagResource')
        tag_h(self.store, {"resourceArn": arn, "tags": [{"key": "tmp", "value": "x"}]})

        untag_h = _load_handler('UntagResource')
        untag_h(self.store, {"resourceArn": arn, "tagKeys": ["tmp"]})

        list_h = _load_handler('ListTagsForResource')
        resp = list_h(self.store, {"resourceArn": arn})
        assert "tmp" not in resp["tags"]
