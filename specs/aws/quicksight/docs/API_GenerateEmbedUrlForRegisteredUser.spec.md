---
id: "@specs/aws/quicksight/docs/API_GenerateEmbedUrlForRegisteredUser"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GenerateEmbedUrlForRegisteredUser"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# GenerateEmbedUrlForRegisteredUser

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_GenerateEmbedUrlForRegisteredUser
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GenerateEmbedUrlForRegisteredUser
<a name="API_GenerateEmbedUrlForRegisteredUser"></a>

Generates an embed URL that you can use to embed an Amazon Quick experience in your website. This action can be used for any type of user registered in an Amazon Quick account. Before you use this action, make sure that you have configured the relevant Amazon Quick resource and permissions.

The following rules apply to the generated URL:
+ It contains a temporary bearer token. It is valid for 5 minutes after it is generated. Once redeemed within this period, it cannot be re-used again.
+ The URL validity period should not be confused with the actual session lifetime that can be customized using the ` [SessionLifetimeInMinutes](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForRegisteredUser.html#QS-GenerateEmbedUrlForRegisteredUser-request-SessionLifetimeInMinutes) ` parameter.

  The resulting user session is valid for 15 minutes (minimum) to 10 hours (maximum). The default session duration is 10 hours.
+ You are charged only when the URL is used or there is interaction with Amazon Quick.

For more information, see [Embedded Analytics](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics.html) in the *Amazon Quick User Guide*.

