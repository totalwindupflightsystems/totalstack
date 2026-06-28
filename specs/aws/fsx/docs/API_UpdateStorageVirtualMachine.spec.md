---
id: "@specs/aws/fsx/docs/API_UpdateStorageVirtualMachine"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UpdateStorageVirtualMachine"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# UpdateStorageVirtualMachine

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_UpdateStorageVirtualMachine
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UpdateStorageVirtualMachine
<a name="API_UpdateStorageVirtualMachine"></a>

Updates an FSx for ONTAP storage virtual machine (SVM).

## Request Syntax
<a name="API_UpdateStorageVirtualMachine_RequestSyntax"></a>

```
{
   "ActiveDirectoryConfiguration": { 
      "NetBiosName": "{{string}}",
      "SelfManagedActiveDirectoryConfiguration": { 
         "DnsIps": [ "{{string}}" ],
         "DomainJoinServiceAccountSecret": "{{string}}",
         "DomainName": "{{string}}",
         "FileSystemAdministratorsGroup": "{{string}}",
         "OrganizationalUnitDistinguishedName": "{{string}}",
         "Password": "{{string}}",
         "UserName": "{{string}}"
      }
   },
   "ClientRequestToken": "{{string}}",
   "StorageVirtualMachineId": "{{string}}",
   "SvmAdminPassword": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateStorageVirtualMachine_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ActiveDirectoryConfiguration](#API_UpdateStorageVirtualMachine_RequestSyntax) **   <a name="FSx-UpdateStorageVirtualMachine-request-ActiveDirectoryConfiguration"></a>
Specifies updates to an SVM's Microsoft Active Directory (AD) configuration.  
Type: [UpdateSvmActiveDirectoryConfiguration](API_UpdateSvmActiveDirectoryConfiguration.md) object  
Required: No

 ** [ClientRequestToken](#API_UpdateStorageVirtualMachine_RequestSyntax) **   <a name="FSx-UpdateStorageVirtualMachine-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [StorageVirtualMachineId](#API_UpdateStorageVirtualMachine_RequestSyntax) **   <a name="FSx-UpdateStorageVirtualMachine-request-StorageVirtualMachineId"></a>
The ID of the SVM that you want to update, in the format `svm-0123456789abcdef0`.  
Type: String  
Length Constraints: Fixed length of 21.  
Pattern: `^(svm-[0-9a-f]{17,})$`   
Required: Yes

 ** [SvmAdminPassword](#API_UpdateStorageVirtualMachine_RequestSyntax) **   <a name="FSx-UpdateStorageVirtualMachine-request-SvmAdminPassword"></a>
Specifies a new SvmAdminPassword.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 50.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{8,50}$`   
Required: No

## Response Syntax
<a name="API_UpdateStorageVirtualMachine_ResponseSyntax"></a>

```
{
   "StorageVirtualMachine": { 
      "ActiveDirectoryConfiguration": { 
         "NetBiosName": "string",
         "SelfManagedActiveDirectoryConfiguration": { 
            "DnsIps": [ "string" ],
            "DomainJoinServiceAccountSecret": "string",
            "DomainName": "string",
            "FileSystemAdministratorsGroup": "string",
            "OrganizationalUnitDistinguishedName": "string",
            "UserName": "string"
         }
      },
      "CreationTime": number,
      "Endpoints": { 
         "Iscsi": { 
            "DNSName": "string",
            "IpAddresses": [ "string" ],
            "Ipv6Addresses": [ "string" ]
         },
         "Management": { 
            "DNSName": "string",
            "IpAddresses": [ "string" ],
            "Ipv6Addresses": [ "string" ]
         },
         "Nfs": { 
            "DNSName": "string",
            "IpAddresses": [ "string" ],
            "Ipv6Addresses": [ "string" ]
         },
         "Smb": { 
            "DNSName": "string",
            "IpAddresses": [ "string" ],
            "Ipv6Addresses": [ "string" ]
         }
      },
      "FileSystemId": "string",
      "Lifecycle": "string",
      "LifecycleTransitionReason": { 
         "Message": "string"
      },
      "Name": "string",
      "ResourceARN": "string",
      "RootVolumeSecurityStyle": "string",
      "StorageVirtualMachineId": "string",
      "Subtype": "string",
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ],
      "UUID": "string"
   }
}
```

## Response Elements
<a name="API_UpdateStorageVirtualMachine_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StorageVirtualMachine](#API_UpdateStorageVirtualMachine_ResponseSyntax) **   <a name="FSx-UpdateStorageVirtualMachine-response-StorageVirtualMachine"></a>
Describes the Amazon FSx for NetApp ONTAP storage virtual machine (SVM) configuration.  
Type: [StorageVirtualMachine](API_StorageVirtualMachine.md) object

## Errors
<a name="API_UpdateStorageVirtualMachine_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** IncompatibleParameterError **   
The error returned when a second request is received with the same client request token but different parameters settings. A client request token should always uniquely identify a single request.    
 ** Message **   
A detailed error message.  
 ** Parameter **   
A parameter that is incompatible with the earlier request.
HTTP Status Code: 400

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

 ** StorageVirtualMachineNotFound **   
No FSx for ONTAP SVMs were found based upon the supplied parameters.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation is not supported for this resource or API.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## Examples
<a name="API_UpdateStorageVirtualMachine_Examples"></a>

### Update an FSx for ONTAP SVM
<a name="API_UpdateStorageVirtualMachine_Example_1"></a>

This example updates the Microsoft Active Directory user credentials of an existing SVM that is joined to a AD.

```
{
   "ActiveDirectoryConfiguration": { 
      "SelfManagedActiveDirectoryConfiguration": { 
         
         "UserName": "admin_user"
         "Password": "new_password",
      }
   },
   "StorageVirtualMachineId": "svm-0123456789abcdef3"
}
```

## See Also
<a name="API_UpdateStorageVirtualMachine_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/UpdateStorageVirtualMachine) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/UpdateStorageVirtualMachine) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/UpdateStorageVirtualMachine) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/UpdateStorageVirtualMachine) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/UpdateStorageVirtualMachine) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/UpdateStorageVirtualMachine) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/UpdateStorageVirtualMachine) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/UpdateStorageVirtualMachine) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/UpdateStorageVirtualMachine) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/UpdateStorageVirtualMachine) 