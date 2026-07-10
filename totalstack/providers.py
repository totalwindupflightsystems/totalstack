"""TotalStack service providers — auto-generated wiring."""
from localstack.services.plugins import Service, aws_provider


@aws_provider(api="amp", name="totalstack")
def amp_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.amp.provider import TotalStackAmpProvider
    provider = TotalStackAmpProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="amplify", name="totalstack")
def amplify_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.amplify.provider import TotalStackAmplifyProvider
    provider = TotalStackAmplifyProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="appconfig", name="totalstack")
def appconfig_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.appconfig.provider import TotalStackAppconfigProvider
    provider = TotalStackAppconfigProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="application-autoscaling", name="totalstack")
def application_autoscaling_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.application-autoscaling.provider import TotalStackApplicationAutoscalingProvider
    provider = TotalStackApplicationAutoscalingProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="appmesh", name="totalstack")
def appmesh_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.appmesh.provider import TotalStackAppmeshProvider
    provider = TotalStackAppmeshProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="appsync", name="totalstack")
def appsync_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.appsync.provider import TotalStackAppsyncProvider
    provider = TotalStackAppsyncProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="athena", name="totalstack")
def athena_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.athena.provider import TotalStackAthenaProvider
    provider = TotalStackAthenaProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="autoscaling", name="totalstack")
def autoscaling_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.autoscaling.provider import TotalStackAutoscalingProvider
    provider = TotalStackAutoscalingProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="backup", name="totalstack")
def backup_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.backup.provider import TotalStackBackupProvider
    provider = TotalStackBackupProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="batch", name="totalstack")
def batch_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.batch.provider import TotalStackBatchProvider
    provider = TotalStackBatchProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="bedrock", name="totalstack")
def bedrock_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.bedrock.provider import TotalStackBedrockProvider
    provider = TotalStackBedrockProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="bedrock-agent", name="totalstack")
def bedrock_agent_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.bedrock-agent.provider import TotalStackBedrockAgentProvider
    provider = TotalStackBedrockAgentProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="bedrock-runtime", name="totalstack")
def bedrock_runtime_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.bedrock-runtime.provider import TotalStackBedrockRuntimeProvider
    provider = TotalStackBedrockRuntimeProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="cloudfront", name="totalstack")
def cloudfront_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.cloudfront.provider import TotalStackCloudfrontProvider
    provider = TotalStackCloudfrontProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="cloudtrail", name="totalstack")
def cloudtrail_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.cloudtrail.provider import TotalStackCloudtrailProvider
    provider = TotalStackCloudtrailProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="codeartifact", name="totalstack")
def codeartifact_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.codeartifact.provider import TotalStackCodeartifactProvider
    provider = TotalStackCodeartifactProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="codebuild", name="totalstack")
def codebuild_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.codebuild.provider import TotalStackCodebuildProvider
    provider = TotalStackCodebuildProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="codedeploy", name="totalstack")
def codedeploy_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.codedeploy.provider import TotalStackCodedeployProvider
    provider = TotalStackCodedeployProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="codepipeline", name="totalstack")
def codepipeline_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.codepipeline.provider import TotalStackCodepipelineProvider
    provider = TotalStackCodepipelineProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="cognito-identity", name="totalstack")
def cognito_identity_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.cognito-identity.provider import TotalStackCognitoIdentityProvider
    provider = TotalStackCognitoIdentityProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="comprehend", name="totalstack")
def comprehend_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.comprehend.provider import TotalStackComprehendProvider
    provider = TotalStackComprehendProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="datasync", name="totalstack")
def datasync_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.datasync.provider import TotalStackDatasyncProvider
    provider = TotalStackDatasyncProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="dms", name="totalstack")
def dms_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.dms.provider import TotalStackDmsProvider
    provider = TotalStackDmsProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="docdb", name="totalstack")
def docdb_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.docdb.provider import TotalStackDocdbProvider
    provider = TotalStackDocdbProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="dynamodbstreams", name="totalstack")
def dynamodbstreams_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.dynamodbstreams.provider import TotalStackDynamodbstreamsProvider
    provider = TotalStackDynamodbstreamsProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="ecr", name="totalstack")
def ecr_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.ecr.provider import TotalStackEcrProvider
    provider = TotalStackEcrProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="efs", name="totalstack")
def efs_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.efs.provider import TotalStackEfsProvider
    provider = TotalStackEfsProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="fis", name="totalstack")
def fis_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.fis.provider import TotalStackFisProvider
    provider = TotalStackFisProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="forecast", name="totalstack")
def forecast_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.forecast.provider import TotalStackForecastProvider
    provider = TotalStackForecastProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="frauddetector", name="totalstack")
def frauddetector_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.frauddetector.provider import TotalStackFrauddetectorProvider
    provider = TotalStackFrauddetectorProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="fsx", name="totalstack")
def fsx_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.fsx.provider import TotalStackFsxProvider
    provider = TotalStackFsxProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="globalaccelerator", name="totalstack")
def globalaccelerator_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.globalaccelerator.provider import TotalStackGlobalacceleratorProvider
    provider = TotalStackGlobalacceleratorProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="grafana", name="totalstack")
def grafana_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.grafana.provider import TotalStackGrafanaProvider
    provider = TotalStackGrafanaProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="greengrassv2", name="totalstack")
def greengrassv2_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.greengrassv2.provider import TotalStackGreengrassv2Provider
    provider = TotalStackGreengrassv2Provider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="identitystore", name="totalstack")
