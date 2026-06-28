---
id: "@specs/aws/quicksight/docs/API_DescribeAnalysisDefinition"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeAnalysisDefinition"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeAnalysisDefinition

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeAnalysisDefinition
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeAnalysisDefinition
<a name="API_DescribeAnalysisDefinition"></a>

Provides a detailed description of the definition of an analysis.

**Note**  
If you do not need to know details about the content of an Analysis, for instance if you are trying to check the status of a recently created or updated Analysis, use the [https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeAnalysis.html](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeAnalysis.html) instead. 

## Request Syntax
<a name="API_DescribeAnalysisDefinition_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/analyses/{{AnalysisId}}/definition HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeAnalysisDefinition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AnalysisId](#API_DescribeAnalysisDefinition_RequestSyntax) **   <a name="QS-DescribeAnalysisDefinition-request-uri-AnalysisId"></a>
The ID of the analysis that you're describing. The ID is part of the URL of the analysis.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [AwsAccountId](#API_DescribeAnalysisDefinition_RequestSyntax) **   <a name="QS-DescribeAnalysisDefinition-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the analysis. You must be using the AWS account that the analysis is in.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_DescribeAnalysisDefinition_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeAnalysisDefinition_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AnalysisId": "string",
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
   "ThemeArn": "string"
}
```

## Response Elements
<a name="API_DescribeAnalysisDefinition_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeAnalysisDefinition_ResponseSyntax) **   <a name="QS-DescribeAnalysisDefinition-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AnalysisId](#API_DescribeAnalysisDefinition_ResponseSyntax) **   <a name="QS-DescribeAnalysisDefinition-response-AnalysisId"></a>
The ID of the analysis described.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

 ** [Definition](#API_DescribeAnalysisDefinition_ResponseSyntax) **   <a name="QS-DescribeAnalysisDefinition-response-Definition"></a>
The definition of an analysis.  
A definition is the data model of all features in a Dashboard, Template, or Analysis.  
Type: [AnalysisDefinition](API_AnalysisDefinition.md) object

 ** [Errors](#API_DescribeAnalysisDefinition_ResponseSyntax) **   <a name="QS-DescribeAnalysisDefinition-response-Errors"></a>
Errors associated with the analysis.  
Type: Array of [AnalysisError](API_AnalysisError.md) objects  
Array Members: Minimum number of 1 item.

 ** [Name](#API_DescribeAnalysisDefinition_ResponseSyntax) **   <a name="QS-DescribeAnalysisDefinition-response-Name"></a>
The descriptive name of the analysis.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [RequestId](#API_DescribeAnalysisDefinition_ResponseSyntax) **   <a name="QS-DescribeAnalysisDefinition-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [ResourceStatus](#API_DescribeAnalysisDefinition_ResponseSyntax) **   <a name="QS-DescribeAnalysisDefinition-response-ResourceStatus"></a>
Status associated with the analysis.  
+  `CREATION_IN_PROGRESS` 
+  `CREATION_SUCCESSFUL` 
+  `CREATION_FAILED` 
+  `UPDATE_IN_PROGRESS` 
+  `UPDATE_SUCCESSFUL` 
+  `UPDATE_FAILED` 
+  `DELETED` 
Type: String  
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED` 

 ** [ThemeArn](#API_DescribeAnalysisDefinition_ResponseSyntax) **   <a name="QS-DescribeAnalysisDefinition-response-ThemeArn"></a>
The ARN of the theme of the analysis.  
Type: String

## Errors
<a name="API_DescribeAnalysisDefinition_Errors"></a>

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
<a name="API_DescribeAnalysisDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeAnalysisDefinition) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeAnalysisDefinition) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeAnalysisDefinition) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeAnalysisDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeAnalysisDefinition) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeAnalysisDefinition) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeAnalysisDefinition) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeAnalysisDefinition) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeAnalysisDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeAnalysisDefinition) 