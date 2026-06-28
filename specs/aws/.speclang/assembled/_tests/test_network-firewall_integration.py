"""Integration test for Network Firewall — real store."""
import os
import importlib.util
import types
import time as _time

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'network-firewall')

models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

NetworkFirewallStore = models_mod.NetworkFirewallStore
InvalidRequestException = models_mod.InvalidRequestException
ResourceNotFoundException = models_mod.ResourceNotFoundException

skip_names = {'time', 'uuid', '<lambda>', 'dataclass'}


def _load_handler(op_name):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.InvalidRequestException = InvalidRequestException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.InternalServerError = models_mod.InternalServerError
    mod.ThrottlingException = models_mod.ThrottlingException
    mod.LimitExceededException = models_mod.LimitExceededException
    mod.time = _time
    mod.uuid = __import__('uuid')
    spec.loader.exec_module(mod)
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            return v
    raise RuntimeError(f"No handler found in {op_name}")


class TestFirewallIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = NetworkFirewallStore()
        return self._store

    def _create_fw(self, name="test-fw"):
        h = _load_handler('create-firewall')
        return h(self.store, {
            "FirewallName": name,
            "FirewallPolicyArn": "arn:aws:network-firewall:us-east-1:000000000000:firewall-policy/test-arn",
        })

    def test_create_firewall_happy(self):
        resp = self._create_fw()
        assert resp["Firewall"]["FirewallName"] == "test-fw"
        assert "FirewallArn" in resp["Firewall"]

    def test_create_firewall_duplicate(self):
        self._create_fw("dup-fw")
        with __import__('pytest').raises(InvalidRequestException):
            self._create_fw("dup-fw")

    def test_describe_firewall_happy(self):
        resp = self._create_fw("desc-fw")
        arn = resp["Firewall"]["FirewallArn"]
        h = _load_handler('describe-firewall')
        resp2 = h(self.store, {"FirewallArn": arn})
        assert resp2["Firewall"]["FirewallName"] == "desc-fw"

    def test_describe_firewall_nonexistent(self):
        h = _load_handler('describe-firewall')
        with __import__('pytest').raises(ResourceNotFoundException):
            h(self.store, {"FirewallArn": "arn:nonexistent"})

    def test_delete_firewall_happy(self):
        resp = self._create_fw("del-fw")
        arn = resp["Firewall"]["FirewallArn"]
        h = _load_handler('delete-firewall')
        h(self.store, {"FirewallArn": arn})
        h2 = _load_handler('describe-firewall')
        with __import__('pytest').raises(ResourceNotFoundException):
            h2(self.store, {"FirewallArn": arn})

    def test_list_firewalls(self):
        self._create_fw("list-fw1")
        self._create_fw("list-fw2")
        h = _load_handler('list-firewalls')
        resp = h(self.store, {})
        assert len(resp["Firewalls"]) >= 2

    def test_update_delete_protection(self):
        resp = self._create_fw("prot-fw")
        arn = resp["Firewall"]["FirewallArn"]
        h = _load_handler('update-firewall-delete-protection')
        resp2 = h(self.store, {"FirewallArn": arn, "DeleteProtection": True})
        assert resp2["DeleteProtection"] is True

    def test_update_description(self):
        resp = self._create_fw("desc-prot-fw")
        arn = resp["Firewall"]["FirewallArn"]
        h = _load_handler('update-firewall-description')
        resp2 = h(self.store, {"FirewallArn": arn, "Description": "test desc"})
        assert resp2["Description"] == "test desc"


class TestFirewallPolicyIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = NetworkFirewallStore()
        return self._store

    def _create_policy(self, name="test-policy"):
        h = _load_handler('create-firewall-policy')
        return h(self.store, {
            "FirewallPolicyName": name,
            "FirewallPolicy": {
                "StatelessDefaultActions": ["aws:forward_to_sfe"],
                "StatelessFragmentDefaultActions": ["aws:forward_to_sfe"],
            },
        })

    def test_create_policy_happy(self):
        resp = self._create_policy()
        assert resp["FirewallPolicyResponse"]["FirewallPolicyName"] == "test-policy"

    def test_create_policy_duplicate(self):
        self._create_policy("dup-pol")
        with __import__('pytest').raises(InvalidRequestException):
            self._create_policy("dup-pol")

    def test_describe_policy_happy(self):
        resp = self._create_policy("desc-pol")
        arn = resp["FirewallPolicyResponse"]["FirewallPolicyArn"]
        h = _load_handler('describe-firewall-policy')
        resp2 = h(self.store, {"FirewallPolicyArn": arn})
        assert resp2["FirewallPolicyResponse"]["FirewallPolicyName"] == "desc-pol"

    def test_describe_policy_nonexistent(self):
        h = _load_handler('describe-firewall-policy')
        with __import__('pytest').raises(ResourceNotFoundException):
            h(self.store, {"FirewallPolicyArn": "arn:nonexistent"})

    def test_update_policy_happy(self):
        resp = self._create_policy("upd-pol")
        arn = resp["FirewallPolicyResponse"]["FirewallPolicyArn"]
        h = _load_handler('update-firewall-policy')
        resp2 = h(self.store, {
            "UpdateToken": "token",
            "FirewallPolicyArn": arn,
            "FirewallPolicy": {
                "StatelessDefaultActions": ["aws:drop"],
                "StatelessFragmentDefaultActions": ["aws:drop"],
            },
            "Description": "updated",
        })
        assert resp2["FirewallPolicyResponse"]["Description"] == "updated"

    def test_list_policies(self):
        self._create_policy("pol-a")
        self._create_policy("pol-b")
        h = _load_handler('list-firewall-policies')
        resp = h(self.store, {})
        assert len(resp["FirewallPolicies"]) >= 2

    def test_delete_policy_happy(self):
        resp = self._create_policy("del-pol")
        arn = resp["FirewallPolicyResponse"]["FirewallPolicyArn"]
        h = _load_handler('delete-firewall-policy')
        h(self.store, {"FirewallPolicyArn": arn})
        h2 = _load_handler('describe-firewall-policy')
        with __import__('pytest').raises(ResourceNotFoundException):
            h2(self.store, {"FirewallPolicyArn": arn})


class TestRuleGroupIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = NetworkFirewallStore()
        return self._store

    def _create_rg(self, name="test-rg", type_="STATELESS"):
        h = _load_handler('create-rule-group')
        return h(self.store, {
            "RuleGroupName": name,
            "Type": type_,
            "Capacity": 100,
        })

    def test_create_rule_group_happy(self):
        resp = self._create_rg()
        assert resp["RuleGroupResponse"]["RuleGroupName"] == "test-rg"
        assert resp["RuleGroupResponse"]["Type"] == "STATELESS"

    def test_create_rule_group_duplicate_same_type(self):
        self._create_rg("dup-rg", "STATELESS")
        with __import__('pytest').raises(InvalidRequestException):
            self._create_rg("dup-rg", "STATELESS")

    def test_describe_rule_group_happy(self):
        resp = self._create_rg("desc-rg")
        arn = resp["RuleGroupResponse"]["RuleGroupArn"]
        h = _load_handler('describe-rule-group')
        resp2 = h(self.store, {"RuleGroupArn": arn})
        assert resp2["RuleGroupResponse"]["RuleGroupName"] == "desc-rg"

    def test_describe_rule_group_nonexistent(self):
        h = _load_handler('describe-rule-group')
        with __import__('pytest').raises(ResourceNotFoundException):
            h(self.store, {"RuleGroupArn": "arn:nonexistent"})

    def test_update_rule_group_happy(self):
        resp = self._create_rg("upd-rg")
        arn = resp["RuleGroupResponse"]["RuleGroupArn"]
        h = _load_handler('update-rule-group')
        resp2 = h(self.store, {
            "UpdateToken": "token",
            "RuleGroupArn": arn,
            "RuleGroup": {"RulesSource": {"StatelessRulesAndCustomActions": {}}},
            "Description": "updated desc",
        })
        assert resp2["RuleGroupResponse"]["Description"] == "updated desc"

    def test_list_rule_groups(self):
        self._create_rg("rg-a")
        self._create_rg("rg-b")
        h = _load_handler('list-rule-groups')
        resp = h(self.store, {})
        assert len(resp["RuleGroups"]) >= 2

    def test_delete_rule_group_happy(self):
        resp = self._create_rg("del-rg")
        arn = resp["RuleGroupResponse"]["RuleGroupArn"]
        h = _load_handler('delete-rule-group')
        h(self.store, {"RuleGroupArn": arn})
        h2 = _load_handler('describe-rule-group')
        with __import__('pytest').raises(ResourceNotFoundException):
            h2(self.store, {"RuleGroupArn": arn})


class TestTagsIntegration:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = NetworkFirewallStore()
        return self._store

    def _create_fw(self):
        h = _load_handler('create-firewall')
        return h(self.store, {
            "FirewallName": "tag-fw",
            "FirewallPolicyArn": "arn:aws:network-firewall:us-east-1:000000000000:firewall-policy/test",
            "Tags": [{"Key": "env", "Value": "test"}],
        })

    def test_tag_resource(self):
        resp = self._create_fw()
        arn = resp["Firewall"]["FirewallArn"]
        h = _load_handler('tag-resource')
        h(self.store, {"ResourceArn": arn, "Tags": [{"Key": "team", "Value": "net"}]})
        h2 = _load_handler('list-tags-for-resource')
        resp2 = h2(self.store, {"ResourceArn": arn})
        tags = {t["Key"]: t["Value"] for t in resp2["Tags"]}
        assert tags.get("team") == "net"
        assert tags.get("env") == "test"

    def test_list_tags(self):
        resp = self._create_fw()
        arn = resp["Firewall"]["FirewallArn"]
        h = _load_handler('list-tags-for-resource')
        resp2 = h(self.store, {"ResourceArn": arn})
        tags = {t["Key"]: t["Value"] for t in resp2["Tags"]}
        assert tags["env"] == "test"

    def test_untag_resource(self):
        resp = self._create_fw()
        arn = resp["Firewall"]["FirewallArn"]
        h = _load_handler('tag-resource')
        h(self.store, {"ResourceArn": arn, "Tags": [{"Key": "tmp", "Value": "x"}]})
        h2 = _load_handler('untag-resource')
        h2(self.store, {"ResourceArn": arn, "TagKeys": ["tmp"]})
        h3 = _load_handler('list-tags-for-resource')
        resp3 = h3(self.store, {"ResourceArn": arn})
        tags = {t["Key"]: t["Value"] for t in resp3["Tags"]}
        assert "tmp" not in tags
        assert tags["env"] == "test"
