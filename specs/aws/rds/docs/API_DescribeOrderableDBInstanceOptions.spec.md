---
id: "@specs/aws/rds/docs/API_DescribeOrderableDBInstanceOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeOrderableDBInstanceOptions"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeOrderableDBInstanceOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeOrderableDBInstanceOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeOrderableDBInstanceOptions
<a name="API_DescribeOrderableDBInstanceOptions"></a>

Describes the orderable DB instance options for a specified DB engine.

## Request Parameters
<a name="API_DescribeOrderableDBInstanceOptions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Engine **   
The name of the database engine to describe DB instance options for.  
Valid Values:  
+  `aurora-mysql` 
+  `aurora-postgresql` 
+  `custom-oracle-ee` 
+  `custom-oracle-ee-cdb` 
+  `custom-oracle-se2` 
+  `custom-oracle-se2-cdb` 
+  `db2-ae` 
+  `db2-ce` 
+  `db2-se` 
+  `mariadb` 
+  `mysql` 
+  `oracle-ee` 
+  `oracle-ee-cdb` 
+  `oracle-se2` 
+  `oracle-se2-cdb` 
+  `postgres` 
+  `sqlserver-ee` 
+  `sqlserver-se` 
+  `sqlserver-ex` 
+  `sqlserver-web` 
Type: String  
Required: Yes

 ** AvailabilityZoneGroup **   
The Availability Zone group associated with a Local Zone. Specify this parameter to retrieve available options for the Local Zones in the group.  
Omit this parameter to show the available options in the specified AWS Region.  
This setting doesn't apply to RDS Custom DB instances.  
Type: String  
Required: No

 ** DBInstanceClass **   
A filter to include only the available options for the specified DB instance class.  
Type: String  
Required: No

 ** EngineVersion **   
A filter to include only the available options for the specified engine version.  
Type: String  
Required: No

 **Filters.Filter.N**   
This parameter isn't currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** LicenseModel **   
A filter to include only the available options for the specified license model.  
RDS Custom supports only the BYOL licensing model.  
Type: String  
Required: No

 ** Marker **   
An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 1000.  
Type: Integer  
Required: No

 ** Vpc **   
Specifies whether to show only VPC or non-VPC offerings. RDS Custom supports only VPC offerings.  
RDS Custom supports only VPC offerings. If you describe non-VPC offerings for RDS Custom, the output shows VPC offerings.  
Type: Boolean  
Required: No

## Response Elements
<a name="API_DescribeOrderableDBInstanceOptions_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
An optional pagination token provided by a previous OrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

 **OrderableDBInstanceOptions.OrderableDBInstanceOption.N**   
An `OrderableDBInstanceOption` structure containing information about orderable options for the DB instance.  
Type: Array of [OrderableDBInstanceOption](API_OrderableDBInstanceOption.md) objects

## Errors
<a name="API_DescribeOrderableDBInstanceOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeOrderableDBInstanceOptions_Examples"></a>

### Example
<a name="API_DescribeOrderableDBInstanceOptions_Example_1"></a>

This example illustrates one usage of DescribeOrderableDBInstanceOptions.

#### Sample Request
<a name="API_DescribeOrderableDBInstanceOptions_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
   ?Action=DescribeOrderableDBInstanceOptions
   &Engine=mysql
   &EngineVersion=8.0.26
   &DBInstanceClass=db.r6gd.large
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140421/us-west-2/rds/aws4_request
   &X-Amz-Date=20211020T205537Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=b49545dd3c933bdded80655d433d84bf743261ea1bebb33a7922c5c2c5240cd8
```

#### Sample Response
<a name="API_DescribeOrderableDBInstanceOptions_Example_1_Response"></a>

```
<DescribeOrderableDBInstanceOptionsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeOrderableDBInstanceOptionsResult>
    <Marker>ZGIubTEuc21hbGwKZ2VuZXJhbC1wdWJsaWMtbGljZW5zZQo1LjEuNjkKTg==</Marker>
    <OrderableDBInstanceOptions>
      <OrderableDBInstanceOption>
        <MultiAZCapable>true</MultiAZCapable>
        <Engine>mysql</Engine>
        <LicenseModel>general-public-license</LicenseModel>
        <ReadReplicaCapable>true</ReadReplicaCapable>
        <Vpc>false</Vpc>
        <EngineVersion>5.1.57</EngineVersion>
        <AvailabilityZones>
          <AvailabilityZone>
            <Name>us-west-2a</Name>
            <ProvisionedIopsCapable>true</ProvisionedIopsCapable>
          </AvailabilityZone>
          <AvailabilityZone>
            <Name>us-west-2b</Name>
            <ProvisionedIopsCapable>true</ProvisionedIopsCapable>
          </AvailabilityZone>
          <AvailabilityZone>
            <Name>us-west-2c</Name>
            <ProvisionedIopsCapable>true</ProvisionedIopsCapable>
          </AvailabilityZone>
        </AvailabilityZones>
        <DBInstanceClass>db.m1.large</DBInstanceClass>
      </OrderableDBInstanceOption>
      <OrderableDBInstanceOption>
        <MultiAZCapable>true</MultiAZCapable>
        <Engine>mysql</Engine>
        <LicenseModel>general-public-license</LicenseModel>
        <ReadReplicaCapable>true</ReadReplicaCapable>
        <Vpc>true</Vpc>
        <EngineVersion>5.1.57</EngineVersion>
        <AvailabilityZones>
          <AvailabilityZone>
            <Name>us-west-2a</Name>
            <ProvisionedIopsCapable>true</ProvisionedIopsCapable>
          </AvailabilityZone>
          <AvailabilityZone>
            <Name>us-west-2b</Name>
            <ProvisionedIopsCapable>true</ProvisionedIopsCapable>
          </AvailabilityZone>
          <AvailabilityZone>
            <Name>us-west-2c</Name>
            <ProvisionedIopsCapable>true</ProvisionedIopsCapable>
          </AvailabilityZone>
        </AvailabilityZones>
        <DBInstanceClass>db.m1.large</DBInstanceClass>
      </OrderableDBInstanceOption>
    </OrderableDBInstanceOptions>
  </DescribeOrderableDBInstanceOptionsResult>
  <ResponseMetadata>
    <RequestId>b7ceb73e-b98c-11d3-a907-5a2c468b9cb0</RequestId>
  </ResponseMetadata>
</DescribeOrderableDBInstanceOptionsResponse>
```

## See Also
<a name="API_DescribeOrderableDBInstanceOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeOrderableDBInstanceOptions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeOrderableDBInstanceOptions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeOrderableDBInstanceOptions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeOrderableDBInstanceOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeOrderableDBInstanceOptions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeOrderableDBInstanceOptions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeOrderableDBInstanceOptions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeOrderableDBInstanceOptions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeOrderableDBInstanceOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeOrderableDBInstanceOptions) 