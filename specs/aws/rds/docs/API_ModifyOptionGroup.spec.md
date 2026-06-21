---
id: "@specs/aws/rds/docs/API_ModifyOptionGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyOptionGroup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# ModifyOptionGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_ModifyOptionGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyOptionGroup
<a name="API_ModifyOptionGroup"></a>

Modifies an existing option group.

## Request Parameters
<a name="API_ModifyOptionGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** OptionGroupName **   
The name of the option group to be modified.  
Permanent options, such as the TDE option for Oracle Advanced Security TDE, can't be removed from an option group, and that option group can't be removed from a DB instance once it is associated with a DB instance  
Type: String  
Required: Yes

 ** ApplyImmediately **   
Specifies whether to apply the change immediately or during the next maintenance window for each instance associated with the option group.  
Type: Boolean  
Required: No

 **OptionsToInclude.OptionConfiguration.N**   
Options in this list are added to the option group or, if already present, the specified configuration is used to update the existing configuration.  
Type: Array of [OptionConfiguration](API_OptionConfiguration.md) objects  
Required: No

 **OptionsToRemove.member.N**   
Options in this list are removed from the option group.  
Type: Array of strings  
Required: No

## Response Elements
<a name="API_ModifyOptionGroup_ResponseElements"></a>

The following element is returned by the service.

 ** OptionGroup **   
  
Type: [OptionGroup](API_OptionGroup.md) object

## Errors
<a name="API_ModifyOptionGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidOptionGroupStateFault **   
The option group isn't in the *available* state.  
HTTP Status Code: 400

 ** OptionGroupNotFoundFault **   
The specified option group could not be found.  
HTTP Status Code: 404

## Examples
<a name="API_ModifyOptionGroup_Examples"></a>

### Example
<a name="API_ModifyOptionGroup_Example_1"></a>

This example illustrates one usage of ModifyOptionGroup.

#### Sample Request
<a name="API_ModifyOptionGroup_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
    ?Action=ModifyOptionGroup
    &ApplyImmediately=true
    &OptionGroupName=myawsuser-og02
    &OptionsToInclude.member.1.DBSecurityGroupMemberships.member.1=default
    &OptionsToInclude.member.1.OptionName=MEMCACHED
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20140501/us-east-1/rds/aws4_request
    &X-Amz-Date=20140501T230529Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=4b278baae6294738704a9948e355af0e9bd4fa0913d5b35b0a9a3c916925aced
```

#### Sample Response
<a name="API_ModifyOptionGroup_Example_1_Response"></a>

```
<ModifyOptionGroupResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ModifyOptionGroupResult>
    <OptionGroup>
      <OptionGroupName>myawsuser-og02</OptionGroupName>
      <MajorEngineVersion>5.6</MajorEngineVersion>
      <AllowsVpcAndNonVpcInstanceMemberships>false</AllowsVpcAndNonVpcInstanceMemberships>
      <EngineName>mysql</EngineName>
      <OptionGroupDescription>my second og</OptionGroupDescription>
      <Options>
        <Option>
          <Port>11211</Port>
          <OptionName>MEMCACHED</OptionName>
          <OptionDescription>Innodb Memcached for MySQL</OptionDescription>
          <Persistent>false</Persistent>
          <OptionSettings>
            <OptionSetting>
              <DataType>BOOLEAN</DataType>
              <IsModifiable>true</IsModifiable>
              <IsCollection>false</IsCollection>
              <Description>If enabled when there is no more memory to store items, memcached will return an error rather than evicting items.</Description>
              <Name>ERROR_ON_MEMORY_EXHAUSTED</Name>
              <Value>0</Value>
              <ApplyType>STATIC</ApplyType>
              <AllowedValues>0,1</AllowedValues>
              <DefaultValue>0</DefaultValue>
            </OptionSetting>
            <OptionSetting>
              <DataType>INTEGER</DataType>
              <IsModifiable>true</IsModifiable>
              <IsCollection>false</IsCollection>
              <Description>The backlog queue configures how many network connections can be waiting to be processed by memcached</Description>
              <Name>BACKLOG_QUEUE_LIMIT</Name>
              <Value>1024</Value>
              <ApplyType>STATIC</ApplyType>
              <AllowedValues>1-2048</AllowedValues>
              <DefaultValue>1024</DefaultValue>
            </OptionSetting>
          </OptionSettings>
          <VpcSecurityGroupMemberships/>
          <Permanent>false</Permanent>
          <DBSecurityGroupMemberships>
            <DBSecurityGroup>
              <Status>authorized</Status>
              <DBSecurityGroupName>default</DBSecurityGroupName>
            </DBSecurityGroup>
          </DBSecurityGroupMemberships>
        </Option>
      </Options>
    </OptionGroup>
  </ModifyOptionGroupResult>
  <ResponseMetadata>
    <RequestId>073cfb45-c184-11d3-a537-cef97546330c</RequestId>
  </ResponseMetadata>
</ModifyOptionGroupResponse>
```

### Example
<a name="API_ModifyOptionGroup_Example_2"></a>

This example illustrates one usage of ModifyOptionGroup.

#### Sample Request
<a name="API_ModifyOptionGroup_Example_2_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
    ?Action=ModifyOptionGroup
    &ApplyImmediately=true
    &OptionGroupName=myawsuser-og02
    &OptionsToRemove.OptionName=MEMCACHED
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20140501/us-east-1/rds/aws4_request
    &X-Amz-Date=20140501T231731Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=fd7ee924d39f1014488eb3444a8fdfb028e958b97703f95845a5addc435c1399
```

#### Sample Response
<a name="API_ModifyOptionGroup_Example_2_Response"></a>

```
<ModifyOptionGroupResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ModifyOptionGroupResult>
    <OptionGroup>
      <OptionGroupName>myawsuser-og02</OptionGroupName>
      <AllowsVpcAndNonVpcInstanceMemberships>true</AllowsVpcAndNonVpcInstanceMemberships>
      <MajorEngineVersion>5.6</MajorEngineVersion>
      <EngineName>mysql</EngineName>
      <OptionGroupDescription>my second og</OptionGroupDescription>
      <Options/>
    </OptionGroup>
  </ModifyOptionGroupResult>
  <ResponseMetadata>
    <RequestId>b5f134f3-c185-11d3-f4c6-37db295f7674</RequestId>
  </ResponseMetadata>
</ModifyOptionGroupResponse>
```

## See Also
<a name="API_ModifyOptionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/ModifyOptionGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/ModifyOptionGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ModifyOptionGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/ModifyOptionGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ModifyOptionGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/ModifyOptionGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/ModifyOptionGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/ModifyOptionGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/ModifyOptionGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ModifyOptionGroup) 