---
id: "@specs/aws/batch/docs/API_TagResource"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS TagResource"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# TagResource

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_TagResource
> **target_lang:** meta — documentation tier. ALL sections preserved.



# TagResource
<a name="API_TagResource"></a>

Associates the specified tags to a resource with the specified `resourceArn`. If existing tags on a resource aren't specified in the request parameters, they aren't changed. When a resource is deleted, the tags that are associated with that resource are deleted as well. AWS Batch resources that support tags are compute environments, jobs, job definitions, job queues, and scheduling policies. ARNs for child jobs of array and multi-node parallel (MNP) jobs aren't supported.

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
POST /v1/tags/{{resourceArn}} HTTP/1.1
Content-type: application/json

{
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_TagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_TagResource_RequestSyntax) **   <a name="Batch-TagResource-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource that tags are added to. AWS Batch resources that support tags are compute environments, jobs, job definitions, job queues, and scheduling policies. ARNs for child jobs of array and multi-node parallel (MNP) jobs aren't supported.  
Required: Yes

## Request Body
<a name="API_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tags](#API_TagResource_RequestSyntax) **   <a name="Batch-TagResource-request-tags"></a>
The tags that you apply to the resource to help you categorize and organize your resources. Each tag consists of a key and an optional value. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in * AWS General Reference*.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Value Length Constraints: Maximum length of 256.  
Required: Yes

## Response Syntax
<a name="API_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_TagResource_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_TagResource_Example_1"></a>

This example adds a tag to the job definition with an ARN of "*arn:aws:batch:us-east-1:123456789012:job-definition/sleep30:1*".

#### Sample Request
<a name="API_TagResource_Example_1_Request"></a>

```
POST /v1/tags/arn%3Aaws%3Abatch%3Aus-east-1%3A123456789012%3Ajob-definition%2Fsleep30%3A1 HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
X-Amz-Date: 20200604T172359Z
X-Amz-Security-Token: [security-token]
Authorization: [authorization-params]
Content-Length: [length-of-JSON]

{
  "tags": {
    "Stage": "alpha"
  }
}
```

#### Sample Response
<a name="API_TagResource_Example_1_Response"></a>

```
HTTP/1.1 204 No Content
Date: Thu, 05 Jun 2020 17:24:04 GMT
Content-Type: application/json
Content-Length: 0
x-amzn-RequestId: [request-id]
Access-Control-Allow-Origin: *
x-amz-apigw-id: [apigw-id]
X-Amzn-Trace-Id: [trace-id]
Connection: keep-alive
```

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/TagResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/TagResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/TagResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/TagResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/TagResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/TagResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/TagResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/TagResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/TagResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/TagResource) 