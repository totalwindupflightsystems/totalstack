---
id: "@specs/aws/quicksight/docs/API_DescribeTemplate"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeTemplate"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeTemplate

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeTemplate
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeTemplate
<a name="API_DescribeTemplate"></a>

Describes a template's metadata.

## Request Syntax
<a name="API_DescribeTemplate_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/templates/{{TemplateId}}?alias-name={{AliasName}}&version-number={{VersionNumber}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AliasName](#API_DescribeTemplate_RequestSyntax) **   <a name="QS-DescribeTemplate-request-uri-AliasName"></a>
The alias of the template that you want to describe. If you name a specific alias, you describe the version that the alias points to. You can specify the latest version of the template by providing the keyword `$LATEST` in the `AliasName` parameter. The keyword `$PUBLISHED` doesn't apply to templates.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[\w\-]+|(\$LATEST)|(\$PUBLISHED)` 

 ** [AwsAccountId](#API_DescribeTemplate_RequestSyntax) **   <a name="QS-DescribeTemplate-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the template that you're describing.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [TemplateId](#API_DescribeTemplate_RequestSyntax) **   <a name="QS-DescribeTemplate-request-uri-TemplateId"></a>
The ID for the template.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [VersionNumber](#API_DescribeTemplate_RequestSyntax) **   <a name="QS-DescribeTemplate-request-uri-VersionNumber"></a>
(Optional) The number for the version to describe. If a `VersionNumber` parameter value isn't provided, the latest version of the template is described.  
Valid Range: Minimum value of 1.

## Request Body
<a name="API_DescribeTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeTemplate_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RequestId": "string",
   "Template": { 
      "Arn": "string",
      "CreatedTime": number,
      "LastUpdatedTime": number,
      "Name": "string",
      "TemplateId": "string",
      "Version": { 
         "CreatedTime": number,
         "DataSetConfigurations": [ 
            { 
               "ColumnGroupSchemaList": [ 
                  { 
                     "ColumnGroupColumnSchemaList": [ 
                        { 
                           "Name": "string"
                        }
                     ],
                     "Name": "string"
                  }
               ],
               "DataSetSchema": { 
                  "ColumnSchemaList": [ 
                     { 
                        "DataType": "string",
                        "GeographicRole": "string",
                        "Name": "string"
                     }
                  ]
               },
               "Placeholder": "string"
            }
         ],
         "Description": "string",
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
         "Sheets": [ 
            { 
               "Images": [ 
                  { 
                     "Actions": [ 
                        { 
                           "ActionOperations": [ 
                              { 
                                 "NavigationOperation": { 
                                    "LocalNavigationConfiguration": { 
                                       "TargetSheetId": "string"
                                    }
                                 },
                                 "SetParametersOperation": { 
                                    "ParameterValueConfigurations": [ 
                                       { 
                                          "DestinationParameterName": "string",
                                          "Value": { 
                                             "CustomValuesConfiguration": { 
                                                "CustomValues": { 
                                                   "DateTimeValues": [ number ],
                                                   "DecimalValues": [ number ],
                                                   "IntegerValues": [ number ],
                                                   "StringValues": [ "string" ]
                                                },
                                                "IncludeNullValue": boolean
                                             },
                                             "SelectAllValueOptions": "string",
                                             "SourceColumn": { 
                                                "ColumnName": "string",
                                                "DataSetIdentifier": "string"
                                             },
                                             "SourceField": "string",
                                             "SourceParameterName": "string"
                                          }
                                       }
                                    ]
                                 },
                                 "URLOperation": { 
                                    "URLTarget": "string",
                                    "URLTemplate": "string"
                                 }
                              }
                           ],
                           "CustomActionId": "string",
                           "Name": "string",
                           "Status": "string",
                           "Trigger": "string"
                        }
                     ],
                     "ImageContentAltText": "string",
                     "Interactions": { 
                        "ImageMenuOption": { 
                           "AvailabilityStatus": "string"
                        }
                     },
                     "Scaling": { 
                        "ScalingType": "string"
                     },
                     "SheetImageId": "string",
                     "Source": { 
                        "SheetImageStaticFileSource": { 
                           "StaticFileId": "string"
                        }
                     },
                     "Tooltip": { 
                        "TooltipText": { 
                           "PlainText": "string"
                        },
                        "Visibility": "string"
                     }
                  }
               ],
               "Name": "string",
               "SheetId": "string"
            }
         ],
         "SourceEntityArn": "string",
         "Status": "string",
         "ThemeArn": "string",
         "VersionNumber": number
      }
   }
}
```

## Response Elements
<a name="API_DescribeTemplate_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeTemplate_ResponseSyntax) **   <a name="QS-DescribeTemplate-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_DescribeTemplate_ResponseSyntax) **   <a name="QS-DescribeTemplate-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [Template](#API_DescribeTemplate_ResponseSyntax) **   <a name="QS-DescribeTemplate-response-Template"></a>
The template structure for the object you want to describe.  
Type: [Template](API_Template.md) object

## Errors
<a name="API_DescribeTemplate_Errors"></a>

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
<a name="API_DescribeTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeTemplate) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeTemplate) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeTemplate) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeTemplate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeTemplate) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeTemplate) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeTemplate) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeTemplate) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeTemplate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeTemplate) 