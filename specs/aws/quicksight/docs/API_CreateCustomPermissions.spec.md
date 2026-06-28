---
id: "@specs/aws/quicksight/docs/API_CreateCustomPermissions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateCustomPermissions"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateCustomPermissions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateCustomPermissions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateCustomPermissions
<a name="API_CreateCustomPermissions"></a>

Creates a custom permissions profile.

## Request Syntax
<a name="API_CreateCustomPermissions_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/custom-permissions HTTP/1.1
Content-type: application/json

{
   "Capabilities": { 
      "AccessAppsNativeDataStore": "{{string}}",
      "Action": "{{string}}",
      "AddOrRunAnomalyDetectionForAnalyses": "{{string}}",
      "AmazonBedrockARSAction": "{{string}}",
      "AmazonBedrockFSAction": "{{string}}",
      "AmazonBedrockKRSAction": "{{string}}",
      "AmazonSThreeAction": "{{string}}",
      "Analysis": "{{string}}",
      "ApproveFlowShareRequests": "{{string}}",
      "Apps": "{{string}}",
      "AsanaAction": "{{string}}",
      "Automate": "{{string}}",
      "BambooHRAction": "{{string}}",
      "BoxAgentAction": "{{string}}",
      "BuildCalculatedFieldWithQ": "{{string}}",
      "CanvaAgentAction": "{{string}}",
      "ChatAgent": "{{string}}",
      "ComprehendAction": "{{string}}",
      "ComprehendMedicalAction": "{{string}}",
      "ConfluenceAction": "{{string}}",
      "CreateAndUpdateAmazonBedrockARSAction": "{{string}}",
      "CreateAndUpdateAmazonBedrockFSAction": "{{string}}",
      "CreateAndUpdateAmazonBedrockKRSAction": "{{string}}",
      "CreateAndUpdateAmazonSThreeAction": "{{string}}",
      "CreateAndUpdateApps": "{{string}}",
      "CreateAndUpdateAsanaAction": "{{string}}",
      "CreateAndUpdateBambooHRAction": "{{string}}",
      "CreateAndUpdateBoxAgentAction": "{{string}}",
      "CreateAndUpdateCanvaAgentAction": "{{string}}",
      "CreateAndUpdateComprehendAction": "{{string}}",
      "CreateAndUpdateComprehendMedicalAction": "{{string}}",
      "CreateAndUpdateConfluenceAction": "{{string}}",
      "CreateAndUpdateDashboardEmailReports": "{{string}}",
      "CreateAndUpdateDatasets": "{{string}}",
      "CreateAndUpdateDataSources": "{{string}}",
      "CreateAndUpdateFactSetAction": "{{string}}",
      "CreateAndUpdateGenericHTTPAction": "{{string}}",
      "CreateAndUpdateGithubAction": "{{string}}",
      "CreateAndUpdateGoogleCalendarAction": "{{string}}",
      "CreateAndUpdateHubspotAction": "{{string}}",
      "CreateAndUpdateHuggingFaceAction": "{{string}}",
      "CreateAndUpdateIntercomAction": "{{string}}",
      "CreateAndUpdateJiraAction": "{{string}}",
      "CreateAndUpdateLinearAction": "{{string}}",
      "CreateAndUpdateMCPAction": "{{string}}",
      "CreateAndUpdateMondayAction": "{{string}}",
      "CreateAndUpdateMSExchangeAction": "{{string}}",
      "CreateAndUpdateMSTeamsAction": "{{string}}",
      "CreateAndUpdateNewRelicAction": "{{string}}",
      "CreateAndUpdateNotionAction": "{{string}}",
      "CreateAndUpdateOneDriveAction": "{{string}}",
      "CreateAndUpdateOpenAPIAction": "{{string}}",
      "CreateAndUpdatePagerDutyAction": "{{string}}",
      "CreateAndUpdateSalesforceAction": "{{string}}",
      "CreateAndUpdateSandPGlobalEnergyAction": "{{string}}",
      "CreateAndUpdateSandPGMIAction": "{{string}}",
      "CreateAndUpdateSAPBillOfMaterialAction": "{{string}}",
      "CreateAndUpdateSAPBusinessPartnerAction": "{{string}}",
      "CreateAndUpdateSAPMaterialStockAction": "{{string}}",
      "CreateAndUpdateSAPPhysicalInventoryAction": "{{string}}",
      "CreateAndUpdateSAPProductMasterDataAction": "{{string}}",
      "CreateAndUpdateServiceNowAction": "{{string}}",
      "CreateAndUpdateSharePointAction": "{{string}}",
      "CreateAndUpdateSlackAction": "{{string}}",
      "CreateAndUpdateSmartsheetAction": "{{string}}",
      "CreateAndUpdateTextractAction": "{{string}}",
      "CreateAndUpdateThemes": "{{string}}",
      "CreateAndUpdateThresholdAlerts": "{{string}}",
      "CreateAndUpdateZendeskAction": "{{string}}",
      "CreateChatAgents": "{{string}}",
      "CreateDashboardExecutiveSummaryWithQ": "{{string}}",
      "CreateSharedFolders": "{{string}}",
      "CreateSpaces": "{{string}}",
      "CreateSPICEDataset": "{{string}}",
      "Dashboard": "{{string}}",
      "EditVisualWithQ": "{{string}}",
      "ExportToCsv": "{{string}}",
      "ExportToCsvInScheduledReports": "{{string}}",
      "ExportToExcel": "{{string}}",
      "ExportToExcelInScheduledReports": "{{string}}",
      "ExportToPdf": "{{string}}",
      "ExportToPdfInScheduledReports": "{{string}}",
      "Extension": "{{string}}",
      "FactSetAction": "{{string}}",
      "Flow": "{{string}}",
      "GenerateAnalyses": "{{string}}",
      "GenericHTTPAction": "{{string}}",
      "GithubAction": "{{string}}",
      "GoogleCalendarAction": "{{string}}",
      "HubspotAction": "{{string}}",
      "HuggingFaceAction": "{{string}}",
      "IncludeContentInScheduledReportsEmail": "{{string}}",
      "IntercomAction": "{{string}}",
      "InvokeAppsAIInference": "{{string}}",
      "JiraAction": "{{string}}",
      "KnowledgeBase": "{{string}}",
      "LinearAction": "{{string}}",
      "ManageSharedFolders": "{{string}}",
      "MCPAction": "{{string}}",
      "MondayAction": "{{string}}",
      "MSExchangeAction": "{{string}}",
      "MSTeamsAction": "{{string}}",
      "NewRelicAction": "{{string}}",
      "NotionAction": "{{string}}",
      "OneDriveAction": "{{string}}",
      "OpenAPIAction": "{{string}}",
      "PagerDutyAction": "{{string}}",
      "PerformFlowUiTask": "{{string}}",
      "PrintReports": "{{string}}",
      "PublishWithoutApproval": "{{string}}",
      "RenameSharedFolders": "{{string}}",
      "Research": "{{string}}",
      "SalesforceAction": "{{string}}",
      "SandPGlobalEnergyAction": "{{string}}",
      "SandPGMIAction": "{{string}}",
      "SAPBillOfMaterialAction": "{{string}}",
      "SAPBusinessPartnerAction": "{{string}}",
      "SAPMaterialStockAction": "{{string}}",
      "SAPPhysicalInventoryAction": "{{string}}",
      "SAPProductMasterDataAction": "{{string}}",
      "Scenario": "{{string}}",
      "SelfUpgradeUserRole": "{{string}}",
      "ServiceNowAction": "{{string}}",
      "ShareAmazonBedrockARSAction": "{{string}}",
      "ShareAmazonBedrockFSAction": "{{string}}",
      "ShareAmazonBedrockKRSAction": "{{string}}",
      "ShareAmazonSThreeAction": "{{string}}",
      "ShareAnalyses": "{{string}}",
      "ShareApps": "{{string}}",
      "ShareAsanaAction": "{{string}}",
      "ShareBambooHRAction": "{{string}}",
      "ShareBoxAgentAction": "{{string}}",
      "ShareCanvaAgentAction": "{{string}}",
      "ShareChatAgents": "{{string}}",
      "ShareComprehendAction": "{{string}}",
      "ShareComprehendMedicalAction": "{{string}}",
      "ShareConfluenceAction": "{{string}}",
      "ShareDashboards": "{{string}}",
      "ShareDatasets": "{{string}}",
      "ShareDataSources": "{{string}}",
      "ShareFactSetAction": "{{string}}",
      "ShareGenericHTTPAction": "{{string}}",
      "ShareGithubAction": "{{string}}",
      "ShareGoogleCalendarAction": "{{string}}",
      "ShareHubspotAction": "{{string}}",
      "ShareHuggingFaceAction": "{{string}}",
      "ShareIntercomAction": "{{string}}",
      "ShareJiraAction": "{{string}}",
      "ShareLinearAction": "{{string}}",
      "ShareMCPAction": "{{string}}",
      "ShareMondayAction": "{{string}}",
      "ShareMSExchangeAction": "{{string}}",
      "ShareMSTeamsAction": "{{string}}",
      "ShareNewRelicAction": "{{string}}",
      "ShareNotionAction": "{{string}}",
      "ShareOneDriveAction": "{{string}}",
      "ShareOpenAPIAction": "{{string}}",
      "SharePagerDutyAction": "{{string}}",
      "SharePointAction": "{{string}}",
      "ShareSalesforceAction": "{{string}}",
      "ShareSandPGlobalEnergyAction": "{{string}}",
      "ShareSandPGMIAction": "{{string}}",
      "ShareSAPBillOfMaterialAction": "{{string}}",
      "ShareSAPBusinessPartnerAction": "{{string}}",
      "ShareSAPMaterialStockAction": "{{string}}",
      "ShareSAPPhysicalInventoryAction": "{{string}}",
      "ShareSAPProductMasterDataAction": "{{string}}",
      "ShareServiceNowAction": "{{string}}",
      "ShareSharePointAction": "{{string}}",
      "ShareSlackAction": "{{string}}",
      "ShareSmartsheetAction": "{{string}}",
      "ShareSpaces": "{{string}}",
      "ShareTextractAction": "{{string}}",
      "ShareZendeskAction": "{{string}}",
      "SlackAction": "{{string}}",
      "SmartsheetAction": "{{string}}",
      "Space": "{{string}}",
      "Story": "{{string}}",
      "SubscribeDashboardEmailReports": "{{string}}",
      "TextractAction": "{{string}}",
      "Topic": "{{string}}",
      "UseAgentWebSearch": "{{string}}",
      "UseAmazonBedrockARSAction": "{{string}}",
      "UseAmazonBedrockFSAction": "{{string}}",
      "UseAmazonBedrockKRSAction": "{{string}}",
      "UseAmazonSThreeAction": "{{string}}",
      "UseAsanaAction": "{{string}}",
      "UseBambooHRAction": "{{string}}",
      "UseBedrockModels": "{{string}}",
      "UseBoxAgentAction": "{{string}}",
      "UseCanvaAgentAction": "{{string}}",
      "UseComprehendAction": "{{string}}",
      "UseComprehendMedicalAction": "{{string}}",
      "UseConfluenceAction": "{{string}}",
      "UseFactSetAction": "{{string}}",
      "UseGenericHTTPAction": "{{string}}",
      "UseGithubAction": "{{string}}",
      "UseGoogleCalendarAction": "{{string}}",
      "UseHubspotAction": "{{string}}",
      "UseHuggingFaceAction": "{{string}}",
      "UseIntercomAction": "{{string}}",
      "UseJiraAction": "{{string}}",
      "UseLinearAction": "{{string}}",
      "UseMCPAction": "{{string}}",
      "UseMondayAction": "{{string}}",
      "UseMSExchangeAction": "{{string}}",
      "UseMSTeamsAction": "{{string}}",
      "UseNewRelicAction": "{{string}}",
      "UseNotionAction": "{{string}}",
      "UseOneDriveAction": "{{string}}",
      "UseOpenAPIAction": "{{string}}",
      "UsePagerDutyAction": "{{string}}",
      "UseSalesforceAction": "{{string}}",
      "UseSandPGlobalEnergyAction": "{{string}}",
      "UseSandPGMIAction": "{{string}}",
      "UseSAPBillOfMaterialAction": "{{string}}",
      "UseSAPBusinessPartnerAction": "{{string}}",
      "UseSAPMaterialStockAction": "{{string}}",
      "UseSAPPhysicalInventoryAction": "{{string}}",
      "UseSAPProductMasterDataAction": "{{string}}",
      "UseServiceNowAction": "{{string}}",
      "UseSharePointAction": "{{string}}",
      "UseSlackAction": "{{string}}",
      "UseSmartsheetAction": "{{string}}",
      "UseTextractAction": "{{string}}",
      "UseZendeskAction": "{{string}}",
      "ViewAccountSPICECapacity": "{{string}}",
      "ZendeskAction": "{{string}}"
   },
   "CustomPermissionsName": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateCustomPermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateCustomPermissions_RequestSyntax) **   <a name="QS-CreateCustomPermissions-request-uri-AwsAccountId"></a>
