---
id: "@specs/aws/redshift/docs/API_DeleteHsmConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteHsmConfiguration"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DeleteHsmConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DeleteHsmConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteHsmConfiguration
<a name="API_DeleteHsmConfiguration"></a>

Deletes the specified Amazon Redshift HSM configuration.

## Request Parameters
<a name="API_DeleteHsmConfiguration_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** HsmConfigurationIdentifier **   
The identifier of the Amazon Redshift HSM configuration to be deleted.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Errors
<a name="API_DeleteHsmConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** HsmConfigurationNotFoundFault **   
There is no Amazon Redshift HSM configuration with the specified identifier.  
HTTP Status Code: 400

 ** InvalidHsmConfigurationStateFault **   
The specified HSM configuration is not in the `available` state, or it is still in use by one or more Amazon Redshift clusters.  
HTTP Status Code: 400

## Examples
<a name="API_DeleteHsmConfiguration_Examples"></a>

### Example
<a name="API_DeleteHsmConfiguration_Example_1"></a>

This example illustrates one usage of DeleteHsmConfiguration.

#### Sample Request
<a name="API_DeleteHsmConfiguration_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DeleteHsmConfiguration
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
<a name="API_DeleteHsmConfiguration_Example_1_Response"></a>

```
<DeleteHsmConfigurationResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <ResponseMetadata>
    <RequestId>3d45f314-283a-11ea-8397-219d1980588b</RequestId>
  </ResponseMetadata>
</DeleteHsmConfigurationResponse>
```

## See Also
<a name="API_DeleteHsmConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DeleteHsmConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DeleteHsmConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DeleteHsmConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DeleteHsmConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DeleteHsmConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DeleteHsmConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DeleteHsmConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DeleteHsmConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DeleteHsmConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DeleteHsmConfiguration) 