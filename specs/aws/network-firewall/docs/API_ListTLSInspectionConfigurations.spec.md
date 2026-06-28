---
id: "@specs/aws/network-firewall/docs/API_ListTLSInspectionConfigurations"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTLSInspectionConfigurations"
status: active
depends_on:
  - "@specs/aws/network-firewall/meta"
---

# ListTLSInspectionConfigurations

> **source:** AWS Documentation
> **spec:id:** @specs/aws/network-firewall/docs/API_ListTLSInspectionConfigurations
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTLSInspectionConfigurations
<a name="API_ListTLSInspectionConfigurations"></a>

Retrieves the metadata for the TLS inspection configurations that you have defined. Depending on your setting for max results and the number of TLS inspection configurations, a single call might not return the full list.

## Request Syntax
<a name="API_ListTLSInspectionConfigurations_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTLSInspectionConfigurations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListTLSInspectionConfigurations_RequestSyntax) **   <a name="networkfirewall-ListTLSInspectionConfigurations-request-MaxResults"></a>
The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a `NextToken` value that you can use in a subsequent call to get the next batch of objects.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [NextToken](#API_ListTLSInspectionConfigurations_RequestSyntax) **   <a name="networkfirewall-ListTLSInspectionConfigurations-request-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `[0-9A-Za-z:\/+=]+$`   
Required: No

## Response Syntax
<a name="API_ListTLSInspectionConfigurations_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "TLSInspectionConfigurations": [ 
      { 
         "Arn": "string",
         "Name": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTLSInspectionConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTLSInspectionConfigurations_ResponseSyntax) **   <a name="networkfirewall-ListTLSInspectionConfigurations-response-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Pattern: `[0-9A-Za-z:\/+=]+$` 

 ** [TLSInspectionConfigurations](#API_ListTLSInspectionConfigurations_ResponseSyntax) **   <a name="networkfirewall-ListTLSInspectionConfigurations-response-TLSInspectionConfigurations"></a>
The TLS inspection configuration metadata objects that you've defined. Depending on your setting for max results and the number of TLS inspection configurations, this might not be the full list.  
Type: Array of [TLSInspectionConfigurationMetadata](API_TLSInspectionConfigurationMetadata.md) objects

## Errors
<a name="API_ListTLSInspectionConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **   
Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request.   
HTTP Status Code: 500

 ** InvalidRequestException **   
The operation failed because of a problem with your request. Examples include:   
+ You specified an unsupported parameter name or value.
+ You tried to update a property with a value that isn't among the available types.
+ Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.
HTTP Status Code: 400

 ** ThrottlingException **   
Unable to process the request due to throttling limitations.  
HTTP Status Code: 400

## See Also
<a name="API_ListTLSInspectionConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/ListTLSInspectionConfigurations) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/ListTLSInspectionConfigurations) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/ListTLSInspectionConfigurations) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/ListTLSInspectionConfigurations) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/ListTLSInspectionConfigurations) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/ListTLSInspectionConfigurations) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/ListTLSInspectionConfigurations) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/ListTLSInspectionConfigurations) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/ListTLSInspectionConfigurations) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/ListTLSInspectionConfigurations) 