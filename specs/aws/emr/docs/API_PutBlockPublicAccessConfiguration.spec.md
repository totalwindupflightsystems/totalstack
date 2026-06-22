---
id: "@specs/aws/emr/docs/API_PutBlockPublicAccessConfiguration"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS PutBlockPublicAccessConfiguration"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# PutBlockPublicAccessConfiguration

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_PutBlockPublicAccessConfiguration
> **target_lang:** meta — documentation tier. ALL sections preserved.



# PutBlockPublicAccessConfiguration
<a name="API_PutBlockPublicAccessConfiguration"></a>

Creates or updates an Amazon EMR block public access configuration for your AWS account in the current Region. For more information see [Configure Block Public Access for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/configure-block-public-access.html) in the *Amazon EMR Management Guide*.

## Request Syntax
<a name="API_PutBlockPublicAccessConfiguration_RequestSyntax"></a>

```
{
   "BlockPublicAccessConfiguration": { 
      "BlockPublicSecurityGroupRules": {{boolean}},
      "PermittedPublicSecurityGroupRuleRanges": [ 
         { 
            "MaxRange": {{number}},
            "MinRange": {{number}}
         }
      ]
   }
}
```

## Request Parameters
<a name="API_PutBlockPublicAccessConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BlockPublicAccessConfiguration](#API_PutBlockPublicAccessConfiguration_RequestSyntax) **   <a name="EMR-PutBlockPublicAccessConfiguration-request-BlockPublicAccessConfiguration"></a>
A configuration for Amazon EMR block public access. The configuration applies to all clusters created in your account for the current Region. The configuration specifies whether block public access is enabled. If block public access is enabled, security groups associated with the cluster cannot have rules that allow inbound traffic from 0.0.0.0/0 or ::/0 on a port, unless the port is specified as an exception using `PermittedPublicSecurityGroupRuleRanges` in the `BlockPublicAccessConfiguration`. By default, Port 22 (SSH) is an exception, and public access is allowed on this port. You can change this by updating `BlockPublicSecurityGroupRules` to remove the exception.  
For accounts that created clusters in a Region before November 25, 2019, block public access is disabled by default in that Region. To use this feature, you must manually enable and configure it. For accounts that did not create an Amazon EMR cluster in a Region before this date, block public access is enabled by default in that Region.
Type: [BlockPublicAccessConfiguration](API_BlockPublicAccessConfiguration.md) object  
Required: Yes

## Response Elements
<a name="API_PutBlockPublicAccessConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutBlockPublicAccessConfiguration_Errors"></a>

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
<a name="API_PutBlockPublicAccessConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/PutBlockPublicAccessConfiguration) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/PutBlockPublicAccessConfiguration) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/PutBlockPublicAccessConfiguration) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/PutBlockPublicAccessConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/PutBlockPublicAccessConfiguration) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/PutBlockPublicAccessConfiguration) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/PutBlockPublicAccessConfiguration) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/PutBlockPublicAccessConfiguration) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/PutBlockPublicAccessConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/PutBlockPublicAccessConfiguration) 