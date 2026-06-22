---
id: "@specs/aws/docdb/docs/API_CreateDBInstance"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDBInstance"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# CreateDBInstance

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_CreateDBInstance
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDBInstance
<a name="API_CreateDBInstance"></a>

Creates a new instance.

## Request Parameters
<a name="API_CreateDBInstance_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterIdentifier **   
The identifier of the cluster that the instance will belong to.  
Type: String  
Required: Yes

 ** DBInstanceClass **   
The compute and memory capacity of the instance; for example, `db.r5.large`.   
Type: String  
Required: Yes

 ** DBInstanceIdentifier **   
The instance identifier. This parameter is stored as a lowercase string.  
Constraints:  
+ Must contain from 1 to 63 letters, numbers, or hyphens.
+ The first character must be a letter.
+ Cannot end with a hyphen or contain two consecutive hyphens.
Example: `mydbinstance`   
Type: String  
Required: Yes

 ** Engine **   
The name of the database engine to be used for this instance.  
Valid value: `docdb`   
Type: String  
Required: Yes

 ** AutoMinorVersionUpgrade **   
This parameter does not apply to Amazon DocumentDB. Amazon DocumentDB does not perform minor version upgrades regardless of the value set.  
Default: `false`   
Type: Boolean  
Required: No

 ** AvailabilityZone **   
The Amazon EC2 Availability Zone that the instance is created in.   
Default: A random, system-chosen Availability Zone in the endpoint's AWS Region.  
Example: `us-east-1d`   
Type: String  
Required: No

 ** CACertificateIdentifier **   
The CA certificate identifier to use for the DB instance's server certificate.  
For more information, see [Updating Your Amazon DocumentDB TLS Certificates](https://docs.aws.amazon.com/documentdb/latest/devguide/ca_cert_rotation.html) and [ Encrypting Data in Transit](https://docs.aws.amazon.com/documentdb/latest/devguide/security.encryption.ssl.html) in the *Amazon DocumentDB Developer Guide*.  
Type: String  
Required: No

 ** CopyTagsToSnapshot **   
A value that indicates whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.  
Type: Boolean  
Required: No

 ** EnablePerformanceInsights **   
A value that indicates whether to enable Performance Insights for the DB Instance. For more information, see [Using Amazon Performance Insights](https://docs.aws.amazon.com/documentdb/latest/devguide/performance-insights.html).  
Type: Boolean  
Required: No

 ** PerformanceInsightsKMSKeyId **   
The AWS KMS key identifier for encryption of Performance Insights data.  
The AWS KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.  
If you do not specify a value for PerformanceInsightsKMSKeyId, then Amazon DocumentDB uses your default KMS key. There is a default KMS key for your Amazon Web Services account. Your Amazon Web Services account has a different default KMS key for each Amazon Web Services region.  
Type: String  
Required: No

 ** PreferredMaintenanceWindow **   
The time range each week during which system maintenance can occur, in Universal Coordinated Time (UTC).  
 Format: `ddd:hh24:mi-ddd:hh24:mi`   
The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.   
Valid days: Mon, Tue, Wed, Thu, Fri, Sat, Sun  
Constraints: Minimum 30-minute window.  
Type: String  
Required: No

 ** PromotionTier **   
A value that specifies the order in which an Amazon DocumentDB replica is promoted to the primary instance after a failure of the existing primary instance.  
Default: 1  
Valid values: 0-15  
Type: Integer  
Required: No

 **Tags.Tag.N**   
The tags to be assigned to the instance. You can assign up to 10 tags to an instance.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateDBInstance_ResponseElements"></a>

The following element is returned by the service.

 ** DBInstance **   
Detailed information about an instance.   
Type: [DBInstance](API_DBInstance.md) object

## Errors
<a name="API_CreateDBInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationNotFound **   
The specified CIDR IP or Amazon EC2 security group isn't authorized for the specified security group.  
Amazon DocumentDB also might not be authorized to perform necessary actions on your behalf using IAM.  
HTTP Status Code: 404

 ** DBClusterNotFoundFault **   
 `DBClusterIdentifier` doesn't refer to an existing cluster.   
HTTP Status Code: 404

 ** DBInstanceAlreadyExists **   
You already have a instance with the given identifier.  
HTTP Status Code: 400

 ** DBParameterGroupNotFound **   
 `DBParameterGroupName` doesn't refer to an existing parameter group.   
HTTP Status Code: 404

 ** DBSecurityGroupNotFound **   
 `DBSecurityGroupName` doesn't refer to an existing security group.   
HTTP Status Code: 404

 ** DBSubnetGroupDoesNotCoverEnoughAZs **   
Subnets in the subnet group should cover at least two Availability Zones unless there is only one Availability Zone.  
HTTP Status Code: 400

 ** DBSubnetGroupNotFoundFault **   
 `DBSubnetGroupName` doesn't refer to an existing subnet group.   
HTTP Status Code: 404

 ** InstanceQuotaExceeded **   
The request would cause you to exceed the allowed number of instances.  
HTTP Status Code: 400

 ** InsufficientDBInstanceCapacity **   
The specified instance class isn't available in the specified Availability Zone.  
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **   
The cluster isn't in a valid state.  
HTTP Status Code: 400

 ** InvalidSubnet **   
The requested subnet is not valid, or multiple subnets were requested that are not all in a common virtual private cloud (VPC).  
HTTP Status Code: 400

 ** InvalidVPCNetworkStateFault **   
The subnet group doesn't cover all Availability Zones after it is created because of changes that were made.  
HTTP Status Code: 400

 ** KMSKeyNotAccessibleFault **   
An error occurred when accessing an AWS KMS key.  
HTTP Status Code: 400

 ** StorageQuotaExceeded **   
The request would cause you to exceed the allowed amount of storage available across all instances.  
HTTP Status Code: 400

 ** StorageTypeNotSupported **   
Storage of the specified `StorageType` can't be associated with the DB instance.   
HTTP Status Code: 400

## See Also
<a name="API_CreateDBInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-2014-10-31/CreateDBInstance) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-2014-10-31/CreateDBInstance) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/CreateDBInstance) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-2014-10-31/CreateDBInstance) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/CreateDBInstance) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-2014-10-31/CreateDBInstance) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-2014-10-31/CreateDBInstance) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-2014-10-31/CreateDBInstance) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-2014-10-31/CreateDBInstance) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/CreateDBInstance) 