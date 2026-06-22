---
id: "@specs/aws/redshift/docs/API_DeleteHsmClientCertificate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteHsmClientCertificate"
status: active
depends_on:
  - "@specs/aws/redshift/meta"
---

# DeleteHsmClientCertificate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/redshift/docs/API_DeleteHsmClientCertificate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteHsmClientCertificate
<a name="API_DeleteHsmClientCertificate"></a>

Deletes the specified HSM client certificate.

## Request Parameters
<a name="API_DeleteHsmClientCertificate_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** HsmClientCertificateIdentifier **   
The identifier of the HSM client certificate to be deleted.  
Type: String  
Length Constraints: Maximum length of 2147483647.  
Required: Yes

## Errors
<a name="API_DeleteHsmClientCertificate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** HsmClientCertificateNotFoundFault **   
There is no Amazon Redshift HSM client certificate with the specified identifier.  
HTTP Status Code: 400

 ** InvalidHsmClientCertificateStateFault **   
The specified HSM client certificate is not in the `available` state, or it is still in use by one or more Amazon Redshift clusters.  
HTTP Status Code: 400

## Examples
<a name="API_DeleteHsmClientCertificate_Examples"></a>

### Example
<a name="API_DeleteHsmClientCertificate_Example_1"></a>

This example illustrates one usage of DeleteHsmClientCertificate.

#### Sample Request
<a name="API_DeleteHsmClientCertificate_Example_1_Request"></a>

```
https://redshift.us-east-2.amazonaws.com/
       ?Action=DeleteHsmClientCertificate
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
<a name="API_DeleteHsmClientCertificate_Example_1_Response"></a>

```
<DeleteHsmClientCertificateResponse xmlns="http://redshift.amazonaws.com/doc/2012-12-01/">
  <ResponseMetadata>
    <RequestId>ff0388ec-2839-11ea-b6af-7126da6f11af</RequestId>
  </ResponseMetadata>
</DeleteHsmClientCertificateResponse>
```

## See Also
<a name="API_DeleteHsmClientCertificate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-2012-12-01/DeleteHsmClientCertificate) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-2012-12-01/DeleteHsmClientCertificate) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/DeleteHsmClientCertificate) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-2012-12-01/DeleteHsmClientCertificate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/DeleteHsmClientCertificate) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-2012-12-01/DeleteHsmClientCertificate) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-2012-12-01/DeleteHsmClientCertificate) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-2012-12-01/DeleteHsmClientCertificate) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-2012-12-01/DeleteHsmClientCertificate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/DeleteHsmClientCertificate) 