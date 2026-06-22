---
id: "@specs/aws/bedrock-agent/docs/API_agent_ValidateFlowDefinition"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ValidateFlowDefinition"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# ValidateFlowDefinition

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_ValidateFlowDefinition
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ValidateFlowDefinition
<a name="API_agent_ValidateFlowDefinition"></a>

Validates the definition of a flow.

## Request Syntax
<a name="API_agent_ValidateFlowDefinition_RequestSyntax"></a>

```
POST /flows/validate-definition HTTP/1.1
Content-type: application/json

{
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
   }
}
```

## URI Request Parameters
<a name="API_agent_ValidateFlowDefinition_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_agent_ValidateFlowDefinition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [definition](#API_agent_ValidateFlowDefinition_RequestSyntax) **   <a name="bedrock-agent_ValidateFlowDefinition-request-definition"></a>
The definition of a flow to validate.  
Type: [FlowDefinition](API_agent_FlowDefinition.md) object  
Required: Yes

## Response Syntax
<a name="API_agent_ValidateFlowDefinition_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "validations": [ 
      { 
         "details": { ... },
         "message": "string",
         "severity": "string",
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_agent_ValidateFlowDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [validations](#API_agent_ValidateFlowDefinition_ResponseSyntax) **   <a name="bedrock-agent_ValidateFlowDefinition-response-validations"></a>
Contains an array of objects, each of which contains an error identified by validation.  
Type: Array of [FlowValidation](API_agent_FlowValidation.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_agent_ValidateFlowDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because of missing access permissions.  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. Retry your request.  
HTTP Status Code: 500

 ** ThrottlingException **   
The number of requests exceeds the limit. Resubmit your request later.  
HTTP Status Code: 429

 ** ValidationException **   
Input validation failed. Check your request parameters and retry the request.    
 ** fieldList **   
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## See Also
<a name="API_agent_ValidateFlowDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/ValidateFlowDefinition) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/ValidateFlowDefinition) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/ValidateFlowDefinition) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/ValidateFlowDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/ValidateFlowDefinition) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/ValidateFlowDefinition) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/ValidateFlowDefinition) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/ValidateFlowDefinition) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/ValidateFlowDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/ValidateFlowDefinition) 