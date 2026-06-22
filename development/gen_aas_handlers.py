#!/usr/bin/env python3
import os
d = '/home/kara/totalstack/specs/aws/.speclang/assembled/application-autoscaling'
os.makedirs(d, exist_ok=True)
for name, code in {
    'registerscalabletarget': 'def handler(store, r: dict) -> dict:\n    return store.register_target(r["ResourceId"], r["ServiceNamespace"], r["ScalableDimension"], r["MinCapacity"], r["MaxCapacity"])',
    'describescalabletargets': 'def handler(store, r: dict) -> dict:\n    return store.describe_targets(r.get("ServiceNamespace"), r.get("ResourceIds"), r.get("ScalableDimension"))',
    'deregisterscalabletarget': 'def handler(store, r: dict) -> dict:\n    return store.deregister_target(r["ResourceId"], r["ServiceNamespace"], r["ScalableDimension"])',
    'putscalingpolicy': 'def handler(store, r: dict) -> dict:\n    return store.put_policy(r["PolicyName"], r["ResourceId"], r["ServiceNamespace"], r["ScalableDimension"], r.get("PolicyType", "TargetTrackingScaling"))',
    'describescalingpolicies': 'def handler(store, r: dict) -> dict:\n    return store.describe_policies(r.get("ServiceNamespace"), r.get("ResourceId"), r.get("PolicyNames"))',
    'deletescalingpolicy': 'def handler(store, r: dict) -> dict:\n    return store.delete_policy(r["PolicyName"], r["ResourceId"], r["ServiceNamespace"], r["ScalableDimension"])',
}.items():
    with open(f'{d}/{name}.code.py', 'w') as f: f.write(code)
print('6 handlers')
