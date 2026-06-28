---
id: "@specs/aws/quicksight/docs/API_CreateDashboard"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateDashboard"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateDashboard

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateDashboard
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateDashboard
<a name="API_CreateDashboard"></a>

Creates a dashboard from either a template or directly with a `DashboardDefinition`. To first create a template, see the ` [CreateTemplate](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateTemplate.html) ` API operation.

A dashboard is an entity in Amazon Quick Sight that identifies Amazon Quick Sight reports, created from analyses. You can share Amazon Quick Sight dashboards. With the right permissions, you can create scheduled email reports from them. If you have the correct permissions, you can create a dashboard from a template that exists in a different AWS account.

## Request Syntax
<a name="API_CreateDashboard_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/dashboards/{{DashboardId}} HTTP/1.1
Content-type: application/json

{
   "DashboardPublishOptions": { 
      "AdHocFilteringOption": { 
         "AvailabilityStatus": "{{string}}"
      },
      "DataPointDrillUpDownOption": { 
         "AvailabilityStatus": "{{string}}"
      },
      "DataPointMenuLabelOption": { 
         "AvailabilityStatus": "{{string}}"
      },
      "DataPointTooltipOption": { 
         "AvailabilityStatus": "{{string}}"
      },
      "DataQAEnabledOption": { 
         "AvailabilityStatus": "{{string}}"
      },
      "DataStoriesSharingOption": { 
         "AvailabilityStatus": "{{string}}"
      },
      "ExecutiveSummaryOption": { 
         "AvailabilityStatus": "{{string}}"
      },
      "ExportToCSVOption": { 
         "AvailabilityStatus": "{{string}}"
      },
      "ExportWithHiddenFieldsOption": { 
         "AvailabilityStatus": "{{string}}"
      },
      "QuickSuiteActionsOption": { 
         "AvailabilityStatus": "{{string}}"
      },
      "SheetControlsOption": { 
         "VisibilityState": "{{string}}"
      },
      "SheetLayoutElementMaximizationOption": { 
         "AvailabilityStatus": "{{string}}"
      },
      "VisualAxisSortOption": { 
         "AvailabilityStatus": "{{string}}"
      },
      "VisualMenuOption": { 
         "AvailabilityStatus": "{{string}}"
      },
      "VisualPublishOptions": { 
         "ExportHiddenFieldsOption": { 
            "AvailabilityStatus": "{{string}}"
         }
      }
   },
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
   "LinkEntities": [ "{{string}}" ],
   "LinkSharingConfiguration": { 
      "Permissions": [ 
         { 
            "Actions": [ "{{string}}" ],
            "Principal": "{{string}}"
         }
      ]
   },
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
   },
   "VersionDescription": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateDashboard_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateDashboard_RequestSyntax) **   <a name="QS-CreateDashboard-request-uri-AwsAccountId"></a>
