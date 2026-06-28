---
id: "@specs/aws/network-firewall/docs/API_DeleteFirewall"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteFirewall"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# DeleteFirewall

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_DeleteFirewall
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteFirewall
<a name="API_DeleteFirewall"></a>

Deletes the specified [Firewall](API_Firewall.md) and its [FirewallStatus](API_FirewallStatus.md). This operation requires the firewall's `DeleteProtection` flag to be `FALSE`. You can't revert this operation. 

You can check whether a firewall is in use by reviewing the route tables for the Availability Zones where you have firewall subnet mappings. Retrieve the subnet mappings by calling [DescribeFirewall](API_DescribeFirewall.md). You define and update the route tables through Amazon VPC. As needed, update the route tables for the zones to remove the firewall endpoints. When the route tables no longer use the firewall endpoints, you can remove the firewall safely.

To delete a firewall, remove the delete protection if you need to using [UpdateFirewallDeleteProtection](API_UpdateFirewallDeleteProtection.md), then delete the firewall by calling [DeleteFirewall](#API_DeleteFirewall). 

## Request Syntax
<a name="API_DeleteFirewall_RequestSyntax"></a>

```
{
   "FirewallArn": "{{string}}",
   "FirewallName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteFirewall_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FirewallArn](#API_DeleteFirewall_RequestSyntax) **   <a name="networkfirewall-DeleteFirewall-request-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [FirewallName](#API_DeleteFirewall_RequestSyntax) **   <a name="networkfirewall-DeleteFirewall-request-FirewallName"></a>
The descriptive name of the firewall. You can't change the name of a firewall after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

## Response Syntax
<a name="API_DeleteFirewall_ResponseSyntax"></a>

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
<a name="API_DeleteFirewall_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Firewall](#API_DeleteFirewall_ResponseSyntax) **   <a name="networkfirewall-DeleteFirewall-response-Firewall"></a>
A firewall defines the behavior of a firewall, the main VPC where the firewall is used, the Availability Zones where the firewall can be used, and one subnet to use for a firewall endpoint within each of the Availability Zones. The Availability Zones are defined implicitly in the subnet specifications.  
In addition to the firewall endpoints that you define in this `Firewall` specification, you can create firewall endpoints in `VpcEndpointAssociation` resources for any VPC, in any Availability Zone where the firewall is already in use.   
The status of the firewall, for example whether it's ready to filter network traffic, is provided in the corresponding [FirewallStatus](API_FirewallStatus.md). You can retrieve both the firewall and firewall status by calling [DescribeFirewall](API_DescribeFirewall.md).  
Type: [Firewall](API_Firewall.md) object

 ** [FirewallStatus](#API_DeleteFirewall_ResponseSyntax) **   <a name="networkfirewall-DeleteFirewall-response-FirewallStatus"></a>
Detailed information about the current status of a [Firewall](API_Firewall.md). You can retrieve this for a firewall by calling [DescribeFirewall](API_DescribeFirewall.md) and providing the firewall name and ARN.  
The firewall status indicates a combined status. It indicates whether all subnets are up-to-date with the latest firewall configurations, which is based on the sync states config values, and also whether all subnets have their endpoints fully enabled, based on their sync states attachment values.   
Type: [FirewallStatus](API_FirewallStatus.md) object

## Errors
<a name="API_DeleteFirewall_Errors"></a>

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
<a name="API_DeleteFirewall_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DeleteFirewall) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DeleteFirewall) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DeleteFirewall) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DeleteFirewall) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DeleteFirewall) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DeleteFirewall) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DeleteFirewall) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DeleteFirewall) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DeleteFirewall) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DeleteFirewall) 