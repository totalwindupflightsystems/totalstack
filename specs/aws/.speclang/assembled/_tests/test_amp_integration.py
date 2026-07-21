"""Integration test for AMP (Amazon Managed Prometheus) — real store."""
import pytest
import os
import importlib.util
import types
import time as _time
import uuid as _uuid

ASSEMBLED_DIR = os.path.dirname(__file__)
SERVICE_DIR = os.path.join(ASSEMBLED_DIR, '..', 'amp')

# Load the models module dynamically
models_spec = importlib.util.spec_from_file_location(
    'models', os.path.join(SERVICE_DIR, 'models.code.py'))
models_mod = importlib.util.module_from_spec(models_spec)
models_spec.loader.exec_module(models_mod)

AMPStore = models_mod.AMPStore
WorkspaceRecord = models_mod.WorkspaceRecord
ScraperRecord = models_mod.ScraperRecord
RuleGroupsNamespaceRecord = models_mod.RuleGroupsNamespaceRecord
AlertManagerDefinitionRecord = models_mod.AlertManagerDefinitionRecord
Destination = models_mod.Destination
AMPConfiguration = models_mod.AMPConfiguration
RoleConfiguration = models_mod.RoleConfiguration
ScrapeConfiguration = models_mod.ScrapeConfiguration
Source = models_mod.Source
EksConfiguration = models_mod.EksConfiguration
InvalidParameterException = models_mod.InvalidParameterException
ResourceNotFoundException = models_mod.ResourceNotFoundException
ConflictException = models_mod.ConflictException
ValidationException = models_mod.ValidationException

skip_names = {'dataclass', 'time', 'uuid', '<lambda>'}


def _load_handler(op_name, globals_inject=None):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.InvalidParameterException = InvalidParameterException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ConflictException = ConflictException
    mod.ValidationException = ValidationException
    mod.WorkspaceRecord = WorkspaceRecord
    mod.ScraperRecord = ScraperRecord
    mod.RuleGroupsNamespaceRecord = RuleGroupsNamespaceRecord
    mod.AlertManagerDefinitionRecord = AlertManagerDefinitionRecord
    mod.Destination = Destination
    mod.AMPConfiguration = AMPConfiguration
    mod.RoleConfiguration = RoleConfiguration
    mod.ScrapeConfiguration = ScrapeConfiguration
    mod.Source = Source
    mod.EksConfiguration = EksConfiguration
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    handler = None
    for v in mod.__dict__.values():
        if (isinstance(v, types.FunctionType)
                and not v.__name__.startswith('_')
                and v.__name__ not in skip_names):
            handler = v
            break
    return handler


def _load_module(op_name, globals_inject=None):
    path = os.path.join(SERVICE_DIR, op_name + '.code.py')
    spec = importlib.util.spec_from_file_location(op_name, path)
    mod = importlib.util.module_from_spec(spec)
    mod.InvalidParameterException = InvalidParameterException
    mod.ResourceNotFoundException = ResourceNotFoundException
    mod.ConflictException = ConflictException
    mod.ValidationException = ValidationException
    mod.WorkspaceRecord = WorkspaceRecord
    mod.ScraperRecord = ScraperRecord
    mod.RuleGroupsNamespaceRecord = RuleGroupsNamespaceRecord
    mod.AlertManagerDefinitionRecord = AlertManagerDefinitionRecord
    mod.Destination = Destination
    mod.AMPConfiguration = AMPConfiguration
    mod.RoleConfiguration = RoleConfiguration
    mod.ScrapeConfiguration = ScrapeConfiguration
    mod.Source = Source
    mod.EksConfiguration = EksConfiguration
    mod.time = _time
    mod.uuid = _uuid
    mod.dataclass = lambda f: f
    if globals_inject:
        for name, value in globals_inject.items():
            setattr(mod, name, value)
    spec.loader.exec_module(mod)
    return mod


# ══════════════════════════════════════════════════════════════════════
# Workspace Tests
# ══════════════════════════════════════════════════════════════════════