The ID of the AWS account where you want to create the dashboard.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [DashboardId](#API_CreateDashboard_RequestSyntax) **   <a name="QS-CreateDashboard-request-uri-DashboardId"></a>
The ID for the dashboard, also added to the IAM policy.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

## Request Body
<a name="API_CreateDashboard_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_CreateDashboard_RequestSyntax) **   <a name="QS-CreateDashboard-request-Name"></a>
The display name of the dashboard.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: Yes

 ** [DashboardPublishOptions](#API_CreateDashboard_RequestSyntax) **   <a name="QS-CreateDashboard-request-DashboardPublishOptions"></a>
Options for publishing the dashboard when you create it:  
+  `AvailabilityStatus` for `AdHocFilteringOption` - This status can be either `ENABLED` or `DISABLED`. When this is set to `DISABLED`, Amazon Quick Sight disables the left filter pane on the published dashboard, which can be used for ad hoc (one-time) filtering. This option is `ENABLED` by default. 
+  `AvailabilityStatus` for `ExportToCSVOption` - This status can be either `ENABLED` or `DISABLED`. The visual option to export data to .CSV format isn't enabled when this is set to `DISABLED`. This option is `ENABLED` by default. 
+  `VisibilityState` for `SheetControlsOption` - This visibility state can be either `COLLAPSED` or `EXPANDED`. This option is `COLLAPSED` by default. 
+  `AvailabilityStatus` for `QuickSuiteActionsOption` - This status can be either `ENABLED` or `DISABLED`. Features related to Actions in Amazon Quick Suite on dashboards are disabled when this is set to `DISABLED`. This option is `DISABLED` by default.
+  `AvailabilityStatus` for `ExecutiveSummaryOption` - This status can be either `ENABLED` or `DISABLED`. The option to build an executive summary is disabled when this is set to `DISABLED`. This option is `ENABLED` by default.
+  `AvailabilityStatus` for `DataStoriesSharingOption` - This status can be either `ENABLED` or `DISABLED`. The option to share a data story is disabled when this is set to `DISABLED`. This option is `ENABLED` by default.
Type: [DashboardPublishOptions](API_DashboardPublishOptions.md) object  
Required: No

 ** [Definition](#API_CreateDashboard_RequestSyntax) **   <a name="QS-CreateDashboard-request-Definition"></a>
The definition of a dashboard.  
A definition is the data model of all features in a Dashboard, Template, or Analysis.  
Either a `SourceEntity` or a `Definition` must be provided in order for the request to be valid.  
Type: [DashboardVersionDefinition](API_DashboardVersionDefinition.md) object  
Required: No

 ** [FolderArns](#API_CreateDashboard_RequestSyntax) **   <a name="QS-CreateDashboard-request-FolderArns"></a>
When you create the dashboard, Amazon Quick Sight adds the dashboard to these folders.  
Type: Array of strings  
Array Members: Maximum number of 1 item.  
Required: No

 ** [LinkEntities](#API_CreateDashboard_RequestSyntax) **   <a name="QS-CreateDashboard-request-LinkEntities"></a>
A list of analysis Amazon Resource Names (ARNs) to be linked to the dashboard.  
Type: Array of strings  
Array Members: Maximum number of 5 items.  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^arn:aws[\w\-]*:quicksight:[\w\-]+:\d+:analysis/[\w\-]{1,512}`   
Required: No

 ** [LinkSharingConfiguration](#API_CreateDashboard_RequestSyntax) **   <a name="QS-CreateDashboard-request-LinkSharingConfiguration"></a>
A structure that contains the permissions of a shareable link to the dashboard.  
Type: [LinkSharingConfiguration](API_LinkSharingConfiguration.md) object  
Required: No

 ** [Parameters](#API_CreateDashboard_RequestSyntax) **   <a name="QS-CreateDashboard-request-Parameters"></a>
The parameters for the creation of the dashboard, which you want to use to override the default settings. A dashboard can have any type of parameters, and some parameters might accept multiple values.   
Type: [Parameters](API_Parameters.md) object  
Required: No

 ** [Permissions](#API_CreateDashboard_RequestSyntax) **   <a name="QS-CreateDashboard-request-Permissions"></a>
A structure that contains the permissions of the dashboard. You can use this structure for granting permissions by providing a list of IAM action information for each principal ARN.   
To specify no permissions, omit the permissions list.  
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 64 items.  
Required: No

 ** [SourceEntity](#API_CreateDashboard_RequestSyntax) **   <a name="QS-CreateDashboard-request-SourceEntity"></a>
The entity that you are using as a source when you create the dashboard. In `SourceEntity`, you specify the type of object you're using as source. You can only create a dashboard from a template, so you use a `SourceTemplate` entity. If you need to create a dashboard from an analysis, first convert the analysis to a template by using the ` [CreateTemplate](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateTemplate.html) ` API operation. For `SourceTemplate`, specify the Amazon Resource Name (ARN) of the source template. The `SourceTemplate`ARN can contain any AWS account and any Amazon Quick Sight-supported AWS Region.   
Use the `DataSetReferences` entity within `SourceTemplate` to list the replacement datasets for the placeholders listed in the original. The schema in each dataset must match its placeholder.   
Either a `SourceEntity` or a `Definition` must be provided in order for the request to be valid.  
Type: [DashboardSourceEntity](API_DashboardSourceEntity.md) object  
Required: No

 ** [Tags](#API_CreateDashboard_RequestSyntax) **   <a name="QS-CreateDashboard-request-Tags"></a>
Contains a map of the key-value pairs for the resource tag or tags assigned to the dashboard.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** [ThemeArn](#API_CreateDashboard_RequestSyntax) **   <a name="QS-CreateDashboard-request-ThemeArn"></a>
The Amazon Resource Name (ARN) of the theme that is being used for this dashboard. If you add a value for this field, it overrides the value that is used in the source entity. The theme ARN must exist in the same AWS account where you create the dashboard.  
Type: String  
Required: No

 ** [ValidationStrategy](#API_CreateDashboard_RequestSyntax) **   <a name="QS-CreateDashboard-request-ValidationStrategy"></a>
The option to relax the validation needed to create a dashboard with definition objects. This option skips the validation step for specific errors.  
Type: [ValidationStrategy](API_ValidationStrategy.md) object  
Required: No

 ** [VersionDescription](#API_CreateDashboard_RequestSyntax) **   <a name="QS-CreateDashboard-request-VersionDescription"></a>
A description for the first version of the dashboard being created.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Required: No

## Response Syntax
<a name="API_CreateDashboard_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "CreationStatus": "string",
   "DashboardId": "string",
   "RequestId": "string",
   "VersionArn": "string"
}
```

## Response Elements
<a name="API_CreateDashboard_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateDashboard_ResponseSyntax) **   <a name="QS-CreateDashboard-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateDashboard_ResponseSyntax) **   <a name="QS-CreateDashboard-response-Arn"></a>
The ARN of the dashboard.  
Type: String

 ** [CreationStatus](#API_CreateDashboard_ResponseSyntax) **   <a name="QS-CreateDashboard-response-CreationStatus"></a>
The status of the dashboard creation request.  
Type: String  
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED` 

 ** [DashboardId](#API_CreateDashboard_ResponseSyntax) **   <a name="QS-CreateDashboard-response-DashboardId"></a>
The ID for the dashboard.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

 ** [RequestId](#API_CreateDashboard_ResponseSyntax) **   <a name="QS-CreateDashboard-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [VersionArn](#API_CreateDashboard_ResponseSyntax) **   <a name="QS-CreateDashboard-response-VersionArn"></a>
The ARN of the dashboard, including the version number of the first version that is created.  
Type: String

## Errors
<a name="API_CreateDashboard_Errors"></a>

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
<a name="API_CreateDashboard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateDashboard) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateDashboard) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateDashboard) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateDashboard) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateDashboard) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateDashboard) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateDashboard) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateDashboard) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateDashboard) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateDashboard) 