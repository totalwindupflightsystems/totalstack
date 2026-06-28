---
id: "@specs/aws/network-firewall/docs/API_ListRuleGroups"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListRuleGroups"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ListRuleGroups

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ListRuleGroups
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListRuleGroups
<a name="API_ListRuleGroups"></a>

Retrieves the metadata for the rule groups that you have defined. Depending on your setting for max results and the number of rule groups, a single call might not return the full list. 

## Request Syntax
<a name="API_ListRuleGroups_RequestSyntax"></a>

```
{
   "ManagedType": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "Scope": "{{string}}",
   "SubscriptionStatus": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_ListRuleGroups_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ManagedType](#API_ListRuleGroups_RequestSyntax) **   <a name="networkfirewall-ListRuleGroups-request-ManagedType"></a>
Indicates the general category of the AWS managed rule group.  
Type: String  
Valid Values: `AWS_MANAGED_THREAT_SIGNATURES | AWS_MANAGED_DOMAIN_LISTS | ACTIVE_THREAT_DEFENSE | PARTNER_MANAGED`   
Required: No

 ** [MaxResults](#API_ListRuleGroups_RequestSyntax) **   <a name="networkfirewall-ListRuleGroups-request-MaxResults"></a>
The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a `NextToken` value that you can use in a subsequent call to get the next batch of objects.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListRuleGroups_RequestSyntax) **   <a name="networkfirewall-ListRuleGroups-request-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `[0-9A-Za-z:\/+=]+$`   
Required: No

 ** [Scope](#API_ListRuleGroups_RequestSyntax) **   <a name="networkfirewall-ListRuleGroups-request-Scope"></a>
The scope of the request. The default setting of `ACCOUNT` or a setting of `NULL` returns all of the rule groups in your account. A setting of `MANAGED` returns all available managed rule groups.  
Type: String  
Valid Values: `MANAGED | ACCOUNT`   
Required: No

 ** [SubscriptionStatus](#API_ListRuleGroups_RequestSyntax) **   <a name="networkfirewall-ListRuleGroups-request-SubscriptionStatus"></a>
Filters the results to show only rule groups with the specified subscription status. Use this to find subscribed or unsubscribed rule groups.  
Type: String  
Valid Values: `NOT_SUBSCRIBED | SUBSCRIBED`   
Required: No

 ** [Type](#API_ListRuleGroups_RequestSyntax) **   <a name="networkfirewall-ListRuleGroups-request-Type"></a>
Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules.  
Type: String  
Valid Values: `STATELESS | STATEFUL | STATEFUL_DOMAIN`   
Required: No

## Response Syntax
<a name="API_ListRuleGroups_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "RuleGroups": [ 
      { 
         "Arn": "string",
         "Name": "string",
         "VendorName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRuleGroups_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListRuleGroups_ResponseSyntax) **   <a name="networkfirewall-ListRuleGroups-response-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `[0-9A-Za-z:\/+=]+$` 

 ** [RuleGroups](#API_ListRuleGroups_ResponseSyntax) **   <a name="networkfirewall-ListRuleGroups-response-RuleGroups"></a>
The rule group metadata objects that you've defined. Depending on your setting for max results and the number of rule groups, this might not be the full list.   
Type: Array of [RuleGroupMetadata](API_RuleGroupMetadata.md) objects

## Errors
<a name="API_ListRuleGroups_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request.   
HTTP Status Code: 500

 ** InvalidRequestException **   
The operation failed because of a problem with your request. Examples include:   
+ You specified an unsupported parameter name or value.
+ You tried to update a property with a value that isn't among the available types.
+ Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.
HTTP Status Code: 400

 ** ThrottlingException **   
Unable to process the request due to throttling limitations.  
HTTP Status Code: 400

## See Also
<a name="API_ListRuleGroups_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/ListRuleGroups) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/ListRuleGroups) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ListRuleGroups) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/ListRuleGroups) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ListRuleGroups) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/ListRuleGroups) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/ListRuleGroups) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/ListRuleGroups) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/ListRuleGroups) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ListRuleGroups) 