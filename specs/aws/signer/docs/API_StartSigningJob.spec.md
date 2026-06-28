---
id: "@specs/aws/signer/docs/API_StartSigningJob"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS StartSigningJob"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# StartSigningJob

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_StartSigningJob
> **target_lang:** meta — documentation tier. ALL sections preserved.



# StartSigningJob
<a name="API_StartSigningJob"></a>

Initiates a signing job to be performed on the code provided. Signing jobs are viewable by the `ListSigningJobs` operation for two years after they are performed. Note the following requirements: 
+  You must create an Amazon S3 source bucket. For more information, see [Creating a Bucket](http://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) in the *Amazon S3 Getting Started Guide*. 
+ Your S3 source bucket must be version enabled.
+ You must create an S3 destination bucket. AWS Signer uses your S3 destination bucket to write your signed code.
+ You specify the name of the source and destination buckets when calling the `StartSigningJob` operation.
+ You must ensure the S3 buckets are from the same Region as the signing profile. Cross-Region signing isn't supported.
+ You must also specify a request token that identifies your request to Signer.

You can call the [DescribeSigningJob](API_DescribeSigningJob.md) and the [ListSigningJobs](API_ListSigningJobs.md) actions after you call `StartSigningJob`.

For a Java example that shows how to use this action, see [StartSigningJob](https://docs.aws.amazon.com/signer/latest/developerguide/api-startsigningjob.html).

## Request Syntax
<a name="API_StartSigningJob_RequestSyntax"></a>

```
POST /signing-jobs HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "destination": { 
      "s3": { 
         "bucketName": "{{string}}",
         "prefix": "{{string}}"
      }
   },
   "profileName": "{{string}}",
   "profileOwner": "{{string}}",
   "source": { 
      "s3": { 
         "bucketName": "{{string}}",
         "key": "{{string}}",
         "version": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_StartSigningJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartSigningJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_StartSigningJob_RequestSyntax) **   <a name="signer-StartSigningJob-request-clientRequestToken"></a>
String that identifies the signing request. All calls after the first that use this token return the same response as the first call.  
Type: String  
Required: Yes

 ** [destination](#API_StartSigningJob_RequestSyntax) **   <a name="signer-StartSigningJob-request-destination"></a>
The S3 bucket in which to save your signed object. The destination contains the name of your bucket and an optional prefix.  
Type: [Destination](API_Destination.md) object  
Required: Yes

 ** [profileName](#API_StartSigningJob_RequestSyntax) **   <a name="signer-StartSigningJob-request-profileName"></a>
The name of the signing profile.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 64.  
Pattern: `^[a-zA-Z0-9_]{2,}`   
Required: Yes

 ** [profileOwner](#API_StartSigningJob_RequestSyntax) **   <a name="signer-StartSigningJob-request-profileOwner"></a>
The AWS account ID of the signing profile owner.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: No

 ** [source](#API_StartSigningJob_RequestSyntax) **   <a name="signer-StartSigningJob-request-source"></a>
The S3 bucket that contains the object to sign or a BLOB that contains your raw code.  
Type: [Source](API_Source.md) object  
Required: Yes

## Response Syntax
<a name="API_StartSigningJob_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobId": "string",
   "jobOwner": "string"
}
```

## Response Elements
<a name="API_StartSigningJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobId](#API_StartSigningJob_ResponseSyntax) **   <a name="signer-StartSigningJob-response-jobId"></a>
The ID of your signing job.  
Type: String

 ** [jobOwner](#API_StartSigningJob_ResponseSyntax) **   <a name="signer-StartSigningJob-response-jobOwner"></a>
The AWS account ID of the signing job owner.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$` 

## Errors
<a name="API_StartSigningJob_Errors"></a>

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

 ** ThrottlingException **   
 *This error has been deprecated.*   
The request was denied due to request throttling.  
Instead of this error, `TooManyRequestsException` should be used.  
HTTP Status Code: 429

 ** TooManyRequestsException **   
The allowed number of job-signing requests has been exceeded.  
This error supersedes the error `ThrottlingException`.  
HTTP Status Code: 429

 ** ValidationException **   
You signing certificate could not be validated.  
HTTP Status Code: 400

## Examples
<a name="API_StartSigningJob_Examples"></a>

### Start a signing job
<a name="API_StartSigningJob_Example_1"></a>

This example illustrates one usage of StartSigningJob.

#### Sample Request
<a name="API_StartSigningJob_Example_1_Request"></a>

```
POST /Prod/signing-jobs HTTP/1.1
Host: signer.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 411
Authorization: AWS4-HMAC-SHA256 Credential=acces_key/20171115/us-east-1/signer/aws4_request, SignedHeaders=host;x-amz-date, Signature=e5a6cf8f72819823373eef632ab310e940aea5abec6c101ab27265b7aaa37aee
X-Amz-Date: 20171115T154708Z
User-Agent: aws-cli/1.11.132 Python/2.7.9 Windows/8 botocore/1.5.95

{
	"source": {
		"s3": {
			"version": "W.OIrIFmjIFeuNXOaBJzPee66.wRg4GR",
			"bucketName": "signer-test-source",
			"key": "my-example-code.java"
		}
	},
	"destination": {
		"s3": {
			"bucketName": "signer-test-dest"
		}
	},
	"platform": "TexasInstruments",
	"signingMaterial": {
		"certificateArn": "arn:aws:acm:region:123456789012:certificate/9ec626ca-0bbb-4be5-83a2-ee563f8386ca"
	},
	"clientRequestToken": "12345"
}
```

#### Sample Response
<a name="API_StartSigningJob_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 48
Date: Wed, 15 Nov 2017 15:47:17 GMT
x-amzn-RequestId: 41bab6aa-ca1c-11e7-84c9-a3126a821e6a
X-Amzn-Trace-Id: sampled=0;root=1-5a0c6184-fcef477f16c548f2ab9a3c29
X-Cache: Miss from cloudfront
Via: 1.1 a44b4468444ef3ee67472bd5c5016098.cloudfront.net (CloudFront)
X-Amz-Cf-Id: JPloXC54wpP2pempPkUcX7S5Qf-5oMmgNE1Uc05KNIlG2igfInFU-g==
Connection: Keep-alive

{"jobId":"ba506303-848d-4fb7-a07f-e8049eb5faa6"}
```

## See Also
<a name="API_StartSigningJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signer-2017-08-25/StartSigningJob) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signer-2017-08-25/StartSigningJob) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/StartSigningJob) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signer-2017-08-25/StartSigningJob) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/StartSigningJob) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signer-2017-08-25/StartSigningJob) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signer-2017-08-25/StartSigningJob) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signer-2017-08-25/StartSigningJob) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signer-2017-08-25/StartSigningJob) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/StartSigningJob) 