---
id: "@specs/aws/redshift/docs/API_DescribeClusterTracks"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeClusterTracks"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeClusterTracks

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeClusterTracks
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeClusterTracks
<a name="API_DescribeClusterTracks"></a>

Returns a list of all the available maintenance tracks.

## Request Parameters
<a name="API_DescribeClusterTracks_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** MaintenanceTrackName **   
The name of the maintenance track.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a `DescribeClusterTracks` request exceed the value specified in `MaxRecords`, Amazon Redshift returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
An integer value for the maximum number of maintenance tracks to return.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeClusterTracks_ResponseElements"></a>

The following elements are returned by the service.

 **MaintenanceTracks.MaintenanceTrack.N**   
A list of maintenance tracks output by the `DescribeClusterTracks` operation.   
Type: Array of [MaintenanceTrack](API_MaintenanceTrack.md) objects

 ** Marker **   
The starting point to return a set of response tracklist records. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.  
Type: String  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_DescribeClusterTracks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidClusterTrack **   
The provided cluster track name is not valid.  
HTTP Status Code: 400

 ** UnauthorizedOperation **   
Your account is not authorized to perform the requested operation.  
HTTP Status Code: 400

## Examples
<a name="API_DescribeClusterTracks_Examples"></a>

### Example
<a name="API_DescribeClusterTracks_Example_1"></a>

This example illustrates one usage of DescribeClusterTracks.

#### Sample Request
<a name="API_DescribeClusterTracks_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeClusterTracks
&MaintenanceTrackName=current
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeClusterTracks_Example_1_Response"></a>

```
<DescribeClusterTracksResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeClusterTracksResult>
    <MaintenanceTracks>
      <MaintenanceTrack>
        <UpdateTargets>
          <UpdateTarget>
            <DatabaseVersion>1.0.11746</DatabaseVersion>
            <MaintenanceTrackName>preview_features</MaintenanceTrackName>
            <SupportedOperations>
              <SupportedOperation>
                <OperationName>restore-from-cluster-snapshot</OperationName>
              </SupportedOperation>
            </SupportedOperations>
          </UpdateTarget>
          <UpdateTarget>
            <DatabaseVersion>1.0.11116</DatabaseVersion>
            <MaintenanceTrackName>trailing</MaintenanceTrackName>
            <SupportedOperations>
              <SupportedOperation>
                <OperationName>restore-from-cluster-snapshot</OperationName>
              </SupportedOperation>
              <SupportedOperation>
                <OperationName>modify-cluster</OperationName>
              </SupportedOperation>
            </SupportedOperations>
          </UpdateTarget>
        </UpdateTargets>
        <DatabaseVersion>1.0.11978</DatabaseVersion>
        <MaintenanceTrackName>current</MaintenanceTrackName>
      </MaintenanceTrack>
    </MaintenanceTracks>
  </DescribeClusterTracksResult>
  <ResponseMetadata>
    <RequestId>7db182a3-283e-11ea-9caa-c956bec1ce87</RequestId>
  </ResponseMetadata>
</DescribeClusterTracksResponse>
```

## See Also
<a name="API_DescribeClusterTracks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeClusterTracks) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeClusterTracks) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeClusterTracks) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeClusterTracks) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeClusterTracks) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeClusterTracks) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeClusterTracks) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeClusterTracks) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeClusterTracks) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeClusterTracks) 