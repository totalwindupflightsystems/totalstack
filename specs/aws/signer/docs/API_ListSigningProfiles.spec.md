---
id: "@specs/aws/signer/docs/API_ListSigningProfiles"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListSigningProfiles"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# ListSigningProfiles

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_ListSigningProfiles
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListSigningProfiles
<a name="API_ListSigningProfiles"></a>

Lists all available signing profiles in your AWS account. Returns only profiles with an `ACTIVE` status unless the `includeCanceled` request field is set to `true`. If additional jobs remain to be listed, AWS Signer returns a `nextToken` value. Use this value in subsequent calls to `ListSigningJobs` to fetch the remaining values. You can continue calling `ListSigningJobs` with your `maxResults` parameter and with new values that Signer returns in the `nextToken` parameter until all of your signing jobs have been returned.

## Request Syntax
<a name="API_ListSigningProfiles_RequestSyntax"></a>

```
GET /signing-profiles?includeCanceled={{includeCanceled}}&maxResults={{maxResults}}&nextToken={{nextToken}}&platformId={{platformId}}&statuses={{statuses}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSigningProfiles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [includeCanceled](#API_ListSigningProfiles_RequestSyntax) **   <a name="signer-ListSigningProfiles-request-uri-includeCanceled"></a>
Designates whether to include profiles with the status of `CANCELED`.

 ** [maxResults](#API_ListSigningProfiles_RequestSyntax) **   <a name="signer-ListSigningProfiles-request-uri-maxResults"></a>
The maximum number of profiles to be returned.  
Valid Range: Minimum value of 1. Maximum value of 25.

 ** [nextToken](#API_ListSigningProfiles_RequestSyntax) **   <a name="signer-ListSigningProfiles-request-uri-nextToken"></a>
Value for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of `nextToken` from the response that you just received.

 ** [platformId](#API_ListSigningProfiles_RequestSyntax) **   <a name="signer-ListSigningProfiles-request-uri-platformId"></a>
Filters results to return only signing jobs initiated for a specified signing platform.

 ** [statuses](#API_ListSigningProfiles_RequestSyntax) **   <a name="signer-ListSigningProfiles-request-uri-statuses"></a>
Filters results to return only signing jobs with statuses in the specified list.  
Valid Values: `Active | Canceled | Revoked` 

## Request Body
<a name="API_ListSigningProfiles_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSigningProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "profiles": [ 
      { 
         "arn": "string",
         "platformDisplayName": "string",
         "platformId": "string",
         "profileName": "string",
         "profileVersion": "string",
         "profileVersionArn": "string",
         "signatureValidityPeriod": { 
            "type": "string",
            "value": number
         },
         "signingMaterial": { 
            "certificateArn": "string"
         },
         "signingParameters": { 
            "string" : "string" 
         },
         "status": "string",
         "tags": { 
            "string" : "string" 
         }
      }
   ]
}
```

## Response Elements
<a name="API_ListSigningProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSigningProfiles_ResponseSyntax) **   <a name="signer-ListSigningProfiles-response-nextToken"></a>
Value for specifying the next set of paginated results to return.  
Type: String

 ** [profiles](#API_ListSigningProfiles_ResponseSyntax) **   <a name="signer-ListSigningProfiles-response-profiles"></a>
A list of profiles that are available in the AWS account. This includes profiles with the status of `CANCELED` if the `includeCanceled` parameter is set to `true`.  
Type: Array of [SigningProfile](API_SigningProfile.md) objects

## Errors
<a name="API_ListSigningProfiles_Errors"></a>

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

## See Also
<a name="API_ListSigningProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signer-2017-08-25/ListSigningProfiles) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signer-2017-08-25/ListSigningProfiles) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/ListSigningProfiles) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signer-2017-08-25/ListSigningProfiles) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/ListSigningProfiles) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signer-2017-08-25/ListSigningProfiles) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signer-2017-08-25/ListSigningProfiles) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signer-2017-08-25/ListSigningProfiles) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signer-2017-08-25/ListSigningProfiles) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/ListSigningProfiles) 