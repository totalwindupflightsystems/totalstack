---
id: "@specs/aws/emr/docs/API_DescribeReleaseLabel"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeReleaseLabel"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# DescribeReleaseLabel

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_DescribeReleaseLabel
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeReleaseLabel
<a name="API_DescribeReleaseLabel"></a>

Provides Amazon EMR release label details, such as the releases available the Region where the API request is run, and the available applications for a specific Amazon EMR release label. Can also list Amazon EMR releases that support a specified version of Spark.

## Request Syntax
<a name="API_DescribeReleaseLabel_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ReleaseLabel": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeReleaseLabel_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DescribeReleaseLabel_RequestSyntax) **   <a name="EMR-DescribeReleaseLabel-request-MaxResults"></a>
Reserved for future use. Currently set to null.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_DescribeReleaseLabel_RequestSyntax) **   <a name="EMR-DescribeReleaseLabel-request-NextToken"></a>
The pagination token. Reserved for future use. Currently set to null.  
Type: String  
Required: No

 ** [ReleaseLabel](#API_DescribeReleaseLabel_RequestSyntax) **   <a name="EMR-DescribeReleaseLabel-request-ReleaseLabel"></a>
The target release label to be described.  
Type: String  
Required: No

## Response Syntax
<a name="API_DescribeReleaseLabel_ResponseSyntax"></a>

```
{
   "Applications": [ 
      { 
         "Name": "string",
         "Version": "string"
      }
   ],
   "AvailableOSReleases": [ 
      { 
         "Label": "string"
      }
   ],
   "NextToken": "string",
   "ReleaseLabel": "string"
}
```

## Response Elements
<a name="API_DescribeReleaseLabel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Applications](#API_DescribeReleaseLabel_ResponseSyntax) **   <a name="EMR-DescribeReleaseLabel-response-Applications"></a>
The list of applications available for the target release label. `Name` is the name of the application. `Version` is the concise version of the application.  
Type: Array of [SimplifiedApplication](API_SimplifiedApplication.md) objects

 ** [AvailableOSReleases](#API_DescribeReleaseLabel_ResponseSyntax) **   <a name="EMR-DescribeReleaseLabel-response-AvailableOSReleases"></a>
The list of available Amazon Linux release versions for an Amazon EMR release. Contains a Label field that is formatted as shown in [https://docs.aws.amazon.com/AL2/latest/relnotes/relnotes-al2.html](https://docs.aws.amazon.com/AL2/latest/relnotes/relnotes-al2.html). For example, [2.0.20220218.1](https://docs.aws.amazon.com/AL2/latest/relnotes/relnotes-20220218.html).  
Type: Array of [OSRelease](API_OSRelease.md) objects

 ** [NextToken](#API_DescribeReleaseLabel_ResponseSyntax) **   <a name="EMR-DescribeReleaseLabel-response-NextToken"></a>
The pagination token. Reserved for future use. Currently set to null.  
Type: String

 ** [ReleaseLabel](#API_DescribeReleaseLabel_ResponseSyntax) **   <a name="EMR-DescribeReleaseLabel-response-ReleaseLabel"></a>
The target release label described in the response.  
Type: String

## Errors
<a name="API_DescribeReleaseLabel_Errors"></a>

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
<a name="API_DescribeReleaseLabel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/DescribeReleaseLabel) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/DescribeReleaseLabel) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/DescribeReleaseLabel) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/DescribeReleaseLabel) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/DescribeReleaseLabel) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/DescribeReleaseLabel) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/DescribeReleaseLabel) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/DescribeReleaseLabel) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/DescribeReleaseLabel) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/DescribeReleaseLabel) 