"""SageMaker Store — TrainingJob, Model, EndpointConfig, Endpoint entities."""
import time as _time


# ── Exception Classes ──────────────────────────────────────────────

class ResourceNotFoundException(Exception):
    pass


class ResourceInUseException(Exception):
    pass


class ResourceLimitExceededException(Exception):
    pass


class ValidationException(Exception):
    pass


# ── Record Classes ─────────────────────────────────────────────────

class TrainingJobRecord:
    def __init__(self, TrainingJobName, TrainingJobArn=None,
                 RoleArn=None, AlgorithmSpecification=None,
                 ResourceConfig=None, OutputDataConfig=None,
                 InputDataConfig=None, VpcConfig=None,
                 StoppingCondition=None, HyperParameters=None,
                 Tags=None, EnableNetworkIsolation=None,
                 EnableInterContainerTrafficEncryption=None,
                 EnableManagedSpotTraining=None,
                 CheckpointConfig=None, DebugHookConfig=None,
                 DebugRuleConfigurations=None,
                 TensorBoardOutputConfig=None,
                 ExperimentConfig=None, ProfilerConfig=None,
                 ProfilerRuleConfigurations=None,
                 Environment=None, RetryStrategy=None,
                 RemoteDebugConfig=None, InfraCheckConfig=None,
                 SessionChainingConfig=None,
                 ServerlessJobConfig=None, MlflowConfig=None,
                 ModelPackageConfig=None,
                 TrainingJobStatus="InProgress",
                 FailureReason=None,
                 ModelArtifacts=None,
                 CreationTime=None, LastModifiedTime=None):
        self.TrainingJobName = TrainingJobName
        self.TrainingJobArn = TrainingJobArn or f"arn:aws:sagemaker:us-east-1:000000000000:training-job/{TrainingJobName}"
        self.RoleArn = RoleArn
        self.AlgorithmSpecification = AlgorithmSpecification
        self.ResourceConfig = ResourceConfig
        self.OutputDataConfig = OutputDataConfig
        self.InputDataConfig = InputDataConfig
        self.VpcConfig = VpcConfig
        self.StoppingCondition = StoppingCondition
        self.HyperParameters = HyperParameters
        self.Tags = Tags
        self.EnableNetworkIsolation = EnableNetworkIsolation
        self.EnableInterContainerTrafficEncryption = EnableInterContainerTrafficEncryption
        self.EnableManagedSpotTraining = EnableManagedSpotTraining
        self.CheckpointConfig = CheckpointConfig
        self.DebugHookConfig = DebugHookConfig
        self.DebugRuleConfigurations = DebugRuleConfigurations
        self.TensorBoardOutputConfig = TensorBoardOutputConfig
        self.ExperimentConfig = ExperimentConfig
        self.ProfilerConfig = ProfilerConfig
        self.ProfilerRuleConfigurations = ProfilerRuleConfigurations
        self.Environment = Environment
        self.RetryStrategy = RetryStrategy
        self.RemoteDebugConfig = RemoteDebugConfig
        self.InfraCheckConfig = InfraCheckConfig
        self.SessionChainingConfig = SessionChainingConfig
        self.ServerlessJobConfig = ServerlessJobConfig
        self.MlflowConfig = MlflowConfig
        self.ModelPackageConfig = ModelPackageConfig
        self.TrainingJobStatus = TrainingJobStatus
        self.FailureReason = FailureReason
        self.ModelArtifacts = ModelArtifacts
        self.CreationTime = CreationTime or _time.time()
        self.LastModifiedTime = LastModifiedTime or _time.time()

    def to_dict(self):
        return {
            "TrainingJobName": self.TrainingJobName,
            "TrainingJobArn": self.TrainingJobArn,
            "RoleArn": self.RoleArn,
            "AlgorithmSpecification": self.AlgorithmSpecification,
            "ResourceConfig": self.ResourceConfig,
            "OutputDataConfig": self.OutputDataConfig,
            "InputDataConfig": self.InputDataConfig,
            "VpcConfig": self.VpcConfig,
            "StoppingCondition": self.StoppingCondition,
            "HyperParameters": self.HyperParameters,
            "Tags": self.Tags,
            "TrainingJobStatus": self.TrainingJobStatus,
            "FailureReason": self.FailureReason,
            "ModelArtifacts": self.ModelArtifacts,
            "CreationTime": self.CreationTime,
            "LastModifiedTime": self.LastModifiedTime,
            "EnableNetworkIsolation": self.EnableNetworkIsolation,
            "EnableInterContainerTrafficEncryption": self.EnableInterContainerTrafficEncryption,
            "EnableManagedSpotTraining": self.EnableManagedSpotTraining,
        }