The ID of the AWS account that you want to create the custom permissions profile in.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_CreateCustomPermissions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CustomPermissionsName](#API_CreateCustomPermissions_RequestSyntax) **   <a name="QS-CreateCustomPermissions-request-CustomPermissionsName"></a>
The name of the custom permissions profile that you want to create.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `^[a-zA-Z0-9+=,.@_-]+$`   
Required: Yes

 ** [Capabilities](#API_CreateCustomPermissions_RequestSyntax) **   <a name="QS-CreateCustomPermissions-request-Capabilities"></a>
A set of actions to include in the custom permissions profile.  
Type: [Capabilities](API_Capabilities.md) object  
Required: No

 ** [Tags](#API_CreateCustomPermissions_RequestSyntax) **   <a name="QS-CreateCustomPermissions-request-Tags"></a>
The tags to associate with the custom permissions profile.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateCustomPermissions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Arn": "string",
   "RequestId": "string",
   "Status": number
}
```

## Response Elements
<a name="API_CreateCustomPermissions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateCustomPermissions_ResponseSyntax) **   <a name="QS-CreateCustomPermissions-response-Arn"></a>
The Amazon Resource Name (ARN) of the custom permissions profile.  
Type: String

 ** [RequestId](#API_CreateCustomPermissions_ResponseSyntax) **   <a name="QS-CreateCustomPermissions-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [Status](#API_CreateCustomPermissions_ResponseSyntax) **   <a name="QS-CreateCustomPermissions-response-Status"></a>
The HTTP status of the request.  
Type: Integer

## Errors
<a name="API_CreateCustomPermissions_Errors"></a>

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

 ** PreconditionNotMetException **   
One or more preconditions aren't met.    
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

 ** ResourceUnavailableException **   
This resource is currently unavailable.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 503

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

## See Also
<a name="API_CreateCustomPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateCustomPermissions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateCustomPermissions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateCustomPermissions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateCustomPermissions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateCustomPermissions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateCustomPermissions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateCustomPermissions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateCustomPermissions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateCustomPermissions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateCustomPermissions) 