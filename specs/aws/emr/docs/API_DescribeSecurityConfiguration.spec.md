---
id: "@specs/aws/emr/docs/API_DescribeSecurityConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeSecurityConfiguration"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# DescribeSecurityConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_DescribeSecurityConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeSecurityConfiguration
<a name="API_DescribeSecurityConfiguration"></a>

Provides the details of a security configuration by returning the configuration JSON.

## Request Syntax
<a name="API_DescribeSecurityConfiguration_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeSecurityConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_DescribeSecurityConfiguration_RequestSyntax) **   <a name="EMR-DescribeSecurityConfiguration-request-Name"></a>
The name of the security configuration.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`   
Required: Yes

## Response Syntax
<a name="API_DescribeSecurityConfiguration_ResponseSyntax"></a>

```
{
   "CreationDateTime": number,
   "Name": "string",
   "SecurityConfiguration": "string"
}
```

## Response Elements
<a name="API_DescribeSecurityConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationDateTime](#API_DescribeSecurityConfiguration_ResponseSyntax) **   <a name="EMR-DescribeSecurityConfiguration-response-CreationDateTime"></a>
The date and time the security configuration was created  
Type: Timestamp

 ** [Name](#API_DescribeSecurityConfiguration_ResponseSyntax) **   <a name="EMR-DescribeSecurityConfiguration-response-Name"></a>
The name of the security configuration.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 10280.  
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*` 

 ** [SecurityConfiguration](#API_DescribeSecurityConfiguration_ResponseSyntax) **   <a name="EMR-DescribeSecurityConfiguration-response-SecurityConfiguration"></a>
The security configuration details in JSON format.  
Type: String

## Errors
<a name="API_DescribeSecurityConfiguration_Errors"></a>

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
<a name="API_DescribeSecurityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/DescribeSecurityConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/DescribeSecurityConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/DescribeSecurityConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/DescribeSecurityConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/DescribeSecurityConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/DescribeSecurityConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/DescribeSecurityConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/DescribeSecurityConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/DescribeSecurityConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/DescribeSecurityConfiguration) 