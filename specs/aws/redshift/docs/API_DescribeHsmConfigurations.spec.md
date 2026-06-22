---
id: "@specs/aws/redshift/docs/API_DescribeHsmConfigurations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeHsmConfigurations"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DescribeHsmConfigurations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DescribeHsmConfigurations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeHsmConfigurations
<a name="API_DescribeHsmConfigurations"></a>

Returns information about the specified Amazon Redshift HSM configuration. If no configuration ID is specified, returns information about all the HSM configurations owned by your AWS account.

If you specify both tag keys and tag values in the same request, Amazon Redshift returns all HSM connections that match any combination of the specified keys and values. For example, if you have `owner` and `environment` for tag keys, and `admin` and `test` for tag values, all HSM connections that have any combination of those values are returned.

If both tag keys and values are omitted from the request, HSM connections are returned regardless of whether they have tag keys or values associated with them.

## Request Parameters
<a name="API_DescribeHsmConfigurations_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** HsmConfigurationIdentifier **   
The identifier of a specific Amazon Redshift HSM configuration to be described. If no identifier is specified, information is returned for all HSM configurations owned by your AWS account.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** Marker **   
An optional parameter that specifies the starting point to return a set of response records. When the results of a [DescribeHsmConfigurations](#API_DescribeHsmConfigurations) request exceed the value specified in `MaxRecords`, AWS returns a value in the `Marker` field of the response. You can retrieve the next set of response records by providing the returned marker value in the `Marker` parameter and retrying the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: No

 ** MaxRecords **   
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified `MaxRecords` value, a value is returned in a `marker` field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.   
Default: `100`   
Constraints: minimum 20, maximum 100.  
Type: Integer  
Required: No

 **TagKeys.TagKey.N**   
A tag key or keys for which you want to return all matching HSM configurations that are associated with the specified key or keys. For example, suppose that you have HSM configurations that are tagged with keys called `owner` and `environment`. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the HSM configurations that have either or both of these tag keys associated with them.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

 **TagValues.TagValue.N**   
A tag value or values for which you want to return all matching HSM configurations that are associated with the specified tag value or values. For example, suppose that you have HSM configurations that are tagged with values called `admin` and `test`. If you specify both of these tag values in the request, Amazon Redshift returns a response with the HSM configurations that have either or both of these tag values associated with them.  
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: No

## Response Elements
<a name="API_DescribeHsmConfigurations_ResponseElements"></a>

The following elements are returned by the service.

 **HsmConfigurations.HsmConfiguration.N**   
A list of `HsmConfiguration` objects.  
Type: Array of [HsmConfiguration](API_HsmConfiguration.md) objects

 ** Marker **   
A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the `Marker` parameter and retrying the command. If the `Marker` field is empty, all response records have been retrieved for the request.   
Type: String  
Length Constraints: Maximum length of 2147483647.

## Errors
<a name="API_DescribeHsmConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** HsmConfigurationNotFoundFault **   
There is no Amazon Redshift HSM configuration with the specified identifier.  
HTTP Status Code: 400

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

## Examples
<a name="API_DescribeHsmConfigurations_Examples"></a>

### Example
<a name="API_DescribeHsmConfigurations_Example_1"></a>

This example illustrates one usage of DescribeHsmConfigurations.

#### Sample Request
<a name="API_DescribeHsmConfigurations_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DescribeHsmConfigurations
&HsmConfigurationIdentifier=myhsmconnection
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_DescribeHsmConfigurations_Example_1_Response"></a>

```
<DescribeHsmConfigurationsResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <DescribeHsmConfigurationsResult>
    <HsmConfigurations>
      <HsmConfiguration>
        <Description>My HSM partition</Description>
        <HsmPartitionName>myhsmpartition</HsmPartitionName>
        <HsmConfigurationIdentifier>myhsmconnection</HsmConfigurationIdentifier>
        <Tags/>
        <HsmIpAddress>192.0.2.09</HsmIpAddress>
      </HsmConfiguration>
    </HsmConfigurations>
  </DescribeHsmConfigurationsResult>
  <ResponseMetadata>
    <RequestId>367be4c0-28cc-11ea-8314-974e2ba81189</RequestId>
  </ResponseMetadata>
</DescribeHsmConfigurationsResponse>
```

## See Also
<a name="API_DescribeHsmConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DescribeHsmConfigurations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DescribeHsmConfigurations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DescribeHsmConfigurations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DescribeHsmConfigurations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DescribeHsmConfigurations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DescribeHsmConfigurations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DescribeHsmConfigurations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DescribeHsmConfigurations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DescribeHsmConfigurations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DescribeHsmConfigurations) 