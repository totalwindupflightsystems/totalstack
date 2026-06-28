---
id: "@specs/aws/quicksight/docs/API_DescribeDashboardDefinition"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDashboardDefinition"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeDashboardDefinition

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeDashboardDefinition
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDashboardDefinition
<a name="API_DescribeDashboardDefinition"></a>

Provides a detailed description of the definition of a dashboard.

**Note**  
If you do not need to know details about the content of a dashboard, for instance if you are trying to check the status of a recently created or updated dashboard, use the [https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDashboard.html](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDashboard.html) instead. 

## Request Syntax
<a name="API_DescribeDashboardDefinition_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/dashboards/{{DashboardId}}/definition?alias-name={{AliasName}}&version-number={{VersionNumber}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDashboardDefinition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AliasName](#API_DescribeDashboardDefinition_RequestSyntax) **   <a name="QS-DescribeDashboardDefinition-request-uri-AliasName"></a>
The alias name.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[\w\-]+|(\$LATEST)|(\$PUBLISHED)` 

 ** [AwsAccountId](#API_DescribeDashboardDefinition_RequestSyntax) **   <a name="QS-DescribeDashboardDefinition-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the dashboard that you're describing.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [DashboardId](#API_DescribeDashboardDefinition_RequestSyntax) **   <a name="QS-DescribeDashboardDefinition-request-uri-DashboardId"></a>
The ID for the dashboard.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [VersionNumber](#API_DescribeDashboardDefinition_RequestSyntax) **   <a name="QS-DescribeDashboardDefinition-request-uri-VersionNumber"></a>
The version number for the dashboard. If a version number isn't passed, the latest published dashboard version is described.   
Valid Range: Minimum value of 1.

## Request Body
<a name="API_DescribeDashboardDefinition_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDashboardDefinition_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "DashboardId": "string",
   "DashboardPublishOptions": { 
      "AdHocFilteringOption": { 
         "AvailabilityStatus": "string"
      },
      "DataPointDrillUpDownOption": { 
         "AvailabilityStatus": "string"
      },
      "DataPointMenuLabelOption": { 
         "AvailabilityStatus": "string"
      },
      "DataPointTooltipOption": { 
         "AvailabilityStatus": "string"
      },
      "DataQAEnabledOption": { 
         "AvailabilityStatus": "string"
      },
      "DataStoriesSharingOption": { 
         "AvailabilityStatus": "string"
      },
      "ExecutiveSummaryOption": { 
         "AvailabilityStatus": "string"
      },
      "ExportToCSVOption": { 
         "AvailabilityStatus": "string"
      },
      "ExportWithHiddenFieldsOption": { 
         "AvailabilityStatus": "string"
      },
      "QuickSuiteActionsOption": { 
         "AvailabilityStatus": "string"
      },
      "SheetControlsOption": { 
         "VisibilityState": "string"
      },
      "SheetLayoutElementMaximizationOption": { 
         "AvailabilityStatus": "string"
      },
      "VisualAxisSortOption": { 
         "AvailabilityStatus": "string"
      },
      "VisualMenuOption": { 
         "AvailabilityStatus": "string"
      },
      "VisualPublishOptions": { 
         "ExportHiddenFieldsOption": { 
            "AvailabilityStatus": "string"
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
         "ExcludedDataSetArns": [ "string" ],
         "QBusinessInsightsStatus": "string",
         "Timezone": "string",
         "WeekStart": "string"
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
   "Errors": [ 
      { 
         "Message": "string",
         "Type": "string",
         "ViolatedEntities": [ 
            { 
               "Path": "string"
            }
         ]
      }
   ],
   "Name": "string",
   "RequestId": "string",
   "ResourceStatus": "string",
   "ThemeArn": "string"
}
```

