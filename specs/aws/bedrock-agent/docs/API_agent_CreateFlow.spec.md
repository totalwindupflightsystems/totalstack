---
id: "@specs/aws/bedrock-agent/docs/API_agent_CreateFlow"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateFlow"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# CreateFlow

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_CreateFlow
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateFlow
<a name="API_agent_CreateFlow"></a>

Creates a prompt flow that you can use to send an input through various steps to yield an output. Configure nodes, each of which corresponds to a step of the flow, and create connections between the nodes to create paths to different outputs. For more information, see [How it works](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html) and [Create a flow in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-create.html) in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_agent_CreateFlow_RequestSyntax"></a>

```
POST /flows/ HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
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
   "name": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_agent_CreateFlow_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_agent_CreateFlow_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_agent_CreateFlow_RequestSyntax) **   <a name="bedrock-agent_CreateFlow-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [customerEncryptionKeyArn](#API_agent_CreateFlow_RequestSyntax) **   <a name="bedrock-agent_CreateFlow-request-customerEncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key to encrypt the flow.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** [definition](#API_agent_CreateFlow_RequestSyntax) **   <a name="bedrock-agent_CreateFlow-request-definition"></a>
A definition of the nodes and connections between nodes in the flow.  
Type: [FlowDefinition](API_agent_FlowDefinition.md) object  
Required: No

 ** [description](#API_agent_CreateFlow_RequestSyntax) **   <a name="bedrock-agent_CreateFlow-request-description"></a>
A description for the flow.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

 ** [executionRoleArn](#API_agent_CreateFlow_RequestSyntax) **   <a name="bedrock-agent_CreateFlow-request-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the service role with permissions to create and manage a flow. For more information, see [Create a service role for flows in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html) in the Amazon Bedrock User Guide.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/(service-role/)?.+`   
Required: Yes

 ** [name](#API_agent_CreateFlow_RequestSyntax) **   <a name="bedrock-agent_CreateFlow-request-name"></a>
A name for the flow.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** [tags](#API_agent_CreateFlow_RequestSyntax) **   <a name="bedrock-agent_CreateFlow-request-tags"></a>
Any tags that you want to attach to the flow. For more information, see [Tagging resources in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html).  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_agent_CreateFlow_ResponseSyntax"></a>

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
   "updatedAt": "string",
   "version": "string"
}
```

## Response Elements
<a name="API_agent_CreateFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_agent_CreateFlow_ResponseSyntax) **   <a name="bedrock-agent_CreateFlow-response-arn"></a>
The Amazon Resource Name (ARN) of the flow.  
Type: String  
Pattern: `arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}` 

 ** [createdAt](#API_agent_CreateFlow_ResponseSyntax) **   <a name="bedrock-agent_CreateFlow-response-createdAt"></a>
The time at which the flow was created.  
Type: Timestamp

 ** [customerEncryptionKeyArn](#API_agent_CreateFlow_ResponseSyntax) **   <a name="bedrock-agent_CreateFlow-response-customerEncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key that you encrypted the flow with.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [definition](#API_agent_CreateFlow_ResponseSyntax) **   <a name="bedrock-agent_CreateFlow-response-definition"></a>
A definition of the nodes and connections between nodes in the flow.  
Type: [FlowDefinition](API_agent_FlowDefinition.md) object

 ** [description](#API_agent_CreateFlow_ResponseSyntax) **   <a name="bedrock-agent_CreateFlow-response-description"></a>
The description of the flow.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [executionRoleArn](#API_agent_CreateFlow_ResponseSyntax) **   <a name="bedrock-agent_CreateFlow-response-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the service role with permissions to create a flow. For more information, see [Create a service role for flows in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html) in the Amazon Bedrock User Guide.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/(service-role/)?.+` 

 ** [id](#API_agent_CreateFlow_ResponseSyntax) **   <a name="bedrock-agent_CreateFlow-response-id"></a>
The unique identifier of the flow.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

 ** [name](#API_agent_CreateFlow_ResponseSyntax) **   <a name="bedrock-agent_CreateFlow-response-name"></a>
The name of the flow.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}` 

 ** [status](#API_agent_CreateFlow_ResponseSyntax) **   <a name="bedrock-agent_CreateFlow-response-status"></a>
The status of the flow. When you submit this request, the status will be `NotPrepared`. If creation fails, the status becomes `Failed`.  
Type: String  
Valid Values: `Failed | Prepared | Preparing | NotPrepared` 

 ** [updatedAt](#API_agent_CreateFlow_ResponseSyntax) **   <a name="bedrock-agent_CreateFlow-response-updatedAt"></a>
The time at which the flow was last updated.  
Type: Timestamp

 ** [version](#API_agent_CreateFlow_ResponseSyntax) **   <a name="bedrock-agent_CreateFlow-response-version"></a>
The version of the flow. When you create a flow, the version created is the `DRAFT` version.  
Type: String  
Length Constraints: Fixed length of 5.  
Pattern: `DRAFT` 

## Errors
<a name="API_agent_CreateFlow_Errors"></a>

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
<a name="API_agent_CreateFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/CreateFlow) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/CreateFlow) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/CreateFlow) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/CreateFlow) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/CreateFlow) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/CreateFlow) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/CreateFlow) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/CreateFlow) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/CreateFlow) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/CreateFlow) 