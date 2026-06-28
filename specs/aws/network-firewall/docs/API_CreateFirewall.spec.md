---
id: "@specs/aws/network-firewall/docs/API_CreateFirewall"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateFirewall"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# CreateFirewall

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_CreateFirewall
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateFirewall
<a name="API_CreateFirewall"></a>

Creates an AWS Network Firewall [Firewall](API_Firewall.md) and accompanying [FirewallStatus](API_FirewallStatus.md) for a VPC. 

The firewall defines the configuration settings for an AWS Network Firewall firewall. The settings that you can define at creation include the firewall policy, the subnets in your VPC to use for the firewall endpoints, and any tags that are attached to the firewall AWS resource. 

After you create a firewall, you can provide additional settings, like the logging configuration. 

To update the settings for a firewall, you use the operations that apply to the settings themselves, for example [UpdateLoggingConfiguration](API_UpdateLoggingConfiguration.md), [AssociateSubnets](API_AssociateSubnets.md), and [UpdateFirewallDeleteProtection](API_UpdateFirewallDeleteProtection.md). 

To manage a firewall's tags, use the standard AWS resource tagging operations, [ListTagsForResource](API_ListTagsForResource.md), [TagResource](API_TagResource.md), and [UntagResource](API_UntagResource.md).

To retrieve information about firewalls, use [ListFirewalls](API_ListFirewalls.md) and [DescribeFirewall](API_DescribeFirewall.md).

To generate a report on the last 30 days of traffic monitored by a firewall, use [StartAnalysisReport](API_StartAnalysisReport.md).

## Request Syntax
<a name="API_CreateFirewall_RequestSyntax"></a>

