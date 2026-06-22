"""Application Auto Scaling Store."""
class ResourceNotFoundException(Exception): pass
class InvalidParameterException(Exception): pass
class ConcurrentUpdateException(Exception): pass
class AlreadyExistsFault(Exception): pass

class AppAutoScalingStore:
    def __init__(self):
        self._targets: dict[str, dict] = {}
        self._policies: dict[str, dict] = {}
    
    def register_target(self, resource_id: str, namespace: str, dimension: str, min_cap: int, max_cap: int, **kwargs) -> dict:
        key = f'{namespace}/{dimension}/{resource_id}'
        if key in self._targets:
            raise AlreadyExistsFault(f"ScalableTarget already registered")
        t = {'ResourceId': resource_id, 'ServiceNamespace': namespace, 'ScalableDimension': dimension,
             'MinCapacity': min_cap, 'MaxCapacity': max_cap, **kwargs}
        self._targets[key] = t
        return {}
    
    def describe_targets(self, namespace: str = None, resource_ids: list = None, dimension: str = None) -> dict:
        targets = list(self._targets.values())
        if namespace:
            targets = [t for t in targets if t['ServiceNamespace'] == namespace]
        if resource_ids:
            targets = [t for t in targets if t['ResourceId'] in resource_ids]
        if dimension:
            targets = [t for t in targets if t['ScalableDimension'] == dimension]
        return {'ScalableTargets': targets}
    
    def deregister_target(self, resource_id: str, namespace: str, dimension: str) -> dict:
        key = f'{namespace}/{dimension}/{resource_id}'
        if key not in self._targets:
            raise ResourceNotFoundException("ScalableTarget not found")
        del self._targets[key]
        return {}
    
    def put_policy(self, name: str, resource_id: str, namespace: str, dimension: str, policy_type: str, **kwargs) -> dict:
        key = f'{namespace}/{dimension}/{resource_id}/{name}'
        p = {'PolicyName': name, 'ResourceId': resource_id, 'ServiceNamespace': namespace,
             'ScalableDimension': dimension, 'PolicyType': policy_type, **kwargs}
        self._policies[key] = p
        return {'PolicyARN': f'arn:aws:autoscaling:{namespace}:policy/{name}'}
    
    def describe_policies(self, namespace: str = None, resource_id: str = None, names: list = None) -> dict:
        policies = list(self._policies.values())
        if namespace:
            policies = [p for p in policies if p['ServiceNamespace'] == namespace]
        if resource_id:
            policies = [p for p in policies if p['ResourceId'] == resource_id]
        if names:
            policies = [p for p in policies if p['PolicyName'] in names]
        return {'ScalingPolicies': policies}
    
    def delete_policy(self, name: str, resource_id: str, namespace: str, dimension: str) -> dict:
        key = f'{namespace}/{dimension}/{resource_id}/{name}'
        if key not in self._policies:
            raise ResourceNotFoundException("ScalingPolicy not found")
        del self._policies[key]
        return {}
