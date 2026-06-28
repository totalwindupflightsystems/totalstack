---
id: "@specs/aws/quicksight/docs/API_CreateTheme"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateTheme"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# CreateTheme

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_CreateTheme
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateTheme
<a name="API_CreateTheme"></a>

Creates a theme.

A *theme* is set of configuration options for color and layout. Themes apply to analyses and dashboards. For more information, see [Using Themes in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/themes-in-quicksight.html) in the *Amazon Quick Sight User Guide*.

## Request Syntax
<a name="API_CreateTheme_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/themes/{{ThemeId}} HTTP/1.1
Content-type: application/json

{
   "BaseThemeId": "{{string}}",
   "Configuration": { 
      "DataColorPalette": { 
         "Colors": [ "{{string}}" ],
         "EmptyFillColor": "{{string}}",
         "MinMaxGradient": [ "{{string}}" ]
      },
      "Sheet": { 
         "Background": { 
            "Color": "{{string}}",
            "Gradient": "{{string}}"
         },
         "Tile": { 
            "BackgroundColor": "{{string}}",
            "Border": { 
               "Color": "{{string}}",
               "Show": {{boolean}},
               "Width": "{{string}}"
            },
            "BorderRadius": "{{string}}",
            "Padding": "{{string}}"
         },
         "TileLayout": { 
            "Gutter": { 
               "Show": {{boolean}}
            },
            "Margin": { 
               "Show": {{boolean}}
            }
         }
      },
      "Typography": { 
         "AxisLabelFontConfiguration": { 
            "FontColor": "{{string}}",
            "FontDecoration": "{{string}}",
            "FontFamily": "{{string}}",
            "FontSize": { 
               "Absolute": "{{string}}",
               "Relative": "{{string}}"
            },
            "FontStyle": "{{string}}",
            "FontWeight": { 
               "Name": "{{string}}"
            }
         },
         "AxisTitleFontConfiguration": { 
            "FontColor": "{{string}}",
            "FontDecoration": "{{string}}",
            "FontFamily": "{{string}}",
            "FontSize": { 
               "Absolute": "{{string}}",
               "Relative": "{{string}}"
            },
            "FontStyle": "{{string}}",
            "FontWeight": { 
               "Name": "{{string}}"
            }
         },
         "ControlTitleFontConfiguration": { 
            "FontConfiguration": { 
               "FontColor": "{{string}}",
               "FontDecoration": "{{string}}",
               "FontFamily": "{{string}}",
               "FontSize": { 
                  "Absolute": "{{string}}",
                  "Relative": "{{string}}"
               },
               "FontStyle": "{{string}}",
               "FontWeight": { 
                  "Name": "{{string}}"
               }
            },
            "TextAlignment": "{{string}}"
         },
         "DataLabelFontConfiguration": { 
            "FontColor": "{{string}}",
            "FontDecoration": "{{string}}",
            "FontFamily": "{{string}}",
            "FontSize": { 
               "Absolute": "{{string}}",
               "Relative": "{{string}}"
            },
            "FontStyle": "{{string}}",
            "FontWeight": { 
               "Name": "{{string}}"
            }
         },
         "FontFamilies": [ 
            { 
               "FontFamily": "{{string}}"
            }
         ],
         "LegendTitleFontConfiguration": { 
            "FontColor": "{{string}}",
            "FontDecoration": "{{string}}",
            "FontFamily": "{{string}}",
            "FontSize": { 
               "Absolute": "{{string}}",
               "Relative": "{{string}}"
            },
            "FontStyle": "{{string}}",
            "FontWeight": { 
               "Name": "{{string}}"
            }
         },
         "LegendValueFontConfiguration": { 
            "FontColor": "{{string}}",
            "FontDecoration": "{{string}}",
            "FontFamily": "{{string}}",
            "FontSize": { 
               "Absolute": "{{string}}",
               "Relative": "{{string}}"
            },
            "FontStyle": "{{string}}",
            "FontWeight": { 
               "Name": "{{string}}"
            }
         },
         "VisualSubtitleFontConfiguration": { 
            "FontConfiguration": { 
               "FontColor": "{{string}}",
               "FontDecoration": "{{string}}",
               "FontFamily": "{{string}}",
               "FontSize": { 
                  "Absolute": "{{string}}",
                  "Relative": "{{string}}"
               },
               "FontStyle": "{{string}}",
               "FontWeight": { 
                  "Name": "{{string}}"
               }
            },
            "TextAlignment": "{{string}}",
            "TextTransform": "{{string}}"
         },
         "VisualTitleFontConfiguration": { 
            "FontConfiguration": { 
               "FontColor": "{{string}}",
               "FontDecoration": "{{string}}",
               "FontFamily": "{{string}}",
               "FontSize": { 
                  "Absolute": "{{string}}",
                  "Relative": "{{string}}"
               },
               "FontStyle": "{{string}}",
               "FontWeight": { 
                  "Name": "{{string}}"
               }
            },
            "TextAlignment": "{{string}}",
            "TextTransform": "{{string}}"
         }
      },
      "UIColorPalette": { 
         "Accent": "{{string}}",
         "AccentForeground": "{{string}}",
         "Danger": "{{string}}",
         "DangerForeground": "{{string}}",
         "Dimension": "{{string}}",
         "DimensionForeground": "{{string}}",
         "Measure": "{{string}}",
         "MeasureForeground": "{{string}}",
         "PrimaryBackground": "{{string}}",
         "PrimaryForeground": "{{string}}",
         "SecondaryBackground": "{{string}}",
         "SecondaryForeground": "{{string}}",
         "Success": "{{string}}",
         "SuccessForeground": "{{string}}",
         "Warning": "{{string}}",
         "WarningForeground": "{{string}}"
      }
   },
   "Name": "{{string}}",
   "Permissions": [ 
      { 
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ],
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VersionDescription": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateTheme_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_CreateTheme_RequestSyntax) **   <a name="QS-CreateTheme-request-uri-AwsAccountId"></a>
The ID of the AWS account where you want to store the new theme.   
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [ThemeId](#API_CreateTheme_RequestSyntax) **   <a name="QS-CreateTheme-request-uri-ThemeId"></a>
An ID for the theme that you want to create. The theme ID is unique per AWS Region in each AWS account.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

## Request Body
<a name="API_CreateTheme_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BaseThemeId](#API_CreateTheme_RequestSyntax) **   <a name="QS-CreateTheme-request-BaseThemeId"></a>
The ID of the theme that a custom theme will inherit from. All themes inherit from one of the starting themes defined by Amazon Quick Sight. For a list of the starting themes, use `ListThemes` or choose **Themes** from within an analysis.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

 ** [Configuration](#API_CreateTheme_RequestSyntax) **   <a name="QS-CreateTheme-request-Configuration"></a>
The theme configuration, which contains the theme display properties.  
Type: [ThemeConfiguration](API_ThemeConfiguration.md) object  
Required: Yes

 ** [Name](#API_CreateTheme_RequestSyntax) **   <a name="QS-CreateTheme-request-Name"></a>
A display name for the theme.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: Yes

 ** [Permissions](#API_CreateTheme_RequestSyntax) **   <a name="QS-CreateTheme-request-Permissions"></a>
A valid grouping of resource permissions to apply to the new theme.   
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 64 items.  
Required: No

 ** [Tags](#API_CreateTheme_RequestSyntax) **   <a name="QS-CreateTheme-request-Tags"></a>
A map of the key-value pairs for the resource tag or tags that you want to add to the resource.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** [VersionDescription](#API_CreateTheme_RequestSyntax) **   <a name="QS-CreateTheme-request-VersionDescription"></a>
A description of the first version of the theme that you're creating. Every time `UpdateTheme` is called, a new version is created. Each version of the theme has a description of the version in the `VersionDescription` field.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Required: No

## Response Syntax
<a name="API_CreateTheme_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "Arn": "string",
   "CreationStatus": "string",
   "RequestId": "string",
   "ThemeId": "string",
   "VersionArn": "string"
}
```

## Response Elements
<a name="API_CreateTheme_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_CreateTheme_ResponseSyntax) **   <a name="QS-CreateTheme-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateTheme_ResponseSyntax) **   <a name="QS-CreateTheme-response-Arn"></a>
The Amazon Resource Name (ARN) for the theme.  
Type: String

 ** [CreationStatus](#API_CreateTheme_ResponseSyntax) **   <a name="QS-CreateTheme-response-CreationStatus"></a>
The theme creation status.  
Type: String  
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED` 

 ** [RequestId](#API_CreateTheme_ResponseSyntax) **   <a name="QS-CreateTheme-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

 ** [ThemeId](#API_CreateTheme_ResponseSyntax) **   <a name="QS-CreateTheme-response-ThemeId"></a>
The ID of the theme.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+` 

 ** [VersionArn](#API_CreateTheme_ResponseSyntax) **   <a name="QS-CreateTheme-response-VersionArn"></a>
The Amazon Resource Name (ARN) for the new theme.  
Type: String

## Errors
<a name="API_CreateTheme_Errors"></a>

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
<a name="API_CreateTheme_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/CreateTheme) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/CreateTheme) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/CreateTheme) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/CreateTheme) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/CreateTheme) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/CreateTheme) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/CreateTheme) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/CreateTheme) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/CreateTheme) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/CreateTheme) 