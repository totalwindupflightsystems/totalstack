---
id: "@specs/aws/quicksight/docs/API_DescribeDashboard"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeDashboard"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeDashboard

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeDashboard
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeDashboard
<a name="API_DescribeDashboard"></a>

Provides a summary for a dashboard.

## Request Syntax
<a name="API_DescribeDashboard_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/dashboards/{{DashboardId}}?alias-name={{AliasName}}&version-number={{VersionNumber}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDashboard_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AliasName](#API_DescribeDashboard_RequestSyntax) **   <a name="QS-DescribeDashboard-request-uri-AliasName"></a>
The alias name.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[\w\-]+|(\$LATEST)|(\$PUBLISHED)` 

 ** [AwsAccountId](#API_DescribeDashboard_RequestSyntax) **   <a name="QS-DescribeDashboard-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the dashboard that you're describing.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [DashboardId](#API_DescribeDashboard_RequestSyntax) **   <a name="QS-DescribeDashboard-request-uri-DashboardId"></a>
The ID for the dashboard.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [VersionNumber](#API_DescribeDashboard_RequestSyntax) **   <a name="QS-DescribeDashboard-request-uri-VersionNumber"></a>
The version number for the dashboard. If a version number isn't passed, the latest published dashboard version is described.   
Valid Range: Minimum value of 1.

## Request Body
<a name="API_DescribeDashboard_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDashboard_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Dashboard": { 
      "Arn": "string",
      "CreatedTime": number,
      "DashboardId": "string",
      "LastPublishedTime": number,
      "LastUpdatedTime": number,
      "LinkEntities": [ "string" ],
      "Name": "string",
      "Version": { 
         "Arn": "string",
         "CreatedTime": number,
         "DataSetArns": [ "string" ],
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
   },
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DescribeDashboard_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeDashboard_ResponseSyntax) **   <a name="QS-DescribeDashboard-response-Status"></a>
The HTTP status of this request.

The following data is returned in JSON format by the service.

 ** [Dashboard](#API_DescribeDashboard_ResponseSyntax) **   <a name="QS-DescribeDashboard-response-Dashboard"></a>
Information about the dashboard.  
Type: [Dashboard](API_Dashboard.md) object

 ** [RequestId](#API_DescribeDashboard_ResponseSyntax) **   <a name="QS-DescribeDashboard-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DescribeDashboard_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You don't have access to this item. The provided credentials couldn't be validated. You might not be authorized to carry out the request. Make sure that your account is authorized to use the Amazon Quick Sight service, that your policies have the correct permissions, and that you are using the correct credentials.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 401

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
<a name="API_DescribeDashboard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeDashboard) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeDashboard) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeDashboard) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeDashboard) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeDashboard) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeDashboard) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeDashboard) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeDashboard) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeDashboard) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeDashboard) 