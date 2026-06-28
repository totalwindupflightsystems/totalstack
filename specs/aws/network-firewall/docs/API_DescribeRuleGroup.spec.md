---
id: "@specs/aws/network-firewall/docs/API_DescribeRuleGroup"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeRuleGroup"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# DescribeRuleGroup

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_DescribeRuleGroup
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeRuleGroup
<a name="API_DescribeRuleGroup"></a>

Returns the data objects for the specified rule group. 

## Request Syntax
<a name="API_DescribeRuleGroup_RequestSyntax"></a>

```
{
   "AnalyzeRuleGroup": {{boolean}},
   "RuleGroupArn": "{{string}}",
   "RuleGroupName": "{{string}}",
   "Type": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeRuleGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AnalyzeRuleGroup](#API_DescribeRuleGroup_RequestSyntax) **   <a name="networkfirewall-DescribeRuleGroup-request-AnalyzeRuleGroup"></a>
Indicates whether you want Network Firewall to analyze the stateless rules in the rule group for rule behavior such as asymmetric routing. If set to `TRUE`, Network Firewall runs the analysis.  
Type: Boolean  
Required: No

 ** [RuleGroupArn](#API_DescribeRuleGroup_RequestSyntax) **   <a name="networkfirewall-DescribeRuleGroup-request-RuleGroupArn"></a>
The Amazon Resource Name (ARN) of the rule group.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [RuleGroupName](#API_DescribeRuleGroup_RequestSyntax) **   <a name="networkfirewall-DescribeRuleGroup-request-RuleGroupName"></a>
The descriptive name of the rule group. You can't change the name of a rule group after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

 ** [Type](#API_DescribeRuleGroup_RequestSyntax) **   <a name="networkfirewall-DescribeRuleGroup-request-Type"></a>
Indicates whether the rule group is stateless or stateful. If the rule group is stateless, it contains stateless rules. If it is stateful, it contains stateful rules.   
This setting is required for requests that do not include the `RuleGroupARN`.
Type: String  
Valid Values: `STATELESS | STATEFUL | STATEFUL_DOMAIN`   
Required: No

## Response Syntax
<a name="API_DescribeRuleGroup_ResponseSyntax"></a>

```
{
   "RuleGroup": { 
      "ReferenceSets": { 
         "IPSetReferences": { 
            "string" : { 
               "ReferenceArn": "string"
            }
         }
      },
      "RulesSource": { 
         "RulesSourceList": { 
            "GeneratedRulesType": "string",
            "Targets": [ "string" ],
            "TargetTypes": [ "string" ]
         },
         "RulesString": "string",
         "StatefulRules": [ 
            { 
               "Action": "string",
               "Header": { 
                  "Destination": "string",
                  "DestinationPort": "string",
                  "Direction": "string",
                  "Protocol": "string",
                  "Source": "string",
                  "SourcePort": "string"
               },
               "RuleOptions": [ 
                  { 
                     "Keyword": "string",
                     "Settings": [ "string" ]
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
                              "Value": "string"
                           }
                        ]
                     }
                  },
                  "ActionName": "string"
               }
            ],
            "StatelessRules": [ 
               { 
                  "Priority": number,
                  "RuleDefinition": { 
                     "Actions": [ "string" ],
                     "MatchAttributes": { 
                        "DestinationPorts": [ 
                           { 
                              "FromPort": number,
                              "ToPort": number
                           }
                        ],
                        "Destinations": [ 
                           { 
                              "AddressDefinition": "string"
                           }
                        ],
                        "Protocols": [ number ],
                        "SourcePorts": [ 
                           { 
                              "FromPort": number,
                              "ToPort": number
                           }
                        ],
                        "Sources": [ 
                           { 
                              "AddressDefinition": "string"
                           }
                        ],
                        "TCPFlags": [ 
                           { 
                              "Flags": [ "string" ],
                              "Masks": [ "string" ]
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
            "string" : { 
               "Definition": [ "string" ]
            }
         },
         "PortSets": { 
            "string" : { 
               "Definition": [ "string" ]
            }
         }
      },
      "StatefulRuleOptions": { 
         "RuleOrder": "string"
      }
   },
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
<a name="API_DescribeRuleGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RuleGroup](#API_DescribeRuleGroup_ResponseSyntax) **   <a name="networkfirewall-DescribeRuleGroup-response-RuleGroup"></a>
The object that defines the rules in a rule group. This, along with [RuleGroupResponse](API_RuleGroupResponse.md), define the rule group. You can retrieve all objects for a rule group by calling [DescribeRuleGroup](#API_DescribeRuleGroup).   
 AWS Network Firewall uses a rule group to inspect and control network traffic. You define stateless rule groups to inspect individual packets and you define stateful rule groups to inspect packets in the context of their traffic flow.   
To use a rule group, you include it by reference in an Network Firewall firewall policy, then you use the policy in a firewall. You can reference a rule group from more than one firewall policy, and you can use a firewall policy in more than one firewall.   
Type: [RuleGroup](API_RuleGroup.md) object

 ** [RuleGroupResponse](#API_DescribeRuleGroup_ResponseSyntax) **   <a name="networkfirewall-DescribeRuleGroup-response-RuleGroupResponse"></a>
The high-level properties of a rule group. This, along with the [RuleGroup](API_RuleGroup.md), define the rule group. You can retrieve all objects for a rule group by calling [DescribeRuleGroup](#API_DescribeRuleGroup).   
Type: [RuleGroupResponse](API_RuleGroupResponse.md) object

 ** [UpdateToken](#API_DescribeRuleGroup_ResponseSyntax) **   <a name="networkfirewall-DescribeRuleGroup-response-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the rule group. The token marks the state of the rule group resource at the time of the request.   
To make changes to the rule group, you provide the token in your request. Network Firewall uses the token to ensure that the rule group hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the rule group again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$` 

## Errors
<a name="API_DescribeRuleGroup_Errors"></a>

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
<a name="API_DescribeRuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DescribeRuleGroup) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DescribeRuleGroup) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DescribeRuleGroup) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DescribeRuleGroup) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DescribeRuleGroup) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DescribeRuleGroup) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DescribeRuleGroup) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DescribeRuleGroup) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DescribeRuleGroup) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DescribeRuleGroup) 