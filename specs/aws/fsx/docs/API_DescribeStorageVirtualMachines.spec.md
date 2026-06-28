---
id: "@specs/aws/fsx/docs/API_DescribeStorageVirtualMachines"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeStorageVirtualMachines"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DescribeStorageVirtualMachines

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DescribeStorageVirtualMachines
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeStorageVirtualMachines
<a name="API_DescribeStorageVirtualMachines"></a>

Describes one or more Amazon FSx for NetApp ONTAP storage virtual machines (SVMs).

## Request Syntax
<a name="API_DescribeStorageVirtualMachines_RequestSyntax"></a>

```
{
   "Filters": [ 
      { 
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "StorageVirtualMachineIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeStorageVirtualMachines_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_DescribeStorageVirtualMachines_RequestSyntax) **   <a name="FSx-DescribeStorageVirtualMachines-request-Filters"></a>
Enter a filter name:value pair to view a select set of SVMs.  
Type: Array of [StorageVirtualMachineFilter](API_StorageVirtualMachineFilter.md) objects  
Array Members: Maximum number of 1 item.  
Required: No

 ** [MaxResults](#API_DescribeStorageVirtualMachines_RequestSyntax) **   <a name="FSx-DescribeStorageVirtualMachines-request-MaxResults"></a>
The maximum number of resources to return in the response. This value must be an integer greater than zero.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 2147483647.  
Required: No

 ** [NextToken](#API_DescribeStorageVirtualMachines_RequestSyntax) **   <a name="FSx-DescribeStorageVirtualMachines-request-NextToken"></a>
(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$`   
Required: No

 ** [StorageVirtualMachineIds](#API_DescribeStorageVirtualMachines_RequestSyntax) **   <a name="FSx-DescribeStorageVirtualMachines-request-StorageVirtualMachineIds"></a>
Enter the ID of one or more SVMs that you want to view.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Fixed length of 21.  
Pattern: `^(svm-[0-9a-f]{17,})$`   
Required: No

## Response Syntax
<a name="API_DescribeStorageVirtualMachines_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "StorageVirtualMachines": [ 
      { 
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
   ]
}
```

## Response Elements
<a name="API_DescribeStorageVirtualMachines_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeStorageVirtualMachines_ResponseSyntax) **   <a name="FSx-DescribeStorageVirtualMachines-response-NextToken"></a>
(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$` 

 ** [StorageVirtualMachines](#API_DescribeStorageVirtualMachines_ResponseSyntax) **   <a name="FSx-DescribeStorageVirtualMachines-response-StorageVirtualMachines"></a>
Returned after a successful `DescribeStorageVirtualMachines` operation, describing each SVM.  
Type: Array of [StorageVirtualMachine](API_StorageVirtualMachine.md) objects  
Array Members: Maximum number of 50 items.

## Errors
<a name="API_DescribeStorageVirtualMachines_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
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

## Examples
<a name="API_DescribeStorageVirtualMachines_Examples"></a>

### View SVMs
<a name="API_DescribeStorageVirtualMachines_Example_1"></a>

The following example will return the SVMs for a specific Amazon FSx for ONTAP file system, showing 5 SVMs per page in the response.

```
{
    "Filters": [
        {
            "Name": "fsx-ontap-fs-id",
            "Values": [ "fs-0123456789abcdef5" ]
        }
    ],
    "MaxResults": 5
}
```

## See Also
<a name="API_DescribeStorageVirtualMachines_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DescribeStorageVirtualMachines) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DescribeStorageVirtualMachines) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DescribeStorageVirtualMachines) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DescribeStorageVirtualMachines) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DescribeStorageVirtualMachines) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DescribeStorageVirtualMachines) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DescribeStorageVirtualMachines) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DescribeStorageVirtualMachines) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DescribeStorageVirtualMachines) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DescribeStorageVirtualMachines) 