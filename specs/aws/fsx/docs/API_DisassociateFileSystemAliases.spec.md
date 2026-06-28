---
id: "@specs/aws/fsx/docs/API_DisassociateFileSystemAliases"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DisassociateFileSystemAliases"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DisassociateFileSystemAliases

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DisassociateFileSystemAliases
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DisassociateFileSystemAliases
<a name="API_DisassociateFileSystemAliases"></a>

Use this action to disassociate, or remove, one or more Domain Name Service (DNS) aliases from an Amazon FSx for Windows File Server file system. If you attempt to disassociate a DNS alias that is not associated with the file system, Amazon FSx responds with an HTTP status code 400 (Bad Request). For more information, see [Working with DNS Aliases](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/managing-dns-aliases.html).

The system generated response showing the DNS aliases that Amazon FSx is attempting to disassociate from the file system. Use the [DescribeFileSystemAliases](API_DescribeFileSystemAliases.md) API operation to monitor the status of the aliases Amazon FSx is disassociating with the file system.

## Request Syntax
<a name="API_DisassociateFileSystemAliases_RequestSyntax"></a>

```
{
   "Aliases": [ "{{string}}" ],
   "ClientRequestToken": "{{string}}",
   "FileSystemId": "{{string}}"
}
```

## Request Parameters
<a name="API_DisassociateFileSystemAliases_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Aliases](#API_DisassociateFileSystemAliases_RequestSyntax) **   <a name="FSx-DisassociateFileSystemAliases-request-Aliases"></a>
An array of one or more DNS alias names to disassociate, or remove, from the file system.  
Type: Array of strings  
Array Members: Maximum number of 50 items.  
Length Constraints: Minimum length of 4. Maximum length of 253.  
Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{4,253}$`   
Required: Yes

 ** [ClientRequestToken](#API_DisassociateFileSystemAliases_RequestSyntax) **   <a name="FSx-DisassociateFileSystemAliases-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [FileSystemId](#API_DisassociateFileSystemAliases_RequestSyntax) **   <a name="FSx-DisassociateFileSystemAliases-request-FileSystemId"></a>
Specifies the file system from which to disassociate the DNS aliases.  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fs-[0-9a-f]{8,})$`   
Required: Yes

## Response Syntax
<a name="API_DisassociateFileSystemAliases_ResponseSyntax"></a>

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
<a name="API_DisassociateFileSystemAliases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Aliases](#API_DisassociateFileSystemAliases_ResponseSyntax) **   <a name="FSx-DisassociateFileSystemAliases-response-Aliases"></a>
An array of one or more DNS aliases that Amazon FSx is attempting to disassociate from the file system.  
Type: Array of [Alias](API_Alias.md) objects  
Array Members: Maximum number of 50 items.

## Errors
<a name="API_DisassociateFileSystemAliases_Errors"></a>

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
<a name="API_DisassociateFileSystemAliases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DisassociateFileSystemAliases) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DisassociateFileSystemAliases) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DisassociateFileSystemAliases) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DisassociateFileSystemAliases) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DisassociateFileSystemAliases) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DisassociateFileSystemAliases) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DisassociateFileSystemAliases) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DisassociateFileSystemAliases) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DisassociateFileSystemAliases) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DisassociateFileSystemAliases) 