---
id: "@specs/aws/rds/docs/API_DescribeOptionGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeOptionGroups"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeOptionGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeOptionGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeOptionGroups
<a name="API_DescribeOptionGroups"></a>

Describes the available option groups.

## Request Parameters
<a name="API_DescribeOptionGroups_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EngineName **   
A filter to only include option groups associated with this database engine.  
Valid Values:  
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
Required: No

 **Filters.Filter.N**   
This parameter isn't currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** MajorEngineVersion **   
Filters the list of option groups to only include groups associated with a specific database engine version. If specified, then EngineName must also be specified.  
Type: String  
Required: No

 ** Marker **   
An optional pagination token provided by a previous DescribeOptionGroups request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** OptionGroupName **   
The name of the option group to describe. Can't be supplied together with EngineName or MajorEngineVersion.  
Type: String  
Required: No

## Response Elements
<a name="API_DescribeOptionGroups_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

 **OptionGroupsList.OptionGroup.N**   
List of option groups.  
Type: Array of [OptionGroup](API_OptionGroup.md) objects

## Errors
<a name="API_DescribeOptionGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OptionGroupNotFoundFault **   
The specified option group could not be found.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeOptionGroups_Examples"></a>

### Example
<a name="API_DescribeOptionGroups_Example_1"></a>

This example illustrates one usage of DescribeOptionGroups.

#### Sample Request
<a name="API_DescribeOptionGroups_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=DescribeOptionGroups
   &MaxRecords=100
   &OptionGroupName=myawsuser-grp1
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140421/us-east-1/rds/aws4_request
   &X-Amz-Date=20140421T231357Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=fabfbeb85c44e3f151d44211790c5135a9074fdb8d85ec117788ac6cfab6c5bc
```

#### Sample Response
<a name="API_DescribeOptionGroups_Example_1_Response"></a>

```
<DescribeOptionGroupsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeOptionGroupsResult>
    <OptionGroupsList>
      <OptionGroup>
        <AllowsVpcAndNonVpcInstanceMemberships>true</AllowsVpcAndNonVpcInstanceMemberships>
        <MajorEngineVersion>5.6</MajorEngineVersion>
        <OptionGroupName>myawsuser-grp1</OptionGroupName>
        <EngineName>mysql</EngineName>
        <OptionGroupDescription>my test option group</OptionGroupDescription>
        <Options/>
      </OptionGroup>
    </OptionGroupsList>
  </DescribeOptionGroupsResult>
  <ResponseMetadata>
    <RequestId>8c6201fc-b9ff-11d3-f92b-31fa5e8dbc99</RequestId>
  </ResponseMetadata>
</DescribeOptionGroupsResponse>
```

### Example
<a name="API_DescribeOptionGroups_Example_2"></a>

This example illustrates one usage of DescribeOptionGroups.

#### Sample Request
<a name="API_DescribeOptionGroups_Example_2_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
    ?Action=DescribeOptionGroups
    &MaxRecords=100
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20140613/us-west-2/rds/aws4_request
    &X-Amz-Date=20140613T223341Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=5ae331adcd684c27d66e0b794a51933effe32a4c026eba2e994ae483ee47a0ba
```

#### Sample Response
<a name="API_DescribeOptionGroups_Example_2_Response"></a>

