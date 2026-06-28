---
id: "@specs/aws/signer/docs/API_ListSigningPlatforms"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListSigningPlatforms"
status: active
depends_on:
  - "@specs/aws/signer/meta"
---

# ListSigningPlatforms

> **source:** AWS Documentation
> **spec:id:** @specs/aws/signer/docs/API_ListSigningPlatforms
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListSigningPlatforms
<a name="API_ListSigningPlatforms"></a>

Lists all signing platforms available in AWS Signer that match the request parameters. If additional jobs remain to be listed, Signer returns a `nextToken` value. Use this value in subsequent calls to `ListSigningJobs` to fetch the remaining values. You can continue calling `ListSigningJobs` with your `maxResults` parameter and with new values that Signer returns in the `nextToken` parameter until all of your signing jobs have been returned.

## Request Syntax
<a name="API_ListSigningPlatforms_RequestSyntax"></a>

```
GET /signing-platforms?category={{category}}&maxResults={{maxResults}}&nextToken={{nextToken}}&partner={{partner}}&target={{target}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSigningPlatforms_RequestParameters"></a>

The request uses the following URI parameters.

 ** [category](#API_ListSigningPlatforms_RequestSyntax) **   <a name="signer-ListSigningPlatforms-request-uri-category"></a>
The category type of a signing platform.

 ** [maxResults](#API_ListSigningPlatforms_RequestSyntax) **   <a name="signer-ListSigningPlatforms-request-uri-maxResults"></a>
The maximum number of results to be returned by this operation.  
Valid Range: Minimum value of 1. Maximum value of 25.

 ** [nextToken](#API_ListSigningPlatforms_RequestSyntax) **   <a name="signer-ListSigningPlatforms-request-uri-nextToken"></a>
Value for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of `nextToken` from the response that you just received.

 ** [partner](#API_ListSigningPlatforms_RequestSyntax) **   <a name="signer-ListSigningPlatforms-request-uri-partner"></a>
Any partner entities connected to a signing platform.

 ** [target](#API_ListSigningPlatforms_RequestSyntax) **   <a name="signer-ListSigningPlatforms-request-uri-target"></a>
The validation template that is used by the target signing platform.

## Request Body
<a name="API_ListSigningPlatforms_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSigningPlatforms_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "platforms": [ 
      { 
         "category": "string",
         "displayName": "string",
         "maxSizeInMB": number,
         "partner": "string",
         "platformId": "string",
         "revocationSupported": boolean,
         "signingConfiguration": { 
            "encryptionAlgorithmOptions": { 
               "allowedValues": [ "string" ],
               "defaultValue": "string"
            },
            "hashAlgorithmOptions": { 
               "allowedValues": [ "string" ],
               "defaultValue": "string"
            }
         },
         "signingImageFormat": { 
            "defaultFormat": "string",
            "supportedFormats": [ "string" ]
         },
         "target": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSigningPlatforms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSigningPlatforms_ResponseSyntax) **   <a name="signer-ListSigningPlatforms-response-nextToken"></a>
Value for specifying the next set of paginated results to return.  
Type: String

 ** [platforms](#API_ListSigningPlatforms_ResponseSyntax) **   <a name="signer-ListSigningPlatforms-response-platforms"></a>
A list of all platforms that match the request parameters.  
Type: Array of [SigningPlatform](API_SigningPlatform.md) objects

## Errors
<a name="API_ListSigningPlatforms_Errors"></a>

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

## See Also
<a name="API_ListSigningPlatforms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signer-2017-08-25/ListSigningPlatforms) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signer-2017-08-25/ListSigningPlatforms) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/ListSigningPlatforms) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signer-2017-08-25/ListSigningPlatforms) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/ListSigningPlatforms) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signer-2017-08-25/ListSigningPlatforms) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signer-2017-08-25/ListSigningPlatforms) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signer-2017-08-25/ListSigningPlatforms) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/signer-2017-08-25/ListSigningPlatforms) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/ListSigningPlatforms) 