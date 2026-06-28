---
id: "@specs/aws/fsx/docs/API_DescribeFileSystemAliases"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeFileSystemAliases"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# DescribeFileSystemAliases

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_DescribeFileSystemAliases
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeFileSystemAliases
<a name="API_DescribeFileSystemAliases"></a>

Returns the DNS aliases that are associated with the specified Amazon FSx for Windows File Server file system. A history of all DNS aliases that have been associated with and disassociated from the file system is available in the list of [AdministrativeAction](API_AdministrativeAction.md) provided in the [DescribeFileSystems](API_DescribeFileSystems.md) operation response.

## Request Syntax
<a name="API_DescribeFileSystemAliases_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "FileSystemId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFileSystemAliases_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_DescribeFileSystemAliases_RequestSyntax) **   <a name="FSx-DescribeFileSystemAliases-request-ClientRequestToken"></a>
(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the AWS Command Line Interface (AWS CLI) or an AWS SDK.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `[A-za-z0-9_.-]{0,63}$`   
Required: No

 ** [FileSystemId](#API_DescribeFileSystemAliases_RequestSyntax) **   <a name="FSx-DescribeFileSystemAliases-request-FileSystemId"></a>
The ID of the file system to return the associated DNS aliases for (String).  
Type: String  
Length Constraints: Minimum length of 11. Maximum length of 21.  
Pattern: `^(fs-[0-9a-f]{8,})$`   
Required: Yes

 ** [MaxResults](#API_DescribeFileSystemAliases_RequestSyntax) **   <a name="FSx-DescribeFileSystemAliases-request-MaxResults"></a>
Maximum number of DNS aliases to return in the response (integer). This parameter value must be greater than 0. The number of items that Amazon FSx returns is the minimum of the `MaxResults` parameter specified in the request and the service's internal maximum number of items per page.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 2147483647.  
Required: No

 ** [NextToken](#API_DescribeFileSystemAliases_RequestSyntax) **   <a name="FSx-DescribeFileSystemAliases-request-NextToken"></a>
Opaque pagination token returned from a previous `DescribeFileSystemAliases` operation (String). If a token is included in the request, the action continues the list from where the previous returning call left off.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$`   
Required: No

## Response Syntax
<a name="API_DescribeFileSystemAliases_ResponseSyntax"></a>

```
{
   "Aliases": [ 
      { 
         "Lifecycle": "string",
         "Name": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_DescribeFileSystemAliases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Aliases](#API_DescribeFileSystemAliases_ResponseSyntax) **   <a name="FSx-DescribeFileSystemAliases-response-Aliases"></a>
An array of one or more DNS aliases currently associated with the specified file system.  
Type: Array of [Alias](API_Alias.md) objects  
Array Members: Maximum number of 50 items.

 ** [NextToken](#API_DescribeFileSystemAliases_ResponseSyntax) **   <a name="FSx-DescribeFileSystemAliases-response-NextToken"></a>
Present if there are more DNS aliases than returned in the response (String). You can use the `NextToken` value in a later request to fetch additional descriptions.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$` 

## Errors
<a name="API_DescribeFileSystemAliases_Errors"></a>

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
<a name="API_DescribeFileSystemAliases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/DescribeFileSystemAliases) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/DescribeFileSystemAliases) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/DescribeFileSystemAliases) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/DescribeFileSystemAliases) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/DescribeFileSystemAliases) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/DescribeFileSystemAliases) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/DescribeFileSystemAliases) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/DescribeFileSystemAliases) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/DescribeFileSystemAliases) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/DescribeFileSystemAliases) 