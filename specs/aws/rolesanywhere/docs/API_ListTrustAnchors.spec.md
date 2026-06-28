---
id: "@specs/aws/rolesanywhere/docs/API_ListTrustAnchors"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTrustAnchors"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# ListTrustAnchors

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_ListTrustAnchors
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTrustAnchors
<a name="API_ListTrustAnchors"></a>

Lists the trust anchors in the authenticated account and AWS Region.

 **Required permissions: ** `rolesanywhere:ListTrustAnchors`. 

## Request Syntax
<a name="API_ListTrustAnchors_RequestSyntax"></a>

```
GET /trustanchors?nextToken={{nextToken}}&pageSize={{pageSize}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTrustAnchors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [nextToken](#API_ListTrustAnchors_RequestSyntax) **   <a name="rolesanywhere-ListTrustAnchors-request-uri-nextToken"></a>
A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.  
Length Constraints: Minimum length of 1. Maximum length of 10000.

 ** [pageSize](#API_ListTrustAnchors_RequestSyntax) **   <a name="rolesanywhere-ListTrustAnchors-request-uri-pageSize"></a>
The number of resources in the paginated list. 

## Request Body
<a name="API_ListTrustAnchors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTrustAnchors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "trustAnchors": [ 
      { 
         "createdAt": "string",
         "enabled": boolean,
         "name": "string",
         "notificationSettings": [ 
            { 
               "channel": "string",
               "configuredBy": "string",
               "enabled": boolean,
               "event": "string",
               "threshold": number
            }
         ],
         "source": { 
            "sourceData": { ... },
            "sourceType": "string"
         },
         "trustAnchorArn": "string",
         "trustAnchorId": "string",
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTrustAnchors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTrustAnchors_ResponseSyntax) **   <a name="rolesanywhere-ListTrustAnchors-response-nextToken"></a>
A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.  
Type: String

 ** [trustAnchors](#API_ListTrustAnchors_ResponseSyntax) **   <a name="rolesanywhere-ListTrustAnchors-response-trustAnchors"></a>
A list of trust anchors.  
Type: Array of [TrustAnchorDetail](API_TrustAnchorDetail.md) objects

## Errors
<a name="API_ListTrustAnchors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 403

 ** ValidationException **   
Validation exception error.  
HTTP Status Code: 400

## See Also
<a name="API_ListTrustAnchors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rolesanywhere-2018-05-10/ListTrustAnchors) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rolesanywhere-2018-05-10/ListTrustAnchors) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/ListTrustAnchors) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rolesanywhere-2018-05-10/ListTrustAnchors) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/ListTrustAnchors) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rolesanywhere-2018-05-10/ListTrustAnchors) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rolesanywhere-2018-05-10/ListTrustAnchors) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rolesanywhere-2018-05-10/ListTrustAnchors) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rolesanywhere-2018-05-10/ListTrustAnchors) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/ListTrustAnchors) 