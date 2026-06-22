"""Integration tests for Auto Scaling."""
import os
import importlib.util
import types
import pytest
A = os.path.dirname(__file__)
S = os.path.join(A, '..', 'autoscaling')
ms = importlib.util.spec_from_file_location('m', os.path.join(S, 'models.code.py'))
mm = importlib.util.module_from_spec(ms); ms.loader.exec_module(mm)
AS = mm.AutoScalingStore
RNF = mm.ResourceNotFoundException
AEF = mm.AlreadyExistsFault
def L(n):
    p = os.path.join(S, n + '.code.py')
    s = importlib.util.spec_from_file_location(n, p)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    for v in m.__dict__.values():
        if isinstance(v, types.FunctionType) and not v.__name__.startswith('_') and v.__name__ != '<lambda>': return v

class TestASG:
    @pytest.fixture
    def store(self): return AS()
    def test_create(self, store):
        L('createautoscalinggroup')(store, {'AutoScalingGroupName': 'asg1', 'MinSize': 1, 'MaxSize': 3})
        r = L('describeautoscalinggroups')(store, {})
        assert r['AutoScalingGroups'][0]['AutoScalingGroupName'] == 'asg1'
    def test_duplicate(self, store):
        L('createautoscalinggroup')(store, {'AutoScalingGroupName': 'asg1', 'MinSize': 1, 'MaxSize': 3})
        with pytest.raises(AEF): L('createautoscalinggroup')(store, {'AutoScalingGroupName': 'asg1', 'MinSize': 1, 'MaxSize': 3})
    def test_update(self, store):
        L('createautoscalinggroup')(store, {'AutoScalingGroupName': 'asg1', 'MinSize': 1, 'MaxSize': 3, 'DesiredCapacity': 1})
        L('updateautoscalinggroup')(store, {'AutoScalingGroupName': 'asg1', 'MinSize': 2, 'MaxSize': 5})
        r = L('describeautoscalinggroups')(store, {})
        assert r['AutoScalingGroups'][0]['MaxSize'] == 5
    def test_set_capacity(self, store):
        L('createautoscalinggroup')(store, {'AutoScalingGroupName': 'asg1', 'MinSize': 1, 'MaxSize': 10, 'DesiredCapacity': 1})
        L('setdesiredcapacity')(store, {'AutoScalingGroupName': 'asg1', 'DesiredCapacity': 5})
        r = L('describeautoscalinggroups')(store, {})
        assert r['AutoScalingGroups'][0]['DesiredCapacity'] == 5
    def test_delete(self, store):
        L('createautoscalinggroup')(store, {'AutoScalingGroupName': 'tmp', 'MinSize': 1, 'MaxSize': 1})
        L('deleteautoscalinggroup')(store, {'AutoScalingGroupName': 'tmp'})
        r = L('describeautoscalinggroups')(store, {})
        assert len(r['AutoScalingGroups']) == 0
    def test_nonexistent(self, store):
        r = L('describeautoscalinggroups')(store, {'AutoScalingGroupNames': ['ghost']})
        assert len(r['AutoScalingGroups']) == 0
    def test_launch_config(self, store):
        L('createlaunchconfiguration')(store, {'LaunchConfigurationName': 'lc1', 'ImageId': 'ami-123', 'InstanceType': 't3.micro'})
        r = L('describelaunchconfigurations')(store, {})
        assert r['LaunchConfigurations'][0]['LaunchConfigurationName'] == 'lc1'
    def test_activities(self, store):
        L('createautoscalinggroup')(store, {'AutoScalingGroupName': 'asg1', 'MinSize': 1, 'MaxSize': 3})
        r = L('describescalingactivities')(store, {'AutoScalingGroupName': 'asg1'})
        assert len(r['Activities']) >= 1

