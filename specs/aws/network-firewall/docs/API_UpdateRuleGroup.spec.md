---
id: "@specs/aws/network-firewall/docs/API_UpdateRuleGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateRuleGroup"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# UpdateRuleGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_UpdateRuleGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateRuleGroup
<a name="API_UpdateRuleGroup"></a>

Updates the rule settings for the specified rule group. You use a rule group by reference in one or more firewall policies. When you modify a rule group, you modify all firewall policies that use the rule group. 

To update a rule group, first call [DescribeRuleGroup](API_DescribeRuleGroup.md) to retrieve the current [RuleGroup](API_RuleGroup.md) object, update the object as needed, and then provide the updated object to this call. 

## Request Syntax
<a name="API_UpdateRuleGroup_RequestSyntax"></a>

```
{
   "AnalyzeRuleGroup": {{boolean}},
   "Description": "{{string}}",
   "DryRun": {{boolean}},
   "EncryptionConfiguration": { 
      "KeyId": "{{string}}",
      "Type": "{{string}}"
   },
   "RuleGroup": { 
      "ReferenceSets": { 
         "IPSetReferences": { 
            "{{string}}" : { 
               "ReferenceArn": "{{string}}"
            }
         }
      },
      "RulesSource": { 
         "RulesSourceList": { 
            "GeneratedRulesType": "{{string}}",
            "Targets": [ "{{string}}" ],
            "TargetTypes": [ "{{string}}" ]
         },
         "RulesString": "{{string}}",
         "StatefulRules": [ 
            { 
               "Action": "{{string}}",
               "Header": { 
                  "Destination": "{{string}}",
                  "DestinationPort": "{{string}}",
                  "Direction": "{{string}}",
                  "Protocol": "{{string}}",
                  "Source": "{{string}}",
                  "SourcePort": "{{string}}"
               },
               "RuleOptions": [ 
                  { 
                     "Keyword": "{{string}}",
                     "Settings": [ "{{string}}" ]
                  }
               ]
            }
         ],
         "StatelessRulesAndCustomActions": { 
            "CustomActions": [ 
               { 
                  "ActionDefinition": { 
                     "PublishMetricAction": { 
                        "Dimensions": [ 
                           { 
                              "Value": "{{string}}"
                           }
                        ]
                     }
                  },
                  "ActionName": "{{string}}"
               }
            ],
            "StatelessRules": [ 
               { 
                  "Priority": {{number}},
                  "RuleDefinition": { 
                     "Actions": [ "{{string}}" ],
                     "MatchAttributes": { 
                        "DestinationPorts": [ 
                           { 
                              "FromPort": {{number}},
                              "ToPort": {{number}}
                           }
                        ],
                        "Destinations": [ 
                           { 
                              "AddressDefinition": "{{string}}"
                           }
                        ],
                        "Protocols": [ {{number}} ],
                        "SourcePorts": [ 
                           { 
                              "FromPort": {{number}},
                              "ToPort": {{number}}
                           }
                        ],
                        "Sources": [ 
                           { 
                              "AddressDefinition": "{{string}}"
                           }
                        ],
                        "TCPFlags": [ 
                           { 
                              "Flags": [ "{{string}}" ],
                              "Masks": [ "{{string}}" ]
                           }
                        ]
                     }
                  }
               }
            ]
         }
      },
      "RuleVariables": { 
         "IPSets": { 
            "{{string}}" : { 
               "Definition": [ "{{string}}" ]
            }
         },
         "PortSets": { 
            "{{string}}" : { 
               "Definition": [ "{{string}}" ]
            }
         }
      },
      "StatefulRuleOptions": { 
         "RuleOrder": "{{string}}"
      }
   },
   "RuleGroupArn": "{{string}}",
   "RuleGroupName": "{{string}}",
   "Rules": "{{string}}",
   "SourceMetadata": { 
      "SourceArn": "{{string}}",
      "SourceUpdateToken": "{{string}}"
   },
   "SummaryConfiguration": { 
      "RuleOptions": [ "{{string}}" ]
   },
   "Type": "{{string}}",
   "UpdateToken": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateRuleGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AnalyzeRuleGroup](#API_UpdateRuleGroup_RequestSyntax) **   <a name="networkfirewall-UpdateRuleGroup-request-AnalyzeRuleGroup"></a>
Indicates whether you want Network Firewall to analyze the stateless rules in the rule group for rule behavior such as asymmetric routing. If set to `TRUE`, Network Firewall runs the analysis and then updates the rule group for you. To run the stateless rule group analyzer without updating the rule group, set `DryRun` to `TRUE`.   
Type: Boolean  
Required: No

 ** [Description](#API_UpdateRuleGroup_RequestSyntax) **   <a name="networkfirewall-UpdateRuleGroup-request-Description"></a>
A description of the rule group.   
Type: String  
Length Constraints: Maximum length of 512.  
Pattern: `^.*$`   
Required: No

 ** [DryRun](#API_UpdateRuleGroup_RequestSyntax) **   <a name="networkfirewall-UpdateRuleGroup-request-DryRun"></a>
Indicates whether you want Network Firewall to just check the validity of the request, rather than run the request.   
If set to `TRUE`, Network Firewall checks whether the request can run successfully, but doesn't actually make the requested changes. The call returns the value that the request would return if you ran it with dry run set to `FALSE`, but doesn't make additions or changes to your resources. This option allows you to make sure that you have the required permissions to run the request and that your request parameters are valid.   
If set to `FALSE`, Network Firewall makes the requested changes to your resources.   
Type: Boolean  
Required: No

 ** [EncryptionConfiguration](#API_UpdateRuleGroup_RequestSyntax) **   <a name="networkfirewall-UpdateRuleGroup-request-EncryptionConfiguration"></a>
A complex type that contains settings for encryption of your rule group resources.  
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object  
Required: No

 ** [RuleGroup](#API_UpdateRuleGroup_RequestSyntax) **   <a name="networkfirewall-UpdateRuleGroup-request-RuleGroup"></a>
An object that defines the rule group rules.   
You must provide either this rule group setting or a `Rules` setting, but not both. 
Type: [RuleGroup](API_RuleGroup.md) object  
Required: No

 ** [RuleGroupArn](#API_UpdateRuleGroup_RequestSyntax) **   <a name="networkfirewall-UpdateRuleGroup-request-RuleGroupArn"></a>
The Amazon Resource Name (ARN) of the rule group.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [RuleGroupName](#API_UpdateRuleGroup_RequestSyntax) **   <a name="networkfirewall-UpdateRuleGroup-request-RuleGroupName"></a>
The descriptive name of the rule group. You can't change the name of a rule group after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [Rules](#API_UpdateRuleGroup_RequestSyntax) **   <a name="networkfirewall-UpdateRuleGroup-request-Rules"></a>
A string containing stateful rule group rules specifications in Suricata flat format, with one rule per line. Use this to import your existing Suricata compatible rule groups.   
You must provide either this rules setting or a populated `RuleGroup` setting, but not both. 
You can provide your rule group specification in Suricata flat format through this setting when you create or update your rule group. The call response returns a [RuleGroup](API_RuleGroup.md) object that Network Firewall has populated from your string.   
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 2000000.  
Required: No

 ** [SourceMetadata](#API_UpdateRuleGroup_RequestSyntax) **   <a name="networkfirewall-UpdateRuleGroup-request-SourceMetadata"></a>
A complex type that contains metadata about the rule group that your own rule group is copied from. You can use the metadata to keep track of updates made to the originating rule group.  
Type: [SourceMetadata](API_SourceMetadata.md) object  
Required: No

 ** [SummaryConfiguration](#API_UpdateRuleGroup_RequestSyntax) **   <a name="networkfirewall-UpdateRuleGroup-request-SummaryConfiguration"></a>
Updates the selected summary configuration for a rule group.  
Changes affect subsequent responses from [DescribeRuleGroupSummary](API_DescribeRuleGroupSummary.md).  
Type: [SummaryConfiguration](API_SummaryConfiguration.md) object  
Required: No

 ** [Type](#API_UpdateRuleGroup_RequestSyntax) **   <a name="networkfirewall-UpdateRuleGroup-request-Type"></a>
Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules.   
This setting is required for requests that do not include the `RuleGroupARN`.
Type: String  
Valid Values: `STATELESS | STATEFUL | STATEFUL_DOMAIN`   
Required: No

 ** [UpdateToken](#API_UpdateRuleGroup_RequestSyntax) **   <a name="networkfirewall-UpdateRuleGroup-request-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the rule group. The token marks the state of the rule group resource at the time of the request.   
To make changes to the rule group, you provide the token in your request. Network Firewall uses the token to ensure that the rule group hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the rule group again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`   
Required: Yes

