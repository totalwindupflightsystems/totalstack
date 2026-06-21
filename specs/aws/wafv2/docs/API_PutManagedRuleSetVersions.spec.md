---
id: "@specs/aws/wafv2/docs/API_PutManagedRuleSetVersions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutManagedRuleSetVersions"
status: active
depends_on:
  - "@specs/aws/wafv2/meta"
---

# PutManagedRuleSetVersions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/wafv2/docs/API_PutManagedRuleSetVersions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutManagedRuleSetVersions
<a name="API_PutManagedRuleSetVersions"></a>

Defines the versions of your managed rule set that you are offering to the customers. Customers see your offerings as managed rule groups with versioning.

**Note**  
This is intended for use only by vendors of managed rule sets. Vendors are AWS and AWS Marketplace sellers.   
Vendors, you can use the managed rule set APIs to provide controlled rollout of your versioned managed rule group offerings for your customers. The APIs are `ListManagedRuleSets`, `GetManagedRuleSet`, `PutManagedRuleSetVersions`, and `UpdateManagedRuleSetVersionExpiryDate`.

Customers retrieve their managed rule group list by calling [ListAvailableManagedRuleGroups](API_ListAvailableManagedRuleGroups.md). The name that you provide here for your managed rule set is the name the customer sees for the corresponding managed rule group. Customers can retrieve the available versions for a managed rule group by calling [ListAvailableManagedRuleGroupVersions](API_ListAvailableManagedRuleGroupVersions.md). You provide a rule group specification for each version. For each managed rule set, you must specify a version that you recommend using. 

To initiate the expiration of a managed rule group version, use [UpdateManagedRuleSetVersionExpiryDate](API_UpdateManagedRuleSetVersionExpiryDate.md).

## Request Syntax
<a name="API_PutManagedRuleSetVersions_RequestSyntax"></a>

```
{
   "Id": "{{string}}",
   "LockToken": "{{string}}",
   "Name": "{{string}}",
   "RecommendedVersion": "{{string}}",
   "Scope": "{{string}}",
   "VersionsToPublish": { 
      "{{string}}" : { 
         "AssociatedRuleGroupArn": "{{string}}",
         "ForecastedLifetime": {{number}}
      }
   }
}
```

## Request Parameters
<a name="API_PutManagedRuleSetVersions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Id](#API_PutManagedRuleSetVersions_RequestSyntax) **   <a name="WAF-PutManagedRuleSetVersions-request-Id"></a>
A unique identifier for the managed rule set. The ID is returned in the responses to commands like `list`. You provide it to operations like `get` and `update`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 36.  
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`   
Required: Yes

 ** [LockToken](#API_PutManagedRuleSetVersions_RequestSyntax) **   <a name="WAF-PutManagedRuleSetVersions-request-LockToken"></a>
A token used for optimistic locking. AWS WAF returns a token to your `get` and `list` requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like `update` and `delete`. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a `WAFOptimisticLockException`. If this happens, perform another `get`, and use the new token returned by that operation.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 36.  
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$`   
Required: Yes

 ** [Name](#API_PutManagedRuleSetVersions_RequestSyntax) **   <a name="WAF-PutManagedRuleSetVersions-request-Name"></a>
The name of the managed rule set. You use this, along with the rule set ID, to identify the rule set.  
This name is assigned to the corresponding managed rule group, which your customers can access and use.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[\w\-]+$`   
Required: Yes

 ** [RecommendedVersion](#API_PutManagedRuleSetVersions_RequestSyntax) **   <a name="WAF-PutManagedRuleSetVersions-request-RecommendedVersion"></a>
The version of the named managed rule group that you'd like your customers to choose, from among your version offerings.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `^[\w#:\.\-/]+$`   
Required: No

 ** [Scope](#API_PutManagedRuleSetVersions_RequestSyntax) **   <a name="WAF-PutManagedRuleSetVersions-request-Scope"></a>
Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an AWS Amplify application, use `CLOUDFRONT`.  
To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:   
+ CLI - Specify the Region when you use the CloudFront scope: `--scope=CLOUDFRONT --region=us-east-1`. 
+ API and SDKs - For all calls, use the Region endpoint us-east-1. 
Type: String  
Valid Values: `CLOUDFRONT | REGIONAL`   
Required: Yes

 ** [VersionsToPublish](#API_PutManagedRuleSetVersions_RequestSyntax) **   <a name="WAF-PutManagedRuleSetVersions-request-VersionsToPublish"></a>
The versions of the named managed rule group that you want to offer to your customers.   
Type: String to [VersionToPublish](API_VersionToPublish.md) object map  
Key Length Constraints: Minimum length of 1. Maximum length of 64.  
Key Pattern: `^[\w#:\.\-/]+$`   
Required: No

## Response Syntax
<a name="API_PutManagedRuleSetVersions_ResponseSyntax"></a>

```
{
   "NextLockToken": "string"
}
```

## Response Elements
<a name="API_PutManagedRuleSetVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextLockToken](#API_PutManagedRuleSetVersions_ResponseSyntax) **   <a name="WAF-PutManagedRuleSetVersions-response-NextLockToken"></a>
A token used for optimistic locking. AWS WAF returns a token to your `get` and `list` requests, to mark the state of the entity at the time of the request. To make changes to the entity associated with the token, you provide the token to operations like `update` and `delete`. AWS WAF uses the token to ensure that no changes have been made to the entity since you last retrieved it. If a change has been made, the update fails with a `WAFOptimisticLockException`. If this happens, perform another `get`, and use the new token returned by that operation.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 36.  
Pattern: `^[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}$` 

## Errors
<a name="API_PutManagedRuleSetVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** WAFNonexistentItemException **   
 AWS WAF couldn’t perform the operation because your resource doesn't exist. If you've just created a resource that you're using in this operation, you might just need to wait a few minutes. It can take from a few seconds to a number of minutes for changes to propagate.   
HTTP Status Code: 400

 ** WAFOptimisticLockException **   
 AWS WAF couldn’t save your changes because you tried to update or delete a resource that has changed since you last retrieved it. Get the resource again, make any changes you need to make to the new copy, and retry your operation.   
HTTP Status Code: 400

## See Also
<a name="API_PutManagedRuleSetVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wafv2-2019-07-29/PutManagedRuleSetVersions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wafv2-2019-07-29/PutManagedRuleSetVersions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/PutManagedRuleSetVersions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wafv2-2019-07-29/PutManagedRuleSetVersions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/PutManagedRuleSetVersions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wafv2-2019-07-29/PutManagedRuleSetVersions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wafv2-2019-07-29/PutManagedRuleSetVersions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wafv2-2019-07-29/PutManagedRuleSetVersions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/wafv2-2019-07-29/PutManagedRuleSetVersions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/PutManagedRuleSetVersions) 