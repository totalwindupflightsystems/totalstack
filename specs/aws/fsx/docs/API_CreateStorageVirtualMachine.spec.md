---
id: "@specs/aws/fsx/docs/API_CreateStorageVirtualMachine"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS CreateStorageVirtualMachine"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# CreateStorageVirtualMachine

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_CreateStorageVirtualMachine
> **target_lang:** meta — documentation tier. ALL sections preserved.



# CreateStorageVirtualMachine
<a name="API_CreateStorageVirtualMachine"></a>

Creates a storage virtual machine (SVM) for an Amazon FSx for ONTAP file system.

## Request Syntax
<a name="API_CreateStorageVirtualMachine_RequestSyntax"></a>

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
   "FileSystemId": "{{string}}",
   "Name": "{{string}}",
   "RootVolumeSecurityStyle": "{{string}}",
   "SvmAdminPassword": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateStorageVirtualMachine_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ActiveDirectoryConfiguration](#API_CreateStorageVirtualMachine_RequestSyntax) **   <a name="FSx-CreateStorageVirtualMachine-request-ActiveDirectoryConfiguration"></a>
Describes the self-managed Microsoft Active Directory to which you want to join the SVM. Joining an Active Directory provides user authentication and access control for SMB clients, including Microsoft Windows and macOS clients accessing the file system.  
Type: [CreateSvmActiveDirectoryConfiguration](API_CreateSvmActiveDirectoryConfiguration.md) object  
Required: No

 ** [ClientRequestToken](#API_CreateStorageVirtualMachine_RequestSyntax) **   <a name="FSx-CreateStorageVirtualMachine-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [FileSystemId](#API_CreateStorageVirtualMachine_RequestSyntax) **   <a name="FSx-CreateStorageVirtualMachine-request-FileSystemId"></a>
The globally unique ID of the file system, assigned by Amazon FSx.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fs-[0-9a-f]{8,})$`   
Required: Yes

 ** [Name](#API_CreateStorageVirtualMachine_RequestSyntax) **   <a name="FSx-CreateStorageVirtualMachine-request-Name"></a>
The name of the SVM.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 47.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,47}$`   
Required: Yes

 ** [RootVolumeSecurityStyle](#API_CreateStorageVirtualMachine_RequestSyntax) **   <a name="FSx-CreateStorageVirtualMachine-request-RootVolumeSecurityStyle"></a>
The security style of the root volume of the SVM. Specify one of the following values:  
+  `UNIX` if the file system is managed by a UNIX administrator, the majority of users are NFS clients, and an application accessing the data uses a UNIX user as the service account.
+  `NTFS` if the file system is managed by a Microsoft Windows administrator, the majority of users are SMB clients, and an application accessing the data uses a Microsoft Windows user as the service account.
+  `MIXED` This is an advanced setting. For more information, see [Volume security style](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/volume-security-style.html) in the Amazon FSx for NetApp ONTAP User Guide.
  
Type: String  
Valid Values: `UNIX | NTFS | MIXED`   
Required: No

 ** [SvmAdminPassword](#API_CreateStorageVirtualMachine_RequestSyntax) **   <a name="FSx-CreateStorageVirtualMachine-request-SvmAdminPassword"></a>
The password to use when managing the SVM using the NetApp ONTAP CLI or REST API. If you do not specify a password, you can still use the file system's `fsxadmin` user to manage the SVM.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 50.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{8,50}$`   
Required: No

 ** [Tags](#API_CreateStorageVirtualMachine_RequestSyntax) **   <a name="FSx-CreateStorageVirtualMachine-request-Tags"></a>
A list of `Tag` values, with a maximum of 50 elements.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: No

## Response Syntax
<a name="API_CreateStorageVirtualMachine_ResponseSyntax"></a>

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
<a name="API_CreateStorageVirtualMachine_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StorageVirtualMachine](#API_CreateStorageVirtualMachine_ResponseSyntax) **   <a name="FSx-CreateStorageVirtualMachine-response-StorageVirtualMachine"></a>
Returned after a successful `CreateStorageVirtualMachine` operation; describes the SVM just created.  
Type: [StorageVirtualMachine](API_StorageVirtualMachine.md) object

## Errors
<a name="API_CreateStorageVirtualMachine_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ActiveDirectoryError **   
An Active Directory error.    
 ** ActiveDirectoryId **   
The directory ID of the directory that an error pertains to.  
 ** Message **   
A detailed error message.  
 ** Type **   
The type of Active Directory error.
HTTP Status Code: 400

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** FileSystemNotFound **   
No Amazon FSx file systems were found based upon supplied parameters.    
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

 ** ServiceLimitExceeded **   
An error indicating that a particular service limit was exceeded. You can increase some service limits by contacting AWS Support.    
 ** Limit **   
Enumeration of the service limit that was exceeded.   
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** UnsupportedOperation **   
The requested operation is not supported for this resource or API.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

## See Also
<a name="API_CreateStorageVirtualMachine_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/CreateStorageVirtualMachine) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/CreateStorageVirtualMachine) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/CreateStorageVirtualMachine) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/CreateStorageVirtualMachine) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/CreateStorageVirtualMachine) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/CreateStorageVirtualMachine) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/CreateStorageVirtualMachine) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/CreateStorageVirtualMachine) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/CreateStorageVirtualMachine) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/CreateStorageVirtualMachine) 