def identitystore_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.identitystore.provider import TotalStackIdentitystoreProvider
    provider = TotalStackIdentitystoreProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="iot", name="totalstack")
def iot_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.iot.provider import TotalStackIotProvider
    provider = TotalStackIotProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="iot-data", name="totalstack")
def iot_data_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.iot-data.provider import TotalStackIotDataProvider
    provider = TotalStackIotDataProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="kendra", name="totalstack")
def kendra_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.kendra.provider import TotalStackKendraProvider
    provider = TotalStackKendraProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="keyspaces", name="totalstack")
def keyspaces_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.keyspaces.provider import TotalStackKeyspacesProvider
    provider = TotalStackKeyspacesProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="lexv2-models", name="totalstack")
def lexv2_models_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.lexv2-models.provider import TotalStackLexv2ModelsProvider
    provider = TotalStackLexv2ModelsProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="lexv2-runtime", name="totalstack")
def lexv2_runtime_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.lexv2-runtime.provider import TotalStackLexv2RuntimeProvider
    provider = TotalStackLexv2RuntimeProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="lightsail", name="totalstack")
def lightsail_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.lightsail.provider import TotalStackLightsailProvider
    provider = TotalStackLightsailProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="mediaconvert", name="totalstack")
def mediaconvert_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.mediaconvert.provider import TotalStackMediaconvertProvider
    provider = TotalStackMediaconvertProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="memorydb", name="totalstack")
def memorydb_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.memorydb.provider import TotalStackMemorydbProvider
    provider = TotalStackMemorydbProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="mq", name="totalstack")
def mq_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.mq.provider import TotalStackMqProvider
    provider = TotalStackMqProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="mwaa", name="totalstack")
def mwaa_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.mwaa.provider import TotalStackMwaaProvider
    provider = TotalStackMwaaProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="neptune", name="totalstack")
def neptune_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.neptune.provider import TotalStackNeptuneProvider
    provider = TotalStackNeptuneProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="network-firewall", name="totalstack")
def network_firewall_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.network-firewall.provider import TotalStackNetworkFirewallProvider
    provider = TotalStackNetworkFirewallProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="opensearchserverless", name="totalstack")
def opensearchserverless_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.opensearchserverless.provider import TotalStackOpensearchserverlessProvider
    provider = TotalStackOpensearchserverlessProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="organizations", name="totalstack")
def organizations_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.organizations.provider import TotalStackOrganizationsProvider
    provider = TotalStackOrganizationsProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="personalize", name="totalstack")
def personalize_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.personalize.provider import TotalStackPersonalizeProvider
    provider = TotalStackPersonalizeProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="polly", name="totalstack")
def polly_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.polly.provider import TotalStackPollyProvider
    provider = TotalStackPollyProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="quicksight", name="totalstack")
def quicksight_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.quicksight.provider import TotalStackQuicksightProvider
    provider = TotalStackQuicksightProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="ram", name="totalstack")
def ram_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.ram.provider import TotalStackRamProvider
    provider = TotalStackRamProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="rekognition", name="totalstack")
def rekognition_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.rekognition.provider import TotalStackRekognitionProvider
    provider = TotalStackRekognitionProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="rolesanywhere", name="totalstack")
def rolesanywhere_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.rolesanywhere.provider import TotalStackRolesanywhereProvider
    provider = TotalStackRolesanywhereProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="s3tables", name="totalstack")
def s3tables_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.s3tables.provider import TotalStackS3tablesProvider
    provider = TotalStackS3tablesProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="servicecatalog", name="totalstack")
def servicecatalog_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.servicecatalog.provider import TotalStackServicecatalogProvider
    provider = TotalStackServicecatalogProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="sesv2", name="totalstack")
def sesv2_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.sesv2.provider import TotalStackSesv2Provider
    provider = TotalStackSesv2Provider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="shield", name="totalstack")
def shield_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.shield.provider import TotalStackShieldProvider
    provider = TotalStackShieldProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="signer", name="totalstack")
def signer_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.signer.provider import TotalStackSignerProvider
    provider = TotalStackSignerProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="sso-admin", name="totalstack")
def sso_admin_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.sso-admin.provider import TotalStackSsoAdminProvider
    provider = TotalStackSsoAdminProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="storagegateway", name="totalstack")
def storagegateway_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.storagegateway.provider import TotalStackStoragegatewayProvider
    provider = TotalStackStoragegatewayProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="textract", name="totalstack")
def textract_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.textract.provider import TotalStackTextractProvider
    provider = TotalStackTextractProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="timestream-influxdb", name="totalstack")
def timestream_influxdb_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.timestream-influxdb.provider import TotalStackTimestreamInfluxdbProvider
    provider = TotalStackTimestreamInfluxdbProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="transcribe", name="totalstack")
def transcribe_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.transcribe.provider import TotalStackTranscribeProvider
    provider = TotalStackTranscribeProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="transfer", name="totalstack")
def transfer_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.transfer.provider import TotalStackTransferProvider
    provider = TotalStackTransferProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)


@aws_provider(api="verifiedpermissions", name="totalstack")
def verifiedpermissions_totalstack():
    from localstack.services.moto import MotoFallbackDispatcher
    from totalstack.services.verifiedpermissions.provider import TotalStackVerifiedpermissionsProvider
    provider = TotalStackVerifiedpermissionsProvider()
    return Service.for_provider(provider, dispatch_table_factory=MotoFallbackDispatcher)
