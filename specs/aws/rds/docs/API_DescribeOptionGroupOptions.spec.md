---
id: "@specs/aws/rds/docs/API_DescribeOptionGroupOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeOptionGroupOptions"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeOptionGroupOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeOptionGroupOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeOptionGroupOptions
<a name="API_DescribeOptionGroupOptions"></a>

Describes all available options for the specified engine.

## Request Parameters
<a name="API_DescribeOptionGroupOptions_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EngineName **   
The name of the engine to describe options for.  
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
Required: Yes

 **Filters.Filter.N**   
This parameter isn't currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** MajorEngineVersion **   
If specified, filters the results to include only options for the specified major engine version.  
Type: String  
Required: No

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeOptionGroupOptions_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String

 **OptionGroupOptions.OptionGroupOption.N**   
List of available option group options.  
Type: Array of [OptionGroupOption](API_OptionGroupOption.md) objects

## Errors
<a name="API_DescribeOptionGroupOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeOptionGroupOptions_Examples"></a>

### Example
<a name="API_DescribeOptionGroupOptions_Example_1"></a>

This example illustrates one usage of DescribeOptionGroupOptions.

#### Sample Request
<a name="API_DescribeOptionGroupOptions_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
   ?Action=DescribeOptionGroupOptions
   &EngineName=oracle-se1
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140421/us-west-2/rds/aws4_request
   &X-Amz-Date=20140421T194733Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=3792d1669ce65ba1ba6a85b2e4057235e46dd3d0072663c17f4b4439fd8af702
```

#### Sample Response
<a name="API_DescribeOptionGroupOptions_Example_1_Response"></a>

```
<DescribeOptionGroupOptionsResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <DescribeOptionGroupOptionsResult>
    <OptionGroupOptions>
      <OptionGroupOption>
        <MajorEngineVersion>11.2</MajorEngineVersion>
        <PortRequired>false</PortRequired>
        <Persistent>false</Persistent>
        <OptionsDependedOn>
          <OptionName>XMLDB</OptionName>
        </OptionsDependedOn>
        <OptionsConflictsWith/>
        <Permanent>false</Permanent>
        <Description>Oracle Application Express Runtime Environment</Description>
        <Name>APEX</Name>
        <OptionGroupOptionSettings/>
        <EngineName>oracle-se1</EngineName>
        <MinimumRequiredMinorEngineVersion>0.2.v4</MinimumRequiredMinorEngineVersion>
      </OptionGroupOption>
      <OptionGroupOption>
        <MajorEngineVersion>11.2</MajorEngineVersion>
        <PortRequired>false</PortRequired>
        <Persistent>false</Persistent>
        <OptionsDependedOn>
          <OptionName>APEX</OptionName>
        </OptionsDependedOn>
        <OptionsConflictsWith/>
        <Permanent>false</Permanent>
        <Description>Oracle Application Express Development Environment</Description>
        <Name>APEX-DEV</Name>
        <OptionGroupOptionSettings/>
        <EngineName>oracle-se1</EngineName>
        <MinimumRequiredMinorEngineVersion>0.2.v4</MinimumRequiredMinorEngineVersion>
      </OptionGroupOption>
      <OptionGroupOption>
        <MajorEngineVersion>11.2</MajorEngineVersion>
        <PortRequired>true</PortRequired>
        <Persistent>false</Persistent>
        <OptionsDependedOn/>
        <OptionsConflictsWith/>        
        <Permanent>false</Permanent>
        <Description>Oracle Enterprise Manager (Database Control only)</Description>
        <DefaultPort>1158</DefaultPort>
        <Name>OEM</Name>
        <OptionGroupOptionSettings/>
        <EngineName>oracle-se1</EngineName>
        <MinimumRequiredMinorEngineVersion>0.2.v3</MinimumRequiredMinorEngineVersion>
      </OptionGroupOption>
    </OptionGroupOptions>
  </DescribeOptionGroupOptionsResult>
  <ResponseMetadata>
    <RequestId>b7b26a8f-b98c-11d3-f272-7cd6cce12cc5</RequestId>
  </ResponseMetadata>
</DescribeOptionGroupOptionsResponse>
```

## See Also
<a name="API_DescribeOptionGroupOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeOptionGroupOptions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeOptionGroupOptions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeOptionGroupOptions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeOptionGroupOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeOptionGroupOptions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeOptionGroupOptions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeOptionGroupOptions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeOptionGroupOptions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeOptionGroupOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeOptionGroupOptions) 