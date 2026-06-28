---
id: "@specs/aws/quicksight/docs/API_GenerateEmbedUrlForRegisteredUserWithIdentity"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS GenerateEmbedUrlForRegisteredUserWithIdentity"
status: active
depends_on:
  - "@specs/aws/quicksight/meta"
---

# GenerateEmbedUrlForRegisteredUserWithIdentity

> **source:** AWS Documentation
> **spec:id:** @specs/aws/quicksight/docs/API_GenerateEmbedUrlForRegisteredUserWithIdentity
> **target_lang:** meta — documentation tier. ALL sections preserved.



# GenerateEmbedUrlForRegisteredUserWithIdentity
<a name="API_GenerateEmbedUrlForRegisteredUserWithIdentity"></a>

Generates an embed URL that you can use to embed an Amazon Quick Sight experience in your website. This action can be used for any type of user that is registered in an Amazon Quick Sight account that uses IAM Identity Center for authentication. This API requires [identity-enhanced IAM Role sessions](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html#types-identity-enhanced-iam-role-sessions) for the authenticated user that the API call is being made for.

This API uses [trusted identity propagation](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation.html) to ensure that an end user is authenticated and receives the embed URL that is specific to that user. The IAM Identity Center application that the user has logged into needs to have [trusted Identity Propagation enabled for Amazon Quick Sight](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-using-customermanagedapps-specify-trusted-apps.html) with the scope value set to `quicksight:read`. Before you use this action, make sure that you have configured the relevant Amazon Quick Sight resource and permissions.

## Request Syntax
<a name="API_GenerateEmbedUrlForRegisteredUserWithIdentity_RequestSyntax"></a>

```
POST /accounts/{{AwsAccountId}}/embed-url/registered-user-with-identity HTTP/1.1
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
   "SessionLifetimeInMinutes": {{number}}
}
```

## URI Request Parameters
<a name="API_GenerateEmbedUrlForRegisteredUserWithIdentity_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AwsAccountId](#API_GenerateEmbedUrlForRegisteredUserWithIdentity_RequestSyntax) **   <a name="QS-GenerateEmbedUrlForRegisteredUserWithIdentity-request-uri-AwsAccountId"></a>
The ID of the AWS registered user.  
Length Constraints: Fixed length of 12.  
Pattern: `^[0-9]{12}$`   
Required: Yes

## Request Body
<a name="API_GenerateEmbedUrlForRegisteredUserWithIdentity_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ExperienceConfiguration](#API_GenerateEmbedUrlForRegisteredUserWithIdentity_RequestSyntax) **   <a name="QS-GenerateEmbedUrlForRegisteredUserWithIdentity-request-ExperienceConfiguration"></a>
The type of experience you want to embed. For registered users, you can embed Quick dashboards or the Amazon Quick Sight console.  
Exactly one of the experience configurations is required. You can choose `Dashboard` or `QuickSightConsole`. You cannot choose more than one experience configuration.
Type: [RegisteredUserEmbeddingExperienceConfiguration](API_RegisteredUserEmbeddingExperienceConfiguration.md) object  
Required: Yes

 ** [AllowedDomains](#API_GenerateEmbedUrlForRegisteredUserWithIdentity_RequestSyntax) **   <a name="QS-GenerateEmbedUrlForRegisteredUserWithIdentity-request-AllowedDomains"></a>
A list of domains to be allowed to generate the embed URL.  
Type: Array of strings  
Required: No

 ** [SessionLifetimeInMinutes](#API_GenerateEmbedUrlForRegisteredUserWithIdentity_RequestSyntax) **   <a name="QS-GenerateEmbedUrlForRegisteredUserWithIdentity-request-SessionLifetimeInMinutes"></a>
The validity of the session in minutes.  
Type: Long  
Valid Range: Minimum value of 15. Maximum value of 600.  
Required: No

## Response Syntax
<a name="API_GenerateEmbedUrlForRegisteredUserWithIdentity_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "EmbedUrl": "string",
   "RequestId": "string"
}
```

## Response Elements
<a name="API_GenerateEmbedUrlForRegisteredUserWithIdentity_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_GenerateEmbedUrlForRegisteredUserWithIdentity_ResponseSyntax) **   <a name="QS-GenerateEmbedUrlForRegisteredUserWithIdentity-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [EmbedUrl](#API_GenerateEmbedUrlForRegisteredUserWithIdentity_ResponseSyntax) **   <a name="QS-GenerateEmbedUrlForRegisteredUserWithIdentity-response-EmbedUrl"></a>
The generated embed URL for the registered user.  
Type: String

 ** [RequestId](#API_GenerateEmbedUrlForRegisteredUserWithIdentity_ResponseSyntax) **   <a name="QS-GenerateEmbedUrlForRegisteredUserWithIdentity-response-RequestId"></a>
The AWS request ID for this operation.  
Type: String

## Errors
<a name="API_GenerateEmbedUrlForRegisteredUserWithIdentity_Errors"></a>

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
<a name="API_GenerateEmbedUrlForRegisteredUserWithIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUserWithIdentity) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUserWithIdentity) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUserWithIdentity) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUserWithIdentity) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUserWithIdentity) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUserWithIdentity) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUserWithIdentity) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUserWithIdentity) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUserWithIdentity) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/GenerateEmbedUrlForRegisteredUserWithIdentity) 