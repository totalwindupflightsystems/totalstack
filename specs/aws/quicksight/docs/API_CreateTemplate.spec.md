---
id: "@specs/aws/quicksight/docs/API_CreateTemplate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateTemplate"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateTemplate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateTemplate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateTemplate
<a name="API_CreateTemplate"></a>

Creates a template either from a `TemplateDefinition` or from an existing Quick Sight analysis or template. You can use the resulting template to create additional dashboards, templates, or analyses.

A *template* is an entity in Quick Sight that encapsulates the metadata required to create an analysis and that you can use to create s dashboard. A template adds a layer of abstraction by using placeholders to replace the dataset associated with the analysis. You can use templates to create dashboards by replacing dataset placeholders with datasets that follow the same schema that was used to create the source analysis and template.

## Request Syntax
<a name="API_CreateTemplate_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/templates/{{TemplateId}} HTTP/1.1
Content-type: application/json

{
   "Definition": { 
      "AnalysisDefaults": { 
         "DefaultNewSheetConfiguration": { ... }
      },
      "CalculatedFields": [ 
         { ... }
      ],
      "ColumnConfigurations": [ 
         { ... }
      ],
      "DataSetConfigurations": [ 
         { ... }
      ],
      "FilterGroups": [ 
         { ... }
      ],
      "Options": { 
         "CustomActionDefaults": { ... },
         "ExcludedDataSetArns": [ "{{string}}" ],
         "QBusinessInsightsStatus": "{{string}}",
         "Timezone": "{{string}}",
         "WeekStart": "{{string}}"
      },
      "ParameterDeclarations": [ 
         { ... }
      ],
      "QueryExecutionOptions": { 
         "QueryExecutionMode": "{{string}}"
      },
      "Sheets": [ 
         { ... }
      ],
      "StaticFiles": [ 
         { ... }
      ],
      "TooltipSheets": [ 
         { ... }
      ]
   },
   "Name": "{{string}}",
   "Permissions": [ 
      { 
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ],
   "SourceEntity": { 
      "SourceAnalysis": { 
         "Arn": "{{string}}",
         "DataSetReferences": [ 
            { 
               "DataSetArn": "{{string}}",
               "DataSetPlaceholder": "{{string}}"
            }
         ]
      },
      "SourceTemplate": { 
         "Arn": "{{string}}"
      }
   },
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "ValidationStrategy": { 
      "Mode": "{{string}}"
   },
   "VersionDescription": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateTemplate_RequestSyntax) **   <a name="QS-CreateTemplate-request-uri-AwsAccountId"></a>
The ID for the AWS account that the group is in. You use the ID for the AWS account that contains your Amazon Quick Sight account.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [TemplateId](#API_CreateTemplate_RequestSyntax) **   <a name="QS-CreateTemplate-request-uri-TemplateId"></a>
An ID for the template that you want to create. This template is unique per AWS Region; in each AWS account.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

## Request Body
<a name="API_CreateTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Definition](#API_CreateTemplate_RequestSyntax) **   <a name="QS-CreateTemplate-request-Definition"></a>
The definition of a template.  
A definition is the data model of all features in a Dashboard, Template, or Analysis.  
Either a `SourceEntity` or a `Definition` must be provided in order for the request to be valid.  
Type: [TemplateVersionDefinition](API_TemplateVersionDefinition.md) object  
Required: No

 ** [Name](#API_CreateTemplate_RequestSyntax) **   <a name="QS-CreateTemplate-request-Name"></a>
A display name for the template.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: No

 ** [Permissions](#API_CreateTemplate_RequestSyntax) **   <a name="QS-CreateTemplate-request-Permissions"></a>
A list of resource permissions to be set on the template.   
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 64 items.  
Required: No

 ** [SourceEntity](#API_CreateTemplate_RequestSyntax) **   <a name="QS-CreateTemplate-request-SourceEntity"></a>
The entity that you are using as a source when you create the template. In `SourceEntity`, you specify the type of object you're using as source: `SourceTemplate` for a template or `SourceAnalysis` for an analysis. Both of these require an Amazon Resource Name (ARN). For `SourceTemplate`, specify the ARN of the source template. For `SourceAnalysis`, specify the ARN of the source analysis. The `SourceTemplate` ARN can contain any AWS account and any Quick Sight-supported AWS Region.   
Use the `DataSetReferences` entity within `SourceTemplate` or `SourceAnalysis` to list the replacement datasets for the placeholders listed in the original. The schema in each dataset must match its placeholder.   
Either a `SourceEntity` or a `Definition` must be provided in order for the request to be valid.  
Type: [TemplateSourceEntity](API_TemplateSourceEntity.md) object  
Required: No

 ** [Tags](#API_CreateTemplate_RequestSyntax) **   <a name="QS-CreateTemplate-request-Tags"></a>
Contains a map of the key-value pairs for the resource tag or tags assigned to the resource.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** [ValidationStrategy](#API_CreateTemplate_RequestSyntax) **   <a name="QS-CreateTemplate-request-ValidationStrategy"></a>
TThe option to relax the validation needed to create a template with definition objects. This skips the validation step for specific errors.  
Type: [ValidationStrategy](API_ValidationStrategy.md) object  
Required: No

 ** [VersionDescription](#API_CreateTemplate_RequestSyntax) **   <a name="QS-CreateTemplate-request-VersionDescription"></a>
A description of the current template version being created. This API operation creates the first version of the template. Every time `UpdateTemplate` is called, a new version is created. Each version of the template maintains a description of the version in the `VersionDescription` field.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Required: No

## Response Syntax
<a name="API_CreateTemplate_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "CreationStatus": "string",
   "RequestId": "string",
   "TemplateId": "string",
   "VersionArn": "string"
}
```

## Response Elements
<a name="API_CreateTemplate_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateTemplate_ResponseSyntax) **   <a name="QS-CreateTemplate-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateTemplate_ResponseSyntax) **   <a name="QS-CreateTemplate-response-Arn"></a>
The ARN for the template.  
Type: String

 ** [CreationStatus](#API_CreateTemplate_ResponseSyntax) **   <a name="QS-CreateTemplate-response-CreationStatus"></a>
The template creation status.  
Type: String  
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED` 

 ** [RequestId](#API_CreateTemplate_ResponseSyntax) **   <a name="QS-CreateTemplate-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [TemplateId](#API_CreateTemplate_ResponseSyntax) **   <a name="QS-CreateTemplate-response-TemplateId"></a>
The ID of the template.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

 ** [VersionArn](#API_CreateTemplate_ResponseSyntax) **   <a name="QS-CreateTemplate-response-VersionArn"></a>
The ARN for the template, including the version information of the first version.  
Type: String

## Errors
<a name="API_CreateTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

 ** ConflictException **   
Updating or deleting a resource can cause an inconsistent state.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **   
An internal failure occurred.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **   
One or more parameters has a value that isn't valid.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **   
A limit is exceeded.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
Limit exceeded.
HTTP Status Code: 409

 ** ResourceExistsException **   
The resource specified already exists.     
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 409

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedUserEditionException **   
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_CreateTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateTemplate) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateTemplate) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateTemplate) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateTemplate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateTemplate) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateTemplate) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateTemplate) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateTemplate) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateTemplate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateTemplate) 