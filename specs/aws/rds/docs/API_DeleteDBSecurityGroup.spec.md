---
id: "@specs/aws/rds/docs/API_DeleteDBSecurityGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteDBSecurityGroup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DeleteDBSecurityGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DeleteDBSecurityGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteDBSecurityGroup
<a name="API_DeleteDBSecurityGroup"></a>

Deletes a DB security group.

The specified DB security group must not be associated with any DB instances.

**Note**  
EC2-Classic was retired on August 15, 2022. If you haven't migrated from EC2-Classic to a VPC, we recommend that you migrate as soon as possible. For more information, see [Migrate from EC2-Classic to a VPC](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-migrate.html) in the *Amazon EC2 User Guide*, the blog [EC2-Classic Networking is Retiring – Here’s How to Prepare](http://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/), and [Moving a DB instance not in a VPC into a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Non-VPC2VPC.html) in the *Amazon RDS User Guide*.

## Request Parameters
<a name="API_DeleteDBSecurityGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBSecurityGroupName **   
The name of the DB security group to delete.  
You can't delete the default DB security group.
Constraints:  
+ Must be 1 to 255 letters, numbers, or hyphens.
+ First character must be a letter
+ Can't end with a hyphen or contain two consecutive hyphens
+ Must not be "Default"
Type: String  
Required: Yes

## Errors
<a name="API_DeleteDBSecurityGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBSecurityGroupNotFound **   
 `DBSecurityGroupName` doesn't refer to an existing DB security group.  
HTTP Status Code: 404

 ** InvalidDBSecurityGroupState **   
The state of the DB security group doesn't allow deletion.  
HTTP Status Code: 400

## Examples
<a name="API_DeleteDBSecurityGroup_Examples"></a>

### Example
<a name="API_DeleteDBSecurityGroup_Example_1"></a>

This example illustrates one usage of DeleteDBSecurityGroup.

#### Sample Request
<a name="API_DeleteDBSecurityGroup_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=DeleteDBSecurityGroup
   &DBSecurityGroupName=mydbsecuritygroup
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31 
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140423/us-east-1/rds/aws4_request
   &X-Amz-Date=20140423T203336Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=873c15061fe60b9db8ea63137e5af82b157019696fc3e9764ef2abd9d71c640a
```

#### Sample Response
<a name="API_DeleteDBSecurityGroup_Example_1_Response"></a>

```
<DeleteDBSecurityGroupResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ResponseMetadata>
    <RequestId>7aec7454-ba25-11d3-855b-576787000e19</RequestId>
  </ResponseMetadata>
</DeleteDBSecurityGroupResponse>
```

## See Also
<a name="API_DeleteDBSecurityGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DeleteDBSecurityGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DeleteDBSecurityGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DeleteDBSecurityGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DeleteDBSecurityGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DeleteDBSecurityGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DeleteDBSecurityGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DeleteDBSecurityGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DeleteDBSecurityGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DeleteDBSecurityGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DeleteDBSecurityGroup) 