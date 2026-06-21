---
id: "@specs/aws/rds/docs/API_DescribeDBSnapshotAttributes"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBSnapshotAttributes"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeDBSnapshotAttributes

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeDBSnapshotAttributes
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBSnapshotAttributes
<a name="API_DescribeDBSnapshotAttributes"></a>

Returns a list of DB snapshot attribute names and values for a manual DB snapshot.

When sharing snapshots with other AWS accounts, `DescribeDBSnapshotAttributes` returns the `restore` attribute and a list of IDs for the AWS accounts that are authorized to copy or restore the manual DB snapshot. If `all` is included in the list of values for the `restore` attribute, then the manual DB snapshot is public and can be copied or restored by all AWS accounts.

To add or remove access for an AWS account to copy or restore a manual DB snapshot, or to make the manual DB snapshot public or private, use the `ModifyDBSnapshotAttribute` API action.

## Request Parameters
<a name="API_DescribeDBSnapshotAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBSnapshotIdentifier **   
The identifier for the DB snapshot to describe the attributes for.  
Type: String  
Required: Yes

## Response Elements
<a name="API_DescribeDBSnapshotAttributes_ResponseElements"></a>

The following element is returned by the service.

 ** DBSnapshotAttributesResult **   
Contains the results of a successful call to the `DescribeDBSnapshotAttributes` API action.  
Manual DB snapshot attributes are used to authorize other AWS accounts to copy or restore a manual DB snapshot. For more information, see the `ModifyDBSnapshotAttribute` API action.  
Type: [DBSnapshotAttributesResult](API_DBSnapshotAttributesResult.md) object

## Errors
<a name="API_DescribeDBSnapshotAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBSnapshotNotFound **   
 `DBSnapshotIdentifier` doesn't refer to an existing DB snapshot.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeDBSnapshotAttributes_Examples"></a>

### Example
<a name="API_DescribeDBSnapshotAttributes_Example_1"></a>

This example illustrates one usage of DescribeDBSnapshotAttributes.

#### Sample Request
<a name="API_DescribeDBSnapshotAttributes_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
    ?Action=DescribeDBSnapshotAttributes
    &DBSnapshotIdentifier=manual-snapshot1
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20151027/us-east-1/rds/aws4_request
    &X-Amz-Date=20151027T210706Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=27413f450dfac3d68b2197453e52109bacd3863f9df1a02d6e40022165bb2e09
```

#### Sample Response
<a name="API_DescribeDBSnapshotAttributes_Example_1_Response"></a>

```
<DescribeDBSnapshotAttributesResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeDBSnapshotAttributesResult>
    <DBSnapshotAttributesResult>
      <DBSnapshotAttributes>
        <DBSnapshotAttribute>
          <AttributeName>restore</AttributeName>
          <AttributeValues>
            <AttributeValue>012345678901</AttributeValue>
          </AttributeValues>
        </DBSnapshotAttribute>
      </DBSnapshotAttributes>
      <DBSnapshotIdentifier>manual-snapshot1</DBSnapshotIdentifier>
    </DBSnapshotAttributesResult>
  </DescribeDBSnapshotAttributesResult>
  <ResponseMetadata>
    <RequestId>ae5be4a2-7cee-11e5-a056-f1c189649a47</RequestId>
  </ResponseMetadata>
</DescribeDBSnapshotAttributesResponse>
```

## See Also
<a name="API_DescribeDBSnapshotAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBSnapshotAttributes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBSnapshotAttributes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBSnapshotAttributes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBSnapshotAttributes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBSnapshotAttributes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBSnapshotAttributes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBSnapshotAttributes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBSnapshotAttributes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBSnapshotAttributes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBSnapshotAttributes) 