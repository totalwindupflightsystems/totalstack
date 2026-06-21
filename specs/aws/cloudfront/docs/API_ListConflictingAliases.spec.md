---
id: "@specs/aws/cloudfront/docs/API_ListConflictingAliases"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListConflictingAliases"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ListConflictingAliases

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ListConflictingAliases
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListConflictingAliases
<a name="API_ListConflictingAliases"></a>

**Note**  
The `ListConflictingAliases` API operation only supports standard distributions. To list domain conflicts for both standard distributions and distribution tenants, we recommend that you use the [ListDomainConflicts](https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDomainConflicts.html) API operation instead.

Gets a list of aliases that conflict or overlap with the provided alias, and the associated CloudFront standard distribution and AWS accounts for each conflicting alias. An alias is commonly known as a custom domain or vanity domain. It can also be called a CNAME or alternate domain name.

In the returned list, the standard distribution and account IDs are partially hidden, which allows you to identify the standard distribution and accounts that you own, and helps to protect the information of ones that you don't own.

Use this operation to find aliases that are in use in CloudFront that conflict or overlap with the provided alias. For example, if you provide `www.example.com` as input, the returned list can include `www.example.com` and the overlapping wildcard alternate domain name (`*.example.com`), if they exist. If you provide `*.example.com` as input, the returned list can include `*.example.com` and any alternate domain names covered by that wildcard (for example, `www.example.com`, `test.example.com`, `dev.example.com`, and so on), if they exist.

To list conflicting aliases, specify the alias to search and the ID of a standard distribution in your account that has an attached TLS certificate that includes the provided alias. For more information, including how to set up the standard distribution and certificate, see [Moving an alternate domain name to a different standard distribution or distribution tenant](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-move) in the *Amazon CloudFront Developer Guide*.

You can optionally specify the maximum number of items to receive in the response. If the total number of items in the list exceeds the maximum that you specify, or the default maximum, the response is paginated. To get the next page of items, send a subsequent request that specifies the `NextMarker` value from the current response as the `Marker` value in the subsequent request.

## Request Syntax
<a name="API_ListConflictingAliases_RequestSyntax"></a>

```
GET /2020-05-31/conflicting-alias?Alias={{Alias}}&DistributionId={{DistributionId}}&Marker={{Marker}}&MaxItems={{MaxItems}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListConflictingAliases_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Alias](#API_ListConflictingAliases_RequestSyntax) **   <a name="cloudfront-ListConflictingAliases-request-uri-Alias"></a>
The alias (also called a CNAME) to search for conflicting aliases.  
Length Constraints: Minimum length of 0. Maximum length of 253.  
Required: Yes

 ** [DistributionId](#API_ListConflictingAliases_RequestSyntax) **   <a name="cloudfront-ListConflictingAliases-request-uri-DistributionId"></a>
The ID of a standard distribution in your account that has an attached TLS certificate that includes the provided alias.  
Length Constraints: Minimum length of 0. Maximum length of 25.  
Required: Yes

 ** [Marker](#API_ListConflictingAliases_RequestSyntax) **   <a name="cloudfront-ListConflictingAliases-request-uri-Marker"></a>
Use this field when paginating results to indicate where to begin in the list of conflicting aliases. The response includes conflicting aliases in the list that occur after the marker. To get the next page of the list, set this field's value to the value of `NextMarker` from the current page's response.

 ** [MaxItems](#API_ListConflictingAliases_RequestSyntax) **   <a name="cloudfront-ListConflictingAliases-request-uri-MaxItems"></a>
The maximum number of conflicting aliases that you want in the response.  
Valid Range: Maximum value of 100.

## Request Body
<a name="API_ListConflictingAliases_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListConflictingAliases_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ConflictingAliasesList>
   <Items>
      <ConflictingAlias>
         <AccountId>string</AccountId>
         <Alias>string</Alias>
         <DistributionId>string</DistributionId>
      </ConflictingAlias>
   </Items>
   <MaxItems>integer</MaxItems>
   <NextMarker>string</NextMarker>
   <Quantity>integer</Quantity>
</ConflictingAliasesList>
```

## Response Elements
<a name="API_ListConflictingAliases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [ConflictingAliasesList](#API_ListConflictingAliases_ResponseSyntax) **   <a name="cloudfront-ListConflictingAliases-response-ConflictingAliasesList"></a>
Root level tag for the ConflictingAliasesList parameters.  
Required: Yes

 ** [Items](#API_ListConflictingAliases_ResponseSyntax) **   <a name="cloudfront-ListConflictingAliases-response-Items"></a>
Contains the conflicting aliases in the list.  
Type: Array of [ConflictingAlias](API_ConflictingAlias.md) objects

 ** [MaxItems](#API_ListConflictingAliases_ResponseSyntax) **   <a name="cloudfront-ListConflictingAliases-response-MaxItems"></a>
The maximum number of conflicting aliases requested.  
Type: Integer

 ** [NextMarker](#API_ListConflictingAliases_ResponseSyntax) **   <a name="cloudfront-ListConflictingAliases-response-NextMarker"></a>
If there are more items in the list than are in this response, this element is present. It contains the value that you should use in the `Marker` field of a subsequent request to continue listing conflicting aliases where you left off.  
Type: String

 ** [Quantity](#API_ListConflictingAliases_ResponseSyntax) **   <a name="cloudfront-ListConflictingAliases-response-Quantity"></a>
The number of conflicting aliases returned in the response.  
Type: Integer

## Errors
<a name="API_ListConflictingAliases_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** NoSuchDistribution **   
The specified distribution does not exist.  
HTTP Status Code: 404

## See Also
<a name="API_ListConflictingAliases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListConflictingAliases) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/ListConflictingAliases) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListConflictingAliases) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListConflictingAliases) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListConflictingAliases) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListConflictingAliases) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListConflictingAliases) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListConflictingAliases) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListConflictingAliases) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListConflictingAliases) 