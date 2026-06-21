---
id: "@specs/aws/rds/docs/API_AuthorizeDBSecurityGroupIngress"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AuthorizeDBSecurityGroupIngress"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# AuthorizeDBSecurityGroupIngress

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_AuthorizeDBSecurityGroupIngress
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AuthorizeDBSecurityGroupIngress
<a name="API_AuthorizeDBSecurityGroupIngress"></a>

Enables ingress to a DBSecurityGroup using one of two forms of authorization. First, EC2 or VPC security groups can be added to the DBSecurityGroup if the application using the database is running on EC2 or VPC instances. Second, IP ranges are available if the application accessing your database is running on the internet. Required parameters for this API are one of CIDR range, EC2SecurityGroupId for VPC, or (EC2SecurityGroupOwnerId and either EC2SecurityGroupName or EC2SecurityGroupId for non-VPC).

You can't authorize ingress from an EC2 security group in one AWS Region to an Amazon RDS DB instance in another. You can't authorize ingress from a VPC security group in one VPC to an Amazon RDS DB instance in another.

For an overview of CIDR ranges, go to the [Wikipedia Tutorial](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).

**Note**  
EC2-Classic was retired on August 15, 2022. If you haven't migrated from EC2-Classic to a VPC, we recommend that you migrate as soon as possible. For more information, see [Migrate from EC2-Classic to a VPC](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-migrate.html) in the *Amazon EC2 User Guide*, the blog [EC2-Classic Networking is Retiring – Here’s How to Prepare](http://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/), and [Moving a DB instance not in a VPC into a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Non-VPC2VPC.html) in the *Amazon RDS User Guide*.

## Request Parameters
<a name="API_AuthorizeDBSecurityGroupIngress_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBSecurityGroupName **   
The name of the DB security group to add authorization to.  
Type: String  
Required: Yes

 ** CIDRIP **   
The IP range to authorize.  
Type: String  
Required: No

 ** EC2SecurityGroupId **   
Id of the EC2 security group to authorize. For VPC DB security groups, `EC2SecurityGroupId` must be provided. Otherwise, `EC2SecurityGroupOwnerId` and either `EC2SecurityGroupName` or `EC2SecurityGroupId` must be provided.  
Type: String  
Required: No

 ** EC2SecurityGroupName **   
Name of the EC2 security group to authorize. For VPC DB security groups, `EC2SecurityGroupId` must be provided. Otherwise, `EC2SecurityGroupOwnerId` and either `EC2SecurityGroupName` or `EC2SecurityGroupId` must be provided.  
Type: String  
Required: No

 ** EC2SecurityGroupOwnerId **   
 AWS account number of the owner of the EC2 security group specified in the `EC2SecurityGroupName` parameter. The AWS access key ID isn't an acceptable value. For VPC DB security groups, `EC2SecurityGroupId` must be provided. Otherwise, `EC2SecurityGroupOwnerId` and either `EC2SecurityGroupName` or `EC2SecurityGroupId` must be provided.  
Type: String  
Required: No

## Response Elements
<a name="API_AuthorizeDBSecurityGroupIngress_ResponseElements"></a>

The following element is returned by the service.

 ** DBSecurityGroup **   
Contains the details for an Amazon RDS DB security group.  
This data type is used as a response element in the `DescribeDBSecurityGroups` action.  
Type: [DBSecurityGroup](API_DBSecurityGroup.md) object

## Errors
<a name="API_AuthorizeDBSecurityGroupIngress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationAlreadyExists **   
The specified CIDR IP range or Amazon EC2 security group is already authorized for the specified DB security group.  
HTTP Status Code: 400

 ** AuthorizationQuotaExceeded **   
The DB security group authorization quota has been reached.  
HTTP Status Code: 400

 ** DBSecurityGroupNotFound **   
 `DBSecurityGroupName` doesn't refer to an existing DB security group.  
HTTP Status Code: 404

 ** InvalidDBSecurityGroupState **   
The state of the DB security group doesn't allow deletion.  
HTTP Status Code: 400

## Examples
<a name="API_AuthorizeDBSecurityGroupIngress_Examples"></a>

### Example
<a name="API_AuthorizeDBSecurityGroupIngress_Example_1"></a>

This example illustrates one usage of AuthorizeDBSecurityGroupIngress.

#### Sample Request
<a name="API_AuthorizeDBSecurityGroupIngress_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=AuthorizeDBSecurityGroupIngress
   &CIDRIP=54.241.217.9%2F32
   &DBSecurityGroupName=default
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140423/us-east-1/rds/aws4_request
   &X-Amz-Date=20140423T154632Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=7803146e430626f47b0da058921cdb9f2ab7ffd881bd99fc859f2f635e4472bd
```

#### Sample Response
<a name="API_AuthorizeDBSecurityGroupIngress_Example_1_Response"></a>

```
<AuthorizeDBSecurityGroupIngressResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <AuthorizeDBSecurityGroupIngressResult>
    <DBSecurityGroup>
      <EC2SecurityGroups>
        <EC2SecurityGroup>
          <Status>authorized</Status>
          <EC2SecurityGroupName>elasticbeanstalk-windows</EC2SecurityGroupName>
          <EC2SecurityGroupOwnerId>803#########</EC2SecurityGroupOwnerId>
          <EC2SecurityGroupId>sg-7f476617</EC2SecurityGroupId>
        </EC2SecurityGroup>
      </EC2SecurityGroups>
      <DBSecurityGroupDescription>default</DBSecurityGroupDescription>
      <IPRanges>
        <IPRange>
          <CIDRIP>192.0.0.0/24</CIDRIP>
          <Status>authorized</Status>
        </IPRange>
        <IPRange>
          <CIDRIP>190.0.1.0/29</CIDRIP>
          <Status>authorized</Status>
        </IPRange>
        <IPRange>
          <CIDRIP>190.0.2.0/29</CIDRIP>
          <Status>authorized</Status>
        </IPRange>
        <IPRange>
          <CIDRIP>10.0.0.0/8</CIDRIP>
          <Status>authorized</Status>
        </IPRange>
      </IPRanges>
      <OwnerId>803#########</OwnerId>
      <DBSecurityGroupName>default</DBSecurityGroupName>
    </DBSecurityGroup>
  </AuthorizeDBSecurityGroupIngressResult>
  <ResponseMetadata>
    <RequestId>6176b5f8-bfed-11d3-f92b-31fa5e8dbc99</RequestId>
  </ResponseMetadata>
</AuthorizeDBSecurityGroupIngressResponse>
```

## See Also
<a name="API_AuthorizeDBSecurityGroupIngress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/AuthorizeDBSecurityGroupIngress) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/AuthorizeDBSecurityGroupIngress) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/AuthorizeDBSecurityGroupIngress) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/AuthorizeDBSecurityGroupIngress) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/AuthorizeDBSecurityGroupIngress) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/AuthorizeDBSecurityGroupIngress) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/AuthorizeDBSecurityGroupIngress) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/AuthorizeDBSecurityGroupIngress) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/AuthorizeDBSecurityGroupIngress) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/AuthorizeDBSecurityGroupIngress) 