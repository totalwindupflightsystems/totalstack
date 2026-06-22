---
id: "@specs/aws/codepipeline/docs/API_GetActionType"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GetActionType"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# GetActionType

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_GetActionType
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GetActionType
<a name="API_GetActionType"></a>

Returns information about an action type created for an external provider, where the action is to be used by customers of the external provider. The action can be created with any supported integration model.

## Request Syntax
<a name="API_GetActionType_RequestSyntax"></a>

```
{
   "category": "{{string}}",
   "owner": "{{string}}",
   "provider": "{{string}}",
   "version": "{{string}}"
}
```

## Request Parameters
<a name="API_GetActionType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [category](#API_GetActionType_RequestSyntax) **   <a name="CodePipeline-GetActionType-request-category"></a>
Defines what kind of action can be taken in the stage. The following are the valid values:  
+  `Source` 
+  `Build` 
+  `Test` 
+  `Deploy` 
+  `Approval` 
+  `Invoke` 
+  `Compute` 
Type: String  
Valid Values: `Source | Build | Deploy | Test | Invoke | Approval | Compute`   
Required: Yes

 ** [owner](#API_GetActionType_RequestSyntax) **   <a name="CodePipeline-GetActionType-request-owner"></a>
The creator of an action type that was created with any supported integration model. There are two valid values: `AWS` and `ThirdParty`.  
Type: String  
Pattern: `AWS|ThirdParty`   
Required: Yes

 ** [provider](#API_GetActionType_RequestSyntax) **   <a name="CodePipeline-GetActionType-request-provider"></a>
The provider of the action type being called. The provider name is specified when the action type is created.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 35.  
Pattern: `[0-9A-Za-z_-]+`   
Required: Yes

 ** [version](#API_GetActionType_RequestSyntax) **   <a name="CodePipeline-GetActionType-request-version"></a>
A string that describes the action type version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 9.  
Pattern: `[0-9A-Za-z_-]+`   
Required: Yes

## Response Syntax
<a name="API_GetActionType_ResponseSyntax"></a>

```
{
   "actionType": { 
      "description": "string",
      "executor": { 
         "configuration": { 
            "jobWorkerExecutorConfiguration": { 
               "pollingAccounts": [ "string" ],
               "pollingServicePrincipals": [ "string" ]
            },
            "lambdaExecutorConfiguration": { 
               "lambdaFunctionArn": "string"
            }
         },
         "jobTimeout": number,
         "policyStatementsTemplate": "string",
         "type": "string"
      },
      "id": { 
         "category": "string",
         "owner": "string",
         "provider": "string",
         "version": "string"
      },
      "inputArtifactDetails": { 
         "maximumCount": number,
         "minimumCount": number
      },
      "outputArtifactDetails": { 
         "maximumCount": number,
         "minimumCount": number
      },
      "permissions": { 
         "allowedAccounts": [ "string" ]
      },
      "properties": [ 
         { 
            "description": "string",
            "key": boolean,
            "name": "string",
            "noEcho": boolean,
            "optional": boolean,
            "queryable": boolean
         }
      ],
      "urls": { 
         "configurationUrl": "string",
         "entityUrlTemplate": "string",
         "executionUrlTemplate": "string",
         "revisionUrlTemplate": "string"
      }
   }
}
```

## Response Elements
<a name="API_GetActionType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionType](#API_GetActionType_ResponseSyntax) **   <a name="CodePipeline-GetActionType-response-actionType"></a>
The action type information for the requested action type, such as the action type ID.  
Type: [ActionTypeDeclaration](API_ActionTypeDeclaration.md) object

## Errors
<a name="API_GetActionType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ActionTypeNotFoundException **   
The specified action type cannot be found.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## See Also
<a name="API_GetActionType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/GetActionType) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/GetActionType) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/GetActionType) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/GetActionType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/GetActionType) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/GetActionType) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/GetActionType) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/GetActionType) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/GetActionType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/GetActionType) 