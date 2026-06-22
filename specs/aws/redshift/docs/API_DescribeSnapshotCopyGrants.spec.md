---
id: "@specs/aws/redshift/docs/API_DescribeSnapshotCopyGrants"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeSnapshotCopyGrants"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeSnapshotCopyGrants

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeSnapshotCopyGrants
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeSnapshotCopyGrants
<a name="API_DescribeSnapshotCopyGrants"></a>

Returns a list of snapshot copy grants owned by the AWS account in the destination region.

 For more information about managing snapshot copy grants, go to [Amazon Redshift Database Encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html) in the *Amazon Redshift Cluster Management Guide*. 

## Request Parameters
<a name="API_DescribeSnapshotCopyGrants_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a `DescribeSnapshotCopyGrant` request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Constraints: You can specify either the **SnapshotCopyGrantName** parameter or the **Marker** parameter, but not both.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `marker` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.   
Default: `100`   
Constraints: minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** SnapshotCopyGrantName **   
The name of the snapshot copy grant.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **TagKeys.TagKey.N**   
A tag key or keys for which you want to return all matching resources that are associated with the specified key or keys. For example, suppose that you have resources tagged with keys called `owner` and `environment`. If you specify both of these tag keys in the request, Amazon Redshift returns a response with all resources that have either or both of these tag keys associated with them.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **TagValues.TagValue.N**   
A tag value or values for which you want to return all matching resources that are associated with the specified value or values. For example, suppose that you have resources tagged with values called `admin` and `test`. If you specify both of these tag values in the request, Amazon Redshift returns a response with all resources that have either or both of these tag values associated with them.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DescribeSnapshotCopyGrants_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a `DescribeSnapshotCopyGrant` request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Constraints: You can specify either the **SnapshotCopyGrantName** parameter or the **Marker** parameter, but not both.   
Type: String  
Length Constraints: Maximum length of 2147483647.

 **SnapshotCopyGrants.SnapshotCopyGrant.N**   
The list of `SnapshotCopyGrant` objects.  
Type: Array of [SnapshotCopyGrant](API_SnapshotCopyGrant.md) objects

## Errors
<a name="API_DescribeSnapshotCopyGrants_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

 ** SnapshotCopyGrantNotFoundFault **   
The specified snapshot copy grant can't be found. Make sure that the name is typed correctly and that the grant exists in the destination region.  
HTTP Status Code: 400

## Examples
<a name="API_DescribeSnapshotCopyGrants_Examples"></a>

### Example
<a name="API_DescribeSnapshotCopyGrants_Example_1"></a>

This example illustrates one usage of DescribeSnapshotCopyGrants.

#### Sample Request
<a name="API_DescribeSnapshotCopyGrants_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeSnapshotCopyGrants
&SnapshotCopyGrantName=mysnapshotcopygrantnew
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeSnapshotCopyGrants_Example_1_Response"></a>

```
<DescribeSnapshotCopyGrantsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeSnapshotCopyGrantsResult>
    <SnapshotCopyGrants>
      <SnapshotCopyGrant>
        <SnapshotCopyGrantName>mysnapshotcopygrantnew</SnapshotCopyGrantName>
        <KmsKeyId>arn:aws:kms:us-east-2:123456789012:key/bPxRfih3yCo8nvbEXAMPLEKEY</KmsKeyId>
        <Tags/>
      </SnapshotCopyGrant>
    </SnapshotCopyGrants>
  </DescribeSnapshotCopyGrantsResult>
  <ResponseMetadata>
    <RequestId>3a843f76-28d2-11ea-9caa-c956bec1ce87</RequestId>
  </ResponseMetadata>
</DescribeSnapshotCopyGrantsResponse>
```

## See Also
<a name="API_DescribeSnapshotCopyGrants_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeSnapshotCopyGrants) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeSnapshotCopyGrants) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeSnapshotCopyGrants) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeSnapshotCopyGrants) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeSnapshotCopyGrants) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeSnapshotCopyGrants) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeSnapshotCopyGrants) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeSnapshotCopyGrants) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeSnapshotCopyGrants) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeSnapshotCopyGrants) 