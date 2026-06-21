---
id: "@specs/aws/rds/docs/API_ModifyDBClusterParameterGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyDBClusterParameterGroup"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# ModifyDBClusterParameterGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_ModifyDBClusterParameterGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyDBClusterParameterGroup
<a name="API_ModifyDBClusterParameterGroup"></a>

Modifies the parameters of a DB cluster parameter group. To modify more than one parameter, submit a list of the following: `ParameterName`, `ParameterValue`, and `ApplyMethod`. A maximum of 20 parameters can be modified in a single request.

**Important**  
There are two types of parameters - dynamic parameters and static parameters. Changes to dynamic parameters are applied to the DB cluster immediately without a reboot. Changes to static parameters are applied only after the DB cluster is rebooted, which can be done using `RebootDBCluster` operation. You can use the *Parameter Groups* option of the [Amazon RDS console](https://console.aws.amazon.com/rds/) or the `DescribeDBClusterParameters` operation to verify that your DB cluster parameter group has been created or modified.

For more information on Amazon Aurora DB clusters, see [ What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide*.

For more information on Multi-AZ DB clusters, see [ Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html) in the *Amazon RDS User Guide.* 

## Request Parameters
<a name="API_ModifyDBClusterParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterParameterGroupName **   
The name of the DB cluster parameter group to modify.  
Type: String  
Required: Yes

 **Parameters.Parameter.N**   
A list of parameters in the DB cluster parameter group to modify.  
Valid Values (for the application method): `immediate | pending-reboot`   
You can use the `immediate` value with dynamic parameters only. You can use the `pending-reboot` value for both dynamic and static parameters.  
When the application method is `immediate`, changes to dynamic parameters are applied immediately to the DB clusters associated with the parameter group. When the application method is `pending-reboot`, changes to dynamic and static parameters are applied after a reboot without failover to the DB clusters associated with the parameter group.
Type: Array of [Parameter](API_Parameter.md) objects  
Required: Yes

## Response Elements
<a name="API_ModifyDBClusterParameterGroup_ResponseElements"></a>

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
<a name="API_ModifyDBClusterParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBParameterGroupNotFound **   
 `DBParameterGroupName` doesn't refer to an existing DB parameter group.  
HTTP Status Code: 404

 ** InvalidDBParameterGroupState **   
The DB parameter group is in use or is in an invalid state. If you are attempting to delete the parameter group, you can't delete it when the parameter group is in this state.  
HTTP Status Code: 400

## Examples
<a name="API_ModifyDBClusterParameterGroup_Examples"></a>

### Example
<a name="API_ModifyDBClusterParameterGroup_Example_1"></a>

This example illustrates one usage of ModifyDBClusterParameterGroup.

#### Sample Request
<a name="API_ModifyDBClusterParameterGroup_Example_1_Request"></a>

```
https://rds.us-west-2.amazonaws.com/
    ?Action=ModifyDBClusterParameterGroup
    &DBClusterParameterGroupName=sample-cluster-pg
    &Parameters.member.1.ApplyMethod=pending-reboot
    &Parameters.member.1.ParameterName=binlog_format
    &Parameters.member.1.ParameterValue=MIXED
    &SignatureMethod=HmacSHA256
    &SignatureVersion=4
    &Version=2014-10-31
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Credential=AKIADQKE4SARGYLE/20160913/us-west-2/rds/aws4_request
    &X-Amz-Date=20160913T173245Z
    &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
    &X-Amz-Signature=cfb4f35de32455f77405636315dd431f2e236a1a997f94e0f6e00183d1f5156e
```

#### Sample Response
<a name="API_ModifyDBClusterParameterGroup_Example_1_Response"></a>

```
<ModifyDBClusterParameterGroupResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
  <ModifyDBClusterParameterGroupResult>
    <DBClusterParameterGroupName>sample-cluster-pg</DBClusterParameterGroupName>
  </ModifyDBClusterParameterGroupResult>
  <ResponseMetadata>
    <RequestId>1534d6a1-79d8-11e6-9b94-838991bd50c6</RequestId>
  </ResponseMetadata>
</ModifyDBClusterParameterGroupResponse>
```

## See Also
<a name="API_ModifyDBClusterParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/ModifyDBClusterParameterGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/ModifyDBClusterParameterGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ModifyDBClusterParameterGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/ModifyDBClusterParameterGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ModifyDBClusterParameterGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/ModifyDBClusterParameterGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/ModifyDBClusterParameterGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/ModifyDBClusterParameterGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/ModifyDBClusterParameterGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ModifyDBClusterParameterGroup) 