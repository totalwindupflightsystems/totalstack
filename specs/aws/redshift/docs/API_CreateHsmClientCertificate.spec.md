---
id: "@specs/aws/redshift/docs/API_CreateHsmClientCertificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateHsmClientCertificate"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# CreateHsmClientCertificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_CreateHsmClientCertificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateHsmClientCertificate
<a name="API_CreateHsmClientCertificate"></a>

Creates an HSM client certificate that an Amazon Redshift cluster will use to connect to the client's HSM in order to store and retrieve the keys used to encrypt the cluster databases.

The command returns a public key, which you must store in the HSM. In addition to creating the HSM certificate, you must create an Amazon Redshift HSM configuration that provides a cluster the information needed to store and use encryption keys in the HSM. For more information, go to [Hardware Security Modules](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html#working-with-HSM) in the *Amazon Redshift Cluster Management Guide*.

## Request Parameters
<a name="API_CreateHsmClientCertificate_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** HsmClientCertificateIdentifier **   
The identifier to be assigned to the new HSM client certificate that the cluster will use to connect to the HSM to use the database encryption keys.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

 **Tags.Tag.N**   
A list of tag instances.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

## Response Elements
<a name="API_CreateHsmClientCertificate_ResponseElements"></a>

The following element is returned by the service.

 ** HsmClientCertificate **   
Returns information about an HSM client certificate. The certificate is stored in a secure Hardware Storage Module (HSM), and used by the Amazon Redshift cluster to encrypt data files.  
Type: [HsmClientCertificate](API_HsmClientCertificate.md) object

## Errors
<a name="API_CreateHsmClientCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** HsmClientCertificateAlreadyExistsFault **   
There is already an existing Amazon Redshift HSM client certificate with the specified identifier.  
HTTP Status Code: 400

 ** HsmClientCertificateQuotaExceededFault **   
The quota for HSM client certificates has been reached. For information about increasing your quota, go to [Limits in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html) in the *Amazon Redshift Cluster Management Guide*.   
HTTP Status Code: 400

 ** InvalidTagFault **   
The tag is invalid.  
HTTP Status Code: 400

 ** TagLimitExceededFault **   
You have exceeded the number of tags allowed.  
HTTP Status Code: 400

## Examples
<a name="API_CreateHsmClientCertificate_Examples"></a>

### Example
<a name="API_CreateHsmClientCertificate_Example_1"></a>

This example illustrates one usage of CreateHsmClientCertificate.

#### Sample Request
<a name="API_CreateHsmClientCertificate_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=CreateHsmClientCertificate
&HsmClientCertificateIdentifier=myhsmclientcert
&SignatureMethod=HmacSHA256&SignatureVersion=4
&Version=2012-12-01
&X-Amz-Algorithm=AWS4-HMAC-SHA256
&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE/20190817/us-east-2/redshift/aws4_request
&X-Amz-Date=20190825T160000Z
&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
&X-Amz-Signature=0aa1234bb5cc678ddddd901ee2ff3aa45678b90c12d345e6ff789012345a6b7b
```

#### Sample Response
<a name="API_CreateHsmClientCertificate_Example_1_Response"></a>

```
<CreateHsmClientCertificateResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <CreateHsmClientCertificateResult>
    <HsmClientCertificate>
      <HsmClientCertificateIdentifier>myhsmclientcert</HsmClientCertificateIdentifier>
      <HsmClientCertificatePublicKey>-----BEGIN CERTIFICATE-----
MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC
VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6
b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd
BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN
MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD
VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z
b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt
YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ
21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T
rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE
Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4
nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb
FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb
NYiytVbZPQUQ5Yaxu2jXnimvw3rEXAMPLE=
-----END CERTIFICATE-----
</HsmClientCertificatePublicKey>
      <Tags/>
    </HsmClientCertificate>
  </CreateHsmClientCertificateResult>
  <ResponseMetadata>
    <RequestId>917e54c0-2833-11ea-9caa-c956bec1ce87</RequestId>
  </ResponseMetadata>
</CreateHsmClientCertificateResponse>
```

## See Also
<a name="API_CreateHsmClientCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/CreateHsmClientCertificate) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/CreateHsmClientCertificate) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/CreateHsmClientCertificate) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/CreateHsmClientCertificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/CreateHsmClientCertificate) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/CreateHsmClientCertificate) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/CreateHsmClientCertificate) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/CreateHsmClientCertificate) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/CreateHsmClientCertificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/CreateHsmClientCertificate) 