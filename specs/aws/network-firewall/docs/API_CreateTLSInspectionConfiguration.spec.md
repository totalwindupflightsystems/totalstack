---
id: "@specs/aws/network-firewall/docs/API_CreateTLSInspectionConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateTLSInspectionConfiguration"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# CreateTLSInspectionConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_CreateTLSInspectionConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateTLSInspectionConfiguration
<a name="API_CreateTLSInspectionConfiguration"></a>

Creates an AWS Network Firewall TLS inspection configuration. Network Firewall uses TLS inspection configurations to decrypt your firewall's inbound and outbound SSL/TLS traffic. After decryption, Network Firewall inspects the traffic according to your firewall policy's stateful rules, and then re-encrypts it before sending it to its destination. You can enable inspection of your firewall's inbound traffic, outbound traffic, or both. To use TLS inspection with your firewall, you must first import or provision certificates using ACM, create a TLS inspection configuration, add that configuration to a new firewall policy, and then associate that policy with your firewall.

To update the settings for a TLS inspection configuration, use [UpdateTLSInspectionConfiguration](API_UpdateTLSInspectionConfiguration.md).

To manage a TLS inspection configuration's tags, use the standard AWS resource tagging operations, [ListTagsForResource](API_ListTagsForResource.md), [TagResource](API_TagResource.md), and [UntagResource](API_UntagResource.md).

To retrieve information about TLS inspection configurations, use [ListTLSInspectionConfigurations](API_ListTLSInspectionConfigurations.md) and [DescribeTLSInspectionConfiguration](API_DescribeTLSInspectionConfiguration.md).

 For more information about TLS inspection configurations, see [Inspecting SSL/TLS traffic with TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html) in the * AWS Network Firewall Developer Guide*. 

## Request Syntax
<a name="API_CreateTLSInspectionConfiguration_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "EncryptionConfiguration": { 
      "KeyId": "{{string}}",
      "Type": "{{string}}"
   },
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TLSInspectionConfiguration": { 
      "ServerCertificateConfigurations": [ 
         { 
            "CertificateAuthorityArn": "{{string}}",
            "CheckCertificateRevocationStatus": { 
               "RevokedStatusAction": "{{string}}",
               "UnknownStatusAction": "{{string}}"
            },
            "Scopes": [ 
               { 
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
                  ]
               }
            ],
            "ServerCertificates": [ 
               { 
                  "ResourceArn": "{{string}}"
               }
            ]
         }
      ]
   },
   "TLSInspectionConfigurationName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateTLSInspectionConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_CreateTLSInspectionConfiguration_RequestSyntax) **   <a name="networkfirewall-CreateTLSInspectionConfiguration-request-Description"></a>
