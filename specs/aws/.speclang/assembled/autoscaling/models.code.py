"""Auto Scaling Store — EC2 Auto Scaling emulation."""
class ResourceNotFoundException(Exception): pass
class AlreadyExistsFault(Exception): pass
class InvalidParameterException(Exception): pass

class AutoScalingStore:
    def __init__(self):
        self._groups: dict[str, dict] = {}
        self._configs: dict[str, dict] = {}
        self._activities: list[dict] = []
    
    def create_group(self, name: str, min_size: int, max_size: int, **kwargs) -> dict:
        if name in self._groups:
            raise AlreadyExistsFault(f"AutoScalingGroup {name} already exists")
        group = {'AutoScalingGroupName': name, 'MinSize': min_size, 'MaxSize': max_size,
                 'DesiredCapacity': kwargs.get('DesiredCapacity', min_size),
                 'Instances': [], 'CreatedTime': 1625000000.0, **kwargs}
        self._groups[name] = group
        self._activities.append({'ActivityId': f'a-{len(self._activities)+1}', 'AutoScalingGroupName': name,
                                  'Cause': 'create', 'StatusCode': 'Successful'})
        return {}
    
    def describe_groups(self, names: list = None) -> dict:
        if names:
            return {'AutoScalingGroups': [self._groups[n] for n in names if n in self._groups]}
        return {'AutoScalingGroups': list(self._groups.values())}
    
    def update_group(self, name: str, **kwargs) -> dict:
        if name not in self._groups:
            raise ResourceNotFoundException(f"AutoScalingGroup {name} not found")
        self._groups[name].update({k: v for k, v in kwargs.items() if v is not None})
        return {}
    
    def delete_group(self, name: str, force: bool = False) -> dict:
        if name not in self._groups:
            raise ResourceNotFoundException(f"AutoScalingGroup {name} not found")
        del self._groups[name]
        return {}
    
    def set_desired_capacity(self, name: str, capacity: int) -> dict:
        if name not in self._groups:
            raise ResourceNotFoundException(f"AutoScalingGroup {name} not found")
        self._groups[name]['DesiredCapacity'] = capacity
        return {}
    
    def describe_activities(self, name: str = None, max_records: int = 50) -> dict:
        acts = [a for a in self._activities if not name or a['AutoScalingGroupName'] == name]
        return {'Activities': acts[-max_records:]}
    
    def create_launch_config(self, name: str, image_id: str, instance_type: str, **kwargs) -> dict:
        if name in self._configs:
            raise AlreadyExistsFault(f"LaunchConfiguration {name} already exists")
        self._configs[name] = {'LaunchConfigurationName': name, 'ImageId': image_id,
                                'InstanceType': instance_type, **kwargs}
        return {}
    
    def describe_launch_configs(self, names: list = None) -> dict:
        if names:
            return {'LaunchConfigurations': [self._configs[n] for n in names if n in self._configs]}
        return {'LaunchConfigurations': list(self._configs.values())}
    
    def delete_launch_config(self, name: str) -> dict:
        if name not in self._configs:
            raise ResourceNotFoundException(f"LaunchConfiguration {name} not found")
        del self._configs[name]
        return {}
