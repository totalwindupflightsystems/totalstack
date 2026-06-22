---
id: "@specs/aws/codepipeline/docs/API_CreateCustomActionType"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateCustomActionType"
status: active
depends_on:
  - "@specs/aws/codepipeline/meta"
---

# CreateCustomActionType

> **source:** AWS Documentation
> **spec:id:** @specs/aws/codepipeline/docs/API_CreateCustomActionType
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateCustomActionType
<a name="API_CreateCustomActionType"></a>

Creates a new custom action that can be used in all pipelines associated with the AWS account. Only used for custom actions.

## Request Syntax
<a name="API_CreateCustomActionType_RequestSyntax"></a>

```
{
   "category": "{{string}}",
   "configurationProperties": [ 
      { 
         "description": "{{string}}",
         "key": {{boolean}},
         "name": "{{string}}",
         "queryable": {{boolean}},
         "required": {{boolean}},
         "secret": {{boolean}},
         "type": "{{string}}"
      }
   ],
   "inputArtifactDetails": { 
      "maximumCount": {{number}},
      "minimumCount": {{number}}
   },
   "outputArtifactDetails": { 
      "maximumCount": {{number}},
      "minimumCount": {{number}}
   },
   "provider": "{{string}}",
   "settings": { 
      "entityUrlTemplate": "{{string}}",
      "executionUrlTemplate": "{{string}}",
      "revisionUrlTemplate": "{{string}}",
      "thirdPartyConfigurationUrl": "{{string}}"
   },
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "version": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateCustomActionType_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [category](#API_CreateCustomActionType_RequestSyntax) **   <a name="CodePipeline-CreateCustomActionType-request-category"></a>
The category of the custom action, such as a build action or a test action.  
Type: String  
Valid Values: `Source | Build | Deploy | Test | Invoke | Approval | Compute`   
Required: Yes

 ** [configurationProperties](#API_CreateCustomActionType_RequestSyntax) **   <a name="CodePipeline-CreateCustomActionType-request-configurationProperties"></a>
The configuration properties for the custom action.  
You can refer to a name in the configuration properties of the custom action within the URL templates by following the format of {Config:name}, as long as the configuration property is both required and not secret. For more information, see [Create a Custom Action for a Pipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/how-to-create-custom-action.html).
Type: Array of [ActionConfigurationProperty](API_ActionConfigurationProperty.md) objects  
Array Members: Maximum number of 10 items.  
Required: No

 ** [inputArtifactDetails](#API_CreateCustomActionType_RequestSyntax) **   <a name="CodePipeline-CreateCustomActionType-request-inputArtifactDetails"></a>
The details of the input artifact for the action, such as its commit ID.  
Type: [ArtifactDetails](API_ArtifactDetails.md) object  
Required: Yes

 ** [outputArtifactDetails](#API_CreateCustomActionType_RequestSyntax) **   <a name="CodePipeline-CreateCustomActionType-request-outputArtifactDetails"></a>
The details of the output artifact of the action, such as its commit ID.  
Type: [ArtifactDetails](API_ArtifactDetails.md) object  
Required: Yes

 ** [provider](#API_CreateCustomActionType_RequestSyntax) **   <a name="CodePipeline-CreateCustomActionType-request-provider"></a>
The provider of the service used in the custom action, such as CodeDeploy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 35.  
Pattern: `[0-9A-Za-z_-]+`   
Required: Yes

 ** [settings](#API_CreateCustomActionType_RequestSyntax) **   <a name="CodePipeline-CreateCustomActionType-request-settings"></a>
URLs that provide users information about this custom action.  
Type: [ActionTypeSettings](API_ActionTypeSettings.md) object  
Required: No

 ** [tags](#API_CreateCustomActionType_RequestSyntax) **   <a name="CodePipeline-CreateCustomActionType-request-tags"></a>
The tags for the custom action.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** [version](#API_CreateCustomActionType_RequestSyntax) **   <a name="CodePipeline-CreateCustomActionType-request-version"></a>
The version identifier of the custom action.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 9.  
Pattern: `[0-9A-Za-z_-]+`   
Required: Yes

## Response Syntax
<a name="API_CreateCustomActionType_ResponseSyntax"></a>

```
{
   "actionType": { 
      "actionConfigurationProperties": [ 
         { 
            "description": "string",
            "key": boolean,
            "name": "string",
            "queryable": boolean,
            "required": boolean,
            "secret": boolean,
            "type": "string"
         }
      ],
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
      "settings": { 
         "entityUrlTemplate": "string",
         "executionUrlTemplate": "string",
         "revisionUrlTemplate": "string",
         "thirdPartyConfigurationUrl": "string"
      }
   },
   "tags": [ 
      { 
         "key": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateCustomActionType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actionType](#API_CreateCustomActionType_ResponseSyntax) **   <a name="CodePipeline-CreateCustomActionType-response-actionType"></a>
Returns information about the details of an action type.  
Type: [ActionType](API_ActionType.md) object

 ** [tags](#API_CreateCustomActionType_ResponseSyntax) **   <a name="CodePipeline-CreateCustomActionType-response-tags"></a>
Specifies the tags applied to the custom action.  
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_CreateCustomActionType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **   
Unable to modify the tag due to a simultaneous update request.  
HTTP Status Code: 400

 ** InvalidTagsException **   
The specified resource tags are invalid.  
HTTP Status Code: 400

 ** LimitExceededException **   
The number of pipelines associated with the AWS account has exceeded the limit allowed for the account.  
HTTP Status Code: 400

 ** TooManyTagsException **   
The tags limit for a resource has been exceeded.  
HTTP Status Code: 400

 ** ValidationException **   
The validation was specified in an invalid format.  
HTTP Status Code: 400

## Examples
<a name="API_CreateCustomActionType_Examples"></a>

### Example
<a name="API_CreateCustomActionType_Example_1"></a>

This example illustrates one usage of CreateCustomActionType.

#### Sample Request
<a name="API_CreateCustomActionType_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: codepipeline.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: 665
X-Amz-Target: CodePipeline_20150709.CreateCustomActionType
X-Amz-Date: 20160707T203658Z
User-Agent: aws-cli/1.7.38 Python/2.7.9 Windows/7
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 Credential=AKIAI44QH8DHBEXAMPLE/20160707/us-east-1/codepipeline/aws4_request, SignedHeaders=content-type;host;user-agent;x-amz-date;x-amz-target, Signature=8d9b5998EXAMPLE

{
  "category": "Build",
  "settings": {
    "entityUrlTemplate": "https://192.0.2.4/job/{Config:ProjectName}/",
    "executionUrlTemplate": "https://192.0.2.4/job/{Config:ProjectName}/lastSuccessfulBuild/{ExternalExecutionId}/"
  },
  "configurationProperties": [
    {
      "description": "The name of the build project must be provided when this action is added to the pipeline.",
      "required": true,
      "secret": false,
      "key": true,
      "type": "String",
      "queryable": false,
      "name": "ProjectName"
    }
  ],
  "version": "1",
  "provider": "JenkinsProviderName",
  "inputArtifactDetails": {
    "maximumCount": 1,
    "minimumCount": 0
  },
  "outputArtifactDetails": {
    "maximumCount": 1,
    "minimumCount": 0
  }
}
```

#### Sample Response
<a name="API_CreateCustomActionType_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: 620484b7-88cb-11e5-b497-75c49EXAMPLE
Content-Type: application/x-amz-json-1.1
Content-Length: 683

{
  "actionType": {
    "actionConfigurationProperties": [
      {
        "description": "The name of the build project must be provided when this action is added to the pipeline.",
        "key": true,
        "name": "ProjectName",
        "queryable": false,
        "required": true,
        "secret": false
      }
    ],
    "id": {
      "__type": "ActionTypeId",
      "category": "Build",
      "owner": "Custom",
      "provider": "JenkinsProviderName",
      "version": "1"
    },
    "inputArtifactDetails": {
      "maximumCount": 1,
      "minimumCount": 0
    },
    "outputArtifactDetails": {
      "maximumCount": 1,
      "minimumCount": 0
    },
    "settings": {
      "entityUrlTemplate": "https://192.0.2.4/job/{Config:ProjectName}/",
      "executionUrlTemplate": "https://192.0.2.4/job/{Config:ProjectName}/lastSuccessfulBuild/{ExternalExecutionId}/"
    }
  }
}
```

## See Also
<a name="API_CreateCustomActionType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codepipeline-2015-07-09/CreateCustomActionType) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codepipeline-2015-07-09/CreateCustomActionType) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/CreateCustomActionType) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codepipeline-2015-07-09/CreateCustomActionType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/CreateCustomActionType) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codepipeline-2015-07-09/CreateCustomActionType) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codepipeline-2015-07-09/CreateCustomActionType) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codepipeline-2015-07-09/CreateCustomActionType) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/codepipeline-2015-07-09/CreateCustomActionType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/CreateCustomActionType) 