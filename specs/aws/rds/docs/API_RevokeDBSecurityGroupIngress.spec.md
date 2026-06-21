---
id: "@specs/aws/rds/docs/API_RevokeDBSecurityGroupIngress"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RevokeDBSecurityGroupIngress"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# RevokeDBSecurityGroupIngress

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_RevokeDBSecurityGroupIngress
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RevokeDBSecurityGroupIngress
<a name="API_RevokeDBSecurityGroupIngress"></a>

Revokes ingress from a DBSecurityGroup for previously authorized IP ranges or EC2 or VPC security groups. Required parameters for this API are one of CIDRIP, EC2SecurityGroupId for VPC, or (EC2SecurityGroupOwnerId and either EC2SecurityGroupName or EC2SecurityGroupId).

**Note**  
EC2-Classic was retired on August 15, 2022. If you haven't migrated from EC2-Classic to a VPC, we recommend that you migrate as soon as possible. For more information, see [Migrate from EC2-Classic to a VPC](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-migrate.html) in the *Amazon EC2 User Guide*, the blog [EC2-Classic Networking is Retiring – Here’s How to Prepare](http://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/), and [Moving a DB instance not in a VPC into a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Non-VPC2VPC.html) in the *Amazon RDS User Guide*.

## Request Parameters
<a name="API_RevokeDBSecurityGroupIngress_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBSecurityGroupName **   
The name of the DB security group to revoke ingress from.  
Type: String  
Required: Yes

 ** CIDRIP **   
The IP range to revoke access from. Must be a valid CIDR range. If `CIDRIP` is specified, `EC2SecurityGroupName`, `EC2SecurityGroupId` and `EC2SecurityGroupOwnerId` can't be provided.  
Type: String  
Required: No

 ** EC2SecurityGroupId **   
The id of the EC2 security group to revoke access from. For VPC DB security groups, `EC2SecurityGroupId` must be provided. Otherwise, EC2SecurityGroupOwnerId and either `EC2SecurityGroupName` or `EC2SecurityGroupId` must be provided.  
Type: String  
Required: No

 ** EC2SecurityGroupName **   
The name of the EC2 security group to revoke access from. For VPC DB security groups, `EC2SecurityGroupId` must be provided. Otherwise, EC2SecurityGroupOwnerId and either `EC2SecurityGroupName` or `EC2SecurityGroupId` must be provided.  
Type: String  
Required: No

 ** EC2SecurityGroupOwnerId **   
The AWS account number of the owner of the EC2 security group specified in the `EC2SecurityGroupName` parameter. The AWS access key ID isn't an acceptable value. For VPC DB security groups, `EC2SecurityGroupId` must be provided. Otherwise, EC2SecurityGroupOwnerId and either `EC2SecurityGroupName` or `EC2SecurityGroupId` must be provided.  
Type: String  
Required: No

## Response Elements
<a name="API_RevokeDBSecurityGroupIngress_ResponseElements"></a>

The following element is returned by the service.

 ** DBSecurityGroup **   
Contains the details for an Amazon RDS DB security group.  
This data type is used as a response element in the `DescribeDBSecurityGroups` action.  
Type: [DBSecurityGroup](API_DBSecurityGroup.md) object

## Errors
<a name="API_RevokeDBSecurityGroupIngress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationNotFound **   
The specified CIDR IP range or Amazon EC2 security group might not be authorized for the specified DB security group.  
Or, RDS might not be authorized to perform necessary actions using IAM on your behalf.  
HTTP Status Code: 404

 ** DBSecurityGroupNotFound **   
 `DBSecurityGroupName` doesn't refer to an existing DB security group.  
HTTP Status Code: 404

 ** InvalidDBSecurityGroupState **   
The state of the DB security group doesn't allow deletion.  
HTTP Status Code: 400

## Examples
<a name="API_RevokeDBSecurityGroupIngress_Examples"></a>

### Example
<a name="API_RevokeDBSecurityGroupIngress_Example_1"></a>

This example illustrates one usage of RevokeDBSecurityGroupIngress.

#### Sample Request
<a name="API_RevokeDBSecurityGroupIngress_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=RevokeDBSecurityGroupIngress 
   &CIDRIP=192.0.0.1%2F32
   &DBSecurityGroupName=mydbsecuritygroup01
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140428/us-east-1/rds/aws4_request
   &X-Amz-Date=20140428T233956Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=d9edabccacae36138704fb2b3cf6755ef08123862191b19d74582497b75e544a
```

#### Sample Response
<a name="API_RevokeDBSecurityGroupIngress_Example_1_Response"></a>

```
<RevokeDBSecurityGroupIngressResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <RevokeDBSecurityGroupIngressResult>
    <DBSecurityGroup>
      <EC2SecurityGroups/>
      <DBSecurityGroupDescription>My new DBSecurityGroup</DBSecurityGroupDescription>
      <IPRanges>
        <IPRange>
          <CIDRIP>192.0.0.1/32</CIDRIP>
          <Status>revoking</Status>
        </IPRange>
      </IPRanges>
      <OwnerId>803#########</OwnerId>
      <DBSecurityGroupName>mydbsecuritygroup01</DBSecurityGroupName>
    </DBSecurityGroup>
  </RevokeDBSecurityGroupIngressResult>
  <ResponseMetadata>
    <RequestId>579d8ba0-be2d-11d3-ae4f-eec568ed6b36</RequestId>
  </ResponseMetadata>
</RevokeDBSecurityGroupIngressResponse>
```

## See Also
<a name="API_RevokeDBSecurityGroupIngress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/RevokeDBSecurityGroupIngress) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/RevokeDBSecurityGroupIngress) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/RevokeDBSecurityGroupIngress) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/RevokeDBSecurityGroupIngress) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/RevokeDBSecurityGroupIngress) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/RevokeDBSecurityGroupIngress) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/RevokeDBSecurityGroupIngress) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/RevokeDBSecurityGroupIngress) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/RevokeDBSecurityGroupIngress) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/RevokeDBSecurityGroupIngress) 