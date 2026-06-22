"""SSM Parameter Store — AWS Systems Manager Parameter Store emulation."""
class ParameterNotFound(Exception):
    pass
class ParameterAlreadyExists(Exception):
    pass
class InvalidParameterException(Exception):
    pass

class SsmStore:
    def __init__(self):
        self._parameters: dict[str, dict] = {}
        self._tags: dict[str, list] = {}
        self._history: dict[str, list] = {}
    
    def put_parameter(self, name: str, value: str, type_: str = "String", description: str = "", overwrite: bool = False, **kwargs) -> dict:
        if name in self._parameters and not overwrite:
            raise ParameterAlreadyExists(f"Parameter {name} already exists")
        version = len(self._history.get(name, [])) + 1
        param = {
            'Name': name, 'Value': value, 'Type': type_,
            'Description': description, 'Version': version,
            'LastModifiedDate': 1625000000.0, 'ARN': f'arn:aws:ssm:us-east-1:123456789012:parameter/{name}'
        }
        self._parameters[name] = param
        self._history.setdefault(name, []).append(param.copy())
        return {'Version': version}
    
    def get_parameter(self, name: str, with_decryption: bool = False) -> dict:
        if name not in self._parameters:
            raise ParameterNotFound(f"Parameter {name} not found")
        return {'Parameter': self._parameters[name]}
    
    def get_parameters(self, names: list, with_decryption: bool = False) -> dict:
        params = []
        invalid = []
        for n in names:
            if n in self._parameters:
                params.append(self._parameters[n])
            else:
                invalid.append(n)
        return {'Parameters': params, 'InvalidParameters': invalid}
    
    def describe_parameters(self, filters: list = None, max_results: int = 50) -> dict:
        params = list(self._parameters.values())
        return {'Parameters': params[:max_results]}
    
    def delete_parameter(self, name: str) -> dict:
        if name not in self._parameters:
            raise ParameterNotFound(f"Parameter {name} not found")
        del self._parameters[name]
        self._history.pop(name, None)
        return {}
    
    def get_parameter_history(self, name: str, max_results: int = 50) -> dict:
        if name not in self._parameters and name not in self._history:
            raise ParameterNotFound(f"Parameter {name} not found")
        history = self._history.get(name, [])
        return {'Parameters': history[-max_results:]}
    
    def add_tags(self, resource_id: str, tags: list) -> dict:
        self._tags.setdefault(resource_id, []).extend(tags)
        return {}
    
    def list_tags(self, resource_id: str) -> dict:
        return {'TagList': self._tags.get(resource_id, [])}
    
    def remove_tags(self, resource_id: str, tag_keys: list) -> dict:
        if resource_id in self._tags:
            self._tags[resource_id] = [t for t in self._tags[resource_id] if t['Key'] not in tag_keys]
        return {}
