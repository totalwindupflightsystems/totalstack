---
id: "@specs/aws/bedrock-agent/docs/API_agent_GetFlow"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetFlow"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GetFlow

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_agent_GetFlow
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetFlow
<a name="API_agent_GetFlow"></a>

Retrieves information about a flow. For more information, see [Manage a flow in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-manage.html) in the Amazon Bedrock User Guide.

## Request Syntax
<a name="API_agent_GetFlow_RequestSyntax"></a>

```
GET /flows/{{flowIdentifier}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_agent_GetFlow_RequestParameters"></a>

The request uses the following URI parameters.

 ** [flowIdentifier](#API_agent_GetFlow_RequestSyntax) **   <a name="bedrock-agent_GetFlow-request-uri-flowIdentifier"></a>
The unique identifier of the flow.  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10})|([0-9a-zA-Z]{10})`   
Required: Yes

## Request Body
<a name="API_agent_GetFlow_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_agent_GetFlow_ResponseSyntax"></a>

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
   "validations": [ 
      { 
         "details": { ... },
         "message": "string",
         "severity": "string",
         "type": "string"
      }
   ],
   "version": "string"
}
```

## Response Elements
<a name="API_agent_GetFlow_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_agent_GetFlow_ResponseSyntax) **   <a name="bedrock-agent_GetFlow-response-arn"></a>
The Amazon Resource Name (ARN) of the flow.  
Type: String  
Pattern: `arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}` 

 ** [createdAt](#API_agent_GetFlow_ResponseSyntax) **   <a name="bedrock-agent_GetFlow-response-createdAt"></a>
The time at which the flow was created.  
Type: Timestamp

 ** [customerEncryptionKeyArn](#API_agent_GetFlow_ResponseSyntax) **   <a name="bedrock-agent_GetFlow-response-customerEncryptionKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key that the flow is encrypted with.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}` 

 ** [definition](#API_agent_GetFlow_ResponseSyntax) **   <a name="bedrock-agent_GetFlow-response-definition"></a>
The definition of the nodes and connections between the nodes in the flow.  
Type: [FlowDefinition](API_agent_FlowDefinition.md) object

 ** [description](#API_agent_GetFlow_ResponseSyntax) **   <a name="bedrock-agent_GetFlow-response-description"></a>
The description of the flow.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.

 ** [executionRoleArn](#API_agent_GetFlow_ResponseSyntax) **   <a name="bedrock-agent_GetFlow-response-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the service role with permissions to create a flow. For more information, see [Create a service row for flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html) in the Amazon Bedrock User Guide.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/(service-role/)?.+` 

 ** [id](#API_agent_GetFlow_ResponseSyntax) **   <a name="bedrock-agent_GetFlow-response-id"></a>
The unique identifier of the flow.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}` 

 ** [name](#API_agent_GetFlow_ResponseSyntax) **   <a name="bedrock-agent_GetFlow-response-name"></a>
The name of the flow.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}` 

 ** [status](#API_agent_GetFlow_ResponseSyntax) **   <a name="bedrock-agent_GetFlow-response-status"></a>
The status of the flow. The following statuses are possible:  
+ NotPrepared – The flow has been created or updated, but hasn't been prepared. If you just created the flow, you can't test it. If you updated the flow, the `DRAFT` version won't contain the latest changes for testing. Send a [PrepareFlow](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_PrepareFlow.html) request to package the latest changes into the `DRAFT` version.
+ Preparing – The flow is being prepared so that the `DRAFT` version contains the latest changes for testing.
+ Prepared – The flow is prepared and the `DRAFT` version contains the latest changes for testing.
+ Failed – The last API operation that you invoked on the flow failed. Send a [GetFlow](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetFlow.html) request and check the error message in the `validations` field.
Type: String  
Valid Values: `Failed | Prepared | Preparing | NotPrepared` 

 ** [updatedAt](#API_agent_GetFlow_ResponseSyntax) **   <a name="bedrock-agent_GetFlow-response-updatedAt"></a>
The time at which the flow was last updated.  
Type: Timestamp

 ** [validations](#API_agent_GetFlow_ResponseSyntax) **   <a name="bedrock-agent_GetFlow-response-validations"></a>
A list of validation error messages related to the last failed operation on the flow.  
Type: Array of [FlowValidation](API_agent_FlowValidation.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [version](#API_agent_GetFlow_ResponseSyntax) **   <a name="bedrock-agent_GetFlow-response-version"></a>
The version of the flow for which information was retrieved.  
Type: String  
Length Constraints: Fixed length of 5.  
Pattern: `DRAFT` 

## Errors
<a name="API_agent_GetFlow_Errors"></a>

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
 ** fieldList **   
A list of objects containing fields that caused validation errors and their corresponding validation error messages.
HTTP Status Code: 400

## See Also
<a name="API_agent_GetFlow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agent-2023-06-05/GetFlow) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agent-2023-06-05/GetFlow) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/GetFlow) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agent-2023-06-05/GetFlow) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/GetFlow) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agent-2023-06-05/GetFlow) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agent-2023-06-05/GetFlow) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agent-2023-06-05/GetFlow) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-agent-2023-06-05/GetFlow) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/GetFlow) 