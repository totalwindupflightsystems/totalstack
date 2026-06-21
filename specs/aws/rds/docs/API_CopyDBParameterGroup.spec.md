---
id: "@specs/aws/rds/docs/API_CopyDBParameterGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CopyDBParameterGroup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# CopyDBParameterGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_CopyDBParameterGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CopyDBParameterGroup
<a name="API_CopyDBParameterGroup"></a>

Copies the specified DB parameter group.

**Note**  
You can't copy a default DB parameter group. Instead, create a new custom DB parameter group, which copies the default parameters and values for the specified DB parameter group family.

## Request Parameters
<a name="API_CopyDBParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SourceDBParameterGroupIdentifier **   
The identifier or ARN for the source DB parameter group. For information about creating an ARN, see [ Constructing an ARN for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing) in the *Amazon RDS User Guide*.  
Constraints:  
+ Must specify a valid DB parameter group.
Type: String  
Required: Yes

 ** TargetDBParameterGroupDescription **   
A description for the copied DB parameter group.  
Type: String  
Required: Yes

 ** TargetDBParameterGroupIdentifier **   
The identifier for the copied DB parameter group.  
Constraints:  
+ Can't be null, empty, or blank
+ Must contain from 1 to 255 letters, numbers, or hyphens
+ First character must be a letter
+ Can't end with a hyphen or contain two consecutive hyphens
Example: `my-db-parameter-group`   
Type: String  
Required: Yes

 **Tags.Tag.N**   
A list of tags.  
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.   
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CopyDBParameterGroup_ResponseElements"></a>

The following element is returned by the service.

 ** DBParameterGroup **   
Contains the details of an Amazon RDS DB parameter group.  
This data type is used as a response element in the `DescribeDBParameterGroups` action.  
Type: [DBParameterGroup](API_DBParameterGroup.md) object

## Errors
<a name="API_CopyDBParameterGroup_Errors"></a>

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
<a name="API_CopyDBParameterGroup_Examples"></a>

### Example
<a name="API_CopyDBParameterGroup_Example_1"></a>

This example illustrates one usage of CopyDBParameterGroup.

#### Sample Request
<a name="API_CopyDBParameterGroup_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=CopyDBParameterGroup
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &SourceDBParameterGroupIdentifier=arn%3Aaws%3Ards%3Aus-west-2%3A815981987263%3pg%3Amy-remote-param-group
   &TargetDBParameterGroupIdentifier=new-local-param-group
   &TargetDBParameterGroupDescription=description
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140429/us-east-1/rds/aws4_request
   &X-Amz-Date=20140429T175351Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=9164337efa99caf850e874a1cb7ef62f3cea29d0b448b9e0e7c53b288ddffed2
```

#### Sample Response
<a name="API_CopyDBParameterGroup_Example_1_Response"></a>

```
<CopyDBParameterGroupResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <CopyDBParameterGroupResult>
    <DBParameterGroup>
      <DBParameterGroupFamily>mysql5.6</DBParameterGroupFamily>
      <Description>description</Description>
      <DBParameterGroupName>new-local-param-group</DBParameterGroupName>
    </DBParameterGroup>
  </CopyDBParameterGroupResult>
  <ResponseMetadata>
    <RequestId>2928d60e-beb6-11d3-8e5c-3ccda5460c46</RequestId>
  </ResponseMetadata>
</CopyDBParameterGroupResponse>
```

## See Also
<a name="API_CopyDBParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/CopyDBParameterGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/CopyDBParameterGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CopyDBParameterGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/CopyDBParameterGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CopyDBParameterGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/CopyDBParameterGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/CopyDBParameterGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/CopyDBParameterGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/CopyDBParameterGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CopyDBParameterGroup) 