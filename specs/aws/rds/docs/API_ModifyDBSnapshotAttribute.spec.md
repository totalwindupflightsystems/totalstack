---
id: "@specs/aws/rds/docs/API_ModifyDBSnapshotAttribute"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyDBSnapshotAttribute"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# ModifyDBSnapshotAttribute

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_ModifyDBSnapshotAttribute
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyDBSnapshotAttribute
<a name="API_ModifyDBSnapshotAttribute"></a>

Adds an attribute and values to, or removes an attribute and values from, a manual DB snapshot.

To share a manual DB snapshot with other AWS accounts, specify `restore` as the `AttributeName` and use the `ValuesToAdd` parameter to add a list of IDs of the AWS accounts that are authorized to restore the manual DB snapshot. Uses the value `all` to make the manual DB snapshot public, which means it can be copied or restored by all AWS accounts.

**Note**  
Don't add the `all` value for any manual DB snapshots that contain private information that you don't want available to all AWS accounts.

If the manual DB snapshot is encrypted, it can be shared, but only by specifying a list of authorized AWS account IDs for the `ValuesToAdd` parameter. You can't use `all` as a value for that parameter in this case.

To view which AWS accounts have access to copy or restore a manual DB snapshot, or whether a manual DB snapshot public or private, use the [DescribeDBSnapshotAttributes](API_DescribeDBSnapshotAttributes.md) API operation. The accounts are returned as values for the `restore` attribute.

## Request Parameters
<a name="API_ModifyDBSnapshotAttribute_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AttributeName **   
The name of the DB snapshot attribute to modify.  
To manage authorization for other AWS accounts to copy or restore a manual DB snapshot, set this value to `restore`.  
To view the list of attributes available to modify, use the [DescribeDBSnapshotAttributes](API_DescribeDBSnapshotAttributes.md) API operation.
Type: String  
Required: Yes

 ** DBSnapshotIdentifier **   
The identifier for the DB snapshot to modify the attributes for.  
Type: String  
Required: Yes

 **ValuesToAdd.AttributeValue.N**   
A list of DB snapshot attributes to add to the attribute specified by `AttributeName`.  
To authorize other AWS accounts to copy or restore a manual snapshot, set this list to include one or more AWS account IDs, or `all` to make the manual DB snapshot restorable by any AWS account. Do not add the `all` value for any manual DB snapshots that contain private information that you don't want available to all AWS accounts.  
Type: Array of strings  
Required: No

 **ValuesToRemove.AttributeValue.N**   
A list of DB snapshot attributes to remove from the attribute specified by `AttributeName`.  
To remove authorization for other AWS accounts to copy or restore a manual snapshot, set this list to include one or more AWS account identifiers, or `all` to remove authorization for any AWS account to copy or restore the DB snapshot. If you specify `all`, an AWS account whose account ID is explicitly added to the `restore` attribute can still copy or restore the manual DB snapshot.  
Type: Array of strings  
Required: No

## Response Elements
<a name="API_ModifyDBSnapshotAttribute_ResponseElements"></a>

The following element is returned by the service.

 ** DBSnapshotAttributesResult **   
Contains the results of a successful call to the `DescribeDBSnapshotAttributes` API action.  
Manual DB snapshot attributes are used to authorize other AWS accounts to copy or restore a manual DB snapshot. For more information, see the `ModifyDBSnapshotAttribute` API action.  
Type: [DBSnapshotAttributesResult](API_DBSnapshotAttributesResult.md) object

## Errors
<a name="API_ModifyDBSnapshotAttribute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBSnapshotNotFound **   
 `DBSnapshotIdentifier` doesn't refer to an existing DB snapshot.  
HTTP Status Code: 404

 ** InvalidDBSnapshotState **   
The state of the DB snapshot doesn't allow deletion.  
HTTP Status Code: 400

 ** SharedSnapshotQuotaExceeded **   
You have exceeded the maximum number of accounts that you can share a manual DB snapshot with.  
HTTP Status Code: 400

## Examples
<a name="API_ModifyDBSnapshotAttribute_Examples"></a>

### Example
<a name="API_ModifyDBSnapshotAttribute_Example_1"></a>

This example illustrates one usage of ModifyDBSnapshotAttribute.

#### Sample Request
<a name="API_ModifyDBSnapshotAttribute_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
    ?Action=ModifyDBSnapshotAttribute
    &AttributeName=restore
    &DBSnapshotIdentifier=manual-snapshot1
    &SignatureMethod=HmacSHA256&SignatureVersion=4
    &ValuesToAdd.member.1=123451234512
    &ValuesToAdd.member.2=123456789012
    &ValuesToRemove.member.1=all
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20150922/us-west-2/rds/aws4_request
    &X-Amz-Date=20150922T220515Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=ef38f1ce3dab4e1dbf113d8d2a265c67d17ece1999ffd36be85714ed36dddbb3
```

#### Sample Response
<a name="API_ModifyDBSnapshotAttribute_Example_1_Response"></a>

```
<ModifyDBSnapshotAttributeResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ModifyDBSnapshotAttributeResult>
    <DBSnapshotAttributesResult>
      <DBSnapshotAttributes>
        <DBSnapshotAttribute>
          <AttributeName>restore</AttributeName>
          <AttributeValues>
            <AttributeValue>123451234512</AttributeValue>
            <AttributeValue>123456789012</AttributeValue>
          </AttributeValues>
        </DBSnapshotAttribute>
      </DBSnapshotAttributes>
      <DBSnapshotIdentifier>manual-snapshot1</DBSnapshotIdentifier>
    </DBSnapshotAttributesResult>
  </ModifyDBSnapshotAttributeResult>
  <ResponseMetadata>
    <RequestId>0122a108-2276-11e5-9cc3-0f535cff56aa</RequestId>
  </ResponseMetadata>
</ModifyDBSnapshotAttributeResponse>
```

## See Also
<a name="API_ModifyDBSnapshotAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/ModifyDBSnapshotAttribute) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/ModifyDBSnapshotAttribute) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ModifyDBSnapshotAttribute) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/ModifyDBSnapshotAttribute) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ModifyDBSnapshotAttribute) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/ModifyDBSnapshotAttribute) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/ModifyDBSnapshotAttribute) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/ModifyDBSnapshotAttribute) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/ModifyDBSnapshotAttribute) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ModifyDBSnapshotAttribute) 