class TestWorkspace:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AMPStore()
        return self._store

    def test_create_workspace_happy(self):
        handler = _load_handler('create-workspace')
        resp = handler(self.store, {'alias': 'test-ws'})
        assert resp is not None
        assert 'workspaceId' in resp
        assert resp['alias'] == 'test-ws'
        assert resp['status']['statusCode'] == 'ACTIVE'

    def test_create_workspace_minimal(self):
        handler = _load_handler('create-workspace')
        resp = handler(self.store, {})
        assert resp is not None
        assert 'workspaceId' in resp
        assert resp['status']['statusCode'] == 'ACTIVE'

    def test_describe_workspace(self):
        create = _load_handler('create-workspace')
        describe = _load_handler('describe-workspace')
        created = create(self.store, {'alias': 'desc-test'})
        resp = describe(self.store, {'workspaceId': created['workspaceId']})
        assert resp['workspaceId'] == created['workspaceId']
        assert resp['alias'] == 'desc-test'

    def test_describe_workspace_not_found(self):
        describe = _load_handler('describe-workspace')
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {'workspaceId': 'ws-nonexistent'})

    def test_delete_workspace(self):
        create = _load_handler('create-workspace')
        delete = _load_handler('delete-workspace')
        describe = _load_handler('describe-workspace')
        created = create(self.store, {'alias': 'del-test'})
        delete(self.store, {'workspaceId': created['workspaceId']})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {'workspaceId': created['workspaceId']})

    def test_delete_workspace_not_found(self):
        delete = _load_handler('delete-workspace')
        with pytest.raises(ResourceNotFoundException):
            delete(self.store, {'workspaceId': 'ws-nonexistent'})

    def test_list_workspaces(self):
        create = _load_handler('create-workspace')
        list_handler = _load_handler('list-workspaces')
        create(self.store, {'alias': 'ws1'})
        create(self.store, {'alias': 'ws2'})
        resp = list_handler(self.store, {})
        assert 'workspaces' in resp
        assert len(resp['workspaces']) >= 2

    def test_update_workspace_alias(self):
        create = _load_handler('create-workspace')
        update = _load_handler('update-workspace-alias')
        describe = _load_handler('describe-workspace')
        created = create(self.store, {'alias': 'old-alias'})
        update(self.store, {'workspaceId': created['workspaceId'], 'alias': 'new-alias'})
        resp = describe(self.store, {'workspaceId': created['workspaceId']})
        assert resp['alias'] == 'new-alias'


# ══════════════════════════════════════════════════════════════════════
# Scraper Tests
# ══════════════════════════════════════════════════════════════════════

class TestScraper:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AMPStore()
        return self._store

    def _create_workspace(self):
        handler = _load_handler('create-workspace')
        return handler(self.store, {'alias': 'scraper-ws'})

    def _scraper_request(self, workspaceId):
        return {
            'alias': 'test-scraper',
            'destination': {
                'ampConfiguration': {
                    'workspaceArn': f'arn:aws:prometheus:us-east-1:000000000000:workspace/{workspaceId}'
                }
            },
            'roleConfiguration': {
                'sourceRoleArn': 'arn:aws:iam::000000000000:role/source',
                'targetRoleArn': 'arn:aws:iam::000000000000:role/target',
            },
            'scrapeConfiguration': {'configurationBlob': 'base64blob'},
            'source': {
                'eksConfiguration': {
                    'clusterArn': 'arn:aws:eks:us-east-1:000000000000:cluster/test',
                    'subnetIds': ['subnet-123'],
                }
            },
        }

    def test_create_scraper_happy(self):
        ws = self._create_workspace()
        handler = _load_handler('create-scraper')
        resp = handler(self.store, self._scraper_request(ws['workspaceId']))
        assert resp is not None
        assert 'scraperId' in resp
        assert resp['alias'] == 'test-scraper'
        assert resp['status']['statusCode'] == 'ACTIVE'

    def test_describe_scraper(self):
        ws = self._create_workspace()
        create = _load_handler('create-scraper')
        describe = _load_handler('describe-scraper')
        created = create(self.store, self._scraper_request(ws['workspaceId']))
        resp = describe(self.store, {'scraperId': created['scraperId']})
        assert resp['scraperId'] == created['scraperId']

    def test_describe_scraper_not_found(self):
        describe = _load_handler('describe-scraper')
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {'scraperId': 's-nonexistent'})

    def test_delete_scraper(self):
        ws = self._create_workspace()
        create = _load_handler('create-scraper')
        delete = _load_handler('delete-scraper')
        describe = _load_handler('describe-scraper')
        created = create(self.store, self._scraper_request(ws['workspaceId']))
        delete(self.store, {'scraperId': created['scraperId']})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {'scraperId': created['scraperId']})

    def test_list_scrapers(self):
        ws = self._create_workspace()
        create = _load_handler('create-scraper')
        list_handler = _load_handler('list-scrapers')
        create(self.store, self._scraper_request(ws['workspaceId']))
        resp = list_handler(self.store, {})
        assert 'scrapers' in resp
        assert len(resp['scrapers']) >= 1

    def test_update_scraper(self):
        ws = self._create_workspace()
        create = _load_handler('create-scraper')
        update = _load_handler('update-scraper')
        describe = _load_handler('describe-scraper')
        created = create(self.store, self._scraper_request(ws['workspaceId']))
        update(self.store, {'scraperId': created['scraperId'], 'alias': 'updated-scraper'})
        resp = describe(self.store, {'scraperId': created['scraperId']})
        assert resp['alias'] == 'updated-scraper'

    def test_get_default_scraper_configuration(self):
        handler = _load_handler('get-default-scraper-configuration')
        resp = handler(self.store, {})
        assert resp is not None
        assert 'configuration' in resp