## Response Elements
<a name="API_DescribeDashboardDefinition_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeDashboardDefinition_ResponseSyntax) **   <a name="QS-DescribeDashboardDefinition-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [DashboardId](#API_DescribeDashboardDefinition_ResponseSyntax) **   <a name="QS-DescribeDashboardDefinition-response-DashboardId"></a>
The ID of the dashboard described.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

 ** [DashboardPublishOptions](#API_DescribeDashboardDefinition_ResponseSyntax) **   <a name="QS-DescribeDashboardDefinition-response-DashboardPublishOptions"></a>
Options for publishing the dashboard:  
+  `AvailabilityStatus` for `AdHocFilteringOption` - This status can be either `ENABLED` or `DISABLED`. When this is set to `DISABLED`, Amazon Quick Sight disables the left filter pane on the published dashboard, which can be used for ad hoc (one-time) filtering. This option is `ENABLED` by default. 
+  `AvailabilityStatus` for `ExportToCSVOption` - This status can be either `ENABLED` or `DISABLED`. The visual option to export data to .CSV format isn't enabled when this is set to `DISABLED`. This option is `ENABLED` by default. 
+  `VisibilityState` for `SheetControlsOption` - This visibility state can be either `COLLAPSED` or `EXPANDED`. This option is `COLLAPSED` by default. 
+  `AvailabilityStatus` for `QuickSuiteActionsOption` - This status can be either `ENABLED` or `DISABLED`. Features related to Actions in Amazon Quick Suite on dashboards are disabled when this is set to `DISABLED`. This option is `DISABLED` by default.
+  `AvailabilityStatus` for `ExecutiveSummaryOption` - This status can be either `ENABLED` or `DISABLED`. The option to build an executive summary is disabled when this is set to `DISABLED`. This option is `ENABLED` by default.
+  `AvailabilityStatus` for `DataStoriesSharingOption` - This status can be either `ENABLED` or `DISABLED`. The option to share a data story is disabled when this is set to `DISABLED`. This option is `ENABLED` by default.
Type: [DashboardPublishOptions](API_DashboardPublishOptions.md) object

 ** [Definition](#API_DescribeDashboardDefinition_ResponseSyntax) **   <a name="QS-DescribeDashboardDefinition-response-Definition"></a>
The definition of a dashboard.  
A definition is the data model of all features in a Dashboard, Template, or Analysis.  
Type: [DashboardVersionDefinition](API_DashboardVersionDefinition.md) object

 ** [Errors](#API_DescribeDashboardDefinition_ResponseSyntax) **   <a name="QS-DescribeDashboardDefinition-response-Errors"></a>
Errors associated with this dashboard version.  
Type: Array of [DashboardError](API_DashboardError.md) objects  
Array Members: Minimum number of 1 item.

 ** [Name](#API_DescribeDashboardDefinition_ResponseSyntax) **   <a name="QS-DescribeDashboardDefinition-response-Name"></a>
The display name of the dashboard.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [RequestId](#API_DescribeDashboardDefinition_ResponseSyntax) **   <a name="QS-DescribeDashboardDefinition-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [ResourceStatus](#API_DescribeDashboardDefinition_ResponseSyntax) **   <a name="QS-DescribeDashboardDefinition-response-ResourceStatus"></a>
Status associated with the dashboard version.  
+  `CREATION_IN_PROGRESS` 
+  `CREATION_SUCCESSFUL` 
+  `CREATION_FAILED` 
+  `UPDATE_IN_PROGRESS` 
+  `UPDATE_SUCCESSFUL` 
+  `UPDATE_FAILED` 
+  `DELETED` 
Type: String  
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED` 

 ** [ThemeArn](#API_DescribeDashboardDefinition_ResponseSyntax) **   <a name="QS-DescribeDashboardDefinition-response-ThemeArn"></a>
The ARN of the theme of the dashboard.  
Type: String

## Errors
<a name="API_DescribeDashboardDefinition_Errors"></a>

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
<a name="API_DescribeDashboardDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeDashboardDefinition) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeDashboardDefinition) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeDashboardDefinition) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeDashboardDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeDashboardDefinition) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeDashboardDefinition) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeDashboardDefinition) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeDashboardDefinition) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeDashboardDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeDashboardDefinition) 