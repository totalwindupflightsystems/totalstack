---
id: "@specs/aws/shield/docs/API_DescribeSubscription"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeSubscription"
status: active
depends_on:
  - "@specs/aws/shield/meta"
---

# DescribeSubscription

> **source:** AWS Documentation
> **spec:id:** @specs/aws/shield/docs/API_DescribeSubscription
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeSubscription
<a name="API_DescribeSubscription"></a>

Provides details about the AWS Shield Advanced subscription for an account.

## Response Syntax
<a name="API_DescribeSubscription_ResponseSyntax"></a>

```
{
   "Subscription": { 
      "AutoRenew": "string",
      "EndTime": number,
      "Limits": [ 
         { 
            "Max": number,
            "Type": "string"
         }
      ],
      "ProactiveEngagementStatus": "string",
      "StartTime": number,
      "SubscriptionArn": "string",
      "SubscriptionLimits": { 
         "ProtectionGroupLimits": { 
            "MaxProtectionGroups": number,
            "PatternTypeLimits": { 
               "ArbitraryPatternLimits": { 
                  "MaxMembers": number
               }
            }
         },
         "ProtectionLimits": { 
            "ProtectedResourceTypeLimits": [ 
               { 
                  "Max": number,
                  "Type": "string"
               }
            ]
         }
      },
      "TimeCommitmentInSeconds": number
   }
}
```

## Response Elements
<a name="API_DescribeSubscription_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Subscription](#API_DescribeSubscription_ResponseSyntax) **   <a name="AWSShield-DescribeSubscription-response-Subscription"></a>
The AWS Shield Advanced subscription details for an account.  
Type: [Subscription](API_Subscription.md) object

## Errors
<a name="API_DescribeSubscription_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **   
Exception that indicates that a problem occurred with the service infrastructure. You can retry the request.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
Exception indicating the specified resource does not exist. If available, this exception includes details in additional properties.     
 ** resourceType **   
Type of resource.
HTTP Status Code: 400

## See Also
<a name="API_DescribeSubscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/shield-2016-06-02/DescribeSubscription) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/shield-2016-06-02/DescribeSubscription) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/DescribeSubscription) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/shield-2016-06-02/DescribeSubscription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/DescribeSubscription) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/shield-2016-06-02/DescribeSubscription) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/shield-2016-06-02/DescribeSubscription) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/shield-2016-06-02/DescribeSubscription) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/shield-2016-06-02/DescribeSubscription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/DescribeSubscription) 