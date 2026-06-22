---
id: "@specs/aws/emr/docs/API_DescribePersistentAppUI"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribePersistentAppUI"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# DescribePersistentAppUI

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_DescribePersistentAppUI
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribePersistentAppUI
<a name="API_DescribePersistentAppUI"></a>

Describes a persistent application user interface.

## Request Syntax
<a name="API_DescribePersistentAppUI_RequestSyntax"></a>

```
{
   "PersistentAppUIId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribePersistentAppUI_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [PersistentAppUIId](#API_DescribePersistentAppUI_RequestSyntax) **   <a name="EMR-DescribePersistentAppUI-request-PersistentAppUIId"></a>
The identifier for the persistent application user interface.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

## Response Syntax
<a name="API_DescribePersistentAppUI_ResponseSyntax"></a>

```
{
   "PersistentAppUI": { 
      "AuthorId": "string",
      "CreationTime": number,
      "LastModifiedTime": number,
      "LastStateChangeReason": "string",
      "PersistentAppUIId": "string",
      "PersistentAppUIStatus": "string",
      "PersistentAppUITypeList": [ "string" ],
      "Tags": [ 
         { 
            "Key": "string",
            "Value": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_DescribePersistentAppUI_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PersistentAppUI](#API_DescribePersistentAppUI_ResponseSyntax) **   <a name="EMR-DescribePersistentAppUI-response-PersistentAppUI"></a>
The persistent application user interface.  
Type: [PersistentAppUI](API_PersistentAppUI.md) object

## Errors
<a name="API_DescribePersistentAppUI_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **   
This exception occurs when there is an internal failure in the Amazon EMR service.    
 ** Message **   
The message associated with the exception.
HTTP Status Code: 500

 ** InvalidRequestException **   
This exception occurs when there is something wrong with user input.    
 ** ErrorCode **   
The error code associated with the exception.  
 ** Message **   
The message associated with the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribePersistentAppUI_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/DescribePersistentAppUI) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/DescribePersistentAppUI) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/DescribePersistentAppUI) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/DescribePersistentAppUI) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/DescribePersistentAppUI) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/DescribePersistentAppUI) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/DescribePersistentAppUI) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/DescribePersistentAppUI) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/DescribePersistentAppUI) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/DescribePersistentAppUI) 