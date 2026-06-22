---
id: "@specs/aws/redshift/docs/API_CreateClusterSecurityGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateClusterSecurityGroup"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# CreateClusterSecurityGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_CreateClusterSecurityGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateClusterSecurityGroup
<a name="API_CreateClusterSecurityGroup"></a>

Creates a new Amazon Redshift security group. You use security groups to control access to non-VPC clusters.

 For information about managing security groups, go to [Amazon Redshift Cluster Security Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-security-groups.html) in the *Amazon Redshift Cluster Management Guide*.

## Request Parameters
<a name="API_CreateClusterSecurityGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ClusterSecurityGroupName **   
The name for the security group. Amazon Redshift stores the value as a lowercase string.  
Constraints:  
+ Must contain no more than 255 alphanumeric characters or hyphens.
+ Must not be "Default".
+ Must be unique for all security groups that are created by your AWS account.
Example: `examplesecuritygroup`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** Description **   
A description for the security group.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 **Tags.Tag.N**   
A list of tag instances.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateClusterSecurityGroup_ResponseElements"></a>

The following element is returned by the service.

 ** ClusterSecurityGroup **   
Describes a security group.  
Type: [ClusterSecurityGroup](API_ClusterSecurityGroup.md) object

## Errors
<a name="API_CreateClusterSecurityGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterSecurityGroupAlreadyExists **   
A cluster security group with the same name already exists.  
HTTP Status Code: 400

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

 ** QuotaExceeded.ClusterSecurityGroup **   
The request would result in the user exceeding the allowed number of cluster security groups. For information about increasing your quota, go to [Limits in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html) in the *Amazon Redshift Cluster Management Guide*.   
HTTP Status Code: 400

 ** TagLimitExceededFault **   
You have exceeded the number of tags allowed.  
HTTP Status Code: 400

## Examples
<a name="API_CreateClusterSecurityGroup_Examples"></a>

### Example
<a name="API_CreateClusterSecurityGroup_Example_1"></a>

This example illustrates one usage of CreateClusterSecurityGroup.

#### Sample Request
<a name="API_CreateClusterSecurityGroup_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
   ?Action=CreateClusterSecurityGroup
   &ClusterSecurityGroupName=securitygroup1
   &Description=my security group
   &Version=2012-12-01
   &x-amz-algorithm=AWS4-HMAC-SHA256
   &x-amz-credential=AKIAIOSFODNN7EXAMPLE/20130123/us-east-2/redshift/aws4_request
   &x-amz-date=20130123T005817Z
   &x-amz-signedheaders=content-type;host;x-amz-date
```

#### Sample Response
<a name="API_CreateClusterSecurityGroup_Example_1_Response"></a>

```
<CreateClusterSecurityGroupResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <CreateClusterSecurityGroupResult>
    <ClusterSecurityGroup>
      <EC2SecurityGroups/>
      <IPRanges/>
      <Description>my security group</Description>
      <ClusterSecurityGroupName>securitygroup1</ClusterSecurityGroupName>
    </ClusterSecurityGroup>
  </CreateClusterSecurityGroupResult>
  <ResponseMetadata>
    <RequestId>f9ee270f-64f7-11e2-a8da-655adc216806</RequestId>
  </ResponseMetadata>
</CreateClusterSecurityGroupResponse>
```

## See Also
<a name="API_CreateClusterSecurityGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/CreateClusterSecurityGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/CreateClusterSecurityGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/CreateClusterSecurityGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/CreateClusterSecurityGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/CreateClusterSecurityGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/CreateClusterSecurityGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/CreateClusterSecurityGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/CreateClusterSecurityGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/CreateClusterSecurityGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/CreateClusterSecurityGroup) 