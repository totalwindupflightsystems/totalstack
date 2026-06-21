---
id: "@specs/aws/rds/docs/API_CreateDBSecurityGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDBSecurityGroup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# CreateDBSecurityGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_CreateDBSecurityGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDBSecurityGroup
<a name="API_CreateDBSecurityGroup"></a>

Creates a new DB security group. DB security groups control access to a DB instance.

A DB security group controls access to EC2-Classic DB instances that are not in a VPC.

**Note**  
EC2-Classic was retired on August 15, 2022. If you haven't migrated from EC2-Classic to a VPC, we recommend that you migrate as soon as possible. For more information, see [Migrate from EC2-Classic to a VPC](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-migrate.html) in the *Amazon EC2 User Guide*, the blog [EC2-Classic Networking is Retiring – Here’s How to Prepare](http://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/), and [Moving a DB instance not in a VPC into a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Non-VPC2VPC.html) in the *Amazon RDS User Guide*.

## Request Parameters
<a name="API_CreateDBSecurityGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBSecurityGroupDescription **   
The description for the DB security group.  
Type: String  
Required: Yes

 ** DBSecurityGroupName **   
The name for the DB security group. This value is stored as a lowercase string.  
Constraints:  
+ Must be 1 to 255 letters, numbers, or hyphens.
+ First character must be a letter
+ Can't end with a hyphen or contain two consecutive hyphens
+ Must not be "Default"
Example: `mysecuritygroup`   
Type: String  
Required: Yes

 **Tags.Tag.N**   
Tags to assign to the DB security group.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateDBSecurityGroup_ResponseElements"></a>

The following element is returned by the service.

 ** DBSecurityGroup **   
Contains the details for an Amazon RDS DB security group.  
This data type is used as a response element in the `DescribeDBSecurityGroups` action.  
Type: [DBSecurityGroup](API_DBSecurityGroup.md) object

## Errors
<a name="API_CreateDBSecurityGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBSecurityGroupAlreadyExists **   
A DB security group with the name specified in `DBSecurityGroupName` already exists.  
HTTP Status Code: 400

 ** DBSecurityGroupNotSupported **   
A DB security group isn't allowed for this action.  
HTTP Status Code: 400

 ** QuotaExceeded.DBSecurityGroup **   
The request would result in the user exceeding the allowed number of DB security groups.  
HTTP Status Code: 400

## Examples
<a name="API_CreateDBSecurityGroup_Examples"></a>

### Example
<a name="API_CreateDBSecurityGroup_Example_1"></a>

This example illustrates one usage of CreateDBSecurityGroup.

#### Sample Request
<a name="API_CreateDBSecurityGroup_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=CreateDBSecurityGroup
   &DBSecurityGroupDescription=My%20new%20DB%20Security%20Group
   &DBSecurityGroupName=mydbsecuritygroup00
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140424/us-east-1/rds/aws4_request
   &X-Amz-Date=20140424T190716Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=c2f180a3f0f5d73b47f9c229937a78f3569bf14392db8093d9b2e6785609ab45
```

#### Sample Response
<a name="API_CreateDBSecurityGroup_Example_1_Response"></a>

```
<CreateDBSecurityGroupResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <CreateDBSecurityGroupResult>
    <DBSecurityGroup>
      <EC2SecurityGroups/>
      <DBSecurityGroupDescription>My new DB Security Group</DBSecurityGroupDescription>
      <IPRanges/>
      <OwnerId>803#########</OwnerId>
      <DBSecurityGroupName>mydbsecuritygroup00</DBSecurityGroupName>
    </DBSecurityGroup>
  </CreateDBSecurityGroupResult>
  <ResponseMetadata>
    <RequestId>e68ef6fa-afc1-11c3-845a-476777009d19</RequestId>
  </ResponseMetadata>
</CreateDBSecurityGroupResponse>
```

## See Also
<a name="API_CreateDBSecurityGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/CreateDBSecurityGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/CreateDBSecurityGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CreateDBSecurityGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/CreateDBSecurityGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CreateDBSecurityGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/CreateDBSecurityGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/CreateDBSecurityGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/CreateDBSecurityGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/CreateDBSecurityGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CreateDBSecurityGroup) 