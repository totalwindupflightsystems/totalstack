---
id: "@specs/aws/redshift/docs/API_ModifyClusterSubnetGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyClusterSubnetGroup"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ModifyClusterSubnetGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ModifyClusterSubnetGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyClusterSubnetGroup
<a name="API_ModifyClusterSubnetGroup"></a>

Modifies a cluster subnet group to include the specified list of VPC subnets. The operation replaces the existing list of subnets with the new list of subnets.

VPC Block Public Access (BPA) enables you to block resources in VPCs and subnets that you own in a Region from reaching or being reached from the internet through internet gateways and egress-only internet gateways. If a subnet group for a provisioned cluster is in an account with VPC BPA turned on, the following capabilities are blocked:
+ Creating a public cluster
+ Restoring a public cluster
+ Modifying a private cluster to be public
+ Adding a subnet with VPC BPA turned on to the subnet group when there's at least one public cluster within the group

For more information about VPC BPA, see [Block public access to VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/security-vpc-bpa.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_ModifyClusterSubnetGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterSubnetGroupName **   
The name of the subnet group to be modified.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 **SubnetIds.SubnetIdentifier.N**   
An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** Description **   
A text description of the subnet group to be modified.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_ModifyClusterSubnetGroup_ResponseElements"></a>

The following element is returned by the service.

 ** ClusterSubnetGroup **   
Describes a subnet group.  
Type: [ClusterSubnetGroup](API_ClusterSubnetGroup.md) object

## Errors
<a name="API_ModifyClusterSubnetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterSubnetGroupNotFoundFault **   
The cluster subnet group name does not refer to an existing cluster subnet group.  
HTTP Status Code: 400

 ** ClusterSubnetQuotaExceededFault **   
The request would result in user exceeding the allowed number of subnets in a cluster subnet groups. For information about increasing your quota, go to [Limits in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html) in the *Amazon Redshift Cluster Management Guide*.   
HTTP Status Code: 400

 ** DependentServiceRequestThrottlingFault **   
The request cannot be completed because a dependent service is throttling requests made by Amazon Redshift on your behalf. Wait and retry the request.  
HTTP Status Code: 400

 ** InvalidSubnet **   
The requested subnet is not valid, or not all of the subnets are in the same VPC.  
HTTP Status Code: 400

 ** SubnetAlreadyInUse **   
A specified subnet is already in use by another cluster.  
HTTP Status Code: 400

 ** UnauthorizedOperation **   
Your account is not authorized to perform the requested operation.  
HTTP Status Code: 400

## Examples
<a name="API_ModifyClusterSubnetGroup_Examples"></a>

### Example
<a name="API_ModifyClusterSubnetGroup_Example_1"></a>

This example illustrates one usage of ModifyClusterSubnetGroup.

#### Sample Request
<a name="API_ModifyClusterSubnetGroup_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=ModifyClusterSubnetGroup
&ClusterSubnetGroupName=mysubnetgroup
&SubnetIds.SubnetIdentifier.1=subnet-a1b21abc
&SubnetIds.SubnetIdentifier.2=subnet-a1b22abc
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_ModifyClusterSubnetGroup_Example_1_Response"></a>

```
<ModifyClusterSubnetGroupResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <ModifyClusterSubnetGroupResult>
    <ClusterSubnetGroup>
      <VpcId>vpc-a1abc1a1</VpcId>
      <Description>My subnet group</Description>
      <Subnets>
        <Subnet>
          <SubnetStatus>Active</SubnetStatus>
          <SubnetIdentifier>subnet-a1b21abc</SubnetIdentifier>
          <SubnetAvailabilityZone>
            <Name>us-east-2f</Name>
          </SubnetAvailabilityZone>
        </Subnet>
        <Subnet>
          <SubnetStatus>Active</SubnetStatus>
          <SubnetIdentifier>subnet-a1b22abc</SubnetIdentifier>
          <SubnetAvailabilityZone>
            <Name>us-east-2a</Name>
          </SubnetAvailabilityZone>
        </Subnet>
      </Subnets>
      <ClusterSubnetGroupName>mysubnetgroup</ClusterSubnetGroupName>
      <SubnetGroupStatus>Complete</SubnetGroupStatus>
      <Tags/>
    </ClusterSubnetGroup>
  </ModifyClusterSubnetGroupResult>
  <ResponseMetadata>
    <RequestId>0b638b21-28eb-11ea-8cc9-43f1872b4b75</RequestId>
  </ResponseMetadata>
</ModifyClusterSubnetGroupResponse>
```

## See Also
<a name="API_ModifyClusterSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/ModifyClusterSubnetGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/ModifyClusterSubnetGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ModifyClusterSubnetGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/ModifyClusterSubnetGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ModifyClusterSubnetGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/ModifyClusterSubnetGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/ModifyClusterSubnetGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/ModifyClusterSubnetGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/ModifyClusterSubnetGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ModifyClusterSubnetGroup) 