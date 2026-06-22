---
id: "@specs/aws/redshift/docs/API_CreateHsmConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateHsmConfiguration"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# CreateHsmConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_CreateHsmConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateHsmConfiguration
<a name="API_CreateHsmConfiguration"></a>

Creates an HSM configuration that contains the information required by an Amazon Redshift cluster to store and use database encryption keys in a Hardware Security Module (HSM). After creating the HSM configuration, you can specify it as a parameter when creating a cluster. The cluster will then store its encryption keys in the HSM.

In addition to creating an HSM configuration, you must also create an HSM client certificate. For more information, go to [Hardware Security Modules](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-HSM.html) in the Amazon Redshift Cluster Management Guide.

## Request Parameters
<a name="API_CreateHsmConfiguration_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Description **   
A text description of the HSM configuration to be created.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** HsmConfigurationIdentifier **   
The identifier to be assigned to the new Amazon Redshift HSM configuration.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** HsmIpAddress **   
The IP address that the Amazon Redshift cluster must use to access the HSM.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** HsmPartitionName **   
The name of the partition in the HSM where the Amazon Redshift clusters will store their database encryption keys.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** HsmPartitionPassword **   
The password required to access the HSM partition.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 ** HsmServerPublicCertificate **   
The HSMs public certificate file. When using Cloud HSM, the file name is server.pem.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 **Tags.Tag.N**   
A list of tag instances.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateHsmConfiguration_ResponseElements"></a>

The following element is returned by the service.

 ** HsmConfiguration **   
Returns information about an HSM configuration, which is an object that describes to Amazon Redshift clusters the information they require to connect to an HSM where they can store database encryption keys.  
Type: [HsmConfiguration](API_HsmConfiguration.md) object

## Errors
<a name="API_CreateHsmConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** HsmConfigurationAlreadyExistsFault **   
There is already an existing Amazon Redshift HSM configuration with the specified identifier.  
HTTP Status Code: 400

 ** HsmConfigurationQuotaExceededFault **   
The quota for HSM configurations has been reached. For information about increasing your quota, go to [Limits in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html) in the *Amazon Redshift Cluster Management Guide*.   
HTTP Status Code: 400

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

 ** TagLimitExceededFault **   
You have exceeded the number of tags allowed.  
HTTP Status Code: 400

## Examples
<a name="API_CreateHsmConfiguration_Examples"></a>

### Example
<a name="API_CreateHsmConfiguration_Example_1"></a>

This example illustrates one usage of CreateHsmConfiguration.

#### Sample Request
<a name="API_CreateHsmConfiguration_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=CreateHsmConfiguration
&HsmConfigurationIdentifier=myhsmconnection
&Description=My+HSM+connection
&HsmIpAddress=192.0.2.09
&HsmPartitionName=myhsmpartition
&HsmPartitionPassword=A1b2c3d4
&HsmServerPublicCertificate=myhsmclientcert
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_CreateHsmConfiguration_Example_1_Response"></a>

```
<CreateHsmConfigurationResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <CreateHsmConfigurationResult>
    <HsmConfiguration>
      <Description>My HSM connection</Description>
      <HsmPartitionName>myhsmpartition</HsmPartitionName>
      <HsmConfigurationIdentifier>myhsmconnection</HsmConfigurationIdentifier>
      <Tags/>
      <HsmIpAddress>192.0.2.09</HsmIpAddress>
    </HsmConfiguration>
  </CreateHsmConfigurationResult>
  <ResponseMetadata>
    <RequestId>e106be9e-2833-11ea-9caa-c956bec1ce87</RequestId>
  </ResponseMetadata>
</CreateHsmConfigurationResponse>
```

## See Also
<a name="API_CreateHsmConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/CreateHsmConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/CreateHsmConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/CreateHsmConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/CreateHsmConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/CreateHsmConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/CreateHsmConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/CreateHsmConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/CreateHsmConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/CreateHsmConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/CreateHsmConfiguration) 