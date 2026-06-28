---
id: "@specs/aws/rolesanywhere/docs/API_ListSubjects"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListSubjects"
status: active
depends_on:
  - "@specs/aws/rolesanywhere/meta"
---

# ListSubjects

> **source:** AWS Documentation
> **spec:id:** @specs/aws/rolesanywhere/docs/API_ListSubjects
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListSubjects
<a name="API_ListSubjects"></a>

Lists the subjects in the authenticated account and AWS Region.

 **Required permissions: ** `rolesanywhere:ListSubjects`. 

## Request Syntax
<a name="API_ListSubjects_RequestSyntax"></a>

```
GET /subjects?nextToken={{nextToken}}&pageSize={{pageSize}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListSubjects_RequestParameters"></a>

The request uses the following URI parameters.

 ** [nextToken](#API_ListSubjects_RequestSyntax) **   <a name="rolesanywhere-ListSubjects-request-uri-nextToken"></a>
A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.  
Length Constraints: Minimum length of 1. Maximum length of 10000.

 ** [pageSize](#API_ListSubjects_RequestSyntax) **   <a name="rolesanywhere-ListSubjects-request-uri-pageSize"></a>
The number of resources in the paginated list. 

## Request Body
<a name="API_ListSubjects_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListSubjects_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "subjects": [ 
      { 
         "createdAt": "string",
         "enabled": boolean,
         "lastSeenAt": "string",
         "subjectArn": "string",
         "subjectId": "string",
         "updatedAt": "string",
         "x509Subject": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSubjects_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSubjects_ResponseSyntax) **   <a name="rolesanywhere-ListSubjects-response-nextToken"></a>
A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.  
Type: String

 ** [subjects](#API_ListSubjects_ResponseSyntax) **   <a name="rolesanywhere-ListSubjects-response-subjects"></a>
A list of subjects.  
Type: Array of [SubjectSummary](API_SubjectSummary.md) objects

## Errors
<a name="API_ListSubjects_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.  
HTTP Status Code: 403

 ** ValidationException **   
Validation exception error.  
HTTP Status Code: 400

## See Also
<a name="API_ListSubjects_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rolesanywhere-2018-05-10/ListSubjects) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rolesanywhere-2018-05-10/ListSubjects) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/ListSubjects) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rolesanywhere-2018-05-10/ListSubjects) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/ListSubjects) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rolesanywhere-2018-05-10/ListSubjects) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rolesanywhere-2018-05-10/ListSubjects) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rolesanywhere-2018-05-10/ListSubjects) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rolesanywhere-2018-05-10/ListSubjects) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/ListSubjects) 