## Response Syntax
<a name="API_UpdateRuleGroup_ResponseSyntax"></a>

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
   },
   "UpdateToken": "string"
}
```

## Response Elements
<a name="API_UpdateRuleGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RuleGroupResponse](#API_UpdateRuleGroup_ResponseSyntax) **   <a name="networkfirewall-UpdateRuleGroup-response-RuleGroupResponse"></a>
The high-level properties of a rule group. This, along with the [RuleGroup](API_RuleGroup.md), define the rule group. You can retrieve all objects for a rule group by calling [DescribeRuleGroup](API_DescribeRuleGroup.md).   
Type: [RuleGroupResponse](API_RuleGroupResponse.md) object

 ** [UpdateToken](#API_UpdateRuleGroup_ResponseSyntax) **   <a name="networkfirewall-UpdateRuleGroup-response-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the rule group. The token marks the state of the rule group resource at the time of the request.   
To make changes to the rule group, you provide the token in your request. Network Firewall uses the token to ensure that the rule group hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the rule group again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$` 

## Errors
<a name="API_UpdateRuleGroup_Errors"></a>

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

 ** InvalidTokenException **   
The token you provided is stale or isn't valid for the operation.   
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Unable to locate a resource using the parameters that you provided.  
HTTP Status Code: 400

 ** ThrottlingException **   
Unable to process the request due to throttling limitations.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateRuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/UpdateRuleGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/UpdateRuleGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/UpdateRuleGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/UpdateRuleGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/UpdateRuleGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/UpdateRuleGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/UpdateRuleGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/UpdateRuleGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/UpdateRuleGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/UpdateRuleGroup) 