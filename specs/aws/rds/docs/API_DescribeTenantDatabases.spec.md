---
id: "@specs/aws/rds/docs/API_DescribeTenantDatabases"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeTenantDatabases"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeTenantDatabases

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeTenantDatabases
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeTenantDatabases
<a name="API_DescribeTenantDatabases"></a>

Describes the tenant databases in a DB instance that uses the multi-tenant configuration. Only RDS for Oracle CDB instances are supported.

## Request Parameters
<a name="API_DescribeTenantDatabases_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **   
The user-supplied DB instance identifier, which must match the identifier of an existing instance owned by the AWS account. This parameter isn't case-sensitive.  
Type: String  
Required: No

 **Filters.Filter.N**   
A filter that specifies one or more database tenants to describe.  
Supported filters:  
+  `tenant-db-name` - Tenant database names. The results list only includes information about the tenant databases that match these tenant DB names.
+  `tenant-database-resource-id` - Tenant database resource identifiers.
+  `dbi-resource-id` - DB instance resource identifiers. The results list only includes information about the tenants contained within the DB instances identified by these resource identifiers.
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeTenantDatabases` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.  
Type: Integer  
Required: No

 ** TenantDBName **   
The user-supplied tenant database name, which must match the name of an existing tenant database on the specified DB instance owned by your AWS account. This parameter isn’t case-sensitive.  
Type: String  
Required: No

## Response Elements
<a name="API_DescribeTenantDatabases_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
An optional pagination token provided by a previous `DescribeTenantDatabases` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

 **TenantDatabases.TenantDatabase.N**   
An array of the tenant databases requested by the `DescribeTenantDatabases` operation.  
Type: Array of [TenantDatabase](API_TenantDatabase.md) objects

## Errors
<a name="API_DescribeTenantDatabases_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBInstanceNotFound **   
 `DBInstanceIdentifier` doesn't refer to an existing DB instance.  
HTTP Status Code: 404

## See Also
<a name="API_DescribeTenantDatabases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeTenantDatabases) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeTenantDatabases) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeTenantDatabases) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeTenantDatabases) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeTenantDatabases) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeTenantDatabases) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeTenantDatabases) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeTenantDatabases) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeTenantDatabases) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeTenantDatabases) 