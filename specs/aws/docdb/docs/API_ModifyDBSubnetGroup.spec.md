---
id: "@specs/aws/docdb/docs/API_ModifyDBSubnetGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyDBSubnetGroup"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# ModifyDBSubnetGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_ModifyDBSubnetGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyDBSubnetGroup
<a name="API_ModifyDBSubnetGroup"></a>

Modifies an existing subnet group. subnet groups must contain at least one subnet in at least two Availability Zones in the AWS Region.

## Request Parameters
<a name="API_ModifyDBSubnetGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBSubnetGroupName **   
The name for the subnet group. This value is stored as a lowercase string. You can't modify the default subnet group.   
Constraints: Must match the name of an existing `DBSubnetGroup`. Must not be default.  
Example: `mySubnetgroup`   
Type: String  
Required: Yes

 **SubnetIds.SubnetIdentifier.N**   
The Amazon EC2 subnet IDs for the subnet group.  
Type: Array of strings  
Required: Yes

 ** DBSubnetGroupDescription **   
The description for the subnet group.  
Type: String  
Required: No

## Response Elements
<a name="API_ModifyDBSubnetGroup_ResponseElements"></a>

The following element is returned by the service.

 ** DBSubnetGroup **   
Detailed information about a subnet group.   
Type: [DBSubnetGroup](API_DBSubnetGroup.md) object

## Errors
<a name="API_ModifyDBSubnetGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBSubnetGroupDoesNotCoverEnoughAZs **   
Subnets in the subnet group should cover at least two Availability Zones unless there is only one Availability Zone.  
HTTP Status Code: 400

 ** DBSubnetGroupNotFoundFault **   
 `DBSubnetGroupName` doesn't refer to an existing subnet group.   
HTTP Status Code: 404

 ** DBSubnetQuotaExceededFault **   
The request would cause you to exceed the allowed number of subnets in a subnet group.  
HTTP Status Code: 400

 ** InvalidSubnet **   
The requested subnet is not valid, or multiple subnets were requested that are not all in a common virtual private cloud (VPC).  
HTTP Status Code: 400

 ** SubnetAlreadyInUse **   
The subnet is already in use in the Availability Zone.  
HTTP Status Code: 400

## See Also
<a name="API_ModifyDBSubnetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/ModifyDBSubnetGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/ModifyDBSubnetGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/ModifyDBSubnetGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/ModifyDBSubnetGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/ModifyDBSubnetGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/ModifyDBSubnetGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/ModifyDBSubnetGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/ModifyDBSubnetGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/ModifyDBSubnetGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/ModifyDBSubnetGroup) 