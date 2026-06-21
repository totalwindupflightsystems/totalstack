---
id: "@specs/aws/rds/docs/API_ModifyDBSubnetGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyDBSubnetGroup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# ModifyDBSubnetGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_ModifyDBSubnetGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyDBSubnetGroup
<a name="API_ModifyDBSubnetGroup"></a>

Modifies an existing DB subnet group. DB subnet groups must contain at least one subnet in at least two AZs in the AWS Region.

## Request Parameters
<a name="API_ModifyDBSubnetGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBSubnetGroupName **   
The name for the DB subnet group. This value is stored as a lowercase string. You can't modify the default subnet group.  
Constraints: Must match the name of an existing DBSubnetGroup. Must not be default.  
Example: `mydbsubnetgroup`   
Type: String  
Required: Yes

 **SubnetIds.SubnetIdentifier.N**   
The EC2 subnet IDs for the DB subnet group.  
Type: Array of strings  
Required: Yes

 ** DBSubnetGroupDescription **   
The description for the DB subnet group.  
Type: String  
Required: No

## Response Elements
<a name="API_ModifyDBSubnetGroup_ResponseElements"></a>

The following element is returned by the service.

 ** DBSubnetGroup **   
Contains the details of an Amazon RDS DB subnet group.  
This data type is used as a response element in the `DescribeDBSubnetGroups` action.  
Type: [DBSubnetGroup](API_DBSubnetGroup.md) object

## Errors
<a name="API_ModifyDBSubnetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBSubnetGroupDoesNotCoverEnoughAZs **   
Subnets in the DB subnet group should cover at least two Availability Zones unless there is only one Availability Zone.  
HTTP Status Code: 400

 ** DBSubnetGroupNotFoundFault **   
 `DBSubnetGroupName` doesn't refer to an existing DB subnet group.  
HTTP Status Code: 404

 ** DBSubnetQuotaExceededFault **   
The request would result in the user exceeding the allowed number of subnets in a DB subnet groups.  
HTTP Status Code: 400

 ** InvalidDBSubnetGroupStateFault **   
The DB subnet group cannot be deleted because it's in use.  
HTTP Status Code: 400

 ** InvalidSubnet **   
The requested subnet is invalid, or multiple subnets were requested that are not all in a common VPC.  
HTTP Status Code: 400

 ** SubnetAlreadyInUse **   
The DB subnet is already in use in the Availability Zone.  
HTTP Status Code: 400

## Examples
<a name="API_ModifyDBSubnetGroup_Examples"></a>

### Example
<a name="API_ModifyDBSubnetGroup_Example_1"></a>

This example illustrates one usage of ModifyDBSubnetGroup.

#### Sample Request
<a name="API_ModifyDBSubnetGroup_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=ModifyDBSubnetGroup
   &DBSubnetGroupDescription=A%20new%20Description
   &DBSubnetGroupName=myawsuser-sngrp
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &SubnetIds.member.1=subnet-e4d398a1
   &SubnetIds.member.2=subnet-c2bdb6ba
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140425/us-east-1/rds/aws4_request
   &X-Amz-Date=20140425T200214Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=213c429d925cb1608fc13a1dde48715bcac3b0794536ee90beac34203265f9af
```

#### Sample Response
<a name="API_ModifyDBSubnetGroup_Example_1_Response"></a>

```
<ModifyDBSubnetGroupResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ModifyDBSubnetGroupResult>
    <DBSubnetGroup>
      <VpcId>vpc-33ac97ea</VpcId>
      <SubnetGroupStatus>Complete</SubnetGroupStatus>
      <DBSubnetGroupDescription>A new Description</DBSubnetGroupDescription>
      <DBSubnetGroupName>myawsuser-sngrp</DBSubnetGroupName>
      <Subnets>
        <Subnet>
          <SubnetStatus>Active</SubnetStatus>
          <SubnetIdentifier>subnet-e4d398a1</SubnetIdentifier>
          <SubnetAvailabilityZone>
            <Name>us-east-1b</Name>
            <ProvisionedIopsCapable>false</ProvisionedIopsCapable>
          </SubnetAvailabilityZone>
        </Subnet>
        <Subnet>
          <SubnetStatus>Active</SubnetStatus>
          <SubnetIdentifier>subnet-c2bdb6ba</SubnetIdentifier>
          <SubnetAvailabilityZone>
            <Name>us-east-1c</Name>
            <ProvisionedIopsCapable>false</ProvisionedIopsCapable>
          </SubnetAvailabilityZone>
        </Subnet>
      </Subnets>
    </DBSubnetGroup>
  </ModifyDBSubnetGroupResult>
  <ResponseMetadata>
    <RequestId>6dd028be-bba3-11d3-f4c6-37db295f7674</RequestId>
  </ResponseMetadata>
</ModifyDBSubnetGroupResponse>
```

## See Also
<a name="API_ModifyDBSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/ModifyDBSubnetGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/ModifyDBSubnetGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ModifyDBSubnetGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/ModifyDBSubnetGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ModifyDBSubnetGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/ModifyDBSubnetGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/ModifyDBSubnetGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/ModifyDBSubnetGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/ModifyDBSubnetGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ModifyDBSubnetGroup) 