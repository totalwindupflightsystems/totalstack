---
id: "@specs/aws/wafv2/docs/API_DescribeManagedRuleGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeManagedRuleGroup"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# DescribeManagedRuleGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_DescribeManagedRuleGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeManagedRuleGroup
<a name="API_DescribeManagedRuleGroup"></a>

Provides high-level information for a managed rule group, including descriptions of the rules. 

## Request Syntax
<a name="API_DescribeManagedRuleGroup_RequestSyntax"></a>

```
{
   "Name": "{{string}}",
   "Scope": "{{string}}",
   "VendorName": "{{string}}",
   "VersionName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeManagedRuleGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_DescribeManagedRuleGroup_RequestSyntax) **   <a name="WAF-DescribeManagedRuleGroup-request-Name"></a>
The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[\w\-]+$`   
Required: Yes

 ** [Scope](#API_DescribeManagedRuleGroup_RequestSyntax) **   <a name="WAF-DescribeManagedRuleGroup-request-Scope"></a>
Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an AWS Amplify application, use `CLOUDFRONT`.  
To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:   
+ CLI - Specify the Region when you use the CloudFront scope: `--scope=CLOUDFRONT --region=us-east-1`. 
+ API and SDKs - For all calls, use the Region endpoint us-east-1. 
Type: String  
Valid Values: `CLOUDFRONT | REGIONAL`   
Required: Yes

 ** [VendorName](#API_DescribeManagedRuleGroup_RequestSyntax) **   <a name="WAF-DescribeManagedRuleGroup-request-VendorName"></a>
The name of the managed rule group vendor. You use this, along with the rule group name, to identify a rule group.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `.*\S.*`   
Required: Yes

 ** [VersionName](#API_DescribeManagedRuleGroup_RequestSyntax) **   <a name="WAF-DescribeManagedRuleGroup-request-VersionName"></a>
The version of the rule group. You can only use a version that is not scheduled for expiration. If you don't provide this, AWS WAF uses the vendor's default version.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `^[\w#:\.\-/]+$`   
Required: No

## Response Syntax
<a name="API_DescribeManagedRuleGroup_ResponseSyntax"></a>

```
{
   "AvailableLabels": [ 
      { 
         "Name": "string"
      }
   ],
   "Capacity": number,
   "ConsumedLabels": [ 
      { 
         "Name": "string"
      }
   ],
   "LabelNamespace": "string",
   "Rules": [ 
      { 
         "Action": { 
            "Allow": { 
               "CustomRequestHandling": { 
                  "InsertHeaders": [ 
                     { 
                        "Name": "string",
                        "Value": "string"
                     }
                  ]
               }
            },
            "Block": { 
               "CustomResponse": { 
                  "CustomResponseBodyKey": "string",
                  "ResponseCode": number,
                  "ResponseHeaders": [ 
                     { 
                        "Name": "string",
                        "Value": "string"
                     }
                  ]
               }
            },
            "Captcha": { 
               "CustomRequestHandling": { 
                  "InsertHeaders": [ 
                     { 
                        "Name": "string",
                        "Value": "string"
                     }
                  ]
               }
            },
            "Challenge": { 
               "CustomRequestHandling": { 
                  "InsertHeaders": [ 
                     { 
                        "Name": "string",
                        "Value": "string"
                     }
                  ]
               }
            },
            "Count": { 
               "CustomRequestHandling": { 
                  "InsertHeaders": [ 
                     { 
                        "Name": "string",
                        "Value": "string"
                     }
                  ]
               }
            },
            "Monetize": { 
               "PriceMultiplier": "string"
            }
         },
         "Name": "string"
      }
   ],
   "SnsTopicArn": "string",
   "VersionName": "string"
}
```

## Response Elements
<a name="API_DescribeManagedRuleGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AvailableLabels](#API_DescribeManagedRuleGroup_ResponseSyntax) **   <a name="WAF-DescribeManagedRuleGroup-response-AvailableLabels"></a>
The labels that one or more rules in this rule group add to matching web requests. These labels are defined in the `RuleLabels` for a [Rule](API_Rule.md).  
Type: Array of [LabelSummary](API_LabelSummary.md) objects

 ** [Capacity](#API_DescribeManagedRuleGroup_ResponseSyntax) **   <a name="WAF-DescribeManagedRuleGroup-response-Capacity"></a>
The web ACL capacity units (WCUs) required for this rule group.  
 AWS WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. AWS WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. For more information, see [AWS WAF web ACL capacity units (WCU)](https://docs.aws.amazon.com/waf/latest/developerguide/aws-waf-capacity-units.html) in the * AWS WAF Developer Guide*.   
Type: Long  
Valid Range: Minimum value of 1.

 ** [ConsumedLabels](#API_DescribeManagedRuleGroup_ResponseSyntax) **   <a name="WAF-DescribeManagedRuleGroup-response-ConsumedLabels"></a>
The labels that one or more rules in this rule group match against in label match statements. These labels are defined in a `LabelMatchStatement` specification, in the [Statement](API_Statement.md) definition of a rule.   
Type: Array of [LabelSummary](API_LabelSummary.md) objects

 ** [LabelNamespace](#API_DescribeManagedRuleGroup_ResponseSyntax) **   <a name="WAF-DescribeManagedRuleGroup-response-LabelNamespace"></a>
The label namespace prefix for this rule group. All labels added by rules in this rule group have this prefix.   
+ The syntax for the label namespace prefix for a managed rule group is the following: 

   `awswaf:managed:<vendor>:<rule group name>`:
+ When a rule with a label matches a web request, AWS WAF adds the fully qualified label to the request. A fully qualified label is made up of the label namespace from the rule group or web ACL where the rule is defined and the label from the rule, separated by a colon: 

   `<label namespace>:<label from rule>` 
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^[0-9A-Za-z_\-:]+$` 

 ** [Rules](#API_DescribeManagedRuleGroup_ResponseSyntax) **   <a name="WAF-DescribeManagedRuleGroup-response-Rules"></a>
  
Type: Array of [RuleSummary](API_RuleSummary.md) objects

 ** [SnsTopicArn](#API_DescribeManagedRuleGroup_ResponseSyntax) **   <a name="WAF-DescribeManagedRuleGroup-response-SnsTopicArn"></a>
The Amazon resource name (ARN) of the Amazon Simple Notification Service SNS topic that's used to provide notification of changes to the managed rule group. You can subscribe to the SNS topic to receive notifications when the managed rule group is modified, such as for new versions and for version expiration. For more information, see the [Amazon Simple Notification Service Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/welcome.html).  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `.*\S.*` 

 ** [VersionName](#API_DescribeManagedRuleGroup_ResponseSyntax) **   <a name="WAF-DescribeManagedRuleGroup-response-VersionName"></a>
The managed rule group's version.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `^[\w#:\.\-/]+$` 

## Errors
<a name="API_DescribeManagedRuleGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** WAFExpiredManagedRuleGroupVersionException **   
The operation failed because the specified version for the managed rule group has expired. You can retrieve the available versions for the managed rule group by calling [ListAvailableManagedRuleGroupVersions](API_ListAvailableManagedRuleGroupVersions.md).  
HTTP Status Code: 400

 ** WAFInternalErrorException **   
Your request is valid, but AWS WAF couldn’t perform the operation because of a system problem. Retry your request.   
HTTP Status Code: 500

 ** WAFInvalidOperationException **   
The operation isn't valid.   
HTTP Status Code: 400

 ** WAFInvalidParameterException **   
The operation failed because AWS WAF didn't recognize a parameter in the request. For example:   
+ You specified a parameter name or value that isn't valid.
+ Your nested statement isn't valid. You might have tried to nest a statement that can’t be nested. 
+ You tried to update a `WebACL` with a `DefaultAction` that isn't among the types available at [DefaultAction](API_DefaultAction.md).
+ Your request references an ARN that is malformed, or corresponds to a resource with which a web ACL can't be associated.  
 ** Field **   
The settings where the invalid parameter was found.   
 ** Parameter **   
The invalid parameter that resulted in the exception.   
 ** Reason **   
Additional information about the exception.
HTTP Status Code: 400

 ** WAFInvalidResourceException **   
 AWS WAF couldn’t perform the operation because the resource that you requested isn’t valid. Check the resource, and try again.  
HTTP Status Code: 400

 ** WAFNonexistentItemException **   
 AWS WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate.   
HTTP Status Code: 400

## See Also
<a name="API_DescribeManagedRuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wafv2-2019-07-29/DescribeManagedRuleGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wafv2-2019-07-29/DescribeManagedRuleGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/DescribeManagedRuleGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wafv2-2019-07-29/DescribeManagedRuleGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/DescribeManagedRuleGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wafv2-2019-07-29/DescribeManagedRuleGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wafv2-2019-07-29/DescribeManagedRuleGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wafv2-2019-07-29/DescribeManagedRuleGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wafv2-2019-07-29/DescribeManagedRuleGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/DescribeManagedRuleGroup) 