---
id: "@specs/aws/redshift/docs/API_BatchDeleteClusterSnapshots"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BatchDeleteClusterSnapshots"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# BatchDeleteClusterSnapshots

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_BatchDeleteClusterSnapshots
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BatchDeleteClusterSnapshots
<a name="API_BatchDeleteClusterSnapshots"></a>

Deletes a set of cluster snapshots.

## Request Parameters
<a name="API_BatchDeleteClusterSnapshots_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Identifiers.DeleteClusterSnapshotMessage.N**   
A list of identifiers for the snapshots that you want to delete.  
Type: Array of [DeleteClusterSnapshotMessage](API_DeleteClusterSnapshotMessage.md) objects  
Required: Yes

## Response Elements
<a name="API_BatchDeleteClusterSnapshots_ResponseElements"></a>

The following elements are returned by the service.

 **Errors.SnapshotErrorMessage.N**   
A list of any errors returned.  
Type: Array of [SnapshotErrorMessage](API_SnapshotErrorMessage.md) objects

 **Resources.String.N**   
A list of the snapshot identifiers that were deleted.   
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_BatchDeleteClusterSnapshots_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BatchDeleteRequestSizeExceeded **   
The maximum number for a batch delete of snapshots has been reached. The limit is 100.   
HTTP Status Code: 400

## Examples
<a name="API_BatchDeleteClusterSnapshots_Examples"></a>

### Example
<a name="API_BatchDeleteClusterSnapshots_Example_1"></a>

This example illustrates one usage of BatchDeleteClusterSnapshots.

#### Sample Request
<a name="API_BatchDeleteClusterSnapshots_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=BatchDeleteClusterSnapshots
    &Identifiers.DeleteClusterSnapshotMessage.1.SnapshotIdentifier=mysnapshotid1
    &Identifiers.DeleteClusterSnapshotMessage.2.SnapshotIdentifier=mysnapshotid2
    &SignatureMethod=HmacSHA256&SignatureVersion=4
    &Version=2012-12-01
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
    &X-Amz-Date=20190825T160000Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_BatchDeleteClusterSnapshots_Example_1_Response"></a>

```
<BatchDeleteClusterSnapshotsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <BatchDeleteClusterSnapshotsResult>
    <Resources>
      <String>mysnapshotid1</String>
      <String>mysnapshotid2</String>
    </Resources>
  </BatchDeleteClusterSnapshotsResult>
  <ResponseMetadata>
    <RequestId>5b43fc38-282e-11ea-8cc9-43f1872b4b75</RequestId>
  </ResponseMetadata>
</BatchDeleteClusterSnapshotsResponse>
```

## See Also
<a name="API_BatchDeleteClusterSnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/BatchDeleteClusterSnapshots) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/BatchDeleteClusterSnapshots) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/BatchDeleteClusterSnapshots) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/BatchDeleteClusterSnapshots) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/BatchDeleteClusterSnapshots) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/BatchDeleteClusterSnapshots) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/BatchDeleteClusterSnapshots) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/BatchDeleteClusterSnapshots) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/BatchDeleteClusterSnapshots) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/BatchDeleteClusterSnapshots) 