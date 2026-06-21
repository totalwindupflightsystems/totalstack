---
id: "@specs/aws/rds/docs/API_CreateOptionGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateOptionGroup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# CreateOptionGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_CreateOptionGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateOptionGroup
<a name="API_CreateOptionGroup"></a>

Creates a new option group. You can create up to 20 option groups.

This command doesn't apply to RDS Custom.

## Request Parameters
<a name="API_CreateOptionGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** EngineName **   
The name of the engine to associate this option group with.  
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

 ** MajorEngineVersion **   
Specifies the major version of the engine that this option group should be associated with.  
Type: String  
Required: Yes

 ** OptionGroupDescription **   
The description of the option group.  
Type: String  
Required: Yes

 ** OptionGroupName **   
Specifies the name of the option group to be created.  
Constraints:  
+ Must be 1 to 255 letters, numbers, or hyphens
+ First character must be a letter
+ Can't end with a hyphen or contain two consecutive hyphens
Example: `myoptiongroup`   
Type: String  
Required: Yes

 **Tags.Tag.N**   
Tags to assign to the option group.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateOptionGroup_ResponseElements"></a>

The following element is returned by the service.

 ** OptionGroup **   
  
Type: [OptionGroup](API_OptionGroup.md) object

## Errors
<a name="API_CreateOptionGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OptionGroupAlreadyExistsFault **   
The option group you are trying to create already exists.  
HTTP Status Code: 400

 ** OptionGroupQuotaExceededFault **   
The quota of 20 option groups was exceeded for this AWS account.  
HTTP Status Code: 400

## Examples
<a name="API_CreateOptionGroup_Examples"></a>

### Example
<a name="API_CreateOptionGroup_Example_1"></a>

This example illustrates one usage of CreateOptionGroup.

#### Sample Request
<a name="API_CreateOptionGroup_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=CreateOptionGroup
   &EngineName=mysql
   &MajorEngineVersion=5.6
   &OptionGroupDescription=My%20Option%20Group
   &OptionGroupName=myawsuser-og00
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140425/us-east-1/rds/aws4_request
   &X-Amz-Date=20140425T174519Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=d3a89afa4511d0c4ecab046d6dc760a72bfe6bb15999cce053adeb2617b60384
```

#### Sample Response
<a name="API_CreateOptionGroup_Example_1_Response"></a>

```
<CreateOptionGroupResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <CreateOptionGroupResult>
    <OptionGroup>
      <AllowsVpcAndNonVpcInstanceMemberships>true</AllowsVpcAndNonVpcInstanceMemberships>
      <MajorEngineVersion>5.6</MajorEngineVersion>
      <OptionGroupName>myawsuser-og00</OptionGroupName>
      <EngineName>mysql</EngineName>
      <OptionGroupDescription>My Option Group</OptionGroupDescription>
      <Options/>
    </OptionGroup>
  </CreateOptionGroupResult>
  <ResponseMetadata>
    <RequestId>4d7f11f2-bbf0-11d3-ae4f-eec568ed6b36</RequestId>
  </ResponseMetadata>
</CreateOptionGroupResponse>
```

## See Also
<a name="API_CreateOptionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/CreateOptionGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/CreateOptionGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/CreateOptionGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/CreateOptionGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/CreateOptionGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/CreateOptionGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/CreateOptionGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/CreateOptionGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/CreateOptionGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/CreateOptionGroup) 