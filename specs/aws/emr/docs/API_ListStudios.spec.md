---
id: "@specs/aws/emr/docs/API_ListStudios"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListStudios"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ListStudios

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ListStudios
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListStudios
<a name="API_ListStudios"></a>

Returns a list of all Amazon EMR Studios associated with the AWS account. The list includes details such as ID, Studio Access URL, and creation time for each Studio.

## Request Syntax
<a name="API_ListStudios_RequestSyntax"></a>

```
{
   "Marker": "{{string}}"
}
```

## Request Parameters
<a name="API_ListStudios_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Marker](#API_ListStudios_RequestSyntax) **   <a name="EMR-ListStudios-request-Marker"></a>
The pagination token that indicates the set of results to retrieve.  
Type: String  
Required: No

## Response Syntax
<a name="API_ListStudios_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "Studios": [ 
      { 
         "AuthMode": "string",
         "CreationTime": number,
         "Description": "string",
         "Name": "string",
         "StudioId": "string",
         "Url": "string",
         "VpcId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListStudios_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_ListStudios_ResponseSyntax) **   <a name="EMR-ListStudios-response-Marker"></a>
The pagination token that indicates the next set of results to retrieve.  
Type: String

 ** [Studios](#API_ListStudios_ResponseSyntax) **   <a name="EMR-ListStudios-response-Studios"></a>
The list of Studio summary objects.  
Type: Array of [StudioSummary](API_StudioSummary.md) objects

## Errors
<a name="API_ListStudios_Errors"></a>

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
<a name="API_ListStudios_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/ListStudios) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/ListStudios) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ListStudios) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/ListStudios) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ListStudios) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/ListStudios) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/ListStudios) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/ListStudios) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/ListStudios) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ListStudios) 