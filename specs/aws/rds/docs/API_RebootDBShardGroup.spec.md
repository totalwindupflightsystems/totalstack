---
id: "@specs/aws/rds/docs/API_RebootDBShardGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS RebootDBShardGroup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# RebootDBShardGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_RebootDBShardGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# RebootDBShardGroup
<a name="API_RebootDBShardGroup"></a>

You might need to reboot your DB shard group, usually for maintenance reasons. For example, if you make certain modifications, reboot the DB shard group for the changes to take effect.

This operation applies only to Aurora Limitless Database DBb shard groups.

## Request Parameters
<a name="API_RebootDBShardGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBShardGroupIdentifier **   
The name of the DB shard group to reboot.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z](?:-?[a-zA-Z0-9]+)*`   
Required: Yes

## Response Elements
<a name="API_RebootDBShardGroup_ResponseElements"></a>

The following elements are returned by the service.

 ** ComputeRedundancy **   
Specifies whether to create standby DB shard groups for the DB shard group. Valid values are the following:  
+ 0 - Creates a DB shard group without a standby DB shard group. This is the default value.
+ 1 - Creates a DB shard group with a standby DB shard group in a different Availability Zone (AZ).
+ 2 - Creates a DB shard group with two standby DB shard groups in two different AZs.
Type: Integer

 ** DBClusterIdentifier **   
The name of the primary DB cluster for the DB shard group.  
Type: String

 ** DBShardGroupArn **   
The Amazon Resource Name (ARN) for the DB shard group.  
Type: String

 ** DBShardGroupIdentifier **   
The name of the DB shard group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[a-zA-Z](?:-?[a-zA-Z0-9]+)*` 

 ** DBShardGroupResourceId **   
The AWS Region-unique, immutable identifier for the DB shard group.  
Type: String

 ** Endpoint **   
The connection endpoint for the DB shard group.  
Type: String

 ** MaxACU **   
The maximum capacity of the DB shard group in Aurora capacity units (ACUs).  
Type: Double

 ** MinACU **   
The minimum capacity of the DB shard group in Aurora capacity units (ACUs).  
Type: Double

 ** PubliclyAccessible **   
Indicates whether the DB shard group is publicly accessible.  
When the DB shard group is publicly accessible, its Domain Name System (DNS) endpoint resolves to the private IP address from within the DB shard group's virtual private cloud (VPC). It resolves to the public IP address from outside of the DB shard group's VPC. Access to the DB shard group is ultimately controlled by the security group it uses. That public access isn't permitted if the security group assigned to the DB shard group doesn't permit it.  
When the DB shard group isn't publicly accessible, it is an internal DB shard group with a DNS name that resolves to a private IP address.  
For more information, see [CreateDBShardGroup](API_CreateDBShardGroup.md).  
This setting is only for Aurora Limitless Database.  
Type: Boolean

 ** Status **   
The status of the DB shard group.  
Type: String

 **TagList.Tag.N**   
A list of tags.  
For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide*.   
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_RebootDBShardGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBShardGroupNotFound **   
The specified DB shard group name wasn't found.  
HTTP Status Code: 404

 ** InvalidDBShardGroupState **   
The DB shard group must be in the available state.  
HTTP Status Code: 400

## See Also
<a name="API_RebootDBShardGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/RebootDBShardGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/RebootDBShardGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/RebootDBShardGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/RebootDBShardGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/RebootDBShardGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/RebootDBShardGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/RebootDBShardGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/RebootDBShardGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/RebootDBShardGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/RebootDBShardGroup) 