---
id: "@specs/aws/batch/docs/API_DescribeServiceEnvironments"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS DescribeServiceEnvironments"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# DescribeServiceEnvironments

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_DescribeServiceEnvironments
> **target_lang:** meta — documentation tier. ALL sections preserved.



# DescribeServiceEnvironments
<a name="API_DescribeServiceEnvironments"></a>

Describes one or more of your service environments.

## Request Syntax
<a name="API_DescribeServiceEnvironments_RequestSyntax"></a>

```
POST /v1/describeserviceenvironments HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "serviceEnvironments": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DescribeServiceEnvironments_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeServiceEnvironments_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_DescribeServiceEnvironments_RequestSyntax) **   <a name="Batch-DescribeServiceEnvironments-request-maxResults"></a>
The maximum number of results returned by `DescribeServiceEnvironments` in paginated output. When this parameter is used, `DescribeServiceEnvironments` only returns `maxResults` results in a single page and a `nextToken` response element. The remaining results of the initial request can be seen by sending another `DescribeServiceEnvironments` request with the returned `nextToken` value. This value can be between 1 and 100. If this parameter isn't used, then `DescribeServiceEnvironments` returns up to 100 results and a `nextToken` value if applicable.  
Type: Integer  
Required: No

 ** [nextToken](#API_DescribeServiceEnvironments_RequestSyntax) **   <a name="Batch-DescribeServiceEnvironments-request-nextToken"></a>
The `nextToken` value returned from a previous paginated `DescribeServiceEnvironments` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is `null` when there are no more results to return.  
Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String  
Required: No

 ** [serviceEnvironments](#API_DescribeServiceEnvironments_RequestSyntax) **   <a name="Batch-DescribeServiceEnvironments-request-serviceEnvironments"></a>
An array of service environment names or ARN entries.  
Type: Array of strings  
Required: No

## Response Syntax
<a name="API_DescribeServiceEnvironments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "serviceEnvironments": [ 
      { 
         "capacityLimits": [ 
            { 
               "capacityUnit": "string",
               "maxCapacity": number
            }
         ],
         "serviceEnvironmentArn": "string",
         "serviceEnvironmentName": "string",
         "serviceEnvironmentType": "string",
         "state": "string",
         "status": "string",
         "tags": { 
            "string" : "string" 
         }
      }
   ]
}
```

## Response Elements
<a name="API_DescribeServiceEnvironments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_DescribeServiceEnvironments_ResponseSyntax) **   <a name="Batch-DescribeServiceEnvironments-response-nextToken"></a>
The `nextToken` value to include in a future `DescribeServiceEnvironments` request. When the results of a `DescribeServiceEnvironments` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.  
Type: String

 ** [serviceEnvironments](#API_DescribeServiceEnvironments_ResponseSyntax) **   <a name="Batch-DescribeServiceEnvironments-response-serviceEnvironments"></a>
The list of service environments that match the request.  
Type: Array of [ServiceEnvironmentDetail](API_ServiceEnvironmentDetail.md) objects

## Errors
<a name="API_DescribeServiceEnvironments_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_DescribeServiceEnvironments_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_DescribeServiceEnvironments_Example_1"></a>

This example describes the specified service environment.

#### Sample Request
<a name="API_DescribeServiceEnvironments_Example_1_Request"></a>

```
POST /v1/describeserviceenvironments HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
Content-Length: [content-length]
Authorization: [authorization-params]
X-Amz-Date: 20250801T142030Z
User-Agent: aws-cli/2.27.33 Python/3.13.4 Darwin/24.3.0

{
  "serviceEnvironments": ["SageMakerTrainingEnv"]
}
```

#### Sample Response
<a name="API_DescribeServiceEnvironments_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: [content-length]
Connection: keep-alive
Date: Mon, 01 Aug 2016 14:20:31 GMT
x-amzn-RequestId: [request-id]
X-Amzn-Trace-Id: [trace-id]
X-Cache: Miss from cloudfront
Via: 1.1 example2m8k7n9p6q3r4s5t8w1xexample.cloudfront.net (CloudFront)
X-Amz-Cf-Id: abc2def5ghi8jkl1mno4pqr7stu0vwx3yz6789abcdefghijklmnopqexample

{
  "serviceEnvironments": [
    {
      "serviceEnvironmentName": "SageMakerTrainingEnv",
      "serviceEnvironmentArn": "arn:aws:batch:us-east-1:123456789012:service-environment/SageMakerTrainingEnv",
      "serviceEnvironmentType": "SAGEMAKER_TRAINING",
      "state": "ENABLED",
      "status": "VALID",
      "capacityLimits": [
        {
          "maxCapacity": 50,
          "capacityUnit": "NUM_INSTANCES"
        }
      ],
      "tags": {}
    }
  ]
}
```

## See Also
<a name="API_DescribeServiceEnvironments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/DescribeServiceEnvironments) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/DescribeServiceEnvironments) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/DescribeServiceEnvironments) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/DescribeServiceEnvironments) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/DescribeServiceEnvironments) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/DescribeServiceEnvironments) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/DescribeServiceEnvironments) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/DescribeServiceEnvironments) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/DescribeServiceEnvironments) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/DescribeServiceEnvironments) 