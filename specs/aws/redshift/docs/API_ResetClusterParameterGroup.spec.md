---
id: "@specs/aws/redshift/docs/API_ResetClusterParameterGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ResetClusterParameterGroup"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# ResetClusterParameterGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_ResetClusterParameterGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ResetClusterParameterGroup
<a name="API_ResetClusterParameterGroup"></a>

Sets one or more parameters of the specified parameter group to their default values and sets the source values of the parameters to "engine-default". To reset the entire parameter group specify the *ResetAllParameters* parameter. For parameter changes to take effect you must reboot any associated clusters. 

## Request Parameters
<a name="API_ResetClusterParameterGroup_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ParameterGroupName **   
The name of the cluster parameter group to be reset.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 **Parameters.Parameter.N**   
An array of names of parameters to be reset. If *ResetAllParameters* option is not used, then at least one parameter name must be supplied.   
Constraints: A maximum of 20 parameters can be reset in a single request.  
Type: Array of [Parameter](API_Parameter.md) objects  
Required: No

 ** ResetAllParameters **   
If `true`, all parameters in the specified parameter group will be reset to their default values.   
Default: `true`   
Type: Boolean  
Required: No

## Response Elements
<a name="API_ResetClusterParameterGroup_ResponseElements"></a>

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
<a name="API_ResetClusterParameterGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterParameterGroupNotFound **   
The parameter group name does not refer to an existing parameter group.  
HTTP Status Code: 404

 ** InvalidClusterParameterGroupState **   
The cluster parameter group action can not be completed because another task is in progress that involves the parameter group. Wait a few moments and try the operation again.  
HTTP Status Code: 400

## Examples
<a name="API_ResetClusterParameterGroup_Examples"></a>

### Example
<a name="API_ResetClusterParameterGroup_Example_1"></a>

This example illustrates one usage of ResetClusterParameterGroup.

#### Sample Request
<a name="API_ResetClusterParameterGroup_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=ResetClusterParameterGroup
&ParameterGroupName=myclusterparametergroup
&ResetAllParameters=true
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_ResetClusterParameterGroup_Example_1_Response"></a>

```
<ResetClusterParameterGroupResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <ResetClusterParameterGroupResult>
    <ParameterGroupName>myclusterparametergroup</ParameterGroupName>
    <ParameterGroupStatus>Your parameter group has been updated. If you changed only dynamic parameters, associated clusters are being modified now. If you changed static parameters, all updates, including dynamic parameters, will be applied when you reboot the associated clusters.</ParameterGroupStatus>
  </ResetClusterParameterGroupResult>
  <ResponseMetadata>
    <RequestId>9e0e57b9-28f5-11ea-9caa-c956bec1ce87</RequestId>
  </ResponseMetadata>
</ResetClusterParameterGroupResponse>
```

## See Also
<a name="API_ResetClusterParameterGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/ResetClusterParameterGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/ResetClusterParameterGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ResetClusterParameterGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/ResetClusterParameterGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ResetClusterParameterGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/ResetClusterParameterGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/ResetClusterParameterGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/ResetClusterParameterGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/ResetClusterParameterGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ResetClusterParameterGroup) 