---
id: "@specs/aws/redshift/docs/API_CreateClusterSubnetGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateClusterSubnetGroup"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# CreateClusterSubnetGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_CreateClusterSubnetGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateClusterSubnetGroup
<a name="API_CreateClusterSubnetGroup"></a>

Creates a new Amazon Redshift subnet group. You must provide a list of one or more subnets in your existing Amazon Virtual Private Cloud (Amazon VPC) when creating Amazon Redshift subnet group.

 For information about subnet groups, go to [Amazon Redshift Cluster Subnet Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-cluster-subnet-groups.html) in the *Amazon Redshift Cluster Management Guide*.

## Request Parameters
<a name="API_CreateClusterSubnetGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterSubnetGroupName **   
The name for the subnet group. Amazon Redshift stores the value as a lowercase string.  
Constraints:  
+ Must contain no more than 255 alphanumeric characters or hyphens.
+ Must not be "Default".
+ Must be unique for all subnet groups that are created by your AWS account.
Example: `examplesubnetgroup`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** Description **   
A description for the subnet group.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 **SubnetIds.SubnetIdentifier.N**   
An array of VPC subnet IDs. A maximum of 20 subnets can be modified in a single request.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 **Tags.Tag.N**   
A list of tag instances.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateClusterSubnetGroup_ResponseElements"></a>

The following element is returned by the service.

 ** ClusterSubnetGroup **   
Describes a subnet group.  
Type: [ClusterSubnetGroup](API_ClusterSubnetGroup.md) object

## Errors
<a name="API_CreateClusterSubnetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterSubnetGroupAlreadyExists **   
A *ClusterSubnetGroupName* is already used by an existing cluster subnet group.   
HTTP Status Code: 400

 ** ClusterSubnetGroupQuotaExceeded **   
The request would result in user exceeding the allowed number of cluster subnet groups. For information about increasing your quota, go to [Limits in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html) in the *Amazon Redshift Cluster Management Guide*.   
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

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

 ** TagLimitExceededFault **   
You have exceeded the number of tags allowed.  
HTTP Status Code: 400

 ** UnauthorizedOperation **   
Your account is not authorized to perform the requested operation.  
HTTP Status Code: 400

## Examples
<a name="API_CreateClusterSubnetGroup_Examples"></a>

### Example
<a name="API_CreateClusterSubnetGroup_Example_1"></a>

This example illustrates one usage of CreateClusterSubnetGroup.

#### Sample Request
<a name="API_CreateClusterSubnetGroup_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=CreateClusterSubnetGroup
&ClusterSubnetGroupName=mysubnetgroup
&Description=My+subnet+group
&SubnetIds.SubnetIdentifier.1=subnet-a1b23abc
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_CreateClusterSubnetGroup_Example_1_Response"></a>

```
<CreateClusterSubnetGroupResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <CreateClusterSubnetGroupResult>
    <ClusterSubnetGroup>
      <VpcId>vpc-a1abc1a1</VpcId>
      <Description>My subnet group</Description>
      <Subnets>
        <Subnet>
          <SubnetStatus>Active</SubnetStatus>
          <SubnetIdentifier>subnet-a1b23abc</SubnetIdentifier>
          <SubnetAvailabilityZone>
            <Name>us-east-2e</Name>
          </SubnetAvailabilityZone>
        </Subnet>
      </Subnets>
      <ClusterSubnetGroupName>mysubnetgroup</ClusterSubnetGroupName>
      <SubnetGroupStatus>Complete</SubnetGroupStatus>
      <Tags/>
    </ClusterSubnetGroup>
  </CreateClusterSubnetGroupResult>
  <ResponseMetadata>
    <RequestId>7062cbdc-2832-11ea-a940-1b28a85fd753</RequestId>
  </ResponseMetadata>
</CreateClusterSubnetGroupResponse>
```

## See Also
<a name="API_CreateClusterSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/CreateClusterSubnetGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/CreateClusterSubnetGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/CreateClusterSubnetGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/CreateClusterSubnetGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/CreateClusterSubnetGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/CreateClusterSubnetGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/CreateClusterSubnetGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/CreateClusterSubnetGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/CreateClusterSubnetGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/CreateClusterSubnetGroup) 