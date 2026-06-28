---
id: "@specs/aws/storagegateway/docs/API_StorageGatewayError"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StorageGatewayError"
status: active
depends_on:
  - "@specs/aws/storagegateway/meta"
---

# StorageGatewayError

> **source:** AWS Documentation
> **spec:id:** @specs/aws/storagegateway/docs/API_StorageGatewayError
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StorageGatewayError
<a name="API_StorageGatewayError"></a>

Provides additional information about an error that was returned by the service. See the `errorCode` and `errorDetails` members for more information about the error.

## Contents
<a name="API_StorageGatewayError_Contents"></a>

 ** errorCode **   <a name="StorageGateway-Type-StorageGatewayError-errorCode"></a>
Additional information about the error.  
Type: String  
Valid Values: `ActivationKeyExpired | ActivationKeyInvalid | ActivationKeyNotFound | GatewayInternalError | GatewayNotConnected | GatewayNotFound | GatewayProxyNetworkConnectionBusy | AuthenticationFailure | BandwidthThrottleScheduleNotFound | Blocked | CannotExportSnapshot | ChapCredentialNotFound | DiskAlreadyAllocated | DiskDoesNotExist | DiskSizeGreaterThanVolumeMaxSize | DiskSizeLessThanVolumeSize | DiskSizeNotGigAligned | DuplicateCertificateInfo | DuplicateSchedule | EndpointNotFound | IAMNotSupported | InitiatorInvalid | InitiatorNotFound | InternalError | InvalidGateway | InvalidEndpoint | InvalidParameters | InvalidSchedule | LocalStorageLimitExceeded | LunAlreadyAllocated | LunInvalid | JoinDomainInProgress | MaximumContentLengthExceeded | MaximumTapeCartridgeCountExceeded | MaximumVolumeCountExceeded | NetworkConfigurationChanged | NoDisksAvailable | NotImplemented | NotSupported | OperationAborted | OutdatedGateway | ParametersNotImplemented | RegionInvalid | RequestTimeout | ServiceUnavailable | SnapshotDeleted | SnapshotIdInvalid | SnapshotInProgress | SnapshotNotFound | SnapshotScheduleNotFound | StagingAreaFull | StorageFailure | TapeCartridgeNotFound | TargetAlreadyExists | TargetInvalid | TargetNotFound | UnauthorizedOperation | VolumeAlreadyExists | VolumeIdInvalid | VolumeInUse | VolumeNotFound | VolumeNotReady`   
Required: No

 ** errorDetails **   <a name="StorageGateway-Type-StorageGatewayError-errorDetails"></a>
Human-readable text that provides detail about the error that occurred.  
Type: String to string map  
Required: No

## See Also
<a name="API_StorageGatewayError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/StorageGatewayError) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/StorageGatewayError) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/StorageGatewayError) 