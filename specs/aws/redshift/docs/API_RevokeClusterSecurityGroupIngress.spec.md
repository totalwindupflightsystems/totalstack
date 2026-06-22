---
id: "@specs/aws/redshift/docs/API_RevokeClusterSecurityGroupIngress"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RevokeClusterSecurityGroupIngress"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# RevokeClusterSecurityGroupIngress

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_RevokeClusterSecurityGroupIngress
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RevokeClusterSecurityGroupIngress
<a name="API_RevokeClusterSecurityGroupIngress"></a>

Revokes an ingress rule in an Amazon Redshift security group for a previously authorized IP range or Amazon EC2 security group. To add an ingress rule, see [AuthorizeClusterSecurityGroupIngress](API_AuthorizeClusterSecurityGroupIngress.md). For information about managing security groups, go to [Amazon Redshift Cluster Security Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html) in the *Amazon Redshift Cluster Management Guide*. 

## Request Parameters
<a name="API_RevokeClusterSecurityGroupIngress_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterSecurityGroupName **   
The name of the security Group from which to revoke the ingress rule.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** CIDRIP **   
The IP range for which to revoke access. This range must be a valid Classless Inter-Domain Routing (CIDR) block of IP addresses. If `CIDRIP` is specified, `EC2SecurityGroupName` and `EC2SecurityGroupOwnerId` cannot be provided.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** EC2SecurityGroupName **   
The name of the EC2 Security Group whose access is to be revoked. If `EC2SecurityGroupName` is specified, `EC2SecurityGroupOwnerId` must also be provided and `CIDRIP` cannot be provided.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** EC2SecurityGroupOwnerId **   
The AWS account number of the owner of the security group specified in the `EC2SecurityGroupName` parameter. The AWS access key ID is not an acceptable value. If `EC2SecurityGroupOwnerId` is specified, `EC2SecurityGroupName` must also be provided. and `CIDRIP` cannot be provided.   
Example: `111122223333`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_RevokeClusterSecurityGroupIngress_ResponseElements"></a>

The following element is returned by the service.

 ** ClusterSecurityGroup **   
Describes a security group.  
Type: [ClusterSecurityGroup](API_ClusterSecurityGroup.md) object

## Errors
<a name="API_RevokeClusterSecurityGroupIngress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationNotFound **   
The specified CIDR IP range or EC2 security group is not authorized for the specified cluster security group.  
HTTP Status Code: 404

 ** ClusterSecurityGroupNotFound **   
The cluster security group name does not refer to an existing cluster security group.  
HTTP Status Code: 404

 ** InvalidClusterSecurityGroupState **   
The state of the cluster security group is not `available`.   
HTTP Status Code: 400

## Examples
<a name="API_RevokeClusterSecurityGroupIngress_Examples"></a>

### Example
<a name="API_RevokeClusterSecurityGroupIngress_Example_1"></a>

This example illustrates one usage of RevokeClusterSecurityGroupIngress.

#### Sample Request
<a name="API_RevokeClusterSecurityGroupIngress_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
    ?Action=RevokeClusterSecurityGroupIngress
    &ClusterSecurityGroupName=securitygroup1
    &CIDRIP=192.168.40.3/32
    &Version=2012-12-01
    &x-amz-algorithm=AWS4-HMAC-SHA256
    &x-amz-credential=AKIAIOSFODNN7EXAMPLE/20130123/us-east-2/redshift/aws4_request
    &x-amz-date=20130123T021606Z
    &x-amz-signedheaders=content-type;host;x-amz-date
```

#### Sample Response
<a name="API_RevokeClusterSecurityGroupIngress_Example_1_Response"></a>

```
<RevokeClusterSecurityGroupIngressResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <RevokeClusterSecurityGroupIngressResult>
    <ClusterSecurityGroup>
      <EC2SecurityGroups/>
      <IPRanges/>
      <Description>my security group</Description>
      <ClusterSecurityGroupName>securitygroup1</ClusterSecurityGroupName>
    </ClusterSecurityGroup>
  </RevokeClusterSecurityGroupIngressResult>
  <ResponseMetadata>
    <RequestId>d8eff363-6502-11e2-a8da-655adc216806</RequestId>
  </ResponseMetadata>
</RevokeClusterSecurityGroupIngressResponse>
```

## See Also
<a name="API_RevokeClusterSecurityGroupIngress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/RevokeClusterSecurityGroupIngress) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/RevokeClusterSecurityGroupIngress) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/RevokeClusterSecurityGroupIngress) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/RevokeClusterSecurityGroupIngress) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/RevokeClusterSecurityGroupIngress) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/RevokeClusterSecurityGroupIngress) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/RevokeClusterSecurityGroupIngress) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/RevokeClusterSecurityGroupIngress) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/RevokeClusterSecurityGroupIngress) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/RevokeClusterSecurityGroupIngress) 