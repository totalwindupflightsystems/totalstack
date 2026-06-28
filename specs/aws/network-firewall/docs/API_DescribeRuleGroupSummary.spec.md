---
id: "@specs/aws/network-firewall/docs/API_DescribeRuleGroupSummary"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeRuleGroupSummary"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# DescribeRuleGroupSummary

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_DescribeRuleGroupSummary
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeRuleGroupSummary
<a name="API_DescribeRuleGroupSummary"></a>

Returns detailed information for a stateful rule group.

For active threat defense AWS managed rule groups, this operation provides insight into the protections enabled by the rule group, based on Suricata rule metadata fields. Summaries are available for rule groups you manage and for active threat defense AWS managed rule groups.

To modify how threat information appears in summaries, use the `SummaryConfiguration` parameter in [UpdateRuleGroup](API_UpdateRuleGroup.md).

## Request Syntax
<a name="API_DescribeRuleGroupSummary_RequestSyntax"></a>

```
{
   "RuleGroupArn": "{{string}}",
   "RuleGroupName": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeRuleGroupSummary_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RuleGroupArn](#API_DescribeRuleGroupSummary_RequestSyntax) **   <a name="networkfirewall-DescribeRuleGroupSummary-request-RuleGroupArn"></a>
Required. The Amazon Resource Name (ARN) of the rule group.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [RuleGroupName](#API_DescribeRuleGroupSummary_RequestSyntax) **   <a name="networkfirewall-DescribeRuleGroupSummary-request-RuleGroupName"></a>
The descriptive name of the rule group. You can't change the name of a rule group after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [Type](#API_DescribeRuleGroupSummary_RequestSyntax) **   <a name="networkfirewall-DescribeRuleGroupSummary-request-Type"></a>
The type of rule group you want a summary for. This is a required field.  
Valid value: `STATEFUL`   
Note that `STATELESS` exists but is not currently supported. If you provide `STATELESS`, an exception is returned.  
Type: String  
Valid Values: `STATELESS | STATEFUL | STATEFUL_DOMAIN`   
Required: No

## Response Syntax
<a name="API_DescribeRuleGroupSummary_ResponseSyntax"></a>

```
{
   "Description": "string",
   "RuleGroupName": "string",
   "Summary": { 
      "RuleSummaries": [ 
         { 
            "Metadata": "string",
            "Msg": "string",
            "SID": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_DescribeRuleGroupSummary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_DescribeRuleGroupSummary_ResponseSyntax) **   <a name="networkfirewall-DescribeRuleGroupSummary-response-Description"></a>
A description of the rule group.   
Type: String  
Length Constraints: Maximum length of 512.  
Pattern: `^.*$` 

 ** [RuleGroupName](#API_DescribeRuleGroupSummary_ResponseSyntax) **   <a name="networkfirewall-DescribeRuleGroupSummary-response-RuleGroupName"></a>
The descriptive name of the rule group. You can't change the name of a rule group after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$` 

 ** [Summary](#API_DescribeRuleGroupSummary_ResponseSyntax) **   <a name="networkfirewall-DescribeRuleGroupSummary-response-Summary"></a>
A complex type that contains rule information based on the rule group's configured summary settings. The content varies depending on the fields that you specified to extract in your SummaryConfiguration. When you haven't configured any summary settings, this returns an empty array. The response might include:  
+ Rule identifiers
+ Rule descriptions
+ Any metadata fields that you specified in your SummaryConfiguration
Type: [Summary](API_Summary.md) object

## Errors
<a name="API_DescribeRuleGroupSummary_Errors"></a>

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
<a name="API_DescribeRuleGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DescribeRuleGroupSummary) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DescribeRuleGroupSummary) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DescribeRuleGroupSummary) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DescribeRuleGroupSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DescribeRuleGroupSummary) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DescribeRuleGroupSummary) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DescribeRuleGroupSummary) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DescribeRuleGroupSummary) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DescribeRuleGroupSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DescribeRuleGroupSummary) 