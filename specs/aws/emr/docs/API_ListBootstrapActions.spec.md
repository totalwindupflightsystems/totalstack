---
id: "@specs/aws/emr/docs/API_ListBootstrapActions"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListBootstrapActions"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ListBootstrapActions

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ListBootstrapActions
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListBootstrapActions
<a name="API_ListBootstrapActions"></a>

Provides information about the bootstrap actions associated with a cluster.

## Request Syntax
<a name="API_ListBootstrapActions_RequestSyntax"></a>

```
{
   "ClusterId": "{{string}}",
   "Marker": "{{string}}"
}
```

## Request Parameters
<a name="API_ListBootstrapActions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClusterId](#API_ListBootstrapActions_RequestSyntax) **   <a name="EMR-ListBootstrapActions-request-ClusterId"></a>
The cluster identifier for the bootstrap actions to list.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: Yes

 ** [Marker](#API_ListBootstrapActions_RequestSyntax) **   <a name="EMR-ListBootstrapActions-request-Marker"></a>
The pagination token that indicates the next set of results to retrieve.  
Type: String  
Required: No

## Response Syntax
<a name="API_ListBootstrapActions_ResponseSyntax"></a>

```
{
   "BootstrapActions": [ 
      { 
         "Args": [ "string" ],
         "Name": "string",
         "ScriptPath": "string"
      }
   ],
   "Marker": "string"
}
```

## Response Elements
<a name="API_ListBootstrapActions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BootstrapActions](#API_ListBootstrapActions_ResponseSyntax) **   <a name="EMR-ListBootstrapActions-response-BootstrapActions"></a>
The bootstrap actions associated with the cluster.  
Type: Array of [Command](API_Command.md) objects

 ** [Marker](#API_ListBootstrapActions_ResponseSyntax) **   <a name="EMR-ListBootstrapActions-response-Marker"></a>
The pagination token that indicates the next set of results to retrieve.  
Type: String

## Errors
<a name="API_ListBootstrapActions_Errors"></a>

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
<a name="API_ListBootstrapActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/ListBootstrapActions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/ListBootstrapActions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ListBootstrapActions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/ListBootstrapActions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ListBootstrapActions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/ListBootstrapActions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/ListBootstrapActions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/ListBootstrapActions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/ListBootstrapActions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ListBootstrapActions) 