---
id: "@specs/aws/cognito-identity/docs/API_ListIdentities"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListIdentities"
status: active
depends_on:
  - "@specs/aws/cognito-identity/meta"
---

# ListIdentities

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cognito-identity/docs/API_ListIdentities
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListIdentities
<a name="API_ListIdentities"></a>

Lists the identities in an identity pool.

**Note**  
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.  
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) 

## Request Syntax
<a name="API_ListIdentities_RequestSyntax"></a>

```
{
   "HideDisabled": {{boolean}},
   "IdentityPoolId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListIdentities_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HideDisabled](#API_ListIdentities_RequestSyntax) **   <a name="CognitoIdentity-ListIdentities-request-HideDisabled"></a>
An optional boolean parameter that allows you to hide disabled identities. If omitted, the ListIdentities API will include disabled identities in the response.  
Type: Boolean  
Required: No

 ** [IdentityPoolId](#API_ListIdentities_RequestSyntax) **   <a name="CognitoIdentity-ListIdentities-request-IdentityPoolId"></a>
An identity pool ID in the format REGION:GUID.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 55.  
Pattern: `[\w-]+:[0-9a-f-]+`   
Required: Yes

 ** [MaxResults](#API_ListIdentities_RequestSyntax) **   <a name="CognitoIdentity-ListIdentities-request-MaxResults"></a>
The maximum number of identities to return.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 60.  
Required: Yes

 ** [NextToken](#API_ListIdentities_RequestSyntax) **   <a name="CognitoIdentity-ListIdentities-request-NextToken"></a>
A pagination token.  
Type: String  
Length Constraints: Minimum length of 1.  
Pattern: `[\S]+`   
Required: No

## Response Syntax
<a name="API_ListIdentities_ResponseSyntax"></a>

```
{
   "Identities": [ 
      { 
         "CreationDate": number,
         "IdentityId": "string",
         "LastModifiedDate": number,
         "Logins": [ "string" ]
      }
   ],
   "IdentityPoolId": "string",
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListIdentities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Identities](#API_ListIdentities_ResponseSyntax) **   <a name="CognitoIdentity-ListIdentities-response-Identities"></a>
An object containing a set of identities and associated mappings.  
Type: Array of [IdentityDescription](API_IdentityDescription.md) objects

 ** [IdentityPoolId](#API_ListIdentities_ResponseSyntax) **   <a name="CognitoIdentity-ListIdentities-response-IdentityPoolId"></a>
An identity pool ID in the format REGION:GUID.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 55.  
Pattern: `[\w-]+:[0-9a-f-]+` 

 ** [NextToken](#API_ListIdentities_ResponseSyntax) **   <a name="CognitoIdentity-ListIdentities-response-NextToken"></a>
A pagination token.  
Type: String  
Length Constraints: Minimum length of 1.  
Pattern: `[\S]+` 

## Errors
<a name="API_ListIdentities_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **   
Thrown when the service encounters an error during processing the request.    
 ** message **   
The message returned by an InternalErrorException.
HTTP Status Code: 500

 ** InvalidParameterException **   
Thrown for missing or bad input parameter(s).    
 ** message **   
The message returned by an InvalidParameterException.
HTTP Status Code: 400

 ** NotAuthorizedException **   
Thrown when a user is not authorized to access the requested resource.    
 ** message **   
The message returned by a NotAuthorizedException
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Thrown when the requested resource (for example, a dataset or record) does not exist.    
 ** message **   
The message returned by a ResourceNotFoundException.
HTTP Status Code: 400

 ** TooManyRequestsException **   
Thrown when a request is throttled.    
 ** message **   
Message returned by a TooManyRequestsException
HTTP Status Code: 400

## Examples
<a name="API_ListIdentities_Examples"></a>

### ListIdentities
<a name="API_ListIdentities_Example_1"></a>

The following examples show a request and a response for the `ListIdentities` action. The request and response bodies have been formatted for readability and may not match the `content-length` value.

#### Sample Request
<a name="API_ListIdentities_Example_1_Request"></a>

```
POST / HTTP/1.1
CONTENT-TYPE: application/json
CONTENT-LENGTH: 234
X-AMZ-TARGET: com.amazonaws.cognito.identity.model.AWSCognitoIdentityService.ListIdentities
HOST: <endpoint>
X-AMZ-DATE: 20140805T162253Z
AUTHORIZATION: AWS4-HMAC-SHA256 Credential=<credential>, SignedHeaders=content-type;content-length;host;x-amz-date;x-amz-target, Signature=<signature>

{
    "IdentityPoolId": "us-east-1:509f9747-5b5d-484e-a2d7-74fcba108147",
    "MaxResults": 10
}
```

#### Sample Response
<a name="API_ListIdentities_Example_1_Response"></a>

```
1.1 200 OK
x-amzn-requestid: 75dbdfc0-29a2-4177-98e5-602c8f2c21eb
date: Tue, 05 Aug 2014 16:22:54 GMT
content-type: application/json
content-length: 353

{
    "Identities": [
    {
        "IdentityId": "us-east-1:1eeb6443-3fbc-4d3f-a96c-28ff0EXAMPLE",
        "Logins": null
    },
    {
        "IdentityId": "us-east-1:6820d0d3-3c95-4d9f-8813-c4448EXAMPLE",
        "Logins": null
    }],
    "IdentityPoolId": "us-east-1:509f9747-5b5d-484e-a2d7-74fcbEXAMPLE",
    "NextToken": null
}
```

## See Also
<a name="API_ListIdentities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-identity-2014-06-30/ListIdentities) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-identity-2014-06-30/ListIdentities) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-identity-2014-06-30/ListIdentities) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-identity-2014-06-30/ListIdentities) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-identity-2014-06-30/ListIdentities) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-identity-2014-06-30/ListIdentities) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-identity-2014-06-30/ListIdentities) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-identity-2014-06-30/ListIdentities) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cognito-identity-2014-06-30/ListIdentities) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-identity-2014-06-30/ListIdentities) 