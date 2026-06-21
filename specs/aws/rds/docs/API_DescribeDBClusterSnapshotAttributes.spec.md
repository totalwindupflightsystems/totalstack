---
id: "@specs/aws/rds/docs/API_DescribeDBClusterSnapshotAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBClusterSnapshotAttributes"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeDBClusterSnapshotAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeDBClusterSnapshotAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBClusterSnapshotAttributes
<a name="API_DescribeDBClusterSnapshotAttributes"></a>

Returns a list of DB cluster snapshot attribute names and values for a manual DB cluster snapshot.

When sharing snapshots with other AWS accounts, `DescribeDBClusterSnapshotAttributes` returns the `restore` attribute and a list of IDs for the AWS accounts that are authorized to copy or restore the manual DB cluster snapshot. If `all` is included in the list of values for the `restore` attribute, then the manual DB cluster snapshot is public and can be copied or restored by all AWS accounts.

To add or remove access for an AWS account to copy or restore a manual DB cluster snapshot, or to make the manual DB cluster snapshot public or private, use the `ModifyDBClusterSnapshotAttribute` API action.

## Request Parameters
<a name="API_DescribeDBClusterSnapshotAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterSnapshotIdentifier **   
The identifier for the DB cluster snapshot to describe the attributes for.  
Type: String  
Required: Yes

## Response Elements
<a name="API_DescribeDBClusterSnapshotAttributes_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterSnapshotAttributesResult **   
Contains the results of a successful call to the `DescribeDBClusterSnapshotAttributes` API action.  
Manual DB cluster snapshot attributes are used to authorize other AWS accounts to copy or restore a manual DB cluster snapshot. For more information, see the `ModifyDBClusterSnapshotAttribute` API action.  
Type: [DBClusterSnapshotAttributesResult](API_DBClusterSnapshotAttributesResult.md) object

## Errors
<a name="API_DescribeDBClusterSnapshotAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterSnapshotNotFoundFault **   
 `DBClusterSnapshotIdentifier` doesn't refer to an existing DB cluster snapshot.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeDBClusterSnapshotAttributes_Examples"></a>

### Example
<a name="API_DescribeDBClusterSnapshotAttributes_Example_1"></a>

This example illustrates one usage of DescribeDBClusterSnapshotAttributes.

#### Sample Request
<a name="API_DescribeDBClusterSnapshotAttributes_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
    ?Action=DescribeDBClusterSnapshotAttributes
    &DBClusterSnapshotIdentifier=manual-cluster-snapshot1
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20230227/us-east-1/rds/aws4_request
    &X-Amz-Date=20230227T210706Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=27413f450dfac3d68b2197453e52109bacd3863f9df1a02d6e40022165bb2e09
```

#### Sample Response
<a name="API_DescribeDBClusterSnapshotAttributes_Example_1_Response"></a>

```
<DescribeDBClusterSnapshotAttributesResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeDBClusterSnapshotAttributesResult>
    <DBClusterSnapshotAttributesResult>
      <DBClusterSnapshotAttributes>
        <DBClusterSnapshotAttribute>
          <AttributeName>restore</AttributeName>
          <AttributeValues>
            <AttributeValue>012345678901</AttributeValue>
          </AttributeValues>
        </DBClusterSnapshotAttribute>
      </DBClusterSnapshotAttributes>
      <DBSnapshotIdentifier>manual-cluster-snapshot1</DBSnapshotIdentifier>
    </DBClusterSnapshotAttributesResult>
  </DescribeDBClusterSnapshotAttributesResult>
  <ResponseMetadata>
    <RequestId>ae5be4a2-7cee-11e5-a056-f1c189649a47</RequestId>
  </ResponseMetadata>
</DescribeDBClusterSnapshotAttributesResponse>
```

## See Also
<a name="API_DescribeDBClusterSnapshotAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBClusterSnapshotAttributes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBClusterSnapshotAttributes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBClusterSnapshotAttributes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBClusterSnapshotAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBClusterSnapshotAttributes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBClusterSnapshotAttributes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBClusterSnapshotAttributes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBClusterSnapshotAttributes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBClusterSnapshotAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBClusterSnapshotAttributes) 