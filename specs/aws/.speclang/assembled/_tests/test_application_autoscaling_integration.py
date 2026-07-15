import os
import importlib.util
import types
import pytest
A = os.path.dirname(__file__)
AD = os.path.dirname(__file__)
S = os.path.join(os.path.dirname(__file__), '..', 'application-autoscaling')
ms = importlib.util.spec_from_file_location('m', os.path.join(S, 'models.code.py'))
mm = importlib.util.module_from_spec(ms); ms.loader.exec_module(mm)
AS = mm.AppAutoScalingStore
RNF = mm.ResourceNotFoundException
AEF = mm.AlreadyExistsFault
def L(n):
    p = os.path.join(S, n + '.code.py')
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    for v in m.__dict__.values():
        if isinstance(v, types.FunctionType) and not v.__name__.startswith('_') and v.__name__ != '<lambda>': return v

class TestAAS:
    @pytest.fixture
    def store(self): return AS()
    def test_register(self, store):
        L('registerscalabletarget')(store, {'ResourceId': 'table/test', 'ServiceNamespace': 'dynamodb', 'ScalableDimension': 'dynamodb:table:WriteCapacityUnits', 'MinCapacity': 1, 'MaxCapacity': 10})
        r = L('describescalabletargets')(store, {'ServiceNamespace': 'dynamodb'})
        assert len(r['ScalableTargets']) == 1
    def test_deregister(self, store):
        L('registerscalabletarget')(store, {'ResourceId': 'table/test', 'ServiceNamespace': 'dynamodb', 'ScalableDimension': 'dynamodb:table:WriteCapacityUnits', 'MinCapacity': 1, 'MaxCapacity': 10})
        L('deregisterscalabletarget')(store, {'ResourceId': 'table/test', 'ServiceNamespace': 'dynamodb', 'ScalableDimension': 'dynamodb:table:WriteCapacityUnits'})
        r = L('describescalabletargets')(store, {'ServiceNamespace': 'dynamodb'})
        assert len(r['ScalableTargets']) == 0
    def test_policy(self, store):
        L('registerscalabletarget')(store, {'ResourceId': 'table/test', 'ServiceNamespace': 'dynamodb', 'ScalableDimension': 'dynamodb:table:WriteCapacityUnits', 'MinCapacity': 1, 'MaxCapacity': 10})
        L('putscalingpolicy')(store, {'PolicyName': 'my-policy', 'ResourceId': 'table/test', 'ServiceNamespace': 'dynamodb', 'ScalableDimension': 'dynamodb:table:WriteCapacityUnits', 'PolicyType': 'TargetTrackingScaling'})
        r = L('describescalingpolicies')(store, {'ServiceNamespace': 'dynamodb'})
        assert r['ScalingPolicies'][0]['PolicyName'] == 'my-policy'
    def test_delete_policy(self, store):
        L('registerscalabletarget')(store, {'ResourceId': 'table/test', 'ServiceNamespace': 'dynamodb', 'ScalableDimension': 'dynamodb:table:WriteCapacityUnits', 'MinCapacity': 1, 'MaxCapacity': 10})
        L('putscalingpolicy')(store, {'PolicyName': 'my-policy', 'ResourceId': 'table/test', 'ServiceNamespace': 'dynamodb', 'ScalableDimension': 'dynamodb:table:WriteCapacityUnits', 'PolicyType': 'TargetTrackingScaling'})
        L('deletescalingpolicy')(store, {'PolicyName': 'my-policy', 'ResourceId': 'table/test', 'ServiceNamespace': 'dynamodb', 'ScalableDimension': 'dynamodb:table:WriteCapacityUnits'})
        r = L('describescalingpolicies')(store, {'ServiceNamespace': 'dynamodb'})
        assert len(r['ScalingPolicies']) == 0

