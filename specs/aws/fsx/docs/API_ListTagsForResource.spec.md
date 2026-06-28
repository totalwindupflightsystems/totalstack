---
id: "@specs/aws/fsx/docs/API_ListTagsForResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListTagsForResource"
status: active
depends_on:
  - "@specs/aws/fsx/meta"
---

# ListTagsForResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/fsx/docs/API_ListTagsForResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Lists tags for Amazon FSx resources.

When retrieving all tags, you can optionally specify the `MaxResults` parameter to limit the number of tags in a response. If more tags remain, Amazon FSx returns a `NextToken` value in the response. In this case, send a later request with the `NextToken` request parameter set to the value of `NextToken` from the last response.

This action is used in an iterative process to retrieve a list of your tags. `ListTagsForResource` is called first without a `NextToken`value. Then the action continues to be called with the `NextToken` parameter set to the value of the last `NextToken` value until a response has no `NextToken`.

When using this action, keep the following in mind:
+ The implementation might return fewer than `MaxResults` file system descriptions while still including a `NextToken` value.
+ The order of tags returned in the response of one `ListTagsForResource` call and the order of tags returned across the responses of a multi-call iteration is unspecified.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceARN": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListTagsForResource_RequestSyntax) **   <a name="FSx-ListTagsForResource-request-MaxResults"></a>
Maximum number of tags to return in the response (integer). This parameter value must be greater than 0. The number of items that Amazon FSx returns is the minimum of the `MaxResults` parameter specified in the request and the service's internal maximum number of items per page.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 2147483647.  
Required: No

 ** [NextToken](#API_ListTagsForResource_RequestSyntax) **   <a name="FSx-ListTagsForResource-request-NextToken"></a>
Opaque pagination token returned from a previous `ListTagsForResource` operation (String). If a token present, the action continues the list from where the returning call left off.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$`   
Required: No

 ** [ResourceARN](#API_ListTagsForResource_RequestSyntax) **   <a name="FSx-ListTagsForResource-request-ResourceARN"></a>
The ARN of the Amazon FSx resource that will have its tags listed.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 512.  
Pattern: `^arn:(?=[^:]+:fsx:[^:]+:\d{12}:)((|(?=[a-z0-9-.]{1,63})(?!\d{1,3}(\.\d{1,3}){3})(?![^:]*-{2})(?![^:]*-\.)(?![^:]*\.-)[a-z0-9].*(?<!-)):){4}(?!/).{0,1024}$`   
Required: Yes

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Tags": [ 
      { 
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTagsForResource_ResponseSyntax) **   <a name="FSx-ListTagsForResource-response-NextToken"></a>
This is present if there are more tags than returned in the response (String). You can use the `NextToken` value in the later request to fetch the tags.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$` 

 ** [Tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="FSx-ListTagsForResource-response-Tags"></a>
A list of tags on the resource.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.

## Errors
<a name="API_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequest **   
A generic error indicating a failure with a client request.    
 ** Message **   
A detailed error message.
HTTP Status Code: 400

 ** InternalServerError **   
A generic error indicating a server-side failure.    
 ** Message **   
A detailed error message.
HTTP Status Code: 500

 ** NotServiceResourceError **   
The resource specified for the tagging operation is not a resource type owned by Amazon FSx. Use the API of the relevant service to perform the operation.     
 ** Message **   
A detailed error message.  
 ** ResourceARN **   
The Amazon Resource Name (ARN) of the non-Amazon FSx resource.
HTTP Status Code: 400

 ** ResourceDoesNotSupportTagging **   
The resource specified does not support tagging.     
 ** Message **   
A detailed error message.  
 ** ResourceARN **   
The Amazon Resource Name (ARN) of the resource that doesn't support tagging.
HTTP Status Code: 400

 ** ResourceNotFound **   
The resource specified by the Amazon Resource Name (ARN) can't be found.    
 ** Message **   
A detailed error message.  
 ** ResourceARN **   
The resource ARN of the resource that can't be found.
HTTP Status Code: 400

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fsx-2018-03-01/ListTagsForResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fsx-2018-03-01/ListTagsForResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/ListTagsForResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fsx-2018-03-01/ListTagsForResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/ListTagsForResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fsx-2018-03-01/ListTagsForResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fsx-2018-03-01/ListTagsForResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fsx-2018-03-01/ListTagsForResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fsx-2018-03-01/ListTagsForResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/ListTagsForResource) 