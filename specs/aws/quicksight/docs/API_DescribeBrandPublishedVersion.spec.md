---
id: "@specs/aws/quicksight/docs/API_DescribeBrandPublishedVersion"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeBrandPublishedVersion"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# DescribeBrandPublishedVersion

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_DescribeBrandPublishedVersion
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeBrandPublishedVersion
<a name="API_DescribeBrandPublishedVersion"></a>

Describes the published version of the brand.

## Request Syntax
<a name="API_DescribeBrandPublishedVersion_RequestSyntax"></a>

```
GET /accounts/{{AwsAccountId}}/brands/{{BrandId}}/publishedversion HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeBrandPublishedVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_DescribeBrandPublishedVersion_RequestSyntax) **   <a name="QS-DescribeBrandPublishedVersion-request-uri-AwsAccountId"></a>
The ID of the AWS account that owns the brand.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

 ** [BrandId](#API_DescribeBrandPublishedVersion_RequestSyntax) **   <a name="QS-DescribeBrandPublishedVersion-request-uri-BrandId"></a>
The ID of the Quick brand.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[\w\-]+`   
Required: Yes

## Request Body
<a name="API_DescribeBrandPublishedVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeBrandPublishedVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "BrandDefinition": { 
      "ApplicationTheme": { 
         "BrandColorPalette": { 
            "Accent": { 
               "Background": "string",
               "Foreground": "string"
            },
            "Danger": { 
               "Background": "string",
               "Foreground": "string"
            },
            "Dimension": { 
               "Background": "string",
               "Foreground": "string"
            },
            "Info": { 
               "Background": "string",
               "Foreground": "string"
            },
            "Measure": { 
               "Background": "string",
               "Foreground": "string"
            },
            "Primary": { 
               "Background": "string",
               "Foreground": "string"
            },
            "Secondary": { 
               "Background": "string",
               "Foreground": "string"
            },
            "Success": { 
               "Background": "string",
               "Foreground": "string"
            },
            "Warning": { 
               "Background": "string",
               "Foreground": "string"
            }
         },
         "BrandElementStyle": { 
            "NavbarStyle": { 
               "ContextualNavbar": { 
                  "Background": "string",
                  "Foreground": "string"
               },
               "GlobalNavbar": { 
                  "Background": "string",
                  "Foreground": "string"
               }
            }
         },
         "ContextualAccentPalette": { 
            "Automation": { 
               "Background": "string",
               "Foreground": "string"
            },
            "Connection": { 
               "Background": "string",
               "Foreground": "string"
            },
            "Insight": { 
               "Background": "string",
               "Foreground": "string"
            },
            "Visualization": { 
               "Background": "string",
               "Foreground": "string"
            }
         }
      },
      "BrandName": "string",
      "Description": "string",
      "LogoConfiguration": { 
         "AltText": "string",
         "LogoSet": { 
            "Favicon": { 
               "Original": { 
                  "Source": { ... }
               }
            },
            "Primary": { 
               "Original": { 
                  "Source": { ... }
               }
            }
         }
      }
   },
   "BrandDetail": { 
      "Arn": "string",
      "BrandId": "string",
      "BrandStatus": "string",
      "CreatedTime": number,
      "Errors": [ "string" ],
      "LastUpdatedTime": number,
      "Logo": { 
         "AltText": "string",
         "LogoSet": { 
            "Favicon": { 
               "Height32": { 
                  "GeneratedImageUrl": "string",
                  "Source": { ... }
               },
               "Height64": { 
                  "GeneratedImageUrl": "string",
                  "Source": { ... }
               },
               "Original": { 
                  "GeneratedImageUrl": "string",
                  "Source": { ... }
               }
            },
            "Primary": { 
               "Height32": { 
                  "GeneratedImageUrl": "string",
                  "Source": { ... }
               },
               "Height64": { 
                  "GeneratedImageUrl": "string",
                  "Source": { ... }
               },
               "Original": { 
                  "GeneratedImageUrl": "string",
                  "Source": { ... }
               }
            }
         }
      },
      "VersionId": "string",
      "VersionStatus": "string"
   },
   "RequestId": "string"
}
```

## Response Elements
<a name="API_DescribeBrandPublishedVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BrandDefinition](#API_DescribeBrandPublishedVersion_ResponseSyntax) **   <a name="QS-DescribeBrandPublishedVersion-response-BrandDefinition"></a>
The definition of the brand.  
Type: [BrandDefinition](API_BrandDefinition.md) object

 ** [BrandDetail](#API_DescribeBrandPublishedVersion_ResponseSyntax) **   <a name="QS-DescribeBrandPublishedVersion-response-BrandDetail"></a>
The details of the brand.  
Type: [BrandDetail](API_BrandDetail.md) object

 ** [RequestId](#API_DescribeBrandPublishedVersion_ResponseSyntax) **   <a name="QS-DescribeBrandPublishedVersion-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_DescribeBrandPublishedVersion_Errors"></a>

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

 ** InternalServerException **   
An internal service exception.  
HTTP Status Code: 500

 ** InvalidRequestException **   
You don't have this feature activated for your account. To fix this issue, contact AWS support.    
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

## See Also
<a name="API_DescribeBrandPublishedVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/DescribeBrandPublishedVersion) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/DescribeBrandPublishedVersion) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DescribeBrandPublishedVersion) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/DescribeBrandPublishedVersion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DescribeBrandPublishedVersion) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/DescribeBrandPublishedVersion) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/DescribeBrandPublishedVersion) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/DescribeBrandPublishedVersion) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/DescribeBrandPublishedVersion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DescribeBrandPublishedVersion) 