A description of the TLS inspection configuration.   
Type: String  
Length Constraints: Maximum length of 512.  
Pattern: `^.*$`   
Required: No

 ** [EncryptionConfiguration](#API_CreateTLSInspectionConfiguration_RequestSyntax) **   <a name="networkfirewall-CreateTLSInspectionConfiguration-request-EncryptionConfiguration"></a>
A complex type that contains optional AWS Key Management Service (KMS) encryption settings for your Network Firewall resources. Your data is encrypted by default with an AWS owned key that AWS owns and manages for you. You can use either the AWS owned key, or provide your own customer managed key. To learn more about KMS encryption of your Network Firewall resources, see [Encryption at rest with AWS Key Managment Service](https://docs.aws.amazon.com/kms/latest/developerguide/kms-encryption-at-rest.html) in the *Network Firewall Developer Guide*.  
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object  
Required: No

 ** [Tags](#API_CreateTLSInspectionConfiguration_RequestSyntax) **   <a name="networkfirewall-CreateTLSInspectionConfiguration-request-Tags"></a>
The key:value pairs to associate with the resource.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 200 items.  
Required: No

 ** [TLSInspectionConfiguration](#API_CreateTLSInspectionConfiguration_RequestSyntax) **   <a name="networkfirewall-CreateTLSInspectionConfiguration-request-TLSInspectionConfiguration"></a>
The object that defines a TLS inspection configuration. This, along with [TLSInspectionConfigurationResponse](API_TLSInspectionConfigurationResponse.md), define the TLS inspection configuration. You can retrieve all objects for a TLS inspection configuration by calling [DescribeTLSInspectionConfiguration](API_DescribeTLSInspectionConfiguration.md).   
 AWS Network Firewall uses a TLS inspection configuration to decrypt traffic. Network Firewall re-encrypts the traffic before sending it to its destination.  
To use a TLS inspection configuration, you add it to a new Network Firewall firewall policy, then you apply the firewall policy to a firewall. Network Firewall acts as a proxy service to decrypt and inspect the traffic traveling through your firewalls. You can reference a TLS inspection configuration from more than one firewall policy, and you can use a firewall policy in more than one firewall. For more information about using TLS inspection configurations, see [Inspecting SSL/TLS traffic with TLS inspection configurations](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection.html) in the * AWS Network Firewall Developer Guide*.  
Type: [TLSInspectionConfiguration](API_TLSInspectionConfiguration.md) object  
Required: Yes

 ** [TLSInspectionConfigurationName](#API_CreateTLSInspectionConfiguration_RequestSyntax) **   <a name="networkfirewall-CreateTLSInspectionConfiguration-request-TLSInspectionConfigurationName"></a>
The descriptive name of the TLS inspection configuration. You can't change the name of a TLS inspection configuration after you create it.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: Yes

## Response Syntax
<a name="API_CreateTLSInspectionConfiguration_ResponseSyntax"></a>

```
{
   "TLSInspectionConfigurationResponse": { 
      "CertificateAuthority": { 
         "CertificateArn": "string",
         "CertificateSerial": "string",
         "Status": "string",
         "StatusMessage": "string"
      },
      "Certificates": [ 
         { 
            "CertificateArn": "string",
            "CertificateSerial": "string",
            "Status": "string",
            "StatusMessage": "string"
         }
      ],
      "Description": "string",
      "EncryptionConfiguration": { 
         "KeyId": "string",
         "Type": "string"
      },
      "LastModifiedTime": number,
      "NumberOfAssociations": number,
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ],
      "TLSInspectionConfigurationArn": "string",
      "TLSInspectionConfigurationId": "string",
      "TLSInspectionConfigurationName": "string",
      "TLSInspectionConfigurationStatus": "string"
   },
   "UpdateToken": "string"
}
```

## Response Elements
<a name="API_CreateTLSInspectionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TLSInspectionConfigurationResponse](#API_CreateTLSInspectionConfiguration_ResponseSyntax) **   <a name="networkfirewall-CreateTLSInspectionConfiguration-response-TLSInspectionConfigurationResponse"></a>
The high-level properties of a TLS inspection configuration. This, along with the [TLSInspectionConfiguration](API_TLSInspectionConfiguration.md), define the TLS inspection configuration. You can retrieve all objects for a TLS inspection configuration by calling [DescribeTLSInspectionConfiguration](API_DescribeTLSInspectionConfiguration.md).   
Type: [TLSInspectionConfigurationResponse](API_TLSInspectionConfigurationResponse.md) object

 ** [UpdateToken](#API_CreateTLSInspectionConfiguration_ResponseSyntax) **   <a name="networkfirewall-CreateTLSInspectionConfiguration-response-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the TLS inspection configuration. The token marks the state of the TLS inspection configuration resource at the time of the request.   
To make changes to the TLS inspection configuration, you provide the token in your request. Network Firewall uses the token to ensure that the TLS inspection configuration hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the TLS inspection configuration again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$` 

## Errors
<a name="API_CreateTLSInspectionConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientCapacityException **   
 AWS doesn't currently have enough available capacity to fulfill your request. Try your request later.   
HTTP Status Code: 500

 ** InternalServerError **   
Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request.   
HTTP Status Code: 500

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
<a name="API_CreateTLSInspectionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/CreateTLSInspectionConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/CreateTLSInspectionConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/CreateTLSInspectionConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/CreateTLSInspectionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/CreateTLSInspectionConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/CreateTLSInspectionConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/CreateTLSInspectionConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/CreateTLSInspectionConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/CreateTLSInspectionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/CreateTLSInspectionConfiguration) 