---
id: "@specs/aws/network-firewall/docs/API_DeleteRuleGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteRuleGroup"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# DeleteRuleGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_DeleteRuleGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteRuleGroup
<a name="API_DeleteRuleGroup"></a>

Deletes the specified [RuleGroup](API_RuleGroup.md). 

## Request Syntax
<a name="API_DeleteRuleGroup_RequestSyntax"></a>

```
{
   "RuleGroupArn": "{{string}}",
   "RuleGroupName": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteRuleGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RuleGroupArn](#API_DeleteRuleGroup_RequestSyntax) **   <a name="networkfirewall-DeleteRuleGroup-request-RuleGroupArn"></a>
The Amazon Resource Name (ARN) of the rule group.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [RuleGroupName](#API_DeleteRuleGroup_RequestSyntax) **   <a name="networkfirewall-DeleteRuleGroup-request-RuleGroupName"></a>
The descriptive name of the rule group. You can't change the name of a rule group after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [Type](#API_DeleteRuleGroup_RequestSyntax) **   <a name="networkfirewall-DeleteRuleGroup-request-Type"></a>
Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules.   
This setting is required for requests that do not include the `RuleGroupARN`.
Type: String  
Valid Values: `STATELESS | STATEFUL | STATEFUL_DOMAIN`   
Required: No

## Response Syntax
<a name="API_DeleteRuleGroup_ResponseSyntax"></a>

```
{
   "RuleGroupResponse": { 
      "AnalysisResults": [ 
         { 
            "AnalysisDetail": "string",
            "IdentifiedRuleIds": [ "string" ],
            "IdentifiedType": "string"
         }
      ],
      "Capacity": number,
      "ConsumedCapacity": number,
      "Description": "string",
      "EncryptionConfiguration": { 
         "KeyId": "string",
         "Type": "string"
      },
      "LastModifiedTime": number,
      "NumberOfAssociations": number,
      "RuleGroupArn": "string",
      "RuleGroupId": "string",
      "RuleGroupName": "string",
      "RuleGroupStatus": "string",
      "SnsTopic": "string",
      "SourceMetadata": { 
         "SourceArn": "string",
         "SourceUpdateToken": "string"
      },
      "SummaryConfiguration": { 
         "RuleOptions": [ "string" ]
      },
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ],
      "Type": "string"
   }
}
```

## Response Elements
<a name="API_DeleteRuleGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RuleGroupResponse](#API_DeleteRuleGroup_ResponseSyntax) **   <a name="networkfirewall-DeleteRuleGroup-response-RuleGroupResponse"></a>
The high-level properties of a rule group. This, along with the [RuleGroup](API_RuleGroup.md), define the rule group. You can retrieve all objects for a rule group by calling [DescribeRuleGroup](API_DescribeRuleGroup.md).   
Type: [RuleGroupResponse](API_RuleGroupResponse.md) object

## Errors
<a name="API_DeleteRuleGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request.   
HTTP Status Code: 500

 ** InvalidOperationException **   
The operation failed because it's not valid. For example, you might have tried to delete a rule group or firewall policy that's in use.  
HTTP Status Code: 400

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

 ** UnsupportedOperationException **   
The operation you requested isn't supported by Network Firewall.   
HTTP Status Code: 400

## See Also
<a name="API_DeleteRuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DeleteRuleGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DeleteRuleGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DeleteRuleGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DeleteRuleGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DeleteRuleGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DeleteRuleGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DeleteRuleGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DeleteRuleGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DeleteRuleGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DeleteRuleGroup) 