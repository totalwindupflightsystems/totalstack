---
id: "@specs/aws/eks/docs/API_UntagResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS UntagResource"
status: active
depends_on:
  - "@specs/aws/eks/meta"
---

# UntagResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/eks/docs/API_UntagResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# UntagResource
<a name="API_UntagResource"></a>

Deletes specified tags from an Amazon EKS resource.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{resourceArn}}?tagKeys={{tagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_UntagResource_RequestSyntax) **   <a name="AmazonEKS-UntagResource-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource to delete tags from.  
Required: Yes

 ** [tagKeys](#API_UntagResource_RequestSyntax) **   <a name="AmazonEKS-UntagResource-request-uri-tagKeys"></a>
The keys of the tags to remove.  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

## Request Body
<a name="API_UntagResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_UntagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** BadRequestException **   
This exception is thrown if the request contains a semantic error. The precise meaning will depend on the API, and will be documented in the error message.    
 ** message **   
This exception is thrown if the request contains a semantic error. The precise meaning will depend on the API, and will be documented in the error message.
HTTP Status Code: 400

 ** NotFoundException **   
A service resource associated with the request could not be found. Clients should not retry such requests.    
 ** message **   
A service resource associated with the request could not be found. Clients should not retry such requests.
HTTP Status Code: 404

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eks-2017-11-01/UntagResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eks-2017-11-01/UntagResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/UntagResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eks-2017-11-01/UntagResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/UntagResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eks-2017-11-01/UntagResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eks-2017-11-01/UntagResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eks-2017-11-01/UntagResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/eks-2017-11-01/UntagResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/UntagResource) 