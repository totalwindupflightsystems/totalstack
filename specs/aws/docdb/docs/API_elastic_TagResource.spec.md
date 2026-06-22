---
id: "@specs/aws/docdb/docs/API_elastic_TagResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TagResource"
status: active
depends_on:
  - "@specs/aws/docdb/meta"
---

# TagResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/docdb/docs/API_elastic_TagResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TagResource
<a name="API_elastic_TagResource"></a>

Adds metadata tags to an elastic cluster resource

## Request Syntax
<a name="API_elastic_TagResource_RequestSyntax"></a>

```
POST /tags/{{resourceArn}} HTTP/1.1
Content-type: application/json

{
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_elastic_TagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_elastic_TagResource_RequestSyntax) **   <a name="documentdb-elastic_TagResource-request-uri-resourceArn"></a>
The ARN identifier of the elastic cluster resource.  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Required: Yes

## Request Body
<a name="API_elastic_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tags](#API_elastic_TagResource_RequestSyntax) **   <a name="documentdb-elastic_TagResource-request-tags"></a>
The tags that are assigned to the elastic cluster resource.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: Yes

## Response Syntax
<a name="API_elastic_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_elastic_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_elastic_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
There was an internal server error.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource could not be located.    
 ** message **   
An error message describing the failure.  
 ** resourceId **   
The ID of the resource that could not be located.  
 ** resourceType **   
The type of the resource that could not be found.
HTTP Status Code: 404

 ** ThrottlingException **   
ThrottlingException will be thrown when request was denied due to request throttling.    
 ** retryAfterSeconds **   
The number of seconds to wait before retrying the operation.
HTTP Status Code: 429

 ** ValidationException **   
A structure defining a validation exception.    
 ** fieldList **   
A list of the fields in which the validation exception occurred.  
 ** message **   
An error message describing the validation exception.  
 ** reason **   
The reason why the validation exception occurred (one of `unknownOperation`, `cannotParse`, `fieldValidationFailed`, or `other`).
HTTP Status Code: 400

## See Also
<a name="API_elastic_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/docdb-elastic-2022-11-28/TagResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/docdb-elastic-2022-11-28/TagResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-elastic-2022-11-28/TagResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/docdb-elastic-2022-11-28/TagResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-elastic-2022-11-28/TagResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/TagResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/docdb-elastic-2022-11-28/TagResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/docdb-elastic-2022-11-28/TagResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/docdb-elastic-2022-11-28/TagResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-elastic-2022-11-28/TagResource) 