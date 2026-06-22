---
id: "@specs/aws/emr/docs/API_ListSecurityConfigurations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListSecurityConfigurations"
status: active
depends_on:
  - "@specs/aws/emr/meta"
---

# ListSecurityConfigurations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/emr/docs/API_ListSecurityConfigurations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListSecurityConfigurations
<a name="API_ListSecurityConfigurations"></a>

Lists all the security configurations visible to this account, providing their creation dates and times, and their names. This call returns a maximum of 50 clusters per call, but returns a marker to track the paging of the cluster list across multiple ListSecurityConfigurations calls.

## Request Syntax
<a name="API_ListSecurityConfigurations_RequestSyntax"></a>

```
{
   "Marker": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSecurityConfigurations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Marker](#API_ListSecurityConfigurations_RequestSyntax) **   <a name="EMR-ListSecurityConfigurations-request-Marker"></a>
The pagination token that indicates the set of results to retrieve.  
Type: String  
Required: No

## Response Syntax
<a name="API_ListSecurityConfigurations_ResponseSyntax"></a>

```
{
   "Marker": "string",
   "SecurityConfigurations": [ 
      { 
         "CreationDateTime": number,
         "Name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSecurityConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Marker](#API_ListSecurityConfigurations_ResponseSyntax) **   <a name="EMR-ListSecurityConfigurations-response-Marker"></a>
A pagination token that indicates the next set of results to retrieve. Include the marker in the next ListSecurityConfiguration call to retrieve the next page of results, if required.  
Type: String

 ** [SecurityConfigurations](#API_ListSecurityConfigurations_ResponseSyntax) **   <a name="EMR-ListSecurityConfigurations-response-SecurityConfigurations"></a>
The creation date and time, and name, of each security configuration.  
Type: Array of [SecurityConfigurationSummary](API_SecurityConfigurationSummary.md) objects

## Errors
<a name="API_ListSecurityConfigurations_Errors"></a>

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
<a name="API_ListSecurityConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticmapreduce-2009-03-31/ListSecurityConfigurations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticmapreduce-2009-03-31/ListSecurityConfigurations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ListSecurityConfigurations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticmapreduce-2009-03-31/ListSecurityConfigurations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ListSecurityConfigurations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticmapreduce-2009-03-31/ListSecurityConfigurations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticmapreduce-2009-03-31/ListSecurityConfigurations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticmapreduce-2009-03-31/ListSecurityConfigurations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticmapreduce-2009-03-31/ListSecurityConfigurations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ListSecurityConfigurations) 