class ModelRecord:
    def __init__(self, ModelName, ModelArn=None,
                 PrimaryContainer=None, Containers=None,
                 InferenceExecutionConfig=None,
                 ExecutionRoleArn=None, VpcConfig=None,
                 Tags=None, EnableNetworkIsolation=None,
                 CreationTime=None):
        self.ModelName = ModelName
        self.ModelArn = ModelArn or f"arn:aws:sagemaker:us-east-1:000000000000:model/{ModelName}"
        self.PrimaryContainer = PrimaryContainer
        self.Containers = Containers
        self.InferenceExecutionConfig = InferenceExecutionConfig
        self.ExecutionRoleArn = ExecutionRoleArn
        self.VpcConfig = VpcConfig
        self.Tags = Tags
        self.EnableNetworkIsolation = EnableNetworkIsolation
        self.CreationTime = CreationTime or _time.time()

    def to_dict(self):
        return {
            "ModelName": self.ModelName,
            "ModelArn": self.ModelArn,
            "PrimaryContainer": self.PrimaryContainer,
            "Containers": self.Containers,
            "InferenceExecutionConfig": self.InferenceExecutionConfig,
            "ExecutionRoleArn": self.ExecutionRoleArn,
            "VpcConfig": self.VpcConfig,
            "Tags": self.Tags,
            "EnableNetworkIsolation": self.EnableNetworkIsolation,
            "CreationTime": self.CreationTime,
        }


class EndpointConfigRecord:
    def __init__(self, EndpointConfigName, EndpointConfigArn=None,
                 ProductionVariants=None, DataCaptureConfig=None,
                 Tags=None, KmsKeyId=None,
                 AsyncInferenceConfig=None, ExplainerConfig=None,
                 ShadowProductionVariants=None,
                 ExecutionRoleArn=None, VpcConfig=None,
                 EnableNetworkIsolation=None, MetricsConfig=None,
                 CreationTime=None):
        self.EndpointConfigName = EndpointConfigName
        self.EndpointConfigArn = EndpointConfigArn or f"arn:aws:sagemaker:us-east-1:000000000000:endpoint-config/{EndpointConfigName}"
        self.ProductionVariants = ProductionVariants or []
        self.DataCaptureConfig = DataCaptureConfig
        self.Tags = Tags
        self.KmsKeyId = KmsKeyId
        self.AsyncInferenceConfig = AsyncInferenceConfig
        self.ExplainerConfig = ExplainerConfig
        self.ShadowProductionVariants = ShadowProductionVariants
        self.ExecutionRoleArn = ExecutionRoleArn
        self.VpcConfig = VpcConfig
        self.EnableNetworkIsolation = EnableNetworkIsolation
        self.MetricsConfig = MetricsConfig
        self.CreationTime = CreationTime or _time.time()

    def to_dict(self):
        return {
            "EndpointConfigName": self.EndpointConfigName,
            "EndpointConfigArn": self.EndpointConfigArn,
            "ProductionVariants": self.ProductionVariants,
            "DataCaptureConfig": self.DataCaptureConfig,
            "Tags": self.Tags,
            "KmsKeyId": self.KmsKeyId,
            "CreationTime": self.CreationTime,
        }


class EndpointRecord:
    def __init__(self, EndpointName, EndpointArn=None,
                 EndpointConfigName=None, DeploymentConfig=None,
                 Tags=None, ProductionVariants=None,
                 DataCaptureConfig=None,
                 EndpointStatus="Creating",
                 FailureReason=None,
                 CreationTime=None, LastModifiedTime=None):
        self.EndpointName = EndpointName
        self.EndpointArn = EndpointArn or f"arn:aws:sagemaker:us-east-1:000000000000:endpoint/{EndpointName}"
        self.EndpointConfigName = EndpointConfigName
        self.DeploymentConfig = DeploymentConfig
        self.Tags = Tags
        self.ProductionVariants = ProductionVariants
        self.DataCaptureConfig = DataCaptureConfig
        self.EndpointStatus = EndpointStatus
        self.FailureReason = FailureReason
        self.CreationTime = CreationTime or _time.time()
        self.LastModifiedTime = LastModifiedTime or _time.time()

    def to_dict(self):
        return {
            "EndpointName": self.EndpointName,
            "EndpointArn": self.EndpointArn,
            "EndpointConfigName": self.EndpointConfigName,
            "EndpointStatus": self.EndpointStatus,
            "FailureReason": self.FailureReason,
            "CreationTime": self.CreationTime,
            "LastModifiedTime": self.LastModifiedTime,
            "Tags": self.Tags,
            "ProductionVariants": self.ProductionVariants,
        }


# ── Store Class ────────────────────────────────────────────────────

