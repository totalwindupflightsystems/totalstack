---
id: "@specs/aws/sesv2/docs/API_ListConfigurationSets"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListConfigurationSets"
status: active
depends_on:
  - "@specs/aws/sesv2/meta"
---

# ListConfigurationSets

> **source:** AWS Documentation
> **spec:id:** @specs/aws/sesv2/docs/API_ListConfigurationSets
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListConfigurationSets
<a name="API_ListConfigurationSets"></a>

List all of the configuration sets associated with your account in the current region.

 *Configuration sets* are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.

## Request Syntax
<a name="API_ListConfigurationSets_RequestSyntax"></a>

```
GET /v2/email/configuration-sets?NextToken={{NextToken}}&PageSize={{PageSize}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListConfigurationSets_RequestParameters"></a>

The request uses the following URI parameters.

 ** [NextToken](#API_ListConfigurationSets_RequestSyntax) **   <a name="SES-ListConfigurationSets-request-uri-NextToken"></a>
A token returned from a previous call to `ListConfigurationSets` to indicate the position in the list of configuration sets.

 ** [PageSize](#API_ListConfigurationSets_RequestSyntax) **   <a name="SES-ListConfigurationSets-request-uri-PageSize"></a>
The number of results to show in a single call to `ListConfigurationSets`. If the number of results is larger than the number you specified in this parameter, then the response includes a `NextToken` element, which you can use to obtain additional results.

## Request Body
<a name="API_ListConfigurationSets_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListConfigurationSets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConfigurationSets": [ "string" ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListConfigurationSets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfigurationSets](#API_ListConfigurationSets_ResponseSyntax) **   <a name="SES-ListConfigurationSets-response-ConfigurationSets"></a>
An array that contains all of the configuration sets in your Amazon SES account in the current AWS Region.  
Type: Array of strings

 ** [NextToken](#API_ListConfigurationSets_ResponseSyntax) **   <a name="SES-ListConfigurationSets-response-NextToken"></a>
A token that indicates that there are additional configuration sets to list. To view additional configuration sets, issue another request to `ListConfigurationSets`, and pass this token in the `NextToken` parameter.  
Type: String

## Errors
<a name="API_ListConfigurationSets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The input you provided is invalid.  
HTTP Status Code: 400

 ** TooManyRequestsException **   
Too many requests have been made to the operation.  
HTTP Status Code: 429

## See Also
<a name="API_ListConfigurationSets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sesv2-2019-09-27/ListConfigurationSets) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sesv2-2019-09-27/ListConfigurationSets) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/ListConfigurationSets) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sesv2-2019-09-27/ListConfigurationSets) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/ListConfigurationSets) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sesv2-2019-09-27/ListConfigurationSets) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sesv2-2019-09-27/ListConfigurationSets) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sesv2-2019-09-27/ListConfigurationSets) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sesv2-2019-09-27/ListConfigurationSets) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/ListConfigurationSets) 