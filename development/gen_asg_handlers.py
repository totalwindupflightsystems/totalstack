#!/usr/bin/env python3
import os
d = '/home/kara/totalstack/specs/aws/.speclang/assembled/autoscaling'
os.makedirs(d, exist_ok=True)
for name, code in {
    'createautoscalinggroup': 'def handler(store, r: dict) -> dict:\n    return store.create_group(r["AutoScalingGroupName"], r["MinSize"], r["MaxSize"], DesiredCapacity=r.get("DesiredCapacity"), LaunchConfigurationName=r.get("LaunchConfigurationName"))',
    'describeautoscalinggroups': 'def handler(store, r: dict) -> dict:\n    return store.describe_groups(r.get("AutoScalingGroupNames"))',
    'updateautoscalinggroup': 'def handler(store, r: dict) -> dict:\n    kwargs = {k: v for k, v in r.items() if k != "AutoScalingGroupName" and v is not None}\n    return store.update_group(r["AutoScalingGroupName"], **kwargs)',
    'deleteautoscalinggroup': 'def handler(store, r: dict) -> dict:\n    return store.delete_group(r["AutoScalingGroupName"], r.get("ForceDelete", False))',
    'setdesiredcapacity': 'def handler(store, r: dict) -> dict:\n    return store.set_desired_capacity(r["AutoScalingGroupName"], r["DesiredCapacity"])',
    'describescalingactivities': 'def handler(store, r: dict) -> dict:\n    return store.describe_activities(r.get("AutoScalingGroupName"))',
    'createlaunchconfiguration': 'def handler(store, r: dict) -> dict:\n    return store.create_launch_config(r["LaunchConfigurationName"], r.get("ImageId", "ami-test"), r.get("InstanceType", "t3.micro"))',
    'describelaunchconfigurations': 'def handler(store, r: dict) -> dict:\n    return store.describe_launch_configs(r.get("LaunchConfigurationNames"))',
    'deletelaunchconfiguration': 'def handler(store, r: dict) -> dict:\n    return store.delete_launch_config(r["LaunchConfigurationName"])',
}.items():
    with open(f'{d}/{name}.code.py', 'w') as f: f.write(code)
print('9 handlers')
