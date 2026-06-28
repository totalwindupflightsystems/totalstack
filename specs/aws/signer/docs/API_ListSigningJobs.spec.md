---
id: "@specs/aws/signer/docs/API_ListSigningJobs"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListSigningJobs"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# ListSigningJobs

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_ListSigningJobs
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListSigningJobs
<a name="API_ListSigningJobs"></a>

Lists all your signing jobs. You can use the `maxResults` parameter to limit the number of signing jobs that are returned in the response. If additional jobs remain to be listed, AWS Signer returns a `nextToken` value. Use this value in subsequent calls to `ListSigningJobs` to fetch the remaining values. You can continue calling `ListSigningJobs` with your `maxResults` parameter and with new values that Signer returns in the `nextToken` parameter until all of your signing jobs have been returned. 

## Request Syntax
<a name="API_ListSigningJobs_RequestSyntax"></a>

```
GET /signing-jobs?isRevoked={{isRevoked}}&jobInvoker={{jobInvoker}}&maxResults={{maxResults}}&nextToken={{nextToken}}&platformId={{platformId}}&requestedBy={{requestedBy}}&signatureExpiresAfter={{signatureExpiresAfter}}&signatureExpiresBefore={{signatureExpiresBefore}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSigningJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [isRevoked](#API_ListSigningJobs_RequestSyntax) **   <a name="signer-ListSigningJobs-request-uri-isRevoked"></a>
Filters results to return only signing jobs with revoked signatures.

 ** [jobInvoker](#API_ListSigningJobs_RequestSyntax) **   <a name="signer-ListSigningJobs-request-uri-jobInvoker"></a>
Filters results to return only signing jobs initiated by a specified IAM entity.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$` 

 ** [maxResults](#API_ListSigningJobs_RequestSyntax) **   <a name="signer-ListSigningJobs-request-uri-maxResults"></a>
Specifies the maximum number of items to return in the response. Use this parameter when paginating results. If additional items exist beyond the number you specify, the `nextToken` element is set in the response. Use the `nextToken` value in a subsequent request to retrieve additional items.   
Valid Range: Minimum value of 1. Maximum value of 25.

 ** [nextToken](#API_ListSigningJobs_RequestSyntax) **   <a name="signer-ListSigningJobs-request-uri-nextToken"></a>
String for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of `nextToken` from the response that you just received.

 ** [platformId](#API_ListSigningJobs_RequestSyntax) **   <a name="signer-ListSigningJobs-request-uri-platformId"></a>
The ID of microcontroller platform that you specified for the distribution of your code image.

 ** [requestedBy](#API_ListSigningJobs_RequestSyntax) **   <a name="signer-ListSigningJobs-request-uri-requestedBy"></a>
The IAM principal that requested the signing job.

 ** [signatureExpiresAfter](#API_ListSigningJobs_RequestSyntax) **   <a name="signer-ListSigningJobs-request-uri-signatureExpiresAfter"></a>
Filters results to return only signing jobs with signatures expiring after a specified timestamp.

 ** [signatureExpiresBefore](#API_ListSigningJobs_RequestSyntax) **   <a name="signer-ListSigningJobs-request-uri-signatureExpiresBefore"></a>
Filters results to return only signing jobs with signatures expiring before a specified timestamp.

 ** [status](#API_ListSigningJobs_RequestSyntax) **   <a name="signer-ListSigningJobs-request-uri-status"></a>
A status value with which to filter your results.  
Valid Values: `InProgress | Failed | Succeeded` 

## Request Body
<a name="API_ListSigningJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSigningJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "jobs": [ 
      { 
         "createdAt": number,
         "isRevoked": boolean,
         "jobId": "string",
         "jobInvoker": "string",
         "jobOwner": "string",
         "platformDisplayName": "string",
         "platformId": "string",
         "profileName": "string",
         "profileVersion": "string",
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
         "source": { 
            "s3": { 
               "bucketName": "string",
               "key": "string",
               "version": "string"
            }
         },
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListSigningJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [jobs](#API_ListSigningJobs_ResponseSyntax) **   <a name="signer-ListSigningJobs-response-jobs"></a>
A list of your signing jobs.  
Type: Array of [SigningJob](API_SigningJob.md) objects

 ** [nextToken](#API_ListSigningJobs_ResponseSyntax) **   <a name="signer-ListSigningJobs-response-nextToken"></a>
String for specifying the next set of paginated results.  
Type: String

## Errors
<a name="API_ListSigningJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 403

 ** InternalServiceErrorException **   
An internal error occurred.  
HTTP Status Code: 500

 ** TooManyRequestsException **   
The allowed number of job-signing requests has been exceeded.  
This error supersedes the error `ThrottlingException`.  
HTTP Status Code: 429

 ** ValidationException **   
You signing certificate could not be validated.  
HTTP Status Code: 400

## Examples
<a name="API_ListSigningJobs_Examples"></a>

### Example
<a name="API_ListSigningJobs_Example_1"></a>

This example illustrates one usage of ListSigningJobs.

#### Sample Request
<a name="API_ListSigningJobs_Example_1_Request"></a>

```
GET /Prod/signing-jobs?status=InProgress&platform=TexasInstruments&maxResults=10 HTTP/1.1
Host: qvvi640b53.execute-api.us-east-1.amazonaws.com
Accept-Encoding: identity
Authorization: AWS4-HMAC-SHA256 Credential=access_key/20171115/us-east-1/signer/aws4_request, SignedHeaders=host;x-amz-date, Signature=59e5f7ac6c2193c1eb163b0a8f3b2b3ec47fc5687631aa4d42bdcfacc14d626a
X-Amz-Date: 20171115T173358Z
User-Agent: aws-cli/1.11.132 Python/2.7.9 Windows/8 botocore/1.5.95
```

#### Sample Response
<a name="API_ListSigningJobs_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 1896
Date: Wed, 15 Nov 2017 17:34:06 GMT
x-amzn-RequestId: 2e5eaaf7-ca2b-11e7-bfa0-e7cd77b24597
X-Amzn-Trace-Id: sampled=0;root=1-5a0c7a8e-66a88aa1083a4631ce1a9e45
X-Cache: Miss from cloudfront
Via: 1.1 9ba06853e586727720bf0a1bf763bad7.cloudfront.net (CloudFront)
X-Amz-Cf-Id: BtaBXTGIVWfSRurtkK7aMOcg39oiA1Uz3UCoPPQm5LWu5bt72gV_cA==
Connection: Keep-alive

{
	"jobs": [{
		"jobId": "ade0f15c-5857-4fcd-b731-43530bbd2d7d",
		"source": {
			"s3": {
				"bucketName": "signer-test-source",
				"key": "my-example-code.java",
				"version": null
			}
		},
		"signedObject": {
			"s3": {
				"bucketName": "signer-test-dest",
				"key": "signed_images/ade0f15c-5857-4fcd-b731-43530bbd2d7d"
			}
		},
		"signingMaterial": {
			"certificateArn": "arn:aws:acm:region:123456789012:certificate/7a0ed941-64dd-419b-8b59-24378756fee3"
		},
		"createdAt": 1508345543,
		"status": "Succeeded"
	},
	{
		"jobId": "9052caa6-1d8d-43b5-9ead-0cb8621c8c74",
		"source": {
			"s3": {
				"bucketName": "signer-test-source",
				"key": "my-example-code.java",
				"version": "W.OIrIFmjIFeuNXOaBJzPee66.wRg4GR"
			}
		},
		"signedObject": {
			"s3": {
				"bucketName": "signer-test-dest",
				"key": "9052caa6-1d8d-43b5-9ead-0cb8621c8c74"
			}
		},
		"signingMaterial": {
			"certificateArn": "arn:aws:acm:region:123456789012:certificate/9ec626ca-0bbb-4be5-83a2-ee563f8386ca"
		},
		"createdAt": 1510695622,
		"status": "Succeeded"
	},
	{
		"jobId": "cc9067a9-9258-489a-abae-1c3408191071",
		"source": {
			"s3": {
				"bucketName": "signer-test-source",
				"key": "my-example-code.java",
				"version": "W.OIrIFmjIFeuNXOaBJzPee66.wRg4GR"
			}
		},
		"signedObject": {
			"s3": {
				"bucketName": "signer-test-dest",
				"key": "cc9067a9-9258-489a-abae-1c3408191071"
			}
		},
		"signingMaterial": {
			"certificateArn": "arn:aws:acm:region:123456789012:certificate/9ec626ca-0bbb-4be5-83a2-ee563f8386ca"
		},
		"createdAt": 1510698374,
		"status": "Succeeded"
	},
	{
		"jobId": "ba506303-848d-4fb7-a07f-e8049eb5faa6",
		"source": {
			"s3": {
				"bucketName": "signer-test-source",
				"key": "my-example-code.java",
				"version": "W.OIrIFmjIFeuNXOaBJzPee66.wRg4GR"
			}
		},
		"signedObject": {
			"s3": {
				"bucketName": "signer-test-dest",
				"key": "ba506303-848d-4fb7-a07f-e8049eb5faa6"
			}
		},
		"signingMaterial": {
			"certificateArn": "arn:aws:acm:region:123456789012:certificate/9ec626ca-0bbb-4be5-83a2-ee563f8386ca"
		},
		"createdAt": 1510760837,
		"status": "Succeeded"
	}],
	"nextToken": null
}
```

## See Also
<a name="API_ListSigningJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signer-2017-08-25/ListSigningJobs) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signer-2017-08-25/ListSigningJobs) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/ListSigningJobs) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signer-2017-08-25/ListSigningJobs) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/ListSigningJobs) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signer-2017-08-25/ListSigningJobs) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signer-2017-08-25/ListSigningJobs) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signer-2017-08-25/ListSigningJobs) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signer-2017-08-25/ListSigningJobs) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/ListSigningJobs) 