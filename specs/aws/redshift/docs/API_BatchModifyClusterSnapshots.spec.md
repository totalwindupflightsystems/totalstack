---
id: "@specs/aws/redshift/docs/API_BatchModifyClusterSnapshots"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS BatchModifyClusterSnapshots"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# BatchModifyClusterSnapshots

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_BatchModifyClusterSnapshots
> **target_lang:** meta — documentation tier. ALL sections preserved.



# BatchModifyClusterSnapshots
<a name="API_BatchModifyClusterSnapshots"></a>

Modifies the settings for a set of cluster snapshots.

## Request Parameters
<a name="API_BatchModifyClusterSnapshots_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **SnapshotIdentifierList.String.N**   
A list of snapshot identifiers you want to modify.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** Force **   
A boolean value indicating whether to override an exception if the retention period has passed.   
Type: Boolean  
Required: No

 ** ManualSnapshotRetentionPeriod **   
The number of days that a manual snapshot is retained. If you specify the value -1, the manual snapshot is retained indefinitely.  
The number must be either -1 or an integer between 1 and 3,653.  
If you decrease the manual snapshot retention period from its current value, existing manual snapshots that fall outside of the new retention period will return an error. If you want to suppress the errors and delete the snapshots, use the force option.   
Type: Integer  
Required: No

## Response Elements
<a name="API_BatchModifyClusterSnapshots_ResponseElements"></a>

The following elements are returned by the service.

 **Errors.SnapshotErrorMessage.N**   
A list of any errors returned.  
Type: Array of [SnapshotErrorMessage](API_SnapshotErrorMessage.md) objects

 **Resources.String.N**   
A list of the snapshots that were modified.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_BatchModifyClusterSnapshots_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BatchModifyClusterSnapshotsLimitExceededFault **   
The maximum number for snapshot identifiers has been reached. The limit is 100.   
HTTP Status Code: 400

 ** InvalidRetentionPeriodFault **   
The retention period specified is either in the past or is not a valid value.  
The value must be either -1 or an integer between 1 and 3,653.  
HTTP Status Code: 400

## Examples
<a name="API_BatchModifyClusterSnapshots_Examples"></a>

### Example
<a name="API_BatchModifyClusterSnapshots_Example_1"></a>

This example illustrates one usage of BatchModifyClusterSnapshots.

#### Sample Request
<a name="API_BatchModifyClusterSnapshots_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=BatchModifyClusterSnapshots
&SnapshotIdentifierList.String.1=mysnapshotid1
&SnapshotIdentifierList.String.2=mysnapshotid2
&ManualSnapshotRetentionPeriod=30
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_BatchModifyClusterSnapshots_Example_1_Response"></a>

```
<BatchModifyClusterSnapshotsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <BatchModifyClusterSnapshotsResult>
    <Resources>
      <String>mysnapshotid1</String>
      <String>mysnapshotid2</String>
    </Resources>
    <Errors/>
  </BatchModifyClusterSnapshotsResult>
  <ResponseMetadata>
    <RequestId>c10326d1-282d-11ea-8314-974e2ba81189</RequestId>
  </ResponseMetadata>
</BatchModifyClusterSnapshotsResponse>
```

## See Also
<a name="API_BatchModifyClusterSnapshots_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/BatchModifyClusterSnapshots) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/BatchModifyClusterSnapshots) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/BatchModifyClusterSnapshots) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/BatchModifyClusterSnapshots) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/BatchModifyClusterSnapshots) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/BatchModifyClusterSnapshots) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/BatchModifyClusterSnapshots) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/BatchModifyClusterSnapshots) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/BatchModifyClusterSnapshots) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/BatchModifyClusterSnapshots) 