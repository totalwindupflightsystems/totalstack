---
id: "@specs/aws/rds/docs/API_DescribeCertificates"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeCertificates"
status: active
depends_on:
  - "@specs/aws/rds/meta"
---

# DescribeCertificates

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rds/docs/API_DescribeCertificates
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeCertificates
<a name="API_DescribeCertificates"></a>

Lists the set of certificate authority (CA) certificates provided by Amazon RDS for this AWS account.

For more information, see [Using SSL/TLS to encrypt a connection to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html) in the *Amazon RDS User Guide* and [ Using SSL/TLS to encrypt a connection to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html) in the *Amazon Aurora User Guide*.

## Request Parameters
<a name="API_DescribeCertificates_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CertificateIdentifier **   
The user-supplied certificate identifier. If this parameter is specified, information for only the identified certificate is returned. This parameter isn't case-sensitive.  
Constraints:  
+ Must match an existing CertificateIdentifier.
Type: String  
Required: No

 **Filters.Filter.N**   
This parameter isn't currently supported.  
Type: Array of [Filter](API_Filter.md) objects  
Required: No

 ** Marker **   
An optional pagination token provided by a previous `DescribeCertificates` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords`.  
Type: String  
Required: No

 ** MaxRecords **   
The maximum number of records to include in the response. If more records exist than the specified `MaxRecords` value, a pagination token called a marker is included in the response so you can retrieve the remaining results.  
Default: 100  
Constraints: Minimum 20, maximum 100.  
Type: Integer  
Required: No

## Response Elements
<a name="API_DescribeCertificates_ResponseElements"></a>

The following elements are returned by the service.

 **Certificates.Certificate.N**   
The list of `Certificate` objects for the AWS account.  
Type: Array of [Certificate](API_Certificate.md) objects

 ** DefaultCertificateForNewLaunches **   
The default root CA for new databases created by your AWS account. This is either the root CA override set on your AWS account or the system default CA for the Region if no override exists. To override the default CA, use the `ModifyCertificates` operation.  
Type: String

 ** Marker **   
An optional pagination token provided by a previous `DescribeCertificates` request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords` .  
Type: String

## Errors
<a name="API_DescribeCertificates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CertificateNotFound **   
 `CertificateIdentifier` doesn't refer to an existing certificate.  
HTTP Status Code: 404

## Examples
<a name="API_DescribeCertificates_Examples"></a>

### Example
<a name="API_DescribeCertificates_Example_1"></a>

This example illustrates one usage of DescribeCertificates.

#### Sample Request
<a name="API_DescribeCertificates_Example_1_Request"></a>

```
https://rds.amazonaws.com/
   ?Action=DescribeCertificates
   &MaxRecords=100
   &SignatureMethod=HmacSHA256
   &SignatureVersion=4
   &Version=2014-10-31
   &X-Amz-Algorithm=AWS4-HMAC-SHA256
   &X-Amz-Credential=AKIADQKE4SARGYLE/20141121/us-west-2/rds/aws4_request
   &X-Amz-Date=20141121T164732Z
   &X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
   &X-Amz-Signature=6e25c542bf96fe24b28c12976ec92d2f856ab1d2a158e21c35441a736e4fde2b
```

#### Sample Response
<a name="API_DescribeCertificates_Example_1_Response"></a>

```
<DescribeCertificatesResponse xmlns="http://rds.amazonaws.com/doc/2014-10-31/">
   <DescribeCertificatesResult>
    <Certificates>
      <Certificate>
        <CertificateIdentifier>rdscacertificate</CertificateIdentifier>
        <CertificateType>ca</CertificateType>
        <ThumbPrint>xxxxxxxxxxxx</ThumbPrint>
        <ValidFrom>2010-05-22T01:12:00.000Z</ValidFrom>
        <ValidTill>2014-05-22T01:12:00.000Z</ValidTill>
      </Certificate>
    </Certificates>
   </DescribeCertificatesResult>
   <ResponseMetadata>
    <RequestId>9135fff3-8509-11e0-bd9b-a7b1ece36d51</RequestId>
   </ResponseMetadata>
  </DescribeCertificatesResponse>
```

## See Also
<a name="API_DescribeCertificates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rds-2014-10-31/DescribeCertificates) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rds-2014-10-31/DescribeCertificates) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DescribeCertificates) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rds-2014-10-31/DescribeCertificates) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DescribeCertificates) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rds-2014-10-31/DescribeCertificates) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rds-2014-10-31/DescribeCertificates) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rds-2014-10-31/DescribeCertificates) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rds-2014-10-31/DescribeCertificates) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DescribeCertificates) 