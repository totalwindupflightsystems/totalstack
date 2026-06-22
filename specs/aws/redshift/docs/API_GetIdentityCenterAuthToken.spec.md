---
id: "@specs/aws/redshift/docs/API_GetIdentityCenterAuthToken"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetIdentityCenterAuthToken"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# GetIdentityCenterAuthToken

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_GetIdentityCenterAuthToken
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetIdentityCenterAuthToken
<a name="API_GetIdentityCenterAuthToken"></a>

Generates an encrypted authentication token that propagates the caller's AWS IAM Identity Center identity to Amazon Redshift clusters. This API extracts the AWS IAM Identity Center identity from enhanced credentials and creates a secure token that Amazon Redshift drivers can use for authentication.

The token is encrypted using AWS Key Management Service (KMS) and can only be decrypted by the specified Amazon Redshift clusters. The token contains the caller's AWS IAM Identity Center identity information and is valid for a limited time period.

This API is exclusively for use with AWS IAM Identity Center enhanced credentials. If the caller is not using enhanced credentials with embedded AWS IAM Identity Center identity, the API will return an error.

## Request Parameters
<a name="API_GetIdentityCenterAuthToken_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **ClusterIds.ClusterIdentifier.N**   
A list of cluster identifiers that the generated token can be used with. The token will be scoped to only allow authentication to the specified clusters.  
Constraints:  
+  `ClusterIds` must contain at least 1 cluster identifier.
+  `ClusterIds` can hold a maximum of 20 cluster identifiers.
+ Cluster identifiers must be 1 to 63 characters in length.
+ The characters accepted for cluster identifiers are the following:
  + Alphanumeric characters
  + Hyphens
+ Cluster identifiers must start with a letter.
+ Cluster identifiers can't end with a hyphen or contain two consecutive hyphens.
Type: Array of strings  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Response Elements
<a name="API_GetIdentityCenterAuthToken_ResponseElements"></a>

The following elements are returned by the service.

 ** ExpirationTime **   
The time (UTC) when the token expires. After this timestamp, the token will no longer be valid for authentication.  
Type: Timestamp

 ** Token **   
The encrypted authentication token containing the caller's AWS IAM Identity Center identity information. This token is encrypted using AWS Key Management Service and can only be decrypted by the specified Amazon Redshift clusters. Use this token with Amazon Redshift drivers to authenticate using your AWS IAM Identity Center identity.  
Type: String

## Errors
<a name="API_GetIdentityCenterAuthToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterNotFound **   
The `ClusterIdentifier` parameter does not refer to an existing cluster.   
HTTP Status Code: 404

 ** InvalidClusterState **   
The specified cluster is not in the `available` state.   
HTTP Status Code: 400

 ** RedshiftInvalidParameter **   
The request contains one or more invalid parameters. This error occurs when required parameters are missing, parameter values are outside acceptable ranges, or parameter formats are incorrect.  
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation isn't supported.  
HTTP Status Code: 400

## Examples
<a name="API_GetIdentityCenterAuthToken_Examples"></a>

### Example
<a name="API_GetIdentityCenterAuthToken_Example_1"></a>

This example illustrates one usage of GetIdentityCenterAuthToken.

#### Sample Request
<a name="API_GetIdentityCenterAuthToken_Example_1_Request"></a>

```
https://redshift.us-east-1.amazonaws.com/
   ?Action=GetIdentityCenterAuthToken
&ClusterIds.member.1=my-cluster-1
&ClusterIds.member.2=my-cluster-2
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20241001/us-east-1/redshift/aws4_request
&X-Amz-Date=20241001T120000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=example1234567890abcdef1234567890abcdef1234567890abcdef
```

#### Sample Response
<a name="API_GetIdentityCenterAuthToken_Example_1_Response"></a>

```
<GetIdentityCenterAuthTokenResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <GetIdentityCenterAuthTokenResult>
    <Token>AQICAHhQvN9+2l...encrypted_token_content...==</Token>
    <ExpirationTime>2024-10-01T13:00:00.000Z</ExpirationTime>
  </GetIdentityCenterAuthTokenResult>
  <ResponseMetadata>
    <RequestId>12345678-1234-1234-1234-123456789012</RequestId>
  </ResponseMetadata>
</GetIdentityCenterAuthTokenResponse>
```

## See Also
<a name="API_GetIdentityCenterAuthToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/GetIdentityCenterAuthToken) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/GetIdentityCenterAuthToken) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/GetIdentityCenterAuthToken) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/GetIdentityCenterAuthToken) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/GetIdentityCenterAuthToken) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/GetIdentityCenterAuthToken) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/GetIdentityCenterAuthToken) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/GetIdentityCenterAuthToken) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/GetIdentityCenterAuthToken) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/GetIdentityCenterAuthToken) 