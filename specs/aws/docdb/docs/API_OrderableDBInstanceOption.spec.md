---
id: "@specs/aws/docdb/docs/API_OrderableDBInstanceOption"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS OrderableDBInstanceOption"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# OrderableDBInstanceOption

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_OrderableDBInstanceOption
> **target_lang:** meta — documentation tier. ALL sections preserved.



# OrderableDBInstanceOption
<a name="API_OrderableDBInstanceOption"></a>

The options that are available for an instance.

## Contents
<a name="API_OrderableDBInstanceOption_Contents"></a>

**Note**  
In the following list, the required parameters are described first.

 ** AvailabilityZones.AvailabilityZone.N **   
A list of Availability Zones for an instance.  
Type: Array of [AvailabilityZone](API_AvailabilityZone.md) objects  
Required: No

 ** DBInstanceClass **   
The instance class for an instance.  
Type: String  
Required: No

 ** Engine **   
The engine type of an instance.  
Type: String  
Required: No

 ** EngineVersion **   
The engine version of an instance.  
Type: String  
Required: No

 ** LicenseModel **   
The license model for an instance.  
Type: String  
Required: No

 ** StorageType **   
The storage type to associate with the DB cluster  
Type: String  
Required: No

 ** Vpc **   
Indicates whether an instance is in a virtual private cloud (VPC).  
Type: Boolean  
Required: No

## See Also
<a name="API_OrderableDBInstanceOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/OrderableDBInstanceOption) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/OrderableDBInstanceOption) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/OrderableDBInstanceOption) 