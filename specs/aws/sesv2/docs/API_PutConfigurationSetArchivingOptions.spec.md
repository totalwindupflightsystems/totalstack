---
id: "@specs/aws/sesv2/docs/API_PutConfigurationSetArchivingOptions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutConfigurationSetArchivingOptions"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# PutConfigurationSetArchivingOptions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_PutConfigurationSetArchivingOptions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutConfigurationSetArchivingOptions
<a name="API_PutConfigurationSetArchivingOptions"></a>

Associate the configuration set with a MailManager archive. When you send email using the `SendEmail` or `SendBulkEmail` operations the message as it will be given to the receiving SMTP server will be archived, along with the recipient information.

## Request Syntax
<a name="API_PutConfigurationSetArchivingOptions_RequestSyntax"></a>

```
PUT /v2/email/configuration-sets/{{ConfigurationSetName}}/archiving-options HTTP/1.1
Content-type: application/json

{
   "ArchiveArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutConfigurationSetArchivingOptions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConfigurationSetName](#API_PutConfigurationSetArchivingOptions_RequestSyntax) **   <a name="SES-PutConfigurationSetArchivingOptions-request-uri-ConfigurationSetName"></a>
The name of the configuration set to associate with a MailManager archive.  
Required: Yes

## Request Body
<a name="API_PutConfigurationSetArchivingOptions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ArchiveArn](#API_PutConfigurationSetArchivingOptions_RequestSyntax) **   <a name="SES-PutConfigurationSetArchivingOptions-request-ArchiveArn"></a>
The Amazon Resource Name (ARN) of the MailManager archive that the Amazon SES API v2 sends email to.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:(aws|aws-[a-z-]+):ses:[a-z]{2,4}-[a-z-]+-[0-9]:[0-9]{1,20}:mailmanager-archive/a-[a-z0-9]{24,62}`   
Required: No

## Response Syntax
<a name="API_PutConfigurationSetArchivingOptions_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutConfigurationSetArchivingOptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutConfigurationSetArchivingOptions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** NotFoundException **   
The resource you attempted to access doesn't exist.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_PutConfigurationSetArchivingOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/PutConfigurationSetArchivingOptions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/PutConfigurationSetArchivingOptions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/PutConfigurationSetArchivingOptions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/PutConfigurationSetArchivingOptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/PutConfigurationSetArchivingOptions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/PutConfigurationSetArchivingOptions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/PutConfigurationSetArchivingOptions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/PutConfigurationSetArchivingOptions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/PutConfigurationSetArchivingOptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/PutConfigurationSetArchivingOptions) 