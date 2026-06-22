---
id: "@specs/aws/bedrock-agent/docs/API_ListEnforcedGuardrailsConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListEnforcedGuardrailsConfiguration"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# ListEnforcedGuardrailsConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_ListEnforcedGuardrailsConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListEnforcedGuardrailsConfiguration
<a name="API_ListEnforcedGuardrailsConfiguration"></a>

Lists the account-level enforced guardrail configurations.

## Request Syntax
<a name="API_ListEnforcedGuardrailsConfiguration_RequestSyntax"></a>

```
GET /enforcedGuardrailsConfiguration?nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEnforcedGuardrailsConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [nextToken](#API_ListEnforcedGuardrailsConfiguration_RequestSyntax) **   <a name="bedrock-ListEnforcedGuardrailsConfiguration-request-uri-nextToken"></a>
Opaque continuation token of previous paginated response.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Request Body
<a name="API_ListEnforcedGuardrailsConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEnforcedGuardrailsConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "guardrailsConfig": [ 
      { 
         "configId": "string",
         "createdAt": "string",
         "createdBy": "string",
         "guardrailArn": "string",
         "guardrailId": "string",
         "guardrailVersion": "string",
         "inputTags": "string",
         "modelEnforcement": { 
            "excludedModels": [ "string" ],
            "includedModels": [ "string" ]
         },
         "owner": "string",
         "selectiveContentGuarding": { 
            "messages": "string",
            "system": "string"
         },
         "updatedAt": "string",
         "updatedBy": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEnforcedGuardrailsConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [guardrailsConfig](#API_ListEnforcedGuardrailsConfiguration_ResponseSyntax) **   <a name="bedrock-ListEnforcedGuardrailsConfiguration-response-guardrailsConfig"></a>
Array of AccountEnforcedGuardrailOutputConfiguration objects.  
Type: Array of [AccountEnforcedGuardrailOutputConfiguration](API_AccountEnforcedGuardrailOutputConfiguration.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [nextToken](#API_ListEnforcedGuardrailsConfiguration_ResponseSyntax) **   <a name="bedrock-ListEnforcedGuardrailsConfiguration-response-nextToken"></a>
Opaque continuation token of previous paginated response.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_ListEnforcedGuardrailsConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.  
HTTP Status Code: 400

## See Also
<a name="API_ListEnforcedGuardrailsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/ListEnforcedGuardrailsConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/ListEnforcedGuardrailsConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ListEnforcedGuardrailsConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/ListEnforcedGuardrailsConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ListEnforcedGuardrailsConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/ListEnforcedGuardrailsConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/ListEnforcedGuardrailsConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListEnforcedGuardrailsConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/ListEnforcedGuardrailsConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ListEnforcedGuardrailsConfiguration) 