---
id: "@specs/aws/batch/docs/API_ListSchedulingPolicies"
version: 1.0.0
target_lang: meta
owned-by: aws-docs
source: "AWS ListSchedulingPolicies"
status: active
depends_on:
  - "@specs/aws/batch/meta"
---

# ListSchedulingPolicies

> **source:** AWS Documentation
> **spec:id:** @specs/aws/batch/docs/API_ListSchedulingPolicies
> **target_lang:** meta — documentation tier. ALL sections preserved.



# ListSchedulingPolicies
<a name="API_ListSchedulingPolicies"></a>

Returns a list of AWS Batch scheduling policies.

## Request Syntax
<a name="API_ListSchedulingPolicies_RequestSyntax"></a>

```
POST /v1/listschedulingpolicies HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListSchedulingPolicies_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListSchedulingPolicies_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListSchedulingPolicies_RequestSyntax) **   <a name="Batch-ListSchedulingPolicies-request-maxResults"></a>
The maximum number of results that's returned by `ListSchedulingPolicies` in paginated output. When this parameter is used, `ListSchedulingPolicies` only returns `maxResults` results in a single page and a `nextToken` response element. You can see the remaining results of the initial request by sending another `ListSchedulingPolicies` request with the returned `nextToken` value. This value can be between 1 and 100. If this parameter isn't used, `ListSchedulingPolicies` returns up to 100 results and a `nextToken` value if applicable.  
Type: Integer  
Required: No

 ** [nextToken](#API_ListSchedulingPolicies_RequestSyntax) **   <a name="Batch-ListSchedulingPolicies-request-nextToken"></a>
The `nextToken` value that's returned from a previous paginated `ListSchedulingPolicies` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value. This value is `null` when there are no more results to return.  
Treat this token as an opaque identifier that's only used to retrieve the next items in a list and not for other programmatic purposes.
Type: String  
Required: No

## Response Syntax
<a name="API_ListSchedulingPolicies_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "schedulingPolicies": [ 
      { 
         "arn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSchedulingPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListSchedulingPolicies_ResponseSyntax) **   <a name="Batch-ListSchedulingPolicies-response-nextToken"></a>
The `nextToken` value to include in a future `ListSchedulingPolicies` request. When the results of a `ListSchedulingPolicies` request exceed `maxResults`, this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.  
Type: String

 ** [schedulingPolicies](#API_ListSchedulingPolicies_ResponseSyntax) **   <a name="Batch-ListSchedulingPolicies-response-schedulingPolicies"></a>
A list of scheduling policies that match the request.  
Type: Array of [SchedulingPolicyListingDetail](API_SchedulingPolicyListingDetail.md) objects

## Errors
<a name="API_ListSchedulingPolicies_Errors"></a>

 ** ClientException **   
These errors are usually caused by a client action. One example cause is using an action or resource on behalf of a user that doesn't have permissions to use the action or resource. Another cause is specifying an identifier that's not valid.  
HTTP Status Code: 400

 ** ServerException **   
These errors are usually caused by a server issue.  
HTTP Status Code: 500

## Examples
<a name="API_ListSchedulingPolicies_Examples"></a>

In the following example or examples, the Authorization header contents (` [authorization-params] `) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the * AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_ListSchedulingPolicies_Example_1"></a>

This example lists the scheduling policies.

#### Sample Request
<a name="API_ListSchedulingPolicies_Example_1_Request"></a>

```
POST /v1/listschedulingpolicies HTTP/1.1
Host: batch.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/1.20.21 Python/3.6.9 Linux/4.4.0-19041-Microsoft botocore/1.21.21
X-Amz-Date: 20210929T001942Z
X-Amz-Security-Token: [security-token]
Authorization: [authorization-params]
Content-Length: 0
```

#### Sample Response
<a name="API_ListSchedulingPolicies_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Wed, 29 Sep 2021 00:19:43 GMT
Content-Type: application/json
Content-Length: [content-length]
x-amzn-RequestId: [request-id]
Access-Control-Allow-Origin: *
x-amz-apigw-id: [apigw-id]
Access-Control-Expose-Headers: X-amzn-errortype,X-amzn-requestid,X-amzn-errormessage,X-amzn-trace-id,X-amz-apigw-id,date
X-Amzn-Trace-Id: [trace-id]
Connection: keep-alive

{
    "schedulingPolicies": [{
        "arn": "arn:aws:batch:us-east-1:123456789012:scheduling-policy/ExampleFairSharePolicy"
    }, {
        "arn": "arn:aws:batch:us-east-1:123456789012:scheduling-policy/ExampleFairSharePolicy2"
    }]
}
```

## See Also
<a name="API_ListSchedulingPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/batch-2016-08-10/ListSchedulingPolicies) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/batch-2016-08-10/ListSchedulingPolicies) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ListSchedulingPolicies) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/batch-2016-08-10/ListSchedulingPolicies) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ListSchedulingPolicies) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/batch-2016-08-10/ListSchedulingPolicies) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/batch-2016-08-10/ListSchedulingPolicies) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/batch-2016-08-10/ListSchedulingPolicies) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/batch-2016-08-10/ListSchedulingPolicies) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ListSchedulingPolicies) 