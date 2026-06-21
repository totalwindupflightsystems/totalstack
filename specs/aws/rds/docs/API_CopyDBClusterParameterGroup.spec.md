---
id: "@specs/aws/rds/docs/API_CopyDBClusterParameterGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CopyDBClusterParameterGroup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# CopyDBClusterParameterGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_CopyDBClusterParameterGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CopyDBClusterParameterGroup
<a name="API_CopyDBClusterParameterGroup"></a>

Copies the specified DB cluster parameter group.

**Note**  
You can't copy a default DB cluster parameter group. Instead, create a new custom DB cluster parameter group, which copies the default parameters and values for the specified DB cluster parameter group family.

## Request Parameters
<a name="API_CopyDBClusterParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SourceDBClusterParameterGroupIdentifier **   
The identifier or Amazon Resource Name (ARN) for the source DB cluster parameter group. For information about creating an ARN, see [ Constructing an ARN for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing) in the *Amazon Aurora User Guide*.  
Constraints:  
+ Must specify a valid DB cluster parameter group.
Type: String  
Required: Yes

 ** TargetDBClusterParameterGroupDescription **   
A description for the copied DB cluster parameter group.  
Type: String  
Required: Yes

 ** TargetDBClusterParameterGroupIdentifier **   
The identifier for the copied DB cluster parameter group.  
Constraints:  
+ Can't be null, empty, or blank
+ Must contain from 1 to 255 letters, numbers, or hyphens
+ First character must be a letter
+ Can't end with a hyphen or contain two consecutive hyphens
Example: `my-cluster-param-group1`   
Type: String  
Required: Yes

 **Tags.Tag.N**   
A list of tags.  
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.   
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CopyDBClusterParameterGroup_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterParameterGroup **   
Contains the details of an Amazon RDS DB cluster parameter group.  
This data type is used as a response element in the `DescribeDBClusterParameterGroups` action.  
Type: [DBClusterParameterGroup](API_DBClusterParameterGroup.md) object

## Errors
<a name="API_CopyDBClusterParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBParameterGroupAlreadyExists **   
A DB parameter group with the same name exists.  
HTTP Status Code: 400

 ** DBParameterGroupNotFound **   
 `DBParameterGroupName` doesn't refer to an existing DB parameter group.  
HTTP Status Code: 404

 ** DBParameterGroupQuotaExceeded **   
The request would result in the user exceeding the allowed number of DB parameter groups.  
HTTP Status Code: 400

## Examples
<a name="API_CopyDBClusterParameterGroup_Examples"></a>

### Example
<a name="API_CopyDBClusterParameterGroup_Example_1"></a>

This example illustrates one usage of CopyDBClusterParameterGroup.

#### Sample Request
<a name="API_CopyDBClusterParameterGroup_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=CopyDBClusterParameterGroup
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &SourceDBClusterParameterGroupIdentifier=arn%3Aaws%3Ards%3Aus-east-1%3A815981987263%3cluster-pg%3Amy-cluster-pg
   &TargetDBParameterGroupIdentifier=new-cluster-pg
   &TargetDBParameterGroupDescription=New%20cluster%20group
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20160705/us-east-1/rds/aws4_request
   &X-Amz-Date=20160705T143101Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=9164337efa99caf850e874a1cb7ef62f3cea29d0b448b9e0e7c53b288ddffed2
```

#### Sample Response
<a name="API_CopyDBClusterParameterGroup_Example_1_Response"></a>

```
<CopyDBClusterParameterGroupResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <CreateDBClusterParameterGroupResult>
    <DBClusterParameterGroup>
      <DBParameterGroupFamily>aurora5.6</DBParameterGroupFamily>
      <Description>New cluster group</Description>
      <DBClusterParameterGroupName>new-cluster-pg</DBClusterParameterGroupName>
    </DBClusterParameterGroup>
  </CreateDBClusterParameterGroupResult>
  <ResponseMetadata>
    <RequestId>ae81a963-cd9d-11e4-8b88-8351746a4c92</RequestId>
  </ResponseMetadata>
</CopyDBClusterParameterGroupResponse>
```

## See Also
<a name="API_CopyDBClusterParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/CopyDBClusterParameterGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/CopyDBClusterParameterGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CopyDBClusterParameterGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/CopyDBClusterParameterGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CopyDBClusterParameterGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/CopyDBClusterParameterGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/CopyDBClusterParameterGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/CopyDBClusterParameterGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/CopyDBClusterParameterGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CopyDBClusterParameterGroup) 