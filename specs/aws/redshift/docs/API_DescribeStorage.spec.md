---
id: "@specs/aws/redshift/docs/API_DescribeStorage"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeStorage"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeStorage

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeStorage
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeStorage
<a name="API_DescribeStorage"></a>

Returns account level backups storage size and provisional storage.

## Response Elements
<a name="API_DescribeStorage_ResponseElements"></a>

The following elements are returned by the service.

 ** TotalBackupSizeInMegaBytes **   
The total amount of storage currently used for snapshots.  
Type: Double

 ** TotalProvisionedStorageInMegaBytes **   
The total amount of storage currently provisioned.  
Type: Double

## Errors
<a name="API_DescribeStorage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeStorage_Examples"></a>

### Example
<a name="API_DescribeStorage_Example_1"></a>

This example illustrates one usage of DescribeStorage.

#### Sample Request
<a name="API_DescribeStorage_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeStorage
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeStorage_Example_1_Response"></a>

```
<DescribeStorageResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeStorageResult>
    <TotalProvisionedStorageInMegaBytes>491520.0</TotalProvisionedStorageInMegaBytes>
    <TotalBackupSizeInMegaBytes>26.0</TotalBackupSizeInMegaBytes>
  </DescribeStorageResult>
  <ResponseMetadata>
    <RequestId>d6b07363-28d3-11ea-8397-219d1980588b</RequestId>
  </ResponseMetadata>
</DescribeStorageResponse>
```

## See Also
<a name="API_DescribeStorage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeStorage) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeStorage) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeStorage) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeStorage) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeStorage) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeStorage) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeStorage) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeStorage) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeStorage) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeStorage) 