# ══════════════════════════════════════════════════════════════════════
# Rule Groups Namespace Tests
# ══════════════════════════════════════════════════════════════════════

class TestRuleGroupsNamespace:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AMPStore()
        return self._store

    def _create_workspace_and_rule(self):
        create_ws = _load_handler('create-workspace')
        ws = create_ws(self.store, {'alias': 'rule-ws'})
        create_rg = _load_handler('create-rule-groups-namespace')
        rg = create_rg(self.store, {
            'workspaceId': ws['workspaceId'],
            'name': 'test-rules',
            'data': b'groups:\n  - name: test\n',
        })
        return ws, rg

    def test_create_rule_groups_namespace_happy(self):
        create_ws = _load_handler('create-workspace')
        ws = create_ws(self.store, {'alias': 'rule-ws'})
        handler = _load_handler('create-rule-groups-namespace')
        resp = handler(self.store, {
            'workspaceId': ws['workspaceId'],
            'name': 'my-rules',
            'data': b'groups:\n  - name: alerts\n    rules:\n      - alert: HighCPU\n',
        })
        assert resp is not None
        assert resp['name'] == 'my-rules'
        assert resp['status']['statusCode'] == 'ACTIVE'

    def test_create_rule_groups_duplicate(self):
        ws, _ = self._create_workspace_and_rule()
        handler = _load_handler('create-rule-groups-namespace')
        with pytest.raises(ConflictException):
            handler(self.store, {
                'workspaceId': ws['workspaceId'],
                'name': 'test-rules',
                'data': b'groups:\n  - name: test\n',
            })

    def test_describe_rule_groups_namespace(self):
        ws, rg = self._create_workspace_and_rule()
        handler = _load_handler('describe-rule-groups-namespace')
        resp = handler(self.store, {
            'workspaceId': ws['workspaceId'],
            'name': 'test-rules',
        })
        assert resp['name'] == 'test-rules'

    def test_describe_rule_groups_not_found(self):
        create_ws = _load_handler('create-workspace')
        ws = create_ws(self.store, {'alias': 'rule-ws'})
        handler = _load_handler('describe-rule-groups-namespace')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {
                'workspaceId': ws['workspaceId'],
                'name': 'nonexistent',
            })

    def test_delete_rule_groups_namespace(self):
        ws, rg = self._create_workspace_and_rule()
        delete = _load_handler('delete-rule-groups-namespace')
        describe = _load_handler('describe-rule-groups-namespace')
        delete(self.store, {
            'workspaceId': ws['workspaceId'],
            'name': 'test-rules',
        })
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {
                'workspaceId': ws['workspaceId'],
                'name': 'test-rules',
            })

    def test_list_rule_groups_namespaces(self):
        ws, rg = self._create_workspace_and_rule()
        handler = _load_handler('list-rule-groups-namespaces')
        resp = handler(self.store, {'workspaceId': ws['workspaceId']})
        assert 'ruleGroupsNamespaces' in resp
        assert len(resp['ruleGroupsNamespaces']) >= 1

    def test_put_rule_groups_namespace(self):
        create_ws = _load_handler('create-workspace')
        ws = create_ws(self.store, {'alias': 'put-ws'})
        handler = _load_handler('put-rule-groups-namespace')
        resp = handler(self.store, {
            'workspaceId': ws['workspaceId'],
            'name': 'put-rules',
            'data': b'groups:\n  - name: updated\n',
        })
        assert resp['name'] == 'put-rules'
        # Put again (should update)
        resp2 = handler(self.store, {
            'workspaceId': ws['workspaceId'],
            'name': 'put-rules',
            'data': b'groups:\n  - name: updated2\n',
        })
        assert resp2['data'] == b'groups:\n  - name: updated2\n'


# ══════════════════════════════════════════════════════════════════════
# Alert Manager Definition Tests
# ══════════════════════════════════════════════════════════════════════

