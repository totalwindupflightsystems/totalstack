---
id: "@specs/aws/bedrock-agent/docs/API_agent_UpdateFlow"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateFlow"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# UpdateFlow

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_UpdateFlow
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateFlow
<a name="API_agent_UpdateFlow"></a>

Modifies a flow. Include both fields that you want to keep and fields that you want to change. For more information, see [How it works](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html) and [Create a flow in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-create.html) in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_agent_UpdateFlow_RequestSyntax"></a>

```
PUT /flows/{{flowIdentifier}}/ HTTP/1.1
Content-type: application/json

{
   "customerEncryptionKeyArn": "{{string}}",
   "definition": { 
      "connections": [ 
         { 
            "configuration": { ... },
            "name": "{{string}}",
            "source": "{{string}}",
            "target": "{{string}}",
            "type": "{{string}}"
         }
      ],
      "nodes": [ 
         { 
            "configuration": { ... },
            "inputs": [ 
               { 
                  "category": "{{string}}",
                  "expression": "{{string}}",
                  "name": "{{string}}",
                  "type": "{{string}}"
               }
            ],
            "name": "{{string}}",
            "outputs": [ 
               { 
                  "name": "{{string}}",
                  "type": "{{string}}"
               }
            ],
            "type": "{{string}}"
         }
      ]
   },
   "description": "{{string}}",
   "executionRoleArn": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_agent_UpdateFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowIdentifier](#API_agent_UpdateFlow_RequestSyntax) **   <a name="bedrock-agent_UpdateFlow-request-uri-flowIdentifier"></a>
The unique identifier of the flow.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10})|([0-9a-zA-Z]{10})`   
Required: Yes

## Request Body
<a name="API_agent_UpdateFlow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [customerEncryptionKeyArn](#API_agent_UpdateFlow_RequestSyntax) **   <a name="bedrock-agent_UpdateFlow-request-customerEncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key to encrypt the flow.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** [definition](#API_agent_UpdateFlow_RequestSyntax) **   <a name="bedrock-agent_UpdateFlow-request-definition"></a>
A definition of the nodes and the connections between the nodes in the flow.  
Type: [FlowDefinition](API_agent_FlowDefinition.md) object  
Required: No

 ** [description](#API_agent_UpdateFlow_RequestSyntax) **   <a name="bedrock-agent_UpdateFlow-request-description"></a>
A description for the flow.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [executionRoleArn](#API_agent_UpdateFlow_RequestSyntax) **   <a name="bedrock-agent_UpdateFlow-request-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the service role with permissions to create and manage a flow. For more information, see [Create a service role for flows in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html) in the Amazon Bedrock User Guide.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/(service-role/)?.+`   
Required: Yes

 ** [name](#API_agent_UpdateFlow_RequestSyntax) **   <a name="bedrock-agent_UpdateFlow-request-name"></a>
A name for the flow.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

## Response Syntax
<a name="API_agent_UpdateFlow_ResponseSyntax"></a>

```
HTTP/1.1 200
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
   "updatedAt": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_agent_UpdateFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_agent_UpdateFlow_ResponseSyntax) **   <a name="bedrock-agent_UpdateFlow-response-arn"></a>
The Amazon Resource Name (ARN) of the flow.  
Type: String  
Pattern: `arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}` 

 ** [createdAt](#API_agent_UpdateFlow_ResponseSyntax) **   <a name="bedrock-agent_UpdateFlow-response-createdAt"></a>
The time at which the flow was created.  
Type: Timestamp

 ** [customerEncryptionKeyArn](#API_agent_UpdateFlow_ResponseSyntax) **   <a name="bedrock-agent_UpdateFlow-response-customerEncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key that the flow was encrypted with.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [definition](#API_agent_UpdateFlow_ResponseSyntax) **   <a name="bedrock-agent_UpdateFlow-response-definition"></a>
A definition of the nodes and the connections between nodes in the flow.  
Type: [FlowDefinition](API_agent_FlowDefinition.md) object

 ** [description](#API_agent_UpdateFlow_ResponseSyntax) **   <a name="bedrock-agent_UpdateFlow-response-description"></a>
The description of the flow.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [executionRoleArn](#API_agent_UpdateFlow_ResponseSyntax) **   <a name="bedrock-agent_UpdateFlow-response-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the service role with permissions to create a flow. For more information, see [Create a service role for flows in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html) in the Amazon Bedrock User Guide.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/(service-role/)?.+` 

 ** [id](#API_agent_UpdateFlow_ResponseSyntax) **   <a name="bedrock-agent_UpdateFlow-response-id"></a>
The unique identifier of the flow.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

 ** [name](#API_agent_UpdateFlow_ResponseSyntax) **   <a name="bedrock-agent_UpdateFlow-response-name"></a>
The name of the flow.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}` 

 ** [status](#API_agent_UpdateFlow_ResponseSyntax) **   <a name="bedrock-agent_UpdateFlow-response-status"></a>
The status of the flow. When you submit this request, the status will be `NotPrepared`. If updating fails, the status becomes `Failed`.  
Type: String  
Valid Values: `Failed | Prepared | Preparing | NotPrepared` 

 ** [updatedAt](#API_agent_UpdateFlow_ResponseSyntax) **   <a name="bedrock-agent_UpdateFlow-response-updatedAt"></a>
The time at which the flow was last updated.  
Type: Timestamp

 ** [version](#API_agent_UpdateFlow_ResponseSyntax) **   <a name="bedrock-agent_UpdateFlow-response-version"></a>
The version of the flow. When you update a flow, the version updated is the `DRAFT` version.  
Type: String  
Length Constraints: Fixed length of 5.  
Pattern: `DRAFT` 

## Errors
<a name="API_agent_UpdateFlow_Errors"></a>

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
<a name="API_agent_UpdateFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/UpdateFlow) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/UpdateFlow) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/UpdateFlow) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/UpdateFlow) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/UpdateFlow) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/UpdateFlow) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/UpdateFlow) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/UpdateFlow) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/UpdateFlow) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/UpdateFlow) 