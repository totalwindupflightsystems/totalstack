---
id: "@specs/aws/redshift/docs/API_DescribeClusterParameters"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeClusterParameters"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeClusterParameters

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeClusterParameters
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeClusterParameters
<a name="API_DescribeClusterParameters"></a>

Returns a detailed list of parameters contained within the specified Amazon Redshift parameter group. For each parameter the response includes information such as parameter name, description, data type, value, whether the parameter value is modifiable, and so on.

You can specify *source* filter to retrieve parameters of only specific type. For example, to retrieve parameters that were modified by a user action such as from [ModifyClusterParameterGroup](API_ModifyClusterParameterGroup.md), you can specify *source* equal to *user*.

 For more information about parameters and parameter groups, go to [Amazon Redshift Parameter Groups](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html) in the *Amazon Redshift Cluster Management Guide*.

## Request Parameters
<a name="API_DescribeClusterParameters_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ParameterGroupName **   
The name of a cluster parameter group for which to return details.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a [DescribeClusterParameters](#API_DescribeClusterParameters) request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `marker` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.   
Default: `100`   
Constraints: minimum 20, maximum 100.  
Type: Integer  
Required: No

 ** Source **   
The parameter types to return. Specify `user` to show parameters that are different form the default. Similarly, specify `engine-default` to show parameters that are the same as the default parameter group.   
Default: All parameter types returned.  
Valid Values: `user` \| `engine-default`   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DescribeClusterParameters_ResponseElements"></a>

The following elements are returned by the service.

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `Marker` parameter and retrying the command. If the `Marker` field is empty, all response records have been retrieved for the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.

 **Parameters.Parameter.N**   
A list of [Parameter](API_Parameter.md) instances. Each instance lists the parameters of one cluster parameter group.   
Type: Array of [Parameter](API_Parameter.md) objects

## Errors
<a name="API_DescribeClusterParameters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterParameterGroupNotFound **   
The parameter group name does not refer to an existing parameter group.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeClusterParameters_Examples"></a>

### Example
<a name="API_DescribeClusterParameters_Example_1"></a>

This example illustrates one usage of DescribeClusterParameters.

#### Sample Request
<a name="API_DescribeClusterParameters_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
    ?Action=DescribeClusterParameters
&ParameterGroupName=myclusterparametergroup
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeClusterParameters_Example_1_Response"></a>

```
<DescribeClusterParametersResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeClusterParametersResult>
    <Parameters>
      <Parameter>
        <ApplyType>static</ApplyType>
        <AllowedValues>true,false</AllowedValues>
        <DataType>boolean</DataType>
        <Description>Use auto analyze</Description>
        <Source>engine-default</Source>
        <ParameterName>auto_analyze</ParameterName>
        <ParameterValue>true</ParameterValue>
        <IsModifiable>true</IsModifiable>
      </Parameter>
      <Parameter>
        <ApplyType>static</ApplyType>
        <DataType>string</DataType>
        <Description>Sets the display format for date and time values.</Description>
        <Source>engine-default</Source>
        <ParameterName>datestyle</ParameterName>
        <ParameterValue>ISO, MDY</ParameterValue>
        <IsModifiable>true</IsModifiable>
      </Parameter>
      <Parameter>
        <ApplyType>static</ApplyType>
        <AllowedValues>true,false</AllowedValues>
        <DataType>boolean</DataType>
        <Description>parameter for audit logging purpose</Description>
        <Source>engine-default</Source>
        <ParameterName>enable_user_activity_logging</ParameterName>
        <ParameterValue>false</ParameterValue>
        <IsModifiable>true</IsModifiable>
      </Parameter>
      <Parameter>
        <ApplyType>static</ApplyType>
        <AllowedValues>-15-2</AllowedValues>
        <DataType>integer</DataType>
        <Description>Sets the number of digits displayed for floating-point values</Description>
        <Source>engine-default</Source>
        <ParameterName>extra_float_digits</ParameterName>
        <ParameterValue>0</ParameterValue>
        <IsModifiable>true</IsModifiable>
      </Parameter>
      <Parameter>
        <ApplyType>static</ApplyType>
        <AllowedValues>0-10</AllowedValues>
        <DataType>integer</DataType>
        <Description>The maximum concurrency scaling clusters can be used.</Description>
        <Source>engine-default</Source>
        <ParameterName>max_concurrency_scaling_clusters</ParameterName>
        <ParameterValue>1</ParameterValue>
        <IsModifiable>true</IsModifiable>
      </Parameter>
      <Parameter>
        <ApplyType>static</ApplyType>
        <AllowedValues>0-14400000</AllowedValues>
        <DataType>integer</DataType>
        <Description>Sets the max cursor result set size</Description>
        <Source>engine-default</Source>
        <ParameterName>max_cursor_result_set_size</ParameterName>
        <ParameterValue>default</ParameterValue>
        <IsModifiable>true</IsModifiable>
      </Parameter>
      <Parameter>
        <ApplyType>static</ApplyType>
        <DataType>string</DataType>
        <Description>This parameter applies a user-defined label to a group of queries that are run during the same session..</Description>
        <Source>engine-default</Source>
        <ParameterName>query_group</ParameterName>
        <ParameterValue>default</ParameterValue>
        <IsModifiable>true</IsModifiable>
      </Parameter>
      <Parameter>
        <ApplyType>static</ApplyType>
        <AllowedValues>true,false</AllowedValues>
        <DataType>boolean</DataType>
        <Description>require ssl for all databaseconnections</Description>
        <Source>engine-default</Source>
        <ParameterName>require_ssl</ParameterName>
        <ParameterValue>false</ParameterValue>
        <IsModifiable>true</IsModifiable>
      </Parameter>
      <Parameter>
        <ApplyType>static</ApplyType>
        <DataType>string</DataType>
        <Description>Sets the schema search order for names that are not schema-qualified.</Description>
        <Source>engine-default</Source>
        <ParameterName>search_path</ParameterName>
        <ParameterValue>$user, public</ParameterValue>
        <IsModifiable>true</IsModifiable>
      </Parameter>
      <Parameter>
        <ApplyType>static</ApplyType>
        <AllowedValues>0,100-2147483647</AllowedValues>
        <DataType>integer</DataType>
        <Description>Stops any statement that takes over the specified number of milliseconds.</Description>
        <Source>engine-default</Source>
        <ParameterName>statement_timeout</ParameterName>
        <ParameterValue>0</ParameterValue>
        <IsModifiable>true</IsModifiable>
      </Parameter>
      <Parameter>
        <ApplyType>static</ApplyType>
        <AllowedValues>true,false</AllowedValues>
        <DataType>boolean</DataType>
        <Description>Use fips ssl library</Description>
        <Source>engine-default</Source>
        <ParameterName>use_fips_ssl</ParameterName>
        <ParameterValue>false</ParameterValue>
        <IsModifiable>true</IsModifiable>
      </Parameter>
      <Parameter>
        <ApplyType>static</ApplyType>
        <DataType>string</DataType>
        <Description>wlm json configuration</Description>
        <Source>engine-default</Source>
        <ParameterName>wlm_json_configuration</ParameterName>
        <ParameterValue>[{"auto_wlm":true}]</ParameterValue>
        <IsModifiable>true</IsModifiable>
      </Parameter>
    </Parameters>
  </DescribeClusterParametersResult>
  <ResponseMetadata>
    <RequestId>a22ce073-2831-11ea-a940-1b28a85fd753</RequestId>
  </ResponseMetadata>
</DescribeClusterParametersResponse>
```

## See Also
<a name="API_DescribeClusterParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeClusterParameters) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeClusterParameters) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeClusterParameters) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeClusterParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeClusterParameters) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeClusterParameters) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeClusterParameters) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeClusterParameters) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeClusterParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeClusterParameters) 