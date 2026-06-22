---
id: "@specs/aws/redshift/docs/API_AuthorizeClusterSecurityGroupIngress"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AuthorizeClusterSecurityGroupIngress"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# AuthorizeClusterSecurityGroupIngress

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_AuthorizeClusterSecurityGroupIngress
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AuthorizeClusterSecurityGroupIngress
<a name="API_AuthorizeClusterSecurityGroupIngress"></a>

Adds an inbound (ingress) rule to an Amazon Redshift security group. Depending on whether the application accessing your cluster is running on the Internet or an Amazon EC2 instance, you can authorize inbound access to either a Classless Interdomain Routing (CIDR)/Internet Protocol (IP) range or to an Amazon EC2 security group. You can add as many as 20 ingress rules to an Amazon Redshift security group.

If you authorize access to an Amazon EC2 security group, specify *EC2SecurityGroupName* and *EC2SecurityGroupOwnerId*. The Amazon EC2 security group and Amazon Redshift cluster must be in the same AWS Region. 

If you authorize access to a CIDR/IP address range, specify *CIDRIP*. For an overview of CIDR blocks, see the Wikipedia article on [Classless Inter-Domain Routing](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing). 

You must also associate the security group with a cluster so that clients running on these IP addresses or the EC2 instance are authorized to connect to the cluster. For information about managing security groups, go to [Working with Security Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html) in the *Amazon Redshift Cluster Management Guide*.

## Request Parameters
<a name="API_AuthorizeClusterSecurityGroupIngress_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterSecurityGroupName **   
The name of the security group to which the ingress rule is added.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** CIDRIP **   
The IP range to be added the Amazon Redshift security group.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** EC2SecurityGroupName **   
The EC2 security group to be added the Amazon Redshift security group.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** EC2SecurityGroupOwnerId **   
The AWS account number of the owner of the security group specified by the *EC2SecurityGroupName* parameter. The AWS Access Key ID is not an acceptable value.   
Example: `111122223333`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_AuthorizeClusterSecurityGroupIngress_ResponseElements"></a>

The following element is returned by the service.

 ** ClusterSecurityGroup **   
Describes a security group.  
Type: [ClusterSecurityGroup](API_ClusterSecurityGroup.md) object

## Errors
<a name="API_AuthorizeClusterSecurityGroupIngress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationAlreadyExists **   
The specified CIDR block or EC2 security group is already authorized for the specified cluster security group.  
HTTP Status Code: 400

 ** AuthorizationQuotaExceeded **   
The authorization quota for the cluster security group has been reached.  
HTTP Status Code: 400

 ** ClusterSecurityGroupNotFound **   
The cluster security group name does not refer to an existing cluster security group.  
HTTP Status Code: 404

 ** InvalidClusterSecurityGroupState **   
The state of the cluster security group is not `available`.   
HTTP Status Code: 400

## Examples
<a name="API_AuthorizeClusterSecurityGroupIngress_Examples"></a>

### Example
<a name="API_AuthorizeClusterSecurityGroupIngress_Example_1"></a>

This example illustrates one usage of AuthorizeClusterSecurityGroupIngress.

#### Sample Request
<a name="API_AuthorizeClusterSecurityGroupIngress_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
    ?Action=AuthorizeClusterSecurityGroupIngress
    &CIDRIP=10.24.34.0/24
    &ClusterSecurityGroupName=example-security-group
    &SignatureMethod=HmacSHA256&SignatureVersion=4
    &Version=2012-12-01
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20150817/us-east-2/redshift/aws4_request
    &X-Amz-Date=20150825T160000Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_AuthorizeClusterSecurityGroupIngress_Example_1_Response"></a>

```
<AuthorizeClusterSecurityGroupIngressResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <AuthorizeClusterSecurityGroupIngressResult>
    <ClusterSecurityGroup>
      <Tags/>
      <EC2SecurityGroups/>
      <IPRanges>
        <IPRange>
          <CIDRIP>10.24.34.0/24</CIDRIP>
          <Status>authorized</Status>
        </IPRange>
      </IPRanges>
      <Description>Example security group</Description>
      <ClusterSecurityGroupName>example-security-group</ClusterSecurityGroupName>
    </ClusterSecurityGroup>
  </AuthorizeClusterSecurityGroupIngressResult>
  <ResponseMetadata>
    <RequestId>534d1bce-46ac-11e5-b673-31d855cc98c6</RequestId>
  </ResponseMetadata>
</AuthorizeClusterSecurityGroupIngressResponse>
```

## See Also
<a name="API_AuthorizeClusterSecurityGroupIngress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/AuthorizeClusterSecurityGroupIngress) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/AuthorizeClusterSecurityGroupIngress) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/AuthorizeClusterSecurityGroupIngress) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/AuthorizeClusterSecurityGroupIngress) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/AuthorizeClusterSecurityGroupIngress) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/AuthorizeClusterSecurityGroupIngress) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/AuthorizeClusterSecurityGroupIngress) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/AuthorizeClusterSecurityGroupIngress) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/AuthorizeClusterSecurityGroupIngress) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/AuthorizeClusterSecurityGroupIngress) 