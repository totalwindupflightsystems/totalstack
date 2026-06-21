---
id: "@specs/aws/rds/docs/API_CreateDBParameterGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDBParameterGroup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# CreateDBParameterGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_CreateDBParameterGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDBParameterGroup
<a name="API_CreateDBParameterGroup"></a>

Creates a new DB parameter group.

A DB parameter group is initially created with the default parameters for the database engine used by the DB instance. To provide custom values for any of the parameters, you must modify the group after creating it using `ModifyDBParameterGroup`. Once you've created a DB parameter group, you need to associate it with your DB instance using `ModifyDBInstance`. When you associate a new DB parameter group with a running DB instance, you need to reboot the DB instance without failover for the new DB parameter group and associated settings to take effect.

This command doesn't apply to RDS Custom.

## Request Parameters
<a name="API_CreateDBParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBParameterGroupFamily **   
The DB parameter group family name. A DB parameter group can be associated with one and only one DB parameter group family, and can be applied only to a DB instance running a database engine and engine version compatible with that DB parameter group family.  
To list all of the available parameter group families for a DB engine, use the following command:  
 `aws rds describe-db-engine-versions --query "DBEngineVersions[].DBParameterGroupFamily" --engine <engine>`   
For example, to list all of the available parameter group families for the MySQL DB engine, use the following command:  
 `aws rds describe-db-engine-versions --query "DBEngineVersions[].DBParameterGroupFamily" --engine mysql`   
The output contains duplicates.
The following are the valid DB engine values:  
+  `aurora-mysql` 
+  `aurora-postgresql` 
+  `db2-ae` 
+  `db2-ce` 
+  `db2-se` 
+  `mysql` 
+  `oracle-ee` 
+  `oracle-ee-cdb` 
+  `oracle-se2` 
+  `oracle-se2-cdb` 
+  `postgres` 
+  `sqlserver-ee` 
+  `sqlserver-se` 
+  `sqlserver-ex` 
+  `sqlserver-web` 
Type: String  
Required: Yes

 ** DBParameterGroupName **   
The name of the DB parameter group.  
Constraints:  
+ Must be 1 to 255 letters, numbers, or hyphens.
+ First character must be a letter
+ Can't end with a hyphen or contain two consecutive hyphens
This value is stored as a lowercase string.
Type: String  
Required: Yes

 ** Description **   
The description for the DB parameter group.  
Type: String  
Required: Yes

 **Tags.Tag.N**   
Tags to assign to the DB parameter group.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateDBParameterGroup_ResponseElements"></a>

The following element is returned by the service.

 ** DBParameterGroup **   
Contains the details of an Amazon RDS DB parameter group.  
This data type is used as a response element in the `DescribeDBParameterGroups` action.  
Type: [DBParameterGroup](API_DBParameterGroup.md) object

## Errors
<a name="API_CreateDBParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBParameterGroupAlreadyExists **   
A DB parameter group with the same name exists.  
HTTP Status Code: 400

 ** DBParameterGroupQuotaExceeded **   
The request would result in the user exceeding the allowed number of DB parameter groups.  
HTTP Status Code: 400

## Examples
<a name="API_CreateDBParameterGroup_Examples"></a>

### Example
<a name="API_CreateDBParameterGroup_Example_1"></a>

This example illustrates one usage of CreateDBParameterGroup.

#### Sample Request
<a name="API_CreateDBParameterGroup_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=CreateDBParameterGroup
   &DBParameterGroupFamily=MySQL5.1
   &DBParameterGroupName=mydbparamgroup3
   &Description=My%20new%20DB%20Parameter%20Group
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140423/us-east-1/rds/aws4_request
   &X-Amz-Date=20140423T201938Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=e9e5e723f627e872e8bccdc6ccc60bdffcf4a32ae6758ef0a3717ffae49097ae
```

#### Sample Response
<a name="API_CreateDBParameterGroup_Example_1_Response"></a>

```
<CreateDBParameterGroupResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <CreateDBParameterGroupResult>
    <DBParameterGroup>
      <DBParameterGroupFamily>mysql5.1</DBParameterGroupFamily>
      <Description>My new DB Parameter Group</Description>
      <DBParameterGroupName>mydbparamgroup3</DBParameterGroupName>
    </DBParameterGroup>
  </CreateDBParameterGroupResult>
  <ResponseMetadata>
    <RequestId>7805c127-af22-11c3-96ac-6999cc5f7e72</RequestId>
  </ResponseMetadata>
</CreateDBParameterGroupResponse>
```

## See Also
<a name="API_CreateDBParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/CreateDBParameterGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/CreateDBParameterGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CreateDBParameterGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/CreateDBParameterGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CreateDBParameterGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/CreateDBParameterGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/CreateDBParameterGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/CreateDBParameterGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/CreateDBParameterGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CreateDBParameterGroup) 