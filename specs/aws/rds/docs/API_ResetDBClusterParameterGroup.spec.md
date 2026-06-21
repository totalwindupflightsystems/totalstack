---
id: "@specs/aws/rds/docs/API_ResetDBClusterParameterGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ResetDBClusterParameterGroup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# ResetDBClusterParameterGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_ResetDBClusterParameterGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ResetDBClusterParameterGroup
<a name="API_ResetDBClusterParameterGroup"></a>

Modifies the parameters of a DB cluster parameter group to the default value. To reset specific parameters submit a list of the following: `ParameterName` and `ApplyMethod`. To reset the entire DB cluster parameter group, specify the `DBClusterParameterGroupName` and `ResetAllParameters` parameters.

When resetting the entire group, dynamic parameters are updated immediately and static parameters are set to `pending-reboot` to take effect on the next DB instance restart or `RebootDBInstance` request. You must call `RebootDBInstance` for every DB instance in your DB cluster that you want the updated static parameter to apply to.

For more information on Amazon Aurora DB clusters, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide*.

For more information on Multi-AZ DB clusters, see [ Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide.* 

## Request Parameters
<a name="API_ResetDBClusterParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterParameterGroupName **   
The name of the DB cluster parameter group to reset.  
Type: String  
Required: Yes

 **Parameters.Parameter.N**   
A list of parameter names in the DB cluster parameter group to reset to the default values. You can't use this parameter if the `ResetAllParameters` parameter is enabled.  
Type: Array of [Parameter](API_Parameter.md) objects  
Required: No

 ** ResetAllParameters **   
Specifies whether to reset all parameters in the DB cluster parameter group to their default values. You can't use this parameter if there is a list of parameter names specified for the `Parameters` parameter.  
Type: Boolean  
Required: No

## Response Elements
<a name="API_ResetDBClusterParameterGroup_ResponseElements"></a>

The following element is returned by the service.

 ** DBClusterParameterGroupName **   
The name of the DB cluster parameter group.  
Constraints:  
+ Must be 1 to 255 letters or numbers.
+ First character must be a letter
+ Can't end with a hyphen or contain two consecutive hyphens
This value is stored as a lowercase string.
Type: String

## Errors
<a name="API_ResetDBClusterParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBParameterGroupNotFound **   
 `DBParameterGroupName` doesn't refer to an existing DB parameter group.  
HTTP Status Code: 404

 ** InvalidDBParameterGroupState **   
The DB parameter group is in use or is in an invalid state. If you are attempting to delete the parameter group, you can't delete it when the parameter group is in this state.  
HTTP Status Code: 400

## Examples
<a name="API_ResetDBClusterParameterGroup_Examples"></a>

### Example
<a name="API_ResetDBClusterParameterGroup_Example_1"></a>

This example illustrates one usage of ResetDBClusterParameterGroup.

#### Sample Request
<a name="API_ResetDBClusterParameterGroup_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
    ?Action=ResetDBClusterParameterGroup
    &DBClusterParameterGroupName=sample-cluster-pg
    &Parameters.member.1.ApplyMethod=pending-reboot
    &Parameters.member.1.ParameterName=binlog_format
    &Parameters.member.2.ApplyMethod=pending-reboot
    &Parameters.member.2.ParameterName=innodb_support_xa
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20160913/us-west-2/rds/aws4_request
    &X-Amz-Date=20160913T230026Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=7cca4504082065e227696f2dd904fab2f39633bc7d120258c4bedd35da3ade7f
```

#### Sample Response
<a name="API_ResetDBClusterParameterGroup_Example_1_Response"></a>

```
<ResetDBClusterParameterGroupResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ResetDBClusterParameterGroupResult>
    <DBClusterParameterGroupName>sample-cluster-pg</DBClusterParameterGroupName>
  </ResetDBClusterParameterGroupResult>
  <ResponseMetadata>
    <RequestId>dc2c61eb-7a05-11e6-b83b-cd70a540d79f</RequestId>
  </ResponseMetadata>
</ResetDBClusterParameterGroupResponse>
```

## See Also
<a name="API_ResetDBClusterParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/ResetDBClusterParameterGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/ResetDBClusterParameterGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ResetDBClusterParameterGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/ResetDBClusterParameterGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ResetDBClusterParameterGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/ResetDBClusterParameterGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/ResetDBClusterParameterGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/ResetDBClusterParameterGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/ResetDBClusterParameterGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ResetDBClusterParameterGroup) 