---
id: "@specs/aws/signer/docs/API_DescribeSigningJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeSigningJob"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# DescribeSigningJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_DescribeSigningJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeSigningJob
<a name="API_DescribeSigningJob"></a>

Returns information about a specific code signing job. You specify the job by using the `jobId` value that is returned by the [StartSigningJob](API_StartSigningJob.md) operation. 

## Request Syntax
<a name="API_DescribeSigningJob_RequestSyntax"></a>

```
GET /signing-jobs/{{jobId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeSigningJob_RequestParameters"></a>

The request uses the following URI parameters.

 ** [jobId](#API_DescribeSigningJob_RequestSyntax) **   <a name="signer-DescribeSigningJob-request-uri-jobId"></a>
The ID of the signing job on input.  
Required: Yes

## Request Body
<a name="API_DescribeSigningJob_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeSigningJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "completedAt": number,
   "createdAt": number,
   "jobId": "string",
   "jobInvoker": "string",
   "jobOwner": "string",
   "overrides": { 
      "signingConfiguration": { 
         "encryptionAlgorithm": "string",
         "hashAlgorithm": "string"
      },
      "signingImageFormat": "string"
   },
   "platformDisplayName": "string",
   "platformId": "string",
   "profileName": "string",
   "profileVersion": "string",
   "requestedBy": "string",
   "revocationRecord": { 
      "reason": "string",
      "revokedAt": number,
      "revokedBy": "string"
   },
   "signatureExpiresAt": number,
   "signedObject": { 
      "s3": { 
         "bucketName": "string",
         "key": "string"
      }
   },
   "signingMaterial": { 
      "certificateArn": "string"
   },
   "signingParameters": { 
      "string" : "string" 
   },
   "source": { 
      "s3": { 
         "bucketName": "string",
         "key": "string",
         "version": "string"
      }
   },
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_DescribeSigningJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [completedAt](#API_DescribeSigningJob_ResponseSyntax) **   <a name="signer-DescribeSigningJob-response-completedAt"></a>
Date and time that the signing job was completed.  
Type: Timestamp

 ** [createdAt](#API_DescribeSigningJob_ResponseSyntax) **   <a name="signer-DescribeSigningJob-response-createdAt"></a>
Date and time that the signing job was created.  
Type: Timestamp

 ** [jobId](#API_DescribeSigningJob_ResponseSyntax) **   <a name="signer-DescribeSigningJob-response-jobId"></a>
The ID of the signing job on output.  
Type: String

 ** [jobInvoker](#API_DescribeSigningJob_ResponseSyntax) **   <a name="signer-DescribeSigningJob-response-jobInvoker"></a>
The IAM entity that initiated the signing job.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$` 

 ** [jobOwner](#API_DescribeSigningJob_ResponseSyntax) **   <a name="signer-DescribeSigningJob-response-jobOwner"></a>
The AWS account ID of the job owner.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$` 

 ** [overrides](#API_DescribeSigningJob_ResponseSyntax) **   <a name="signer-DescribeSigningJob-response-overrides"></a>
A list of any overrides that were applied to the signing operation.  
Type: [SigningPlatformOverrides](API_SigningPlatformOverrides.md) object

 ** [platformDisplayName](#API_DescribeSigningJob_ResponseSyntax) **   <a name="signer-DescribeSigningJob-response-platformDisplayName"></a>
A human-readable name for the signing platform associated with the signing job.  
Type: String

 ** [platformId](#API_DescribeSigningJob_ResponseSyntax) **   <a name="signer-DescribeSigningJob-response-platformId"></a>
The microcontroller platform to which your signed code image will be distributed.  
Type: String

 ** [profileName](#API_DescribeSigningJob_ResponseSyntax) **   <a name="signer-DescribeSigningJob-response-profileName"></a>
The name of the profile that initiated the signing operation.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 64.  
Pattern: `^[a-zA-Z0-9_]{2,}` 

 ** [profileVersion](#API_DescribeSigningJob_ResponseSyntax) **   <a name="signer-DescribeSigningJob-response-profileVersion"></a>
The version of the signing profile used to initiate the signing job.  
Type: String  
Length Constraints: Fixed length of 10.  
Pattern: `^[a-zA-Z0-9]{10}$` 

 ** [requestedBy](#API_DescribeSigningJob_ResponseSyntax) **   <a name="signer-DescribeSigningJob-response-requestedBy"></a>
The IAM principal that requested the signing job.  
Type: String

 ** [revocationRecord](#API_DescribeSigningJob_ResponseSyntax) **   <a name="signer-DescribeSigningJob-response-revocationRecord"></a>
A revocation record if the signature generated by the signing job has been revoked. Contains a timestamp and the ID of the IAM entity that revoked the signature.  
Type: [SigningJobRevocationRecord](API_SigningJobRevocationRecord.md) object

 ** [signatureExpiresAt](#API_DescribeSigningJob_ResponseSyntax) **   <a name="signer-DescribeSigningJob-response-signatureExpiresAt"></a>
Thr expiration timestamp for the signature generated by the signing job.  
Type: Timestamp

 ** [signedObject](#API_DescribeSigningJob_ResponseSyntax) **   <a name="signer-DescribeSigningJob-response-signedObject"></a>
Name of the S3 bucket where the signed code image is saved by AWS Signer.  
Type: [SignedObject](API_SignedObject.md) object

 ** [signingMaterial](#API_DescribeSigningJob_ResponseSyntax) **   <a name="signer-DescribeSigningJob-response-signingMaterial"></a>
The Amazon Resource Name (ARN) of your code signing certificate.  
Type: [SigningMaterial](API_SigningMaterial.md) object

 ** [signingParameters](#API_DescribeSigningJob_ResponseSyntax) **   <a name="signer-DescribeSigningJob-response-signingParameters"></a>
Map of user-assigned key-value pairs used during signing. These values contain any information that you specified for use in your signing job.   
Type: String to string map

 ** [source](#API_DescribeSigningJob_ResponseSyntax) **   <a name="signer-DescribeSigningJob-response-source"></a>
The object that contains the name of your S3 bucket or your raw code.  
Type: [Source](API_Source.md) object

 ** [status](#API_DescribeSigningJob_ResponseSyntax) **   <a name="signer-DescribeSigningJob-response-status"></a>
Status of the signing job.  
Type: String  
Valid Values: `InProgress | Failed | Succeeded` 

 ** [statusReason](#API_DescribeSigningJob_ResponseSyntax) **   <a name="signer-DescribeSigningJob-response-statusReason"></a>
String value that contains the status reason.  
Type: String

## Errors
<a name="API_DescribeSigningJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 403

 ** InternalServiceErrorException **   
An internal error occurred.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
A specified resource could not be found.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
The allowed number of job-signing requests has been exceeded.  
This error supersedes the error `ThrottlingException`.  
HTTP Status Code: 429

## Examples
<a name="API_DescribeSigningJob_Examples"></a>

### Describe a signing job
<a name="API_DescribeSigningJob_Example_1"></a>

This example illustrates one usage of DescribeSigningJob.

#### Sample Request
<a name="API_DescribeSigningJob_Example_1_Request"></a>

```
GET /Prod/signing-jobs/9052caa6-1d8d-43b5-9ead-0cb8621c8c74 HTTP/1.1
Host: signer.us-east-1.amazonaws.com
Accept-Encoding: identity
Authorization: AWS4-HMAC-SHA256 Credential=access_key/us-east-1/signer/aws4_request, SignedHeaders=host;x-amz-date, Signature=93e24ab743082913abfb466a13b2f65a7f3eec9893aa2dcbdc91d160b3d7ff67
X-Amz-Date: 20171115T165923Z
User-Agent: aws-cli/1.11.132 Python/2.7.9 Windows/8 botocore/1.5.95
```

#### Sample Response
<a name="API_DescribeSigningJob_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 631
Date: Wed, 15 Nov 2017 16:59:31 GMT
x-amzn-RequestId: 5946a79a-ca26-11e7-ae27-cda958f39b26
X-Amzn-Trace-Id: sampled=0;root=1-5a0c7273-fd33420b90425c1dc4b94bcc
X-Cache: Miss from cloudfront
Via: 1.1 ce270f4a88edde7438864bc44406e83a.cloudfront.net (CloudFront)
X-Amz-Cf-Id: hAkstXf07ycoa3HgI2MebhYgvyZ39K7zn2Z9mpqxsRlPjPphgaHZUQ==
Connection: Keep-alive

{
	"jobId": "9052caa6-1d8d-43b5-9ead-0cb8621c8c74",
	"source": {
		"s3": {
			"bucketName": "signer-test-source",
			"key": "my-example-code.java",
			"version": "W.OIrIFmjIFeuNXOaBJzPee66.wRg4GR"
		}
	},
	"signingMaterial": {
		"certificateArn": "arn:aws:acm:region:123456789012:certificate/9ec626ca-0bbb-4be5-83a2-ee563f8386ca"
	},
	"platform": "TexasInstruments",
	"signingParameters": null,
	"createdAt": 1510695622,
	"completedAt": 1510695623,
	"requestedBy": "arn:aws:iam::123456789012:root",
	"status": "Succeeded",
	"statusReason": "Signing success",
	"signedObject": {
		"s3": {
			"bucketName": "signer-test-dest",
			"key": "9052caa6-1d8d-43b5-9ead-0cb8621c8c74"
		}
	}
}
```

## See Also
<a name="API_DescribeSigningJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signer-2017-08-25/DescribeSigningJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signer-2017-08-25/DescribeSigningJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/DescribeSigningJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signer-2017-08-25/DescribeSigningJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/DescribeSigningJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signer-2017-08-25/DescribeSigningJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signer-2017-08-25/DescribeSigningJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signer-2017-08-25/DescribeSigningJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signer-2017-08-25/DescribeSigningJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/DescribeSigningJob) 