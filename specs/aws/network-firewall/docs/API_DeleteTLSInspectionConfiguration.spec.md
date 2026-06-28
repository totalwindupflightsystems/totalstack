---
id: "@specs/aws/network-firewall/docs/API_DeleteTLSInspectionConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteTLSInspectionConfiguration"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# DeleteTLSInspectionConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_DeleteTLSInspectionConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteTLSInspectionConfiguration
<a name="API_DeleteTLSInspectionConfiguration"></a>

Deletes the specified [TLSInspectionConfiguration](API_TLSInspectionConfiguration.md).

## Request Syntax
<a name="API_DeleteTLSInspectionConfiguration_RequestSyntax"></a>

```
{
   "TLSInspectionConfigurationArn": "{{string}}",
   "TLSInspectionConfigurationName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteTLSInspectionConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TLSInspectionConfigurationArn](#API_DeleteTLSInspectionConfiguration_RequestSyntax) **   <a name="networkfirewall-DeleteTLSInspectionConfiguration-request-TLSInspectionConfigurationArn"></a>
The Amazon Resource Name (ARN) of the TLS inspection configuration.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `^arn:aws.*`   
Required: No

 ** [TLSInspectionConfigurationName](#API_DeleteTLSInspectionConfiguration_RequestSyntax) **   <a name="networkfirewall-DeleteTLSInspectionConfiguration-request-TLSInspectionConfigurationName"></a>
The descriptive name of the TLS inspection configuration. You can't change the name of a TLS inspection configuration after you create it.  
You must specify the ARN or the name, and you can specify both.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^[a-zA-Z0-9-]+$`   
Required: No

## Response Syntax
<a name="API_DeleteTLSInspectionConfiguration_ResponseSyntax"></a>

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
   }
}
```

## Response Elements
<a name="API_DeleteTLSInspectionConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TLSInspectionConfigurationResponse](#API_DeleteTLSInspectionConfiguration_ResponseSyntax) **   <a name="networkfirewall-DeleteTLSInspectionConfiguration-response-TLSInspectionConfigurationResponse"></a>
The high-level properties of a TLS inspection configuration. This, along with the [TLSInspectionConfiguration](API_TLSInspectionConfiguration.md), define the TLS inspection configuration. You can retrieve all objects for a TLS inspection configuration by calling [DescribeTLSInspectionConfiguration](API_DescribeTLSInspectionConfiguration.md).   
Type: [TLSInspectionConfigurationResponse](API_TLSInspectionConfigurationResponse.md) object

## Errors
<a name="API_DeleteTLSInspectionConfiguration_Errors"></a>

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

## See Also
<a name="API_DeleteTLSInspectionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DeleteTLSInspectionConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DeleteTLSInspectionConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DeleteTLSInspectionConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DeleteTLSInspectionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DeleteTLSInspectionConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DeleteTLSInspectionConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DeleteTLSInspectionConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DeleteTLSInspectionConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DeleteTLSInspectionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DeleteTLSInspectionConfiguration) 