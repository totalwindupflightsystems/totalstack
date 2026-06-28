"""Integration test for Identity Store."""
import pytest
import os
import importlib.util
import types

AD = os.path.dirname(__file__)
SD = os.path.join(AD, '..', 'identitystore')
ms = importlib.util.spec_from_file_location('models', os.path.join(SD, 'models.code.py'))
mm = importlib.util.module_from_spec(ms)
ms.loader.exec_module(mm)
Store = mm.IdentityStoreStore
RNF = mm.ResourceNotFoundException

def _h(name):
    p = os.path.join(SD, name + '.code.py')
    s = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(s)
    m.ResourceNotFoundException = RNF
    s.loader.exec_module(m)
    for v in m.__dict__.values():
        if isinstance(v, types.FunctionType) and not v.__name__.startswith('_'):
            return v

SID = "d-9067b8a90b"
class TestUser:
    _s = None
    @property
    def store(self):
        if self._s is None: self._s = Store()
        return self._s

    def test_create(self):
        r = _h('create-user')(self.store, {"identityStoreId": SID, "userName": "alice"})
        assert r["userId"]
    def test_describe(self):
        r = _h('create-user')(self.store, {"identityStoreId": SID, "userName": "bob"})
        r2 = _h('describe-user')(self.store, {"identityStoreId": SID, "userId": r["userId"]})
        assert r2["userName"] == "bob"
    def test_describe_nonexistent(self):
        with pytest.raises(RNF): _h('describe-user')(self.store, {"identityStoreId": SID, "userId": "nope"})
    def test_delete(self):
        r = _h('create-user')(self.store, {"identityStoreId": SID, "userName": "delme"})
        _h('delete-user')(self.store, {"identityStoreId": SID, "userId": r["userId"]})
        with pytest.raises(RNF): _h('describe-user')(self.store, {"identityStoreId": SID, "userId": r["userId"]})
    def test_list(self):
        _h('create-user')(self.store, {"identityStoreId": SID, "userName": "u1"})
        _h('create-user')(self.store, {"identityStoreId": SID, "userName": "u2"})
        r = _h('list-users')(self.store, {"identityStoreId": SID})
        assert len(r["users"]) >= 2

class TestGroup:
    _s = None
    @property
    def store(self):
        if self._s is None: self._s = Store()
        return self._s

    def test_create(self):
        r = _h('create-group')(self.store, {"identityStoreId": SID, "displayName": "Admins"})
        assert r["groupId"]
    def test_describe(self):
        r = _h('create-group')(self.store, {"identityStoreId": SID, "displayName": "Devs"})
        r2 = _h('describe-group')(self.store, {"identityStoreId": SID, "groupId": r["groupId"]})
        assert r2["displayName"] == "Devs"
    def test_delete(self):
        r = _h('create-group')(self.store, {"identityStoreId": SID, "displayName": "Temp"})
        _h('delete-group')(self.store, {"identityStoreId": SID, "groupId": r["groupId"]})
        with pytest.raises(RNF): _h('describe-group')(self.store, {"identityStoreId": SID, "groupId": r["groupId"]})
    def test_list(self):
        _h('create-group')(self.store, {"identityStoreId": SID, "displayName": "G1"})
        r = _h('list-groups')(self.store, {"identityStoreId": SID})
        assert len(r["groups"]) >= 1

class TestMembership:
    _s = None
    @property
    def store(self):
        if self._s is None: self._s = Store()
        return self._s

    def test_create(self):
        u = _h('create-user')(self.store, {"identityStoreId": SID, "userName": "memuser"})
        g = _h('create-group')(self.store, {"identityStoreId": SID, "displayName": "MemGroup"})
        r = _h('create-group-membership')(self.store, {"identityStoreId": SID, "groupId": g["groupId"], "memberId": u["userId"]})
        assert r["membershipId"]
    def test_describe(self):
        u = _h('create-user')(self.store, {"identityStoreId": SID, "userName": "duser"})
        g = _h('create-group')(self.store, {"identityStoreId": SID, "displayName": "DGroup"})
        r = _h('create-group-membership')(self.store, {"identityStoreId": SID, "groupId": g["groupId"], "memberId": u["userId"]})
        r2 = _h('describe-group-membership')(self.store, {"identityStoreId": SID, "membershipId": r["membershipId"]})
        assert r2["groupId"] == g["groupId"]
    def test_delete(self):
        u = _h('create-user')(self.store, {"identityStoreId": SID, "userName": "xuser"})
        g = _h('create-group')(self.store, {"identityStoreId": SID, "displayName": "XGroup"})
        r = _h('create-group-membership')(self.store, {"identityStoreId": SID, "groupId": g["groupId"], "memberId": u["userId"]})
        _h('delete-group-membership')(self.store, {"identityStoreId": SID, "membershipId": r["membershipId"]})
        with pytest.raises(RNF): _h('describe-group-membership')(self.store, {"identityStoreId": SID, "membershipId": r["membershipId"]})
    def test_list_by_group(self):
        u = _h('create-user')(self.store, {"identityStoreId": SID, "userName": "luser"})
        g = _h('create-group')(self.store, {"identityStoreId": SID, "displayName": "LGroup"})
        _h('create-group-membership')(self.store, {"identityStoreId": SID, "groupId": g["groupId"], "memberId": u["userId"]})
        r = _h('list-group-memberships')(self.store, {"identityStoreId": SID, "groupId": g["groupId"]})
        assert len(r["groupMemberships"]) == 1
    def test_list_for_member(self):
        u = _h('create-user')(self.store, {"identityStoreId": SID, "userName": "fuser"})
        g = _h('create-group')(self.store, {"identityStoreId": SID, "displayName": "FGroup"})
        _h('create-group-membership')(self.store, {"identityStoreId": SID, "groupId": g["groupId"], "memberId": u["userId"]})
        r = _h('list-group-memberships-for-member')(self.store, {"identityStoreId": SID, "memberId": u["userId"]})
        assert len(r["groupMemberships"]) == 1
    def test_is_member(self):
        u = _h('create-user')(self.store, {"identityStoreId": SID, "userName": "icheck"})
        g = _h('create-group')(self.store, {"identityStoreId": SID, "displayName": "ICheck"})
        _h('create-group-membership')(self.store, {"identityStoreId": SID, "groupId": g["groupId"], "memberId": u["userId"]})
        r = _h('is-member-in-groups')(self.store, {"identityStoreId": SID, "memberId": u["userId"], "groupIds": [g["groupId"], "nonexistent"]})
        assert r["results"][0]["membershipExists"] is True
        assert r["results"][1]["membershipExists"] is False
