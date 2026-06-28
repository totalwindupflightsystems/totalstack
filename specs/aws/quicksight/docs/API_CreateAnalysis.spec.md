---
id: "@specs/aws/quicksight/docs/API_CreateAnalysis"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateAnalysis"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateAnalysis

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateAnalysis
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateAnalysis
<a name="API_CreateAnalysis"></a>

Creates an analysis in Amazon Quick Sight. Analyses can be created either from a template or from an `AnalysisDefinition`.

## Request Syntax
<a name="API_CreateAnalysis_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/analyses/{{AnalysisId}} HTTP/1.1
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
      "DataSetIdentifierDeclarations": [ 
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
   "FolderArns": [ "{{string}}" ],
   "Name": "{{string}}",
   "Parameters": { 
      "DateTimeParameters": [ 
         { 
            "Name": "{{string}}",
            "Values": [ {{number}} ]
         }
      ],
      "DecimalParameters": [ 
         { 
            "Name": "{{string}}",
            "Values": [ {{number}} ]
         }
      ],
      "IntegerParameters": [ 
         { 
            "Name": "{{string}}",
            "Values": [ {{number}} ]
         }
      ],
      "StringParameters": [ 
         { 
            "Name": "{{string}}",
            "Values": [ "{{string}}" ]
         }
      ]
   },
   "Permissions": [ 
      { 
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ],
   "SourceEntity": { 
      "SourceTemplate": { 
         "Arn": "{{string}}",
         "DataSetReferences": [ 
            { 
               "DataSetArn": "{{string}}",
               "DataSetPlaceholder": "{{string}}"
            }
         ]
      }
   },
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "ThemeArn": "{{string}}",
   "ValidationStrategy": { 
      "Mode": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateAnalysis_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AnalysisId](#API_CreateAnalysis_RequestSyntax) **   <a name="QS-CreateAnalysis-request-uri-AnalysisId"></a>
The ID for the analysis that you're creating. This ID displays in the URL of the analysis.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [AwsAccountId](#API_CreateAnalysis_RequestSyntax) **   <a name="QS-CreateAnalysis-request-uri-AwsAccountId"></a>
The ID of the AWS account where you are creating an analysis.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_CreateAnalysis_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_CreateAnalysis_RequestSyntax) **   <a name="QS-CreateAnalysis-request-Name"></a>
A descriptive name for the analysis that you're creating. This name displays for the analysis in the Amazon Quick Sight console.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: Yes

 ** [Definition](#API_CreateAnalysis_RequestSyntax) **   <a name="QS-CreateAnalysis-request-Definition"></a>
The definition of an analysis.  
A definition is the data model of all features in a Dashboard, Template, or Analysis.  
Either a `SourceEntity` or a `Definition` must be provided in order for the request to be valid.  
Type: [AnalysisDefinition](API_AnalysisDefinition.md) object  
Required: No

 ** [FolderArns](#API_CreateAnalysis_RequestSyntax) **   <a name="QS-CreateAnalysis-request-FolderArns"></a>
When you create the analysis, Amazon Quick Sight adds the analysis to these folders.  
Type: Array of strings  
Array Members: Maximum number of 1 item.  
Required: No

 ** [Parameters](#API_CreateAnalysis_RequestSyntax) **   <a name="QS-CreateAnalysis-request-Parameters"></a>
The parameter names and override values that you want to use. An analysis can have any parameter type, and some parameters might accept multiple values.   
Type: [Parameters](API_Parameters.md) object  
Required: No

 ** [Permissions](#API_CreateAnalysis_RequestSyntax) **   <a name="QS-CreateAnalysis-request-Permissions"></a>
A structure that describes the principals and the resource-level permissions on an analysis. You can use the `Permissions` structure to grant permissions by providing a list of AWS Identity and Access Management (IAM) action information for each principal listed by Amazon Resource Name (ARN).   
To specify no permissions, omit `Permissions`.  
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 64 items.  
Required: No

 ** [SourceEntity](#API_CreateAnalysis_RequestSyntax) **   <a name="QS-CreateAnalysis-request-SourceEntity"></a>
A source entity to use for the analysis that you're creating. This metadata structure contains details that describe a source template and one or more datasets.  
Either a `SourceEntity` or a `Definition` must be provided in order for the request to be valid.  
Type: [AnalysisSourceEntity](API_AnalysisSourceEntity.md) object  
Required: No

 ** [Tags](#API_CreateAnalysis_RequestSyntax) **   <a name="QS-CreateAnalysis-request-Tags"></a>
Contains a map of the key-value pairs for the resource tag or tags assigned to the analysis.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** [ThemeArn](#API_CreateAnalysis_RequestSyntax) **   <a name="QS-CreateAnalysis-request-ThemeArn"></a>
The ARN for the theme to apply to the analysis that you're creating. To see the theme in the Amazon Quick Sight console, make sure that you have access to it.  
Type: String  
Required: No

 ** [ValidationStrategy](#API_CreateAnalysis_RequestSyntax) **   <a name="QS-CreateAnalysis-request-ValidationStrategy"></a>
The option to relax the validation needed to create an analysis with definition objects. This skips the validation step for specific errors.  
Type: [ValidationStrategy](API_ValidationStrategy.md) object  
Required: No

## Response Syntax
<a name="API_CreateAnalysis_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AnalysisId": "string",
   "Arn": "string",
   "CreationStatus": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_CreateAnalysis_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateAnalysis_ResponseSyntax) **   <a name="QS-CreateAnalysis-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AnalysisId](#API_CreateAnalysis_ResponseSyntax) **   <a name="QS-CreateAnalysis-response-AnalysisId"></a>
The ID of the analysis.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

 ** [Arn](#API_CreateAnalysis_ResponseSyntax) **   <a name="QS-CreateAnalysis-response-Arn"></a>
The ARN for the analysis.  
Type: String

 ** [CreationStatus](#API_CreateAnalysis_ResponseSyntax) **   <a name="QS-CreateAnalysis-response-CreationStatus"></a>
The status of the creation of the analysis.   
Type: String  
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED` 

 ** [RequestId](#API_CreateAnalysis_ResponseSyntax) **   <a name="QS-CreateAnalysis-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_CreateAnalysis_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_CreateAnalysis_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateAnalysis) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateAnalysis) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateAnalysis) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateAnalysis) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateAnalysis) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateAnalysis) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateAnalysis) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateAnalysis) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateAnalysis) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateAnalysis) 