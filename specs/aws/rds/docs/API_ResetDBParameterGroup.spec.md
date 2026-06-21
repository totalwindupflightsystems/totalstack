---
id: "@specs/aws/rds/docs/API_ResetDBParameterGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ResetDBParameterGroup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# ResetDBParameterGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_ResetDBParameterGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ResetDBParameterGroup
<a name="API_ResetDBParameterGroup"></a>

Modifies the parameters of a DB parameter group to the engine/system default value. To reset specific parameters, provide a list of the following: `ParameterName` and `ApplyMethod`. To reset the entire DB parameter group, specify the `DBParameterGroup` name and `ResetAllParameters` parameters. When resetting the entire group, dynamic parameters are updated immediately and static parameters are set to `pending-reboot` to take effect on the next DB instance restart or `RebootDBInstance` request.

## Request Parameters
<a name="API_ResetDBParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBParameterGroupName **   
The name of the DB parameter group.  
Constraints:  
+ Must match the name of an existing `DBParameterGroup`.
Type: String  
Required: Yes

 **Parameters.Parameter.N**   
To reset the entire DB parameter group, specify the `DBParameterGroup` name and `ResetAllParameters` parameters. To reset specific parameters, provide a list of the following: `ParameterName` and `ApplyMethod`. A maximum of 20 parameters can be modified in a single request.  
 **MySQL**   
Valid Values (for Apply method): `immediate` \| `pending-reboot`   
You can use the immediate value with dynamic parameters only. You can use the `pending-reboot` value for both dynamic and static parameters, and changes are applied when DB instance reboots.  
 **MariaDB**   
Valid Values (for Apply method): `immediate` \| `pending-reboot`   
You can use the immediate value with dynamic parameters only. You can use the `pending-reboot` value for both dynamic and static parameters, and changes are applied when DB instance reboots.  
 **Oracle**   
Valid Values (for Apply method): `pending-reboot`   
Type: Array of [Parameter](API_Parameter.md) objects  
Required: No

 ** ResetAllParameters **   
Specifies whether to reset all parameters in the DB parameter group to default values. By default, all parameters in the DB parameter group are reset to default values.  
Type: Boolean  
Required: No

## Response Elements
<a name="API_ResetDBParameterGroup_ResponseElements"></a>

The following element is returned by the service.

 ** DBParameterGroupName **   
The name of the DB parameter group.  
Type: String

## Errors
<a name="API_ResetDBParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBParameterGroupNotFound **   
 `DBParameterGroupName` doesn't refer to an existing DB parameter group.  
HTTP Status Code: 404

 ** InvalidDBParameterGroupState **   
The DB parameter group is in use or is in an invalid state. If you are attempting to delete the parameter group, you can't delete it when the parameter group is in this state.  
HTTP Status Code: 400

## Examples
<a name="API_ResetDBParameterGroup_Examples"></a>

### Example
<a name="API_ResetDBParameterGroup_Example_1"></a>

This example illustrates one usage of ResetDBParameterGroup.

#### Sample Request
<a name="API_ResetDBParameterGroup_Example_1_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=ResetDBParameterGroup
   &DBParameterGroupName=mydbparametergroup01
   &ResetAllParameters=true
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140428/us-east-1/rds/aws4_request
   &X-Amz-Date=20140428T225714Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=709d1418c91c5ef4129d4665e5c2820002a9665699acf4204683c778f03c3573
```

#### Sample Response
<a name="API_ResetDBParameterGroup_Example_1_Response"></a>

```
<ResetDBParameterGroupResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ResetDBParameterGroupResult>
    <DBParameterGroupName>mydbparametergroup01</DBParameterGroupName>
  </ResetDBParameterGroupResult>
  <ResponseMetadata>
    <RequestId>610909c6-be27-11d3-a71c-13dc2f771e41</RequestId>
  </ResponseMetadata>
</ResetDBParameterGroupResponse>
```

### Example
<a name="API_ResetDBParameterGroup_Example_2"></a>

This example illustrates one usage of ResetDBParameterGroup.

#### Sample Request
<a name="API_ResetDBParameterGroup_Example_2_Request"></a>

```
https://rds.us-east-1.amazonaws.com/
   ?Action=ResetDBParameterGroup
   &DBParameterGroupName=mydbparametergroup01
   &Parameters.member.1.ApplyMethod=immediate
   &Parameters.member.1.ParameterName=bulk_insert_buffer_size
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20140428/us-east-1/rds/aws4_request
   &X-Amz-Date=20140428T230509Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=d343dd7fcc3789d30295b5e3fc67262f28af15d71fcaf978921f0e8846b2d1e6
```

#### Sample Response
<a name="API_ResetDBParameterGroup_Example_2_Response"></a>

```
<ResetDBParameterGroupResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ResetDBParameterGroupResult>
    <DBParameterGroupName>mydbparametergroup01</DBParameterGroupName>
  </ResetDBParameterGroupResult>
  <ResponseMetadata>
    <RequestId>7acb72cf-be28-11d3-a4fc-e3b7f6c20c5f</RequestId>
  </ResponseMetadata>
</ResetDBParameterGroupResponse>
```

## See Also
<a name="API_ResetDBParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/ResetDBParameterGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/ResetDBParameterGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ResetDBParameterGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/ResetDBParameterGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ResetDBParameterGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/ResetDBParameterGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/ResetDBParameterGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/ResetDBParameterGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/ResetDBParameterGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ResetDBParameterGroup) 