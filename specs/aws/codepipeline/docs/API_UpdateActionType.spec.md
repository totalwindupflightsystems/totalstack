---
id: "@specs/aws/codepipeline/docs/API_UpdateActionType"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateActionType"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# UpdateActionType

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_UpdateActionType
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateActionType
<a name="API_UpdateActionType"></a>

Updates an action type that was created with any supported integration model, where the action type is to be used by customers of the action type provider. Use a JSON file with the action definition and `UpdateActionType` to provide the full structure.

## Request Syntax
<a name="API_UpdateActionType_RequestSyntax"></a>

```
{
   "actionType": { 
      "description": "{{string}}",
      "executor": { 
         "configuration": { 
            "jobWorkerExecutorConfiguration": { 
               "pollingAccounts": [ "{{string}}" ],
               "pollingServicePrincipals": [ "{{string}}" ]
            },
            "lambdaExecutorConfiguration": { 
               "lambdaFunctionArn": "{{string}}"
            }
         },
         "jobTimeout": {{number}},
         "policyStatementsTemplate": "{{string}}",
         "type": "{{string}}"
      },
      "id": { 
         "category": "{{string}}",
         "owner": "{{string}}",
         "provider": "{{string}}",
         "version": "{{string}}"
      },
      "inputArtifactDetails": { 
         "maximumCount": {{number}},
         "minimumCount": {{number}}
      },
      "outputArtifactDetails": { 
         "maximumCount": {{number}},
         "minimumCount": {{number}}
      },
      "permissions": { 
         "allowedAccounts": [ "{{string}}" ]
      },
      "properties": [ 
         { 
            "description": "{{string}}",
            "key": {{boolean}},
            "name": "{{string}}",
            "noEcho": {{boolean}},
            "optional": {{boolean}},
            "queryable": {{boolean}}
         }
      ],
      "urls": { 
         "configurationUrl": "{{string}}",
         "entityUrlTemplate": "{{string}}",
         "executionUrlTemplate": "{{string}}",
         "revisionUrlTemplate": "{{string}}"
      }
   }
}
```

## Request Parameters
<a name="API_UpdateActionType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [actionType](#API_UpdateActionType_RequestSyntax) **   <a name="CodePipeline-UpdateActionType-request-actionType"></a>
The action type definition for the action type to be updated.  
Type: [ActionTypeDeclaration](API_ActionTypeDeclaration.md) object  
Required: Yes

## Response Elements
<a name="API_UpdateActionType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateActionType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ActionTypeNotFoundException **   
The specified action type cannot be found.  
HTTP Status Code: 400

 ** RequestFailedException **   
The request failed because of an unknown error, exception, or failure.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateActionType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/UpdateActionType) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/UpdateActionType) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/UpdateActionType) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/UpdateActionType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/UpdateActionType) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/UpdateActionType) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/UpdateActionType) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/UpdateActionType) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/UpdateActionType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/UpdateActionType) 