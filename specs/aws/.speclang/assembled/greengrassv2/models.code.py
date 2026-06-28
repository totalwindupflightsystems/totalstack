"""GreengrassV2 Store — Component, Deployment, CoreDevice entities."""
import time as _time
import uuid as _uuid


class ResourceNotFoundException(Exception):
    pass


class ConflictException(Exception):
    pass


class ValidationException(Exception):
    pass


class ComponentRecord:
    def __init__(self, componentName=None, componentVersion=None,
                 arn=None, inlineRecipe=None, lambdaFunction=None,
                 creationTimestamp=None):
        self.componentName = componentName
        self.componentVersion = componentVersion
        self.arn = arn or f"arn:aws:greengrass:us-east-1:000000000000:components/{componentName}:versions/{componentVersion}"
        self.inlineRecipe = inlineRecipe or ""
        self.lambdaFunction = lambdaFunction
        self.creationTimestamp = creationTimestamp or _time.time()

    def to_dict(self):
        return {
            "componentName": self.componentName,
            "componentVersion": self.componentVersion,
            "arn": self.arn,
            "creationTimestamp": self.creationTimestamp,
        }


class DeploymentRecord:
    def __init__(self, deploymentName=None, deploymentId=None,
                 targetArn=None, components=None,
                 deploymentStatus="ACTIVE", creationTimestamp=None):
        self.deploymentName = deploymentName
        self.deploymentId = deploymentId or f"deployment-{_uuid.uuid4().hex[:10]}"
        self.targetArn = targetArn
        self.components = components or {}
        self.deploymentStatus = deploymentStatus
        self.creationTimestamp = creationTimestamp or _time.time()

    def to_dict(self):
        return {
            "deploymentName": self.deploymentName,
            "deploymentId": self.deploymentId,
            "targetArn": self.targetArn,
            "deploymentStatus": self.deploymentStatus,
            "creationTimestamp": self.creationTimestamp,
        }


class CoreDeviceRecord:
    def __init__(self, coreDeviceThingName, coreDeviceThingArn=None,
                 status="HEALTHY", lastStatusUpdateTimestamp=None):
        self.coreDeviceThingName = coreDeviceThingName
        self.coreDeviceThingArn = coreDeviceThingArn or f"arn:aws:iot:us-east-1:000000000000:thing/{coreDeviceThingName}"
        self.status = status
        self.lastStatusUpdateTimestamp = lastStatusUpdateTimestamp or _time.time()

    def to_dict(self):
        return {
            "coreDeviceThingName": self.coreDeviceThingName,
            "coreDeviceThingArn": self.coreDeviceThingArn,
            "status": self.status,
            "lastStatusUpdateTimestamp": self.lastStatusUpdateTimestamp,
        }


class GreengrassV2Store:
    def __init__(self):
        self._components: dict[str, ComponentRecord] = {}  # name:version -> record
        self._deployments: dict[str, DeploymentRecord] = {}
        self._core_devices: dict[str, CoreDeviceRecord] = {}

    def _comp_key(self, name, version):
        return f"{name}:{version}"

    # ── Component ──
    def create_component_version(self, **kwargs):
        key = self._comp_key(kwargs["componentName"], kwargs["componentVersion"])
        if key in self._components:
            raise ConflictException(f"Component {key} already exists")
        record = ComponentRecord(**kwargs)
        self._components[key] = record
        return record.to_dict()

    def describe_component(self, componentName, componentVersion):
        key = self._comp_key(componentName, componentVersion)
        record = self._components.get(key)
        if not record:
            raise ResourceNotFoundException(f"Component {key} not found")
        return record.to_dict()

    def list_components(self, **kwargs):
        return [r.to_dict() for r in self._components.values()]

    def delete_component(self, componentName, componentVersion):
        key = self._comp_key(componentName, componentVersion)
        if key not in self._components:
            raise ResourceNotFoundException(f"Component {key} not found")
        del self._components[key]

    # ── Deployment ──
    def create_deployment(self, **kwargs):
        record = DeploymentRecord(**kwargs)
        self._deployments[record.deploymentId] = record
        return record.to_dict()

    def describe_deployment(self, deploymentId):
        record = self._deployments.get(deploymentId)
        if not record:
            raise ResourceNotFoundException(f"Deployment {deploymentId} not found")
        return record.to_dict()

    def list_deployments(self, **kwargs):
        return [r.to_dict() for r in self._deployments.values()]

    def delete_deployment(self, deploymentId):
        if deploymentId not in self._deployments:
            raise ResourceNotFoundException(f"Deployment {deploymentId} not found")
        del self._deployments[deploymentId]

    # ── CoreDevice ──
    def create_core_device(self, **kwargs):
        name = kwargs["coreDeviceThingName"]
        if name in self._core_devices:
            raise ConflictException(f"CoreDevice {name} already exists")
        record = CoreDeviceRecord(**kwargs)
        self._core_devices[name] = record
        return record.to_dict()

    def describe_core_device(self, coreDeviceThingName):
        record = self._core_devices.get(coreDeviceThingName)
        if not record:
            raise ResourceNotFoundException(f"CoreDevice {coreDeviceThingName} not found")
        return record.to_dict()

    def list_core_devices(self, **kwargs):
        return [r.to_dict() for r in self._core_devices.values()]

    def delete_core_device(self, coreDeviceThingName):
        if coreDeviceThingName not in self._core_devices:
            raise ResourceNotFoundException(f"CoreDevice {coreDeviceThingName} not found")
        del self._core_devices[coreDeviceThingName]
