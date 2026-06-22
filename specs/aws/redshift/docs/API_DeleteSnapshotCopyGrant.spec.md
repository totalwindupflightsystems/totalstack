---
id: "@specs/aws/redshift/docs/API_DeleteSnapshotCopyGrant"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteSnapshotCopyGrant"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DeleteSnapshotCopyGrant

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DeleteSnapshotCopyGrant
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteSnapshotCopyGrant
<a name="API_DeleteSnapshotCopyGrant"></a>

Deletes the specified snapshot copy grant.

## Request Parameters
<a name="API_DeleteSnapshotCopyGrant_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SnapshotCopyGrantName **   
The name of the snapshot copy grant to delete.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Errors
<a name="API_DeleteSnapshotCopyGrant_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidSnapshotCopyGrantStateFault **   
The snapshot copy grant can't be deleted because it is used by one or more clusters.  
HTTP Status Code: 400

 ** SnapshotCopyGrantNotFoundFault **   
The specified snapshot copy grant can't be found. Make sure that the name is typed correctly and that the grant exists in the destination region.  
HTTP Status Code: 400

## Examples
<a name="API_DeleteSnapshotCopyGrant_Examples"></a>

### Example
<a name="API_DeleteSnapshotCopyGrant_Example_1"></a>

This example illustrates one usage of DeleteSnapshotCopyGrant.

#### Sample Request
<a name="API_DeleteSnapshotCopyGrant_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DeleteSnapshotCopyGrant
&SnapshotCopyGrantName=mysnapshotcopygrantname
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DeleteSnapshotCopyGrant_Example_1_Response"></a>

```
<DeleteSnapshotCopyGrantResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <ResponseMetadata>
    <RequestId>a0c0f3ad-283c-11ea-a940-1b28a85fd753</RequestId>
  </ResponseMetadata>
</DeleteSnapshotCopyGrantResponse>
```

## See Also
<a name="API_DeleteSnapshotCopyGrant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DeleteSnapshotCopyGrant) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DeleteSnapshotCopyGrant) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DeleteSnapshotCopyGrant) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DeleteSnapshotCopyGrant) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DeleteSnapshotCopyGrant) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DeleteSnapshotCopyGrant) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DeleteSnapshotCopyGrant) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DeleteSnapshotCopyGrant) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DeleteSnapshotCopyGrant) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DeleteSnapshotCopyGrant) 