```
<DescribeOptionGroupsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeOptionGroupsResult>
    <OptionGroupsList>
      <OptionGroup>
        <OptionGroupName>default:mysql-5-5</OptionGroupName>
        <AllowsVpcAndNonVpcInstanceMemberships>true</AllowsVpcAndNonVpcInstanceMemberships>
        <MajorEngineVersion>5.5</MajorEngineVersion>
        <EngineName>mysql</EngineName>
        <OptionGroupDescription>Default option group MySQL 5.5</OptionGroupDescription>
        <Options/>
      </OptionGroup>
      <OptionGroup>
        <OptionGroupName>default:postgres-9-3</OptionGroupName>
        <AllowsVpcAndNonVpcInstanceMemberships>true</AllowsVpcAndNonVpcInstanceMemberships>
        <MajorEngineVersion>9.3</MajorEngineVersion>
        <EngineName>postgres</EngineName>
        <OptionGroupDescription>Default option group for postgres 9.3</OptionGroupDescription>
        <Options/>
      </OptionGroup>
      <OptionGroup>
        <OptionGroupName>default:sqlserver-ex-10-50</OptionGroupName>
        <AllowsVpcAndNonVpcInstanceMemberships>true</AllowsVpcAndNonVpcInstanceMemberships>
        <MajorEngineVersion>10.50</MajorEngineVersion>
        <EngineName>sqlserver-ex</EngineName>
        <OptionGroupDescription>Default option group for sqlserver-ex 10.50</OptionGroupDescription>
        <Options/>
      </OptionGroup>
      <OptionGroup>
        <OptionGroupName>default:sqlserver-se-10-50-mirrored</OptionGroupName>
        <AllowsVpcAndNonVpcInstanceMemberships>true</AllowsVpcAndNonVpcInstanceMemberships>
        <MajorEngineVersion>10.50</MajorEngineVersion>
        <EngineName>sqlserver-se</EngineName>
        <OptionGroupDescription>Default Mirroring-enabled option group for sqlserver-se 10.50</OptionGroupDescription>
        <Options>
          <Option>
            <OptionName>Mirroring</OptionName>
            <OptionDescription>SQLServer Database Mirroring</OptionDescription>
            <Persistent>false</Persistent>
            <Permanent>false</Permanent>
            <OptionSettings/>
            <VpcSecurityGroupMemberships/>
            <DBSecurityGroupMemberships/>
          </Option>
        </Options>
      </OptionGroup>
      <OptionGroup>
        <OptionGroupName>default:sqlserver-se-11-00</OptionGroupName>
        <AllowsVpcAndNonVpcInstanceMemberships>true</AllowsVpcAndNonVpcInstanceMemberships>
        <MajorEngineVersion>11.00</MajorEngineVersion>
        <EngineName>sqlserver-se</EngineName>
        <OptionGroupDescription>Default option group for sqlserver-se 11.00</OptionGroupDescription>
        <Options/>
      </OptionGroup>
      <OptionGroup>
        <OptionGroupName>myawsuser-opt-grp</OptionGroupName>
        <AllowsVpcAndNonVpcInstanceMemberships>false</AllowsVpcAndNonVpcInstanceMemberships>
        <MajorEngineVersion>11.2</MajorEngineVersion>
        <EngineName>oracle-ee</EngineName>
        <OptionGroupDescription>test option group</OptionGroupDescription>
        <Options>
          <Option>
            <OptionName>NATIVE_NETWORK_ENCRYPTION</OptionName>
            <OptionDescription>Oracle Advanced Security - Native Network Encryption</OptionDescription>
            <Persistent>false</Persistent>
            <Permanent>false</Permanent>
            <OptionSettings>
              <OptionSetting>
                <DataType>STRING</DataType>
                <IsModifiable>true</IsModifiable>
                <IsCollection>true</IsCollection>
                <Description>Specifies list of checksumming algorithms in order of intended use</Description>
                <Name>SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER</Name>
                <Value>SHA1,MD5</Value>
                <ApplyType>STATIC</ApplyType>
                <DefaultValue>SHA1,MD5</DefaultValue>
                <AllowedValues>SHA1,MD5</AllowedValues>
              </OptionSetting>
              <OptionSetting>
                <DataType>STRING</DataType>
                <IsModifiable>true</IsModifiable>
                <IsCollection>true</IsCollection>
                <Description>Specifies list of encryption algorithms in order of intended use</Description>
                <Name>SQLNET.ENCRYPTION_TYPES_SERVER</Name>
                <Value>RC4_256,AES256,AES192,3DES168,RC4_128,AES128,3DES112,RC4_56,DES,RC4_40,DES40</Value>
                <ApplyType>STATIC</ApplyType>
                <DefaultValue>RC4_256,AES256,AES192,3DES168,RC4_128,AES128,3DES112,RC4_56,DES,RC4_40,DES40</DefaultValue>
                <AllowedValues>RC4_256,AES256,AES192,3DES168,RC4_128,AES128,3DES112,RC4_56,DES,RC4_40,DES40</AllowedValues>
              </OptionSetting>
              <OptionSetting>
                <DataType>STRING</DataType>
                <IsModifiable>true</IsModifiable>
                <IsCollection>false</IsCollection>
                <Description>Specifies the desired encryption behavior</Description>
                <Name>SQLNET.ENCRYPTION_SERVER</Name>
                <Value>REQUESTED</Value>
                <ApplyType>STATIC</ApplyType>
                <DefaultValue>REQUESTED</DefaultValue>
                <AllowedValues>ACCEPTED,REJECTED,REQUESTED,REQUIRED</AllowedValues>
              </OptionSetting>
              <OptionSetting>
                <DataType>STRING</DataType>
                <IsModifiable>true</IsModifiable>
                <IsCollection>false</IsCollection>
                <Description>Specifies the desired data integrity behavior</Description>
                <Name>SQLNET.CRYPTO_CHECKSUM_SERVER</Name>
                <Value>REQUESTED</Value>
                <ApplyType>STATIC</ApplyType>
                <DefaultValue>REQUESTED</DefaultValue>
                <AllowedValues>ACCEPTED,REJECTED,REQUESTED,REQUIRED</AllowedValues>
              </OptionSetting>
            </OptionSettings>
            <VpcSecurityGroupMemberships/>
            <DBSecurityGroupMemberships/>
          </Option>
          <Option>
            <OptionName>XMLDB</OptionName>
            <OptionDescription>Oracle XMLDB Repository</OptionDescription>
            <Persistent>false</Persistent>
            <Permanent>false</Permanent>
            <OptionSettings/>
            <VpcSecurityGroupMemberships/>
            <DBSecurityGroupMemberships/>
          </Option>
          <Option>
            <Port>1158</Port>
            <OptionName>OEM</OptionName>
            <OptionDescription>Oracle Enterprise Manager (Database Control only)</OptionDescription>
            <Persistent>false</Persistent>
            <Permanent>false</Permanent>
            <OptionSettings/>
            <VpcSecurityGroupMemberships/>
            <DBSecurityGroupMemberships>
              <DBSecurityGroup>
                <Status>authorized</Status>
                <DBSecurityGroupName>sg-db-sec-grp</DBSecurityGroupName>
              </DBSecurityGroup>
            </DBSecurityGroupMemberships>
          </Option>
        </Options>
      </OptionGroup>
          <Option>
            <OptionName>APEX</OptionName>
            <OptionDescription>Oracle Application Express Runtime Environment</OptionDescription>
            <Persistent>false</Persistent>
            <Permanent>false</Permanent>
            <OptionSettings/>
            <VpcSecurityGroupMemberships/>
            <DBSecurityGroupMemberships/>
          </Option>
        </Options>
      </OptionGroup>
    </OptionGroupsList>
  </DescribeOptionGroupsResult>
  <ResponseMetadata>
    <RequestId>b2ce0772-f55a-11e3-bd0f-bb88ac05a37c</RequestId>
  </ResponseMetadata>
</DescribeOptionGroupsResponse>
```

## See Also
<a name="API_DescribeOptionGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeOptionGroups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeOptionGroups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeOptionGroups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeOptionGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeOptionGroups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeOptionGroups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeOptionGroups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeOptionGroups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeOptionGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeOptionGroups) 