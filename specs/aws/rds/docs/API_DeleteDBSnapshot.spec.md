---
id: "@specs/aws/rds/docs/API_DeleteDBSnapshot"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteDBSnapshot"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DeleteDBSnapshot

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DeleteDBSnapshot
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteDBSnapshot
<a name="API_DeleteDBSnapshot"></a>

Deletes a DB snapshot. If the snapshot is being copied, the copy operation is terminated.

**Note**  
The DB snapshot must be in the `available` state to be deleted.

## Request Parameters
<a name="API_DeleteDBSnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBSnapshotIdentifier **   
The DB snapshot identifier.  
Constraints: Must be the name of an existing DB snapshot in the `available` state.  
Type: String  
Required: Yes

## Response Elements
<a name="API_DeleteDBSnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** DBSnapshot **   
Contains the details of an Amazon RDS DB snapshot.  
This data type is used as a response element in the `DescribeDBSnapshots` action.  
Type: [DBSnapshot](API_DBSnapshot.md) object

## Errors
<a name="API_DeleteDBSnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBSnapshotNotFound **   
 `DBSnapshotIdentifier` doesn't refer to an existing DB snapshot.  
HTTP Status Code: 404

 ** InvalidDBSnapshotState **   
The state of the DB snapshot doesn't allow deletion.  
HTTP Status Code: 400

## Examples
<a name="API_DeleteDBSnapshot_Examples"></a>

### Example
<a name="API_DeleteDBSnapshot_Example_1"></a>

This example illustrates one usage of DeleteDBSnapshot.

#### Sample Request
<a name="API_DeleteDBSnapshot_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=DeleteDBSnapshot
   &DBSnapshotIdentifier=mysqldb-snap-02
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20210623/us-east-1/rds/aws4_request
   &X-Amz-Date=20210623T203337Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=619f04acffeb4b80d2f442526b1c9da79d0b3097151c24f28e83e851d6541414
```

#### Sample Response
<a name="API_DeleteDBSnapshot_Example_1_Response"></a>

```
<DeleteDBSnapshotResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DeleteDBSnapshotResult>
    <DBSnapshot>
      <Port>3306</Port>
      <OptionGroupName>default:mysql-5-6</OptionGroupName>
      <Status>deleted</Status>
      <Engine>mysql</Engine>
      <SnapshotType>manual</SnapshotType>
      <LicenseModel>general-public-license</LicenseModel>
      <DBInstanceIdentifier>mysqldb</DBInstanceIdentifier>
      <EngineVersion>5.6.44</EngineVersion>
      <DBSnapshotIdentifier>mysqldb-snap-02</DBSnapshotIdentifier>
      <SnapshotCreateTime>2021-04-27T08:16:05.356Z</SnapshotCreateTime>   
      <OriginalSnapshotCreateTime>2021-04-27T08:16:05.356Z</OriginalSnapshotCreateTime>    
      <AvailabilityZone>us-east-1a</AvailabilityZone>
      <InstanceCreateTime>2021-04-21T22:24:26.573Z</InstanceCreateTime>
      <PercentProgress>100</PercentProgress>
      <AllocatedStorage>100</AllocatedStorage>
      <MasterUsername>myawsuser</MasterUsername>
    </DBSnapshot>
  </DeleteDBSnapshotResult>
  <ResponseMetadata>
    <RequestId>7b17b2b1-ba25-11d3-a537-cef97546330c</RequestId>
  </ResponseMetadata>
</DeleteDBSnapshotResponse>
```

## See Also
<a name="API_DeleteDBSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DeleteDBSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DeleteDBSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DeleteDBSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DeleteDBSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DeleteDBSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DeleteDBSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DeleteDBSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DeleteDBSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DeleteDBSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DeleteDBSnapshot) 