---
id: "@specs/aws/bedrock/docs/API_agent_CreateFlowVersion"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateFlowVersion"
status: active
depends_on:
  - "@specs/aws/bedrock/meta"
---

# CreateFlowVersion

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock/docs/API_agent_CreateFlowVersion
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateFlowVersion
<a name="API_agent_CreateFlowVersion"></a>

Creates a version of the flow that you can deploy. For more information, see [Deploy a flow in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-deploy.html) in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_agent_CreateFlowVersion_RequestSyntax"></a>

```
POST /flows/{{flowIdentifier}}/versions HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_agent_CreateFlowVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowIdentifier](#API_agent_CreateFlowVersion_RequestSyntax) **   <a name="bedrock-agent_CreateFlowVersion-request-uri-flowIdentifier"></a>
The unique identifier of the flow that you want to create a version of.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10})|([0-9a-zA-Z]{10})`   
Required: Yes

## Request Body
<a name="API_agent_CreateFlowVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_agent_CreateFlowVersion_RequestSyntax) **   <a name="bedrock-agent_CreateFlowVersion-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_agent_CreateFlowVersion_RequestSyntax) **   <a name="bedrock-agent_CreateFlowVersion-request-description"></a>
A description of the version of the flow.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

## Response Syntax
<a name="API_agent_CreateFlowVersion_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "createdAt": "string",
   "customerEncryptionKeyArn": "string",
   "definition": { 
      "connections": [ 
         { 
            "configuration": { ... },
            "name": "string",
            "source": "string",
            "target": "string",
            "type": "string"
         }
      ],
      "nodes": [ 
         { 
            "configuration": { ... },
            "inputs": [ 
               { 
                  "category": "string",
                  "expression": "string",
                  "name": "string",
                  "type": "string"
               }
            ],
            "name": "string",
            "outputs": [ 
               { 
                  "name": "string",
                  "type": "string"
               }
            ],
            "type": "string"
         }
      ]
   },
   "description": "string",
   "executionRoleArn": "string",
   "id": "string",
   "name": "string",
   "status": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_agent_CreateFlowVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_agent_CreateFlowVersion_ResponseSyntax) **   <a name="bedrock-agent_CreateFlowVersion-response-arn"></a>
The Amazon Resource Name (ARN) of the flow.  
Type: String  
Pattern: `arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}` 

 ** [createdAt](#API_agent_CreateFlowVersion_ResponseSyntax) **   <a name="bedrock-agent_CreateFlowVersion-response-createdAt"></a>
The time at which the flow was created.  
Type: Timestamp

 ** [customerEncryptionKeyArn](#API_agent_CreateFlowVersion_ResponseSyntax) **   <a name="bedrock-agent_CreateFlowVersion-response-customerEncryptionKeyArn"></a>
The KMS key that the flow is encrypted with.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [definition](#API_agent_CreateFlowVersion_ResponseSyntax) **   <a name="bedrock-agent_CreateFlowVersion-response-definition"></a>
A definition of the nodes and connections in the flow.  
Type: [FlowDefinition](API_agent_FlowDefinition.md) object

 ** [description](#API_agent_CreateFlowVersion_ResponseSyntax) **   <a name="bedrock-agent_CreateFlowVersion-response-description"></a>
The description of the version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [executionRoleArn](#API_agent_CreateFlowVersion_ResponseSyntax) **   <a name="bedrock-agent_CreateFlowVersion-response-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the service role with permissions to create a flow. For more information, see [Create a service role for flows in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html) in the Amazon Bedrock User Guide.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/(service-role/)?.+` 

 ** [id](#API_agent_CreateFlowVersion_ResponseSyntax) **   <a name="bedrock-agent_CreateFlowVersion-response-id"></a>
The unique identifier of the flow.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

 ** [name](#API_agent_CreateFlowVersion_ResponseSyntax) **   <a name="bedrock-agent_CreateFlowVersion-response-name"></a>
The name of the version.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}` 

 ** [status](#API_agent_CreateFlowVersion_ResponseSyntax) **   <a name="bedrock-agent_CreateFlowVersion-response-status"></a>
The status of the flow.  
Type: String  
Valid Values: `Failed | Prepared | Preparing | NotPrepared` 

 ** [version](#API_agent_CreateFlowVersion_ResponseSyntax) **   <a name="bedrock-agent_CreateFlowVersion-response-version"></a>
The version of the flow that was created. Versions are numbered incrementally, starting from 1.  
Type: String  
Pattern: `[0-9]{1,5}` 

## Errors
<a name="API_agent_CreateFlowVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** ConflictException **   
There was a conflict performing an operation.  
HTTP Status Code: 409

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
The number of requests exceeds the service quota. Resubmit your request later.  
HTTP Status Code: 402

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.    
 ** fieldList **   
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## See Also
<a name="API_agent_CreateFlowVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/CreateFlowVersion) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/CreateFlowVersion) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/CreateFlowVersion) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/CreateFlowVersion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/CreateFlowVersion) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/CreateFlowVersion) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/CreateFlowVersion) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/CreateFlowVersion) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/CreateFlowVersion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/CreateFlowVersion) 