class TestAlertManagerDefinition:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AMPStore()
        return self._store

    def _create_workspace(self):
        handler = _load_handler('create-workspace')
        return handler(self.store, {'alias': 'alert-ws'})

    def test_create_alert_manager_happy(self):
        ws = self._create_workspace()
        handler = _load_handler('create-alert-manager-definition')
        resp = handler(self.store, {
            'workspaceId': ws['workspaceId'],
            'data': b'alertmanager_config: |\n  route:\n    receiver: default\n',
        })
        assert resp is not None
        assert resp['status']['statusCode'] == 'ACTIVE'

    def test_create_alert_manager_duplicate(self):
        ws = self._create_workspace()
        handler = _load_handler('create-alert-manager-definition')
        handler(self.store, {
            'workspaceId': ws['workspaceId'],
            'data': b'alertmanager_config: |\n',
        })
        with pytest.raises(ConflictException):
            handler(self.store, {
                'workspaceId': ws['workspaceId'],
                'data': b'alertmanager_config: |\n',
            })

    def test_describe_alert_manager(self):
        ws = self._create_workspace()
        create = _load_handler('create-alert-manager-definition')
        describe = _load_handler('describe-alert-manager-definition')
        create(self.store, {
            'workspaceId': ws['workspaceId'],
            'data': b'alertmanager_config: |\n',
        })
        resp = describe(self.store, {'workspaceId': ws['workspaceId']})
        assert resp is not None
        assert 'data' in resp

    def test_describe_alert_manager_not_found(self):
        ws = self._create_workspace()
        describe = _load_handler('describe-alert-manager-definition')
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {'workspaceId': ws['workspaceId']})

    def test_delete_alert_manager(self):
        ws = self._create_workspace()
        create = _load_handler('create-alert-manager-definition')
        delete = _load_handler('delete-alert-manager-definition')
        describe = _load_handler('describe-alert-manager-definition')
        create(self.store, {
            'workspaceId': ws['workspaceId'],
            'data': b'alertmanager_config: |\n',
        })
        delete(self.store, {'workspaceId': ws['workspaceId']})
        with pytest.raises(ResourceNotFoundException):
            describe(self.store, {'workspaceId': ws['workspaceId']})

    def test_put_alert_manager(self):
        ws = self._create_workspace()
        handler = _load_handler('put-alert-manager-definition')
        resp = handler(self.store, {
            'workspaceId': ws['workspaceId'],
            'data': b'alertmanager_config: |\n  route:\n    receiver: ops\n',
        })
        assert resp is not None
        # Put again
        resp2 = handler(self.store, {
            'workspaceId': ws['workspaceId'],
            'data': b'alertmanager_config: |\n  route:\n    receiver: dev\n',
        })
        assert b'dev' in resp2['data']


# ══════════════════════════════════════════════════════════════════════
# Tags Tests
# ══════════════════════════════════════════════════════════════════════

class TestTags:
    _store = None

    @property
    def store(self):
        if self._store is None:
            self._store = AMPStore()
        return self._store

    def _create_workspace_with_tags(self):
        handler = _load_handler('create-workspace')
        return handler(self.store, {
            'alias': 'tagged-ws',
            'tags': {'env': 'test', 'team': 'backend'}
        })

    def test_list_tags_for_resource(self):
        ws = self._create_workspace_with_tags()
        handler = _load_handler('list-tags-for-resource')
        resp = handler(self.store, {'resourceArn': ws['arn']})
        assert 'tags' in resp
        assert resp['tags']['env'] == 'test'
        assert resp['tags']['team'] == 'backend'

    def test_tag_resource(self):
        ws = self._create_workspace_with_tags()
        handler = _load_handler('tag-resource')
        handler(self.store, {
            'resourceArn': ws['arn'],
            'tags': [{'key': 'project', 'value': 'amp'}],
        })
        list_tags = _load_handler('list-tags-for-resource')
        resp = list_tags(self.store, {'resourceArn': ws['arn']})
        assert resp['tags']['project'] == 'amp'
        assert resp['tags']['env'] == 'test'

    def test_untag_resource(self):
        ws = self._create_workspace_with_tags()
        handler = _load_handler('untag-resource')
        handler(self.store, {
            'resourceArn': ws['arn'],
            'tagKeys': ['team'],
        })
        list_tags = _load_handler('list-tags-for-resource')
        resp = list_tags(self.store, {'resourceArn': ws['arn']})
        assert 'team' not in resp['tags']
        assert resp['tags']['env'] == 'test'

    def test_list_tags_for_resource_not_found(self):
        handler = _load_handler('list-tags-for-resource')
        with pytest.raises(ResourceNotFoundException):
            handler(self.store, {'resourceArn': 'arn:aws:prometheus:us-east-1:000000000000:workspace/ws-nonexistent'})
