---
id: "@specs/aws/network-firewall/docs/API_DescribeRuleGroupMetadata"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeRuleGroupMetadata"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# DescribeRuleGroupMetadata

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_DescribeRuleGroupMetadata
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeRuleGroupMetadata
<a name="API_DescribeRuleGroupMetadata"></a>

High-level information about a rule group, returned by operations like create and describe. You can use the information provided in the metadata to retrieve and manage a rule group. You can retrieve all objects for a rule group by calling [DescribeRuleGroup](API_DescribeRuleGroup.md). 

## Request Syntax
<a name="API_DescribeRuleGroupMetadata_RequestSyntax"></a>

```
{
   "RuleGroupArn": "{{string}}",
   "RuleGroupName": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeRuleGroupMetadata_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RuleGroupArn](#API_DescribeRuleGroupMetadata_RequestSyntax) **   <a name="networkfirewall-DescribeRuleGroupMetadata-request-RuleGroupArn"></a>
The descriptive name of the rule group. You can't change the name of a rule group after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [RuleGroupName](#API_DescribeRuleGroupMetadata_RequestSyntax) **   <a name="networkfirewall-DescribeRuleGroupMetadata-request-RuleGroupName"></a>
The descriptive name of the rule group. You can't change the name of a rule group after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [Type](#API_DescribeRuleGroupMetadata_RequestSyntax) **   <a name="networkfirewall-DescribeRuleGroupMetadata-request-Type"></a>
Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules.   
This setting is required for requests that do not include the `RuleGroupARN`.
Type: String  
Valid Values: `STATELESS | STATEFUL | STATEFUL_DOMAIN`   
Required: No

## Response Syntax
<a name="API_DescribeRuleGroupMetadata_ResponseSyntax"></a>

```
{
   "Capacity": number,
   "Description": "string",
   "LastModifiedTime": number,
   "ListingName": "string",
   "ProductId": "string",
   "RuleGroupArn": "string",
   "RuleGroupName": "string",
   "StatefulRuleOptions": { 
      "RuleOrder": "string"
   },
   "Type": "string",
   "VendorName": "string"
}
```

## Response Elements
<a name="API_DescribeRuleGroupMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Capacity](#API_DescribeRuleGroupMetadata_ResponseSyntax) **   <a name="networkfirewall-DescribeRuleGroupMetadata-response-Capacity"></a>
The maximum operating resources that this rule group can use. Rule group capacity is fixed at creation. When you update a rule group, you are limited to this capacity. When you reference a rule group from a firewall policy, Network Firewall reserves this capacity for the rule group.   
You can retrieve the capacity that would be required for a rule group before you create the rule group by calling [CreateRuleGroup](API_CreateRuleGroup.md) with `DryRun` set to `TRUE`.   
Type: Integer

 ** [Description](#API_DescribeRuleGroupMetadata_ResponseSyntax) **   <a name="networkfirewall-DescribeRuleGroupMetadata-response-Description"></a>
Returns the metadata objects for the specified rule group.   
Type: String  
Length Constraints: Maximum length of 512.  
Pattern: `^.*$` 

 ** [LastModifiedTime](#API_DescribeRuleGroupMetadata_ResponseSyntax) **   <a name="networkfirewall-DescribeRuleGroupMetadata-response-LastModifiedTime"></a>
A timestamp indicating when the rule group was last modified.  
Type: Timestamp

 ** [ListingName](#API_DescribeRuleGroupMetadata_ResponseSyntax) **   <a name="networkfirewall-DescribeRuleGroupMetadata-response-ListingName"></a>
The display name of the product listing for this rule group.  
Type: String

 ** [ProductId](#API_DescribeRuleGroupMetadata_ResponseSyntax) **   <a name="networkfirewall-DescribeRuleGroupMetadata-response-ProductId"></a>
The unique identifier for the product listing associated with this rule group.  
Type: String

 ** [RuleGroupArn](#API_DescribeRuleGroupMetadata_ResponseSyntax) **   <a name="networkfirewall-DescribeRuleGroupMetadata-response-RuleGroupArn"></a>
The descriptive name of the rule group. You can't change the name of a rule group after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*` 

 ** [RuleGroupName](#API_DescribeRuleGroupMetadata_ResponseSyntax) **   <a name="networkfirewall-DescribeRuleGroupMetadata-response-RuleGroupName"></a>
The descriptive name of the rule group. You can't change the name of a rule group after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$` 

 ** [StatefulRuleOptions](#API_DescribeRuleGroupMetadata_ResponseSyntax) **   <a name="networkfirewall-DescribeRuleGroupMetadata-response-StatefulRuleOptions"></a>
Additional options governing how Network Firewall handles the rule group. You can only use these for stateful rule groups.  
Type: [StatefulRuleOptions](API_StatefulRuleOptions.md) object

 ** [Type](#API_DescribeRuleGroupMetadata_ResponseSyntax) **   <a name="networkfirewall-DescribeRuleGroupMetadata-response-Type"></a>
Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules.   
This setting is required for requests that do not include the `RuleGroupARN`.
Type: String  
Valid Values: `STATELESS | STATEFUL | STATEFUL_DOMAIN` 

 ** [VendorName](#API_DescribeRuleGroupMetadata_ResponseSyntax) **   <a name="networkfirewall-DescribeRuleGroupMetadata-response-VendorName"></a>
The name of the AWS Marketplace vendor that provides this rule group.  
Type: String

## Errors
<a name="API_DescribeRuleGroupMetadata_Errors"></a>

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

 ** ResourceNotFoundException **   
Unable to locate a resource using the parameters that you provided.  
HTTP Status Code: 400

 ** ThrottlingException **   
Unable to process the request due to throttling limitations.  
HTTP Status Code: 400

## See Also
<a name="API_DescribeRuleGroupMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DescribeRuleGroupMetadata) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DescribeRuleGroupMetadata) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DescribeRuleGroupMetadata) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DescribeRuleGroupMetadata) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DescribeRuleGroupMetadata) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DescribeRuleGroupMetadata) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DescribeRuleGroupMetadata) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DescribeRuleGroupMetadata) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DescribeRuleGroupMetadata) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DescribeRuleGroupMetadata) 