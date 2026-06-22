---
id: "@specs/aws/bedrock-agent/docs/API_GetAutomatedReasoningPolicyBuildWorkflowResultAssets"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetAutomatedReasoningPolicyBuildWorkflowResultAssets"
status: active
depends_on:
  - "@specs/aws/bedrock-agent/meta"
---

# GetAutomatedReasoningPolicyBuildWorkflowResultAssets

> **source:** AWS Documentation
> **spec:id:** @specs/aws/bedrock-agent/docs/API_GetAutomatedReasoningPolicyBuildWorkflowResultAssets
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetAutomatedReasoningPolicyBuildWorkflowResultAssets
<a name="API_GetAutomatedReasoningPolicyBuildWorkflowResultAssets"></a>

Retrieves the resulting assets from a completed Automated Reasoning policy build workflow, including build logs, quality reports, and generated policy artifacts.

## Request Syntax
<a name="API_GetAutomatedReasoningPolicyBuildWorkflowResultAssets_RequestSyntax"></a>

```
GET /automated-reasoning-policies/{{policyArn}}/build-workflows/{{buildWorkflowId}}/result-assets?assetId={{assetId}}&assetType={{assetType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAutomatedReasoningPolicyBuildWorkflowResultAssets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [assetId](#API_GetAutomatedReasoningPolicyBuildWorkflowResultAssets_RequestSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyBuildWorkflowResultAssets-request-uri-assetId"></a>
The unique identifier of the specific asset to retrieve when multiple assets of the same type exist. This is required when retrieving SOURCE\_DOCUMENT assets, as multiple source documents may have been used in the workflow. The asset ID can be obtained from the asset manifest.  
Length Constraints: Minimum length of 0. Maximum length of 36.  
Pattern: `[0-9a-fA-F\-]+` 

 ** [assetType](#API_GetAutomatedReasoningPolicyBuildWorkflowResultAssets_RequestSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyBuildWorkflowResultAssets-request-uri-assetType"></a>
The type of asset to retrieve (e.g., BUILD\_LOG, QUALITY\_REPORT, POLICY\_DEFINITION, GENERATED\_TEST\_CASES, POLICY\_SCENARIOS, FIDELITY\_REPORT, ASSET\_MANIFEST, SOURCE\_DOCUMENT).  
Valid Values: `BUILD_LOG | QUALITY_REPORT | POLICY_DEFINITION | GENERATED_TEST_CASES | POLICY_SCENARIOS | FIDELITY_REPORT | ASSET_MANIFEST | SOURCE_DOCUMENT`   
Required: Yes

 ** [buildWorkflowId](#API_GetAutomatedReasoningPolicyBuildWorkflowResultAssets_RequestSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyBuildWorkflowResultAssets-request-uri-buildWorkflowId"></a>
The unique identifier of the build workflow whose result assets you want to retrieve.  
Length Constraints: Minimum length of 0. Maximum length of 36.  
Pattern: `[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}`   
Required: Yes

 ** [policyArn](#API_GetAutomatedReasoningPolicyBuildWorkflowResultAssets_RequestSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyBuildWorkflowResultAssets-request-uri-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflow assets you want to retrieve.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?`   
Required: Yes

## Request Body
<a name="API_GetAutomatedReasoningPolicyBuildWorkflowResultAssets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAutomatedReasoningPolicyBuildWorkflowResultAssets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "buildWorkflowAssets": { ... },
   "buildWorkflowId": "string",
   "policyArn": "string"
}
```

## Response Elements
<a name="API_GetAutomatedReasoningPolicyBuildWorkflowResultAssets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [buildWorkflowAssets](#API_GetAutomatedReasoningPolicyBuildWorkflowResultAssets_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyBuildWorkflowResultAssets-response-buildWorkflowAssets"></a>
The requested build workflow asset. This is a union type that returns only one of the available asset types (logs, reports, or generated artifacts) based on the specific asset type requested in the API call.  
Type: [AutomatedReasoningPolicyBuildResultAssets](API_AutomatedReasoningPolicyBuildResultAssets.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [buildWorkflowId](#API_GetAutomatedReasoningPolicyBuildWorkflowResultAssets_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyBuildWorkflowResultAssets-response-buildWorkflowId"></a>
The unique identifier of the build workflow.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 36.  
Pattern: `[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}` 

 ** [policyArn](#API_GetAutomatedReasoningPolicyBuildWorkflowResultAssets_ResponseSyntax) **   <a name="bedrock-GetAutomatedReasoningPolicyBuildWorkflowResultAssets-response-policyArn"></a>
The Amazon Resource Name (ARN) of the Automated Reasoning policy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:automated-reasoning-policy/[a-z0-9]{12}(:([1-9][0-9]{0,11}))?` 

## Errors
<a name="API_GetAutomatedReasoningPolicyBuildWorkflowResultAssets_Errors"></a>

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
<a name="API_GetAutomatedReasoningPolicyBuildWorkflowResultAssets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-2023-04-20/GetAutomatedReasoningPolicyBuildWorkflowResultAssets) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-2023-04-20/GetAutomatedReasoningPolicyBuildWorkflowResultAssets) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/GetAutomatedReasoningPolicyBuildWorkflowResultAssets) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-2023-04-20/GetAutomatedReasoningPolicyBuildWorkflowResultAssets) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/GetAutomatedReasoningPolicyBuildWorkflowResultAssets) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-2023-04-20/GetAutomatedReasoningPolicyBuildWorkflowResultAssets) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-2023-04-20/GetAutomatedReasoningPolicyBuildWorkflowResultAssets) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/GetAutomatedReasoningPolicyBuildWorkflowResultAssets) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-2023-04-20/GetAutomatedReasoningPolicyBuildWorkflowResultAssets) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/GetAutomatedReasoningPolicyBuildWorkflowResultAssets) 