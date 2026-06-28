---
id: "@specs/aws/fsx/docs/API_AssociateFileSystemAliases"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS AssociateFileSystemAliases"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# AssociateFileSystemAliases

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_AssociateFileSystemAliases
> **target_lang:** meta — documentation tier. ALL sections preserved.



# AssociateFileSystemAliases
<a name="API_AssociateFileSystemAliases"></a>

Use this action to associate one or more Domain Name Server (DNS) aliases with an existing Amazon FSx for Windows File Server file system. A file system can have a maximum of 50 DNS aliases associated with it at any one time. If you try to associate a DNS alias that is already associated with the file system, FSx takes no action on that alias in the request. For more information, see [Working with DNS Aliases](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html) and [Walkthrough 5: Using DNS aliases to access your file system](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/walkthrough05-file-system-custom-CNAME.html), including additional steps you must take to be able to access your file system using a DNS alias.

The system response shows the DNS aliases that Amazon FSx is attempting to associate with the file system. Use the [DescribeFileSystemAliases](API_DescribeFileSystemAliases.md) API operation to monitor the status of the aliases Amazon FSx is associating with the file system.

## Request Syntax
<a name="API_AssociateFileSystemAliases_RequestSyntax"></a>

```
{
   "Aliases": [ "{{string}}" ],
   "ClientRequestToken": "{{string}}",
   "FileSystemId": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateFileSystemAliases_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Aliases](#API_AssociateFileSystemAliases_RequestSyntax) **   <a name="FSx-AssociateFileSystemAliases-request-Aliases"></a>
An array of one or more DNS alias names to associate with the file system. The alias name has to comply with the following formatting requirements:  
+ Formatted as a fully-qualified domain name (FQDN), * `hostname.domain` *, for example, `accounting.corp.example.com`.
+ Can contain alphanumeric characters and the hyphen (-).
+ Cannot start or end with a hyphen.
+ Can start with a numeric.
For DNS alias names, Amazon FSx stores alphabetic characters as lowercase letters (a-z), regardless of how you specify them: as uppercase letters, lowercase letters, or the corresponding letters in escape codes.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 4. Maximum length of 253.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{4,253}$`   
Required: Yes

 ** [ClientRequestToken](#API_AssociateFileSystemAliases_RequestSyntax) **   <a name="FSx-AssociateFileSystemAliases-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [FileSystemId](#API_AssociateFileSystemAliases_RequestSyntax) **   <a name="FSx-AssociateFileSystemAliases-request-FileSystemId"></a>
Specifies the file system with which you want to associate one or more DNS aliases.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fs-[0-9a-f]{8,})$`   
Required: Yes

## Response Syntax
<a name="API_AssociateFileSystemAliases_ResponseSyntax"></a>

```
{
   "Aliases": [ 
      { 
         "Lifecycle": "string",
         "Name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_AssociateFileSystemAliases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Aliases](#API_AssociateFileSystemAliases_ResponseSyntax) **   <a name="FSx-AssociateFileSystemAliases-response-Aliases"></a>
An array of the DNS aliases that Amazon FSx is associating with the file system.  
Type: Array of [Alias](API_Alias.md) objects  
Array Members: Maximum number of 50 items.

## Errors
<a name="API_AssociateFileSystemAliases_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

## See Also
<a name="API_AssociateFileSystemAliases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/AssociateFileSystemAliases) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/AssociateFileSystemAliases) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/AssociateFileSystemAliases) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/AssociateFileSystemAliases) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/AssociateFileSystemAliases) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/AssociateFileSystemAliases) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/AssociateFileSystemAliases) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/AssociateFileSystemAliases) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/AssociateFileSystemAliases) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/AssociateFileSystemAliases) 