---
id: "@specs/aws/rds/docs/API_DescribeDBSubnetGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDBSubnetGroups"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeDBSubnetGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeDBSubnetGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDBSubnetGroups
<a name="API_DescribeDBSubnetGroups"></a>

Returns a list of DBSubnetGroup descriptions. If a DBSubnetGroupName is specified, the list will contain only the descriptions of the specified DBSubnetGroup.

For an overview of CIDR ranges, go to the [Wikipedia Tutorial](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing).

## Request Parameters
<a name="API_DescribeDBSubnetGroups_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBSubnetGroupName **   
The name of the DB subnet group to return details for.  
Type: String  
Required: No

 **Filters.Filter.N**   
This parameter isn't currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
An optional pagination token provided by a previous DescribeDBSubnetGroups request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeDBSubnetGroups_ResponseElements"></a>

The following elements are returned by the service.

 **DBSubnetGroups.DBSubnetGroup.N**   
A list of `DBSubnetGroup` instances.  
Type: Array of [DBSubnetGroup](API_DBSubnetGroup.md) objects

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

## Errors
<a name="API_DescribeDBSubnetGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBSubnetGroupNotFoundFault **   
 `DBSubnetGroupName` doesn't refer to an existing DB subnet group.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeDBSubnetGroups_Examples"></a>

### Example
<a name="API_DescribeDBSubnetGroups_Example_1"></a>

This example illustrates one usage of DescribeDBSubnetGroups.

#### Sample Request
<a name="API_DescribeDBSubnetGroups_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
   ?Action=DescribeDBSubnetGroups
   &MaxRecords=100
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140421/us-west-2/rds/aws4_request
   &X-Amz-Date=20140421T194732Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=6cc9b2825866148e1d6290b8aa2e9d75b1884b116d8665759942d87ebfbed426
```

#### Sample Response
<a name="API_DescribeDBSubnetGroups_Example_1_Response"></a>

```
<DescribeDBSubnetGroupsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeDBSubnetGroupsResult>
    <DBSubnetGroups>
      <DBSubnetGroup>
        <VpcId>vpc-e7abbdce</VpcId>
        <SubnetGroupStatus>Complete</SubnetGroupStatus>
        <DBSubnetGroupDescription>DB subnet group 1</DBSubnetGroupDescription>
        <DBSubnetGroupName>mydbsubnetgroup1</DBSubnetGroupName>
        <Subnets>
          <Subnet>
            <SubnetStatus>Active</SubnetStatus>
            <SubnetIdentifier>subnet-e8b3e5b1</SubnetIdentifier>
            <SubnetAvailabilityZone>
              <Name>us-west-2a</Name>
              <ProvisionedIopsCapable>false</ProvisionedIopsCapable>
            </SubnetAvailabilityZone>
          </Subnet>
          <Subnet>
            <SubnetStatus>Active</SubnetStatus>
            <SubnetIdentifier>subnet-44b2f22e</SubnetIdentifier>
            <SubnetAvailabilityZone>
              <Name>us-west-2b</Name>
              <ProvisionedIopsCapable>false</ProvisionedIopsCapable>
            </SubnetAvailabilityZone>
          </Subnet>
        </Subnets>
      </DBSubnetGroup>
      <DBSubnetGroup>
        <VpcId>vpc-c1e17bb8</VpcId>
        <SubnetGroupStatus>Complete</SubnetGroupStatus>
        <DBSubnetGroupDescription>My DB subnet group 2</DBSubnetGroupDescription>
        <DBSubnetGroupName>sub-grp-2</DBSubnetGroupName>
        <Subnets>
          <Subnet>
            <SubnetStatus>Active</SubnetStatus>
            <SubnetIdentifier>subnet-d281ef8a</SubnetIdentifier>
            <SubnetAvailabilityZone>
              <Name>us-west-2a</Name>
              <ProvisionedIopsCapable>false</ProvisionedIopsCapable>
            </SubnetAvailabilityZone>
          </Subnet>
          <Subnet>
            <SubnetStatus>Active</SubnetStatus>
            <SubnetIdentifier>subnet-b381ef9f</SubnetIdentifier>
            <SubnetAvailabilityZone>
              <Name>us-west-2c</Name>
              <ProvisionedIopsCapable>false</ProvisionedIopsCapable>
            </SubnetAvailabilityZone>
          </Subnet>
          <Subnet>
            <SubnetStatus>Active</SubnetStatus>
            <SubnetIdentifier>subnet-e1e17ebd</SubnetIdentifier>
            <SubnetAvailabilityZone>
              <Name>us-west-2b</Name>
              <ProvisionedIopsCapable>false</ProvisionedIopsCapable>
            </SubnetAvailabilityZone>
          </Subnet>
        </Subnets>
      </DBSubnetGroup>
    </DBSubnetGroups>
  </DescribeDBSubnetGroupsResult>
  <ResponseMetadata>
    <RequestId>b783db3b-b98c-11d3-fbc7-5c0aad74da7c</RequestId>
  </ResponseMetadata>
</DescribeDBSubnetGroupsResponse>
```

## See Also
<a name="API_DescribeDBSubnetGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeDBSubnetGroups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeDBSubnetGroups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeDBSubnetGroups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeDBSubnetGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeDBSubnetGroups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeDBSubnetGroups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeDBSubnetGroups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeDBSubnetGroups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeDBSubnetGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeDBSubnetGroups) 