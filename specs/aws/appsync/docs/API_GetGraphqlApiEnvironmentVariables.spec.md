---
id: "@specs/aws/appsync/docs/API_GetGraphqlApiEnvironmentVariables"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetGraphqlApiEnvironmentVariables"
status: active
depends_on:
  - "@specs/aws/appsync/meta"
---

# GetGraphqlApiEnvironmentVariables

> **source:** AWS Documentation
> **spec:id:** @specs/aws/appsync/docs/API_GetGraphqlApiEnvironmentVariables
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetGraphqlApiEnvironmentVariables
<a name="API_GetGraphqlApiEnvironmentVariables"></a>

Retrieves the list of environmental variable key-value pairs associated with an API by its ID value.

## Request Syntax
<a name="API_GetGraphqlApiEnvironmentVariables_RequestSyntax"></a>

```
GET /v1/apis/{{apiId}}/environmentVariables HTTP/1.1
```

## URI Request Parameters
<a name="API_GetGraphqlApiEnvironmentVariables_RequestParameters"></a>

The request uses the following URI parameters.

 ** [apiId](#API_GetGraphqlApiEnvironmentVariables_RequestSyntax) **   <a name="appsync-GetGraphqlApiEnvironmentVariables-request-uri-apiId"></a>
The ID of the API from which the environmental variable list will be retrieved.  
Required: Yes

## Request Body
<a name="API_GetGraphqlApiEnvironmentVariables_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetGraphqlApiEnvironmentVariables_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "environmentVariables": { 
      "string" : "string" 
   }
}
```

## Response Elements
<a name="API_GetGraphqlApiEnvironmentVariables_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environmentVariables](#API_GetGraphqlApiEnvironmentVariables_ResponseSyntax) **   <a name="appsync-GetGraphqlApiEnvironmentVariables-response-environmentVariables"></a>
The payload containing each environmental variable in the `"key" : "value"` format.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 2. Maximum length of 64.  
Key Pattern: `^[A-Za-z]+\w*$`   
Value Length Constraints: Minimum length of 0. Maximum length of 512.

## Errors
<a name="API_GetGraphqlApiEnvironmentVariables_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to perform this operation on this resource.  
HTTP Status Code: 403

 ** BadRequestException **   
The request is not well formed. For example, a value is invalid or a required field is missing. Check the field values, and then try again.    
 ** detail **   
Provides further details for the reason behind the bad request. For reason type `CODE_ERROR`, the detail will contain a list of code errors.  
 ** reason **   
Provides context for the cause of the bad request. The only supported value is `CODE_ERROR`.
HTTP Status Code: 400

 ** InternalFailureException **   
An internal AWS AppSync error occurred. Try your request again.  
HTTP Status Code: 500

 ** NotFoundException **   
The resource specified in the request was not found. Check the resource, and then try again.  
HTTP Status Code: 404

 ** UnauthorizedException **   
You aren't authorized to perform this operation.  
HTTP Status Code: 401

## See Also
<a name="API_GetGraphqlApiEnvironmentVariables_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appsync-2017-07-25/GetGraphqlApiEnvironmentVariables) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appsync-2017-07-25/GetGraphqlApiEnvironmentVariables) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/GetGraphqlApiEnvironmentVariables) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appsync-2017-07-25/GetGraphqlApiEnvironmentVariables) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/GetGraphqlApiEnvironmentVariables) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appsync-2017-07-25/GetGraphqlApiEnvironmentVariables) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appsync-2017-07-25/GetGraphqlApiEnvironmentVariables) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appsync-2017-07-25/GetGraphqlApiEnvironmentVariables) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appsync-2017-07-25/GetGraphqlApiEnvironmentVariables) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/GetGraphqlApiEnvironmentVariables) 