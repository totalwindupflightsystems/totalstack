---
id: "@specs/aws/cloudfront/docs/API_ListTagsForResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTagsForResource"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# ListTagsForResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_ListTagsForResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTagsForResource
<a name="API_ListTagsForResource"></a>

List tags for a CloudFront resource. For more information, see [Tagging a distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/tagging.html) in the *Amazon CloudFront Developer Guide*.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
GET /2020-05-31/tagging?Resource={{Resource}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Resource](#API_ListTagsForResource_RequestSyntax) **   <a name="cloudfront-ListTagsForResource-request-uri-Resource"></a>
An ARN of a CloudFront resource.  
Pattern: `arn:aws(-cn)?:cloudfront::[0-9]+:.*`   
Required: Yes

## Request Body
<a name="API_ListTagsForResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<Tags>
   <Items>
      <Tag>
         <Key>string</Key>
         <Value>string</Value>
      </Tag>
   </Items>
</Tags>
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [Tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="cloudfront-ListTagsForResource-response-Tags"></a>
Root level tag for the Tags parameters.  
Required: Yes

 ** [Items](#API_ListTagsForResource_ResponseSyntax) **   <a name="cloudfront-ListTagsForResource-response-Items"></a>
A complex type that contains `Tag` elements.  
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** InvalidArgument **   
An argument is invalid.  
HTTP Status Code: 400

 ** InvalidTagging **   
The tagging specified is not valid.  
HTTP Status Code: 400

 ** NoSuchResource **   
A resource that was specified is not valid.  
HTTP Status Code: 404

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListTagsForResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/ListTagsForResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListTagsForResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListTagsForResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListTagsForResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListTagsForResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListTagsForResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListTagsForResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListTagsForResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListTagsForResource) 