```
{
   "AvailabilityZoneChangeProtection": {{boolean}},
   "AvailabilityZoneMappings": [ 
      { 
         "AvailabilityZone": "{{string}}"
      }
   ],
   "DeleteProtection": {{boolean}},
   "Description": "{{string}}",
   "EnabledAnalysisTypes": [ "{{string}}" ],
   "EncryptionConfiguration": { 
      "KeyId": "{{string}}",
      "Type": "{{string}}"
   },
   "FirewallName": "{{string}}",
   "FirewallPolicyArn": "{{string}}",
   "FirewallPolicyChangeProtection": {{boolean}},
   "SubnetChangeProtection": {{boolean}},
   "SubnetMappings": [ 
      { 
         "IPAddressType": "{{string}}",
         "SubnetId": "{{string}}"
      }
   ],
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TransitGatewayId": "{{string}}",
   "VpcId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateFirewall_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AvailabilityZoneChangeProtection](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-AvailabilityZoneChangeProtection"></a>
Optional. A setting indicating whether the firewall is protected against changes to its Availability Zone configuration. When set to `TRUE`, you cannot add or remove Availability Zones without first disabling this protection using [UpdateAvailabilityZoneChangeProtection](API_UpdateAvailabilityZoneChangeProtection.md).  
Default value: `FALSE`   
Type: Boolean  
Required: No

 ** [AvailabilityZoneMappings](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-AvailabilityZoneMappings"></a>
Required. The Availability Zones where you want to create firewall endpoints for a transit gateway-attached firewall. You must specify at least one Availability Zone. Consider enabling the firewall in every Availability Zone where you have workloads to maintain Availability Zone isolation.  
You can modify Availability Zones later using [AssociateAvailabilityZones](API_AssociateAvailabilityZones.md) or [DisassociateAvailabilityZones](API_DisassociateAvailabilityZones.md), but this may briefly disrupt traffic. The `AvailabilityZoneChangeProtection` setting controls whether you can make these modifications.  
Type: Array of [AvailabilityZoneMapping](API_AvailabilityZoneMapping.md) objects  
Required: No

 ** [DeleteProtection](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-DeleteProtection"></a>
A flag indicating whether it is possible to delete the firewall. A setting of `TRUE` indicates that the firewall is protected against deletion. Use this setting to protect against accidentally deleting a firewall that is in use. When you create a firewall, the operation initializes this flag to `TRUE`.  
Type: Boolean  
Required: No

 ** [Description](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-Description"></a>
A description of the firewall.  
Type: String  
Length Constraints: Maximum length of 512.  
Pattern: `^.*$`   
Required: No

 ** [EnabledAnalysisTypes](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-EnabledAnalysisTypes"></a>
An optional setting indicating the specific traffic analysis types to enable on the firewall.   
Type: Array of strings  
Valid Values: `TLS_SNI | HTTP_HOST`   
Required: No

 ** [EncryptionConfiguration](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-EncryptionConfiguration"></a>
A complex type that contains settings for encryption of your firewall resources.  
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object  
Required: No

 ** [FirewallName](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-FirewallName"></a>
The descriptive name of the firewall. You can't change the name of a firewall after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: Yes

 ** [FirewallPolicyArn](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-FirewallPolicyArn"></a>
The Amazon Resource Name (ARN) of the [FirewallPolicy](API_FirewallPolicy.md) that you want to use for the firewall.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: Yes

 ** [FirewallPolicyChangeProtection](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-FirewallPolicyChangeProtection"></a>
A setting indicating whether the firewall is protected against a change to the firewall policy association. Use this setting to protect against accidentally modifying the firewall policy for a firewall that is in use. When you create a firewall, the operation initializes this setting to `TRUE`.  
Type: Boolean  
Required: No

 ** [SubnetChangeProtection](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-SubnetChangeProtection"></a>
A setting indicating whether the firewall is protected against changes to the subnet associations. Use this setting to protect against accidentally modifying the subnet associations for a firewall that is in use. When you create a firewall, the operation initializes this setting to `TRUE`.  
Type: Boolean  
Required: No

 ** [SubnetMappings](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-SubnetMappings"></a>
The public subnets to use for your Network Firewall firewalls. Each subnet must belong to a different Availability Zone in the VPC. Network Firewall creates a firewall endpoint in each subnet.   
Type: Array of [SubnetMapping](API_SubnetMapping.md) objects  
Required: No

 ** [Tags](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-Tags"></a>
The key:value pairs to associate with the resource.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** [TransitGatewayId](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-TransitGatewayId"></a>
Required when creating a transit gateway-attached firewall. The unique identifier of the transit gateway to attach to this firewall. You can provide either a transit gateway from your account or one that has been shared with you through AWS Resource Access Manager.  
After creating the firewall, you cannot change the transit gateway association. To use a different transit gateway, you must create a new firewall.
For information about creating firewalls, see [CreateFirewall](#API_CreateFirewall). For specific guidance about transit gateway-attached firewalls, see [Considerations for transit gateway-attached firewalls](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tgw-firewall-considerations.html) in the * AWS Network Firewall Developer Guide*.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^tgw-[0-9a-z]+$`   
Required: No

 ** [VpcId](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-VpcId"></a>
The unique identifier of the VPC where Network Firewall should create the firewall.   
You can't change this setting after you create the firewall.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^vpc-[0-9a-f]+$`   
Required: No

## Response Syntax
<a name="API_CreateFirewall_ResponseSyntax"></a>

```
{
   "Firewall": { 
      "AvailabilityZoneChangeProtection": boolean,
      "AvailabilityZoneMappings": [ 
         { 
            "AvailabilityZone": "string"
         }
      ],
      "DeleteProtection": boolean,
      "Description": "string",
      "EnabledAnalysisTypes": [ "string" ],
      "EncryptionConfiguration": { 
         "KeyId": "string",
         "Type": "string"
      },
      "FirewallArn": "string",
      "FirewallId": "string",
      "FirewallName": "string",
      "FirewallPolicyArn": "string",
      "FirewallPolicyChangeProtection": boolean,
      "NumberOfAssociations": number,
      "SubnetChangeProtection": boolean,
      "SubnetMappings": [ 
         { 
            "IPAddressType": "string",
            "SubnetId": "string"
         }
      ],
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ],
      "TransitGatewayId": "string",
      "TransitGatewayOwnerAccountId": "string",
      "VpcId": "string"
   },
   "FirewallStatus": { 
      "CapacityUsageSummary": { 
         "CIDRs": { 
            "AvailableCIDRCount": number,
            "IPSetReferences": { 
               "string" : { 
                  "ResolvedCIDRCount": number
               }
            },
            "UtilizedCIDRCount": number
         }
      },
      "ConfigurationSyncStateSummary": "string",
      "Status": "string",
      "SyncStates": { 
         "string" : { 
            "Attachment": { 
               "EndpointId": "string",
               "Status": "string",
               "StatusMessage": "string",
               "SubnetId": "string"
            },
            "Config": { 
               "string" : { 
                  "SyncStatus": "string",
                  "UpdateToken": "string"
               }
            }
         }
      },
      "TransitGatewayAttachmentSyncState": { 
         "AttachmentId": "string",
         "StatusMessage": "string",
         "TransitGatewayAttachmentStatus": "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateFirewall_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Firewall](#API_CreateFirewall_ResponseSyntax) **   <a name="networkfirewall-CreateFirewall-response-Firewall"></a>
The configuration settings for the firewall. These settings include the firewall policy and the subnets in your VPC to use for the firewall endpoints.   
Type: [Firewall](API_Firewall.md) object

 ** [FirewallStatus](#API_CreateFirewall_ResponseSyntax) **   <a name="networkfirewall-CreateFirewall-response-FirewallStatus"></a>
Detailed information about the current status of a [Firewall](API_Firewall.md). You can retrieve this for a firewall by calling [DescribeFirewall](API_DescribeFirewall.md) and providing the firewall name and ARN.  
The firewall status indicates a combined status. It indicates whether all subnets are up-to-date with the latest firewall configurations, which is based on the sync states config values, and also whether all subnets have their endpoints fully enabled, based on their sync states attachment values.   
Type: [FirewallStatus](API_FirewallStatus.md) object

## Errors
<a name="API_CreateFirewall_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientCapacityException **   
 AWS doesn't currently have enough available capacity to fulfill your request. Try your request later.   
HTTP Status Code: 500

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

 ** LimitExceededException **   
Unable to perform the operation because doing so would violate a limit setting.   
HTTP Status Code: 400

 ** ThrottlingException **   
Unable to process the request due to throttling limitations.  
HTTP Status Code: 400

## See Also
<a name="API_CreateFirewall_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/CreateFirewall) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/CreateFirewall) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/CreateFirewall) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/CreateFirewall) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/CreateFirewall) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/CreateFirewall) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/CreateFirewall) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/CreateFirewall) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/CreateFirewall) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/CreateFirewall) 