---
id: "@specs/aws/redshift/docs/API_ModifyClusterParameterGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ModifyClusterParameterGroup"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ModifyClusterParameterGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ModifyClusterParameterGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ModifyClusterParameterGroup
<a name="API_ModifyClusterParameterGroup"></a>

Modifies the parameters of a parameter group. For the parameters parameter, it can't contain ASCII characters.

 For more information about parameters and parameter groups, go to [Amazon Redshift Parameter Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) in the *Amazon Redshift Cluster Management Guide*.

## Request Parameters
<a name="API_ModifyClusterParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ParameterGroupName **   
The name of the parameter group to be modified.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 **Parameters.Parameter.N**   
An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.  
For each parameter to be modified, you must supply at least the parameter name and parameter value; other name-value pairs of the parameter are optional.  
For the workload management (WLM) configuration, you must supply all the name-value pairs in the wlm\_json\_configuration parameter.  
Type: Array of [Parameter](API_Parameter.md) objects  
Required: Yes

## Response Elements
<a name="API_ModifyClusterParameterGroup_ResponseElements"></a>

The following elements are returned by the service.

 ** ParameterGroupName **   
The name of the cluster parameter group.  
Type: String  
Length Constraints: Maximum length of 2147483647.

 ** ParameterGroupStatus **   
The status of the parameter group. For example, if you made a change to a parameter group name-value pair, then the change could be pending a reboot of an associated cluster.  
Type: String  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_ModifyClusterParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterParameterGroupNotFound **   
The parameter group name does not refer to an existing parameter group.  
HTTP Status Code: 404

 ** InvalidClusterParameterGroupState **   
The cluster parameter group action can not be completed because another task is in progress that involves the parameter group. Wait a few moments and try the operation again.  
HTTP Status Code: 400

## Examples
<a name="API_ModifyClusterParameterGroup_Examples"></a>

### Example
<a name="API_ModifyClusterParameterGroup_Example_1"></a>

This example illustrates one usage of ModifyClusterParameterGroup.

#### Sample Request
<a name="API_ModifyClusterParameterGroup_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=ModifyClusterParameterGroup
&ParameterGroupName=myclusterparametergroup
&Parameters.Parameter.1.ParameterName=auto_analyze
&Parameters.Parameter.1.ParameterValue=false
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_ModifyClusterParameterGroup_Example_1_Response"></a>

```
<ModifyClusterParameterGroupResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <ModifyClusterParameterGroupResult>
    <ParameterGroupName>myclusterparametergroup</ParameterGroupName>
    <ParameterGroupStatus>Your parameter group has been updated. If you changed only dynamic parameters, associated clusters are being modified now. If you changed static parameters, all updates, including dynamic parameters, will be applied when you reboot the associated clusters.</ParameterGroupStatus>
  </ModifyClusterParameterGroupResult>
  <ResponseMetadata>
    <RequestId>565b33e6-28e9-11ea-9939-5fccefa818c0</RequestId>
  </ResponseMetadata>
</ModifyClusterParameterGroupResponse>
```

## See Also
<a name="API_ModifyClusterParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/ModifyClusterParameterGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/ModifyClusterParameterGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ModifyClusterParameterGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/ModifyClusterParameterGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ModifyClusterParameterGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/ModifyClusterParameterGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/ModifyClusterParameterGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/ModifyClusterParameterGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/ModifyClusterParameterGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ModifyClusterParameterGroup) 