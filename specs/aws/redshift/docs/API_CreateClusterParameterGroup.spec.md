---
id: "@specs/aws/redshift/docs/API_CreateClusterParameterGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateClusterParameterGroup"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# CreateClusterParameterGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_CreateClusterParameterGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateClusterParameterGroup
<a name="API_CreateClusterParameterGroup"></a>

Creates an Amazon Redshift parameter group.

Creating parameter groups is independent of creating clusters. You can associate a cluster with a parameter group when you create the cluster. You can also associate an existing cluster with a parameter group after the cluster is created by using [ModifyCluster](API_ModifyCluster.md). 

Parameters in the parameter group define specific behavior that applies to the databases you create on the cluster. For more information about parameters and parameter groups, go to [Amazon Redshift Parameter Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) in the *Amazon Redshift Cluster Management Guide*.

## Request Parameters
<a name="API_CreateClusterParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Description **   
A description of the parameter group.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** ParameterGroupFamily **   
The Amazon Redshift engine version to which the cluster parameter group applies. The cluster engine version determines the set of parameters.  
To get a list of valid parameter group family names, you can call [DescribeClusterParameterGroups](API_DescribeClusterParameterGroups.md). By default, Amazon Redshift returns a list of all the parameter groups that are owned by your AWS account, including the default parameter groups for each Amazon Redshift engine version. The parameter group family names associated with the default parameter groups provide you the valid values. For example, a valid family name is "redshift-1.0".   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** ParameterGroupName **   
The name of the cluster parameter group.  
Constraints:  
+ Must be 1 to 255 alphanumeric characters or hyphens
+ First character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
+ Must be unique withing your AWS account.
This value is stored as a lower-case string.
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 **Tags.Tag.N**   
A list of tag instances.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateClusterParameterGroup_ResponseElements"></a>

The following element is returned by the service.

 ** ClusterParameterGroup **   
Describes a parameter group.  
Type: [ClusterParameterGroup](API_ClusterParameterGroup.md) object

## Errors
<a name="API_CreateClusterParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterParameterGroupAlreadyExists **   
A cluster parameter group with the same name already exists.  
HTTP Status Code: 400

 ** ClusterParameterGroupQuotaExceeded **   
The request would result in the user exceeding the allowed number of cluster parameter groups. For information about increasing your quota, go to [Limits in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html) in the *Amazon Redshift Cluster Management Guide*.   
HTTP Status Code: 400

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

 ** TagLimitExceededFault **   
You have exceeded the number of tags allowed.  
HTTP Status Code: 400

## Examples
<a name="API_CreateClusterParameterGroup_Examples"></a>

### Example
<a name="API_CreateClusterParameterGroup_Example_1"></a>

This example illustrates one usage of CreateClusterParameterGroup.

#### Sample Request
<a name="API_CreateClusterParameterGroup_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=CreateClusterParameterGroup
&ParameterGroupName=myclusterparametergroup
&ParameterGroupFamily=redshift-1.0
&Description=My+first+cluster+parameter+group
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_CreateClusterParameterGroup_Example_1_Response"></a>

```
<CreateClusterParameterGroupResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <CreateClusterParameterGroupResult>
    <ClusterParameterGroup>
      <ParameterGroupName>myclusterparametergroup</ParameterGroupName>
      <Description>My first cluster parameter group</Description>
      <ParameterGroupFamily>redshift-1.0</ParameterGroupFamily>
      <Tags/>
    </ClusterParameterGroup>
  </CreateClusterParameterGroupResult>
  <ResponseMetadata>
    <RequestId>d52df43b-281e-11ea-8314-974e2ba81189</RequestId>
  </ResponseMetadata>
</CreateClusterParameterGroupResponse>
```

## See Also
<a name="API_CreateClusterParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/CreateClusterParameterGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/CreateClusterParameterGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/CreateClusterParameterGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/CreateClusterParameterGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/CreateClusterParameterGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/CreateClusterParameterGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/CreateClusterParameterGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/CreateClusterParameterGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/CreateClusterParameterGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/CreateClusterParameterGroup) 