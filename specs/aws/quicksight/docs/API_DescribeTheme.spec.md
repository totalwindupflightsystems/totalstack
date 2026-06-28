---
id: "@specs/aws/quicksight/docs/API_DescribeTheme"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeTheme"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeTheme

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeTheme
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeTheme
<a name="API_DescribeTheme"></a>

Describes a theme.

## Request Syntax
<a name="API_DescribeTheme_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/themes/{{ThemeId}}?alias-name={{AliasName}}&version-number={{VersionNumber}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeTheme_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AliasName](#API_DescribeTheme_RequestSyntax) **   <a name="QS-DescribeTheme-request-uri-AliasName"></a>
The alias of the theme that you want to describe. If you name a specific alias, you describe the version that the alias points to. You can specify the latest version of the theme by providing the keyword `$LATEST` in the `AliasName` parameter. The keyword `$PUBLISHED` doesn't apply to themes.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[\w\-]+|(\$LATEST)|(\$PUBLISHED)` 

 ** [AwsAccountId](#API_DescribeTheme_RequestSyntax) **   <a name="QS-DescribeTheme-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the theme that you're describing.  
Pattern: `^(aws|[0-9]{12})$`   
Required: Yes

 ** [ThemeId](#API_DescribeTheme_RequestSyntax) **   <a name="QS-DescribeTheme-request-uri-ThemeId"></a>
The ID for the theme.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [VersionNumber](#API_DescribeTheme_RequestSyntax) **   <a name="QS-DescribeTheme-request-uri-VersionNumber"></a>
The version number for the version to describe. If a `VersionNumber` parameter value isn't provided, the latest version of the theme is described.  
Valid Range: Minimum value of 1.

## Request Body
<a name="API_DescribeTheme_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeTheme_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "RequestId": "string",
   "Theme": { 
      "Arn": "string",
      "CreatedTime": number,
      "LastUpdatedTime": number,
      "Name": "string",
      "ThemeId": "string",
      "Type": "string",
      "Version": { 
         "Arn": "string",
         "BaseThemeId": "string",
         "Configuration": { 
            "DataColorPalette": { 
               "Colors": [ "string" ],
               "EmptyFillColor": "string",
               "MinMaxGradient": [ "string" ]
            },
            "Sheet": { 
               "Background": { 
                  "Color": "string",
                  "Gradient": "string"
               },
               "Tile": { 
                  "BackgroundColor": "string",
                  "Border": { 
                     "Color": "string",
                     "Show": boolean,
                     "Width": "string"
                  },
                  "BorderRadius": "string",
                  "Padding": "string"
               },
               "TileLayout": { 
                  "Gutter": { 
                     "Show": boolean
                  },
                  "Margin": { 
                     "Show": boolean
                  }
               }
            },
            "Typography": { 
               "AxisLabelFontConfiguration": { 
                  "FontColor": "string",
                  "FontDecoration": "string",
                  "FontFamily": "string",
                  "FontSize": { 
                     "Absolute": "string",
                     "Relative": "string"
                  },
                  "FontStyle": "string",
                  "FontWeight": { 
                     "Name": "string"
                  }
               },
               "AxisTitleFontConfiguration": { 
                  "FontColor": "string",
                  "FontDecoration": "string",
                  "FontFamily": "string",
                  "FontSize": { 
                     "Absolute": "string",
                     "Relative": "string"
                  },
                  "FontStyle": "string",
                  "FontWeight": { 
                     "Name": "string"
                  }
               },
               "ControlTitleFontConfiguration": { 
                  "FontConfiguration": { 
                     "FontColor": "string",
                     "FontDecoration": "string",
                     "FontFamily": "string",
                     "FontSize": { 
                        "Absolute": "string",
                        "Relative": "string"
                     },
                     "FontStyle": "string",
                     "FontWeight": { 
                        "Name": "string"
                     }
                  },
                  "TextAlignment": "string"
               },
               "DataLabelFontConfiguration": { 
                  "FontColor": "string",
                  "FontDecoration": "string",
                  "FontFamily": "string",
                  "FontSize": { 
                     "Absolute": "string",
                     "Relative": "string"
                  },
                  "FontStyle": "string",
                  "FontWeight": { 
                     "Name": "string"
                  }
               },
               "FontFamilies": [ 
                  { 
                     "FontFamily": "string"
                  }
               ],
               "LegendTitleFontConfiguration": { 
                  "FontColor": "string",
                  "FontDecoration": "string",
                  "FontFamily": "string",
                  "FontSize": { 
                     "Absolute": "string",
                     "Relative": "string"
                  },
                  "FontStyle": "string",
                  "FontWeight": { 
                     "Name": "string"
                  }
               },
               "LegendValueFontConfiguration": { 
                  "FontColor": "string",
                  "FontDecoration": "string",
                  "FontFamily": "string",
                  "FontSize": { 
                     "Absolute": "string",
                     "Relative": "string"
                  },
                  "FontStyle": "string",
                  "FontWeight": { 
                     "Name": "string"
                  }
               },
               "VisualSubtitleFontConfiguration": { 
                  "FontConfiguration": { 
                     "FontColor": "string",
                     "FontDecoration": "string",
                     "FontFamily": "string",
                     "FontSize": { 
                        "Absolute": "string",
                        "Relative": "string"
                     },
                     "FontStyle": "string",
                     "FontWeight": { 
                        "Name": "string"
                     }
                  },
                  "TextAlignment": "string",
                  "TextTransform": "string"
               },
               "VisualTitleFontConfiguration": { 
                  "FontConfiguration": { 
                     "FontColor": "string",
                     "FontDecoration": "string",
                     "FontFamily": "string",
                     "FontSize": { 
                        "Absolute": "string",
                        "Relative": "string"
                     },
                     "FontStyle": "string",
                     "FontWeight": { 
                        "Name": "string"
                     }
                  },
                  "TextAlignment": "string",
                  "TextTransform": "string"
               }
            },
            "UIColorPalette": { 
               "Accent": "string",
               "AccentForeground": "string",
               "Danger": "string",
               "DangerForeground": "string",
               "Dimension": "string",
               "DimensionForeground": "string",
               "Measure": "string",
               "MeasureForeground": "string",
               "PrimaryBackground": "string",
               "PrimaryForeground": "string",
               "SecondaryBackground": "string",
               "SecondaryForeground": "string",
               "Success": "string",
               "SuccessForeground": "string",
               "Warning": "string",
               "WarningForeground": "string"
            }
         },
         "CreatedTime": number,
         "Description": "string",
         "Errors": [ 
            { 
               "Message": "string",
               "Type": "string"
            }
         ],
         "Status": "string",
         "VersionNumber": number
      }
   }
}
```

## Response Elements
<a name="API_DescribeTheme_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_DescribeTheme_ResponseSyntax) **   <a name="QS-DescribeTheme-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_DescribeTheme_ResponseSyntax) **   <a name="QS-DescribeTheme-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [Theme](#API_DescribeTheme_ResponseSyntax) **   <a name="QS-DescribeTheme-response-Theme"></a>
The information about the theme that you are describing.  
Type: [Theme](API_Theme.md) object

## Errors
<a name="API_DescribeTheme_Errors"></a>

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
<a name="API_DescribeTheme_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeTheme) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeTheme) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeTheme) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeTheme) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeTheme) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeTheme) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeTheme) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeTheme) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeTheme) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeTheme) 