class SageMakerStore:
    def __init__(self):
        self._training_jobs: dict[str, TrainingJobRecord] = {}
        self._models: dict[str, ModelRecord] = {}
        self._endpoint_configs: dict[str, EndpointConfigRecord] = {}
        self._endpoints: dict[str, EndpointRecord] = {}

    # ── TrainingJobs accessor (method-style for generated handlers) ──
    def training_jobs(self, name: str = None):
        if name is not None:
            return self._training_jobs.get(name)
        return list(self._training_jobs.values())

    # ── Models accessor ──
    def models(self, name: str = None):
        if name is not None:
            return self._models.get(name)
        return list(self._models.values())

    # ── EndpointConfigs accessor ──
    def endpoint_configs(self, name: str = None):
        if name is not None:
            return self._endpoint_configs.get(name)
        return list(self._endpoint_configs.values())

    # ── Endpoints accessor ──
    def endpoints(self, name: str = None):
        if name is not None:
            return self._endpoints.get(name)
        return list(self._endpoints.values())

    # ── TrainingJob CRUD ──
    def create_training_job(self, **kwargs):
        name = kwargs["TrainingJobName"]
        if name in self._training_jobs:
            raise ResourceInUseException(f"TrainingJob {name} already exists")
        record = TrainingJobRecord(**kwargs)
        self._training_jobs[name] = record
        return record.to_dict()

    def describe_training_job(self, TrainingJobName):
        record = self._training_jobs.get(TrainingJobName)
        if not record:
            raise ResourceNotFoundException(f"TrainingJob {TrainingJobName} not found")
        return record.to_dict()

    def list_training_jobs(self, **kwargs):
        return [r.to_dict() for r in self._training_jobs.values()]

    def delete_training_job(self, TrainingJobName):
        if TrainingJobName not in self._training_jobs:
            raise ResourceNotFoundException(f"TrainingJob {TrainingJobName} not found")
        del self._training_jobs[TrainingJobName]

    def stop_training_job(self, TrainingJobName):
        record = self._training_jobs.get(TrainingJobName)
        if not record:
            raise ResourceNotFoundException(f"TrainingJob {TrainingJobName} not found")
        record.TrainingJobStatus = "Stopped"

    # ── Model CRUD ──
    def create_model(self, **kwargs):
        name = kwargs["ModelName"]
        if name in self._models:
            raise ResourceInUseException(f"Model {name} already exists")
        record = ModelRecord(**kwargs)
        self._models[name] = record
        return record.to_dict()

    def describe_model(self, ModelName):
        record = self._models.get(ModelName)
        if not record:
            raise ResourceNotFoundException(f"Model {ModelName} not found")
        return record.to_dict()

    def list_models(self, **kwargs):
        return [r.to_dict() for r in self._models.values()]

    def delete_model(self, ModelName):
        if ModelName not in self._models:
            raise ResourceNotFoundException(f"Model {ModelName} not found")
        del self._models[ModelName]

    # ── EndpointConfig CRUD ──
    def create_endpoint_config(self, **kwargs):
        name = kwargs["EndpointConfigName"]
        if name in self._endpoint_configs:
            raise ResourceInUseException(f"EndpointConfig {name} already exists")
        record = EndpointConfigRecord(**kwargs)
        self._endpoint_configs[name] = record
        return record.to_dict()

    def describe_endpoint_config(self, EndpointConfigName):
        record = self._endpoint_configs.get(EndpointConfigName)
        if not record:
            raise ResourceNotFoundException(f"EndpointConfig {EndpointConfigName} not found")
        return record.to_dict()

    def list_endpoint_configs(self, **kwargs):
        return [r.to_dict() for r in self._endpoint_configs.values()]

    def delete_endpoint_config(self, EndpointConfigName):
        if EndpointConfigName not in self._endpoint_configs:
            raise ResourceNotFoundException(f"EndpointConfig {EndpointConfigName} not found")
        del self._endpoint_configs[EndpointConfigName]

    # ── Endpoint CRUD ──
    def create_endpoint(self, **kwargs):
        name = kwargs["EndpointName"]
        if name in self._endpoints:
            raise ResourceInUseException(f"Endpoint {name} already exists")
        record = EndpointRecord(**kwargs)
        self._endpoints[name] = record
        return record.to_dict()

    def describe_endpoint(self, EndpointName):
        record = self._endpoints.get(EndpointName)
        if not record:
            raise ResourceNotFoundException(f"Endpoint {EndpointName} not found")
        return record.to_dict()

    def list_endpoints(self, **kwargs):
        return [r.to_dict() for r in self._endpoints.values()]

    def delete_endpoint(self, EndpointName):
        if EndpointName not in self._endpoints:
            raise ResourceNotFoundException(f"Endpoint {EndpointName} not found")
        del self._endpoints[EndpointName]

    def update_endpoint(self, **kwargs):
        name = kwargs["EndpointName"]
        record = self._endpoints.get(name)
        if not record:
            raise ResourceNotFoundException(f"Endpoint {name} not found")
        if "EndpointConfigName" in kwargs:
            record.EndpointConfigName = kwargs["EndpointConfigName"]
        record.LastModifiedTime = _time.time()
        return record.to_dict()
