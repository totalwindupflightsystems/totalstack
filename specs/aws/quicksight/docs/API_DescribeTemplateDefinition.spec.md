---
id: "@specs/aws/quicksight/docs/API_DescribeTemplateDefinition"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeTemplateDefinition"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeTemplateDefinition

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeTemplateDefinition
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeTemplateDefinition
<a name="API_DescribeTemplateDefinition"></a>

Provides a detailed description of the definition of a template.

**Note**  
If you do not need to know details about the content of a template, for instance if you are trying to check the status of a recently created or updated template, use the [https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeTemplate.html](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeTemplate.html) instead. 

## Request Syntax
<a name="API_DescribeTemplateDefinition_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/templates/{{TemplateId}}/definition?alias-name={{AliasName}}&version-number={{VersionNumber}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeTemplateDefinition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AliasName](#API_DescribeTemplateDefinition_RequestSyntax) **   <a name="QS-DescribeTemplateDefinition-request-uri-AliasName"></a>
The alias of the template that you want to describe. If you name a specific alias, you describe the version that the alias points to. You can specify the latest version of the template by providing the keyword `$LATEST` in the `AliasName` parameter. The keyword `$PUBLISHED` doesn't apply to templates.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[\w\-]+|(\$LATEST)|(\$PUBLISHED)` 

 ** [AwsAccountId](#API_DescribeTemplateDefinition_RequestSyntax) **   <a name="QS-DescribeTemplateDefinition-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the template. You must be using the AWS account that the template is in.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [TemplateId](#API_DescribeTemplateDefinition_RequestSyntax) **   <a name="QS-DescribeTemplateDefinition-request-uri-TemplateId"></a>
The ID of the template that you're describing.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [VersionNumber](#API_DescribeTemplateDefinition_RequestSyntax) **   <a name="QS-DescribeTemplateDefinition-request-uri-VersionNumber"></a>
The version number of the template.  
Valid Range: Minimum value of 1.

## Request Body
<a name="API_DescribeTemplateDefinition_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeTemplateDefinition_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
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
         "ExcludedDataSetArns": [ "string" ],
         "QBusinessInsightsStatus": "string",
         "Timezone": "string",
         "WeekStart": "string"
      },
      "ParameterDeclarations": [ 
         { ... }
      ],
      "QueryExecutionOptions": { 
         "QueryExecutionMode": "string"
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
   "TemplateId": "string",
   "ThemeArn": "string"
}
```

## Response Elements
<a name="API_DescribeTemplateDefinition_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeTemplateDefinition_ResponseSyntax) **   <a name="QS-DescribeTemplateDefinition-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Definition](#API_DescribeTemplateDefinition_ResponseSyntax) **   <a name="QS-DescribeTemplateDefinition-response-Definition"></a>
The definition of the template.  
A definition is the data model of all features in a Dashboard, Template, or Analysis.  
Type: [TemplateVersionDefinition](API_TemplateVersionDefinition.md) object

 ** [Errors](#API_DescribeTemplateDefinition_ResponseSyntax) **   <a name="QS-DescribeTemplateDefinition-response-Errors"></a>
Errors associated with the template version.  
Type: Array of [TemplateError](API_TemplateError.md) objects  
Array Members: Minimum number of 1 item.

 ** [Name](#API_DescribeTemplateDefinition_ResponseSyntax) **   <a name="QS-DescribeTemplateDefinition-response-Name"></a>
The descriptive name of the template.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [RequestId](#API_DescribeTemplateDefinition_ResponseSyntax) **   <a name="QS-DescribeTemplateDefinition-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [ResourceStatus](#API_DescribeTemplateDefinition_ResponseSyntax) **   <a name="QS-DescribeTemplateDefinition-response-ResourceStatus"></a>
Status associated with the template.  
+  `CREATION_IN_PROGRESS` 
+  `CREATION_SUCCESSFUL` 
+  `CREATION_FAILED` 
+  `UPDATE_IN_PROGRESS` 
+  `UPDATE_SUCCESSFUL` 
+  `UPDATE_FAILED` 
+  `DELETED` 
Type: String  
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED` 

 ** [TemplateId](#API_DescribeTemplateDefinition_ResponseSyntax) **   <a name="QS-DescribeTemplateDefinition-response-TemplateId"></a>
The ID of the template described.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

 ** [ThemeArn](#API_DescribeTemplateDefinition_ResponseSyntax) **   <a name="QS-DescribeTemplateDefinition-response-ThemeArn"></a>
The ARN of the theme of the template.  
Type: String

## Errors
<a name="API_DescribeTemplateDefinition_Errors"></a>

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
<a name="API_DescribeTemplateDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeTemplateDefinition) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeTemplateDefinition) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeTemplateDefinition) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeTemplateDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeTemplateDefinition) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeTemplateDefinition) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeTemplateDefinition) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeTemplateDefinition) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeTemplateDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeTemplateDefinition) 