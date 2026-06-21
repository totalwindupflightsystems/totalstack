---
id: "@specs/aws/cloudfront/docs/API_DeleteStreamingDistribution"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DeleteStreamingDistribution"
status: active
depends_on:
  - "@specs/aws/cloudfront/meta"
---

# DeleteStreamingDistribution

> **source:** AWS Documentation
> **spec:id:** @specs/aws/cloudfront/docs/API_DeleteStreamingDistribution
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DeleteStreamingDistribution
<a name="API_DeleteStreamingDistribution"></a>

Delete a streaming distribution. To delete an RTMP distribution using the CloudFront API, perform the following steps.

 **To delete an RTMP distribution using the CloudFront API**:

1. Disable the RTMP distribution.

1. Submit a `GET Streaming Distribution Config` request to get the current configuration and the `Etag` header for the distribution. 

1. Update the XML document that was returned in the response to your `GET Streaming Distribution Config` request to change the value of `Enabled` to `false`.

1. Submit a `PUT Streaming Distribution Config` request to update the configuration for your distribution. In the request body, include the XML document that you updated in Step 3. Then set the value of the HTTP `If-Match` header to the value of the `ETag` header that CloudFront returned when you submitted the `GET Streaming Distribution Config` request in Step 2.

1. Review the response to the `PUT Streaming Distribution Config` request to confirm that the distribution was successfully disabled.

1. Submit a `GET Streaming Distribution Config` request to confirm that your changes have propagated. When propagation is complete, the value of `Status` is `Deployed`.

1. Submit a `DELETE Streaming Distribution` request. Set the value of the HTTP `If-Match` header to the value of the `ETag` header that CloudFront returned when you submitted the `GET Streaming Distribution Config` request in Step 2.

1. Review the response to your `DELETE Streaming Distribution` request to confirm that the distribution was successfully deleted.

For information about deleting a distribution using the CloudFront console, see [Deleting a Distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowToDeleteDistribution.html) in the *Amazon CloudFront Developer Guide*.

## Request Syntax
<a name="API_DeleteStreamingDistribution_RequestSyntax"></a>

```
DELETE /2020-05-31/streaming-distribution/{{Id}} HTTP/1.1
If-Match: {{IfMatch}}
```

## URI Request Parameters
<a name="API_DeleteStreamingDistribution_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Id](#API_DeleteStreamingDistribution_RequestSyntax) **   <a name="cloudfront-DeleteStreamingDistribution-request-uri-Id"></a>
The distribution ID.  
Required: Yes

 ** [If-Match](#API_DeleteStreamingDistribution_RequestSyntax) **   <a name="cloudfront-DeleteStreamingDistribution-request-IfMatch"></a>
The value of the `ETag` header that you received when you disabled the streaming distribution. For example: `E2QWRUHAPOMQZL`.

## Request Body
<a name="API_DeleteStreamingDistribution_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteStreamingDistribution_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteStreamingDistribution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteStreamingDistribution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **   
Access denied.  
HTTP Status Code: 403

 ** InvalidIfMatchVersion **   
The `If-Match` version is missing or not valid.  
HTTP Status Code: 400

 ** NoSuchStreamingDistribution **   
The specified streaming distribution does not exist.  
HTTP Status Code: 404

 ** PreconditionFailed **   
The precondition in one or more of the request fields evaluated to `false`.  
HTTP Status Code: 412

 ** StreamingDistributionNotDisabled **   
The specified CloudFront distribution is not disabled. You must disable the distribution before you can delete it.  
HTTP Status Code: 409

## See Also
<a name="API_DeleteStreamingDistribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteStreamingDistribution) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/DeleteStreamingDistribution) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteStreamingDistribution) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteStreamingDistribution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteStreamingDistribution) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteStreamingDistribution) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteStreamingDistribution) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteStreamingDistribution) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteStreamingDistribution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteStreamingDistribution) 