For more information about the high-level steps for embedding and for an interactive demo of the ways you can customize embedding, visit the [Amazon Quick Developer Portal](https://docs.aws.amazon.com/quicksight/latest/user/quicksight-dev-portal.html).

## Request Syntax
<a name="API_GenerateEmbedUrlForRegisteredUser_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/embed-url/registered-user HTTP/1.1
Content-type: application/json

{
   "AllowedDomains": [ "{{string}}" ],
   "ExperienceConfiguration": { 
      "Dashboard": { 
         "FeatureConfigurations": { 
            "AmazonQInQuickSight": { 
               "ExecutiveSummary": { 
                  "Enabled": {{boolean}}
               }
            },
            "Bookmarks": { 
               "Enabled": {{boolean}}
            },
            "DashboardCustomizationSummary": { 
               "Enabled": {{boolean}}
            },
            "RecentSnapshots": { 
               "Enabled": {{boolean}}
            },
            "Schedules": { 
               "Enabled": {{boolean}}
            },
            "SharedView": { 
               "Enabled": {{boolean}}
            },
            "StatePersistence": { 
               "Enabled": {{boolean}}
            },
            "ThresholdAlerts": { 
               "Enabled": {{boolean}}
            }
         },
         "InitialDashboardId": "{{string}}"
      },
      "DashboardVisual": { 
         "InitialDashboardVisualId": { 
            "DashboardId": "{{string}}",
            "SheetId": "{{string}}",
            "VisualId": "{{string}}"
         }
      },
      "GenerativeQnA": { 
         "InitialTopicId": "{{string}}"
      },
      "QSearchBar": { 
         "InitialTopicId": "{{string}}"
      },
      "QuickChat": { 
      },
      "QuickSightConsole": { 
         "FeatureConfigurations": { 
            "AmazonQInQuickSight": { 
               "DataQnA": { 
                  "Enabled": {{boolean}}
               },
               "DataStories": { 
                  "Enabled": {{boolean}}
               },
               "ExecutiveSummary": { 
                  "Enabled": {{boolean}}
               },
               "GenerativeAuthoring": { 
                  "Enabled": {{boolean}}
               }
            },
            "DashboardCustomizationSummary": { 
               "Enabled": {{boolean}}
            },
            "RecentSnapshots": { 
               "Enabled": {{boolean}}
            },
            "Schedules": { 
               "Enabled": {{boolean}}
            },
            "SharedView": { 
               "Enabled": {{boolean}}
            },
            "StatePersistence": { 
               "Enabled": {{boolean}}
            },
            "ThresholdAlerts": { 
               "Enabled": {{boolean}}
            }
         },
         "InitialPath": "{{string}}"
      }
   },
   "SessionLifetimeInMinutes": {{number}},
   "UserArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GenerateEmbedUrlForRegisteredUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_GenerateEmbedUrlForRegisteredUser_RequestSyntax) **   <a name="QS-GenerateEmbedUrlForRegisteredUser-request-uri-AwsAccountId"></a>
The ID for the AWS account that contains the dashboard that you're embedding.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_GenerateEmbedUrlForRegisteredUser_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ExperienceConfiguration](#API_GenerateEmbedUrlForRegisteredUser_RequestSyntax) **   <a name="QS-GenerateEmbedUrlForRegisteredUser-request-ExperienceConfiguration"></a>
The experience that you want to embed. For registered users, you can embed Quick dashboards, Amazon Quick Sight visuals, the Amazon Quick Sight Q search bar, the Amazon Quick Sight Generative Q&A experience, or the entire Amazon Quick Sight console.  
Type: [RegisteredUserEmbeddingExperienceConfiguration](API_RegisteredUserEmbeddingExperienceConfiguration.md) object  
Required: Yes

 ** [UserArn](#API_GenerateEmbedUrlForRegisteredUser_RequestSyntax) **   <a name="QS-GenerateEmbedUrlForRegisteredUser-request-UserArn"></a>
The Amazon Resource Name for the registered user.  
Type: String  
Required: Yes

 ** [AllowedDomains](#API_GenerateEmbedUrlForRegisteredUser_RequestSyntax) **   <a name="QS-GenerateEmbedUrlForRegisteredUser-request-AllowedDomains"></a>
The domains that you want to add to the allow list for access to the generated URL that is then embedded. This optional parameter overrides the static domains that are configured in the Manage Quick Sight menu in the Amazon Quick Sight console. Instead, it allows only the domains that you include in this parameter. You can list up to three domains or subdomains in each API call.  
To include all subdomains under a specific domain to the allow list, use `*`. For example, `https://*.sapp.amazon.com` includes all subdomains under `https://sapp.amazon.com`.  
Type: Array of strings  
Required: No

 ** [SessionLifetimeInMinutes](#API_GenerateEmbedUrlForRegisteredUser_RequestSyntax) **   <a name="QS-GenerateEmbedUrlForRegisteredUser-request-SessionLifetimeInMinutes"></a>
How many minutes the session is valid. The session lifetime must be in [15-600] minutes range.  
Type: Long  
Valid Range: Minimum value of 15. Maximum value of 600.  
Required: No

## Response Syntax
<a name="API_GenerateEmbedUrlForRegisteredUser_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "EmbedUrl": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_GenerateEmbedUrlForRegisteredUser_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_GenerateEmbedUrlForRegisteredUser_ResponseSyntax) **   <a name="QS-GenerateEmbedUrlForRegisteredUser-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [EmbedUrl](#API_GenerateEmbedUrlForRegisteredUser_ResponseSyntax) **   <a name="QS-GenerateEmbedUrlForRegisteredUser-response-EmbedUrl"></a>
The embed URL for the Amazon Quick Sight dashboard, visual, Q search bar, Generative Q&A experience, or console.  
Type: String

 ** [RequestId](#API_GenerateEmbedUrlForRegisteredUser_ResponseSyntax) **   <a name="QS-GenerateEmbedUrlForRegisteredUser-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_GenerateEmbedUrlForRegisteredUser_Errors"></a>

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

 ** QuickSightUserNotFoundException **   
The user with the provided name isn't found. This error can happen in any operation that requires finding a user based on a provided user name, such as `DeleteUser`, `DescribeUser`, and so on.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 404

 ** ResourceNotFoundException **   
One or more resources can't be found.    
 ** RequestId **   
The AWS request ID for this request.  
 ** ResourceType **   
The resource type for this request.
HTTP Status Code: 404

 ** SessionLifetimeInMinutesInvalidException **   
The number of minutes specified for the lifetime of a session isn't valid. The session lifetime must be 15-600 minutes.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 400

 ** ThrottlingException **   
Access is throttled.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedPricingPlanException **   
This error indicates that you are calling an embedding operation in Amazon Quick Sight without the required pricing plan on your AWS account. Before you can use embedding for anonymous users, a Quick Suite administrator needs to add capacity pricing to Quick Sight. You can do this on the **Manage Quick Suite** page.   
After capacity pricing is added, you can use the ` [GetDashboardEmbedUrl](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GetDashboardEmbedUrl.html) ` API operation with the `--identity-type ANONYMOUS` option.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

 ** UnsupportedUserEditionException **   
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.    
 ** RequestId **   
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_GenerateEmbedUrlForRegisteredUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUser) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUser) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUser) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUser) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUser) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUser) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUser) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUser) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUser) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUser) 